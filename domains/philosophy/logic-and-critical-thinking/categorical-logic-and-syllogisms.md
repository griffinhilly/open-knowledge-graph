---
id: categorical-logic-and-syllogisms
title: Categorical Logic and Syllogisms
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: universal-and-existential-statements
  type: hard
- id: predicate-logic-introduction
  type: soft
builds-toward:
- middle-term-distribution
- logical-form
tags:
- categorical-logic
- syllogisms
- deductive
stage: abstract-reasoning
status: draft
---

# Categorical Logic and Syllogisms

## Core Idea
Categorical logic operates with four statement types: A (all S are P), E (no S are P), I (some S are P), O (some S are not P). A categorical syllogism has exactly three terms across three statements. The validity of a syllogism depends on whether the middle term (the term appearing in both premises) properly links the major and minor terms.

## How It's Best Learned
Learn the four forms (A, E, I, O) with examples. Use Venn diagrams to visualize all three terms. Practice identifying valid and invalid forms before learning formal rules.

## Common Misconceptions
Misunderstanding what 'distributed' means (a term is distributed if the statement speaks of all members of that class). Making errors with negative premises or too many negatives.

## Explainer

You already know how to work with universal statements ("All S are P") and existential statements ("Some S are P"). Categorical logic systematizes exactly four ways to relate two categories. The **A statement** ("All S are P") affirms universally: every member of S is also in P. The **E statement** ("No S are P") denies universally: no member of S is in P. The **I statement** ("Some S are P") affirms existentially: at least one member of S is also in P. And the **O statement** ("Some S are not P") denies existentially: at least one member of S falls outside P. These four types—A, E, I, O—are the only building blocks categorical logic uses. Any argument in this system is built from statements of these four forms.

A **categorical syllogism** is a deductive argument with exactly three statements (two premises and a conclusion) and exactly three terms. Each term appears in exactly two of the three statements. The **major term** is the predicate of the conclusion; the **minor term** is the subject of the conclusion; and the **middle term** appears in both premises but not in the conclusion. The middle term is the logical bridge: it connects the major and minor terms across the two premises. "All humans are mortal; all philosophers are human; therefore, all philosophers are mortal" — here "mortal" is the major term, "philosophers" is the minor term, and "humans" is the middle term that links them.

The key concept for assessing validity is **distribution**: a term is distributed in a statement if the statement says something about *all* members of that term's class. In an A statement ("All S are P"), S is distributed but P is not—we're saying something about every S, but only claiming that *those* S's are in P, not that everything in P is an S. In an E statement ("No S are P"), both terms are distributed—the statement says something about *all* S's and *all* P's (namely, that none of each overlaps with the other). I statements distribute neither term; O statements distribute only the predicate. The rules of syllogistic validity turn on these distributions: the middle term must be distributed in at least one premise, and any term distributed in the conclusion must already be distributed in its corresponding premise.

The best tool for checking syllogisms visually is the **Venn diagram** with three overlapping circles, one per term. Each premise eliminates regions (or marks them as non-empty), and validity amounts to whether the conclusion's claim is already implicit in what the premises have drawn. If after drawing both premises the conclusion is already forced by the diagram, the syllogism is valid. If you can imagine a world consistent with both premises where the conclusion is false, the syllogism is invalid—meaning the premises fail to necessitate the conclusion regardless of what is actually true. This diagram check is more reliable than memorizing valid moods and figures, and it builds genuine intuition about why distribution rules work.
