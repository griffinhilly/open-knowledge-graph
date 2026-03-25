---
id: multi-case-analysis-knowledge
title: Multi-Case Analysis and Knowledge Conditions
domain: philosophy
course: epistemology
prerequisites:
- id: gettier-cases-formal-analysis
  type: hard
- id: margin-error-semantics
  type: soft
builds-toward:
- defeasibility-conditions-knowledge
- anti-luck-conditions-knowledge
tags:
- knowledge
- formal-analysis
- methodology
- cases
stage: formal-systems
status: validated
---
# Multi-Case Analysis and Knowledge Conditions

## Core Idea
Multi-case analysis systematically compares intuitions across related cases that differ in subtle ways to identify necessary and sufficient conditions for knowledge. By varying one feature at a time and noting how intuitions change, epistemologists create a formal landscape of knowledge conditions. This methodology has proven invaluable in responding to Gettier and in developing anti-luck accounts.

## How It's Best Learned
Take a proposed knowledge condition and construct case pairs that test it: one where the condition holds and knowledge seems present, one where it doesn't and knowledge seems absent. Use this to refine the condition. This systematic approach builds intuitions about what knowledge fundamentally requires.

## Common Misconceptions
- Multi-case analysis doesn't assume all our intuitions about cases are reliable. - The methodology aims to find stable patterns across many cases, not rely on any single case. - Disagreements in case intuitions don't invalidate the methodology; they highlight areas needing further analysis.

## Questions

```yaml
- question: "An epistemologist proposes that sensitivity (if P were false, the agent wouldn't believe P) is necessary for knowledge. A critic constructs a case where sensitivity holds but knowledge clearly doesn't, then another where sensitivity fails but knowledge seems present. What do these two cases together establish?"
  type: multiple-choice
  options:
    - "That sensitivity is neither necessary nor sufficient for knowledge"
    - "That intuitions about knowledge are too unreliable to use as evidence"
    - "That sensitivity is sufficient but not necessary for knowledge"
    - "That the Gettier problem has been definitively resolved by the sensitivity condition"
  answer: 0
  explanation: "Two cases are needed to establish two distinct failures. A case where sensitivity holds but knowledge doesn't shows sensitivity is not sufficient (you can have sensitivity without knowledge). A case where sensitivity fails but knowledge seems present shows sensitivity is not necessary (you can have knowledge without sensitivity). Together, they establish that sensitivity neither suffices nor is required — it is neither necessary nor sufficient. This is controlled variation in action: each case changes exactly the variable being tested."

- question: "What is the primary purpose of controlled variation in multi-case analysis?"
  type: multiple-choice
  options:
    - "To generate as many cases as possible so that no critic can address them all"
    - "To change exactly one feature between a pair of cases so that any change in intuitions can be attributed specifically to that feature"
    - "To confirm that philosophical intuitions are consistent across all cultures and individuals"
    - "To show that a single well-constructed case is sufficient to establish a philosophical conclusion"
  answer: 1
  explanation: "Controlled variation is a methodological discipline: hold everything constant except the one feature being tested. If intuitions change between the two cases, the changed feature is responsible. If they don't change, the feature doesn't affect knowledge attribution. This allows epistemologists to systematically test proposed conditions rather than generating cases haphazardly. It is the same logic as a controlled experiment: isolate the variable of interest by keeping everything else fixed."

- question: "The evidential strength of multi-case analysis comes from the convergence of intuitions across many carefully varied cases, not from any single case being conclusive."
  type: true-false
  answer: true
  explanation: "This is the methodological core of the approach. A single case can always be dismissed as an intuition pump, a misleading scenario, or a confusion about what the case stipulates. But when dozens of varied cases — manipulation cases, fake-barn cases, doxastic incontinence cases — all point in the same direction, that convergence constitutes evidence that is much harder to dismiss. The methodology treats intuitions as fallible data points; accumulation and convergence is what builds philosophical confidence."

- question: "If a proposed knowledge condition fails to correctly categorize all test cases, the entire methodology of case analysis is undermined."
  type: true-false
  answer: false
  explanation: "A condition failing for some cases is evidence about the condition, not evidence against the methodology. The methodology is designed to detect exactly this: if a condition doesn't work for all cases, that tells you the condition needs refinement. Cases are data; the methodology is the process of collecting and interpreting them. A failed condition prompts a revised condition, which gets tested against further cases. The methodology is self-correcting, not invalidated by any single failure."

- question: "Why does a large collection of carefully varied cases provide stronger evidence about knowledge conditions than a single counterexample like the original Gettier case?"
  type: short-answer
  answer: "A single case can be dismissed as a misleading intuition pump, an unusual exception, or a scenario that trades on ambiguity. Many carefully varied cases that all point in the same direction are much harder to dismiss — if different scenarios with different details all produce the same pattern of intuitions, that convergence suggests the pattern reflects something real about the structure of our knowledge concept rather than an artifact of one particular case's framing."
  explanation: "The Gettier cases were powerful enough to overturn a millennia-old analysis — but they were still debated. Subsequent case analysis built up an entire landscape: fake-barn cases, barn-façade cases, manipulation cases, each varying different features. When the same problems recur across all of them, the evidence is cumulative. This is why the post-Gettier literature generated hundreds of cases rather than just arguing from the original two — cases are the medium of evidence in analytic epistemology."
```

## Explainer

From your formal analysis of Gettier cases, you know how a single carefully constructed scenario can overturn a philosophical theory that had stood for millennia. The original Gettier cases were not just counterexamples — they were existence proofs that the three conditions of the JTB analysis (truth, belief, justification) are individually necessary but jointly insufficient. Once that was established, the question became: what further conditions are needed? **Multi-case analysis** is the systematic methodology for answering that question — not by finding one perfect case, but by building up a dense landscape of cases that collectively triangulate where the real conditions lie.

The core technique is **controlled variation**: you take a scenario and change exactly one feature, then ask whether your intuition about whether the agent knows changes. Suppose a proposed condition says "an agent knows P only if their belief is sensitive to P's truth" (roughly: if P were false, they would not believe P). You can test this by constructing pairs of cases — one where sensitivity holds and one where it does not — while keeping everything else identical. If knowledge tracks sensitivity in both directions (present when sensitivity holds, absent when it fails), that is evidence the condition is onto something. If you can construct a case where sensitivity holds but knowledge clearly doesn't (or vice versa), that tells you the condition is not quite right.

What makes this methodology powerful is accumulation. A single case can always be dismissed as an intuition pump, a misleading special case, or a confusion about the scenario's details. But when dozens of carefully varied cases all point in the same direction — when manipulation, justified falsehood, barn façade counties, and doxastic incontinence cases all exhibit the same pattern — the convergence is hard to ignore. The methodology treats philosophical intuitions about cases as data points: individually fallible, but collectively informative about the underlying structure of our concept of knowledge. This is why the post-Gettier literature produced such a proliferation of cases rather than simple arguments — cases are the medium of evidence in analytic epistemology.

The methodology also has important **limits** that disciplined practitioners keep in mind. Intuitions vary across individuals and cultures, so what seems obviously knowledge to one philosopher may not to another. A case designed to test one variable may inadvertently change others, making the result harder to interpret. And there is a deep question about whether our intuitions about artificial philosophers' cases track anything important about real knowledge, or merely track our folk-psychological reactions to stylized thought experiments. These limits do not abandon the method — they are reasons to practice it carefully, with multiple cases, explicit attention to what each case varies, and epistemic humility about what the pattern of intuitions establishes.
