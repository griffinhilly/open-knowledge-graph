---
id: ad-hoc-polymorphism-overloading
title: Ad Hoc Polymorphism and Function Overloading
domain: computer-science
course: compilers
prerequisites:
- id: type-systems-overview
  type: hard
- id: symbol-tables-and-scope
  type: hard
builds-toward:
- overload-resolution-typing
tags:
- polymorphism
- type-systems
- overloading
stage: advanced
status: draft
---

# Ad Hoc Polymorphism and Function Overloading

## Core Idea
Ad hoc polymorphism (overloading) allows functions with the same name to behave differently for different argument types. Unlike parametric polymorphism which uses a single implementation, ad hoc polymorphism provides distinct code per type, selected at compile-time during overload resolution.
