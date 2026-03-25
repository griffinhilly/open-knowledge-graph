---
id: space-complexity-classes
title: 'Space Complexity: PSPACE, L, and NL'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: time-complexity-classes
  type: hard
- id: nondeterministic-complexity
  type: soft
- id: big-o-complexity-analysis
  type: soft
- id: asymptotic-notation-big-o-omega-theta
  type: soft
tags:
- PSPACE
- L
- NL
- space-complexity
- Savitch
stage: advanced
status: validated
---

# Space Complexity: PSPACE, L, and NL

## Core Idea
Space complexity classes measure memory usage rather than time. PSPACE contains problems solvable in polynomial space (e.g., quantified Boolean formula satisfiability, TQBF), and is known to contain NP and P. The class L consists of problems solvable in logarithmic space on a deterministic TM; NL uses nondeterministic log space. Savitch's theorem shows NPSPACE = PSPACE, meaning nondeterminism buys much less in space than it might in time. Space and time complexity interact deeply: PSPACE ⊆ EXPTIME, and P ⊆ NP ⊆ PSPACE, but most containments are strict.

## How It's Best Learned
Work through the TQBF PSPACE-completeness proof as the space analogue of Cook-Levin. Understand NL-completeness of graph reachability (ST-Connectivity) and how the Immerman-Szelepcsényi theorem shows NL = co-NL.

## Common Misconceptions
- Thinking PSPACE is just 'NP with more memory' — PSPACE is strictly larger than NP is believed to be, and contains problems like two-player game evaluation that seem qualitatively harder.
- Assuming Savitch's theorem applies to time — it is specific to space; nondeterminism can provide exponential time savings in theory.

## Questions

```yaml
- question: "Savitch's theorem states that NSPACE(f(n)) ⊆ DSPACE(f(n)²). What is the most important corollary of this theorem for polynomial space?"
  type: multiple-choice
  options:
    - "NP = P, because nondeterminism provides no advantage for polynomial-bounded computations"
    - "NPSPACE = PSPACE, because squaring a polynomial still yields a polynomial"
    - "PSPACE ⊆ NP, because any polynomial-space computation can be verified nondeterministically"
    - "L = NL, because squaring logarithm still gives a logarithm"
  answer: 1
  explanation: "Squaring a polynomial p(n) gives another polynomial p(n)², so NSPACE(p(n)) ⊆ DSPACE(p(n)²) places NPSPACE inside PSPACE — and since PSPACE ⊆ NPSPACE trivially, we get NPSPACE = PSPACE. This collapses nondeterministic and deterministic polynomial space together. Note that L and NL do NOT collapse under Savitch's theorem: squaring O(log n) gives O((log n)²) = O(log² n), which is a larger space class (DSPACE(log² n)), not O(log n) — so NL ⊆ DSPACE(log² n) but this doesn't prove NL = L."

- question: "Why is PSPACE believed to be strictly larger than NP, even though NP ⊆ PSPACE?"
  type: multiple-choice
  options:
    - "Because PSPACE problems require exponential time, which cannot be verified in polynomial time"
    - "Because PSPACE-complete problems like TQBF involve alternating quantifiers (∀ and ∃), while NP problems involve only existential quantifiers, suggesting qualitatively harder structure"
    - "Because PSPACE is closed under complement and NP is not, proving they differ"
    - "Because Savitch's theorem shows PSPACE has strictly more computational power than any nondeterministic class"
  answer: 1
  explanation: "PSPACE-complete problems like TQBF (True Quantified Boolean Formulas) involve alternating universal and existential quantifiers, modeling adversarial two-player games. A witness for an NP problem is a short certificate that a verifier checks — one party's move. TQBF requires evaluating game trees where both players play optimally, which seems to require exploring an exponentially large space of play sequences. NP captures 'someone can demonstrate a solution exists'; PSPACE captures 'we can determine the winner regardless of what the opponent does.' The qualitative difference in problem structure strongly suggests strict containment, though it remains unproven."

- question: "Savitch's theorem shows that nondeterminism provides no more than a quadratic advantage in space, unlike in time where nondeterminism might provide an exponential advantage."
  type: true-false
  answer: true
  explanation: "Savitch's theorem establishes NSPACE(f(n)) ⊆ DSPACE(f(n)²) — nondeterminism adds at most a quadratic cost in space. This contrasts sharply with time: we do not know whether nondeterminism provides an exponential advantage in time (the P vs NP question), but if NP ≠ P, it would. Intuitively, space can be reused (old tape cells can be overwritten) while time cannot — a computation that guesses and checks can reuse its workspace for each guess. This reusability is why nondeterminism is less powerful in space than it might be in time."

- question: "PSPACE is simply 'NP with more memory' — any NP problem can be efficiently solved using polynomial space."
  type: true-false
  answer: false
  explanation: "While NP ⊆ PSPACE (every NP problem can be solved in polynomial space — just simulate the nondeterministic machine using polynomial space), PSPACE is believed to be strictly larger than NP. PSPACE contains problems — like evaluating game positions with alternating play (TQBF is PSPACE-complete) — that are thought to be qualitatively harder than any NP problem. The phrase 'more memory' misses the point: PSPACE captures problems where the key difficulty is exploring an adversarial search space, not merely finding a single certificate whose existence witnesses a 'yes' answer."

- question: "In what ways does nondeterminism behave differently in space complexity than in time complexity, and what does Savitch's theorem tell us about this difference?"
  type: short-answer
  answer: "In time complexity, nondeterminism may provide an exponential speedup — this is the unsolved P vs NP question. In space complexity, Savitch's theorem shows nondeterminism provides at most a quadratic advantage: NSPACE(f(n)) ⊆ DSPACE(f(n)²). The reason is that space is reusable: a deterministic machine can simulate nondeterministic reachability by recursively checking whether a configuration is reachable in 2^k steps (checking both halves of a midpoint), reusing the same workspace across recursive calls. This recursion depth is only log(f(n)) deep, so the space cost is f(n)·log(f(n)) or f(n)², not exponential. Time cannot be similarly reused because each computation step is consumed irreversibly."
  explanation: "The contrast highlights a fundamental difference between time and space as computational resources. Space is a renewable resource — the same cells can be overwritten — while time flows in one direction. This makes space amenable to compression via reuse in a way time is not, collapsing the nondeterministic and deterministic polynomial-space classes (NPSPACE = PSPACE) while leaving the analogous time question (NP =? P) open."
```

