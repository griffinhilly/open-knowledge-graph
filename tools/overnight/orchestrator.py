#!/usr/bin/env python3
"""
Overnight orchestrator for Open Knowledge Graph topic generation.

Invokes Claude Code CLI (claude --print) per course, captures JSON output,
generates .md topic files, validates, and commits. Tracks progress for resume.

Usage:
    python tools/overnight/orchestrator.py              # Run full queue
    python tools/overnight/orchestrator.py --resume     # Resume from last checkpoint
    python tools/overnight/orchestrator.py --dry-run    # Show queue without executing
    python tools/overnight/orchestrator.py --start-from physics--classical-mechanics
    python tools/overnight/orchestrator.py --model sonnet  # Use a specific model
"""

import json
import re
import subprocess
import sys
import os
import time
import logging
from pathlib import Path
from datetime import datetime

# Add overnight dir to path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "tools" / "overnight"))

from subjects import MATH_COURSES, DOMAIN_SPECS, build_queue
from generator import process_output, apply_crosslink_edits

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

OVERNIGHT_DIR = PROJECT_ROOT / "tools" / "overnight"
OUTPUT_DIR = OVERNIGHT_DIR / "output"
PROGRESS_FILE = OVERNIGHT_DIR / "progress.json"
LOG_FILE = OVERNIGHT_DIR / "run.log"
DOMAINS_DIR = PROJECT_ROOT / "domains"

CLAUDE_CMD = ["claude", "--print"]
CLAUDE_BASE_FLAGS = ["--dangerously-skip-permissions"]
CLAUDE_MODEL = None  # Set via --model flag

AGENT_TIMEOUT = 1800  # 30 min per invocation

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger("overnight")

# ---------------------------------------------------------------------------
# Progress tracking
# ---------------------------------------------------------------------------

def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {"completed": [], "failed": [], "started_at": None}


def save_progress(progress: dict):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


# ---------------------------------------------------------------------------
# Existing topic ID collection
# ---------------------------------------------------------------------------

def get_existing_topic_ids(filter_domains: list[str] | None = None) -> dict[str, list[str]]:
    """Scan domains/ for all existing topic IDs, grouped by domain."""
    result = {}
    if not DOMAINS_DIR.exists():
        return result
    for domain_dir in DOMAINS_DIR.iterdir():
        if not domain_dir.is_dir():
            continue
        domain_name = domain_dir.name
        if filter_domains and domain_name not in filter_domains:
            continue
        ids = []
        for course_dir in domain_dir.iterdir():
            if not course_dir.is_dir():
                continue
            for md_file in course_dir.glob("*.md"):
                ids.append(md_file.stem)
        if ids:
            result[domain_name] = sorted(ids)
    return result


def get_topic_ids_with_courses(domain: str) -> list[dict]:
    """Get topic IDs with their course for cross-domain review."""
    domain_dir = DOMAINS_DIR / domain
    if not domain_dir.exists():
        return []
    topics = []
    for course_dir in domain_dir.iterdir():
        if not course_dir.is_dir():
            continue
        for md_file in course_dir.glob("*.md"):
            topics.append({"id": md_file.stem, "course": course_dir.name})
    return sorted(topics, key=lambda t: (t["course"], t["id"]))


def format_existing_ids(ids_by_domain: dict[str, list[str]]) -> str:
    if not ids_by_domain:
        return "No existing topics yet."
    parts = []
    for domain, ids in ids_by_domain.items():
        parts.append(f"\n### {domain} ({len(ids)} topics)")
        for i in range(0, len(ids), 5):
            parts.append(", ".join(ids[i:i+5]))
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Prompt templates
# ---------------------------------------------------------------------------

SCHEMA_EXCERPT = """
## Topic Schema (condensed)

Required fields:
- id: globally unique, lowercase-hyphenated, matches filename
- title: human-readable name
- domain: domain name (e.g., "mathematics", "physics")
- course: course within domain (e.g., "algebra-1", "classical-mechanics")
- prerequisites: list of {id, type} where type is "hard" or "soft"
  - hard = cannot learn without prereq; soft = helpful but not required
  - Root topics use empty list []

Optional: builds-toward (list of IDs), tags, stage, status (always "draft"), aliases

Body sections: Core Idea (required, 2-5 sentences), How It's Best Learned, Common Misconceptions
""".strip()

