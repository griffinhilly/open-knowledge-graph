---
id: busy-beaver-function
title: Busy Beaver Function and Non-Computability
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: hard
- id: halting-problem-formal
  type: hard
- id: undecidability-and-godel
  type: soft
tags:
- non-computability
- undecidability
- functions
stage: advanced
status: draft
---

# Busy Beaver Function and Non-Computability

## Core Idea
The busy beaver function BB(n) is the maximum number of steps a halting n-state Turing machine can take on a blank tape. BB is non-computable: no Turing machine can compute BB(n) for all n. Because computing BB would require solving the halting problem, busy beavers demonstrate that even well-defined integer sequences can be uncomputable, illustrating fundamental limits of computation.

## Explainer

From your study of Turing machines, you know a Turing machine with n states can behave in enormously varied ways. Fix the simplest interesting case: all n-state, 2-symbol Turing machines that start on a blank tape. Some of these will run forever; others will halt. Among those that halt, some do so quickly, others after many steps. The **busy beaver function** BB(n) picks out the winner: the maximum number of steps taken by any n-state, 2-symbol Turing machine that eventually halts. It is a purely combinatorial, completely well-defined integer sequence — BB(1) = 1, BB(2) = 6, BB(3) = 21, BB(4) = 107. Yet BB(5) is already in the tens of millions, BB(6) likely exceeds 10↑↑15, and the sequence grows faster than any computable function.

The non-computability of BB follows directly from the halting problem you already know. Suppose, for contradiction, that there were a Turing machine C that computed BB(n) for all n. Given any n-state Turing machine M, you could compute BB(n) via C, then simulate M for exactly BB(n) steps. If M has not halted after BB(n) steps, it never will — by definition of BB(n). This would decide the halting problem for all n-state machines, which you know is impossible. Therefore C cannot exist: BB is **not computable** by any Turing machine, even though every value BB(n) is a perfectly well-defined natural number.

This is the conceptual shock: non-computability is not about being poorly defined or infinite. BB(5) is a specific integer — researchers have bounded it with great effort — but no uniform algorithm can produce BB(n) for arbitrary n. The function grows faster than any computable function, faster than any tower of exponentials you can write down. If f is any computable function, then BB(n) > f(n) for all sufficiently large n. This is a hierarchy result: BB sits strictly above the entire computable universe in the growth-rate ordering.

The busy beaver also has a remarkable side-effect: it provides a reduction between mathematical undecidability and concrete machine behavior. Rado, who defined the busy beaver in 1962, showed that BB gives a precise yardstick for undecidability. For each consistent extension of ZF set theory, there exists a specific n such that ZF cannot prove the exact value of BB(n). Every time mathematicians settle BB(n) for a new n, they are, in a precise sense, extending the reach of formal arithmetic — and the values they cannot settle mark the edge of the provable. Gödel's incompleteness theorem, which you may know as an abstract existence result, thus has a concrete, computational face in the busy beaver sequence.

The broader lesson is a strengthening of the halting problem's meaning. The halting problem showed that there is no algorithm for a specific decision task. The busy beaver shows that non-computability is not a narrow exception — entire regions of mathematics are computationally unreachable, not because the objects are ill-defined, but because computation itself has fundamental ceiling limits on what it can calculate.

