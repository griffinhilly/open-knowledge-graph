#!/bin/bash

# Batch generator for Questions and Explainer sections
# Uses Python with ANTHROPIC_API_KEY from environment

python3 << 'PYSCRIPT'
import os
import re
import anthropic
import json
import sys

# Initialize Anthropic client with explicit API key handling
client = anthropic.Anthropic()

def extract_from_file(filepath):
    """Extract title and core idea from file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    title_match = re.search(r"^title: ['\"](.+?)['\"]", content, re.MULTILINE)
    title = title_match.group(1) if title_match else "Unknown"

    match = re.search(r'## Core Idea\n\n(.+?)(?=\n## |\Z)', content, re.DOTALL)
    if not match:
        match = re.search(r'## Core Idea\n(.+?)(?=\n## |\Z)', content, re.DOTALL)

    core_idea = match.group(1).strip() if match else None
    return title, core_idea, content

def generate_content(title, core_idea):
    """Generate questions and explainer using Claude."""

    prompt = f"""You are an educational content expert. For this genre-fiction topic, generate:

1. EXACTLY 5 questions in valid YAML format (in a ```yaml code fence):
   - 2 multiple-choice (4 options, answer 0-3, with explanation)
   - 2 true-false (one true, one false, each with explanation)
   - 1 short-answer (with explanation of good answer components)

2. An EXPLAINER: 3-5 paragraphs teaching the concept, progressive from foundational to nuanced.

Topic: {title}

Core Idea: {core_idea}

RESPONSE FORMAT (EXACT):

```yaml
questions:
  - type: multiple-choice
    question: "Question text?"
    options:
      - "Option A"
      - "Option B"
      - "Option C"
      - "Option D"
    correct_answer: 0
    explanation: "Explanation here"
  - type: multiple-choice
    question: "Question text?"
    options:
      - "Option A"
      - "Option B"
      - "Option C"
      - "Option D"
    correct_answer: 1
    explanation: "Explanation here"
  - type: true-false
    question: "Statement?"
    correct_answer: true
    explanation: "Explanation"
  - type: true-false
    question: "Statement?"
    correct_answer: false
    explanation: "Explanation"
  - type: short-answer
    question: "Question?"
    explanation: "What good answers should include..."
```

EXPLAINER TEXT:

[3-5 paragraphs of clear, progressive explanation]"""

    message = client.messages.create(
        model="claude-opus-4-1-20250805",
        max_tokens=2000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text

def parse_response(response_text):
    """Parse Claude's response."""
    yaml_match = re.search(r'```yaml\n(.*?)\n```', response_text, re.DOTALL)
    yaml_content = yaml_match.group(1) if yaml_match else None

    # Find explainer after the code fence
    parts = response_text.split('```')
    if len(parts) >= 2:
        explainer = parts[-1].strip()
        # Remove "EXPLAINER TEXT:" prefix if present
        explainer = re.sub(r'^EXPLAINER TEXT.*?:\s*', '', explainer, flags=re.DOTALL)
    else:
        explainer = None

    return yaml_content, explainer

def append_to_file(filepath, yaml_content, explainer):
    """Append Questions and Explainer to file."""
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(f"\n## Questions\n\n```yaml\n{yaml_content}\n```\n")
        f.write(f"\n## Explainer\n\n{explainer}\n")

# Main processing
directory = r"C:\Users\griff\Projects\griffin\open-knowledge-graph\domains\literature\genre-fiction"
md_files = sorted([f for f in os.listdir(directory) if f.endswith('.md')])

processed = 0
skipped = 0
failed = 0

for i, filename in enumerate(md_files, 1):
    filepath = os.path.join(directory, filename)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has Questions
    if '## Questions' in content:
        skipped += 1
        continue

    print(f"[{i}/{len(md_files)}] {filename}", file=sys.stderr)

    try:
        title, core_idea, content = extract_from_file(filepath)

        if not core_idea:
            print(f"  SKIP: No Core Idea found", file=sys.stderr)
            skipped += 1
            continue

        response = generate_content(title, core_idea)
        yaml_content, explainer = parse_response(response)

        if not yaml_content or not explainer:
            print(f"  FAIL: Could not parse response", file=sys.stderr)
            failed += 1
            continue

        append_to_file(filepath, yaml_content, explainer)
        processed += 1
        print(f"  OK", file=sys.stderr)

    except Exception as e:
        print(f"  ERROR: {e}", file=sys.stderr)
        failed += 1

print(f"\n=== SUMMARY ===", file=sys.stderr)
print(f"Processed: {processed}", file=sys.stderr)
print(f"Skipped (already done): {skipped}", file=sys.stderr)
print(f"Failed: {failed}", file=sys.stderr)

PYSCRIPT
