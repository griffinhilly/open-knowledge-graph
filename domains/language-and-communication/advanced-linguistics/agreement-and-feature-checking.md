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
stage: advanced
status: draft
---

# Agreement and Feature Checking in Syntax

## Core Idea
Agreement is systematic covariation of morphosyntactic features (person, number, gender) between sentence elements, as in subject-verb agreement. Feature-checking theory explains agreement as matching and elimination of interpretable/uninterpretable feature pairs during syntactic derivation, a core mechanism in current generative syntax.

## How It's Best Learned
Map agreement patterns across diverse languages; study cases where agreement breaks down (collective nouns, coordinated subjects) to understand when feature matching applies.

## Common Misconceptions
Agreement is not just copying information; it is driven by checked features and reflects deep syntactic relationships, not mere surface pattern-matching.

## Explainer

From the Minimalist Program, you already know that syntactic derivations operate by assembling structures through operations like **Merge** and **Move**, and that morphemes — from your morphology prerequisite — are the minimal meaning-bearing units that surface as affixes and free forms. Agreement is the phenomenon that links these two domains: it is the mechanism by which morphosyntactic information is shared between different elements in a sentence, and feature-checking theory is the Minimalist explanation for *how* that sharing is constrained and enforced.

Consider a simple example: *The boy runs* vs. *The boys run*. The verb changes its form depending on the number of the subject — not because the verb "sees" the subject directly, but because both the subject and the verb carry **features** (in this case, [singular] or [plural], combined with person features) that must be put into correspondence during the derivation. In the Minimalist framework, features come in two types: **interpretable features** are those that contribute semantic content (the noun *boys* is genuinely plural — there are multiple boys), while **uninterpretable features** are purely grammatical markers that exist only to trigger agreement. The verb *runs* carries an uninterpretable number feature that has no independent meaning — it is a grammatical reflex that must be checked against an interpretable feature on the noun in order to be licensed in the derivation.

**Feature checking** is the operation that resolves this. When a functional head (like T, the Tense head in the clause) enters into a checking relation with a DP (the subject), the uninterpretable features on T are matched against the interpretable features of the DP. If they match (both [plural], both third person), the uninterpretable features are deleted — the derivation proceeds. If they don't match, the derivation crashes at the interface, which is why *the boy run* is ungrammatical: the features don't check. Movement (the subject DP raising to [Spec,TP]) is often what brings the two elements into the checking configuration.

The power of this framework becomes clear when you look at cases where agreement breaks down in interesting ways. Collective nouns in English (*the committee have decided*, common in British English) show that agreement can target **notional** rather than **grammatical** number — the noun is singular in form but plural in meaning, and speakers vacillate between the two. **Agreement attraction** — a processing error where speakers produce *the key to the cabinets are* because the plural noun *cabinets* is nearby — shows that feature checking is not just a syntactic operation but also a real-time cognitive process subject to interference. Cross-linguistic variation adds further richness: many languages show **differential object marking** (agreement applies to some objects but not others based on animacy or definiteness), **inverse systems** where agreement reflects which participant outranks the other on a salience hierarchy, or **polypersonal morphology** where a single verb simultaneously marks agreement with multiple arguments. All of these patterns, despite their surface diversity, reflect the same underlying logic: morphosyntactic features on different elements must be put into correspondence, and the mechanisms of feature checking determine when, how, and with what consequences.
