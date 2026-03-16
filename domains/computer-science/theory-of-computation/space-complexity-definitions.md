---
id: space-complexity-definitions
title: 'Space Complexity: L, NL, and PSPACE'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: boolean-satisfiability-and-reductions
  type: soft
- id: space-complexity-and-savitch-theorem
  type: hard
builds-toward:
- savitch-theorem-and-implications
tags:
- space-complexity
- log-space
- pspace
- l
- nl
- definitions
stage: advanced
status: draft
---

# Space Complexity: L, NL, and PSPACE

## Core Idea
Space complexity measures memory usage: L is log-space (useful for streaming), NL is nondeterministic log-space (path finding), PSPACE is polynomial space. Unlike time, space is reusable, so space classes have different hierarchies. PSPACE-complete problems include QBF (quantified Boolean formulas)—intractable despite polynomial space sufficing theoretically.

## Explainer

Time complexity asks "how many steps does a computation take?" Space complexity asks a different question: "how much memory does a computation need?" From your work on Savitch's theorem, you already know that the relationship between deterministic and nondeterministic space is tighter than the corresponding relationship for time. Space complexity classes formalize this by grouping problems according to how much work tape a Turing machine needs beyond the read-only input.

**L** (deterministic log-space) contains problems solvable using only O(log n) work tape cells. Since log n bits can only store a constant number of pointers into the input, L captures computations that scan the input while maintaining a bounded amount of bookkeeping — things like checking whether a string is a palindrome of a specific form, or testing basic properties of a graph given as an adjacency matrix. **NL** (nondeterministic log-space) allows nondeterministic choices with the same log-space restriction. The canonical NL-complete problem is **graph reachability**: given a directed graph, is there a path from node s to node t? A nondeterministic machine can guess the path one node at a time, needing only log-space to store the current node, but a deterministic machine seems to need more memory to systematically explore all paths.

**PSPACE** contains problems solvable with polynomial work space, regardless of time. This is a much larger class. The key insight is that space can be reused — once a computation finishes with a section of memory, it can overwrite it. This means a polynomial-space machine can run for exponentially many steps (since the number of distinct configurations is exponential in the space bound), exploring vast search trees by depth-first traversal that reclaims memory at each backtrack. The canonical PSPACE-complete problem is **QBF** (quantified Boolean formula satisfiability): given a Boolean formula with alternating universal and existential quantifiers, is it true? QBF generalizes SAT by adding "for all" quantifiers, and this alternation of quantifiers captures the back-and-forth reasoning that makes game-playing and planning problems computationally hard.

The known inclusions are L ⊆ NL ⊆ P ⊆ NP ⊆ PSPACE, and Savitch's theorem guarantees that NL ⊆ L² (deterministic log²-space) and more generally that nondeterministic space S(n) is contained in deterministic space S(n)². This quadratic blowup is remarkably small compared to the exponential gap we suspect between P and NP for time. Whether any of these inclusions are strict remains open, but we do know L ≠ PSPACE by the space hierarchy theorem — so at least one of the intermediate inclusions must be strict. Understanding these classes gives you a finer-grained map of computational difficulty than time complexity alone provides.
