#!/bin/bash
# ============================================================
# OKG Autonomous Build — Agent Swarm Domain Expansion
# ============================================================
# Runs claude -p in non-interactive mode to autonomously build
# out all 19 knowledge graph domains, then enhances detail.
#
# Scheduled to run overnight. Continues on failure (no set -e).
# Each phase/course gets its own claude invocation with a budget cap.
# ============================================================

set -uo pipefail

PROJECT_DIR="/c/Users/griff/open-knowledge-graph"
LOG_DIR="$PROJECT_DIR/output/autonomous-logs"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG="$LOG_DIR/run_$TIMESTAMP.log"
SUMMARY="$LOG_DIR/summary_$TIMESTAMP.txt"
CLAUDE="/c/Users/griff/.local/bin/claude"

# No per-invocation budget caps — running under Max plan limits
MODEL="sonnet"

# 18 new domains in tier order (math = #1, already done)
# Tier 1: Heavy math overlap
# Tier 2: Well-structured disciplines
# Tier 3: Structured but branching
# Tier 4: Humanities
# Tier 5: Arts & expression
DOMAINS=(
  # Tier 1
  physics
  computer-science
  formal-sciences
  # Tier 2
  chemistry
  biology
  earth-and-space-sciences
  economics
  # Tier 3
  psychology
  engineering
  health-sciences
  # Tier 4
  history
  philosophy
  social-sciences
  # Tier 5
  language
  literature
  music
  arts
  practical-life-skills
)

# Human-readable names for prompts
declare -A DOMAIN_TITLES=(
  [physics]="Physics"
  [computer-science]="Computer Science & Information"
  [formal-sciences]="Formal Sciences & Logic"
  [chemistry]="Chemistry"
  [biology]="Biology"
  [earth-and-space-sciences]="Earth & Space Sciences"
  [economics]="Economics & Political Economy"
  [psychology]="Psychology & Cognitive Science"
  [engineering]="Engineering & Technology"
  [health-sciences]="Health & Human Development"
  [history]="History & Civilization"
  [philosophy]="Philosophy & Ethics"
  [social-sciences]="Social Sciences"
  [language]="Language & Communication"
  [literature]="Literature"
  [music]="Music"
  [arts]="Arts & Aesthetics"
  [practical-life-skills]="Practical Life Skills"
)

# Domain descriptions for planning prompts
declare -A DOMAIN_HINTS=(
  [physics]="Mechanics, E&M, Thermodynamics, Waves, Modern Physics. Heavily references math prerequisites. Most sequential science."
  [computer-science]="Discrete math, logic, algorithms, data structures, systems, networks, AI/ML. Strong math ties."
  [formal-sciences]="Propositional logic, predicate logic, set theory, proof methods, computability. Small but foundational. Overlaps with math methods-of-proof."
  [chemistry]="Atomic structure, bonding, reactions, stoichiometry, thermochem, organic. Very sequential. Builds on physics."
  [biology]="Cell biology, genetics, ecology, evolution, anatomy, physiology. Builds on chemistry."
  [earth-and-space-sciences]="Geology, astronomy, atmospheric science, oceanography, climate. Builds on physics + chemistry."
  [economics]="Microeconomics, macroeconomics, econometrics, game theory, development. Math-heavy, clean prereq chains."
  [psychology]="Research methods, perception, cognition, developmental, social, clinical. Builds on biology + statistics."
  [engineering]="Statics, dynamics, circuits, materials, thermodynamics, controls. Builds heavily on physics + math."
  [health-sciences]="Anatomy, physiology, nutrition, epidemiology, public health, child development. Builds on biology."
  [history]="Ancient, medieval, early modern, modern, world history. Chronological structure = natural ordering."
  [philosophy]="Logic, epistemology, metaphysics, ethics, political philosophy, aesthetics. Logic prereqs from formal-sciences."
  [social-sciences]="Sociology, anthropology, political science, human geography. Broader prereq chains."
  [language]="Grammar, rhetoric, composition, linguistics, phonetics, syntax, semantics."
  [literature]="Literary analysis, genres, periods, critical theory, world literature. Prereqs on language."
  [music]="Music theory, harmony, counterpoint, composition, orchestration. Actually quite sequential."
  [arts]="Visual arts principles, design, art history, color theory, sculpture. More parallel than sequential."
  [practical-life-skills]="Financial literacy, cooking, first aid, time management, basic repairs. Loosest prereq structure."
)

