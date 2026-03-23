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
status: validated
---

# Space Complexity: L, NL, and PSPACE

## Core Idea
Space complexity measures memory usage: L is log-space (useful for streaming), NL is nondeterministic log-space (path finding), PSPACE is polynomial space. Unlike time, space is reusable, so space classes have different hierarchies. PSPACE-complete problems include QBF (quantified Boolean formulas)—intractable despite polynomial space sufficing theoretically.

## Questions

```yaml
- question: "Why can a polynomial-space machine solve problems that seem to require exponential time?"
  type: multiple-choice
  options:
    - "Because PSPACE machines run faster than Turing machines by definition"
    - "Because space can be reused: a polynomial-space machine can execute exponentially many steps by revisiting configurations"
    - "Because polynomial space is equivalent to polynomial time due to compression"
    - "Because nondeterminism in PSPACE eliminates the need for most computation"
  answer: 1
  explanation: "The key insight is that space is reusable — once a machine finishes using a memory region, it can overwrite it. This means the number of distinct configurations of a machine using S(n) space is at most exponential (roughly 2^S(n) × n × state count). A PSPACE machine can run for exponentially many steps by cycling through exponentially many configurations, exploring an exponential search tree via depth-first traversal that reclaims memory at each backtrack. This is why QBF, a PSPACE-complete problem, seems to require exponential time but only polynomial space."

- question: "The canonical NL-complete problem is graph reachability. Why does this problem seem to require more than log space for a deterministic machine?"
  type: multiple-choice
  options:
    - "Because adjacency matrices require O(n²) storage for any graph"
    - "Because a deterministic machine must systematically explore all paths, seemingly requiring O(n) space to track visited nodes"
    - "Because graph reachability is actually in P but not in L"
    - "Because nondeterminism and determinism are equivalent for space complexity"
  answer: 1
  explanation: "To check reachability deterministically, a machine must avoid revisiting nodes (to terminate) and track which nodes have been visited — which requires O(n) space for an n-node graph. Nondeterministically, a machine can simply guess a path one node at a time, storing only the current node (O(log n) space to index n nodes). Savitch's theorem shows NL ⊆ L² (log²-space deterministically), which is better than O(n) but still not known to equal L. Whether L = NL remains open — it's the space analog of the P vs NP question."

- question: "Because space is reusable, PSPACE ⊆ P — any polynomial-space algorithm can be converted to a polynomial-time one."
  type: true-false
  answer: false
  explanation: "This reverses the known inclusion. P ⊆ PSPACE (any polynomial-time algorithm uses at most polynomial space since it can only write to polynomially many cells in poly time), but PSPACE is widely believed to be strictly larger than P. The fact that a PSPACE machine can execute exponentially many steps means it can explore search spaces that would take exponential time even with polynomial space — that is power, not a limitation. QBF (PSPACE-complete) is not known to be in P, and if it were, the polynomial hierarchy would collapse."

- question: "The space hierarchy theorem guarantees that L ≠ PSPACE, so at least one of the containments in L ⊆ NL ⊆ P ⊆ NP ⊆ PSPACE must be strict."
  type: true-false
  answer: true
  explanation: "The space hierarchy theorem states that more space strictly increases computational power: there exist problems solvable in O(n²) space but not O(n) space, and so on. Since log n is asymptotically smaller than any polynomial, L ≠ PSPACE is guaranteed by this theorem. This means the chain L ⊆ NL ⊆ P ⊆ NP ⊆ PSPACE contains at least one strict inclusion — but we don't know which. It's entirely possible (though not believed) that NL = P = NP while L ≠ NL and NP ⊊ PSPACE, or any other combination."

- question: "Explain why the relationship between nondeterministic and deterministic space complexity is much tighter than the corresponding relationship for time complexity."
  type: short-answer
  answer: "For space, Savitch's theorem proves that nondeterministic S(n) space can be simulated deterministically in S(n)² space — at most a quadratic blowup. For time, the best known simulation of nondeterministic time T(n) requires deterministic time roughly 2^T(n) — an exponential blowup. The difference comes from reusability: a deterministic simulation of a nondeterministic space-bounded machine can explore all nondeterministic branches by depth-first search, reusing the same space at each branch, incurring only a polynomial overhead in how the space is used."
  explanation: "The quadratic blowup from NL to L² seems strange — why not exponential? The key is that a nondeterministic computation path of length at most n through a space-S machine can be simulated by a divide-and-conquer approach: to check if state A reaches state B in 2^k steps, check if there's an intermediate state C reachable from A in 2^(k-1) steps and from which B is reachable in 2^(k-1) steps. Each level of recursion adds log-space overhead for bookkeeping, giving O(log²n) total. This is Savitch's elegant argument, and it has no time analog because time isn't reusable."
```

## Explainer

Time complexity asks "how many steps does a computation take?" Space complexity asks a different question: "how much memory does a computation need?" From your work on Savitch's theorem, you already know that the relationship between deterministic and nondeterministic space is tighter than the corresponding relationship for time. Space complexity classes formalize this by grouping problems according to how much work tape a Turing machine needs beyond the read-only input.

**L** (deterministic log-space) contains problems solvable using only O(log n) work tape cells. Since log n bits can only store a constant number of pointers into the input, L captures computations that scan the input while maintaining a bounded amount of bookkeeping — things like checking whether a string is a palindrome of a specific form, or testing basic properties of a graph given as an adjacency matrix. **NL** (nondeterministic log-space) allows nondeterministic choices with the same log-space restriction. The canonical NL-complete problem is **graph reachability**: given a directed graph, is there a path from node s to node t? A nondeterministic machine can guess the path one node at a time, needing only log-space to store the current node, but a deterministic machine seems to need more memory to systematically explore all paths.

**PSPACE** contains problems solvable with polynomial work space, regardless of time. This is a much larger class. The key insight is that space can be reused — once a computation finishes with a section of memory, it can overwrite it. This means a polynomial-space machine can run for exponentially many steps (since the number of distinct configurations is exponential in the space bound), exploring vast search trees by depth-first traversal that reclaims memory at each backtrack. The canonical PSPACE-complete problem is **QBF** (quantified Boolean formula satisfiability): given a Boolean formula with alternating universal and existential quantifiers, is it true? QBF generalizes SAT by adding "for all" quantifiers, and this alternation of quantifiers captures the back-and-forth reasoning that makes game-playing and planning problems computationally hard.

The known inclusions are L ⊆ NL ⊆ P ⊆ NP ⊆ PSPACE, and Savitch's theorem guarantees that NL ⊆ L² (deterministic log²-space) and more generally that nondeterministic space S(n) is contained in deterministic space S(n)². This quadratic blowup is remarkably small compared to the exponential gap we suspect between P and NP for time. Whether any of these inclusions are strict remains open, but we do know L ≠ PSPACE by the space hierarchy theorem — so at least one of the intermediate inclusions must be strict. Understanding these classes gives you a finer-grained map of computational difficulty than time complexity alone provides.
