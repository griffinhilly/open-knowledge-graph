---
id: lookahead-and-parsing-power
title: Lookahead in Parsing and Grammar Classes
domain: computer-science
course: compilers
prerequisites:
- id: ll-parsing
  type: hard
- id: lr-parsing
  type: hard
builds-toward:
- compiler-error-recovery
tags:
- parsing
- theory
- lookahead
stage: advanced
status: draft
---

# Lookahead in Parsing and Grammar Classes

## Core Idea
Different parsers require different lookahead: LL(1) uses 1-token lookahead and is limited to certain grammar classes; LR(1) implicitly encodes more context in parse tables. Understanding lookahead determines parsing algorithm selection and reveals whether a grammar is parseable without backtracking.
