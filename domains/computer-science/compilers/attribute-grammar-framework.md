---
id: attribute-grammar-framework
title: Attribute Grammar Framework
domain: computer-science
course: compilers
prerequisites:
- id: ast-node-representation
  type: hard
- id: parse-trees-derivations
  type: soft
builds-toward:
- semantic-error-detection-reporting
tags:
- semantic-analysis
- attributes
- grammars
stage: advanced
status: draft
---

# Attribute Grammar Framework

## Core Idea
Attribute grammars associate attributes (semantic values) with grammar symbols and define rules for computing attributes. Synthesized attributes are computed from children; inherited attributes from parents. This framework elegantly separates parsing from semantic analysis.

## How It's Best Learned
Write attribute grammars for a small language using tools like Antlr. Implement both bottom-up and top-down attribute evaluators.

## Common Misconceptions
Attribute grammars are the only way to do semantic analysis (they are one useful approach; ad-hoc traversal is simpler for many tasks). All attributes must be computed in one pass (multiple passes can be clearer).
