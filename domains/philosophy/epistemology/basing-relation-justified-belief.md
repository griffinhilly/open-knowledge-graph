---
id: basing-relation-justified-belief
title: The Basing Relation in Justified Belief
domain: philosophy
course: epistemology
prerequisites:
- id: justified-true-belief
  type: hard
- id: foundationalism
  type: soft
builds-toward:
- virtue-integration-knowledge-proper
tags:
- justification
- basing
- belief-forming
- intentionality
stage: formal-systems
status: validated
---

# The Basing Relation in Justified Belief

## Core Idea
The basing relation specifies how a belief must be appropriately connected to its justifying reasons—not merely that one possesses justification, but that one's belief stands in the right causal or rational relationship to that justification. This distinguishes genuine justified belief from cases where a person has available justification they aren't actually using. Understanding the basing relation is essential for avoiding counterexamples where someone holds a true, seemingly-justified belief for the wrong reasons.

## How It's Best Learned
Study cases where someone has available justification but fails to base their belief on it—such as forming a belief for psychological comfort despite evidence against it. Compare with cases where the belief is properly based on available reasons.

## Common Misconceptions
- Thinking the basing relation is merely about being able to cite justifying reasons when asked.
- Confusing the basing relation with the cause of one's belief (they're related but distinct).
- Assuming all cases of justified belief involve explicit conscious reasoning.

## Questions

```yaml
- question: "Maria has excellent analyst reports confirming her stock pick will succeed, but she never reads them. She buys the stock because her lucky coffee mug fell in a way she interprets as a good omen. Is her belief that the stock will succeed justified?"
  type: multiple-choice
  options:
    - "Yes — she possesses the justification (the analyst reports exist), so her belief counts as justified"
    - "No — she has no justification at all, since superstitious reasoning provides zero evidential support"
    - "No — although she possesses justification, her belief is not based on it; it is based on the omen, not the evidence"
    - "Yes — the basing relation only requires that adequate justification be available in principle, not that it causally produced the belief"
  answer: 2
  explanation: "This is the core case the basing relation is designed to diagnose. Maria has justification — the evidence exists — but her belief is not *based* on it. Her belief was formed through superstition, not through the available evidence. Options A and D represent exactly the misconception the basing relation corrects: having justification in one's possession is necessary but not sufficient. The justification must be *operative* — it must be what actually produces and sustains the belief. Option B is too strong; the point is not that she has no justification at all, but that the justification she has is not doing the epistemic work."

- question: "Which of the following best captures the distinction between rationalization and genuine justified belief?"
  type: multiple-choice
  options:
    - "Rationalization involves false beliefs; genuine justified belief always involves true beliefs"
    - "Rationalization means reaching a conclusion first (for non-evidential reasons), then finding supporting justification afterward; genuine justified belief means the justification actually produces and sustains the belief"
    - "Rationalization is always unconscious; genuine justified belief always involves explicit, conscious reasoning from evidence"
    - "Rationalization uses emotional rather than empirical evidence; genuine justified belief excludes all emotional influence"
  answer: 1
  explanation: "The epistemically important difference is about the direction of causation. In rationalization, you already hold the belief (from desire, emotion, social pressure) and then identify supporting reasons post hoc. The reasons are collected to justify a conclusion you've already reached, not to generate it. In genuine justified belief, the evidence or reasons causally (or reasons-responsively) produce the belief. A rationalizer and a genuine believer may have identical sets of available evidence — the difference lies entirely in whether that evidence is doing the epistemic work."

- question: "If a person can correctly articulate good reasons for their belief when asked, that is sufficient evidence that their belief is properly based on those reasons."
  type: true-false
  answer: false
  explanation: "Being able to cite justification retrospectively does not show that the justification was operative in forming the belief. A skilled rationalizer can articulate compelling reasons for a conclusion she reached through wishful thinking. The basing relation requires that the reasons *causally or reasons-responsively* produced the belief — not that they can be mentioned when prompted. The misconception conflates having access to a justification (a cognitive resource) with having a belief that was formed by that justification (an epistemic achievement)."

- question: "The basing relation matters even in cases where both the belief and the available justification are correct — what is at issue is not the truth of the belief or the quality of the justification, but whether the justification is actually doing the work of producing the belief."
  type: true-false
  answer: true
  explanation: "This is precisely why the basing relation is philosophically significant and not just a practical concern. Imagine someone with complete, accurate evidence for a true conclusion, who nonetheless believes that conclusion for irrelevant reasons. The justification is excellent, the belief is true, but the belief is not *based* on the justification — and epistemologists argue it therefore does not constitute knowledge. The basing relation separates having the right epistemic resources from using them correctly."

- question: "Why is possessing adequate justification not sufficient for a belief to count as genuinely justified? What additional condition does the basing relation require, and why does this matter for Gettier-style problems?"
  type: short-answer
  answer: "Possessing justification means the relevant evidence or good reasons exist in your cognitive repertoire. But a belief can be formed through completely different processes — emotion, habit, superstition — while the justification remains unused. The basing relation requires that the justification be causally or reasons-responsively operative: the belief must be formed and maintained *because of* the justification, not merely alongside it. For Gettier cases, this matters because many proposed repairs to the JTB account require that the belief 'tracks' or 'flows from' the justification in the right way — not merely that justification exists nearby."
  explanation: "The basing relation also clarifies the difference between propositional justification (you have reasons that would justify a belief) and doxastic justification (your belief is actually supported by those reasons in the right way). Only doxastic justification — belief based on justification — is epistemically valuable. This distinction explains why rationalization is epistemically defective even when the rationalizer has good evidence: the evidence isn't doing the epistemic work, so the belief isn't genuinely justified despite the evidence being available."
```

