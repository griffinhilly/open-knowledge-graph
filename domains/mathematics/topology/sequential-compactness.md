---
id: sequential-compactness
title: Sequential Compactness
domain: mathematics
course: topology
prerequisites:
- id: compact-spaces-open-covers
  type: hard
builds-toward:
- metrization-theorems
tags:
- sequential-compactness
- convergent-subsequences
stage: advanced
status: draft
---

# Sequential Compactness

## Core Idea
A space is sequentially compact if every sequence has a convergent subsequence. In metric spaces, sequential compactness is equivalent to compactness, but in general topology they differ. Sequential compactness characterizes compactness using sequences, the more intuitive notion from calculus.

## Explainer

You already know that **compactness** — defined via open covers — is one of the most powerful properties a topological space can have. But the open cover definition is notoriously abstract: a space is compact if every open cover has a finite subcover. It tells you what compactness does (any covering has a finite reduction), but it doesn't say anything about how individual points or sequences behave. Sequential compactness offers a different perspective using the language of sequences, which is more directly intuitive for anyone who has studied calculus.

A space X is **sequentially compact** if every sequence (xₙ) in X has a **convergent subsequence** — a subsequence (xₙₖ) that converges to some point in X. Think about what this means in ℝ: the Bolzano-Weierstrass theorem says every bounded sequence in ℝ has a convergent subsequence. The closed interval [0, 1] is sequentially compact because no sequence in [0, 1] can escape to infinity, and by Bolzano-Weierstrass, some subsequence must converge — and since [0, 1] is closed, the limit must land back in [0, 1]. The open interval (0, 1) is not sequentially compact: the sequence 1/n converges to 0, which is outside (0, 1), so no subsequence converges within the space.

In metric spaces, sequential compactness and compactness are equivalent — they capture the same property in two different vocabularies. This equivalence is not obvious to prove; it requires showing that in a metric space, having the Bolzano-Weierstrass property (convergent subsequences) is the same as having no infinite open cover that can't be reduced to a finite one. The proof goes through the concept of **total boundedness** (the space can be covered by finitely many ε-balls for any ε > 0) and uses the metric structure in an essential way. This is why the equivalence breaks down in general topological spaces — without a metric, sequences don't capture the full complexity of the topology. There exist compact spaces that are not sequentially compact, and sequentially compact spaces that are not compact, in the general topological setting.

The practical value of sequential compactness is that it gives you a hands-on tool for proving things about compact metric spaces. To show a function achieves its maximum on a compact metric space, you can take a maximizing sequence (f(xₙ) → sup f) and extract a convergent subsequence (xₙₖ → x*) — then continuity shows f(x*) = sup f. To show a set is compact, you can produce convergent subsequences from arbitrary sequences. Many existence proofs in analysis follow exactly this pattern: take a sequence of approximate solutions, extract a convergent subsequence, and identify the limit as an exact solution. Sequential compactness makes these arguments rigorous.
