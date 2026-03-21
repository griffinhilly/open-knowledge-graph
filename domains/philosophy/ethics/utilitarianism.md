---
id: utilitarianism
title: Utilitarianism
domain: philosophy
course: ethics
prerequisites:
- id: consequentialism
  type: hard
builds-toward:
- act-vs-rule-utilitarianism
- trolley-problem
- applied-ethics-intro
tags:
- normative-ethics
- utilitarianism
- Bentham
- Mill
- happiness
stage: formal-systems
status: validated
---

# Utilitarianism

## Core Idea
Utilitarianism, developed by Jeremy Bentham and refined by John Stuart Mill, holds that the right action is the one that maximizes total utility—typically understood as happiness, pleasure, or preference satisfaction—summed across all affected parties. Bentham proposed a felicific calculus measuring pleasures by intensity and duration; Mill introduced qualitative distinctions between higher and lower pleasures. Classical utilitarianism is impartial (everyone's utility counts equally) and aggregative (we sum across individuals). Major challenges include the repugnant conclusion in population ethics, the problem of utility monsters, and situations where maximizing utility requires violating individual rights.

## How It's Best Learned
Read Mill's Utilitarianism in full—it is short and addresses many standard objections. Then test the view on cases like organ harvesting (killing one to save five) and explain why utilitarian intuitions either align or conflict with common moral intuitions.

## Common Misconceptions
- Utilitarianism does not say 'do whatever makes you happiest'; it requires impartiality—your own happiness counts no more than anyone else's.
- Mill's higher/lower pleasure distinction was explicitly designed to avoid the objection that utilitarianism rates poetry lower than pushpin if more people enjoy pushpin.

## Questions

```yaml
- question: "A pharmaceutical company could save $5 million by skipping a safety test, with an estimated 1-in-10,000 chance of causing one death. A classical utilitarian analysis of this decision requires:"
  type: multiple-choice
  options:
    - "Prioritizing the company's welfare since corporations count as persons in modern law"
    - "Weighing the expected utility of the financial gain against the expected disutility of harm to all affected parties, including the potential victim, with equal weight"
    - "Deferring to individual autonomy — consumers can choose whether to take the risk"
    - "Rejecting the cost-benefit framing as a category error in ethical reasoning"
  answer: 1
  explanation: "Classical utilitarianism requires aggregating utility across all affected parties with impartiality — the company's profit counts, but so does the potential victim's welfare, counted equally. The correct utilitarian analysis compares expected benefits to expected harms across everyone affected. Option A violates impartiality (companies don't get privileged standing); option C smuggles in autonomy-based reasoning foreign to classical utilitarianism; option D rejects the consequentialist framework entirely."

- question: "The 'organ harvesting' thought experiment — killing one healthy patient to save five dying ones — is a challenge to utilitarianism because:"
  type: multiple-choice
  options:
    - "It shows utilitarianism cannot handle cases involving more than two people"
    - "The utilitarian calculus appears to endorse killing an innocent person to maximize aggregate welfare, which conflicts with the intuition that individuals have rights that cannot be violated even for the greater good"
    - "Utilitarianism cannot calculate the utility of dying patients accurately"
    - "Mill explicitly argued that organ harvesting is always impermissible under higher pleasures"
  answer: 1
  explanation: "The organ harvesting case is designed to reveal a structural tension: if utilitarianism requires maximizing total utility, and five lives saved produces more utility than one life preserved, the calculus seems to endorse the killing. This conflicts with the near-universal intuition that individuals have rights that function as side-constraints — things you cannot do to them even for aggregate benefit. Most utilitarians respond with rule utilitarianism or indirect arguments, but the tension is genuine and is the point of the thought experiment."

- question: "According to utilitarian theory, your own suffering deserves equal moral weight to the suffering of a complete stranger."
  type: true-false
  answer: true
  explanation: "Impartiality is one of utilitarianism's most demanding and most important features. When summing utility across affected parties, every person's welfare enters the calculation with equal weight — your own suffering is not privileged over a stranger's, and a stranger's is not more important than yours. This is what distinguishes utilitarianism from egoism (maximize your own welfare) and from partial theories that give special weight to family or community. The common misconception is that utilitarianism is about maximizing your own happiness — it is not."

- question: "Mill's distinction between higher and lower pleasures solves the problem of utilitarianism by showing that intellectual and moral pleasures always outweigh physical pleasures in utilitarian calculations."
  type: true-false
  answer: false
  explanation: "Mill's distinction introduces a qualitative criterion — experienced judges who have tried both prefer higher pleasures — but it does not make higher pleasures automatically outweigh lower ones in all calculations. It complicates, rather than solves, the utilitarian framework by adding a criterion (the preferences of competent judges) that goes beyond simple pleasure measurement. Furthermore, the distinction introduces its own problems: it depends on who counts as a competent judge and whether their preferences are themselves utility-maximizing."

- question: "What is Derek Parfit's 'repugnant conclusion,' and what does it reveal about classical utilitarianism as an ethical theory?"
  type: short-answer
  answer: "The repugnant conclusion is the result that classical utilitarianism favors a world with a vast population of people whose lives are barely worth living over a smaller world of flourishing people, as long as the total sum of utility is higher. It reveals that the aggregative, impartial structure of classical utilitarianism generates counterintuitive verdicts in population ethics — specifically, that adding people with marginally positive lives always increases total utility, even if it dilutes average welfare enormously."
  explanation: "Parfit's conclusion is not a mere curiosity — it exposes a structural feature of any theory that maximizes total welfare without regard to distribution or average. The result seems clearly wrong to most people: a world of billions barely scraping by seems worse than a smaller, flourishing civilization. Yet classical utilitarianism is committed to it. Responses include switching to average utilitarianism (maximize average, not total welfare) or adopting a critical level for what counts as a life worth adding. Each response generates new counterintuitive results, showing how deep the problem runs."
```

## Explainer

You already know from studying consequentialism that the rightness of an action is determined by its outcomes. Utilitarianism is the most influential consequentialist theory: it specifies exactly what outcome matters — **utility**, understood as happiness, pleasure, or preference satisfaction — and exactly how to aggregate it: sum across all affected individuals, giving each person's welfare equal weight. Jeremy Bentham systematized this into a **felicific calculus** that attempted to measure pleasures by intensity, duration, certainty, propinquity, fecundity, purity, and extent. The right action is the one that, of all available options, produces the greatest sum of this calculated happiness.

John Stuart Mill accepted Bentham's framework but found it too crude. A life of intellectual engagement felt intuitively more valuable than one of mere bodily pleasure, even if the latter contained more pleasure by Bentham's measures. Mill responded by introducing **qualitative distinctions** between higher pleasures (intellectual, aesthetic, moral) and lower pleasures (physical, sensory). His test: anyone who has experienced both types, and experienced them fully, prefers the higher. "It is better to be Socrates dissatisfied than a fool satisfied." This move saves utilitarianism from the "pig satisfied" objection but introduces a criterion — the preferences of experienced judges — that goes beyond simple pleasure measurement.

The **impartiality** requirement is utilitarianism's most demanding feature and its most important. Your own welfare counts no more than a stranger's; a stranger's welfare counts no more than your own. This is egalitarian in a deep sense: everyone's utility is entered into the sum with equal weight. But it also generates counterintuitive verdicts. If killing one healthy patient and distributing their organs would save five dying patients, the utilitarian calculus seems to favor the killing. This **organ harvesting problem** is the canonical challenge: utilitarianism appears to require violating individual rights whenever doing so maximizes aggregate welfare. Most utilitarians have responses — rule utilitarianism, indirect utilitarianism, accounts of secondary effects — but the tension remains a genuine problem.

Two further challenges deserve attention. The **utility monster** is a being that gets vastly more utility from resources than anyone else: utilitarianism seems to require transferring everything to it. The **repugnant conclusion** (Derek Parfit) shows that classical utilitarianism favors a world of vast numbers of people whose lives are barely worth living over a smaller world of flourishing people, as long as the total utility is higher. These aren't mere thought experiments — they reveal structural features of an aggregative, impartial calculus that any utilitarian theory must address. Understanding both the theory's remarkable clarity and these deep difficulties is what separates genuine engagement with utilitarianism from caricature.
