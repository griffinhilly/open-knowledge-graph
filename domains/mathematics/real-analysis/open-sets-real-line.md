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
status: draft
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

## Explainer

From your work with ε-N convergence, you know what an ε-neighborhood looks like: a tiny interval (x − ε, x + ε) centered at a point x. Open sets are built from exactly this idea. A set U ⊆ ℝ is **open** if every point in U has some wiggle room — you can move a little in either direction and stay inside U. Formally: for every x ∈ U, there exists ε > 0 such that (x − ε, x + ε) ⊆ U. No point in an open set is "trapped at the edge" with half its neighborhood falling outside.

The canonical examples clarify the intuition. The open interval (a, b) is open: pick any x strictly between a and b, and you can find ε small enough (say, ε = min(x − a, b − x)) that (x − ε, x + ε) stays within (a, b). The closed interval [a, b] is *not* open: the endpoint a has no ε-neighborhood contained in [a, b], since any interval (a − ε, a + ε) extends to the left of a, which lies outside [a, b]. The entire real line ℝ is open (every point has plenty of room), and the empty set ∅ is vacuously open (there are no points to check). These two extreme examples — ℝ and ∅ — are both open *and* closed, a fact that sometimes surprises beginners.

The three axioms for open sets capture what "openness" must do under set operations. Arbitrary unions of open sets remain open: even if you take uncountably many open intervals, their union still guarantees every point has some ε-neighborhood inside. But you must restrict to *finite* intersections to preserve openness. The classic counterexample is the family (−1/n, 1/n) for n = 1, 2, 3, …: each is an open interval, but their infinite intersection is just {0}, which is a single point — not open. Finite intersections are safe because you can take the minimum of finitely many ε values; with infinitely many, the infimum might collapse to zero.

The power of this definition is that it isolates what matters for continuity and convergence, which you will formalize next in ε-δ continuity and topology. A function is continuous precisely when preimages of open sets are open — a statement that makes sense only because "open" has been pinned down so precisely here. The abstraction might seem like overhead for the real line, where you can already reason with intervals. But the same definition, verbatim, extends to arbitrary spaces — metric spaces, function spaces, and beyond — where intervals don't exist. Open sets on the real line are your first encounter with a structural definition that will generalize far beyond its starting point.

