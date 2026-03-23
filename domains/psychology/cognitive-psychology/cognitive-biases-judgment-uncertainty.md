---
id: cognitive-biases-judgment-uncertainty
title: Cognitive Biases in Judgment Under Uncertainty
domain: psychology
course: cognitive-psychology
prerequisites:
- id: reasoning-biases-and-errors
  type: hard
tags:
- biases
- heuristics
- judgment
- probability
- decision
stage: formal-systems
status: draft
---

# Cognitive Biases in Judgment Under Uncertainty

## Core Idea
When judging probabilities or likelihoods, people rely on heuristics producing systematic biases. The representativeness heuristic causes overestimation of small-sample probabilities; the availability heuristic causes frequency estimates biased by memory accessibility; anchoring bias shows initial values disproportionately influence final judgments. These biases persist despite awareness and remain difficult to overcome.

## Questions

```yaml
- question: "Linda is 31, single, outspoken, and very concerned with social justice. Which is more probable? (A) Linda is a bank teller. (B) Linda is a bank teller and a feminist activist."
  type: multiple-choice
  options:
    - "Option B — the description fits a feminist teller so much better that the probability is higher."
    - "Option A — P(A) ≥ P(A and B) always holds; every feminist teller is also a teller, so teller alone is at least as probable."
    - "They are equally probable because feminist teller is simply a more specific version of teller."
    - "Option B — adding true, fitting information to a description always increases its probability."
  answer: 1
  explanation: "This is the conjunction fallacy, driven by the representativeness heuristic. The description makes 'feminist teller' feel more probable because it fits the narrative better — but the basic probability rule P(A) ≥ P(A and B) is unconditional: the set of all bank tellers must include all feminist tellers plus any non-feminist tellers. Adding a condition can only maintain or reduce probability, never increase it. Option D states the bias explicitly and is wrong for the same reason. The Linda problem shows how narrative coherence overrides logic."

- question: "A disease affects 1 person in 1,000. A diagnostic test is 99% accurate (1% false positive rate). A patient tests positive. A physician estimates there is roughly a 99% chance the patient has the disease. Which cognitive error is the physician making?"
  type: multiple-choice
  options:
    - "Availability bias — the vividness of a positive test result inflates its perceived reliability."
    - "Base rate neglect driven by the representativeness heuristic — the test's accuracy is salient while the disease's rarity is ignored."
    - "Anchoring bias — the 99% figure in the test's accuracy anchors the probability estimate upward."
    - "No error — 99% test accuracy means a positive result is 99% reliable."
  answer: 1
  explanation: "Applying Bayes' theorem: out of 1,000 patients tested, about 1 is a true positive and about 10 are false positives (1% × 999). So only roughly 1 in 11 positive tests (~9%) reflects actual disease. The physician focuses on the accuracy figure — which feels representative of a reliable result — and ignores the base rate (1 in 1,000). This is base rate neglect: the representativeness of 'accurate test → positive result' crowds out the prior probability. Option D is the misconception being tested."

- question: "Anchoring effects on judgment persist even when subjects are explicitly told the initial anchor value is random and irrelevant to the question."
  type: true-false
  answer: true
  explanation: "In Tversky and Kahneman's classic studies, subjects who spun a wheel rigged to land on 10 or 65 gave systematically different estimates of the percentage of African nations in the UN — despite knowing the wheel was random. Awareness does not eliminate anchoring because the bias operates in the automatic, fast-processing system that generates the initial estimate before deliberate reasoning can intervene. This is what makes anchoring practically important: debiasing requires structural interventions (removing the anchor, requiring explicit base rate information) rather than mere awareness."

- question: "The availability heuristic produces accurate frequency estimates when events are salient and easy to recall, because salient events are usually frequent."
  type: true-false
  answer: false
  explanation: "The heuristic is a useful rule of thumb precisely because frequency and memorability are often correlated — but the correlation breaks down when events are memorable for reasons other than frequency: emotional salience, novelty, media coverage, and personal relevance all inflate availability without reflecting actual rates. Shark attacks are far rarer than deaths by vending machine but vastly more memorable. The heuristic systematically misestimates exactly those cases where society's attention and resources are most misallocated — dramatic, visible risks are overweighted relative to chronic, statistical ones."

- question: "Why do cognitive biases in probability judgment persist even when people are aware of them, and what does this imply about effective debiasing?"
  type: short-answer
  answer: "Cognitive biases arise from fast, automatic heuristic processing that generates judgments before deliberate reasoning can intervene. Awareness engages slower, deliberative reasoning, but typically too late to override the initial biased estimate — you can recognize the Linda problem as a conjunction fallacy after the fact while still having 'felt' option B was more probable. Research shows awareness reduces bias only marginally. What works better are structural interventions: presenting base rates explicitly and prominently, requiring decision-makers to consider the opposite hypothesis, using checklists that force consideration of alternatives, and redesigning choice architectures to remove anchors."
  explanation: "The practical implication is that individual education is a weak debiasing tool. The biases are features of the cognitive architecture, not merely failures of knowledge. Effective debiasing changes the environment of the decision — the structure of how information is presented — rather than relying on individuals to mentally correct for biases they know they have."
```

