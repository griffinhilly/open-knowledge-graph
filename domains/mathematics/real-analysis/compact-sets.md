---
id: compact-sets
title: Compact Sets
domain: mathematics
course: real-analysis
prerequisites:
- id: open-sets-real-line
  type: hard
- id: subsequences
  type: hard
builds-toward:
- heine-borel-theorem
- uniform-continuity-compact-sets
- extreme-value-theorem-rigorous
tags:
- compact
- compactness
- topology
- sequences
stage: advanced
status: draft
---

# Compact Sets

## Core Idea
A set K is compact if every open cover has a finite subcover: if K ⊆ ∪ᵢUᵢ with each Uᵢ open, then K ⊆ Uᵢ₁ ∪ ... ∪ Uᵢₙ for some finite selection. Intuitively, compact sets are 'closed and bounded' in ℝ and generalize finite sets to infinite settings. They are the workhorse of real analysis.
