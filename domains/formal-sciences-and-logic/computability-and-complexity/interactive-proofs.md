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
