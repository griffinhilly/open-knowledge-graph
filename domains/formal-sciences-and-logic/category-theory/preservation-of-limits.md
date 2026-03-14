---
id: preservation-of-limits
title: Preservation and Reflection of Limits
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: functors
  type: hard
- id: limits-and-colimits
  type: hard
builds-toward:
- adjoint-functors
- kan-extensions
tags:
- functor-properties
- limits
- universal-properties
stage: advanced
status: draft
---

# Preservation and Reflection of Limits

## Core Idea
A functor F: C → D preserves limits if whenever a diagram in C has a limit cone, F maps it to a limit cone in D. A functor reflects limits if F's image of a cone is a limit in D only when the original cone was a limit in C. Preservation relates to the idea that F respects 'universal' constructions.