## Explainer

From your study of time complexity, you know that P and NP classify problems by how much *time* a Turing machine needs. **Space complexity** asks a different question: how many tape cells does the machine use? This shift in resource leads to a different — and in some ways richer — hierarchy of complexity classes, because space can be reused (you can overwrite a tape cell) while time cannot be recovered.

**PSPACE** contains all problems solvable using a polynomial amount of memory, regardless of how long the computation takes. Its complete problem is **TQBF** (True Quantified Boolean Formulas): given a Boolean formula with alternating universal and existential quantifiers, determine whether it is true. Think of TQBF as a two-player game — one player tries to make the formula true, the other tries to make it false, and they alternate choosing variable assignments. This game-theoretic flavor is characteristic of PSPACE problems: evaluating game positions, planning under adversarial conditions, and verifying properties of systems with alternating control all tend to land in PSPACE. We know P ⊆ NP ⊆ PSPACE ⊆ EXPTIME, but whether any of these containments are strict remains open.

At the other end of the space spectrum, **L** (logarithmic space) contains problems solvable using only O(log n) bits of working memory beyond the read-only input. This is barely enough to store a constant number of pointers into the input. **NL** (nondeterministic log space) allows nondeterministic guessing on that same tiny workspace. The canonical NL-complete problem is **ST-Connectivity**: given a directed graph, is there a path from s to t? A nondeterministic machine can guess the path one node at a time, needing only enough memory to store the current node. A remarkable result — the **Immerman-Szelepcsényi theorem** — shows that NL = co-NL, meaning if you can nondeterministically verify reachability, you can also nondeterministically verify *non*-reachability in log space.

The most surprising structural result is **Savitch's theorem**: NSPACE(f(n)) ⊆ DSPACE(f(n)²). This means nondeterminism gives at most a quadratic advantage in space, unlike the potentially exponential advantage it might give in time (the P vs NP question). The proof is elegant — it uses a recursive divide-and-conquer strategy to check whether a configuration is reachable in 2^k steps by checking whether some midpoint configuration is reachable in 2^(k-1) steps from both ends. As an immediate corollary, NPSPACE = PSPACE, collapsing the nondeterministic and deterministic polynomial-space classes together. This contrasts sharply with time complexity, where NP and P are widely believed to differ.
