---
id: rice-theorem
title: Rice's Theorem
domain: computer-science
course: theory-of-computation
prerequisites:
- id: undecidability-reductions
  type: hard
tags:
- Rice-theorem
- undecidability
- semantic-property
- TM
stage: advanced
status: draft
---

# Rice's Theorem

## Core Idea
Rice's Theorem states that every non-trivial semantic property of Turing machines is undecidable. A property is semantic if it depends only on the language recognized by the TM (not on the TM's internal mechanics), and non-trivial if some TMs have it and some do not. Examples include: 'Does M accept at least one string?', 'Does M accept all strings?', 'Does M accept a regular language?' — all undecidable by Rice's theorem. The theorem is proved by reducing HALT_TM to any such property, using a gadget TM that simulates the original machine and then runs a reference TM.

## How It's Best Learned
Internalize what 'semantic property' means by contrasting it with syntactic properties (e.g., 'does M have exactly 5 states?' — syntactic, and often decidable). Then apply the theorem as a rapid undecidability test: before working out a full reduction, check if the problem is a non-trivial semantic property.

## Common Misconceptions
- Applying Rice's theorem to syntactic properties — it does *not* apply to properties of the TM description itself, only properties of its language.
- Thinking Rice's theorem says 'everything about TMs is undecidable' — many syntactic properties are decidable.
