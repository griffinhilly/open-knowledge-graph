---
id: online-learning-and-regret-bounds
title: Online Learning and Regret Bounds
domain: computer-science
course: machine-learning-theory
prerequisites:
- id: pac-learning-framework
  type: hard
- id: gradient-descent-optimization
  type: soft
- id: convex-optimization-fundamentals
  type: soft
tags:
- online-learning
- regret
- adversarial
- sequential-prediction
stage: expert
status: validated
---

# Online Learning and Regret Bounds

## Core Idea
Online learning is a sequential prediction framework where a learner makes decisions one at a time, observes a loss after each decision, and aims to minimize cumulative regret — the difference between the learner's total loss and the total loss of the best fixed strategy in hindsight. Unlike PAC learning, online learning makes no distributional assumptions: the sequence of examples can be adversarially chosen. The fundamental result is that O(sqrt(T)) regret is achievable and optimal for many problems, meaning the learner's average loss converges to the best fixed strategy's loss at rate 1/sqrt(T). This framework unifies prediction, optimization, and game theory.

## Questions

```yaml
- question: "After T = 10,000 rounds, an online learner has cumulative regret of 500 compared to the best expert. Is this good performance?"
  type: multiple-choice
  options:
    - "No — 500 regret means the learner made 500 more mistakes than the best expert"
    - "Yes — regret of 500 over 10,000 rounds means the average per-round regret is 0.05, and since optimal regret scales as sqrt(T) ≈ 100, the learner is performing within a constant factor of optimal"
    - "It depends entirely on the number of experts — with few experts, 500 is bad; with many, it is good"
    - "Regret of 500 is always considered large regardless of T"
  answer: 1
  explanation: "The benchmark is O(sqrt(T)) regret, which for T = 10,000 is about 100 (times a constant depending on the number of experts and the loss range). Regret of 500 is within a constant factor of this optimal rate. More importantly, the average regret per round is 500/10,000 = 0.05, which goes to zero — meaning the learner is converging to the performance of the best expert. In online learning, sublinear regret (o(T)) is the goal, and sqrt(T) is the achievable rate. Linear regret (proportional to T) would mean the learner is systematically worse and not improving."

- question: "Online learning with adversarial data sequences is strictly harder than PAC learning with i.i.d. data — any problem learnable online is also PAC-learnable, but not vice versa."
  type: true-false
  answer: false
  explanation: "The relationship is more nuanced than a simple hierarchy. Online learning and PAC learning are different frameworks with different guarantees. Some problems are learnable in both settings, some in one but not the other. Online learning does not require distributional assumptions (the adversary can choose any sequence), which makes it harder in one sense. But online learning only competes with the best fixed hypothesis in hindsight, while PAC learning guarantees low absolute error. For binary classification, online learnability (finite Littlestone dimension) is strictly more restrictive than PAC learnability (finite VC dimension) — there exist classes that are PAC-learnable but not online-learnable. So the relationship runs the other direction for classification."

- question: "O(sqrt(T)) regret is achievable for online convex optimization even against an adversary, but O(1) regret (bounded regret independent of T) is generally not achievable."
  type: true-false
  answer: true
  explanation: "The sqrt(T) regret rate is both achievable and optimal (up to constants) for most online learning problems with adversarial sequences. Achieving O(1) regret would mean the total excess loss is bounded regardless of how long the game continues — this is too much to ask against an adversary who can always present difficult examples. The sqrt(T) rate means the average regret per round is O(1/sqrt(T)), which goes to zero but the total grows without bound. Sublinear regret (o(T)) is the achievability boundary: it means the learner is 'no-regret' in the sense that the per-round average vanishes, even though the cumulative regret grows."

- question: "Explain why regret, rather than absolute loss, is the natural performance measure in online learning, and what it means for a learner to achieve sublinear regret."
  type: short-answer
  answer: "In online learning, an adversary chooses the loss sequence, so no learner can guarantee low absolute loss — the adversary can make every outcome costly. Regret measures performance relative to the best fixed strategy in hindsight, which is a fair benchmark because it asks: 'how much worse did you do compared to the best you could have done knowing everything in advance?' Sublinear regret (regret growing slower than T, typically as sqrt(T)) means the learner's average per-round performance converges to the best fixed strategy's. With regret R(T) = O(sqrt(T)), the average regret R(T)/T = O(1/sqrt(T)) -> 0, so the learner eventually matches the best expert's average loss rate. This is the strongest guarantee possible without distributional assumptions — you cannot guarantee being as good as the best expert on every round, but you can guarantee your average converges to theirs."
  explanation: "The regret framework also connects to game theory (minimax strategies), optimization (online gradient descent achieves sqrt(T) regret for convex losses), and statistics (prediction with expert advice). This universality makes it a foundational concept across theoretical computer science."
```

## Explainer

PAC learning assumes data is drawn i.i.d. from a fixed distribution — a strong assumption that may not hold in practice. Online learning drops this assumption entirely, operating in a sequential, potentially adversarial setting. The learner and the environment take turns: at each round t, the learner chooses an action (prediction, hypothesis, or strategy), the environment reveals a loss, and the learner updates. There are no distributional assumptions — the environment can be an adversary that chooses the worst possible sequence for the learner.

The performance measure in this adversarial setting cannot be absolute loss, because a sufficiently malicious adversary can impose high loss on any learner. Instead, the learner is measured by **regret**: the difference between its cumulative loss and the cumulative loss of the best fixed action in hindsight. Formally, Regret(T) = sum_{t=1}^{T} loss(learner_t) - min_{h in H} sum_{t=1}^{T} loss(h_t). The comparator is the single best fixed hypothesis over the entire sequence — the learner does not need to beat every hypothesis, just approach the best one's performance.

The central result is that O(sqrt(T)) regret is achievable for a wide class of problems. For prediction with expert advice (choosing among N experts each round), the Hedge algorithm achieves regret O(sqrt(T * ln N)). For online convex optimization (choosing a point in a convex set, then observing a convex loss), online gradient descent achieves regret O(sqrt(T)). These bounds hold against any adversary — no distributional assumption is needed. The sqrt(T) rate is also optimal: for most problems, no algorithm can achieve o(sqrt(T)) regret in the worst case.

The implications extend far beyond sequential prediction. Online learning algorithms can be converted to batch learning algorithms (online-to-batch conversion), providing an alternative route to generalization bounds that does not require uniform convergence. The regret framework also connects to game theory — no-regret strategies correspond to Nash equilibria in repeated games — and to optimization, where online gradient descent is the template for stochastic gradient descent. The framework's generality and adversarial robustness make it a cornerstone of modern theoretical machine learning, complementing the distributional assumptions of PAC learning with guarantees that hold in the worst case.
