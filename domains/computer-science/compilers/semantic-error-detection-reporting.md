---
id: semantic-error-detection-reporting
title: Semantic Error Detection and Reporting
domain: computer-science
course: compilers
prerequisites:
- id: attribute-grammar-framework
  type: hard
- id: semantic-analysis
  type: hard
builds-toward:
- scope-binding-resolution
tags:
- semantic-analysis
- error-detection
- diagnostics
stage: advanced
status: draft
---

# Semantic Error Detection and Reporting

## Core Idea
Semantic analysis discovers errors invisible to the parser—undeclared variables, type mismatches, undefined functions. Effective error detection requires traversing the AST, gathering context, and comparing actual vs expected properties.

## How It's Best Learned
Implement a semantic analyzer detecting multiple error categories. Practice writing clear, actionable error messages with precise locations.

## Common Misconceptions
Semantic analysis is just type checking (it includes scope checking, usage rules, and more). Errors should stop compilation immediately (collect all errors so users see all problems).