cd "$PROJECT_DIR"
mkdir -p "$LOG_DIR"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG"; }

run_claude() {
  local description=$1
  # Prompt comes from stdin (heredoc)

  log "START: $description"
  local start_time=$(date +%s)

  "$CLAUDE" -p \
    --dangerously-skip-permissions \
    --model "$MODEL" \
    2>&1 >> "$LOG"

  local exit_code=$?
  local end_time=$(date +%s)
  local duration=$(( end_time - start_time ))

  if [ $exit_code -eq 0 ]; then
    log "DONE: $description (${duration}s)"
  else
    log "FAIL: $description (exit $exit_code, ${duration}s)"
  fi

  return $exit_code
}

count_topics() {
  local dir=$1
  find "$dir" -name '*.md' ! -name '_*' ! -name 'COURSES.md' ! -name 'README.md' 2>/dev/null | wc -l
}

# ============================================================
echo "========================================================" >> "$LOG"
log "OKG AUTONOMOUS BUILD STARTED"
log "Model: $MODEL"
log "Domains to build: ${#DOMAINS[@]} new (+ math already done)"
echo "========================================================" >> "$LOG"

# ============================================================
# PHASE 1: Fix dangling prerequisite references in math
# ============================================================
log "=== PHASE 1: Fix dangling prerequisite references ==="

run_claude "Fix dangling prerequisite references" <<'PROMPT'
You are working in the open-knowledge-graph project.
Read CLAUDE.md and meta/schema.md for project context.

TASK: Fix all dangling prerequisite references in the mathematics domain.

1. Run: python tools/validate.py — note all 'not found' prerequisite warnings
2. For each dangling reference, determine the best fix:
   a. If a topic with a similar name already exists, update the reference to use the correct existing ID
   b. If no similar topic exists, create a proper stub topic file with:
      - Correct YAML frontmatter (id, title, domain, course, prerequisites)
      - A ## Core Idea section (2-3 sentences minimum)
      - Place it in the most appropriate course directory
3. After all fixes, run validate.py again to confirm zero dangling references
4. Run: python tools/stats.py to report final counts

Use the Task tool to parallelize where possible — e.g., spawn sub-agents to create multiple stub files simultaneously.
PROMPT

# ============================================================
# PHASE 2: Populate empty math courses
# ============================================================
log "=== PHASE 2: Populate remaining math courses ==="

declare -A MATH_COURSE_TOPICS=(
  [linear-algebra]=35
  [multivariable-calculus]=35
  [methods-of-proof]=25
  [probability-and-statistics]=35
  [discrete-math]=30
)

for course in linear-algebra multivariable-calculus methods-of-proof probability-and-statistics discrete-math; do
  target=${MATH_COURSE_TOPICS[$course]}

  # Skip if already populated
  existing=$(count_topics "domains/mathematics/$course")
  if [ "$existing" -gt 5 ]; then
    log "SKIP: math/$course already has $existing topics"
    continue
  fi

  run_claude "Populate math/$course (~$target topics)" <<PROMPT
You are working in the open-knowledge-graph project.
Read CLAUDE.md and meta/schema.md for the full schema specification.
Read 2-3 existing topic files from domains/mathematics/calculus-2/ and domains/mathematics/precalculus/ for format and quality reference.

TASK: Create approximately $target topic files for the $course course under domains/mathematics/$course/.

