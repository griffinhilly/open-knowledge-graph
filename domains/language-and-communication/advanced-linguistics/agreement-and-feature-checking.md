---
id: agreement-and-feature-checking
title: Agreement and Feature Checking in Syntax
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: minimalist-program-core-concepts
  type: hard
- id: morpheme-types
  type: hard
tags:
- syntax
- morphology
- agreement
stage: expert
status: draft
---

# Agreement and Feature Checking in Syntax

## Core Idea
Agreement is systematic covariation of morphosyntactic features (person, number, gender) between sentence elements, as in subject-verb agreement. Feature-checking theory explains agreement as matching and elimination of interpretable/uninterpretable feature pairs during syntactic derivation, a core mechanism in current generative syntax.

## How It's Best Learned
Map agreement patterns across diverse languages; study cases where agreement breaks down (collective nouns, coordinated subjects) to understand when feature matching applies.

## Common Misconceptions
Agreement is not just copying information; it is driven by checked features and reflects deep syntactic relationships, not mere surface pattern-matching.

## Questions

```yaml
- question: "A speaker says 'The key to the cabinets are on the table,' agreeing the verb with 'cabinets' rather than 'key.' In feature-checking terms, this error is best explained as:"
  type: multiple-choice
  options:
    - "The speaker correctly checking T's uninterpretable feature against the closest DP bearing an interpretable number feature"
    - "A processing failure in which the nearby plural noun 'cabinets' interferes with feature checking against the head noun 'key'"
    - "Evidence that plural verbs carry interpretable number features in English"
    - "The derivation crashing and being rescued by the adjacent plural feature"
  answer: 1
  explanation: "This is 'agreement attraction' — a well-documented production error. In feature-checking theory, T's uninterpretable number feature should be checked against the interpretable number feature on the subject 'key' (singular). The error occurs because 'cabinets,' though inside a PP modifying the head noun, is the closest overt plural during processing, and its interpretable [plural] feature interferes with the correct checking operation. This shows feature checking is not purely syntactic — it is also a real-time cognitive process subject to interference."

- question: "What happens to uninterpretable features after successful feature checking in the Minimalist framework?"
  type: multiple-choice
  options:
    - "They are transferred from the verb to the noun phrase, which then expresses the shared feature"
    - "They are deleted, allowing the derivation to proceed to the phonological and semantic interfaces"
    - "They are retained on the verb and interpreted compositionally at the semantic interface"
    - "They trigger a second round of Merge to create additional agreement morphology"
  answer: 1
  explanation: "Uninterpretable features must be deleted before the derivation reaches the interfaces — they would appear as uninterpretable material at the Logical Form interface, causing the derivation to crash. Feature checking licenses this deletion: when an uninterpretable feature is matched against a corresponding interpretable feature, it is eliminated. This is why grammaticality correlates with feature matching: unmatched uninterpretable features cannot be deleted, and undeleted uninterpretable features cause interface failure."

- question: "The verb's agreement morpheme in 'The boy runs' has an interpretable number feature, because singular agreement conveys the meaning that the subject is singular."
  type: true-false
  answer: false
  explanation: "Only the noun's number feature is interpretable — there really is one boy in 'The boy runs,' and that singularity is part of the noun's semantic content. The verb's agreement morpheme is uninterpretable: 'runs' adds no new information about number that isn't already conveyed by 'boy.' The verb's agreement feature exists purely to be checked against the noun's interpretable feature and then deleted. This asymmetry — interpretable on nouns, uninterpretable on verbs — is what makes agreement a feature-checking operation rather than simple semantic co-reference."

- question: "In the Minimalist framework, the subject DP moving to [Spec,TP] creates the structural configuration needed for its features to be checked against the Tense head."
  type: true-false
  answer: true
  explanation: "Feature-checking relations require local structural relationships — typically a specifier-head or head-complement configuration. The subject raises to [Spec,TP] not primarily for semantic reasons but to satisfy feature-checking requirements: T carries uninterpretable phi-features (person, number) that can only be matched and deleted when a DP with interpretable phi-features occupies the appropriate structural position. Movement is thus driven by the need to establish checking configurations."

- question: "What is the difference between an interpretable and an uninterpretable feature in the Minimalist framework, and why must uninterpretable features be checked and deleted before the derivation reaches the interfaces?"
  type: short-answer
  answer: "An interpretable feature contributes semantic content: the plural feature on 'boys' is interpretable because it means there are multiple boys. An uninterpretable feature is a purely grammatical marker with no independent semantic content: the plural agreement morpheme on a verb simply mirrors the noun's number without adding new meaning. At the Logical Form interface, only interpretable features can be processed — uninterpretable features are semantically vacuous and would cause the derivation to crash if they survived. Feature checking is the mechanism that eliminates them: by entering a checking relation with a matching interpretable feature, the uninterpretable feature is licensed for deletion."
  explanation: "This asymmetry is what makes agreement non-trivial in the Minimalist framework. It reframes agreement not as 'copying information' (a surface description) but as a derivational necessity: the grammar forces a checking relation between elements because uninterpretable features must be eliminated for the output to be interpretable at the interfaces. The grammaticality of a sentence turns on whether all uninterpretable features can find checking partners."
```

