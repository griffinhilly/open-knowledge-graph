---
id: pac-learning-framework
title: PAC Learning Framework
domain: computer-science
course: machine-learning-theory
prerequisites:
- id: supervised-learning-intro
  type: hard
- id: discrete-random-variables
  type: hard
- id: bayes-theorem
  type: soft
- id: bias-variance-tradeoff
  type: soft
tags:
- learning-theory
- computational-learning
- sample-complexity
stage: expert
status: validated
---

# PAC Learning Framework

## Core Idea
Probably Approximately Correct (PAC) learning, introduced by Leslie Valiant in 1984, formalizes what it means for a learning algorithm to succeed. A concept class is PAC-learnable if there exists an algorithm that, for any target concept in the class and any distribution over inputs, produces a hypothesis with error at most epsilon with probability at least 1 - delta, using a number of samples polynomial in 1/epsilon, 1/delta, and the representation size. This framework transforms the informal question "can we learn this?" into a precise mathematical statement about sample efficiency and computational feasibility.

## Questions

```yaml
- question: "A learning algorithm is given 500 training examples drawn i.i.d. from an unknown distribution and outputs a hypothesis with 3% test error. A colleague claims this proves the concept class is PAC-learnable. What is wrong with this claim?"
  type: multiple-choice
  options:
    - "500 examples is too few for any PAC guarantee — PAC learning requires at least 10,000 samples"
    - "PAC learnability is a property of the concept class and algorithm pair that must hold for ALL distributions and ALL target concepts, not just one empirical run"
    - "3% error is too high — PAC learning requires zero error on the test set"
    - "The claim is correct — achieving low error on a single run is sufficient to establish PAC learnability"
  answer: 1
  explanation: "PAC learnability is a worst-case guarantee over all possible distributions D and all target concepts c in the class. A single successful experiment shows the algorithm worked for one distribution and one target, but says nothing about whether it would succeed for adversarially chosen distributions or different targets. The 'probably' (1 - delta) and 'approximately' (epsilon) parameters must be achievable for any requested epsilon and delta, with sample complexity polynomial in 1/epsilon and 1/delta."

- question: "In the PAC framework, why does the sample complexity bound depend on 1/epsilon and 1/delta rather than on epsilon and delta directly?"
  type: multiple-choice
  options:
    - "It is a notational convention with no mathematical significance"
    - "Smaller epsilon (tighter accuracy) and smaller delta (higher confidence) are harder guarantees that require more data — the inverse relationship captures that more stringent requirements demand more samples"
    - "The dependence on 1/epsilon comes from Bayes' theorem and 1/delta comes from the central limit theorem"
    - "The inverse dependence ensures the bound goes to zero as the number of samples increases"
  answer: 1
  explanation: "Epsilon is the allowed error rate and delta is the allowed failure probability. Wanting lower error (smaller epsilon) or higher confidence (smaller delta) naturally requires more evidence. The sample complexity scales as O(1/epsilon) or O(1/epsilon^2) depending on the setting, and O(log(1/delta)) typically — reflecting that tightening accuracy is expensive while boosting confidence is relatively cheap (logarithmic). This inverse relationship is not a convention but a mathematical consequence of concentration inequalities."

- question: "PAC learning requires that the learning algorithm succeed for any distribution over the input space, including adversarially chosen ones."
  type: true-false
  answer: true
  explanation: "This is the distribution-free property of PAC learning. The algorithm must work without knowing or assuming anything about the distribution D that generates the data. The same algorithm must achieve the (epsilon, delta) guarantee whether D is uniform, Gaussian, concentrated on a few points, or any other distribution. This is a very strong requirement — it means the learner cannot exploit distributional assumptions. The tradeoff is that PAC bounds are often loose for specific 'nice' distributions precisely because they must hold in the worst case."

- question: "A concept class that requires exponential time to learn but only polynomial samples is considered PAC-learnable."
  type: true-false
  answer: false
  explanation: "PAC learnability requires both polynomial sample complexity AND polynomial computational complexity. The algorithm must run in time polynomial in 1/epsilon, 1/delta, and the size of the representation. A concept class that needs exponentially many computation steps — even if the number of training examples is polynomial — is not efficiently PAC-learnable. This computational requirement distinguishes PAC learning from purely statistical frameworks and connects learning theory to complexity theory."

- question: "Explain the role of the 'probably' and 'approximately' components in PAC learning and why both relaxations are necessary."
  type: short-answer
  answer: "The 'approximately' component (epsilon) allows the learned hypothesis to have small but nonzero error — it does not need to perfectly identify the target concept, only get within epsilon of it. The 'probably' component (delta) allows the algorithm to fail with small probability — on some unlucky draws of training data, the hypothesis may have error greater than epsilon, but this happens with probability at most delta. Both relaxations are necessary because learning from finite samples is inherently uncertain: any finite training set might be unrepresentative (justifying delta), and even a representative sample cannot perfectly pin down the target when hypothesis space is rich (justifying epsilon). Without the 'approximately' relaxation, only trivial concept classes would be learnable; without 'probably,' no finite sample could provide guarantees since there is always some probability of drawing a pathologically unrepresentative sample."
  explanation: "The two parameters give the framework its power and flexibility. Users can dial epsilon and delta to any desired level, paying in sample complexity. The framework then tells you exactly how many samples suffice. This parametric structure is what makes PAC learning a practical tool for reasoning about learning algorithms, not just an existence result."
```

## Explainer

Before the PAC framework, machine learning lacked a rigorous answer to a basic question: when can we say an algorithm has "learned" a concept? Empirical success on a test set is encouraging but proves nothing about future performance or worst-case behavior. Leslie Valiant's 1984 framework answered this by defining learning in terms of two tolerances — an accuracy parameter epsilon and a confidence parameter delta — and requiring that the algorithm's resource usage (both samples and computation) scale polynomially with the difficulty of the guarantee.

The formal setup works as follows. There is an unknown target concept c (a function mapping inputs to {0, 1}) drawn from a known concept class C, and an unknown distribution D over the input space. The learner receives m training examples drawn i.i.d. from D, each labeled by c. The learner must output a hypothesis h such that the probability of h disagreeing with c on a fresh random example from D is at most epsilon, and this guarantee must hold with probability at least 1 - delta over the random draw of the training set. A concept class C is PAC-learnable if there exists an algorithm and a function m(epsilon, delta) polynomial in 1/epsilon and 1/delta such that for every c in C and every D, drawing m(epsilon, delta) examples suffices.

The distribution-free requirement is crucial and often misunderstood. The same algorithm must work regardless of how inputs are distributed — it cannot assume data is Gaussian, uniform, or structured in any particular way. This makes PAC guarantees robust but conservative: real data often has exploitable structure, so PAC bounds can be pessimistic for benign distributions. The computational requirement is equally important: the algorithm must run in polynomial time, connecting learning theory directly to complexity theory. Some concept classes are "information-theoretically" learnable (enough samples exist) but not "computationally" learnable (no known polynomial-time algorithm can find the right hypothesis).

The PAC framework serves as the foundation for most of learning theory. The sample complexity bounds it produces — typically involving the VC dimension or other complexity measures of the hypothesis class — tell you how many examples are necessary and sufficient for learning. It also provides a clean separation between learnable and unlearnable concept classes: some classes (conjunctions, decision lists) are efficiently PAC-learnable, while others (general Boolean functions, certain cryptographic concepts) are provably not under standard complexity assumptions. This framework gives you the language and tools to ask precise questions about learnability, and every subsequent topic in this course builds on or extends the PAC model.