EXAMPLE_TOPIC_JSON = """{
  "id": "quadratic-formula",
  "title": "The Quadratic Formula",
  "domain": "mathematics",
  "course": "algebra-1",
  "prerequisites": [
    {"id": "solving-quadratics-by-factoring", "type": "hard"},
    {"id": "square-roots-intro", "type": "hard"}
  ],
  "builds_toward": ["discriminant", "complex-numbers"],
  "tags": ["quadratics", "solving", "roots"],
  "stage": "abstract-reasoning",
  "status": "draft",
  "core_idea": "The quadratic formula solves any quadratic equation ax² + bx + c = 0: x = (−b ± sqrt(b² − 4ac)) / (2a). It works for every quadratic — factorable or not.",
  "how_best_learned": "First use it on equations that can also be factored to verify answers. Then apply to non-factorable quadratics.",
  "common_misconceptions": "- Forgetting the 2a denominator.\\n- Sign errors when b is negative."
}"""


def build_math_prompt(subject: dict, existing_ids: dict) -> str:
    return f"""You are a curriculum designer for the Open Knowledge Graph project.

Generate topics for "{subject['course_title']}" (mathematics domain).
Course ID: {subject['course_id']} | Stage: {subject['stage']} | Target: ~{subject['target_topics']} topics

{SCHEMA_EXCERPT}

Example topic: {EXAMPLE_TOPIC_JSON}

Output ONLY a JSON object: {{"domain": "mathematics", "topics": [...]}}
Each topic needs: id, title, domain, course, prerequisites, builds_toward, tags, stage, status, core_idea.
Include how_best_learned and common_misconceptions for at least half.

Subject guidance: {subject['guidance']}

Existing topic IDs (reference as prerequisites where appropriate):
{format_existing_ids(existing_ids)}

Rules: unique IDs, no cycles, substantive core_ideas (2-5 real sentences), standard textbook terminology.
Output ONLY the JSON. Nothing else."""


def build_domain_course_prompt(subject: dict, existing_ids: dict) -> str:
    return f"""You are a curriculum designer for the Open Knowledge Graph project.

Generate topics for the course "{subject['course_title']}" in the {subject['domain_title']} domain.
Domain: {subject['domain']} | Course: {subject['course_id']} | Stage: {subject['stage']}
Target: ~{subject['target_topics']} topics

{SCHEMA_EXCERPT}

Example topic: {EXAMPLE_TOPIC_JSON}

Output ONLY a JSON object: {{"domain": "{subject['domain']}", "topics": [...]}}
Each topic needs: id, title, domain (= "{subject['domain']}"), course (= "{subject['course_id']}"), prerequisites, builds_toward, tags, stage, status, core_idea.
Include how_best_learned and common_misconceptions for at least half.

Course guidance: {subject['guidance']}

Existing topic IDs from this domain and prerequisite domains (reference as prerequisites):
{format_existing_ids(existing_ids)}

Rules:
- IDs must be globally unique — do NOT reuse any ID listed above
- No cycles in prerequisites
- Substantive core_ideas (2-5 real sentences, not placeholders)
- Cross-reference existing topics as prerequisites where appropriate
- Use standard academic terminology
Output ONLY the JSON. Nothing else."""


