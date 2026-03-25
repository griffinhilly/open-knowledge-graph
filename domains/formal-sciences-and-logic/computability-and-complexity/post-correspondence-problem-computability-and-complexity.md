---
id: post-correspondence-problem-computability-and-complexity
title: Post Correspondence Problem
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: halting-problem-formal
  type: hard
- id: computability-reductions
  type: soft
- id: regular-expressions-and-languages
  type: soft
tags:
- computability
- undecidability
- formal-languages
stage: advanced
status: validated
---
# Post Correspondence Problem

## Core Idea
The Post Correspondence Problem (PCP) asks, given a finite set of domino-like pairs of strings (u_i, v_i), whether there exists a nonempty sequence of indices i_1, ..., i_k such that u_{i_1}...u_{i_k} = v_{i_1}...v_{i_k}. Despite its deceptively simple formulation, PCP is undecidable — there is no algorithm that can solve it for all instances. PCP is a workhorse for proving undecidability of other problems: many undecidability results in formal language theory (ambiguity of CFGs, equivalence of CFGs) are established by reduction from PCP rather than directly from the halting problem.

## How It's Best Learned
Work through small PCP instances by hand — some with solutions and some without — to develop intuition for the matching constraint. Then study the reduction from the halting problem to PCP, which encodes a TM computation as a growing sequence of domino matches. Finally, see how PCP is reduced to prove undecidability of CFG ambiguity.

## Common Misconceptions
- PCP is undecidable in general, but specific restricted variants (e.g., over a unary alphabet, or with only two pairs under certain constraints) may be decidable.
- The difficulty is not finding a short solution — it is that no algorithm can determine whether any solution exists at all, regardless of length.

## Questions

```yaml
- question: "An engineer builds a program to solve the Post Correspondence Problem: it searches all domino sequences of length 1, 2, 3, … in order and reports 'no solution exists' if no match is found after 10¹⁰⁰ steps. Why is this not a correct decision procedure for PCP?"
  type: multiple-choice
  options:
    - "The algorithm is too slow for practical use — a correct algorithm would need to run in polynomial time"
    - "A valid matching sequence might have length 10¹⁰⁰ + 1 or longer — there is no finite bound N such that the absence of a solution of length at most N certifies that no solution exists at all"
    - "The algorithm does not check all permutations of each length, only sequences in a fixed order"
    - "PCP is only undecidable for instances with more than 7 string pairs; the algorithm works correctly on small instances"
  answer: 1
  explanation: "Undecidability is not about speed — it is about the impossibility of a correct algorithm for all instances. The algorithm above is correct whenever a solution exists (it will eventually find it), but it fails on instances with no solution: it reports 'no solution' after 10¹⁰⁰ steps, but the real answer might still be 'a solution exists' at a greater length. Since there is no bound on the minimum solution length (it can be arbitrarily large even when a solution exists), no finite cutoff can serve as a reliable certificate of non-existence. This 'no finite witness of failure' is the structural reason PCP is undecidable."

- question: "Why is the Post Correspondence Problem especially useful as an intermediate step for proving undecidability results in formal language theory, rather than always reducing directly from the halting problem?"
  type: multiple-choice
  options:
    - "Because the halting problem is decidable in special cases where PCP is not, making PCP a stronger reduction source"
    - "Because PCP's clean combinatorial structure — matching string sequences — is much easier to embed into formal language problems such as CFG ambiguity than full Turing machine computation histories"
    - "Because PCP is more computationally complex than the halting problem, making reductions from it yield stronger undecidability results"
    - "Because formal language proofs require reductions that operate only on context-free grammars, not Turing machines"
  answer: 1
  explanation: "Reducing from the halting problem to a new problem requires encoding TM computations into the new domain, which is complex and TM-specific. PCP is already proved undecidable via the halting problem (done once), and its structure — does any sequence of dominoes produce a matching top-bottom string? — maps naturally into questions about formal languages. Proving CFG ambiguity or CFG equivalence undecidable via PCP only requires showing how to encode a PCP instance as a grammar construction, which is shorter and cleaner. PCP acts as a laundered form of undecidability: the messiness of TM encodings is hidden in the PCP construction once, and all downstream reductions start from that clean domino-matching formulation."

- question: "The Post Correspondence Problem is undecidable in general, but restricted to instances over a unary alphabet (strings built from a single symbol), it becomes decidable."
  type: true-false
  answer: true
  explanation: "This illustrates that undecidability is a property of the general problem, not every restricted variant. Over a unary alphabet, the matching condition reduces to an integer equation: do there exist positive integers n₁, …, n_k (the domino indices) such that the sum of top-string lengths equals the sum of bottom-string lengths? This is a system of linear Diophantine equations, which is decidable. Undecidability of general PCP relies on the ability to encode arbitrary computations in string structure — something a unary alphabet cannot do."

- question: "The undecidability of PCP means that PCP instances are simply too computationally hard for current computers — a sufficiently powerful future computer could solve all instances."
  type: true-false
  answer: false
  explanation: "Undecidability is not a statement about computational resources. An undecidable problem cannot be solved by any algorithm regardless of speed or memory, because no algorithm can produce a correct yes/no answer on all instances. For PCP, the issue is that no algorithm can correctly distinguish all solvable instances from all unsolvable ones in principle — not because the computation takes too long, but because the problem has no algorithmic decision procedure. A computer running for the lifetime of the universe still could not decide all PCP instances correctly."

- question: "Why does the 'no finite witness of failure' property explain why no algorithm can decide PCP, and what makes this property characteristic of undecidable problems more generally?"
  type: short-answer
  answer: "For a 'yes' instance of PCP, there is a finite witness of success: the matching sequence itself, which can be verified in polynomial time by checking that top strings concatenate to the same string as bottom strings. But for a 'no' instance, there is no finite object that certifies the absence of any solution. If no sequence of length 1 through N matches, a solution could still exist at length N+1, N+2, or arbitrarily longer — there is no structural property of PCP instances that bounds the minimum solution length or rules out longer solutions. Any algorithm that stops at a finite bound will sometimes classify a solvable instance as unsolvable. This is characteristic of undecidable problems: the negative direction lacks a verifiable certificate. By contrast, decidable problems like graph connectivity have short certificates for both yes (a connected spanning tree) and no (a separating cut), allowing exhaustive search to terminate."
  explanation: "This 'no certificate of failure' structure separates undecidable problems from NP-hard ones: NP-hard problems have efficiently verifiable yes-certificates (solutions), so even if finding them is hard, verification works. Undecidable problems lack even this guarantee for one direction."
```

