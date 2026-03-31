---
id: heuristics-and-biases
title: Heuristics and Biases
domain: economics
course: behavioral-economics
prerequisites:
- id: bounded-rationality
  type: hard
tags:
- heuristics
- representativeness
- availability
- anchoring
- Kahneman-Tversky
stage: advanced
status: validated
---

# Heuristics and Biases

## Core Idea
Heuristics are mental shortcuts that simplify complex judgments by substituting an easier question for a harder one. Kahneman and Tversky identified three primary heuristics: representativeness (judging probability by similarity to a prototype), availability (judging frequency or probability by ease of recall), and anchoring and adjustment (estimating by starting from an initial value and adjusting insufficiently). Each heuristic is useful in many situations but produces systematic biases when the shortcut departs from statistical reality. The heuristics-and-biases program demonstrated that human judgment deviates from normative standards in predictable, systematic ways — not randomly — challenging the assumption that errors cancel out in aggregate and laying the psychological foundations for behavioral economics.

## Questions

```yaml
- question: "A doctor estimates that a rare disease is common because she recently treated three cases. This judgment most likely reflects which heuristic?"
  type: multiple-choice
  options:
    - "Representativeness — the cases are representative of the disease"
    - "Availability — recent vivid experiences make the disease seem more common than it is"
    - "Anchoring — the doctor is anchored on the number three"
    - "Affect — the doctor has an emotional reaction to the disease"
  answer: 1
  explanation: "The availability heuristic judges the probability or frequency of an event by the ease with which examples come to mind. Recent, vivid, or emotionally charged events are easier to recall and therefore judged as more frequent or probable. Three recent cases are highly available in the doctor's memory, leading to an overestimate of the disease's prevalence. The actual base rate of the disease is the relevant statistic, but availability substitutes ease of recall for statistical analysis."

- question: "Heuristics are always harmful because they deviate from optimal statistical reasoning."
  type: true-false
  answer: false
  explanation: "Heuristics are cognitive adaptations that trade accuracy for speed and efficiency. In many environments, they produce good-enough judgments with minimal cognitive cost. The representativeness heuristic often works because similar things do tend to belong to the same category; the availability heuristic often works because frequent events are indeed easier to recall. Biases arise at the margins — when the heuristic diverges from the statistical reality — but for everyday judgments under time pressure, heuristics are often the only feasible approach. Gigerenzer's ecological rationality program argues that heuristics can even outperform complex optimization in uncertain environments."

- question: "What is the anchoring effect, and why is it particularly difficult to overcome?"
  type: short-answer
  answer: "Anchoring occurs when an initial value (the anchor) disproportionately influences subsequent judgments, even when the anchor is arbitrary or irrelevant. People start from the anchor and adjust insufficiently toward the true value. It is difficult to overcome because anchoring operates through both deliberate adjustment (which people can try to correct) and selective accessibility (the anchor primes anchor-consistent information in memory), making it resistant to debiasing efforts. Even awareness of the bias does not eliminate it."
  explanation: "Tversky and Kahneman showed that spinning a wheel of fortune to generate a random number influenced estimates of the percentage of African countries in the UN — an obviously irrelevant anchor. Real-world anchoring affects salary negotiations (the first number named anchors the zone of possible agreement), legal judgments (damage award demands anchor jury deliberations), and retail pricing (suggested retail prices anchor willingness to pay). The dual-mechanism explanation (insufficient adjustment + selective accessibility) explains why anchoring is robust even among informed, motivated judges."
```

## Explainer

The heuristics-and-biases research program, launched by Tversky and Kahneman in the 1970s, fundamentally changed how economists and psychologists think about human judgment. Before their work, errors in judgment were typically attributed to random noise — people make mistakes, but errors cancel out on average, so aggregate behavior approximates rational expectations. Tversky and Kahneman showed that errors are not random — they are systematic, predictable, and driven by identifiable cognitive mechanisms.

The representativeness heuristic judges the probability that an object belongs to a category based on how similar it is to the category's prototype. "Steve is meticulous, orderly, detail-oriented, and shy. Is Steve more likely a librarian or a farmer?" Most people judge librarian, because Steve's description matches the librarian stereotype. But this ignores the base rate: there are far more farmers than librarians, so Steve is statistically more likely to be a farmer regardless of his personality description. The representativeness heuristic produces base-rate neglect (ignoring prior probabilities), the conjunction fallacy (judging "Linda is a bank teller and a feminist" as more probable than "Linda is a bank teller"), and insensitivity to sample size (treating small samples as equally informative as large ones).

The availability heuristic judges the frequency or probability of events by how easily examples come to mind. Events that are recent, vivid, emotionally intense, or heavily media-covered are more "available" and therefore judged as more frequent. People overestimate the risk of dramatic events (plane crashes, shark attacks, terrorism) and underestimate the risk of mundane events (heart disease, car accidents, diabetes) — not because they lack the statistical data but because availability substitutes for data. This has real consequences for risk perception, insurance purchasing, and public policy: fear of terrorism drives more security spending per life saved than fear of heart disease, even though heart disease kills orders of magnitude more people.

The anchoring and adjustment heuristic begins with an initial value and adjusts from it to reach a final estimate. The adjustment is typically insufficient — people do not move far enough from the anchor. In negotiations, the first number named becomes an anchor that influences the final agreement even when both parties know the anchor is arbitrary. In legal settings, plaintiff damage demands anchor jury awards. In real estate, listing prices anchor buyer offers. The mechanism has two components: deliberate adjustment (people consciously try to correct away from the anchor but stop too early) and selective accessibility (the anchor primes anchor-consistent information, biasing the evidence that comes to mind during evaluation). This dual mechanism explains why anchoring is so resistant to debiasing.

The broader significance of the heuristics-and-biases program for economics is that it provided the psychological microfoundations for behavioral economics. If people systematically misjudge probabilities, then expected utility maximization is not descriptively accurate. If anchoring influences willingness to pay, then market prices may not reflect "true" valuations. If availability shapes risk perception, then insurance markets and regulatory priorities may be distorted. These are not abstract possibilities — they are empirically documented patterns with real economic consequences, and they form the empirical base on which prospect theory, nudge theory, and behavioral finance are built.
