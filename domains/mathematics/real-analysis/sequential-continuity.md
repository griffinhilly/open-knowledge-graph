---
id: sequential-continuity
title: Sequential Characterization of Continuity
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-delta-continuity
  type: hard
- id: epsilon-n-convergence
  type: hard
builds-toward:
- uniform-convergence-preserves-continuity
tags:
- continuity
- sequences
- equivalence
stage: advanced
status: validated
---

# Sequential Characterization of Continuity

## Core Idea
A function f is continuous at c if and only if for every sequence (xₙ) with xₙ → c, we have f(xₙ) → f(c). This equivalence allows switching between ε-δ and sequential definitions: use sequences when natural, ε-δ when rigor demands it. The equivalence is a fundamental tool for proofs.

## How It's Best Learned
Prove f(x) = x² is continuous at 2 using both definitions, then use sequences to show f(x) = ⌊x⌋ is not continuous at integers.

## Common Misconceptions
- Assuming sequences must approach the continuity point monotonically or regularly; any convergent sequence works.
- Forgetting the 'if and only if': the equivalence works in both directions.
- Thinking sequential continuity is weaker; it is equivalent to ε-δ continuity in ℝ.

## Questions

```yaml
- question: "A student wants to prove that f(x) = ⌊x⌋ (the floor function) is discontinuous at x = 2. Which approach is most direct using sequential continuity?"
  type: multiple-choice
  options:
    - "Find ε > 0 and show no δ > 0 works by explicit case analysis"
    - "Show that every sequence converging to 2 has f(xₙ) not converging to 2"
    - "Exhibit a single sequence xₙ → 2 with f(xₙ) ↛ f(2)"
    - "Show f is not differentiable at 2, which implies discontinuity"
  answer: 2
  explanation: "Sequential continuity makes discontinuity easy to demonstrate: one counterexample sequence suffices. For example, xₙ = 2 − 1/n → 2, but f(xₙ) = 1 for all n, so f(xₙ) → 1 ≠ 2 = f(2). You do not need to show all sequences fail — a single bad sequence establishes discontinuity. The ε-δ approach would work but requires more case analysis."

- question: "Which statement correctly describes the relationship between sequential continuity and ε-δ continuity for real-valued functions on ℝ?"
  type: multiple-choice
  options:
    - "ε-δ continuity implies sequential continuity, but not vice versa"
    - "Sequential continuity implies ε-δ continuity, but not vice versa"
    - "They are logically equivalent — each implies the other"
    - "They agree on continuous functions but diverge on discontinuous ones"
  answer: 2
  explanation: "In ℝ (and all metric spaces), the two notions are exactly equivalent. This is the content of the sequential characterization theorem. A common misconception is that sequential continuity is weaker; it is not. Any discontinuity detectable by ε-δ is also detectable by a sequence, and vice versa. The equivalence holds in both directions."

- question: "To prove a function is continuous at c using sequential continuity, it suffices to find one specific sequence (xₙ) converging to c such that f(xₙ) → f(c)."
  type: true-false
  answer: false
  explanation: "To prove continuity, you must show that EVERY sequence converging to c has its image converge to f(c). Finding one well-behaved sequence is not enough — a function could behave well on some sequences but fail on others. To prove DISCONTINUITY, however, finding a single bad sequence does suffice."

- question: "The proof that sequential continuity implies ε-δ continuity is typically proved by contradiction: assume the function is not ε-δ continuous, then construct a sequence converging to c whose images do not converge to f(c)."
  type: true-false
  answer: true
  explanation: "The 'if' direction requires contradiction. Assuming f is not ε-δ continuous at c means: there exists ε > 0 such that for every δ > 0 = 1/n, some xₙ satisfies |xₙ − c| < 1/n but |f(xₙ) − f(c)| ≥ ε. This constructs a sequence xₙ → c with f(xₙ) ↛ f(c), contradicting the sequential hypothesis. This direction is the more surprising and instructive of the two."

- question: "Explain in your own words why the sequential characterization of continuity is a valuable proof tool, even though it is logically equivalent to the ε-δ definition."
  type: short-answer
  answer: "The equivalence means you can choose whichever formulation is more convenient. Sequences are especially natural for disproving continuity (one counterexample sequence suffices), for Bolzano-Weierstrass arguments, and for reasoning about limits of compositions. The ε-δ formulation is often cleaner when constructing explicit bounds or proving continuity directly. The value is flexibility: the same mathematical content can be accessed in whichever form the problem makes most tractable."
  explanation: "Neither form is more powerful — they are equivalent. But a proof that is awkward in one language may be transparent in the other. Recognizing which mode fits the problem is itself a mathematical skill."
```

## Explainer

You already have two tools: the ε-δ definition of continuity and the ε-N definition of sequence convergence. **Sequential continuity** is the bridge between them — it says that continuous functions and convergent sequences commute: you can take the function inside the limit. Formally, f is continuous at c if and only if, for every sequence (xₙ) converging to c, the sequence (f(xₙ)) converges to f(c). This is not a new concept layered on top of continuity — it is an exact restatement of what ε-δ continuity means, translated into sequential language.

The "only if" direction is the one most students master first: if f is ε-δ continuous at c and xₙ → c, then f(xₙ) → f(c). The proof is clean — given ε > 0, find δ from continuity, then use the convergence of xₙ to find N such that |xₙ − c| < δ for n ≥ N. The "if" direction — proving ε-δ continuity from the sequential condition — requires a proof by contradiction and is typically more surprising: assume f is *not* ε-δ continuous at c, construct a sequence xₙ → c with f(xₙ) ↛ f(c), contradicting the hypothesis.

The power of sequential continuity is in how it lets you choose your proof style to match the problem. The floor function ⌊x⌋ provides the clearest example of the sequential approach for *disproving* continuity: at any integer n, take the sequence xₙ = n − 1/n, which converges to n from below. Then f(xₙ) = n − 1 for all n, so f(xₙ) → n − 1 ≠ n = f(n). One sequence, one counterexample, proof complete. Doing the same job with ε-δ requires careful case analysis around the specific integer.

Sequences are particularly natural when working with limits of compositions, limits of function sequences, or arguments involving Bolzano-Weierstrass. If a proof begins "let (xₙ) be any sequence converging to c," you are in sequential mode. The equivalence guarantees that any conclusion you reach — continuity or discontinuity — is as rigorous as any ε-δ argument. The skill is recognizing which mode is cleaner for the problem at hand.
