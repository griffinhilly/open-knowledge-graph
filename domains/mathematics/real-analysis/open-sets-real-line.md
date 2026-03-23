---
id: open-sets-real-line
title: Open Sets on the Real Line
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
builds-toward:
- closed-sets-real-line
- compact-sets
- epsilon-delta-continuity
tags:
- open-sets
- topology
- neighborhoods
stage: advanced
status: validated
---

# Open Sets on the Real Line

## Core Idea
A set U ⊆ ℝ is open if for every x ∈ U, there exists ε > 0 such that the interval (x - ε, x + ε) ⊆ U. Open sets are the basic objects of topology: unions of open sets are open, finite intersections of open sets are open, and ℝ and ∅ are open. They formalize the idea of 'interior points'.

## How It's Best Learned
Verify (a,b), ℝ, and ∅ are open; show [a,b] is not open (endpoints have no ε-neighborhood inside). Prove that finite intersection of open intervals can be closed: (0,2) ∩ (1,3) = (1,2) is open, but ∩ᵢ(0,1/i) = ∅.

## Common Misconceptions
- Confusing open with 'having no boundary'; (0,1) is open but has a well-defined boundary.
- Assuming open means 'sparse' or 'disconnected'; ℝ is open and fully connected.
- Forgetting infinite unions of open sets are open but infinite intersections need not be.

## Questions

```yaml
- question: "Which of the following sets is open in ℝ?"
  type: multiple-choice
  options:
    - "[0, 1) — it contains 0 but not 1, so it is half-open and qualifies as open"
    - "(0, 1) ∪ (2, 3) — the union of two open intervals"
    - "[0, 1] — the closed interval contains all its boundary points"
    - "{x ∈ ℝ : x ≠ 0} is not open because it excludes exactly one point"
  answer: 1
  explanation: "A finite or infinite union of open sets is always open. (0,1) and (2,3) are open intervals, so their union is open. [0,1) fails because 0 has no ε-neighborhood contained in the set — any interval (−ε, ε) extends to negative numbers, which are outside [0,1). [0,1] fails for both endpoints. The set {x : x ≠ 0} = (−∞,0) ∪ (0,∞) is actually open — it is a union of two open rays. The key test is always: does every point have a full ε-neighborhood inside the set?"

- question: "Consider the family of open intervals Iₙ = (−1/n, 1/n) for n = 1, 2, 3, …. What is their infinite intersection ∩ₙ Iₙ, and is it open?"
  type: multiple-choice
  options:
    - "The empty set ∅, which is open"
    - "The single point {0}, which is not open"
    - "The interval (−1, 1), which is open"
    - "All of ℝ, which is open"
  answer: 1
  explanation: "Every interval (−1/n, 1/n) contains 0, so 0 ∈ ∩ₙ Iₙ. But for any other point x ≠ 0, choosing n large enough so that 1/n < |x| excludes x from Iₙ, so x ∉ ∩ₙ Iₙ. Therefore the intersection is exactly {0}. The single-point set {0} is not open: any ε-neighborhood (−ε, ε) contains points other than 0, which are not in {0}. This counterexample shows why the axiom requires *finite* intersections of open sets to be open — infinite intersections can collapse to a non-open set."

- question: "The empty set ∅ is open in ℝ because the condition for openness is vacuously satisfied — there are no points in ∅ to violate it."
  type: true-false
  answer: true
  explanation: "The definition says: for every x ∈ U, there exists ε > 0 such that (x−ε, x+ε) ⊆ U. If U = ∅, the universal quantifier 'for every x ∈ ∅' ranges over an empty domain — no x exists to check — so the statement is vacuously true. This may feel unsatisfying, but the vacuous case is logically sound and necessary: ∅ must be open to satisfy the topology axioms (unions and intersections of open sets must be open, and ∅ = ℝ ∩ ∅ must itself be one of the axiomatically declared open sets)."

- question: "An infinite union of open sets is always open, and so is an infinite intersection of open sets."
  type: true-false
  answer: false
  explanation: "Arbitrary (including infinite) *unions* of open sets are always open. But infinite *intersections* need not be open. The canonical counterexample: ∩ₙ(−1/n, 1/n) = {0}, a single point that is not open. The intuition: to prove a point has an ε-neighborhood inside a *finite* intersection, you can take the minimum of finitely many ε values. With infinitely many, the infimum of those ε values may be zero — giving you no room to maneuver."

- question: "Explain in your own words why the endpoint a of the closed interval [a, b] prevents [a, b] from being open."
  type: short-answer
  answer: "For [a,b] to be open, every point in it must have some ε-neighborhood entirely contained in [a,b]. But for the endpoint a, any ε-neighborhood (a−ε, a+ε) extends to the left of a by ε. The points in (a−ε, a) are less than a and therefore not in [a,b]. So no matter how small ε is, the ε-neighborhood of a always leaks outside [a,b]. Since a ∈ [a,b] but has no valid ε-neighborhood inside [a,b], the set fails the openness condition."
  explanation: "This is exactly what 'interior point' means: a point is an interior point if it has some wiggle room in all directions while staying in the set. The endpoints of [a,b] are boundary points — they are 'at the edge' with half their ε-neighborhood falling outside the set. Open sets consist entirely of interior points; that is the definition restated in geometric terms."
```

## Explainer

From your work with ε-N convergence, you know what an ε-neighborhood looks like: a tiny interval (x − ε, x + ε) centered at a point x. Open sets are built from exactly this idea. A set U ⊆ ℝ is **open** if every point in U has some wiggle room — you can move a little in either direction and stay inside U. Formally: for every x ∈ U, there exists ε > 0 such that (x − ε, x + ε) ⊆ U. No point in an open set is "trapped at the edge" with half its neighborhood falling outside.

The canonical examples clarify the intuition. The open interval (a, b) is open: pick any x strictly between a and b, and you can find ε small enough (say, ε = min(x − a, b − x)) that (x − ε, x + ε) stays within (a, b). The closed interval [a, b] is *not* open: the endpoint a has no ε-neighborhood contained in [a, b], since any interval (a − ε, a + ε) extends to the left of a, which lies outside [a, b]. The entire real line ℝ is open (every point has plenty of room), and the empty set ∅ is vacuously open (there are no points to check). These two extreme examples — ℝ and ∅ — are both open *and* closed, a fact that sometimes surprises beginners.

The three axioms for open sets capture what "openness" must do under set operations. Arbitrary unions of open sets remain open: even if you take uncountably many open intervals, their union still guarantees every point has some ε-neighborhood inside. But you must restrict to *finite* intersections to preserve openness. The classic counterexample is the family (−1/n, 1/n) for n = 1, 2, 3, …: each is an open interval, but their infinite intersection is just {0}, which is a single point — not open. Finite intersections are safe because you can take the minimum of finitely many ε values; with infinitely many, the infimum might collapse to zero.

The power of this definition is that it isolates what matters for continuity and convergence, which you will formalize next in ε-δ continuity and topology. A function is continuous precisely when preimages of open sets are open — a statement that makes sense only because "open" has been pinned down so precisely here. The abstraction might seem like overhead for the real line, where you can already reason with intervals. But the same definition, verbatim, extends to arbitrary spaces — metric spaces, function spaces, and beyond — where intervals don't exist. Open sets on the real line are your first encounter with a structural definition that will generalize far beyond its starting point.