Guidelines:
- domain: mathematics, course: $course
- Follow the schema exactly (YAML frontmatter + required/optional body sections)
- One .md file per topic, filename = topic ID
- Prerequisites should reference existing topics from earlier courses where appropriate
- Include both hard and soft prerequisites
- Use stage: formal-systems or advanced as appropriate
- Build realistic prerequisite chains within the course
- IDs must be globally unique — read domains/mathematics/ to check existing IDs first
- Write substantive Core Idea sections (2-5 sentences), not stubs
- Include How It's Best Learned and Common Misconceptions for at least half the topics

Use the Task tool to spawn sub-agents for parallel topic creation when possible.
After creating all files, run: python tools/validate.py
Report: number of topics created, any validation errors.
PROMPT
done

# ============================================================
# PHASE 3: Build new domains (Tiers 1-5)
# ============================================================
log "=== PHASE 3: Build new domains ==="

for domain in "${DOMAINS[@]}"; do
  title="${DOMAIN_TITLES[$domain]}"
  hint="${DOMAIN_HINTS[$domain]}"

  log "--- Domain: $domain ($title) ---"

  # Skip if domain already has substantial content
  if [ -d "domains/$domain" ]; then
    existing=$(count_topics "domains/$domain")
    if [ "$existing" -gt 20 ]; then
      log "SKIP: domains/$domain already has $existing topics"
      continue
    fi
  fi

  # Step 1: Plan the domain structure
  run_claude "Plan domain: $domain" <<PROMPT
You are working in the open-knowledge-graph project.
Read CLAUDE.md, meta/schema.md, meta/course-list.md, and meta/developmental-stages.md for context.
Read domains/mathematics/_domain.yml for the domain config format.

TASK: Design the course structure for the '$domain' domain ("$title").

Domain context: $hint

Steps:
1. Create directory: domains/$domain/
2. Create domains/$domain/_domain.yml with:
   - domain: $domain
   - title: "$title"
   - description: (2-3 sentence description)
   - courses: list of course objects with id, title, stage
3. Create subdirectories for each course under domains/$domain/
4. Design 6-10 courses that reflect how $title is typically taught:
   - Start from introductory/foundational level
   - Progress through intermediate to advanced undergraduate
   - Each course should map to roughly 25-40 topics
   - Set appropriate developmental stages
5. For courses that build on mathematics or other domains already in the graph,
   note the cross-domain prerequisite connections in a brief comment in _domain.yml

Follow how this subject is actually organized in education. Use standard course names.
PROMPT

  # Step 2: Populate each course
  if [ -d "domains/$domain" ]; then
    for course_dir in "domains/$domain"/*/; do
      [ -d "$course_dir" ] || continue
      course=$(basename "$course_dir")
      [[ "$course" == _* || "$course" == "." || "$course" == ".." ]] && continue

      # Skip if already populated
      existing=$(count_topics "$course_dir")
      if [ "$existing" -gt 5 ]; then
        log "SKIP: $domain/$course already has $existing topics"
        continue
      fi

      run_claude "Build $domain/$course" <<PROMPT
You are working in the open-knowledge-graph project.
Read CLAUDE.md and meta/schema.md for the schema specification.
Read domains/$domain/_domain.yml for the domain plan.
Read 1-2 existing math topic files from domains/mathematics/algebra-1/ for format reference.

TASK: Create topic files for the '$course' course in the '$domain' domain.
Directory: domains/$domain/$course/

Guidelines:
- domain: $domain, course: $course
- Create 25-40 topic files (one .md file per topic, filename = topic ID)
- Follow the schema exactly: YAML frontmatter + ## Core Idea (required) + optional sections
- Build realistic prerequisite chains:
  - Within this course (topics building on earlier topics)
  - To prior courses in this domain
  - Cross-domain prerequisites to mathematics topics where appropriate
    (e.g., physics topics depending on calculus, econ depending on algebra)
- IDs must be globally unique — prefix with domain name if there's ambiguity risk
  (e.g., physics-vectors, chem-equilibrium)
- Write substantive Core Idea sections (2-5 sentences)
- Include How It's Best Learned and Common Misconceptions for at least half the topics
- Set appropriate developmental stage (pre-formal through advanced)

Use the Task tool to spawn sub-agents for parallel topic creation.
After creating all files, run: python tools/validate.py
Report the count of topics created and any validation issues.
PROMPT
    done
  else
    log "WARN: domains/$domain not created by planning step, skipping courses"
  fi

  # Checkpoint: validate after each domain
  log "Validating after $domain..."
  python tools/validate.py >> "$LOG" 2>&1 || true
done

# ============================================================
# PHASE 4: Final validation and stats
# ============================================================
log "=== PHASE 4: Final validation ==="
python tools/validate.py 2>&1 | tee -a "$LOG" || true
python tools/stats.py 2>&1 | tee -a "$LOG" || true

# Count results
total_domains=$(ls -d domains/*/ 2>/dev/null | wc -l)
total_topics=$(count_topics "domains/")