def build_crosslink_prompt(subject: dict, domain_topics: list[dict], existing_ids: dict) -> str:
    topics_list = "\n".join(
        f"  {t['id']} (course: {t['course']})" for t in domain_topics
    )
    return f"""You are reviewing cross-domain prerequisite connections in the Open Knowledge Graph.

Domain under review: {subject['domain_title']} ({subject['domain']})
Prerequisite domains: {', '.join(subject['prereq_domains'])}

Topics in {subject['domain_title']}:
{topics_list}

Available topics from prerequisite domains:
{format_existing_ids(existing_ids)}

Your task: Identify MISSING cross-domain prerequisites. For each, output an edit.

Output ONLY a JSON array of edits:
[
  {{
    "topic_id": "topic-in-this-domain",
    "domain": "{subject['domain']}",
    "course": "course-id",
    "add_prerequisites": [{{"id": "prereq-from-other-domain", "type": "soft"}}],
    "add_builds_toward": ["optional-forward-link"]
  }}
]

Rules:
- Only add GENUINE prerequisites — not vague associations
- Prefer "soft" type for cross-domain links unless truly required
- Focus on the most important 20-40 connections, not exhaustive linking
- Output ONLY the JSON array. Nothing else."""


# ---------------------------------------------------------------------------
# Agent execution
# ---------------------------------------------------------------------------

def run_claude(prompt: str) -> str | None:
    """Run claude --print with the given prompt. Returns stdout or None on failure."""
    flags = list(CLAUDE_BASE_FLAGS)
    if CLAUDE_MODEL:
        flags += ["--model", CLAUDE_MODEL]
    cmd = CLAUDE_CMD + flags
    log.info(f"Running: {' '.join(cmd)} (prompt: {len(prompt)} chars)")

    env = os.environ.copy()
    env.pop("CLAUDECODE", None)
    env["PYTHONIOENCODING"] = "utf-8"

    try:
        result = subprocess.run(
            cmd,
            input=prompt,
            capture_output=True,
            timeout=AGENT_TIMEOUT,
            cwd=str(PROJECT_ROOT),
            env=env,
            encoding="utf-8",
            errors="replace",
        )

        if result.returncode != 0:
            log.error(f"Claude exited with code {result.returncode}")
            if result.stderr:
                log.error(f"stderr: {result.stderr[:2000]}")
            combined = (result.stderr or "") + (result.stdout or "")
            if any(phrase in combined.lower() for phrase in
                   ["rate limit", "quota", "too many requests", "usage limit"]):
                log.error("RATE LIMIT DETECTED")
                return "RATE_LIMIT"
            return None

        return result.stdout

    except subprocess.TimeoutExpired:
        log.error(f"Claude timed out after {AGENT_TIMEOUT}s")
        return None
    except FileNotFoundError:
        log.error("'claude' command not found")
        sys.exit(1)


