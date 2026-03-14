---
id: measure-spaces-definition
title: 'Measure Spaces: Definition and Examples'
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: measurable-sets-properties
  type: hard
builds-toward:
- outer-measure-definition
- null-sets-almost-everywhere
- product-measures-definition
tags:
- measure-theory
- measure-spaces
stage: abstract-reasoning
status: draft
---

# Measure Spaces: Definition and Examples

## Core Idea
A measure space is a triple (X, ℱ, μ) where X is a set, ℱ is a σ-algebra, and μ: ℱ → [0,∞] is countably additive with μ(∅) = 0. This unifies notions of length, area, volume, and probability in a single framework.

## How It's Best Learned
Examine (ℝ, Borel sets, Lebesgue measure), discrete spaces with counting measure, and probability spaces. Verify countable additivity in concrete examples.

## Common Misconceptions
Not all subsets are measurable in general spaces (though they are in Lebesgue's construction on ℝ). Countable additivity is stronger than finite additivity and requires care in proofs.