## Explainer

From your study of reasoning biases, you know that human judgment systematically deviates from normative probability theory. Kahneman and Tversky's **heuristics and biases** program (1970s–2000s) catalogued these deviations — not as random errors but as predictable, replicable patterns that arise from specific cognitive shortcuts. Three heuristics account for the most practically significant biases: representativeness, availability, and anchoring.

The **representativeness heuristic** means we judge probability by how well something matches a prototype or stereotype, ignoring base rates. The classic case: "Linda is 31, single, outspoken, concerned with social justice. Which is more probable — Linda is a bank teller, or Linda is a bank teller and a feminist?" Most people choose the conjunction (teller AND feminist), even though elementary probability says P(A) ≥ P(A and B) always. The narrative fit of "feminist teller" feels more probable than "teller" because it matches the description better — representativeness overrides logic. The same heuristic causes **base rate neglect**: if a disease affects 1 in 1,000 people and a test is 99% accurate, most people say a positive test result means you almost certainly have the disease — forgetting that with such a low base rate, false positives vastly outnumber true positives. Representativeness also produces **the gambler's fallacy**: after five heads in a row, tails feels "due" because HHHHHT is more representative of a fair coin than HHHHHH, even though the coin has no memory.

The **availability heuristic** means we estimate the frequency of events by how easily examples come to mind. Deaths by shark attack are massively overestimated relative to deaths by falling vending machines — because shark attacks are vivid, media-covered, and memorable. Deaths by vending machine are neither dramatic nor covered. The heuristic is useful (frequent events are usually easier to recall) but fails when memorability is driven by factors other than frequency: novelty, emotional salience, recency, and personal relevance all inflate availability without reflecting actual rates. This creates predictable policy distortions — societies allocate vastly disproportionate resources to dramatic, visible risks while underinvesting in chronic, statistical ones.

**Anchoring** is perhaps the most surprising bias because it operates even when the anchor is obviously arbitrary. When asked to estimate the percentage of African nations in the UN, subjects first spin a wheel rigged to land on 10 or 65; those who saw 10 guessed ~25%, those who saw 65 guessed ~45%. The wheel should be irrelevant — but it isn't. The anchor establishes a starting point, and **adjustment from anchor is typically insufficient**, leaving final estimates clustered near the starting value. Anchoring affects salary negotiations (whoever names first captures the anchor), legal sentencing (prosecutors' numerical recommendations influence judges' sentences), and medical diagnosis (the first diagnosis mentioned biases subsequent evaluation). The disturbing implication is that these biases persist even when people are aware of them, even with financial incentives for accuracy, and even in experts in their domains. Awareness debiases marginally; structural changes (checklists, explicit base rate information, consider-the-opposite exercises) help more.
