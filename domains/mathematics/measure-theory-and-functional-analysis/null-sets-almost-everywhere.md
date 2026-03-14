---
id: null-sets-almost-everywhere
title: Null Sets and Almost Everywhere
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: measure-spaces-definition
  type: hard
builds-toward:
- lebesgue-integral-simple-functions
- dominated-convergence-theorem
tags:
- measure-theory
- null-sets
stage: abstract-reasoning
status: draft
---

# Null Sets and Almost Everywhere

## Core Idea
A set has measure zero (is null) if μ(A) = 0. A property holds almost everywhere (a.e.) if the set where it fails is null. This allows us to ignore 'small' sets and treat functions differing on a null set as equivalent.

## How It's Best Learned
Observe that single points in ℝ have Lebesgue measure zero, as do all countable sets. See how L^p spaces identify functions equal almost everywhere.

## Common Misconceptions
Null sets are not necessarily empty; the Cantor set has measure zero but is uncountable. 'Almost every' quantification must be formalized via measures, not classical logic.
