---
id: ultimatum-dictator-games
title: Ultimatum and Dictator Games
domain: economics
course: behavioral-economics
prerequisites:
- id: social-preferences
  type: hard
tags:
- ultimatum-game
- dictator-game
- experimental-games
- fairness
- rejection
stage: advanced
status: validated
---

# Ultimatum and Dictator Games

## Core Idea
The ultimatum game and dictator game are canonical experimental paradigms for studying social preferences. In the ultimatum game, a proposer offers a division of a sum to a responder, who can accept (both receive their shares) or reject (both receive nothing). In the dictator game, the proposer unilaterally decides the split with no possibility of rejection. Standard game-theoretic predictions (offer the minimum; accept any positive amount) fail dramatically: ultimatum proposers typically offer 40-50%, responders reject offers below 20% roughly half the time, and dictators give 20-30% on average. These robust findings provide the primary empirical evidence for fairness concerns, inequality aversion, and costly punishment, and they have been replicated across cultures, stake sizes, and experimental designs.

## Questions

```yaml
- question: "The dictator game eliminates the strategic motive for generosity present in the ultimatum game. Why is this methodologically important?"
  type: multiple-choice
  options:
    - "It makes the game simpler to explain to participants"
    - "It isolates pure fairness/altruism motives from strategic fear of rejection — any giving in the dictator game must reflect genuine other-regarding preferences"
    - "It tests whether people can do basic arithmetic"
    - "It eliminates all experimental demand effects"
  answer: 1
  explanation: "In the ultimatum game, generous offers could be strategically motivated — the proposer offers fairly not because they care about fairness but because they fear rejection. The dictator game eliminates this strategic concern by removing the responder's ability to reject. Any positive transfer by the dictator must reflect some form of other-regarding preference — altruism, fairness norms, guilt aversion, or inequality aversion. The fact that dictators still give substantial amounts (mean ~25%) is strong evidence against pure self-interest."

- question: "Rejection of low offers in the ultimatum game is irrational because the responder receives nothing instead of a small positive amount."
  type: true-false
  answer: false
  explanation: "Calling rejection 'irrational' assumes that the responder's only goal is to maximize their own monetary payoff. If the responder's utility function includes a fairness component — disutility from accepting an unfair division or utility from punishing unfair behavior — then rejection can be perfectly rational given those preferences. The responder is paying a material cost to express disapproval, enforce a fairness norm, or reduce inequality. From a social preferences perspective, the utility of punishment exceeds the disutility of losing the money."

- question: "What did Henrich et al.'s cross-cultural study of the ultimatum game reveal about the universality of fairness behavior?"
  type: short-answer
  answer: "Henrich et al. (2001) played the ultimatum game across 15 small-scale societies worldwide and found substantial cultural variation. Mean offers ranged from 26% (Machiguenga) to 58% (Lamelara). Offers were higher in societies with greater market integration (more experience with anonymous exchange) and greater dependence on cooperation. This suggests that while some fairness concern may be universal, its expression and magnitude are shaped by cultural norms and institutional environments."
  explanation: "The cross-cultural variation challenges both the pure self-interest prediction (offers were always above the minimum) and the idea that a specific fairness norm (e.g., 50/50 splits) is universal. Instead, the data suggest that market participation and cooperative institutions cultivate stronger norms of fairness in anonymous exchanges. The study remains one of the most important contributions to understanding the interplay between culture and economic behavior."
```

## Explainer

The ultimatum game and dictator game are to behavioral economics what the fruit fly is to genetics — simple, well-understood experimental systems that reveal fundamental mechanisms. Their power lies in their stark simplicity: the games strip social interaction down to its bare essence (one person has money and must decide how to share it) and generate behavior that directly contradicts the foundational assumption of economic theory.

In the ultimatum game, the subgame-perfect Nash equilibrium under self-interested preferences is clear: the proposer should offer the smallest possible amount (e.g., $1 out of $10), and the responder should accept because $1 is better than $0. This prediction fails spectacularly. Across hundreds of experiments in dozens of countries, modal offers cluster around 40-50% of the total. Offers below 20% are rejected about half the time. This pattern holds even when the stakes are raised to several months' wages (in developing-country replications), ruling out the hypothesis that people are fair only when the amounts are trivial.

The dictator game provides the critical control. By removing the responder's ability to reject, it eliminates the strategic motive for generosity. If ultimatum game offers are driven entirely by fear of rejection, dictator game offers should be zero. They are not. Mean dictator transfers are about 25-30% of the total, with significant heterogeneity — roughly a third give nothing, a third give 20-40%, and a smaller fraction give 50% or more. This demonstrates that at least some portion of giving in economic interactions reflects genuine other-regarding preferences rather than strategic calculation.

The rejection behavior in the ultimatum game is particularly revealing. Responders who reject low offers are sacrificing material payoffs to punish perceived unfairness — a form of "costly punishment" or "negative reciprocity." This behavior is difficult to reconcile with standard theory but makes sense under fairness models. In the Fehr-Schmidt inequality aversion model, responders suffer disutility from accepting a very unequal split, and if this disutility exceeds the material gain from accepting, rejection is utility-maximizing. Alternatively, responders may derive satisfaction from enforcing a fairness norm by punishing violators, even at a cost. The willingness to incur costs to punish is a powerful mechanism for sustaining cooperation in society.

Variations on these basic games have yielded further insights. Third-party punishment games show that uninvolved observers will pay to punish unfair allocations between others — indicating that fairness enforcement is not just a self-interested reaction to being shortchanged. Repeated games show that cooperation can be sustained through conditional strategies, with cooperation decaying when punishment is unavailable. Double-blind designs (where experimenters cannot identify individual choices) reduce but do not eliminate giving, suggesting that social image concerns contribute to but do not fully explain prosocial behavior. Together, this experimental program has built a detailed picture of human social motivation that informs theoretical models, organizational design, and public policy.
