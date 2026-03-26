---
id: case-theory-and-abstract-case
title: Case Theory and Abstract Case Assignment
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: minimalist-program-core-concepts
  type: hard
- id: morphological-structure
  type: hard
- id: binding-theory-anaphora-coreference
  type: soft
tags:
- syntax
- morphology
- case
stage: expert
status: validated
---
# Case Theory and Abstract Case Assignment

## Core Idea
Case theory explains how noun phrases receive morphological case (nominative, accusative, dative, etc.) through syntactic position and grammatical relations. In Minimalism, case is checked via feature agreement between functional heads and their dependents; failure to check case results in ungrammaticality.

## How It's Best Learned
Examine languages with rich case systems (Finnish, Japanese, German) to see how case tracks argument roles; study case-marking patterns in complex structures like passives and ditransitives.

## Common Misconceptions
Case is not merely morphology; abstract case exists even in languages with no morphological case realization and governs syntactic well-formedness.

## Questions

```yaml
- question: "English nouns do not show morphological case (the word 'dog' is identical whether subject or object). Yet linguists argue English has abstract case. The clearest evidence for this claim is:"
  type: multiple-choice
  options:
    - "English verbs agree with their subjects in person and number, showing a relationship between T and the subject NP"
    - "English pronouns must appear in accusative form after certain verbs (e.g., 'I expect *him* to leave,' not *'I expect *he* to leave')"
    - "English has prepositions that mark semantic roles where other languages use case endings"
    - "English word order is strictly SVO, which eliminates the need for case marking"
  answer: 1
  explanation: "The key evidence for abstract case in English is pronoun alternation in ECM (Exceptional Case Marking) constructions: 'I expect him to leave' is grammatical; 'I expect he to leave' is not. The only reason to use accusative *him* rather than nominative *he* is case assignment from the matrix verb to the subject of the infinitival complement. Since no morphological case appears on ordinary nouns here, this alternation reveals that the underlying syntactic system is tracking case even when it is not overtly realized. Option A (verb agreement) is about phi-features, not case. Options C and D describe surface properties without speaking to abstract case licensing."

- question: "In the passive sentence 'John was kicked (by Mary),' John appears in subject position. Abstract case theory explains this as:"
  type: multiple-choice
  options:
    - "A stylistic fronting rule that places patients before agents for emphasis"
    - "Obligatory: the passive morphology absorbs the verb's accusative case-assigning capacity, so John must move to the specifier of T to receive nominative case"
    - "Optional: 'Was kicked John by Mary' is an equally grammatical alternative with the same case assignment"
    - "An agreement effect: John moves to subject position so the verb can agree with it in number"
  answer: 1
  explanation: "In an active sentence, the verb assigns accusative case to its object. Passive morphology absorbs this case-assigning capacity — the verb can no longer value the accusative case feature of its internal argument. John, generated as the internal argument (direct object), now has an unvalued case feature that cannot be satisfied in its base position. The derivation forces movement to the specifier of T, where finite T can assign nominative case. This movement is not stylistic but case-driven: John must move or the derivation crashes. This is the abstract case theory account of subject raising in passives."

- question: "Abstract case theory primarily applies to languages that have visible, morphological case endings on nouns — languages like English, which lack overt case morphology on common nouns, are outside the theory's scope."
  type: true-false
  answer: false
  explanation: "Abstract case is precisely the claim that case is a syntactic requirement that holds independent of whether it surfaces morphologically. English lacks visible case on most nouns, but the pronoun alternation data (he/him, she/her, they/them) and the grammaticality contrasts in ECM constructions show that case is still being assigned and checked at the syntactic level. The theory's central insight is that languages like English 'hide' the system but still obey its logic — case governs syntactic well-formedness even when it is phonologically silent."

- question: "In the Minimalist Program, case is valued through Agree: a functional head (like T or v) probes downward, finds an NP with an unvalued case feature, and values it — licensing the NP to remain in the derivation."
  type: true-false
  answer: true
  explanation: "Agree is the core mechanism of feature valuation in Minimalism. A probe (a functional head with an uninterpretable feature) searches its c-command domain for a goal (an element with a matching but unvalued feature) and values it. For case: T probes for the closest NP with unvalued case and assigns nominative; v/V probes for its internal argument and assigns accusative. An NP that cannot find a probe to value its case feature causes the derivation to crash (the Case Filter). This is why every overt NP must appear in a position where a case-assigning head is accessible."

- question: "Why does abstract case theory predict that noun phrases sometimes must move from their base-generated positions to different syntactic positions?"
  type: short-answer
  answer: "Every overt NP must receive case or the derivation crashes. Some base-generated positions cannot provide case — most importantly, the subject of a non-finite (infinitival) clause cannot receive nominative from infinitival T, which lacks tense and therefore lacks case-assigning capacity. An NP stranded in such a position has an unvalued case feature that will crash the derivation. Movement is case-driven: the NP moves to the nearest position where a case-assigning functional head (typically finite T, assigning nominative) can value its case feature. Movement is thus not free but motivated by the need for case licensing."
  explanation: "This is what unifies apparently disparate phenomena — passivization, raising, ECM — under a single principle. In each case, an NP is base-generated in a position that cannot case-license it, and movement (or case assignment across a clause boundary) solves the problem. The cross-linguistic variation in how case is morphologically realized obscures the underlying unity, but abstract case theory reveals that the same syntactic requirement is operating across all languages."
```

