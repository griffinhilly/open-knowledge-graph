#!/usr/bin/env python3
"""
Add Questions and Explainer sections to all topic files in genre-fiction directory.

For each .md file:
1. Read the file
2. Extract Core Idea
3. Generate 5 questions (2 MC, 2 TF, 1 SA) in YAML format
4. Generate 3-5 paragraph explainer
5. Append both sections to file
"""

import os
import re
import anthropic

# Initialize Anthropic client - will use ANTHROPIC_API_KEY environment variable
try:
    client = anthropic.Anthropic()
except Exception as e:
    print(f"ERROR: Could not initialize Anthropic client: {e}")
    exit(1)

def extract_core_idea(content):
    """Extract the Core Idea section from markdown content."""
    # Match "## Core Idea" followed by blank line, then capture content until next section or EOF
    match = re.search(r'## Core Idea\n\n(.+?)(?=\n## |\Z)', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    # Try alternative pattern without blank line
    match = re.search(r'## Core Idea\n(.+?)(?=\n## |\Z)', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def extract_title(content):
    """Extract the title from YAML frontmatter."""
    match = re.search(r"^title: ['\"](.+?)['\"]", content, re.MULTILINE)
    if match:
        return match.group(1)
    return "Unknown"

def generate_questions_and_explainer(title, core_idea):
    """Use Claude to generate questions and explainer."""

    prompt = f"""You are an educational content expert. For the following topic, generate:

1. EXACTLY 5 questions in YAML format:
   - 2 multiple-choice questions (with 4 options labeled 0-3, one correct answer, and explanation)
   - 2 true-false questions (one true, one false, each with explanation)
   - 1 short-answer question (with explanation of what a good answer should include)

2. An EXPLAINER section: a 3-5 paragraph mini-lesson teaching the core concept. Target intermediate learners. Use clear language. Build from foundational to more nuanced understanding.

Topic Title: {title}

Core Idea:
{core_idea}

FORMAT YOUR RESPONSE EXACTLY AS FOLLOWS:

```yaml
questions:
  - type: multiple-choice
    question: "Question text?"
    options:
      - "Option 0"
      - "Option 1"
      - "Option 2"
      - "Option 3"
    correct_answer: 0
    explanation: "Why this is correct..."
  - type: multiple-choice
    question: "Question text?"
    options:
      - "Option 0"
      - "Option 1"
      - "Option 2"
      - "Option 3"
    correct_answer: X
    explanation: "Why this is correct..."
  - type: true-false
    question: "Statement to evaluate?"
    correct_answer: true
    explanation: "Why this is true..."
  - type: true-false
    question: "Statement to evaluate?"
    correct_answer: false
    explanation: "Why this is false..."
  - type: short-answer
    question: "Question requiring short written response?"
    explanation: "Explanation of what a good answer should include and why this matters..."
```

EXPLAINER TEXT (3-5 paragraphs):
[Your 3-5 paragraph mini-lesson here, teaching the core concept clearly and progressively]

Make sure questions test UNDERSTANDING of the core concept, not just recall. Make the explainer accessible but substantive."""

    message = client.messages.create(
        model="claude-opus-4-1-20250805",
        max_tokens=2000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text

def parse_response(response_text):
    """Parse Claude's response into questions YAML and explainer text."""
    # Find the YAML code fence
    yaml_match = re.search(r'```yaml\n(.*?)\n```', response_text, re.DOTALL)
    if not yaml_match:
        print("WARNING: Could not find YAML code fence")
        return None, None

    yaml_content = yaml_match.group(1)

    # Find explainer text after the code fence
    explainer_match = re.search(r'```\n\n(.*?)$', response_text, re.DOTALL)
    if not explainer_match:
        # Try alternative pattern
        explainer_match = re.search(r'EXPLAINER TEXT.*?:\n(.*?)$', response_text, re.DOTALL)

    explainer_text = explainer_match.group(1).strip() if explainer_match else ""

    return yaml_content, explainer_text

def append_sections_to_file(filepath, yaml_content, explainer_text):
    """Append Questions and Explainer sections to the file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create sections to append
    questions_section = f"\n## Questions\n\n```yaml\n{yaml_content}\n```\n"
    explainer_section = f"\n## Explainer\n\n{explainer_text}\n"

    # Append to file
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(questions_section)
        f.write(explainer_section)

def process_directory(directory):
    """Process all .md files in the directory."""
    md_files = sorted([f for f in os.listdir(directory) if f.endswith('.md')])

    print(f"Found {len(md_files)} .md files to process")

    successful = 0
    failed = 0

    for i, filename in enumerate(md_files, 1):
        filepath = os.path.join(directory, filename)
        print(f"\n[{i}/{len(md_files)}] Processing: {filename}")

        try:
            # Read file
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract title and core idea
            title = extract_title(content)
            core_idea = extract_core_idea(content)

            if not core_idea:
                print(f"  ERROR: Could not extract Core Idea from {filename}")
                failed += 1
                continue

            # Generate questions and explainer
            print(f"  Generating content for: {title}")
            response = generate_questions_and_explainer(title, core_idea)

            # Parse response
            yaml_content, explainer_text = parse_response(response)

            if not yaml_content or not explainer_text:
                print(f"  ERROR: Failed to parse response for {filename}")
                failed += 1
                continue

            # Append sections
            append_sections_to_file(filepath, yaml_content, explainer_text)
            print(f"  SUCCESS: Added Questions and Explainer sections")
            successful += 1

        except Exception as e:
            print(f"  ERROR: {e}")
            failed += 1

    print(f"\n\n=== SUMMARY ===")
    print(f"Successful: {successful}/{len(md_files)}")
    print(f"Failed: {failed}/{len(md_files)}")

if __name__ == "__main__":
    directory = r"C:\Users\griff\Projects\griffin\open-knowledge-graph\domains\literature\genre-fiction"
    process_directory(directory)
