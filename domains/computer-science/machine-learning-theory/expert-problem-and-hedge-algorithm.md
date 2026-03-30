---
id: expert-problem-and-hedge-algorithm
title: Expert Problem and Hedge Algorithm
domain: computer-science
course: machine-learning-theory
prerequisites:
- id: multiplicative-weights-method
  type: hard
- id: online-learning-and-regret-bounds
  type: hard
- id: discrete-random-variables-basics
  type: soft
tags:
- online-learning
- experts
- hedge
- prediction
stage: expert
status: validated
---

# Expert Problem and Hedge Algorithm

## Core Idea
The expert problem is the canonical online learning setting: at each round, a learner must choose among N experts' advice, then suffers the loss of the chosen expert. The goal is to achieve cumulative loss close to the best expert in hindsight. The Hedge algorithm (also called the exponential weights algorithm) solves this by maintaining a probability distribution over experts, updated multiplicatively: p_i^{(t+1)} proportional to p_i^{(t)} * exp(-eta * loss_i^{(t)}). Hedge achieves regret O(sqrt(T * ln N)), which is optimal — no algorithm can do better against an adversary. The expert problem serves as the theoretical foundation for ensemble methods, model selection, and boosting.

## Questions

```yaml
- question: "You have N = 100 experts and must predict for T = 10,000 rounds. What is the optimal learning rate for Hedge, and what regret can you expect?"
  type: multiple-choice
  options:
    - "eta = 1/T = 0.0001, achieving regret O(T/ln(N)) ≈ 2,170"
    - "eta = sqrt(ln(N)/T) = sqrt(ln(100)/10000) ≈ 0.021, achieving regret O(sqrt(T * ln N)) ≈ sqrt(10000 * 4.6) ≈ 215"
    - "eta = 1/sqrt(N) ≈ 0.1, achieving regret O(sqrt(N * T)) ≈ 1,000"
    - "eta = ln(N)/T ≈ 0.00046, achieving regret O(T * sqrt(ln(N)/T)) ≈ 215"
  answer: 1
  explanation: "The optimal learning rate for Hedge is eta = sqrt(ln(N)/T), which minimizes the regret bound. Plugging in: eta = sqrt(4.6/10000) ≈ 0.021. The resulting regret is 2 * sqrt(T * ln(N)) = 2 * sqrt(10000 * 4.6) ≈ 2 * 214 ≈ 428. The O() hides constants, but the scaling is sqrt(T * ln N) ≈ 215 (times a constant). This means the learner's average loss per round exceeds the best expert's by only about 0.04 — essentially matching the best expert's performance over 10,000 rounds, despite not knowing which expert is best in advance."

- question: "The Hedge algorithm requires knowing the time horizon T in advance to set the optimal learning rate. Without this knowledge, the algorithm cannot achieve sublinear regret."
  type: true-false
  answer: false
  explanation: "While the optimal eta = sqrt(ln(N)/T) does require knowing T, the 'doubling trick' eliminates this requirement. The idea: run Hedge with eta optimized for T = 1, then restart with eta optimized for T = 2, then T = 4, 8, 16, and so on, doubling the horizon each time. The total regret across all epochs is at most a constant factor worse than knowing T in advance, still achieving O(sqrt(T * ln N)). Alternatively, a time-varying learning rate eta_t = sqrt(ln(N)/t) (decreasing with t) achieves the same bound without restarts. Sublinear regret is achievable without foreknowledge of the horizon."

- question: "If all N experts have identical cumulative loss after T rounds, the Hedge algorithm's regret is zero."
  type: true-false
  answer: true
  explanation: "Regret is defined as the learner's cumulative loss minus the best expert's cumulative loss. If all experts have the same cumulative loss L, the best expert also has loss L. The Hedge learner, who randomizes over experts, has expected cumulative loss equal to a weighted average of expert losses. Since all expert losses are equal, the learner's expected loss each round equals each expert's loss, giving cumulative loss L. Regret = L - L = 0. This makes intuitive sense: when all experts are equally good, there is nothing to learn, and any strategy — including uniform randomization — achieves zero regret."

- question: "Explain why the regret bound for the expert problem scales with ln(N) rather than N, and what this means for practical applicability with large expert pools."
  type: short-answer
  answer: "The logarithmic dependence on N comes from the multiplicative weight structure. Each expert starts with weight 1/N, so the initial 'cost' of including an expert is ln(N) in the potential function analysis (the log of the total weight). As the algorithm runs, it only needs to distinguish the best expert from the rest — it does not need to individually estimate each expert's quality. The multiplicative update naturally concentrates weight on good experts exponentially fast, and the regret analysis tracks the ratio of the total weight to the best expert's weight, which involves ln(N) rather than N. Practically, this means Hedge scales extraordinarily well: with N = 1,000,000 experts, the regret only increases by a factor of sqrt(ln(10^6)/ln(10)) ≈ 2.4 compared to N = 10. You can include a massive pool of candidate strategies with minimal cost."
  explanation: "This logarithmic scaling is why the expert problem framework is practical for model selection: you can combine thousands of base models with Hedge-like algorithms, and the regret penalty for including a bad model is negligible. The cost of having more options is essentially free."
```

## Explainer

The expert problem is the simplest and most fundamental setting in online learning. Each round, N experts offer advice (implicitly, through their predicted actions), the learner chooses one or randomizes among them, and then nature reveals the outcome and each expert's loss. The learner's goal is to minimize regret — the gap between its cumulative loss and the best expert's cumulative loss in hindsight. No assumptions are made about how the losses are generated; they could be adversarial.

The Hedge algorithm solves this problem optimally. It maintains a weight w_i for each expert, initialized to 1. At each round: assign probability p_i = w_i / sum_j w_j to expert i, sample an expert according to this distribution (or play the mixed strategy directly if losses are linear), observe all experts' losses, and update w_i <- w_i * exp(-eta * loss_i). The exponential update is the defining feature: experts with high loss see their weights decrease exponentially, while low-loss experts maintain or increase their relative weight. Over time, the distribution concentrates on consistently good experts.

The regret analysis uses a potential function argument. Define Phi_t = ln(sum_i w_i^{(t)}). The potential decreases each round by at least eta * (learner's expected loss) - eta^2 (a second-order correction). At the end, the potential is at least ln(w_best^{(T)}) = -eta * (best expert's total loss). Combining the upper and lower bounds on the potential change gives: learner's loss <= best expert's loss + (ln N)/eta + eta * T. The optimal eta = sqrt(ln(N)/T) balances these terms, yielding regret 2 * sqrt(T * ln N).

The O(sqrt(T * ln N)) regret bound is optimal — a matching lower bound shows no algorithm can achieve o(sqrt(T * ln N)) regret in the worst case. The logarithmic dependence on N is remarkable and practically important: the cost of including additional experts is negligible. This makes the expert framework a natural foundation for ensemble methods (combine many base learners), model selection (compete with a pool of candidate models), and online portfolio selection (compete with the best stock in hindsight). The Hedge algorithm also serves as the template for more sophisticated online learning algorithms — online mirror descent generalizes Hedge from discrete experts to continuous action spaces, inheriting its optimal regret guarantees.
