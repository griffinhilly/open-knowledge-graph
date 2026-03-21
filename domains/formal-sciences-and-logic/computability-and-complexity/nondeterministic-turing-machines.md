---
id: nondeterministic-turing-machines
title: Nondeterministic Turing Machines
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: hard
- id: time-complexity-classes-formal
  type: soft
builds-toward:
- np-and-polynomial-time
- space-complexity-classes-formal
tags:
- computation
- nondeterminism
- automata
- complexity
stage: advanced
status: validated
---

# Nondeterministic Turing Machines

## Core Idea
A nondeterministic Turing machine (NTM) has a transition relation rather than a function, allowing multiple possible moves at each step. An NTM accepts an input if *some* branch of its computation tree accepts. Any NTM can be simulated by a deterministic TM, but at an exponential cost in time — the deterministic machine must explore the entire computation tree. This exponential simulation gap is the heart of the P vs. NP question: can nondeterminism for polynomial-time computation always be eliminated without super-polynomial cost?

## How It's Best Learned
Visualize NTM computation as a tree of computation paths, with acceptance defined by the existence of an accepting leaf. Then prove the simulation theorem: a DTM simulates an NTM running in time t(n) in time 2^O(t(n)) by BFS over the computation tree.

## Common Misconceptions
- Nondeterminism is not probabilistic computation; an NTM accepts if *any* branch accepts, whereas a probabilistic TM accepts based on the fraction of accepting branches.
- NTMs are not more computationally powerful than DTMs in terms of *what* they compute (same Turing-computable functions), only potentially in *how efficiently* they compute.

## Questions

```yaml
- question: "An NTM is given an input and runs. One branch of its computation accepts, but 999 other branches reject. What does the NTM do?"
  type: multiple-choice
  options:
    - "It rejects, since the majority of branches reject"
    - "It accepts, since at least one branch accepts"
    - "It accepts with probability 0.1%, since 1 of 1000 branches accepts"
    - "The result is undefined — NTMs require all branches to agree"
  answer: 1
  explanation: "By definition, an NTM accepts if *any* branch of its computation tree accepts. Rejection requires *all* branches to reject (or loop). This is a logical OR over all branches, not a vote or a probability. A probabilistic TM would accept based on the fraction of accepting branches (option C describes BPP-style computation), but that is a different computational model. The NTM is asking: 'does a solution exist?' not 'how many solutions exist?' This is why NP is naturally characterized by NTMs — NP problems have a 'guess-and-verify' structure where one correct guess suffices."

- question: "Which of the following best describes what an NTM adds beyond the power of a DTM?"
  type: multiple-choice
  options:
    - "It can compute functions that a DTM cannot — it solves undecidable problems"
    - "It can decide the halting problem, which a DTM cannot"
    - "It potentially solves certain problems faster (in fewer steps), but computes the same set of functions as a DTM"
    - "It eliminates the need for exponential time by parallelizing computation physically"
  answer: 2
  explanation: "NTMs and DTMs are equivalent in computability — they decide exactly the same set of languages (both characterize Turing-computable functions). An NTM cannot solve the halting problem or any undecidable problem. What NTMs potentially offer is an *efficiency* advantage: an NTM might decide a problem in polynomial time that a DTM requires exponential time to decide. Whether this gap is real for NP vs P problems is precisely the P vs. NP question. Option D misunderstands NTMs as physical parallel computers — they are a theoretical model, not a description of real hardware."

- question: "A nondeterministic Turing machine is just a Turing machine that makes random choices between transitions."
  type: true-false
  answer: false
  explanation: "This is the most important misconception about NTMs. A *probabilistic* Turing machine makes random choices, and its acceptance is defined by the probability of accepting branches. An NTM accepts if *any* branch accepts — there is no randomness or probability. Nondeterminism is a theoretical abstraction for 'existential choice': the machine is defined to succeed if there *exists* a sequence of choices leading to acceptance, regardless of how likely or unlikely any single branch is. NTMs and probabilistic TMs define different complexity classes (NP vs. BPP) and answer different questions."

- question: "An NTM that runs in polynomial time can always be simulated by a DTM in polynomial time."
  type: true-false
  answer: false
  explanation: "This is exactly what the P vs. NP question asks — and the answer is unknown. What we do know is that a DTM can simulate an NTM running in time t(n) in time 2^{O(t(n))} by performing BFS over the computation tree. This simulation is exponentially expensive. If the NTM runs in polynomial time (NP), the DTM simulation costs exponential time. Whether there is always a polynomial-time DTM equivalent is the central open problem in computer science."

- question: "Why is the computation tree the right way to visualize NTM execution, and how does the acceptance condition connect to NP problems in practice?"
  type: short-answer
  answer: "An NTM's execution is not a single timeline but a branching tree: at each step where multiple transitions are possible, the machine splits into all possibilities simultaneously. The root is the initial configuration; each path through the tree is one possible sequence of choices. The NTM accepts if any leaf is an accepting state. This models NP problems naturally because NP problems have a 'guess-and-verify' structure: an NTM can nondeterministically guess a candidate solution (one path) and then verify it in polynomial time. If even one guess-path leads to acceptance (a correct solution), the NTM accepts. The difficulty of simulating this with a DTM is that the DTM must search all paths, not just find one."
  explanation: "The tree visualization makes clear why BFS simulation is expensive: the tree can have exponentially many nodes. It also makes clear why acceptance is 'existential' — the NTM is equivalent to asking 'does an accepting leaf exist?' not 'how many accepting leaves exist?' The SAT problem fits perfectly: an NTM guesses a truth assignment (one path down the tree) and verifies it (the rest of that path) — if any assignment satisfies the formula, one branch accepts."
```

