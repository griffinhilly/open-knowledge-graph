---
id: pumping-lemma-for-regular-languages
title: Pumping Lemma for Regular Languages
domain: computer-science
course: theory-of-computation
prerequisites:
- id: closure-properties-regular-languages
  type: hard
builds-toward:
- limitations-of-finite-automata
tags:
- regular-languages
- non-regularity
- proof-technique
stage: abstract-reasoning
status: draft
---

# Pumping Lemma for Regular Languages

## Core Idea
The pumping lemma states: if a language L is regular, then there exists a constant p such that any string z in L with |z| ≥ p can be decomposed as z = uvw where |uv| ≤ p, |v| > 0, and uvⁱw ∈ L for all i ≥ 0. Proof by contradiction using this lemma establishes that a language is not regular.

## How It's Best Learned
Work through proofs for standard non-regular languages (e.g., {aⁿbⁿ}). Understand the adversarial game: the pumping lemma chooses p, we choose z, the adversary chooses u, v, w.
