---
id: lottery-ticket-hypothesis
title: Lottery Ticket Hypothesis
domain: computer-science
course: machine-learning-theory
prerequisites:
- id: neural-network-approximation-theory
  type: hard
- id: regularization-theory
  type: hard
- id: overparameterization-theory
  type: soft
tags:
- network-pruning
- sparsity
- lottery-ticket
- overparameterization
stage: expert
status: validated
---

# Lottery Ticket Hypothesis

## Core Idea
The Lottery Ticket Hypothesis (LTH), proposed by Frankle and Carbin (2019), posits that dense neural networks contain sparse subnetworks ("winning lottery tickets") that, when trained in isolation from random initialization, achieve test accuracy comparable to the original dense network. A winning ticket is found by training a dense network, pruning low-magnitude weights, and training the remaining weights from their original initialization (not from scratch). This suggests that dense networks redundantly encode multiple possible solutions; training initializes an implicit lottery where some random initializations hit a winning ticket. LTH has profound implications for neural network structure, generalization, and optimization efficiency.

## Questions

```yaml
- question: "In the Lottery Ticket Hypothesis, what is a 'winning ticket'?"
  type: multiple-choice
  options:
    - "A dense network that achieves 100% training accuracy"
    - "A sparse subnetwork that, trained from its original weights at original initialization, reaches comparable test accuracy to the original dense network"
    - "A subset of training data that, if used alone, allows perfect generalization"
    - "A random initialization that guarantees fast convergence"
  answer: 1
  explanation: "A winning ticket is a sparse, well-chosen subnetwork that retains its original weight initialization from the dense network. The critical point is training from the original initialization, not from scratch. Training the same subnetwork topology from scratch (random initialization) typically fails to achieve good performance, showing that the original initialization is crucial. This distinguishes lottery ticket pruning from other pruning methods and suggests that random initialization holds information."

- question: "The lottery ticket hypothesis claims that pruning weights AFTER training and retraining from the SAME initialization recovers performance. Why is training from the original initialization important?"
  type: short-answer
  answer: "If you retrain a pruned subnetwork from a fresh random initialization, it often performs poorly. Training from the original initialization works because that initialization was already compatible with the pruned subnetwork structure — the original initialization implicitly 'chose' which subnetwork to develop. This suggests that random initialization is not truly random but contains implicit structure that biases optimization toward certain solutions. The hypothesis proposes that the dense network, starting from a fixed initialization, had multiple possible paths (winning tickets), and training selected one. Retraining from the same initialization is rewinding to the fork in the road where the original dense training made its choice."
  explanation: "This touches on a deep question: what makes some initializations 'winners' and others 'losers'? The original initialization must encode information that guides optimization toward good solutions. This is a profound finding because it suggests random initialization is not truly uninformative — it constrains the optimization landscape in beneficial ways."

- question: "How does the Lottery Ticket Hypothesis relate to overparameterization and generalization?"
  type: multiple-choice
  options:
    - "LTH proves that overparameterization is harmful and causes overfitting"
    - "LTH suggests that overparameterization provides redundancy; the network contains multiple generalizing solutions, and optimization selects one via implicit regularization"
    - "LTH has no connection to overparameterization; it is purely about network pruning"
    - "LTH shows that sparse networks always generalize better than dense networks"
  answer: 1
  explanation: "LTH offers a new perspective on why overparameterized networks generalize: they contain embedded redundancy. A dense network can be thought of as encoding many possible sparse subnetworks, all capable of solving the task. The optimization process (gradient descent on the dense network) selects one subnetwork to develop by setting weights to large values while keeping others near zero. The selected subnetwork generalizes because implicit regularization during dense training ensures the winning ticket inherits good generalization properties. This resolves the puzzle of overfitting: overparameterization provides flexibility that, combined with the right optimization algorithm, allows finding simple (sparse) solutions."

- question: "True or False: You can take a pruned lottery ticket subnetwork, randomly shuffle the weights, and retrain from the shuffled initialization while achieving the original dense network's performance."
  type: true-false
  answer: false
  explanation: "False. The lottery ticket hypothesis specifically requires training from the original initialization. Random shuffling destroys the implicit information encoded in the original initialization. This highlights that LTH is not just about pruning to remove redundancy — it is about preserving the specific initialization that enables efficient learning of the winning subnetwork. This is a key distinction and suggests that optimization and initialization are deeply entangled."
```

## Explainer

The Lottery Ticket Hypothesis challenges how we think about neural network training and pruning. The classical view treats network training as a search for weights that minimize loss. Dense networks are often pruned after training by removing low-magnitude weights, reducing parameters and computation. The lottery ticket hypothesis reframes this: dense networks are not learning machines in the traditional sense but **lottery ticket machines** that identify which of many embedded subnetworks can be developed efficiently.

The experimental protocol is elegant. Start with a dense network randomly initialized with weights w^0. Train it to convergence on a task, obtaining weights w^t*. Identify a pruning mask m (binary, selecting which weights to keep) by selecting high-magnitude weights. Define the "winning ticket" as the subnetwork g(theta_0 ⊙ m), where ⊙ is element-wise multiplication. Crucially, retrain this subnetwork from the original initialization w^0 ⊙ m, not from scratch, and it recovers the original dense network's performance.

Why is this surprising? First, traditional wisdom says retraining a pruned network requires fresh random initialization; starting from pruned dense weights (even at the original magnitude) often performs worse. LTH shows that the solution is to restore weights to their original initialization while keeping the pruning mask. Second, retraining the same pruned topology from a different random initialization fails, suggesting the original random seed encodes useful structure.

LTH has several profound implications. It suggests that **randomness in initialization is not truly noise but encodes inductive biases**. Different random seeds induce different winning tickets; some seeds are naturally "luckier" than others. It also reframes overparameterization: dense networks contain many subnetworks, and optimization selects one. This selection happens implicitly through gradient descent, which has an implicit bias toward sparse, generalizing solutions (implicit regularization). The hypothesis unifies the success of overparameterized networks with the efficiency of sparse models: you need the overparameterization to find good sparse solutions, but the actual solution is sparse.

Practical implications are significant. If LTH holds, you can dramatically reduce network size and computation by first training dense, then pruning and retraining from the original initialization. This is a form of "progressive shrinking" where you train a large model and extract a smaller, more efficient subnetwork. However, the dense training cost is not reduced, so the practical speedup is limited to inference and storage.

Limitations and open questions remain. LTH has been verified empirically for image classification, but results are more mixed for other domains (NLP, other architectures). The hypothesis fails at very high pruning levels (>99% of weights removed), and the "rewinding" procedure (returning to the original initialization) is non-trivial. Theoretically, explaining *why* the original initialization is special remains open. The mechanism by which sparse subnetworks with original weights can match dense network performance, and what properties of the initialization allow this, are frontiers of research.

The Lottery Ticket Hypothesis has spawned follow-up research on training dynamics, edge rewinding (finding winning tickets earlier in training), and various pruning strategies. It stands as a reminder that deep learning contains structural surprises: dense networks are not monolithic learners but collections of possible learners, and optimization selects among them through mechanisms still not fully understood.
