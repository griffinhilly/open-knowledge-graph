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

## Questions

```yaml
- question: "In the sentence 'John told Bill about himself,' the reflexive 'himself' can refer to John or Bill but not to some other person mentioned in prior discourse. Which principle of binding theory explains this?"
  type: multiple-choice
  options:
    - "Principle B — pronouns must be free within the binding domain"
    - "Principle C — R-expressions must be free everywhere"
    - "Principle A — anaphors must be bound within the binding domain"
    - "The binding domain parameter — reflexives in English are always clause-local"
  answer: 2
  explanation: "Principle A states that anaphors (including reflexives like 'himself') must be bound — must have a c-commanding antecedent — within their binding domain. In this sentence, the binding domain is the clause, and both 'John' and 'Bill' c-command 'himself' within it. A discourse-external person cannot serve as antecedent because Principle A requires the antecedent to be within the local clause. Option D correctly names the locality restriction but misidentifies its source as parameterization rather than Principle A itself."

- question: "A student argues: 'The sentence \"John likes him\" sounds weird if \"him\" refers to John, so binding theory classifies it as merely pragmatically dispreferred.' What is the error in this reasoning?"
  type: multiple-choice
  options:
    - "The student is correct — Principle B makes local co-reference merely dispreferred, not ungrammatical"
    - "Binding constraints are structural grammaticality rules, not pragmatic preferences — Principle B makes that co-reference ungrammatical, not just awkward"
    - "Principle B only blocks co-reference when the pronoun and antecedent are adjacent"
    - "Principle B applies only to reciprocals, not to pronouns like 'him'"
  answer: 1
  explanation: "The Common Misconception in binding theory is treating the constraints as pragmatic preferences rather than grammaticality conditions. Binding theory makes categorical predictions: a sentence violating Principle B is ungrammatical with the local co-referential interpretation — not just awkward or dispreferred. The constraints are defined over structural relations (c-command, binding domains) that either hold or don't, producing categorical rather than gradient judgments."

- question: "Binding constraints are structural grammaticality rules, not merely pragmatic preferences about which interpretations 'sound right.'"
  type: true-false
  answer: true
  explanation: "This is the core methodological point of binding theory: the constraints predict categorical grammaticality, not gradient acceptability. 'John hurt himself' is grammatical with local co-reference; 'Himself hurt John' is ungrammatical. The constraints are categorical because they are defined over structural relations (c-command, binding domains) that either hold or don't. Pragmatic factors may influence what interpretations are preferred in context, but they operate on top of the grammaticality constraint, not instead of it."

- question: "The fact that Icelandic reflexives can refer to subjects in higher clauses across clause boundaries shows that binding theory's claim about binding domains is incorrect."
  type: true-false
  answer: false
  explanation: "Icelandic long-distance reflexives don't refute binding theory — they motivate it to treat the binding domain as a parameterized variable rather than a fixed universal. The universal principle is that anaphors must be bound within their binding domain; the parameter is how each language fixes the boundaries of that domain. Icelandic defines its binding domain more broadly than English. Cross-linguistic variation is evidence for parameterization within the theory, not against the theory itself."

- question: "Why must anaphors and pronouns have complementary distributions within a binding domain? What would break down if a pronoun could have a local c-commanding antecedent?"
  type: short-answer
  answer: "If pronouns could co-refer with local c-commanding noun phrases, the distinction between pronouns and reflexives would collapse within that domain — both could take local antecedents. Languages maintain the contrast because reflexives signal bound, local co-reference (Principle A) while pronouns signal non-local or free reference (Principle B). Allowing pronoun-antecedent co-reference locally would create systematic ambiguity between 'John hurt him' (someone else) and 'John hurt himself' (John), undermining the expressive distinction these forms encode."
  explanation: "The complementarity of Principles A and B is not accidental — it creates a complementary distribution of anaphors and pronouns that allows speakers to reliably signal whether co-reference is local or non-local. This is a productive grammatical contrast that speakers exploit without conscious awareness."
```

## Explainer

From your study of X-bar theory, you have a structural representation of sentences as hierarchically organized phrase trees. From your study of c-command and binding, you know the key structural relationship: node A **c-commands** node B if every branching node dominating A also dominates B. Binding theory uses c-command to explain a puzzle any English speaker has implicit knowledge of: why "John hurt himself" is grammatical (himself refers to John) but "Himself hurt John" is not, and why "John thinks Mary likes him" allows *him* to refer to someone other than John but "John thinks Mary likes himself" is odd.

Binding theory divides nominal expressions into three types with different referential behaviors. **Anaphors** (reflexives like *himself*, *herself*, *themselves*, and reciprocals like *each other*) must be **bound** — must have a c-commanding antecedent — within a local domain called the **binding domain** (roughly, the minimal clause containing the anaphor). **Pronouns** like *him* and *her* must be **free** — must not have a c-commanding antecedent — within that same local domain, though they can co-refer with something outside it. **R-expressions** (full noun phrases like *John*, *the president*) must be free everywhere. These constraints are formalized as **Principles A, B, and C** respectively.

The elegance of binding theory is that it reduces a complex set of grammaticality patterns to three structural principles, all defined in terms of c-command and binding domains. Consider: "John told Bill about himself" — *himself* can only refer to John or Bill (whoever c-commands it within the clause), not to some discourse-external person. Compare: "John told Bill that he was wrong" — here *he* cannot refer to John or Bill within the relevant domain, so it must refer to someone mentioned elsewhere in discourse. The theory makes precise, testable predictions about what interpretations are and are not available.

Cross-linguistic evidence reveals that the binding domain is not universally fixed. In English, *himself* must find its antecedent within the minimal clause. But Icelandic has **long-distance reflexives** — reflexives that can refer to subjects in higher clauses across clause boundaries. This cross-linguistic variation is captured as **parameter variation** in how the binding domain is defined. The existence of these patterns across typologically diverse languages provides evidence that binding theory reflects a universal structural principle that languages parameterize differently — connecting directly to the broader generative grammar project of separating what is universal from what varies.
