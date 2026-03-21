---
id: effective-altruism-and-scope
title: "Effective Altruism and Scope"
domain: philosophy
course: applied-rationality
prerequisites:
  - id: scope-sensitivity
    type: hard
  - id: expected-value-decision-making
    type: hard
  - id: tail-risk-and-black-swans
    type: soft
tags: ["effective-altruism", "scope", "rationality", "ethics", "impact"]
stage: advanced
status: draft
---

## Core Idea

Effective altruism applies Rationalist principles — scope sensitivity, expected value reasoning, calibrated uncertainty — to the question of how to do the most good. The core insight: if you are going to invest time or money in helping others, the same principles that make you a better forecaster make you a better philanthropist. Interventions vary by orders of magnitude in cost-effectiveness — distributing bed nets to prevent malaria saves a life for roughly $5,000, while some popular charitable causes cost millions per life saved. Scope sensitivity demands taking these differences seriously rather than giving based on emotional resonance alone. Effective altruism also applies expected value reasoning to cause selection: prioritizing by scale (how big is the problem?), neglectedness (how much is already being done?), and tractability (can additional resources make progress?).

## How It's Best Learned

Compare the cost-effectiveness of charitable interventions using GiveWell's research. Estimate the expected impact per dollar for two causes you care about. Practice separating emotional resonance from quantitative impact — which interventions feel most compelling to you, and which actually produce the most good per dollar? Notice the gap.

## Common Misconceptions

- Effective altruism is not utilitarian by definition — it is a framework for improving the effectiveness of whatever moral values you hold.
- EA does not mean only donating to the single most effective charity — it means being informed and deliberate about impact, which allows for diverse cause prioritization.
- Quantifying impact does not mean ignoring things that are hard to measure — it means being honest about uncertainty while still making comparisons.

## Questions

```yaml
- question: "A donor gives $10,000 to a local symphony because 'music enriches our community.' A GiveWell-recommended charity could use the same money to prevent roughly two deaths from malaria. Which principle of effective altruism does the donor's reasoning most directly violate?"
  type: multiple-choice
  options:
    - "The principle that all charitable giving should be directed to global poverty"
    - "Scope sensitivity — the donor's emotional resonance with local culture does not scale with the magnitude of impact"
    - "Expected value reasoning — the donor failed to calculate the probability that the symphony would fail without their donation"
    - "Neglectedness — local symphonies receive far too little funding compared to global health"
  answer: 1
  explanation: "The donor's reasoning reflects scope insensitivity: the warm feeling of supporting local culture is not proportional to the actual difference made. Effective altruism's core demand is that if you are going to help, you should take seriously the differences in how much good different interventions do — including the difference between saving two lives and enriching one community's concert season. The violation is not that the donor chose arts over poverty (EA is not prescriptive about cause areas) but that the decision was driven by emotional resonance rather than comparative impact."

- question: "The EA prioritization framework evaluates causes by scale, neglectedness, and tractability. Which of the following best describes why 'neglectedness' is a distinct criterion from 'scale'?"
  type: multiple-choice
  options:
    - "Neglectedness measures how emotionally urgent the problem feels; scale measures how many people are affected"
    - "A large-scale problem may already be well-funded, meaning marginal resources have limited impact — neglectedness captures where additional resources can do the most good"
    - "Neglectedness applies only to global health causes; scale applies to existential risks"
    - "Neglectedness and scale are actually the same criterion measured in different units"
  answer: 1
  explanation: "A problem can be enormous in scale (affecting billions) and still be heavily funded, leaving little room for marginal impact. Neglectedness asks: given existing resources, how much can one more dollar or hour of effort accomplish? A smaller problem that receives almost no attention may offer much higher returns to additional investment than a huge problem that already commands billions in funding. This is why EA analysis separates the size of the problem from the gap between the problem's importance and current resource allocation."

- question: "Effective altruism is by definition a utilitarian framework — it requires believing that the only thing that matters morally is maximizing total welfare."
  type: true-false
  answer: false
  explanation: "EA is a framework for improving the *effectiveness* of whatever moral values you hold, not a commitment to any specific ethical theory. Someone who values animal welfare, existential risk reduction, or systemic justice can apply EA principles — scope sensitivity, expected value reasoning, cause prioritization — to pursue their values more effectively. The claim is methodological, not first-order ethical: be deliberate and quantitative about impact. This is one of the most common misconceptions about EA."

- question: "If Charity A costs $5,000 per life saved and Charity B costs $1,000,000 per life saved, then according to EA reasoning, $1,000,000 donated to Charity A does 200 times more good than the same amount donated to Charity B."
  type: true-false
  answer: true
  explanation: "This is exactly the kind of calculation EA demands. $1M to Charity A saves 200 lives; $1M to Charity B saves 1 life. The 200x difference is real and morally significant — not an artifact of cold calculation but what scope sensitivity actually means. Many donors resist this reasoning because Charity B may have higher emotional salience or personal resonance. EA's contribution is to insist that these differences matter and should drive decision-making."

- question: "Why isn't 'giving to the cause that resonates most emotionally' a reliable guide to maximizing impact, even when the donor genuinely wants to do good?"
  type: short-answer
  answer: "Emotional resonance tracks identifiability, vividness, and personal connection — not scale of impact. Identified, visible suffering (a child in a news story) generates more emotional response than statistical suffering (millions dying from preventable disease), even when the statistical harm is vastly greater. This is scope insensitivity: our feelings do not scale with the magnitude of the problem. Giving by emotional resonance also favors causes with compelling narratives over neglected causes where marginal impact is highest. The gap between emotional salience and quantitative impact is exactly what EA tries to close."
  explanation: "This is the core problem EA was designed to address. The psychology of charitable giving is well-documented to favor proximity, identifiability, and narrative. These are not reliable signals of where additional resources will do the most good. EA does not say emotions are bad — it says they should be calibrated against evidence, not used as the final arbiter of cause selection."
```
