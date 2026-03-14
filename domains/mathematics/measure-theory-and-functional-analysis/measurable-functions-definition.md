---
id: measurable-functions-definition
title: 'Measurable Functions: Definition and Properties'
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: sigma-algebras-and-measurable-sets
  type: hard
- id: open-sets-topology
  type: soft
builds-toward:
- simple-functions-approximation
- lebesgue-integral-simple-functions
tags:
- measure-theory
- measurable-functions
stage: abstract-reasoning
status: draft
---

# Measurable Functions: Definition and Properties

## Core Idea
A function f: X → ℝ is measurable if the preimage of every Borel set in ℝ is a measurable set in X (i.e., f⁻¹(B) ∈ ℱ for all B ∈ ℬ(ℝ)). Measurable functions are precisely those we can integrate.

## How It's Best Learned
Start by showing continuous functions are measurable (preimages of open sets are open). Build to indicator functions of measurable sets.

## Common Misconceptions
Measurability differs from continuity; discontinuous functions can be measurable. You only need f⁻¹(open interval) measurable, not f⁻¹(single point).
