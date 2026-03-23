---
id: complexity-class-p-definition
title: 'Complexity Class P: Polynomial Time'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: p-vs-np-problem
  type: hard
- id: time-complexity-classes
  type: soft
- id: asymptotic-notation-big-o-omega-theta
  type: soft
builds-toward:
- complexity-class-np-definition
tags:
- p-class
- polynomial-time
- tractable
- efficient
- definition
stage: advanced
status: validated
---

# Complexity Class P: Polynomial Time

## Core Idea
The class P contains languages decided by deterministic TMs in polynomial time. P represents problems solvable efficiently in theory (sorting, shortest paths, primality testing). P is robust: all standard polynomial-time models (RAM, circuits, multi-tape TMs) agree on P due to polynomial equivalence. P is widely believed tractable; whether P = NP is the central open problem in CS.

## Questions

```yaml
- question: "An algorithm for a decision problem runs in O(n^100) time on inputs of length n. Which of the following is correct?"
  type: multiple-choice
  options:
    - "The problem is not in P because n^100 grows too fast to be considered efficient"
    - "The problem is in P, but this tells us nothing about whether the algorithm is practical"
    - "The problem is in P and is therefore efficiently solvable for large inputs"
    - "Whether the problem is in P depends on the specific machine model used to run the algorithm"
  answer: 1
  explanation: "P is defined by the existence of a polynomial-time algorithm, not by practical efficiency. n^100 is a polynomial, so the problem is in P. But P membership does not guarantee practicality — n^100 is completely useless for any real input. The significance of P is theoretical robustness and a robust threshold for tractability, not a guarantee that polynomial = fast. This is the central misconception the definition is designed to resist."

- question: "Why is 'polynomial time' specifically chosen as the defining boundary for class P, rather than a more restrictive class like O(n²) or O(n log n)?"
  type: multiple-choice
  options:
    - "Polynomial time was chosen because most practical algorithms run in quadratic or sub-quadratic time"
    - "The polynomial boundary is closed under composition and is model-independent: a polynomial of a polynomial is still a polynomial, and all standard computational models agree on it"
    - "Polynomial time was chosen by convention after Cobham's thesis, without strong theoretical justification"
    - "The boundary corresponds exactly to problems solvable on physical hardware within the age of the universe"
  answer: 1
  explanation: "The key property is robustness. Polynomials are closed under composition: if algorithm A calls subroutine B, and both run in polynomial time, the whole thing runs in polynomial time. More importantly, switching between standard computational models (single-tape TM, multi-tape TM, RAM) can multiply running time by a polynomial factor — but a polynomial times a polynomial is still a polynomial. This makes P invariant across all standard models of deterministic computation, unlike any fixed bound like O(n²)."

- question: "A problem in P can always be solved efficiently in practice, regardless of the degree of the polynomial."
  type: true-false
  answer: false
  explanation: "P membership is a theoretical classification, not a practical guarantee. An algorithm running in n^50 time is in P but completely impractical for any non-trivial input. The importance of P is its robustness as a complexity class — the fact that polynomial time is model-independent and closed under composition — not that all polynomial-time algorithms are fast. In practice, algorithms with degree > 4 or 5 are often replaced by heuristics."

- question: "If a problem is shown to be in P using a multi-tape Turing machine, it is also in P for a single-tape Turing machine."
  type: true-false
  answer: true
  explanation: "This is precisely the robustness property of P. Converting a multi-tape TM to a single-tape TM can square the running time, but a polynomial squared is still a polynomial. All standard deterministic models of computation — single-tape TMs, multi-tape TMs, random-access machines, Boolean circuits — agree on which problems are in P. This model-independence is what makes P a fundamental class rather than an artifact of one particular machine model."

- question: "What is the theoretical significance of P, given that some problems in P (like one running in n^100 time) are completely impractical?"
  type: short-answer
  answer: "P's significance is its robustness as a complexity class: it is closed under composition, closed under simulation between standard computational models, and captures a stable, model-independent notion of efficient computability. It forms a meaningful boundary because all standard deterministic models agree on it, and it contrasts sharply with problems requiring exponential time. P is a theoretical threshold, not a practical guarantee — it rules out inherent intractability even if the constant or degree matters enormously in practice."
  explanation: "The point of P is to identify problems that can be solved by a systematic deterministic procedure (not brute-force search), as opposed to problems like NP-complete ones that seem to require exponential exploration. The contrast between P and NP — between finding and verifying — is where P's definition earns its keep. Whether P = NP is the most important open problem in CS precisely because the distinction between these two classes is so fundamental."
```

## Explainer

From your study of time complexity and Big-O notation, you know how to measure the growth rate of an algorithm's running time as a function of input size. **The complexity class P** draws a line in the sand: it contains exactly those decision problems (yes/no questions) that can be solved by a deterministic Turing machine in time bounded by some polynomial function of the input length. If the input has n bits, a problem is in P if there exists an algorithm that always halts with the correct answer in at most n^k steps for some fixed constant k — whether that is n², n³, or n^100.

The polynomial boundary is not chosen because polynomial-time algorithms are always fast in practice. An algorithm running in n^50 time is technically in P but completely impractical. The significance of P is **theoretical robustness**. Every reasonable model of deterministic computation — single-tape Turing machines, multi-tape machines, random-access machines, Boolean circuits — agrees on which problems are polynomial-time solvable. Switching between these models may square or cube the running time, but a polynomial of a polynomial is still a polynomial. This means P is not an artifact of one particular machine model; it captures something fundamental about what is efficiently computable.

Concrete problems in P anchor the abstraction. Sorting an array of n elements takes O(n log n) time — solidly polynomial. Finding the shortest path in a graph with n nodes and m edges takes O(n² ) or O(m + n log n) depending on the algorithm. Testing whether a number with n digits is prime was proved to be in P by the AKS algorithm in 2002, settling a long-standing question. Linear programming, matching in bipartite graphs, and determining whether two strings are anagrams are all in P. What unites them is the existence of a step-by-step procedure that systematically reaches the answer without needing to guess or explore exponentially many possibilities.

The importance of P becomes clear when contrasted with problems that appear to resist polynomial-time solution. Many natural problems — scheduling, graph coloring, Boolean satisfiability — seem to require brute-force search over exponentially many candidates. These problems sit in the class NP, where solutions can be *verified* quickly but (as far as anyone knows) not *found* quickly. Whether P equals NP — whether every problem whose solution can be checked in polynomial time can also be *solved* in polynomial time — is the most important open question in theoretical computer science. If P = NP, the distinction between finding and verifying would collapse, with profound consequences for cryptography, optimization, and mathematics itself.
