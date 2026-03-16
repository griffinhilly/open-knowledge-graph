---
id: alternating-machines-hierarchy
title: Alternating Turing Machines and the Polynomial Hierarchy
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: nondeterministic-turing-machines
  type: hard
- id: pspace-completeness
  type: soft
builds-toward:
- counting-complexity-sharp-p
tags:
- alternating-machines
- polynomial-hierarchy
- alternation
stage: advanced
status: draft
---

# Alternating Turing Machines and the Polynomial Hierarchy

## Core Idea
Alternating Turing machines extend nondeterminism by allowing both existential (there exists a successor state) and universal (all successor states lead to acceptance) choices. The complexity classes defined by alternating machines form the polynomial hierarchy: Σₖ correspond to k-quantifier alternations starting with existential. Alternation captures the power of interactive reasoning between a prover and verifier.

## How It's Best Learned
Simulate alternating machines on simple problems (e.g., game trees with alternating turns). See how existential and universal states correspond to ∃ and ∀ quantifiers in logic.

## Explainer

You already know that a nondeterministic Turing machine (NTM) guesses at each step: it accepts if *some* branch of its computation accepts. The key word is "some" — this is an **existential** choice. An **alternating Turing machine** (ATM) generalizes this by also allowing **universal** states, where the machine accepts only if *all* successor branches accept. Each state is labeled either existential (∃) or universal (∀), and the machine alternates between these modes as computation proceeds.

The game-tree analogy makes this vivid. Imagine a two-player game where you (existential) want to win and your opponent (universal) is adversarial. An existential state corresponds to your move — you just need one good choice. A universal state corresponds to your opponent's move — every response they make must still lead to your victory. A problem is in an alternating complexity class if you can design such a game where the machine decides the winner in polynomial time.

This directly produces the **polynomial hierarchy**. **Σ₁ᵖ = NP**: one existential quantifier ("does there exist a certificate?"). **Π₁ᵖ = co-NP**: one universal quantifier ("do all configurations fail?"). **Σ₂ᵖ**: existential then universal — "does there exist a move such that for all opponent responses, I win?" Each additional level k adds one more quantifier alternation. The class **PH** (polynomial hierarchy) is the union of all these levels. Alternating machines with k alternations characterize Σₖᵖ exactly.

The connection to PSPACE (your prerequisite) completes the picture: ATMs running in polynomial *time* with *unrestricted* alternations are equivalent to deterministic polynomial-space computation. This is a deep theorem — APTIME = PSPACE — and it explains why PSPACE sits above the entire polynomial hierarchy. Each level of the hierarchy uses a fixed number of quantifier alternations; PSPACE allows polynomially many. The hierarchy collapses into PSPACE at the limit of unlimited alternation.

Practically, the polynomial hierarchy matters because many natural problems live at specific levels. Graph isomorphism sits in Σ₂ᵖ ∩ Π₂ᵖ (though likely not NP-complete). Deciding whether a Boolean formula with alternating quantifiers is true is Σₖᵖ-complete for k alternations. Understanding which level a problem occupies tells you exactly what kind of "guessing and verifying" resource is needed — and which hardness results apply.
