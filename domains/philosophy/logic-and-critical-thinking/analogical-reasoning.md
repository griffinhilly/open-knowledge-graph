---
id: analogical-reasoning
title: Analogical Reasoning and Argument by Analogy
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: inductive-reasoning
  type: hard
builds-toward:
- abductive-reasoning
tags:
- analogy
- analogical-reasoning
- similarity
- induction
stage: formal-systems
status: validated
---

# Analogical Reasoning and Argument by Analogy

## Core Idea
Analogical reasoning infers that because two things are similar in relevant respects, they are likely similar in a further respect. The strength of an analogy depends on: the number of similarities, the relevance of those similarities to the conclusion, the absence of relevant disanalogies, and the scope of the claim being made. Analogies are the primary tool of legal reasoning (precedent), much of moral philosophy, and scientific hypothesis generation. A disanalogy — a relevant difference between the compared cases — is the standard way to challenge an analogical argument.

## How It's Best Learned
Evaluate the standard analogies in moral philosophy (e.g., Thomson's violinist analogy for abortion rights): list similarities, then list disanalogies, and assess whether the disanalogies undermine the conclusion. Practice generating disanalogies yourself.

## Common Misconceptions
- Thinking any similarity grounds an analogy — only relevant similarities count.
- Believing a disanalogy automatically defeats an analogy; a strong analogy may survive some disanalogies if they are not relevant to the conclusion.

## Questions

```yaml
- question: "A critic of Judith Thomson's violinist analogy points out that conception (unlike waking up connected to a stranger) can involve a voluntary act. Under what condition does this disanalogy actually undermine Thomson's conclusion?"
  type: multiple-choice
  options:
    - "Any difference between the cases automatically defeats the analogy, so the argument fails"
    - "Only if the voluntary nature of conception is relevant to the moral conclusion about the permissibility of disconnecting from the violinist"
    - "Only if the critic can identify three or more disanalogies, since a single difference is not enough"
    - "It always undermines the analogy, because disanalogies reveal that the cases are fundamentally different"
  answer: 1
  explanation: "A disanalogy defeats an analogical argument only when it is *relevant to the conclusion*. Thomson's analogy argues that being kept alive by another person's body does not automatically obligate that person to continue. The critic's disanalogy — voluntary conception — is relevant only if voluntarily creating a dependency changes the moral obligation to sustain it. Whether this disanalogy is relevant is itself a substantive moral question, not a logical one. The analogy may survive if the critic cannot show that voluntariness changes the obligation in the relevant way."

- question: "Which of the following analogical arguments is STRONGEST, given the criteria for evaluating analogical reasoning?"
  type: multiple-choice
  options:
    - "Country A and Country B are both in the Northern Hemisphere, so they probably have similar economic policies"
    - "Drug X cured the same disease in mice and rats, sharing 12 physiologically relevant biological pathways with humans, so it is likely to be effective in humans too"
    - "City A and City B both have rivers, so they probably have similar flood risks"
    - "Author A and Author B both wrote in the 19th century, so their novels probably share the same themes"
  answer: 1
  explanation: "Option B is strongest because it satisfies all key criteria: many similarities (12 pathways), those similarities are directly relevant to the conclusion (biological pathways determine drug efficacy), and the scope of the claim is appropriately narrow (likely effective). Options A, C, and D all rest on similarities (hemisphere, river, century) that are not clearly relevant to the proposed conclusions. Relevance of similarities — not mere quantity — is the decisive factor."

- question: "Finding any difference between two cases being compared in an analogical argument defeats the analogy."
  type: true-false
  answer: false
  explanation: "Disanalogies only undermine an analogical argument when they are *relevant to the conclusion*. Two cases will always differ in countless ways, most of which have nothing to do with what is being argued. A car and a bicycle differ in that one has an engine — but this difference is irrelevant to an analogy about road safety regulations based on speed limits. The systematic evaluation requires asking, for each difference: does this difference affect the property being argued about? If not, the disanalogy is harmless."

- question: "Only similarities that are relevant to the conclusion strengthen an analogical argument."
  type: true-false
  answer: true
  explanation: "This is the central principle of analogical evaluation. Two countries might share dozens of surface features — similar population sizes, similar climates, similar historical periods — but if none of those features are relevant to the economic conclusion being drawn, the analogy is weak despite the many similarities. Relevance is determined by causal or explanatory connection: does the shared property actually affect the property being predicted? Quantity of similarities is only evidence of strength when those similarities bear on the conclusion."

- question: "Why is a disanalogy only an effective rebuttal if it is relevant to the conclusion? Explain using an example."
  type: short-answer
  answer: "A disanalogy is relevant when the difference between the cases affects the very property being inferred. If I argue that City A's traffic plan should work in City B because both have similar populations, road density, and commuter patterns, pointing out that the cities have different names is an irrelevant disanalogy — the difference doesn't affect traffic behavior. But pointing out that City A has flat terrain while City B is mountainous IS relevant if terrain affects how traffic flows. The same logical principle applies in moral philosophy: a disanalogy matters only if it plausibly changes whether the conclusion holds."
  explanation: "This principle explains why analogical arguments are often productive even when disanalogies exist. The debate over Thomson's violinist focuses not on whether differences exist (they obviously do) but on whether those differences are morally relevant — whether they change the obligation in question. This forces the discussion to identify exactly which features of a situation determine moral conclusions, which is far more illuminating than simply noting the cases differ."
```

## Explainer

You already understand inductive reasoning: reasoning from specific observations to probable generalizations. Analogical reasoning is a close cousin, but instead of generalizing from many cases to a type, you reason from one case to another based on their similarity. The basic structure is: case A has properties P1, P2, P3 and also property P4; case B has P1, P2, P3; therefore B probably also has P4. The move is licensed not by repetition across many instances but by the strength of the resemblance between A and B.

The central skill is learning to evaluate analogical strength. Three factors matter most. First, **quantity of relevant similarities**: the more shared features, the stronger the analogy — but only relevant ones count. That two countries share a coastline is unlikely to be relevant to whether they will have similar economic policies. Second, **absence of relevant disanalogies**: a single important difference between the cases can undermine even a superficially strong analogy. The question is always whether the difference is *relevant to the conclusion*. Third, **scope of the claim**: a narrow conclusion ("B will probably exhibit P4 in similar circumstances") is easier to support analogically than a sweeping one ("B is fundamentally just like A in all respects").

Legal reasoning depends almost entirely on analogical reasoning in the form of precedent. When a court decides a new case by looking to prior rulings, it asks: is this case sufficiently similar to the precedent that the same rule should apply? Arguments in legal briefs are often exercises in showing why the present case resembles — or does not resemble — an earlier decision. Moral philosophy uses analogies the same way. Judith Jarvis Thomson's famous violinist argument for abortion rights invites you to imagine waking up connected to a famous violinist whose survival depends on remaining connected to your circulatory system for nine months. The analogy is designed to test your intuitions by stripping away emotionally loaded features of the original case. The correct response is to assess whether the relevant similarities hold — and to look carefully for relevant disanalogies.

A **disanalogy** — a relevant difference between the compared cases — is the standard tool for rebutting an analogical argument. Critics of Thomson's violinist argue that the cases differ in morally relevant ways: the origin of the dependency (voluntary conception vs. waking up connected to a stranger), the nature of the relationship, and so on. The analogy may still be illuminating even if the disanalogies are real — it can shift the terms of debate, expose hidden assumptions, and narrow the actual point of disagreement. This is why analogical reasoning in philosophy is rarely a knockdown move; it is more often a framing device that forces explicit engagement with what we actually believe about the features being compared.

The practical lesson is to be systematic when evaluating analogies. List the similarities; then list the differences; then ask, for each item on each list, whether it is *relevant to the conclusion*. An analogy that survives this analysis — where similarities are relevant and disanalogies are not — is genuinely strong. An analogy that fails it — where the apparent similarities are superficial and the disanalogies cut to the heart of the conclusion — is weak regardless of how intuitively compelling the comparison first appeared.
