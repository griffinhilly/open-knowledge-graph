---
id: grammar-design-for-compilation
title: Grammar Design for Compilation
domain: computer-science
course: compilers
prerequisites:
- id: compiler-phases-and-organization
  type: hard
- id: context-free-grammars-compiler-design
  type: hard
builds-toward:
- recursive-descent-parser-design
- shift-reduce-bottom-up-parsing
tags:
- grammar
- formal-languages
- language-design
stage: advanced
status: draft
---

# Grammar Design for Compilation

## Core Idea
Not every context-free grammar is equally suitable for parsing. Some have shift-reduce conflicts, left-recursion, or ambiguities making parsing difficult. Grammar designers must write grammars that are both unambiguous and compatible with the target parsing algorithm.

## How It's Best Learned
Write grammars for small languages and test them with parser generators. Experiment with resolving conflicts through grammar transformations.

## Common Misconceptions
Any grammar accepting the language is fine (some are much harder to parse than others). Removing left-recursion is the only transformation needed (you may also eliminate ambiguities or handle precedence).
