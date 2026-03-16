---
id: interactive-proofs
title: Interactive Proofs
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: pspace-and-complexity-hierarchy
  type: hard
- id: probabilistic-computation
  type: hard
tags:
- complexity
- interactive-proofs
- IP
- Arthur-Merlin
stage: formal-systems
status: draft
---

# Interactive Proofs

## Core Idea
An interactive proof system consists of an all-powerful prover and a probabilistic polynomial-time verifier who exchange messages. The verifier must accept valid claims with high probability (completeness) and reject false claims with high probability regardless of the prover's strategy (soundness). The class IP contains all languages with interactive proof systems. The landmark result IP = PSPACE (Shamir, 1992) shows that interactive proofs are far more powerful than static NP certificates. Arthur-Merlin games, where the verifier's randomness is public, yield the same class, showing that private coins do not add power.

## How It's Best Learned
Start with the interactive proof for graph non-isomorphism: the verifier secretly permutes one of two graphs and challenges the prover to identify which one — a sound proof that seems impossible with a static certificate. Then study the sum-check protocol, the key technical tool behind IP = PSPACE, which reduces a PSPACE-complete problem to a sequence of low-degree polynomial evaluations.

## Common Misconceptions
- The prover is computationally unbounded but must still convince a skeptical polynomial-time verifier — the verifier's randomness is what prevents a cheating prover from succeeding.
- IP = PSPACE does NOT mean interactive proofs are impractical — practical protocols like those in zero-knowledge cryptography use the same framework with efficient provers.

## Explainer

You know from studying PSPACE that some problems are hard precisely because there is no short static certificate for their answers — the entire computation tree must be explored. **Interactive proof systems** get around this by replacing a static certificate with a *conversation*. The setup has two parties: an all-powerful **prover** P who knows everything, and a **probabilistic polynomial-time verifier** V who is skeptical and resource-limited. They exchange messages — the verifier asks challenges drawn randomly, the prover answers — and at the end the verifier accepts or rejects. A valid language must satisfy two properties: **completeness** (an honest prover can always convince the verifier to accept) and **soundness** (no cheating prover can convince the verifier to accept a false claim, except with negligible probability).

The classic intuition is **graph non-isomorphism**. Two graphs are non-isomorphic if no relabeling of one produces the other. No one knows a short static proof of non-isomorphism, but there is a clean interactive proof: the verifier secretly picks one of the two graphs, applies a random permutation, and shows the result to the prover, asking "which graph did I start from?" An all-knowing prover can always answer correctly (since the graphs look different). A cheating prover — trying to fake non-isomorphism when the graphs are actually isomorphic — sees a random graph that could have come from either, and can only guess correctly half the time. Repeating the challenge many times drives the cheating probability exponentially close to zero.

The landmark theorem **IP = PSPACE** (Shamir, 1992) reveals that interactive proofs are far more powerful than NP certificates. The key technical tool is the **sum-check protocol**: given a multivariate polynomial over a finite field, the verifier can check that the sum of its values over all boolean inputs equals a target value in polynomial time and rounds of interaction, even though the sum has exponentially many terms. This protocol reduces any PSPACE-complete language (like quantified Boolean formula) to a sequence of polynomial identity checks, each requiring only constant-degree verification. The prover's unbounded power handles the arithmetic; the verifier's randomness catches any cheating.

**Arthur-Merlin games** are a variant where the verifier's random coins are public rather than private. Arthur (the verifier) flips coins openly; Merlin (the prover) then responds knowing the randomness. Surprisingly, public and private coins yield the same class AM = IP — meaning the verifier gains nothing from hiding its randomness. This is counterintuitive but follows from the fact that the prover is computationally unbounded anyway, so it can simulate the verifier's private randomness; the verifier's power comes from the *structure* of the interaction, not the secrecy of its coins.
