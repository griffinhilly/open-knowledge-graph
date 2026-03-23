---
id: rawlsian-justice-principles
title: Rawls's Two Principles of Justice
domain: philosophy
course: political-philosophy
prerequisites:
- id: rawls-original-position
  type: hard
- id: rawlsian-justice
  type: hard
builds-toward:
- egalitarianism-contemporary
- justice-comparative-theories
tags:
- Rawls
- justice
- fairness
- difference-principle
stage: formal-systems
status: validated
---

# Rawls's Two Principles of Justice

## Core Idea
From the original position behind a veil of ignorance, Rawls argues rational parties would select two principles: equal basic liberties for all, and inequality only if it benefits the least-advantaged. This maximin approach prioritizes protecting the worst-off and dominates contemporary political philosophy as a framework for evaluating institutions.

## Questions

```yaml
- question: "Under Rawls's theory, a society proposes trading some political freedoms for significantly higher average wealth that would benefit even the least advantaged. Is this just?"
  type: multiple-choice
  options:
    - "Yes — if the trade improves the position of the least advantaged, the difference principle permits it"
    - "Yes — if a majority votes for it from behind the veil of ignorance, it satisfies Rawls's conditions"
    - "No — basic liberties cannot be traded for economic advantages under the first principle's lexical priority"
    - "It depends on the magnitude of the economic gain and how severely the liberty is curtailed"
  answer: 2
  explanation: "Rawls's first principle has lexical priority: equal basic liberties must be fully satisfied before any economic considerations apply. No economic gain — however large, and even one that benefits the least advantaged — can justify restricting basic liberties. This is what 'lexical priority' means: the first principle is not weighed against the second, it must be satisfied first. Options A and B both violate this ordering by treating liberty as tradeable against wealth. This distinguishes Rawls sharply from utilitarianism, which could permit such tradeoffs."

- question: "In a Rawlsian society, doctors earn ten times more than janitors. This inequality leads hospitals to invest in equipment that measurably improves health outcomes for the poorest citizens. Is this arrangement just under the difference principle?"
  type: multiple-choice
  options:
    - "No — the difference principle requires equal pay for all members of society"
    - "No — permitting the wealthy to earn disproportionately is inherently unjust regardless of downstream effects"
    - "Yes — the inequality benefits the least advantaged members, satisfying the difference principle"
    - "Yes — any arrangement chosen behind the veil of ignorance is automatically just"
  answer: 2
  explanation: "The difference principle explicitly permits inequalities when they improve the position of the least advantaged. If higher doctor salaries create incentives that generate better healthcare for the worst-off, the inequality is justified on Rawlsian grounds. Option A confuses the difference principle with strict egalitarianism — Rawls never required equal outcomes. Option D is incorrect: Rawls's argument is that these specific two principles are what rational actors would choose, not that any veil-of-ignorance outcome is valid."

- question: "Rawls's difference principle requires that all members of a just society have equal income and wealth."
  type: true-false
  answer: false
  explanation: "This is one of the most common misreadings of Rawls. The difference principle does not mandate equality — it *permits* inequalities, provided they benefit the least advantaged. Rawls recognized that strict equality might actually harm the worst-off, because some inequalities create productive incentives. The difference principle is a constraint: inequalities are just if and only if they make the least-advantaged group better off than they would be under equal distribution. This rules out inequalities that only benefit the already-advantaged, but not inequality per se."

- question: "In Rawls's framework, the first principle of equal basic liberties cannot be sacrificed even to greatly improve the economic position of the least advantaged."
  type: true-false
  answer: true
  explanation: "This is precisely what lexical priority means. The first principle must be fully satisfied before the second principle applies at all. No amount of economic improvement — even a dramatic increase in the welfare of the worst-off — justifies restricting basic liberties. Rawls built this ordering deliberately to protect rights that he believed could not be subject to utilitarian-style cost-benefit analysis. A society that sacrifices political freedom for economic gain, however beneficently distributed, fails Rawlsian justice at the first step."

- question: "Why would rational people behind the veil of ignorance choose the maximin strategy, and how does this reasoning lead to the difference principle?"
  type: short-answer
  answer: "Behind the veil of ignorance, you don't know whether you'll be born wealthy or disadvantaged, talented or not. Since you can't assign probabilities to your social position, Rawls argues you'd adopt maximin: choose the arrangement whose worst possible outcome is the best available. This risk-averse strategy makes sense when the stakes are permanent (your entire life's prospects) and the downside is severe. Maximin leads directly to the difference principle: since you might end up at the bottom, you want the worst-off position to be as good as possible — so you only accept inequalities that make that position better than equality would."
  explanation: "The veil of ignorance creates genuine uncertainty about your place in society, not just ignorance of specific probabilities. Rawls argued this uncertainty makes gambling on a high expected value irrational when the worst outcome is a life of severe disadvantage. The rational response is to protect the floor. Critics like Nozick argue maximin is not the uniquely rational response to uncertainty, but Rawls's point is that given the stakes — a whole lifetime, not a one-time gamble — protecting the worst case is the defensible choice from behind the veil."
```

## Explainer

You already understand Rawls's original position: the thought experiment in which rational individuals choose principles of justice without knowing their place in society — their class, wealth, natural talents, race, sex, or conception of the good. The veil of ignorance strips away the information that typically biases our moral and political judgments. Rawls argues that principles chosen from this impartial standpoint would be genuinely fair — "justice as fairness." Now we arrive at the content: what two principles would people actually choose?

The **First Principle** is lexically prior and non-negotiable: each person is to have the most extensive system of equal basic liberties compatible with a similar system for all. "Basic liberties" include political liberties (to vote, run for office), freedom of speech and assembly, liberty of conscience, personal freedoms, and rights against arbitrary seizure. Crucially, these liberties cannot be traded away for economic advantage — you cannot choose a society with greater wealth at the cost of losing political freedom. Rawls calls this **lexical priority**: the first principle must be fully satisfied before the second applies.

The **Second Principle** governs inequalities in income, wealth, and social positions. It has two parts. First, **fair equality of opportunity**: positions must be open to all under genuine conditions of fair competition — not just formally open, but open in practice, requiring that those with similar talents and motivation have similar prospects regardless of class background. Second, the **difference principle**: social and economic inequalities are just only if they work to the greatest benefit of the **least advantaged members of society** — the worst-off group, defined by their share of primary social goods.

The difference principle requires careful interpretation. It doesn't mandate equality — it permits inequality whenever inequality makes the worst-off better off than they would be under an equal arrangement. The idea is that some inequalities create incentives that grow the overall pie, and if the worst-off get a larger slice even while the best-off get a disproportionate share, the arrangement is justified. What it rules out are inequalities that only benefit the already-advantaged. The rational basis for choosing this principle from behind the veil is the **maximin strategy**: choose the arrangement whose worst possible outcome is best. Since you might turn out to be the least advantaged, you want that position to be as good as possible.

What makes this framework so influential — and so contested — is the difference principle's egalitarian bite. It implies that vast inequalities are unjust unless they continuously improve the situation of the worst-off. In practice this requires not just formal equality of opportunity but substantial investment in education, healthcare, and social mobility for the disadvantaged. Libertarians like Nozick object that the difference principle disregards how people came to have what they have; utilitarians argue it may sacrifice aggregate welfare to protect the worst-off. Rawls maintained that justice, properly understood, is neither about maximizing aggregate welfare nor about enforcing historical entitlements, but about designing institutions that no one behind the veil could reasonably reject.
