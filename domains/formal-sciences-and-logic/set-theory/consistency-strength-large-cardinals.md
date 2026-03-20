---
id: consistency-strength-large-cardinals
title: Consistency Strength and the Large-Cardinal Hierarchy
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: large-cardinals-intro
  type: hard
- id: measurable-cardinals-ultra-filters
  type: soft
builds-toward:
- inner-models-relative-consistency
tags:
- consistency-strength
- large-cardinals
- hierarchy
- provability
stage: advanced
status: draft
---

# Consistency Strength and the Large-Cardinal Hierarchy

## Core Idea
Large cardinals are ordered by consistency strength: the existence of an inaccessible is consistent with ZFC but strictly stronger than ZFC; the existence of a measurable is strictly stronger than inaccessible; supercompacts are stronger still. This hierarchy is studied via inner models and reflection principles. Consistency strength provides a refined notion of 'how much you add' when extending ZFC.

## How It's Best Learned
Introduce the Veblen hierarchy of inaccessible, measurable, supercompact, and extendible cardinals. Show consistency of large-cardinal axioms is unprovable in ZFC by Gödel's incompleteness. Use inner-model theory (L, HOD, V) to compare consistency strengths.

## Common Misconceptions
- Assuming all large cardinals are 'equally large' (the consistency hierarchy reveals subtle differences).
- Conflating the cardinal itself being large with its consistency-strength; a weakly compact cardinal has lower consistency strength than many 'smaller' cardinals by ordinal comparison.

## Explainer

You know from studying **large cardinals** that certain cardinals — inaccessible, measurable, supercompact — are so large that their existence cannot be proved from ZFC alone. Each such axiom extends the standard axioms of set theory. **Consistency strength** is the tool for comparing how much is added by each extension. One theory T₁ has lower consistency strength than T₂ if: whenever T₂ is consistent, so is T₁ — but not necessarily conversely. Equivalently, T₂ proves that T₁ is consistent, but T₁ cannot prove T₂ is consistent. This defines a preorder (actually a linear order, empirically) on large-cardinal axioms: each stronger axiom implies the consistency of all weaker ones.

The hierarchy begins just above ZFC. An **inaccessible cardinal** κ is a regular strong limit cardinal — no smaller set of sets of size less than κ can reach κ by taking power sets or unions. If κ is inaccessible, then V_κ (the universe of all sets of rank below κ) is a model of ZFC. So the existence of an inaccessible implies ZFC is consistent — which by Gödel's incompleteness theorem means this assumption cannot be proved within ZFC itself. A **measurable cardinal** is strictly stronger: its existence implies not only that inaccessibles exist but that there are inaccessibly many inaccessibles, and far beyond. Above measurables lie Woodin cardinals, supercompact cardinals, and extendible cardinals, each implying the consistency of all smaller large-cardinal axioms.

**Gödel's incompleteness theorems** are what give the consistency hierarchy its teeth. No consistent theory extending PA (and therefore ZFC) can prove its own consistency. So if ZFC + "a measurable cardinal exists" is consistent, ZFC alone cannot prove this. The existence of any large cardinal is a genuine new assumption — not a theorem. Set theorists therefore calibrate the strength of mathematical claims by asking: "over which large-cardinal axiom is this provable?" A statement that requires measurables to prove is intrinsically stronger than one requiring only inaccessibles. This gives a precise meaning to the informal notion that some mathematical claims are "bolder" than others.

**Inner model theory** is the primary technical instrument for comparing consistency strengths. For each large-cardinal level, set theorists construct canonical inner models — structures like L[μ] for one measurable or L[E] for extenders — that contain exactly the large cardinals needed and no more. Two theories have the same consistency strength if and only if their canonical inner models are the same. The remarkable empirical fact is that virtually all natural mathematical theories fall into this linear hierarchy: every "natural" set-theoretic statement is equiconsistent with some large-cardinal axiom. This linearity was not logically inevitable, but it has held without exception, suggesting a deep structural order underlying the universe of sets.