def extract_json(text: str) -> dict | list | None:
    """Extract JSON from agent output."""
    if not text:
        return None

    # Try JSON in code fence
    match = re.search(r'```(?:json)?\s*\n(.*?)\n```', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError as e:
            log.warning(f"JSON in code fence failed: {e}")

    # Try whole text
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        pass

    # Find outermost { } or [ ]
    for open_c, close_c in [('{', '}'), ('[', ']')]:
        start = text.find(open_c)
        end = text.rfind(close_c)
        if start != -1 and end != -1 and end > start:
            try:
                return json.loads(text[start:end + 1])
            except json.JSONDecodeError:
                pass

    log.error("Could not extract valid JSON from agent output")
    return None


# ---------------------------------------------------------------------------
# Validation & Git
# ---------------------------------------------------------------------------

def run_validation() -> tuple[bool, str]:
    try:
        result = subprocess.run(
            [sys.executable, str(PROJECT_ROOT / "tools" / "validate.py")],
            capture_output=True, text=True, timeout=120, cwd=str(PROJECT_ROOT),
        )
        output = result.stdout + result.stderr
        has_errors = "ERROR" in output.upper() and "0 errors" not in output.lower()
        return (not has_errors, output)
    except Exception as e:
        return (False, f"Validation failed: {e}")


def git_commit(subject_id: str, description: str):
    try:
        subprocess.run(["git", "add", "domains/"], cwd=str(PROJECT_ROOT),
                        capture_output=True, timeout=30)
        msg = (f"Add {subject_id}: {description}\n\n"
               f"Generated by overnight orchestrator.\n\n"
               f"Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")
        subprocess.run(["git", "commit", "-m", msg], cwd=str(PROJECT_ROOT),
                        capture_output=True, timeout=30)
        log.info(f"Committed {subject_id}")
    except Exception as e:
        log.warning(f"Git commit failed for {subject_id}: {e}")


# ---------------------------------------------------------------------------
# Domain setup
# ---------------------------------------------------------------------------

def setup_domain(subject: dict):
    """Create _domain.yml and course directories for a new domain."""
    import yaml
    domain_dir = DOMAINS_DIR / subject["domain"]
    domain_dir.mkdir(parents=True, exist_ok=True)

    config = {
        "domain": subject["domain"],
        "title": subject["domain_title"],
        "description": subject["domain_description"],
        "courses": subject["courses"],
    }

    yml_path = domain_dir / "_domain.yml"
    with open(yml_path, "w", encoding="utf-8") as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    for course in subject["courses"]:
        (domain_dir / course["id"]).mkdir(exist_ok=True)

    log.info(f"Created domain structure: {subject['domain']} ({len(subject['courses'])} courses)")


def ensure_math_k3():
    """Ensure K-3 course directories exist."""
    for cid in ["kindergarten", "1st-grade", "2nd-grade", "3rd-grade"]:
        (DOMAINS_DIR / "mathematics" / cid).mkdir(exist_ok=True)


# ---------------------------------------------------------------------------
# Subject processors
# ---------------------------------------------------------------------------

def process_math_course(subject: dict) -> bool | str:
    relevant = list(subject.get("prereq_domains", [])) + ["mathematics"]
    existing_ids = get_existing_topic_ids(relevant)
    prompt = build_math_prompt(subject, existing_ids)
    return _run_build_agent(subject["id"], prompt, "mathematics")


def process_domain_course(subject: dict) -> bool | str:
    relevant = list(subject.get("prereq_domains", [])) + [subject["domain"]]
    existing_ids = get_existing_topic_ids(relevant)
    prompt = build_domain_course_prompt(subject, existing_ids)
    return _run_build_agent(subject["id"], prompt, subject["domain"])


def process_crosslinks(subject: dict) -> bool | str:
    domain_topics = get_topic_ids_with_courses(subject["domain"])
    if not domain_topics:
        log.warning(f"No topics found for {subject['domain']} — skipping crosslinks")
        return True

    existing_ids = get_existing_topic_ids(subject["prereq_domains"])
    prompt = build_crosslink_prompt(subject, domain_topics, existing_ids)

    output = run_claude(prompt)
    if output == "RATE_LIMIT":
        return "RATE_LIMIT"
    if not output:
        return False

    # Save raw
    raw_path = OUTPUT_DIR / f"{subject['id']}.raw.txt"
    raw_path.write_text(output, encoding="utf-8")

    data = extract_json(output)
    if not data:
        return False

    json_path = OUTPUT_DIR / f"{subject['id']}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    try:
        modified = apply_crosslink_edits(json_path)
        log.info(f"Applied {modified} cross-domain edits for {subject['domain']}")
    except Exception as e:
        log.error(f"Failed to apply crosslink edits: {e}")
        return False

    git_commit(subject["id"], f"{modified} cross-domain links")
    return True


def _run_build_agent(subject_id: str, prompt: str, domain: str) -> bool | str:
    """Common build flow: run agent, extract JSON, generate files, validate, commit."""
    output = run_claude(prompt)
    if output == "RATE_LIMIT":
        return "RATE_LIMIT"
    if not output:
        log.error(f"No output for {subject_id}")
        return False

    # Save raw
    raw_path = OUTPUT_DIR / f"{subject_id}.raw.txt"
    raw_path.write_text(output, encoding="utf-8")

    # Extract JSON
    data = extract_json(output)
    if not data:
        log.error(f"Failed to extract JSON for {subject_id}")
        return False

    # Save parsed JSON
    json_path = OUTPUT_DIR / f"{subject_id}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # Generate .md files
    try:
        created = process_output(json_path, fallback_domain=domain)
        log.info(f"Generated {len(created)} files for {subject_id}")
    except Exception as e:
        log.error(f"File generation failed for {subject_id}: {e}")
        return False

    # Validate
    success, val_output = run_validation()
    if not success:
        log.warning(f"Validation issues for {subject_id} (continuing anyway)")
    else:
        log.info(f"Validation passed for {subject_id}")

    git_commit(subject_id, f"{len(created)} topic files")
    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Overnight OKG generator")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")
    parser.add_argument("--dry-run", action="store_true", help="Show queue only")
    parser.add_argument("--start-from", type=str, help="Skip to a subject ID")
    parser.add_argument("--only", type=str, help="Run only one subject ID")
    parser.add_argument("--model", type=str, help="Claude model (e.g. sonnet, opus)")
    parser.add_argument("--retry-failed", action="store_true",
                        help="Re-attempt previously failed subjects")
    args = parser.parse_args()

    global CLAUDE_MODEL
    if args.model:
        CLAUDE_MODEL = args.model

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    progress = load_progress() if args.resume or args.retry_failed else {
        "completed": [], "failed": [], "started_at": datetime.now().isoformat()
    }
    if not progress.get("started_at"):
        progress["started_at"] = datetime.now().isoformat()

    # If retrying failed, move them back to the queue
    if args.retry_failed and progress.get("failed"):
        log.info(f"Retrying {len(progress['failed'])} failed subjects")
        progress["failed"] = []
        save_progress(progress)

    ensure_math_k3()

    # Build queue
    queue = build_queue()

    if args.only:
        queue = [s for s in queue if s["id"] == args.only]
        if not queue:
            log.error(f"Subject '{args.only}' not found")
            sys.exit(1)
    elif args.start_from:
        idx = next((i for i, s in enumerate(queue) if s["id"] == args.start_from), None)
        if idx is None:
            log.error(f"Subject '{args.start_from}' not found")
            sys.exit(1)
        queue = queue[idx:]

    remaining = [s for s in queue if s["id"] not in progress["completed"]]

    log.info(f"Queue: {len(remaining)} remaining / {len(queue)} total")

    if args.dry_run:
        for i, s in enumerate(remaining, 1):
            label = s.get("course_title", s.get("domain_title", s.get("domain", "")))
            log.info(f"  {i}. [{s['type']}] {s['id']} — {label}")
        return

    # Execute
    for i, subject in enumerate(remaining, 1):
        stype = subject["type"]
        log.info(f"\n[{i}/{len(remaining)}] {subject['id']} ({stype})")

        if stype == "domain-setup":
            setup_domain(subject)
            progress["completed"].append(subject["id"])
            save_progress(progress)
            continue

        log.info("=" * 60)
        log.info(f"STARTING: {subject['id']}")
        log.info("=" * 60)

        if stype == "math-course":
            result = process_math_course(subject)
        elif stype == "domain-course":
            result = process_domain_course(subject)
        elif stype == "cross-domain-review":
            result = process_crosslinks(subject)
        else:
            log.error(f"Unknown type: {stype}")
            result = False

        if result == "RATE_LIMIT":
            log.error("Rate limit hit. Saving progress.")
            log.error("Resume: python tools/overnight/orchestrator.py --resume")
            save_progress(progress)
            sys.exit(2)
        elif result is True:
            progress["completed"].append(subject["id"])
            done = len(progress["completed"])
            log.info(f"COMPLETED: {subject['id']} ({done}/{len(queue)} total)")
        else:
            progress["failed"].append(subject["id"])
            log.warning(f"FAILED: {subject['id']}")

        save_progress(progress)

        if i < len(remaining):
            time.sleep(3)

    # Summary
    log.info(f"\n{'='*60}")
    log.info("OVERNIGHT RUN COMPLETE")
    log.info(f"  Completed: {len(progress['completed'])}")
    log.info(f"  Failed: {len(progress['failed'])}")
    if progress["failed"]:
        log.info(f"  Failed: {progress['failed']}")
    log.info(f"{'='*60}")


if __name__ == "__main__":
    main()