## Explainer

From the halting problem, you know that some questions about computation have no algorithmic answer — no matter how clever your program, it cannot decide whether an arbitrary Turing machine halts on an arbitrary input. The Post Correspondence Problem is a second, structurally simpler-looking problem that is also undecidable, and its value lies precisely in that simplicity. Because PCP is undecidable and involves nothing more than matching strings, it makes an efficient stepping stone for proving other problems undecidable without always tracing a path back through Turing machine encodings.

The setup is this: you are given a finite collection of **dominoes**, each with a top string and a bottom string — for example, [ab/a], [b/ba], [a/bab]. Your task is to pick a nonempty sequence of these dominoes (with repetition allowed) such that reading all the top strings in order yields exactly the same string as reading all the bottom strings in order. For the example above, the sequence [ab/a], [b/ba], [ab/a], [b/ba] gives top = "ab" + "b" + "ab" + "b" = "abbabb" and bottom = "a" + "ba" + "a" + "ba" = "abaaba" — not a match. Finding a match requires trial and error, and the length of the solution sequence can be astronomically large even when a solution exists.

The undecidability proof shows that if you could solve PCP, you could solve the halting problem — a contradiction. The reduction works by encoding a Turing machine's computation history as a PCP instance. Each step of the TM's computation corresponds to a domino designed so that a valid matching sequence spells out a valid sequence of configuration snapshots: the full history from start to halt. The top strings spell out one phase of the computation and the bottom strings spell out the next, and a solution exists exactly when the machine halts. Because constructing this reduction is mechanical, a PCP solver would become a halting problem solver, which we know is impossible.

PCP's real utility is as a **reduction intermediate**. Many problems in formal language theory — does a context-free grammar generate an ambiguous language? Are two context-free grammars equivalent? — are proved undecidable by reducing PCP to them rather than going directly from the halting problem. The reductions are shorter because PCP has a cleaner combinatorial structure than Turing machine computations. You can think of PCP as a "laundered" form of undecidability: the messiness of TM encodings has been pushed into the PCP construction once, and all downstream reductions start from that clean domino-matching form.

The key intuition for why no algorithm can solve PCP is that the search space has no exploitable bound. If no solution exists among sequences of length up to k, a solution might still exist at length k+1. There is no certificate of non-existence to check, no structural property that rules out longer solutions, and no depth at which you can safely stop searching. This "no finite witness of failure" structure is characteristic of undecidable problems and is worth recognizing as a general pattern: deciding that something cannot happen, over an infinite search space, is the hard direction.

