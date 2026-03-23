---
id: stylometry-distant-reading
title: Stylometry and Quantitative Textual Analysis
domain: literature
course: comparative-literature
prerequisites:
- id: moretti-distant-reading
  type: hard
- id: narratology
  type: soft
tags:
- digital-humanities
- quantitative-methods
- authorship
- stylometry
stage: expert
status: draft
---

# Stylometry and Quantitative Textual Analysis

## Core Idea
Stylometry uses computational analysis to identify authorial 'style' by measuring linguistic features (word frequencies, sentence length, punctuation patterns) across texts. Stylometric methods can solve attribution problems, identify ghostwriting, and reveal patterns invisible to close reading. In comparative literature, stylometry enables large-scale analysis of stylistic variation across languages, periods, and traditions. However, stylometry raises philosophical questions: Can style be meaningfully quantified? What is hidden when literature becomes numerical data?

## How It's Best Learned
Run stylometric analysis on a corpus of texts and interpret the results. Compare algorithmic findings with interpretive readings. Consider what stylometric evidence supports and what it obscures.

## Common Misconceptions
That stylometry reveals objective truth about texts. Stylometric measures are interpretive choices (which features to measure?), and their meaning depends on theoretical framing. Quantification doesn't ensure objectivity.

## Explainer

You know from Moretti's distant reading that literary scholarship can operate on large corpora rather than individual texts, using aggregation to reveal patterns invisible to close reading. Stylometry is one of the most developed quantitative methods within this tradition, and it applies a specific wager: that authors leave measurable traces in the surface features of their prose — word frequencies, function word distributions, sentence length patterns, punctuation habits — and that these traces are stable enough to identify authorship even when content varies. The analogy is forensic: just as handwriting has distinctive features even when the message changes, writing style carries authorial fingerprints.

The best-known application is **authorship attribution**: determining who wrote a disputed or anonymous text. The Federalist Papers case is canonical — statistical analysis of function word frequencies (words like "the," "of," "by") supported the attribution of disputed papers to Madison rather than Hamilton, because function words are largely unconscious and therefore harder to fake than content words. The technique has been applied to Shakespeare's collaborators, Elena Ferrante's identity, and the detection of ghostwritten books. The insight is that style is not just what you consciously choose to say — it is also the unconscious rhythms of how you say it.

Stylometry raises immediate philosophical questions that any serious practitioner must engage. **What features to measure?** Choosing word frequency over sentence rhythm, or including punctuation versus ignoring it, are not neutral decisions — they encode assumptions about what constitutes "style." Different feature sets can yield different authorship conclusions for the same texts. Stylometric analysis is therefore not the mechanical production of truth; it is a series of interpretive choices about what counts as evidence, followed by computation, followed by more interpretation of what the numbers mean. Quantification does not remove the interpreter — it embeds the interpreter's assumptions in the algorithm.

The deeper question is: **what is "style" when made computational?** Close reading assumes that style is meaningful — Hemingway's short sentences carry thematic weight, Faulkner's long ones enact consciousness. Stylometry treats style as a byproduct of cognitive habit, largely unconscious and content-independent. These are genuinely different theories of what literary style is and does. The most sophisticated work in the field holds both: using computational methods to identify large-scale patterns and then returning to close reading to interpret what those patterns mean. The numbers answer "who?" and point toward "what pattern?"; interpretation answers "so what?" Distance and close reading are not rivals — they are sequential tools, each doing what the other cannot.

## Questions

```yaml
- question: "Stylometric analysis attributes a disputed text to Author A with 94% confidence. A literary scholar argues the text's themes are inconsistent with A's known work. Which statement best characterizes the relationship between these two forms of evidence?"
  type: multiple-choice
  options:
    - "The statistical evidence is stronger because it is objective; the thematic argument is subjective"
    - "Both are interpretive, and they answer different questions — stylometry addresses surface linguistic habits, thematic analysis addresses meaning"
    - "The thematic evidence overrides the statistical evidence because literature is about meaning, not statistics"
    - "The conflict means neither result is reliable and the attribution must remain unknown"
  answer: 1
  explanation: "Stylometry and thematic analysis answer different questions. Stylometry asks: whose unconscious linguistic habits produced this surface? Thematic analysis asks: whose conscious ideas shaped this content? These can diverge — ghostwriting and collaboration are common, and authors change. Neither method is simply 'more objective.' Understanding their different claims prevents false conflicts and enables more nuanced attribution arguments."

- question: "Why does the choice of which linguistic features to measure in stylometry count as an interpretive decision rather than a neutral technical choice?"
  type: short-answer
  answer: "Different feature sets (function words, sentence length, punctuation, rare words) rest on different assumptions about what constitutes 'style' — whether it is unconscious habit or deliberate choice, whether it is lexical or syntactic. Different assumptions produce different results for the same texts. The choice of features is therefore a theoretical claim about the nature of style embedded in the methodology, not a value-neutral technical setting."
  explanation: "This connects to the broader epistemological point that quantification doesn't guarantee objectivity — it relocates interpretive decisions into the design of the method. Stylometry's power comes from consistency (the same features are measured the same way across texts), but consistency is not the same as neutrality. The scholar who chooses which features to measure is making an argument about what style is, and that argument shapes all subsequent results."
```
