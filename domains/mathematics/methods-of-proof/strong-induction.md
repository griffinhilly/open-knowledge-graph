---
id: strong-induction
title: Strong Induction
domain: mathematics
course: methods-of-proof
prerequisites:
- id: mathematical-induction
  type: hard
builds-toward:
- well-ordering-principle
tags:
- induction
- proof
- complete
stage: formal-systems
status: draft
---

# Strong Induction

## Core Idea
Strong induction assumes the statement holds for all values up to n when proving it for n+1, rather than just for n. This stronger hypothesis is necessary when the inductive step depends on multiple previous cases.
