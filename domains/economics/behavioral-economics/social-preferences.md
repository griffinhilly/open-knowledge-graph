---
id: social-preferences
title: Social Preferences
domain: economics
course: behavioral-economics
prerequisites:
- id: bounded-rationality
  type: soft
- id: prospect-theory
  type: soft
tags:
- fairness
- altruism
- reciprocity
- inequality-aversion
- other-regarding-preferences
stage: advanced
status: validated
---

# Social Preferences

## Core Idea
Social preferences refer to the empirical finding that people care about the outcomes of others — not just their own — in systematic ways that violate the standard self-interest assumption. Laboratory experiments (ultimatum games, dictator games, public goods games, trust games) consistently show that people sacrifice material payoffs to achieve fairness, punish unfair behavior, reward cooperation, and share with strangers. Theoretical models by Fehr and Schmidt (inequality aversion), Rabin (fairness equilibrium), and Bolton and Ockenfels (ERC model) formalize these preferences. The evidence challenges the homo economicus assumption and has implications for contract design, public goods provision, tax compliance, and organizational management.

## Questions

```yaml
- question: "In the ultimatum game, a proposer offers a split of $10 and a responder can accept (both get their shares) or reject (both get nothing). Standard game theory predicts the proposer will offer the minimum and the responder will accept any positive amount. In practice, what happens?"
  type: multiple-choice
  options:
    - "Proposers offer the minimum and responders always accept, consistent with theory"
    - "Proposers typically offer 40-50% of the total, and responders frequently reject offers below 20-30%, even though rejection is costly"
    - "Proposers always offer exactly 50% to avoid any risk of rejection"
    - "Responders always reject because they prefer getting nothing over accepting an unfair offer"
  answer: 1
  explanation: "The modal offer is 40-50% of the total, and offers below 20% are rejected roughly half the time. This pattern is remarkably stable across cultures and stakes (replicated with several months' wages in developing countries). Proposers offer generously partly from fairness motives and partly from strategic fear of rejection. Responders reject low offers at a material cost to themselves, revealing a willingness to sacrifice money to punish unfairness. This behavior is incompatible with pure self-interest but consistent with models incorporating fairness or inequality aversion."

- question: "Social preferences only appear in laboratory experiments and do not affect real economic behavior outside the lab."
  type: true-false
  answer: false
  explanation: "Social preferences have been documented in numerous field settings. Workers reciprocate higher wages with greater effort (gift exchange), taxpayers comply at rates far exceeding what audit probabilities alone would justify (conditional cooperation), consumers pay premium prices for fair-trade products, and individuals contribute to public goods and charities at rates incompatible with pure self-interest. While laboratory and field magnitudes may differ, the fundamental pattern — that people care about fairness, reciprocity, and others' outcomes — is robust across contexts."

- question: "How does the Fehr-Schmidt model of inequality aversion formalize social preferences?"
  type: short-answer
  answer: "The Fehr-Schmidt model adds disutility from inequality to the standard utility function. An individual suffers from 'disadvantageous inequality' (when others earn more, weighted by alpha) and 'advantageous inequality' (when they earn more than others, weighted by beta), with alpha > beta (people dislike being behind more than being ahead). This parsimoniously explains ultimatum game rejections (reducing disadvantageous inequality), dictator game giving (reducing advantageous inequality), and conditional cooperation in public goods games."
  explanation: "The model's elegance lies in explaining a wide range of experimental results with just two parameters. It captures the asymmetry between envy (disliking being behind) and guilt (disliking being ahead), with envy being the stronger motive. It also explains heterogeneity: people differ in their alpha and beta parameters, and the distribution of types in a population determines equilibrium outcomes in strategic settings. This allows the model to accommodate both selfish and fair-minded behavior within a single framework."
```

## Explainer

Standard economic theory assumes that people are self-interested — they maximize their own material payoffs without regard for others' outcomes. This assumption is powerful because it is simple and generates clear predictions. But laboratory experiments designed to test it have produced a mass of evidence that it is descriptively wrong in important ways. People share money with strangers, reject unfair offers at a personal cost, cooperate in social dilemmas, and punish free-riders even when it hurts them. Social preferences research documents and models these patterns.

The experimental evidence is anchored in a set of canonical games. In the dictator game, one player unilaterally decides how to split a sum of money with an anonymous partner who has no say. Pure self-interest predicts giving nothing; in practice, the average offer is about 25-30% of the total, and only about a third of dictators give nothing. In the ultimatum game, the responder can reject the offer (destroying both payoffs), and rejection rates for low offers are high — about 50% of offers below 20% are rejected. In the public goods game, players can contribute to a common pool that is multiplied and shared equally; contributions start around 40-60% and decline over time as cooperators react to free-riding, but costly punishment of free-riders restores cooperation. In the trust game, one player sends money that is tripled, and the recipient decides how much to return; average returns are substantial, indicating both trust and trustworthiness.

Theoretical models have formalized these observations in different ways. Fehr and Schmidt's inequality aversion model adds a term to the utility function representing disutility from unequal outcomes — both advantageous and disadvantageous inequality reduce utility, but being behind is worse than being ahead. Rabin's fairness equilibrium model makes preferences conditional on intentions — people are kind to those who are kind to them and unkind to those who are unkind. Bolton and Ockenfels' ERC model focuses on relative payoffs — people care about their share of the total rather than the absolute level of inequality. Each model captures different aspects of the data, and no single model dominates.

The economic implications are substantial. In labor markets, social preferences explain why workers reciprocate higher wages with greater effort (efficiency wages work partly through the gift-exchange mechanism), why transparent pay inequality reduces morale and performance, and why perceived unfairness triggers counterproductive work behavior. In public economics, social preferences explain why tax compliance far exceeds levels predicted by audit probabilities and penalties — people comply partly because they believe it is fair and because they see others complying. In mechanism design, accounting for social preferences changes optimal contract structure — contracts that feel unfair may be rejected even when they are materially advantageous.

The relationship between social preferences and culture is nuanced. While ultimatum game results are remarkably stable across Western countries, Henrich et al.'s cross-cultural study found substantial variation in offers and rejection rates across 15 small-scale societies. Offers were higher in societies with greater market integration and in societies where public goods provision is more important. This suggests that social preferences are shaped by the institutional environment — not innate at fixed levels — and that culture, norms, and institutional incentives interact with whatever psychological substrate underlies fairness concern.
