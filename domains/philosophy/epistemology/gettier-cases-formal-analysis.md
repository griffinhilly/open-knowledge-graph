---
id: gettier-cases-formal-analysis
title: Gettier Cases and Formal Analysis
domain: philosophy
course: epistemology
prerequisites:
- id: justified-true-belief
  type: hard
- id: gettier-problems
  type: hard
- id: first-order-logic-syntax
  type: soft
- id: logical-consequence-and-validity
  type: soft
builds-toward:
- no-false-lemmas-condition
- defeasibility-conditions-knowledge
- anti-luck-conditions-knowledge
- multi-case-analysis-knowledge
tags:
- gettier
- knowledge
- counterexamples
- formal-analysis
stage: formal-systems
status: draft
---

# Gettier Cases and Formal Analysis

## Core Idea
Gettier cases present situations where someone has a justified true belief that fails to constitute knowledge due to a subtle break in the truth-dependence of justification. Formal analysis of these cases reveals the need for additional conditions beyond JTB to capture what knowledge really requires. The systematic study of Gettier cases has become central to contemporary epistemology.

## How It's Best Learned
Work through classic cases like the Smith-Jones example and the barn facade problem. Try to identify what exactly goes wrong in each case and why the person doesn't have knowledge despite meeting traditional JTB conditions. Then attempt to construct your own Gettier-style cases to test proposed definitions.

## Common Misconceptions
- Not all counterexamples to JTB are Gettier cases; some simply fail to meet one of the JTB conditions. - Gettier cases don't show that JTB is meaningless; they just show it's insufficient. - Not every weird case involving luck is a Gettier case.

## Explainer

You already know the justified true belief (JTB) analysis of knowledge — that S knows that P if and only if P is true, S believes P, and S is justified in believing P — and you have encountered Gettier problems as counterexamples showing that JTB is insufficient. Formal analysis of Gettier cases goes further: it asks exactly *why* each case fails and what that reveals about the structure of knowledge.

The original Gettier case has a precise structure. Smith justifiably believes "Jones will get the job and Jones has ten coins in his pocket." He infers the logical consequence: "The person who will get the job has ten coins in their pocket." This inference is valid. But Smith, not Jones, gets the job — and Smith happens to have ten coins in his own pocket. So the proposition is true, Smith believes it, and the belief is justified by valid reasoning from a justified premise. Yet something has clearly gone wrong: Smith's true belief is accidentally true. His justification supports the proposition only through a false intermediate belief (that Jones will get the job). The truth of the final proposition is "disconnected" from what actually made the intermediate premise true.

Formal analysis identifies the failure point: the justification that supports the belief is not properly connected to the truth-maker of the belief. In the Smith-Jones case, the justification runs through a false lemma. This diagnosis led to the **No False Lemmas condition**: knowledge requires that S's belief not be inferred through any false intermediate premise. But this patch is too narrow. The barn facade case shows a Gettier structure without any false lemma. Henry drives through an area that looks normal but is filled with fake barn facades; one real barn is in the field, and Henry happens to look at it and form the true belief "that's a barn." He uses no false premise, but he still lacks knowledge because in that environment, his belief-forming process is unreliable.

What formal analysis across many cases reveals is a general pattern: **epistemic luck** is the culprit. In every Gettier case, the agent's justification and the truth of the belief come apart in some way — the belief is true, but not *because of* the justification. This suggests that knowledge requires some kind of robust connection between justification and truth: a condition ensuring that the agent's belief-forming process or justification is sensitive to the actual truth-maker. Different proposals — safety conditions, sensitivity conditions, tracking theories, no-defeat conditions — each try to capture this connection differently. Analyzing Gettier cases formally is the method epistemologists use to test these proposals, seeking cases where the proposed condition is satisfied but knowledge is still intuitively absent, or vice versa.