## Explainer

You already know that a **deterministic Turing machine (DTM)** processes its input one step at a time, with each configuration uniquely determining the next move. A **nondeterministic Turing machine (NTM)** relaxes this: at each step, the machine may have several valid transitions available. The right mental model is not a single thread of computation but a **computation tree** — the root is the initial configuration, and each node branches into all possible next steps. The NTM accepts an input if *at least one* leaf in this tree is an accepting state. Rejection requires every branch to reject or loop.

This definition captures a natural abstraction for search problems. Consider checking whether a Boolean formula is satisfiable (the SAT problem): an NTM can nondeterministically "guess" a truth assignment in one step and then verify it in polynomial time. The NTM doesn't enumerate all assignments one by one — it explores all branches simultaneously in the abstract model. This is precisely why **NP** (nondeterministic polynomial time) is defined as the class of problems decidable by NTMs in polynomial time: each problem in NP has a polynomial-time "guess-and-verify" structure that corresponds naturally to an NTM computation.

A critical distinction: an NTM is not a **probabilistic Turing machine**. A probabilistic TM accepts based on the fraction of branches that accept — it models randomized algorithms. An NTM accepts if *any* branch accepts — it is a logical OR over all branches, finding the "best case" outcome. Nondeterminism is a theoretical tool for characterizing problem complexity, not a description of actual random computation. The complexity class BPP (bounded-error probabilistic polynomial time) captures probabilistic computation; NP captures nondeterministic computation. These are different classes.

Any NTM can be simulated by a DTM by **breadth-first search** over the computation tree: the deterministic machine systematically explores all branches level by level. If the NTM runs in time t(n), its computation tree has depth t(n) and at most some constant branching factor b, yielding at most b^{t(n)} nodes total. The DTM must visit all of them, so the simulation costs 2^{O(t(n))} time — an exponential blowup. Whether this blowup is unavoidable is the P vs. NP question: can every NP problem (solvable by an NTM in polynomial time) also be solved by a DTM in polynomial time? No one knows. The NTM is, in essence, the formal model whose expressive power the entire P vs. NP question is about.