## Explainer

From your study of morphological structure, you know that case endings on nouns mark grammatical roles — in Latin, *puella* (nominative, subject) vs. *puellam* (accusative, object). From your study of the Minimalist Program, you know that grammar is driven by feature checking: syntactic operations apply to satisfy formal requirements on lexical items. Case theory brings these two threads together: **case features** are a core mechanism through which noun phrases are licensed to appear in particular syntactic positions.

The key insight of **abstract case** is that case is not just a surface morphological phenomenon but a syntactic requirement that holds even when there is no visible marking. In English, nouns don't inflect for case on their surface form — "the dog" is the same whether subject or object. But English still obeys case constraints. Consider: "I expect him to win" (grammatical) vs. *"I expect he to win" (ungrammatical). The pronoun following "expect" must be accusative (*him*, not *he*), even though nothing visible on "him" tells you the syntactic structure. Abstract case theory says that every overt noun phrase must receive case, and that certain positions assign case while others don't. A noun phrase without case — **unvalued case feature** in Minimalist terms — causes the derivation to crash.

How does case get assigned? In the Minimalist Program, case is **valued through Agree**: a functional head like T (Tense) or v (little-v, the verb phrase–introducing head) has a case feature that probes downward, finds a goal (a noun phrase with unvalued case), and values it. Nominative case is assigned to the subject by T in its specifier position; accusative case is assigned to the object by v or by V itself. **Dative** case is assigned by a different functional head, often P (preposition) or by a ditransitive verb structure. In languages with richer morphology — German, Finnish, Russian, Japanese — these abstract assignments surface visibly, giving you direct evidence for the underlying structure. Languages like English "hide" the system but still follow its logic.

One of the most instructive case environments is **passivization**. In an active sentence "Mary kicked John," John receives accusative case from the verb. In the passive "John was kicked (by Mary)," the verb is morphologically changed — its accusative case-assigning capacity is **absorbed** by the passive morphology. John now must receive nominative case from T, which forces movement to the subject position. Abstract case theory thus explains movement: noun phrases move not randomly, but to reach positions where they can get their case valued. This same logic explains a range of cross-linguistic patterns, including why subjects of infinitival complements must sometimes appear as accusatives (they can't get nominative from the infinitival T, which lacks tense and therefore can't assign it) and why there are restrictions on what can appear in subject position in certain clause types.
