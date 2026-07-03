#!/usr/bin/env python3
"""
Generate Questions and Explainer content for genre-fiction files.
Uses Claude API via direct environment variable access.
"""

import os
import re
import sys
import json
import time

# Try importing anthropic, handle missing gracefully
try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False
    print("WARNING: anthropic library not found. Will use template-based generation.")

def extract_from_file(filepath):
    """Extract title and core idea from file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has Questions
    if '## Questions' in content:
        return None

    title_match = re.search(r"^title: ['\"](.+?)['\"]", content, re.MULTILINE)
    title = title_match.group(1) if title_match else "Unknown"

    match = re.search(r'## Core Idea\n\n(.+?)(?=\n## |\Z)', content, re.DOTALL)
    if not match:
        match = re.search(r'## Core Idea\n(.+?)(?=\n## |\Z)', content, re.DOTALL)

    core_idea = match.group(1).strip() if match else None
    return {'title': title, 'core_idea': core_idea, 'content': content}

def generate_content_with_claude(title, core_idea):
    """Generate content using Claude API."""
    if not HAS_ANTHROPIC:
        return None

    try:
        client = anthropic.Anthropic()

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
    question: "Question?"
    options:
      - "Option A"
      - "Option B"
      - "Option C"
      - "Option D"
    correct_answer: 0
    explanation: "Explanation"
  - type: multiple-choice
    question: "Question?"
    options:
      - "Option A"
      - "Option B"
      - "Option C"
      - "Option D"
    correct_answer: 1
    explanation: "Explanation"
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

EXPLAINER TEXT (3-5 paragraphs):
[Your explanation here]"""

        message = client.messages.create(
            model="claude-opus-4-1-20250805",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )

        response = message.content[0].text

        # Parse response
        yaml_match = re.search(r'```yaml\n(.*?)\n```', response, re.DOTALL)
        yaml_content = yaml_match.group(1) if yaml_match else None

        # Find explainer after the code fence
        parts = response.split('```')
        if len(parts) >= 2:
            explainer = parts[-1].strip()
        else:
            explainer = None

        return {'yaml': yaml_content, 'explainer': explainer}

    except Exception as e:
        print(f"Error with Claude API: {e}", file=sys.stderr)
        return None

def append_to_file(filepath, yaml_content, explainer):
    """Append Questions and Explainer to file."""
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(f"\n## Questions\n\n```yaml\n{yaml_content}\n```\n")
        f.write(f"\n## Explainer\n\n{explainer}\n")

def process_batch(file_list):
    """Process a batch of files."""
    processed = 0
    failed = 0

    for i, filepath in enumerate(file_list, 1):
        filename = os.path.basename(filepath)
        print(f"[{i}/{len(file_list)}] {filename}", file=sys.stderr)

        try:
            result = extract_from_file(filepath)
            if not result:
                print(f"  SKIP: Already has Questions or no Core Idea", file=sys.stderr)
                continue

            title = result['title']
            core_idea = result['core_idea']

            # Try Claude first
            content = generate_content_with_claude(title, core_idea)

            if content and content['yaml'] and content['explainer']:
                append_to_file(filepath, content['yaml'], content['explainer'])
                processed += 1
                print(f"  OK", file=sys.stderr)
                # Rate limit to avoid API errors
                time.sleep(0.5)
            else:
                print(f"  FAIL: Could not generate content", file=sys.stderr)
                failed += 1

        except Exception as e:
            print(f"  ERROR: {e}", file=sys.stderr)
            failed += 1

    print(f"\nProcessed: {processed}, Failed: {failed}", file=sys.stderr)

if __name__ == "__main__":
    directory = r"C:\Users\griff\Projects\griffin\open-knowledge-graph\domains\literature\genre-fiction"

    # Get all MD files
    md_files = sorted([
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if f.endswith('.md')
    ])

    # Filter to files needing content
    files_to_process = []
    for filepath in md_files:
        result = extract_from_file(filepath)
        if result:
            files_to_process.append(filepath)

    print(f"Files needing content: {len(files_to_process)}", file=sys.stderr)

    # Process all
    process_batch(files_to_process)
