---
id: composition-of-functions-sets
title: Function Composition and Functional Structure
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: functions-and-function-properties
  type: hard
builds-toward:
- well-founded-relations-and-recursion
- natural-numbers-as-iterative-construction
tags:
- composition
- structure
- identity
stage: formal-systems
status: draft
---

# Function Composition and Functional Structure

## Core Idea
Given f: A → B and g: B → C, their composition (g ∘ f): A → C is defined by (g ∘ f)(a) = g(f(a)). Composition is associative and has an identity function id_A for each set, making it a fundamental operation. Bijections compose to bijections, and injections/surjections preserve their properties under composition.
