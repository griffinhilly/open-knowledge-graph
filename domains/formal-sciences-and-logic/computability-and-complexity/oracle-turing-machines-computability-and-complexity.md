---
id: oracle-turing-machines-computability-and-complexity
title: Oracle Turing Machines
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: hard
- id: halting-problem-formal
  type: hard
builds-toward:
- turing-degrees
- arithmetical-hierarchy
tags:
- computability
- oracles
- relativized-computation
stage: formal-systems
status: draft
---

# Oracle Turing Machines

## Core Idea
An oracle Turing machine is a standard Turing machine augmented with a black-box oracle for some decision problem — it can query the oracle and receive an answer in a single step, regardless of the problem's actual complexity. Oracle machines formalize "relative computability": what could be computed if a particular problem were solvable for free. The oracle hierarchy, built by iterating the halting oracle (K, K', K'', ...), produces a strict hierarchy of unsolvable problems. Baker, Gill, and Solovay showed that relativized results can go either way for P vs NP, demonstrating that any proof resolving P vs NP must use non-relativizing techniques.

## How It's Best Learned
Start with a concrete oracle — the halting problem K — and show how a TM with oracle K can decide problems that no ordinary TM can, such as the totality problem. Then construct K' (the halting problem relativized to K) and show it is strictly harder than K. This iterated construction makes the arithmetical hierarchy tangible.

## Common Misconceptions
- An oracle does not make the machine "more powerful" in an absolute sense — it makes it more powerful relative to a specific problem, and different oracles yield different computational landscapes.
- Oracle results do not automatically transfer to the unrelativized world — the Baker-Gill-Solovay theorem shows there exist oracles where P = NP and others where P != NP.
