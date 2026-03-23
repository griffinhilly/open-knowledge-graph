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
status: validated
---

# Quantifiers: ALL, SOME, and NONE

## Core Idea
Quantifiers (all, some, none) specify how many class members have a property. Understanding logical relationships between quantified statements is crucial: 'All A are B' differs logically from 'Some A are B.' Mistakes with quantifiers lead to invalid inferences. From 'Some students passed,' we cannot conclude 'All students passed.'

## Questions

```yaml
- question: "A study finds that some professional athletes use performance-enhancing drugs. A journalist writes the headline: 'Professional athletes use performance-enhancing drugs.' What quantifier error does the headline commit?"
  type: multiple-choice
  options:
    - "Illicit conversion — the subject and predicate have been switched"
    - "Overgeneralization — omitting 'some' implies a universal claim, making a conclusion with greater scope than the evidence warrants"
    - "False dilemma — the headline suggests only two options exist"
    - "No error — omitting a quantifier is standard journalistic practice that preserves the original meaning"
  answer: 1
  explanation: "Dropping 'some' produces a de facto universal claim: 'Professional athletes use drugs' implies all or most do. This is overgeneralization — the conclusion has greater quantifier scope than the evidence supports. The evidence warrants only 'Some professional athletes use performance-enhancing drugs.' This is one of the most common quantifier errors in public discourse."

- question: "From the premise 'All senators are politicians,' what can we validly conclude?"
  type: multiple-choice
  options:
    - "Nothing — universal statements don't imply particular ones"
    - "Some senators are politicians — the universal entails the particular, assuming the class is non-empty"
    - "Some politicians are senators — the subject and predicate can be freely swapped"
    - "No non-senators are politicians — the contrapositive follows automatically"
  answer: 1
  explanation: "From 'All A are B' we can validly conclude 'Some A are B,' provided A is non-empty — the particular is weaker than the universal, so the universal implies it. What is NOT valid is the reverse: from 'Some A are B' you cannot conclude 'All A are B.' Option C is the error of illicit conversion: 'All senators are politicians' does NOT entail 'All politicians are senators.'"

- question: "In formal logic, 'Some A are B' is compatible with 'All A are B' — the word 'some' means at least one, not 'only some.'"
  type: true-false
  answer: true
  explanation: "Logically, 'some' sets a floor (at least one), not a ceiling. If all A are B, then certainly some A are B. The two statements are compatible. In everyday speech 'some' often pragmatically implies 'not all,' but in formal logic no such implication holds. This matters for evaluating arguments: 'Some students passed' does not conflict with 'All students passed' — it is consistent with it."

- question: "'All A are B' and 'No A are B' are contradictories — exactly one must be true."
  type: true-false
  answer: false
  explanation: "'All A are B' and 'No A are B' are contraries, not contradictories. Contraries cannot both be true but can both be false: if some A are B and some are not, both universal claims are false simultaneously. Contradictories (such as 'All A are B' and 'Some A are not B') cannot both be true AND cannot both be false — exactly one must hold. The distinction between contrary and contradictory is essential for valid inference."

- question: "Why can we not move from 'Some A are B' to 'All A are B' in logical reasoning?"
  type: short-answer
  answer: "'Some A are B' tells us only that at least one member of A has property B — it gives no information about the remaining members. Moving to 'All A are B' would claim that every member of A has property B, a scope the particular premise does not support. The conclusion reaches beyond the evidence: we observed a subset and generalized to the whole class, which is the fallacy of overgeneralization."
  explanation: "Formally: 'Some A are B' is existential (∃x(Ax ∧ Bx)), while 'All A are B' is universal (∀x(Ax → Bx)). An existential statement never entails a universal — no finite number of confirming instances proves a universal claim."
```

## Explainer

From your study of arguments, premises, and conclusions, you know that the validity of an inference depends on the *logical form* of its statements — not just the content. **Quantifiers** are the terms that specify logical scope: how much of a class a claim applies to. Getting quantifiers right is not pedantic hair-splitting; it is the foundation of categorical reasoning, where whole argument structures turn on whether a claim says *all*, *some*, or *none*.

The three basic quantifiers create four standard claim types. **Universal affirmative** ("All A are B") claims every member of A has property B. **Universal negative** ("No A are B") denies it of every member. **Particular affirmative** ("Some A are B") claims at least one member of A has B. **Particular negative** ("Some A are not B") denies it of at least one member. The word "some" in logic means at least one — it does not imply "only some" or "not all." This catches many people out: "Some politicians are honest" is compatible with "All politicians are honest."

The relationships between these forms have determinate logical structure. A universal claim **contradicts** its particular counterpart of opposite quality: "All swans are white" and "Some swans are not white" cannot both be true, and cannot both be false — exactly one must hold. Two universals of opposite quality (**contraries**) cannot both be true but can both be false: "All students passed" and "No students passed" are both false if some passed and some didn't. Knowing these relationships lets you spot valid inferences at a glance: from "All A are B" you can immediately conclude "Some A are B" (assuming A is non-empty); from "No A are B" you can conclude "Some A are not B"; but from "Some A are B" you cannot move to "All A are B."

The most common quantifier errors in everyday reasoning involve **overgeneralization** and **illicit particular**. Overgeneralization moves from "some" to "all" — "some immigrants commit crimes" becomes "immigrants are criminals." Illicit particular moves from a universal to an unwarranted particular about a specific case — "All politicians are corrupt, so this particular politician, even though she's new, must be corrupt" ignores that the universal might be false, or might not apply to her specifically. Both errors have the same underlying structure: the quantifier scope in the conclusion exceeds what the premises actually warrant.

If you have encountered first-order logic syntax, you'll recognize these quantifiers as ∀ (for all) and ∃ (there exists). The formal machinery encodes exactly the distinctions above: ∀x(Ax → Bx) is "All A are B"; ∃x(Ax ∧ Bx) is "Some A are B." The formal notation makes it impossible to conflate these, which is one of its main advantages over natural language — where "some" and "all" often get blurred in fast speech and writing. Categorical syllogisms, which you'll study next, are built entirely from these four quantified forms, and their validity depends on applying exactly these logical relationships correctly.