# ============================================================
# PHASE 5: Detail pass (only if all 19 domains exist)
# ============================================================
if [ "$total_domains" -ge 19 ]; then
  log "=== PHASE 5: All 19 domains present — starting detail enhancement ==="

  for domain_dir in domains/*/; do
    domain=$(basename "$domain_dir")

    for course_dir in "$domain_dir"*/; do
      [ -d "$course_dir" ] || continue
      course=$(basename "$course_dir")
      [[ "$course" == _* || "$course" == "." || "$course" == ".." ]] && continue

      # Only enhance courses that have content
      topic_count=$(count_topics "$course_dir")
      [ "$topic_count" -lt 5 ] && continue

      run_claude "Enhance $domain/$course" <<PROMPT
You are working in the open-knowledge-graph project.
Read CLAUDE.md and meta/schema.md for context.

TASK: Enhance the topic files in domains/$domain/$course/ with more detail.

For each .md topic file in this directory:
1. If ## How It's Best Learned is missing, add it (pedagogical notes: effective representations, activities, sequencing advice)
2. If ## Common Misconceptions is missing, add it (known student errors and why they occur)
3. If the ## Core Idea is fewer than 2 sentences, expand it to 2-5 sentences
4. If builds-toward is empty [], fill in any known forward dependencies within the domain
5. Verify prerequisite types (hard vs soft) are appropriate — hard means "will fail without it", soft means "helpful but not required"
6. Add tags if the tags list is empty

Use the Edit tool to modify files in place. Don't rewrite files that are already complete (have all sections with substantive content).
Use the Task tool to parallelize — spawn sub-agents to enhance multiple files simultaneously.
PROMPT
    done
  done
else
  log "Only $total_domains domains present (need 19 for detail pass). Skipping Phase 5."
fi

# ============================================================
# FINAL SUMMARY
# ============================================================
total_domains=$(ls -d domains/*/ 2>/dev/null | wc -l)
total_topics=$(count_topics "domains/")

cat > "$SUMMARY" <<EOF
OKG Autonomous Build Summary
=============================
Completed: $(date)
Log: $LOG

Domains: $total_domains
Total topic files: $total_topics
Model: $MODEL

Phase 1: Fix dangling refs — $(grep -c "DONE.*dangling" "$LOG" 2>/dev/null || echo "check log")
Phase 2: Math expansion — $(grep -c "DONE.*math/" "$LOG" 2>/dev/null || echo "check log")
Phase 3: New domains — $(grep -c "DONE.*Build " "$LOG" 2>/dev/null || echo "check log") courses built
Phase 4: Validation — see log
Phase 5: Detail pass — $(grep -c "DONE.*Enhance" "$LOG" 2>/dev/null || echo "not reached")

Failures: $(grep -c "FAIL:" "$LOG" 2>/dev/null || echo "0")

Next steps:
- Review the log for any failures
- Run: python tools/validate.py
- Run: python tools/stats.py
- Spot-check topic quality in new domains
- Generate visualizations for new domains
EOF

log "=========================================="
log "BUILD COMPLETE"
log "Domains: $total_domains | Topics: $total_topics"
log "Summary: $SUMMARY"
log "=========================================="
