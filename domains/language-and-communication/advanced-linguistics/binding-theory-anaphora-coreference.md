---
id: binding-theory-anaphora-coreference
title: Binding Theory and Anaphora Resolution
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: x-bar-theory
  type: hard
- id: c-command-and-binding
  type: hard
builds-toward:
- pronoun-antecedent-identification
tags:
- syntax
- binding
- anaphora
stage: advanced
status: draft
---

# Binding Theory and Anaphora Resolution

## Core Idea
Binding theory explains constraints on where pronouns and reflexives can occur and what noun phrases they can refer to, using c-command and locality domains (binding domains) to determine licit anaphoric relations.

## How It's Best Learned
Work through classic examples from English and cross-linguistic cases where reflexives have different distributions (e.g., long-distance reflexives in Icelandic), testing predictions about binding domain parameters.

## Common Misconceptions
Binding constraints are structural, not pragmatic preferences; a sentence might satisfy binding theory but be pragmatically awkward due to discourse factors.

## Explainer

From your study of X-bar theory, you have a structural representation of sentences as hierarchically organized phrase trees. From your study of c-command and binding, you know the key structural relationship: node A **c-commands** node B if every branching node dominating A also dominates B. Binding theory uses c-command to explain a puzzle any English speaker has implicit knowledge of: why "John hurt himself" is grammatical (himself refers to John) but "Himself hurt John" is not, and why "John thinks Mary likes him" allows *him* to refer to someone other than John but "John thinks Mary likes himself" is odd.

Binding theory divides nominal expressions into three types with different referential behaviors. **Anaphors** (reflexives like *himself*, *herself*, *themselves*, and reciprocals like *each other*) must be **bound** — must have a c-commanding antecedent — within a local domain called the **binding domain** (roughly, the minimal clause containing the anaphor). **Pronouns** like *him* and *her* must be **free** — must not have a c-commanding antecedent — within that same local domain, though they can co-refer with something outside it. **R-expressions** (full noun phrases like *John*, *the president*) must be free everywhere. These constraints are formalized as **Principles A, B, and C** respectively.

The elegance of binding theory is that it reduces a complex set of grammaticality patterns to three structural principles, all defined in terms of c-command and binding domains. Consider: "John told Bill about himself" — *himself* can only refer to John or Bill (whoever c-commands it within the clause), not to some discourse-external person. Compare: "John told Bill that he was wrong" — here *he* cannot refer to John or Bill within the relevant domain, so it must refer to someone mentioned elsewhere in discourse. The theory makes precise, testable predictions about what interpretations are and are not available.

Cross-linguistic evidence reveals that the binding domain is not universally fixed. In English, *himself* must find its antecedent within the minimal clause. But Icelandic has **long-distance reflexives** — reflexives that can refer to subjects in higher clauses across clause boundaries. This cross-linguistic variation is captured as **parameter variation** in how the binding domain is defined. The existence of these patterns across typologically diverse languages provides evidence that binding theory reflects a universal structural principle that languages parameterize differently — connecting directly to the broader generative grammar project of separating what is universal from what varies.
