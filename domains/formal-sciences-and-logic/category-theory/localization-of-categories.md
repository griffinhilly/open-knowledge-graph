---
id: localization-of-categories
title: Localization of Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: functors
  type: hard
- id: equivalence-of-categories
  type: hard
builds-toward:
- derived-categories
- quotient-categories
tags:
- localization
- inverting-morphisms
- quotient-categories
stage: abstract-reasoning
status: draft
---

# Localization of Categories

## Core Idea
Localization is the process of formally inverting a class of morphisms in a category to create a new category where those morphisms become isomorphisms. This is analogous to localization in ring theory and allows systematic modification of categorical structure. The resulting localized category admits a universal property characterizing functors that preserve the inverted morphisms.

## How It's Best Learned
Study localization in the category of modules, where localizing at a multiplicative set yields the category of localized modules. Understand the universal property and verify that the localization functor is universal. Explore applications to homological algebra and algebraic geometry.

## Common Misconceptions
Localization does not always result in a category equivalent to a known category; checking whether a localization is 'nice' requires careful analysis. Also, different classes of morphisms can yield very different localizations.