## Explainer

From the Minimalist Program, you already know that syntactic derivations operate by assembling structures through operations like **Merge** and **Move**, and that morphemes — from your morphology prerequisite — are the minimal meaning-bearing units that surface as affixes and free forms. Agreement is the phenomenon that links these two domains: it is the mechanism by which morphosyntactic information is shared between different elements in a sentence, and feature-checking theory is the Minimalist explanation for *how* that sharing is constrained and enforced.

Consider a simple example: *The boy runs* vs. *The boys run*. The verb changes its form depending on the number of the subject — not because the verb "sees" the subject directly, but because both the subject and the verb carry **features** (in this case, [singular] or [plural], combined with person features) that must be put into correspondence during the derivation. In the Minimalist framework, features come in two types: **interpretable features** are those that contribute semantic content (the noun *boys* is genuinely plural — there are multiple boys), while **uninterpretable features** are purely grammatical markers that exist only to trigger agreement. The verb *runs* carries an uninterpretable number feature that has no independent meaning — it is a grammatical reflex that must be checked against an interpretable feature on the noun in order to be licensed in the derivation.

**Feature checking** is the operation that resolves this. When a functional head (like T, the Tense head in the clause) enters into a checking relation with a DP (the subject), the uninterpretable features on T are matched against the interpretable features of the DP. If they match (both [plural], both third person), the uninterpretable features are deleted — the derivation proceeds. If they don't match, the derivation crashes at the interface, which is why *the boy run* is ungrammatical: the features don't check. Movement (the subject DP raising to [Spec,TP]) is often what brings the two elements into the checking configuration.

The power of this framework becomes clear when you look at cases where agreement breaks down in interesting ways. Collective nouns in English (*the committee have decided*, common in British English) show that agreement can target **notional** rather than **grammatical** number — the noun is singular in form but plural in meaning, and speakers vacillate between the two. **Agreement attraction** — a processing error where speakers produce *the key to the cabinets are* because the plural noun *cabinets* is nearby — shows that feature checking is not just a syntactic operation but also a real-time cognitive process subject to interference. Cross-linguistic variation adds further richness: many languages show **differential object marking** (agreement applies to some objects but not others based on animacy or definiteness), **inverse systems** where agreement reflects which participant outranks the other on a salience hierarchy, or **polypersonal morphology** where a single verb simultaneously marks agreement with multiple arguments. All of these patterns, despite their surface diversity, reflect the same underlying logic: morphosyntactic features on different elements must be put into correspondence, and the mechanisms of feature checking determine when, how, and with what consequences.
