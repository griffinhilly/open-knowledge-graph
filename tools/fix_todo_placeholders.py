"""
Fix TODO placeholders in Core Idea sections by extracting the first 2-3
sentences (up to ~80 words) from the Explainer section.
"""

import os
import re

DOMAINS_DIR = os.path.join(os.path.dirname(__file__), '..', 'domains')
DOMAINS_DIR = os.path.normpath(DOMAINS_DIR)


def split_sentences(text):
    """Split text into sentences (simple heuristic)."""
    # Split on period followed by space or end-of-string, but not on common
    # abbreviations like "e.g.", "i.e.", "vs.", "Dr.", etc.
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)
    return [s.strip() for s in sentences if s.strip()]


def extract_core_idea(explainer_text, max_words=80, max_sentences=3):
    """Extract first 2-3 sentences up to ~80 words from explainer."""
    # Strip markdown bold/italic but keep the text
    clean = re.sub(r'\*\*([^*]+)\*\*', r'\1', explainer_text)
    clean = re.sub(r'\*([^*]+)\*', r'\1', clean)

    # Take first paragraph only
    paragraphs = clean.split('\n\n')
    first_para = paragraphs[0].strip() if paragraphs else clean

    # Remove any leading "From your study of..." or similar preamble?
    # No -- keep it natural, just take the first sentences.

    sentences = split_sentences(first_para)
    if not sentences:
        return None

    result_sentences = []
    word_count = 0
    for sent in sentences[:max_sentences]:
        sent_words = len(sent.split())
        if word_count + sent_words > max_words and result_sentences:
            break
        result_sentences.append(sent)
        word_count += sent_words

    if not result_sentences:
        return None

    return ' '.join(result_sentences)


def find_and_fix_todos():
    """Find topics with TODO/empty Core Ideas and fix from Explainer."""
    changes = []

    for root, dirs, files in os.walk(DOMAINS_DIR):
        for fname in files:
            if not fname.endswith('.md') or fname.startswith('_'):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Find Core Idea section
            core_match = re.search(
                r'(## Core Idea\s*\n)(.*?)(?=\n## |\Z)',
                content,
                re.DOTALL,
            )
            if not core_match:
                continue

            core_text = core_match.group(2).strip()

            # Check if TODO or essentially empty
            is_todo = 'TODO' in core_text or len(core_text.split()) < 10
            if not is_todo:
                continue

            # Check for Explainer section
            explainer_match = re.search(
                r'## Explainer\s*\n(.*?)(?=\n## |\Z)',
                content,
                re.DOTALL,
            )
            if not explainer_match:
                continue

            explainer_text = explainer_match.group(1).strip()
            if not explainer_text or len(explainer_text.split()) < 10:
                continue

            # Generate core idea from explainer
            new_core = extract_core_idea(explainer_text)
            if not new_core:
                continue

            # Replace the Core Idea content
            # Match from "## Core Idea\n" to the next "## " section
            old_section = core_match.group(0)
            new_section = core_match.group(1) + new_core + '\n'

            new_content = content.replace(old_section, new_section, 1)

            if new_content != content:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                changes.append({
                    'file': fname,
                    'filepath': fpath,
                    'old_core': core_text,
                    'new_core': new_core,
                })

    return changes


def main():
    print("Scanning for TODO/empty Core Idea sections...\n")
    changes = find_and_fix_todos()

    if not changes:
        print("No TODO placeholders found.")
        return

    print(f"Fixed {len(changes)} TODO Core Idea sections:\n")
    for c in changes:
        print(f"  [{c['file']}]")
        print(f"    OLD: {c['old_core'][:60]}...")
        print(f"    NEW: {c['new_core'][:120]}...")
        print(f"    file: {c['filepath']}")
        print()

    print(f"Done. {len(changes)} files updated.")


if __name__ == '__main__':
    main()
