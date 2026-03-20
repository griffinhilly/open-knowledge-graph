---
id: quantifiers-in-reasoning
title: 'Quantifiers: ALL, SOME, and NONE'
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: arguments-premises-and-conclusions
  type: hard
- id: first-order-logic-syntax
  type: soft
builds-toward:
- categorical-logic-and-syllogisms
- universal-and-existential-statements
tags:
- quantifiers
- categorical-logic
- reasoning
stage: formal-systems
status: draft
---

# Quantifiers: ALL, SOME, and NONE

## Core Idea
Quantifiers (all, some, none) specify how many class members have a property. Understanding logical relationships between quantified statements is crucial: 'All A are B' differs logically from 'Some A are B.' Mistakes with quantifiers lead to invalid inferences. From 'Some students passed,' we cannot conclude 'All students passed.'

## Explainer

From your study of arguments, premises, and conclusions, you know that the validity of an inference depends on the *logical form* of its statements — not just the content. **Quantifiers** are the terms that specify logical scope: how much of a class a claim applies to. Getting quantifiers right is not pedantic hair-splitting; it is the foundation of categorical reasoning, where whole argument structures turn on whether a claim says *all*, *some*, or *none*.

The three basic quantifiers create four standard claim types. **Universal affirmative** ("All A are B") claims every member of A has property B. **Universal negative** ("No A are B") denies it of every member. **Particular affirmative** ("Some A are B") claims at least one member of A has B. **Particular negative** ("Some A are not B") denies it of at least one member. The word "some" in logic means at least one — it does not imply "only some" or "not all." This catches many people out: "Some politicians are honest" is compatible with "All politicians are honest."

The relationships between these forms have determinate logical structure. A universal claim **contradicts** its particular counterpart of opposite quality: "All swans are white" and "Some swans are not white" cannot both be true, and cannot both be false — exactly one must hold. Two universals of opposite quality (**contraries**) cannot both be true but can both be false: "All students passed" and "No students passed" are both false if some passed and some didn't. Knowing these relationships lets you spot valid inferences at a glance: from "All A are B" you can immediately conclude "Some A are B" (assuming A is non-empty); from "No A are B" you can conclude "Some A are not B"; but from "Some A are B" you cannot move to "All A are B."

The most common quantifier errors in everyday reasoning involve **overgeneralization** and **illicit particular**. Overgeneralization moves from "some" to "all" — "some immigrants commit crimes" becomes "immigrants are criminals." Illicit particular moves from a universal to an unwarranted particular about a specific case — "All politicians are corrupt, so this particular politician, even though she's new, must be corrupt" ignores that the universal might be false, or might not apply to her specifically. Both errors have the same underlying structure: the quantifier scope in the conclusion exceeds what the premises actually warrant.

If you have encountered first-order logic syntax, you'll recognize these quantifiers as ∀ (for all) and ∃ (there exists). The formal machinery encodes exactly the distinctions above: ∀x(Ax → Bx) is "All A are B"; ∃x(Ax ∧ Bx) is "Some A are B." The formal notation makes it impossible to conflate these, which is one of its main advantages over natural language — where "some" and "all" often get blurred in fast speech and writing. Categorical syllogisms, which you'll study next, are built entirely from these four quantified forms, and their validity depends on applying exactly these logical relationships correctly.
