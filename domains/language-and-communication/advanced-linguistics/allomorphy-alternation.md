---
id: allomorphy-alternation
title: Allomorphy and Phonologically-Conditioned Alternation
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: morpheme-types
  type: hard
- id: morphological-structure
  type: hard
- id: morphological-composition
  type: soft
tags:
- allomorphy
- morphology
- variation
stage: advanced
status: validated
---

# Allomorphy and Phonologically-Conditioned Alternation

## Core Idea
Allomorphs are variant forms of a single morpheme, triggered by phonological context or morphological properties. The English plural -s surfaces as [z] after voiced sounds, [s] after voiceless sounds, [əz] after sibilants—this phonologically-conditioned allomorphy follows from phonological rules. Suppletive allomorphy (go/went) and morphologically-conditioned allomorphy (English man/men) require lexical specification. Understanding allomorphy determines the inventory of underlying morphemes.

## How It's Best Learned
Identify allomorphic variants of a morpheme across contexts, determine whether conditioning is phonological, morphological, or arbitrary, and write rules or constraints deriving the distribution.

## Common Misconceptions
- Allomorphy is not always rule-based; some allomorphic relationships are lexically specified or reflect historical sound change.
- The same surface alternation might be phonological in one language and morphological in another.

## Questions

```yaml
- question: "An English speaker correctly produces 'dogs' [dɒgz], 'cats' [kæts], and 'buses' [bʌsɪz] without being explicitly taught these forms. A linguist analyzing these plural forms should conclude:"
  type: multiple-choice
  options:
    - "These are three distinct plural morphemes with slightly different grammatical meanings"
    - "These are three allomorphs of a single plural morpheme, with the choice conditioned by the phonological environment of the stem — voiced non-sibilant → [z], voiceless non-sibilant → [s], sibilant → [əz]"
    - "These forms must be stored individually as lexical entries because the variation is unpredictable"
    - "These are morphologically-conditioned allomorphs, like man/men, that require lexical class specifications"
  answer: 1
  explanation: "The distribution of [z], [s], and [əz] is entirely predictable from the phonological environment of the stem — it is phonologically-conditioned allomorphy. Positing three separate morphemes misses the generalization that they are in complementary distribution and their distribution follows from the phonology of the language. A single underlying form plus a phonological rule (or set of constraints) explains the three forms with less machinery than three separate entries. Native speakers extend this pattern automatically to novel words (e.g., 'blicks' → [blɪks]), proving the rule is productive."

- question: "Which of the following is the clearest example of suppletive allomorphy?"
  type: multiple-choice
  options:
    - "The English plural alternation: [z] in 'dogs,' [s] in 'cats,' [əz] in 'buses'"
    - "The English present/past alternation in 'go' / 'went'"
    - "The [f]/[v] alternation in 'leaf' / 'leaves'"
    - "The vowel change in 'sing' / 'sang'"
  answer: 1
  explanation: "'Go' and 'went' are the canonical example of suppletive allomorphy: the past tense form is historically from an entirely different verb (*wend*), and no phonological rule derives 'went' from 'go.' The relationship must be stored as an arbitrary lexical pairing. By contrast, the plural alternation ([z]/[s]/[əz]) follows a productive phonological rule; 'leaf/leaves' reflects a semi-regular morphological class; 'sing/sang' follows an ablaut pattern shared by other strong verbs. Suppletive allomorphs are the residue that cannot be derived by rule — pure lexical accidents of history."

- question: "Suppletive allomorphs like 'go/went' and 'good/better/best' must be stored as separate lexical entries in the grammar because no productive phonological or morphological rule can derive one form from the other."
  type: true-false
  answer: true
  explanation: "Correct. The goal of morphophonological analysis is to reduce surface alternations to a single underlying form plus rules wherever possible. When no rule captures the alternation — because the relationship is historically arbitrary — the grammar has no choice but to list the forms separately. Suppletive forms are identified by the diagnostic that native speakers do not extend them to new words: you cannot form the plural of a new noun using vowel change (*'mouses' → [maɪs]?), and children must learn 'went' explicitly rather than deriving it from 'go.'"

- question: "Because [z], [s], and [əz] are three different surface forms, they represent three separate plural morphemes in the grammar of English."
  type: true-false
  answer: false
  explanation: "This is the key mistake in analyzing allomorphy. Having different surface forms does not imply different underlying morphemes. The three forms are in complementary distribution (each appears in a distinct, non-overlapping environment) and collectively cover all plural contexts — the hallmark of allomorphs of a single morpheme. Positing three morphemes makes the grammar redundant: it lists three entries where one plus a rule would suffice, and it fails to capture the generalization that all three mark plurality. Morpheme identity is determined by function and distribution, not surface form."

- question: "Why do linguists prefer to analyze the English plural [z/s/əz] as one morpheme with phonologically-conditioned allomorphs rather than as three separate morphemes? What analytical principle motivates this choice?"
  type: short-answer
  answer: "The three-morpheme analysis duplicates information: it lists three separate entries that all mean 'plural,' without explaining why they appear in mutually exclusive environments. The one-morpheme analysis captures the generalization that the alternation is entirely predictable from the phonological context of the stem — voiced non-sibilant, voiceless non-sibilant, sibilant — using a single rule rather than arbitrary listing. The guiding principle is economy: prefer the analysis that captures alternations as productive rules over one that treats them as coincidental. Suppletive allomorphs are the exceptions that cannot be derived by rule; phonologically-conditioned allomorphs are the norm that reveals the language's phonological grammar."
  explanation: "This is the core methodological principle of morphophonology: reduce surface complexity to underlying simplicity through rules. The morpheme inventory should be as small as possible while still accounting for the data."
```

