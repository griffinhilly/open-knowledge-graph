---
id: closure-properties-context-free
title: Closure Properties of Context-Free Languages
domain: computer-science
course: theory-of-computation
prerequisites:
- id: cyk-parsing-algorithm
  type: hard
builds-toward:
- limitations-of-context-free
tags:
- context-free
- closure
- properties
stage: abstract-reasoning
status: draft
---

# Closure Properties of Context-Free Languages

## Core Idea
Context-free languages are closed under union, concatenation, and Kleene star, but NOT under intersection or complement. This asymmetry makes CFLs less robust than regular languages and has important implications for language design and decidability.
