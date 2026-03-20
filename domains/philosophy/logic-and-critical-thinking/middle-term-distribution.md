---
id: middle-term-distribution
title: Middle Term Distribution and Validity Rules
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: categorical-logic-and-syllogisms
  type: hard
builds-toward:
- logical-form
tags:
- categorical-logic
- distribution
- validity-rules
stage: formal-systems
status: draft
---

# Middle Term Distribution and Validity Rules

## Core Idea
For a categorical syllogism to be valid, the middle term must be distributed (taken in its entirety) at least once across the premises. Additionally, if a term is distributed in the conclusion, it must be distributed in its premise. These distribution rules ensure that the middle term actually links the major and minor terms.

## How It's Best Learned
Master identifying which terms are distributed in each of the four statement types (A, E, I, O). Apply the rules to test validity of given syllogisms. Show how distributing the middle term in only one premise can lead to invalid conclusions.

## Common Misconceptions
Forgetting to check all three distribution rules, not realizing that term distribution depends on statement type, assuming a valid-looking form is valid without checking distribution.

## Explainer

You already know from categorical logic and syllogisms that a syllogism connects three terms—major, minor, and middle—through two premises and a conclusion. The **middle term** is the pivot: it appears in both premises but not the conclusion. Its job is to link the other two terms together. The distribution rules exist to ensure this linkage is actually doing logical work rather than creating a fake bridge.

A term is **distributed** in a statement when the statement makes a claim about *all* members of that category. In an A-statement ("All S are P"), the subject S is distributed—we are making a claim about every S. In an E-statement ("No S are P"), both S and P are distributed—we are excluding every S from every P. In an I-statement ("Some S are P"), neither term is distributed—we are only claiming overlap among some members. In an O-statement ("Some S are not P"), only the predicate P is distributed—the claim excludes some S from the *entirety* of P. A useful mnemonic: **A**ffirming distributes the **s**ubject; **E**xcluding distributes **b**oth; **I**nclusion distributes **n**either; **O**nly the predicate in O.

Now consider why the middle term must be distributed at least once. Suppose neither premise distributes the middle term M. Then the first premise talks about *some* M, and the second talks about *some* M—but these might be completely different subsets of M. The middle term connects S and P only if at least one premise covers all of M, guaranteeing genuine overlap. The classic fallacy of the **undistributed middle** looks like: "All cats are mammals; all dogs are mammals; therefore all cats are dogs." The middle term "mammals" is the predicate of two I-type claims (distributionally speaking)—never fully covered—so cats and dogs are only linked via overlapping subsets of mammals, not logically entailed to share membership.

The second rule—that if a term is distributed in the conclusion it must be distributed in its premise—prevents **illicit process**: sneaking in a claim about *all* of a category when the premise only warranted a claim about *some*. If the conclusion says "No S are P" (distributing P), but the premise only said "Some P are Q," you have made a stronger claim about P than you ever established. Together, these rules are not arbitrary technicalities—they are the precise conditions under which the middle term genuinely establishes the connection the conclusion asserts.
