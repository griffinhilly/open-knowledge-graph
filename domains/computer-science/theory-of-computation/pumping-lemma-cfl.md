---
id: pumping-lemma-cfl
title: Pumping Lemma for Context-Free Languages
domain: computer-science
course: theory-of-computation
prerequisites:
- id: cfg-pda-equivalence
  type: hard
- id: pumping-lemma-regular
  type: soft
- id: chomsky-normal-form
  type: soft
- id: mathematical-induction
  type: soft
- id: proof-by-contradiction
  type: soft
builds-toward:
- turing-machines
tags:
- pumping-lemma
- context-free
- non-CFL
- proof
stage: advanced
status: draft
---

# Pumping Lemma for Context-Free Languages

## Core Idea
The CFL pumping lemma states that for every CFL L there is a pumping length p such that any string s ∈ L with |s| ≥ p can be split into s = uvxyz where |vy| ≥ 1, |vxy| ≤ p, and for all i ≥ 0 the string uvⁱxyⁱz ∈ L. The proof uses the fact that in a CNF parse tree for a long string, some variable must repeat on a root-to-leaf path, giving two pumpable substrings. It is used to show languages like {aⁿbⁿcⁿ} and {aⁿ² } are not context-free.

## How It's Best Learned
Use the same adversarial game structure as the regular pumping lemma but now the adversary splits into 5 parts. For {aⁿbⁿcⁿ}, note that v and y together cannot cover all three symbol types, so pumping either inflates one or two but not all three counts equally.

## Common Misconceptions
- Thinking the pumping lemma can prove a language *is* CFL — like the regular version, it only provides a necessary condition.
- Forgetting that both v and y are pumped simultaneously (to uvⁱxyⁱz), unlike the regular version.
- Choosing a pumpable string that allows the adversary to pick v and y entirely within a single symbol block, requiring a careful case analysis.
