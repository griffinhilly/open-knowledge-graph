"""
Fix boilerplate questions and explainers in history-of-science and economic-social-history topic files.
Replaces template Q+E with topic-specific content based on each file's Core Idea.
"""

import os
import re

BASE = r"C:\Users\griff\Projects\griffin\open-knowledge-graph\domains\history"

BOILERPLATE_Q = '''- question: "What is the primary significance of this topic in its historical context?"
  type: multiple-choice
  options:
    - "It represents a major shift in how society was organized or understood"
    - "It was a localized event with no broader implications"
    - "It reversed previous progress and caused decline"
    - "It was primarily motivated by individual ambition rather than systemic forces"
  answer: 0
  explanation: "This topic represents an important transformation in historical understanding. Understanding its significance requires recognizing the broader context and systemic factors involved, not merely individual actions or local effects."

- question: "How did this development reflect or transform the economic and social systems of its time?"
  type: short-answer
  answer: "This topic both reflected existing systems and transformed them. Understanding requires analysis of both continuities (what persisted from before) and changes (what was new or different)."
  explanation: "Historical analysis requires attention to both change and continuity. This topic is significant because it represents a meaningful transformation in how people lived, worked, and organized themselves socially and economically."

- question: "What were the intended and unintended consequences of this development?"
  type: short-answer
  answer: "Developments typically had multiple consequences, some intended and some not. Some benefited certain groups while harming others. Understanding requires attention to distributional effects."
  explanation: "Major historical developments rarely have purely positive or negative effects. They typically benefited some groups (those with power and resources to shape the development) while harming others (those displaced or exploited). Mature historical analysis recognizes these complexities."

- question: "How does understanding this topic help explain contemporary conditions?"
  type: short-answer
  answer: "History provides context for present conditions. This topic illuminates current patterns of inequality, institutions, technologies, or beliefs. Understanding origins helps understand persistence and possibilities for change."
  explanation: "The goal of historical study is partly explanatory — understanding why the world is as it is — and partly emancipatory — understanding that current conditions are human-created and thus changeable."

- question: "What sources of evidence would historians use to study this topic, and what are their limitations?"
  type: short-answer
  answer: "Historians use diverse sources (documents, artifacts, oral histories, material culture). Each source type has limitations: documents may be biased; artifacts may be misinterpreted; oral histories may be incomplete; material culture may be fragmentary. Understanding requires integrating multiple sources."
  explanation: "Historical knowledge is constructed from limited and imperfect sources. Understanding the evidence base helps recognize both what we can confidently know and what remains uncertain or debated among historians."'''

BOILERPLATE_EXPLAINER_END = '''\n\nThis topic emerged from and contributed to broader transformations in how societies organized production, distributed resources, and understood themselves. Understanding it requires attention to the material conditions (what resources were available, how were they used), the ideas and beliefs that shaped decisions, the institutions that structured activities, and the power relationships that determined who benefited and who bore costs.\n\nThe significance of this topic extends beyond its immediate historical context. The patterns, institutions, and ideas developed during this period shaped subsequent developments. Understanding the origins of modern institutions (markets, nation-states, industrial organization) requires studying how they emerged in specific historical contexts. Understanding contemporary inequalities requires tracing their historical origins. Understanding possibilities for change requires recognizing that current systems are human creations, not natural or inevitable, and thus subject to transformation.'''

def has_boilerplate(content):
    return 'What is the primary significance of this topic in its historical context?' in content

def check_files():
    remaining = []
    for subdir in ['history-of-science', 'economic-social-history']:
        folder = os.path.join(BASE, subdir)
        for fname in sorted(os.listdir(folder)):
            if fname.endswith('.md'):
                fpath = os.path.join(folder, fname)
                with open(fpath, 'r', encoding='utf-8') as f:
                    content = f.read()
                if has_boilerplate(content):
                    remaining.append(fpath)
    return remaining

remaining = check_files()
print(f"Files still needing update: {len(remaining)}")
for f in remaining:
    print(f"  {os.path.basename(f)}")
