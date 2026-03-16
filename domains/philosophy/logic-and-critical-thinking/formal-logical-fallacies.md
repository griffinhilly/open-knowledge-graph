---
id: formal-logical-fallacies
title: Formal Logical Fallacies
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: logical-form
  type: hard
- id: validity-and-soundness
  type: hard
tags:
- formal-fallacy
- deduction
- logical-form
stage: abstract-reasoning
status: draft
---

# Formal Logical Fallacies

## Core Idea
Formal fallacies are errors that arise from the structure of an argument rather than its content. The three most common are affirming the consequent ('If P then Q; Q; therefore P'), denying the antecedent ('If P then Q; not P; therefore not Q'), and equivocation (shifting the meaning of a term mid-argument so the logical form breaks down). Unlike informal fallacies, these can be identified purely by inspecting the argument's symbolic structure without knowing what the terms refer to. Mastering formal fallacies sharpens the ability to distinguish valid from invalid inference patterns.

## How It's Best Learned
Place each fallacy next to its valid counterpart: affirming the consequent beside modus ponens, denying the antecedent beside modus tollens. Symbolize real-world arguments and check whether the inference pattern is licensed. Practice with examples that sound persuasive but fail structurally.

## Common Misconceptions
- Assuming that a formally fallacious argument must have a false conclusion — the conclusion may still be true, just not proven by that argument.
- Treating equivocation as purely informal; when a term shifts meaning between premises, the argument's logical form itself becomes invalid.

## Explainer

From your study of logical form and validity, you know that a deductively valid argument is one where, necessarily, if all the premises are true, the conclusion must be true. Validity is a structural property — it depends entirely on the form of the argument, not the truth of its content. Formal fallacies exploit that structural character: they are argument patterns that look like valid inference forms but are not. You can identify them without knowing whether the premises are true, because the flaw is in the skeleton of the reasoning itself.

The most common formal fallacy is **affirming the consequent**. You know modus ponens: "If P then Q; P; therefore Q." This is valid — the conclusion follows necessarily. Affirming the consequent smuggles in an extra step: "If P then Q; Q; therefore P." This is invalid. An example: "If it is raining, the streets are wet. The streets are wet. Therefore, it is raining." The streets might be wet because a water main broke. The conditional tells you what follows from rain; it does not tell you that only rain can cause wet streets. The conclusion does not follow from the premises. Its valid counterpart — modus tollens ("If P then Q; not Q; therefore not P") — gives you information from the consequent only when the consequent is *absent*.

**Denying the antecedent** makes the symmetric error: "If P then Q; not P; therefore not Q." Example: "If you study hard, you will pass. You did not study hard. Therefore, you will not pass." Again invalid — the conditional says studying leads to passing, not that studying is the *only* path to passing. Its valid counterpart, modus tollens, negates the consequent to infer the negation of the antecedent — not the reverse.

**Equivocation** is the subtlest of the three because it masquerades as an issue of content but is really structural. When a key term shifts meaning between its occurrence in one premise and another, the argument form breaks down. A classic example: "A feather is light. What is light cannot be dark. Therefore, no feather can be dark." The word "light" means *low in weight* in the first premise and *bright* in the second. Once you disambiguate, the two premises don't connect. Symbolically, the apparent chain of inference contains two different terms treated as one. The lesson from all three formal fallacies is the same: the appearance of valid inference does not guarantee validity. Symbolizing arguments forces the structure into the open, where these patterns become visible.

