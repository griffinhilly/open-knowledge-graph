---
id: counterexamples-and-disproofs
title: Counterexamples and Disproofs
domain: mathematics
course: methods-of-proof
prerequisites:
- id: predicates-and-quantifiers-intro
  type: hard
- id: proof-structure-terminology
  type: soft
tags:
- proof
- counterexample
- negation
stage: formal-systems
status: validated
---

# Counterexamples and Disproofs

## Core Idea
To disprove a universal statement 'For all x, P(x)', we need only find a single counterexample where P(x) is false. A counterexample is a concrete instance proving the statement false. Disproofs by counterexample are often simpler than constructing positive proofs and are the primary tool for showing that conjectures are false.

## Questions

```yaml
- question: "A mathematician conjectures: 'For any positive integers a and b, if a divides b² then a divides b.' Which of the following best disproves this conjecture?"
  type: multiple-choice
  options:
    - "Show that the statement fails for infinitely many pairs of integers"
    - "Exhibit the single case a = 4, b = 6, since 4 divides 36 but 4 does not divide 6"
    - "Construct a formal proof by contradiction that the statement cannot hold universally"
    - "Find a general pattern of values where the divisibility property fails"
  answer: 1
  explanation: "One counterexample is logically sufficient. For a = 4 and b = 6: 4 divides 36 (= 6²), but 4 does not divide 6. Exhibiting this single concrete case where P(4, 6) is false immediately establishes ∃a, b such that the statement fails — the disproof is complete. No additional cases, patterns, or general arguments are needed. This is the asymmetry: disproving a universal requires only one witness."

- question: "What positive work does a good counterexample do beyond simply showing a conjecture is false?"
  type: multiple-choice
  options:
    - "It demonstrates the logical form of proof by contradiction"
    - "It calibrates the conjecture by revealing where the boundary between truth and falsity lies"
    - "It shows that no valid proof of the original conjecture can possibly be constructed"
    - "It establishes that the domain of the conjecture was improperly specified"
  answer: 1
  explanation: "Counterexamples are diagnostic tools, not just destroyers. If the counterexample exploits a boundary or degenerate case, it suggests the conjecture can be saved by restricting the domain. If it is generic, the conjecture is fundamentally wrong. In either case, the counterexample reveals exactly where truth ends and falsity begins — pointing toward the correct, restricted statement worth proving."

- question: "To disprove 'All prime numbers are odd,' you need to show that infinitely many even primes exist."
  type: true-false
  answer: false
  explanation: "One counterexample is logically complete. The prime 2 is even, and that single case immediately refutes the universal claim. Gathering more even primes would be redundant — the disproof is finished the moment you exhibit one case where the predicate fails. The logical negation of 'For all primes p, p is odd' is 'There exists a prime p that is even,' and 2 proves the existential."

- question: "A counterexample found in a degenerate or boundary case (such as x = 0 or the empty set) is weaker evidence against a conjecture than a counterexample using typical values."
  type: true-false
  answer: false
  explanation: "Any counterexample has identical logical force — one case is one case. Logically, a boundary counterexample and a central counterexample are equally decisive. In practice, boundary cases (0, 1, the empty set, constant functions, disconnected graphs) are PREFERRED starting points for finding counterexamples precisely because many universal claims fail there. The force of the disproof is independent of how typical the witness is."

- question: "Why does the logical structure of universal statements create such a strong asymmetry between proof and disproof?"
  type: short-answer
  answer: "A universal statement 'For all x, P(x)' makes a claim that must hold for every element in the domain — no finite collection of confirming instances constitutes a proof, only a general argument covering all cases. But its logical negation is the existential claim 'There exists x such that ¬P(x),' which is proved by exhibiting a single witness. Proving the universal requires universality; disproving it requires only one concrete counterexample that satisfies the domain condition and fails the predicate."
  explanation: "This asymmetry is a direct consequence of the semantics of quantifiers. Universal and existential quantifiers are logical duals: the negation of ∀x P(x) is ∃x ¬P(x). A proof of an existential claim is always a witness — one concrete element. So a counterexample IS a proof of the negation, complete and rigorous. Understanding this makes disproofs feel less like failures and more like what they are: successful proofs of a different kind of statement."
```

## Explainer

From predicates and quantifiers, you know that a universal statement "For all x, P(x)" makes a sweeping claim — it must hold for every element in the domain. This creates a profound asymmetry: to prove such a statement true, you must account for every case; to prove it false, one case suffices. A **counterexample** is a single element c for which P(c) is false, and its existence immediately establishes ∃x ¬P(x) — the logical negation of the universal. Finding that single element is the entire disproof.

The strategy for finding counterexamples is guided by the structure of the claim. Extreme and degenerate cases are often the most productive starting points: 0 and 1 in arithmetic (does this property hold for the multiplicative identity?), the empty set in combinatorics, the zero vector in linear algebra, a constant function in analysis, a disconnected graph in graph theory. Many universal claims that seem plausible in the typical case fail at the boundary. The claim "every continuous function is differentiable" sounds reasonable, but f(x) = |x| is continuous everywhere and fails to be differentiable at exactly one point — x = 0 — which is all that is needed to disprove it.

A well-constructed counterexample is minimal and targeted. It directly violates the predicate with as little extraneous structure as possible. If the claim is "all primes are odd," the counterexample is 2 — not a long argument about even composites. Once found, the logical form of the disproof is always the same: exhibit the counterexample, confirm it satisfies the domain condition, and show that P(c) fails by direct calculation or reference to a known fact. The argument is short and the verification is explicit.

Counterexamples also do positive work: they calibrate conjectures. If a counterexample violates only a boundary condition, it suggests that the conjecture can be salvaged by restricting the domain — "all differentiable functions are continuous" does hold, even though the converse fails. If the counterexample is generic or central, the conjecture is fundamentally wrong and should be abandoned or rebuilt. In this sense, counterexamples are not just destroyers of claims — they are diagnostic tools that reveal exactly where the boundary between truth and falsity lies, pointing toward the correct, restricted statement worth proving.
