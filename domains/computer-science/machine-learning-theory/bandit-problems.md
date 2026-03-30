---
id: bandit-problems
title: Bandit Problems (Multi-Armed Bandits)
domain: computer-science
course: machine-learning-theory
prerequisites:
- id: online-learning-and-regret-bounds
  type: hard
- id: concentration-inequalities
  type: hard
- id: expected-value
  type: soft
- id: bayes-theorem
  type: soft
tags:
- bandits
- exploration-exploitation
- online-learning
- sequential-decisions
stage: expert
status: validated
---

# Bandit Problems (Multi-Armed Bandits)

## Core Idea
The multi-armed bandit problem is an online learning setting with partial feedback: after choosing an action (pulling an arm), the learner observes only the reward of the chosen arm, not the rewards of the other arms. This creates the exploration-exploitation dilemma — the learner must try different arms to estimate their rewards (explore) while also pulling the arm it believes is best to accumulate reward (exploit). The UCB (Upper Confidence Bound) algorithm achieves O(sqrt(KT * ln T)) regret over T rounds with K arms by choosing the arm with the highest upper confidence bound on its mean reward. The minimax optimal regret for K-armed bandits is Theta(sqrt(KT)), showing that partial feedback costs a sqrt(K) factor compared to the full-information expert setting.

## Questions

```yaml
- question: "In the multi-armed bandit setting, why can't you simply use the Hedge algorithm from the full-information expert problem?"
  type: multiple-choice
  options:
    - "Hedge requires continuous loss values, but bandits only produce binary rewards"
    - "Hedge updates weights for ALL experts each round, but in bandits you only observe the reward of the chosen arm — you lack the information to update the weights of unchosen arms"
    - "Hedge has higher computational complexity than bandit algorithms"
    - "Hedge assumes the losses are adversarial, but bandit problems assume stochastic rewards"
  answer: 1
  explanation: "The fundamental difference between the expert setting and the bandit setting is the information structure. In the expert setting (full information), you observe the loss of every expert each round, allowing you to update all weights. In the bandit setting (partial feedback), you only observe the reward of the arm you pulled. The Hedge update requires knowing all experts' losses — information that is unavailable in the bandit setting. To bridge this gap, bandit algorithms like EXP3 use importance-weighted estimators to construct unbiased estimates of the unseen losses, but these estimates have higher variance, which is why bandit regret is higher (sqrt(KT) vs sqrt(T ln K))."

- question: "The UCB1 algorithm selects the arm with the highest value of (empirical mean + sqrt(2 * ln(t) / n_i)), where n_i is the number of times arm i has been pulled. What does the second term accomplish?"
  type: multiple-choice
  options:
    - "It adds random noise to encourage exploration in early rounds"
    - "It is a confidence bonus that is larger for arms that have been pulled fewer times, ensuring that under-explored arms are given a fair chance — implementing 'optimism in the face of uncertainty'"
    - "It penalizes arms that have been pulled too often to prevent over-exploitation"
    - "It corrects for the bias in the empirical mean estimate when sample sizes are small"
  answer: 1
  explanation: "The sqrt(2 * ln(t) / n_i) term is an upper confidence bound derived from Hoeffding's inequality. For arms that have been pulled many times (large n_i), this term is small — the empirical mean is reliable and exploration is less needed. For rarely-pulled arms (small n_i), the term is large — there is high uncertainty about the arm's true mean, and the algorithm gives it the benefit of the doubt by adding a large bonus. This 'optimism in the face of uncertainty' principle ensures every arm is explored enough to get a reliable estimate, while concentrating pulls on the arm that is genuinely best once estimates become accurate."

- question: "In a stochastic K-armed bandit, the minimax optimal regret is Theta(sqrt(KT)), while in the full-information setting with K experts it is Theta(sqrt(T ln K)). The extra sqrt(K/ln K) factor is the price of partial feedback."
  type: true-false
  answer: true
  explanation: "The gap between sqrt(KT) and sqrt(T ln K) is precisely the information cost of the bandit setting. In the full-information setting, you observe all K experts' losses each round, giving K data points per round. In the bandit setting, you observe only 1 reward per round, so after T rounds you have T total observations spread across K arms — roughly T/K per arm. This K-fold information deficit per arm translates to the sqrt(K) factor in the regret. The ln K term in the full-information bound becomes sqrt(K) because you must actually pull each arm to learn about it, rather than passively observing."

- question: "Explain the exploration-exploitation dilemma in bandits and why it does not arise in the full-information expert setting."
  type: short-answer
  answer: "In bandits, the learner only observes the reward of the chosen arm. To learn about an arm's quality, you must pull it — there is no other way to gain information. But pulling a suboptimal arm incurs opportunity cost (you forgo the reward of the best arm). This creates a dilemma: exploration (pulling arms to learn their rewards) directly conflicts with exploitation (pulling the arm you believe is best). In the full-information expert setting, this dilemma does not exist because you observe all experts' losses every round regardless of which expert you follow. Information about every expert is free — it arrives whether you use that expert or not. The learner never needs to sacrifice reward to gain information, so there is no exploration cost."
  explanation: "The exploration-exploitation dilemma is the defining feature that separates bandits from full-information online learning. Every bandit algorithm must manage this tradeoff, and the different approaches — optimism (UCB), randomization (Thompson sampling), information-theoretic (EXP3) — represent different strategies for balancing information acquisition against reward maximization."
```

## Explainer

The multi-armed bandit problem, named after a gambler facing a row of slot machines (one-armed bandits), captures a dilemma that pervades sequential decision-making: you must balance exploring options you know little about against exploiting the option you currently believe is best. The partial-feedback structure — you only learn the outcome of actions you take — is what makes bandits fundamentally different from (and harder than) the full-information expert problem.

In the stochastic setting, each arm i has an unknown mean reward mu_i, and pulling arm i yields a random reward drawn from a distribution with mean mu_i. The UCB1 algorithm handles this elegantly through the principle of "optimism in the face of uncertainty." At each round t, it pulls the arm maximizing mean_hat_i + sqrt(2 * ln(t) / n_i), where mean_hat_i is the empirical mean reward of arm i and n_i is the number of times it has been pulled. The confidence bonus sqrt(2 * ln(t) / n_i) is wide for under-explored arms and narrow for well-explored ones. This automatically balances exploration and exploitation: uncertain arms get a generous bonus that ensures they are tried, while well-understood suboptimal arms have their bonus shrink below the best arm's empirical mean.

UCB1 achieves regret O(sqrt(KT * ln T)), which is near-optimal — the minimax lower bound is Theta(sqrt(KT)). The logarithmic factor can be removed with more sophisticated algorithms. In the adversarial setting (where rewards are chosen by an adversary, not drawn from fixed distributions), the EXP3 algorithm extends the Hedge approach using importance-weighted reward estimates. Since the learner only observes the reward of the chosen arm, EXP3 constructs unbiased estimates by dividing the observed reward by the probability of having chosen that arm. These estimates are noisier than full-information observations, which is the fundamental reason adversarial bandit regret is sqrt(KT) rather than the expert setting's sqrt(T ln K).

The bandit framework has enormous practical reach. Clinical trials must balance testing treatments against assigning patients to the best-known treatment. Online advertising must decide which ad to show while learning click-through rates. Recommendation systems must balance showing familiar content against discovering new preferences. In each case, the partial-feedback structure and the exploration-exploitation tradeoff are the core challenges. Thompson sampling (a Bayesian approach that samples from the posterior distribution of each arm's mean) has emerged as a practical favorite, often matching UCB's theoretical guarantees with better empirical performance and more natural uncertainty quantification through the Bayesian prior.
