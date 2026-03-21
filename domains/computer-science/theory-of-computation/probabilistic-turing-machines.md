---
id: probabilistic-turing-machines
title: Probabilistic Turing Machines
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machines
  type: hard
- id: nondeterministic-finite-automata
  type: soft
builds-toward:
- bpp-complexity-class
- rp-corp-complexity
tags:
- randomization
- probabilistic-computation
stage: advanced
status: draft
---

# Probabilistic Turing Machines

## Core Idea
A probabilistic Turing machine (PTM) is a nondeterministic TM where each branch is taken with specified probability. Unlike NTM (existential: accept if any branch succeeds), PTM explores branches stochastically. A PTM decides a language L with error probability ε if for x ∈ L it accepts with probability ≥ 1-ε and for x ∉ L it rejects with probability ≥ 1-ε. PTMs formalize randomized algorithms and enable analysis of error probability via amplification.

## Questions

```yaml
- question: "A nondeterministic Turing machine (NTM) and a probabilistic Turing machine (PTM) both branch into multiple computational paths. What is the fundamental difference in how they determine acceptance?"
  type: multiple-choice
  options:
    - "NTMs use randomness to choose branches; PTMs explore all branches systematically"
    - "NTMs accept if any single branch accepts (existential); PTMs accept if a sufficiently large fraction of branches accept (statistical)"
    - "NTMs are faster because they find the accepting branch immediately; PTMs must run all branches"
    - "PTMs and NTMs accept by the same criterion but differ only in whether they can be simulated efficiently"
  answer: 1
  explanation: "The distinction is existential vs. statistical acceptance. An NTM asks: does *any* computation path accept? One accepting branch is enough. A PTM asks: does a *large enough fraction* of random computation paths accept? This is why PTMs are said to 'decide' a language with bounded error probability — the fraction of accepting branches must exceed a threshold (e.g., 2/3) for yes-instances and fall below it (e.g., 1/3) for no-instances. Option A has it backwards — PTMs use randomness, NTMs use existential nondeterminism."

- question: "A randomized algorithm for a decision problem gives the correct answer with probability 2/3 on each independent run. An engineer runs it 100 times and takes a majority vote. What happens to the probability of a wrong majority answer?"
  type: multiple-choice
  options:
    - "It stays at 1/3, because the underlying error probability of each run is fixed at 1/3"
    - "It increases, because running more trials compounds the chances of encountering errors"
    - "It drops exponentially — the probability of a wrong majority answer becomes negligibly small"
    - "It decreases linearly to approximately 1/300, each run contributing an equal reduction"
  answer: 2
  explanation: "This is probability amplification. For a majority of 100 runs to be wrong, more than 50 runs must individually err. Since each run errs independently with probability 1/3 < 1/2, the probability that a majority err is bounded by the Chernoff bound and drops exponentially in the number of runs. With 100 runs, the error probability is far below 2^{−50}. The key insight: because each run's error probability is below 1/2, more independent runs make it exponentially harder for errors to dominate."

- question: "A probabilistic Turing machine's error probability can be reduced to an arbitrarily small level by running it multiple times independently and taking a majority vote."
  type: true-false
  answer: true
  explanation: "True — this is the probability amplification theorem. As long as each independent run has bounded error probability ε < 1/2, running k runs and taking the majority vote reduces the probability of a wrong answer exponentially in k. This is why the specific error threshold (2/3, 3/4, 0.99) in the definition of PTMs doesn't fundamentally matter — any constant advantage over 1/2 can be amplified to essentially 1."

- question: "Probabilistic Turing machines are strictly more computationally powerful than deterministic Turing machines — they can decide languages that no deterministic TM can decide."
  type: true-false
  answer: false
  explanation: "False — this conflates computational power (what can be decided at all) with efficiency (what can be decided in polynomial time). PTMs and deterministic TMs decide the same set of languages in principle; a PTM cannot solve the halting problem or decide any undecidable language. The open question is whether randomness helps with *efficiency*: does BPP = P? Most theorists believe it does, meaning every problem solvable efficiently with randomness also has an efficient deterministic algorithm. PTMs don't expand what is decidable — they may (or may not) expand what is feasibly tractable."

- question: "Why is probability amplification central to the usefulness of probabilistic Turing machines? What property of the error probability makes it work?"
  type: short-answer
  answer: "Amplification works because independent runs' errors are uncorrelated. For the majority vote to be wrong, more than half of k independent runs must err simultaneously. If each run has error probability ε < 1/2, the probability that a majority err falls exponentially in k (by the Chernoff bound). The crucial property is that ε < 1/2 — if errors occurred more than half the time, majority voting would amplify mistakes. Because the algorithm is correct more often than not on each run, accumulating independent samples drives error probability to zero exponentially fast."
  explanation: "This is why the '2/3' threshold in PTM definitions is not special: any constant advantage over random guessing (any ε < 1/2) suffices for amplification to work. The amplification technique means a 51% correct algorithm can be boosted to 1 − 2^{−100} correct with polynomial overhead, which is why the exact error bound in the definition of BPP doesn't matter."
```

## Explainer

You already know that a standard Turing machine follows a single deterministic path of computation, and that a nondeterministic TM can branch into many paths simultaneously (accepting if any branch accepts). A **probabilistic Turing machine** sits between these two models: at each step where multiple transitions are possible, the machine flips a coin to decide which branch to follow. Instead of exploring all branches or just one, it randomly walks through one computational path — and that randomness turns out to be surprisingly powerful.

The key difference from nondeterminism is how acceptance works. A nondeterministic TM asks an existential question: "does *some* branch accept?" A probabilistic TM asks a statistical question: "does a *large fraction* of branches accept?" Formally, a PTM decides a language with bounded error if it gives the correct answer with probability at least 2/3 (or any constant greater than 1/2). The specific threshold doesn't matter much, because of a technique called **probability amplification**: if you run the machine many times independently and take a majority vote, the error probability drops exponentially. Run it 100 times, and the chance of a wrong majority answer becomes astronomically small.

This model formalizes real randomized algorithms you may encounter in practice. The Miller-Rabin primality test, for example, can determine whether a number is prime with high probability in polynomial time — something that was not known to be achievable deterministically until much later (and the deterministic algorithm is slower in practice). Randomized quicksort, random sampling algorithms, and many graph algorithms exploit the same idea: a little randomness can make hard problems tractable or make algorithms faster on average.

PTMs give rise to important complexity classes like **BPP** (bounded-error probabilistic polynomial time), which captures problems solvable efficiently with randomness and two-sided error, and **RP** (randomized polynomial time), where errors occur only on one side. Whether BPP equals P — whether randomness actually helps — remains an open question, though most complexity theorists conjecture that it does not, meaning every efficient randomized algorithm has an efficient deterministic counterpart we just haven't found yet.
