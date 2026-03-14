---
id: simple-functions-approximation
title: Simple Functions and Approximation
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: measurable-functions-definition
  type: hard
builds-toward:
- lebesgue-integral-simple-functions
tags:
- measure-theory
- simple-functions
stage: abstract-reasoning
status: draft
---

# Simple Functions and Approximation

## Core Idea
A simple function is a finite linear combination of indicator functions: φ = Σᵢ aᵢ 𝟙ₐᵢ. Every non-negative measurable function is the pointwise limit of an increasing sequence of simple functions. Simple functions form the foundation for constructing the Lebesgue integral.

## How It's Best Learned
Construct increasing sequences of simple approximations by discretizing height levels of a given measurable function.

## Common Misconceptions
Simple functions must be finite sums. While countable sums of measurable functions remain measurable, they are no longer 'simple.' Approximation is pointwise, not uniform.