## Explainer

From justified true belief, you know that knowledge — in the standard pre-Gettier analysis — requires three components: a belief that is true, and justification for holding it. But there is a gap in that account. Consider a person who has excellent evidence that their flight departs at noon (they checked the airline website, their phone calendar, and a printed itinerary), but who believes it departs at noon for a completely different reason — a superstition about the number 12 or a gut feeling from a dream. Do they have justified belief? They possess justification (the evidence exists), but their belief is not *based* on that justification. The **basing relation** is the connection that determines whether the justification you possess is actually doing the work of supporting your belief.

The distinction between *having* justification and *basing* a belief on that justification runs throughout epistemology. Foundationalism, your soft prerequisite, tells you that justification ultimately rests on basic beliefs that are non-inferentially justified. But even if such a foundation exists, an upper-level belief might fail to be properly grounded in it. You might have a foundationally secure perceptual belief ("I see something red") and also hold a belief about the tomato in front of you, but if your tomato-belief is actually formed by wishful thinking rather than by inference from your perceptual state, it is not properly based — even if all the inferential support is theoretically available to you.

The basing relation is typically analyzed as either **causal** or **reasons-responsive**. A causal account says your belief is based on a reason if and only if that reason causally produced the belief through an appropriate process. A reasons-responsive account says your belief is properly based if you would revise it in response to changes in the evidence. Both accounts try to capture the intuition that belief-formation is not just a matter of having reasons filed away somewhere in your head — the reasons must be *operative*, actually influencing how you form and maintain the belief. This is why the misconception of "citing reasons when asked" fails: you might be able to articulate justification after the fact without that justification having played any role in forming the belief.

The basing relation matters most when diagnosing epistemically defective cases that are not outright irrational. A person with a motivated belief — someone who believes their child is innocent because they love them, while also possessing (but not consulting) exculpatory evidence — may have access to all the right justification and still fail to *know*, because the belief is based on love rather than evidence. The basing relation captures the difference between rationalization (finding justification for a conclusion you've already reached for other reasons) and genuine justified belief (reaching a conclusion because of your evidence). For Gettier problems and their successors, understanding this relation becomes essential: many proposed repairs to the JTB account turn precisely on ensuring that the belief connects to its justification in the right way, not merely that justification exists somewhere in the vicinity.
