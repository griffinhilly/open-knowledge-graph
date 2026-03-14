---
id: quadruple-intermediate-representation
title: Quadruple Intermediate Representation
domain: computer-science
course: compilers
prerequisites:
- id: three-address-intermediate-code
  type: hard
builds-toward:
- basic-block-analysis
tags:
- ir
- intermediate-representation
stage: advanced
status: draft
---

# Quadruple Intermediate Representation

## Core Idea
A quadruple explicitly represents a three-address instruction as a 4-tuple: (op, arg1, arg2, result). Quadruples are more explicit than textual 3AC and support easier manipulation during optimization. Triples (omitting the result field) are more compact but harder to optimize.

## How It's Best Learned
Implement both quadruple and triple representations. Compare them on a real optimization task to understand trade-offs.