## Explainer

From your study of morpheme types and morphological structure, you know that words are built from smaller meaningful units — morphemes — and that these units combine in systematic ways. Allomorphy is what happens when the same morpheme shows up in different phonological shapes depending on context. The key conceptual move is distinguishing the **morpheme** (the abstract unit of meaning) from the **morph** (the actual phonological form). A single morpheme can have multiple morphs — those are its allomorphs.

The English plural is the clearest example to start with. The plural morpheme is one thing — it means "more than one" — but it surfaces as three different sounds: [z] in *dogs*, [s] in *cats*, and [əz] in *buses*. This is **phonologically-conditioned allomorphy**: the choice of allomorph is fully predictable from the phonological environment. After a voiced consonant or vowel, you get [z]; after a voiceless consonant (other than a sibilant), you get [s]; after a sibilant, you get [əz]. No one taught you this rule explicitly — you generalized it from input as a child — but it operates consistently. The analysis task is to take the three surface forms, identify the conditioning environment for each, and reduce them to a single underlying representation plus a rule (or constraint set) that derives them.

**Suppletive allomorphy** is the other end of the spectrum. *Go* and *went* are allomorphs of the same verb — the past tense of "go" — but no phonological rule derives *went* from *go*. The relationship is historically arbitrary, a relic of the merger of two different Old English verbs. These must be **lexically specified**: the grammar simply stores the pair. Similarly, *man/men* and *mouse/mice* are morphologically-conditioned allomorphs of the noun plural, where the alternation follows from the word's lexical class (historically, the old Germanic *umlaut* plural), not from the phonological environment. The analytical challenge is figuring out *which* type of conditioning is at work in any given case.

Why does this matter? Because identifying the correct allomorphic analysis determines your morpheme inventory — the set of underlying units your grammar operates over. If you treat [z], [s], and [əz] as three separate plural morphemes, your grammar becomes redundant and misses the generalization. If you posit one underlying form and a phonological rule, you capture the generalization with less machinery. This is the core principle of morphophonological analysis: prefer the analysis that captures alternations as regular rules over one that requires arbitrary lexical listings. Suppletive forms are the residue that cannot be derived by rule — they are the cases where the historical generalization has been lost, and the grammar has no choice but to memorize.
