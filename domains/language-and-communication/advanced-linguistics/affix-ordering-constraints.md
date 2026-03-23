---
id: affix-ordering-constraints
title: Affix Ordering and Position Classes
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: morphological-structure
  type: hard
- id: distributed-morphology
  type: soft
tags:
- affix-ordering
- morphology
- position-classes
stage: expert
status: validated
---

# Affix Ordering and Position Classes

## Core Idea
Affixes attach in fixed orders: English prefixes precede the root, and suffixes follow in a predictable sequence (e.g., derivational before inflectional). This order is not random but reflects the structure of word formation: position classes define which affixes can occupy which slots. Violations of canonical affix order are rare and often involve special morphological processes (infixation, circumfixation), suggesting ordering constraints are fundamental to morphological systems.

## How It's Best Learned
Collect words with multiple affixes and determine the position class of each. Identify deviations and explain them as special morphological phenomena or exceptions.

## Common Misconceptions
- Affix order is not purely sequential; it may be hierarchically determined by the syntax-morphology interface.
- Deviations from canonical affix order are not arbitrary; they follow systematic principles.

## Questions

```yaml
- question: "Why do inflectional affixes appear at the outer edge of words, further from the root, compared to derivational affixes?"
  type: multiple-choice
  options:
    - "Inflectional affixes are historically older and so attach first in word history, ending up outermost"
    - "Derivational affixes are phonologically heavier and must be adjacent to the root for stress assignment"
    - "Inflectional affixes adjust a fully-formed word for its syntactic context, so they must be added after the word's lexical identity is established by derivational morphology"
    - "Inflectional affixes attach outside derivational ones by an arbitrary convention fixed in Proto-Indo-European"
  answer: 2
  explanation: "The ordering reflects the sequence of grammatical operations, not arbitrary convention or phonology. Derivational morphology builds the word's lexical identity — changing its category or meaning (un- + kind = unkind; unkind + -ness = unkindness). Inflectional morphology then adjusts that fully-formed word for its role in a sentence (tense, number, agreement). Since syntax operates on complete lexical items, inflectional affixes must be added last — outermost. This is not a coincidence; it reflects the architecture of grammar, from lexical construction outward to syntactic deployment."

- question: "A student analyzes the word 'unkindnesses' and argues that 'un-' should appear outside '-ness-' because prefixes precede the root while suffixes follow it. What is wrong with this analysis?"
  type: multiple-choice
  options:
    - "The prefix 'un-' is actually a suffix in this word, not a prefix"
    - "Both 'un-' and '-ness' are derivational affixes that sit inside the inflectional plural '-es' — the relevant distinction is derivational vs. inflectional, not prefix vs. suffix"
    - "Prefixes and suffixes are not distinguished in English morphology"
    - "The word 'unkindnesses' is not grammatical in standard English"
  answer: 1
  explanation: "The student's error is applying the wrong organizational principle. The relevant axis is not prefix/suffix (a positional description) but derivational/inflectional (a functional distinction). In 'unkindnesses,' both 'un-' and '-ness' are derivational — they build the word 'unkindness' from the root 'kind.' The plural '-es' is inflectional, adjusting the fully-formed noun for syntactic use. The correct structure is [[un-[kind]-ness]-es]: derivational operations are nested inside the inflectional one, regardless of whether the derivational morpheme is a prefix or suffix. Position relative to the root is a different question from position in the hierarchy of operations."

- question: "Affix ordering in human languages is an arbitrary convention that varies freely across languages without principled explanation."
  type: true-false
  answer: false
  explanation: "Affix ordering reflects universal properties of grammar — specifically, the sequence of operations that build words (derivational morphology) before placing them in syntactic structures (inflectional morphology). Across typologically diverse languages with very different surface structures, this inside-out ordering tendency is systematic and cross-linguistically robust. It is not arbitrary, and it does not vary freely. Apparent exceptions (infixes, circumfixes) follow their own systematic principles (prosodic constraints, bracketing morphology) — they are not random violations but alternative morphological processes with their own logic."

- question: "The English expletive infix ('fan-f***ing-tastic') appears to violate positional ordering rules but actually follows systematic prosodic constraints — it appears before the main-stressed syllable of the host word."
  type: true-false
  answer: true
  explanation: "This is an important test case for the broader principle: apparent violations of affix ordering are not random exceptions but reveal alternative systematic processes. Infixes in English follow a prosodic rule: they insert before the primary stressed syllable of the host. This is why 'a-b-s-o-f***ing-lutely' inserts before '-lute-' (the stressed syllable), not at the beginning or end of the word. The systematic nature of the exception confirms the rule: whenever affix order seems irregular, there is an alternative process operating, not unexplained chaos."

- question: "Explain why derivational affixes appear closer to the root than inflectional affixes, in terms of the sequence of grammatical operations they represent."
  type: short-answer
  answer: "Derivational morphology performs the 'inner' operation of building a word's lexical identity — changing its syntactic category (verb → noun), altering its meaning (kind → unkind), or creating a new lexical item. This operation must happen first because inflectional morphology takes a fully-formed word as its input and adjusts it for its syntactic context (marking tense, number, agreement). Syntax then operates on words that have already been fully inflected. The ordering reflects this causal sequence: derivation builds the word, inflection fits it to its grammatical slot, syntax deploys it. Since derivational affixes are added in the earlier operation, they are structurally interior — closer to the root — and inflectional affixes, added in the later operation, appear at the outer edge."
  explanation: "The key is to see affix ordering not as a surface fact about word shape but as a window into the sequential architecture of grammar. Understanding this explains why the pattern is cross-linguistically robust: it reflects something deep about how word formation and syntax are sequenced, not an arbitrary rule of any particular language."
```

## Explainer

From your study of morphological structure, you know that words are built from meaningful units — roots, prefixes, and suffixes — assembled according to systematic rules. But one question morphological structure leaves open is: when a word takes multiple affixes, why do they appear in the order they do? You cannot say *un-kind-ness* and then freely rearrange it as *kind-un-ness* or *ness-un-kind*. The order is fixed, and the study of affix ordering constraints explains why.

The core concept is **position class**: a slot in the word-template that can be filled by a specific set of affixes. Think of it like a template with numbered positions: [PREFIX-2] [PREFIX-1] [ROOT] [SUFFIX-1] [SUFFIX-2] [SUFFIX-3]. Each position has a defined role, and affixes belong to exactly one position class. In English, derivational affixes (which change a word's category or meaning: *-ness*, *-ful*, *un-*, *re-*) generally appear closer to the root, while inflectional affixes (which mark grammatical relationships: *-s*, *-ed*, *-ing*) appear at the outer edges. So you get *un-kind-ness-es* (prefix + root + derivational suffix + plural), not *un-ness-kind-es*. This isn't a coincidence — it reflects the hierarchical structure of word formation.

Why does derivational morphology sit inside inflectional morphology? The answer connects to the syntax-morphology interface you may have encountered in distributed morphology. Derivational operations are part of building the lexical item itself — changing what the word *is*. Inflectional operations are added later, adjusting the word for its syntactic context (tense, number, agreement). Since syntax operates on fully-formed words, inflectional affixes must be added after the word's core meaning is established. The ordering is therefore not arbitrary: it reflects the sequence of operations in grammar, from lexical construction outward to syntactic deployment.

**Violations** of canonical affix order are rare but informative. **Infixes** — affixes inserted inside a root (the English expletive infix in *fan-f\*\*king-tastic*) — appear to break positional rules but in fact follow their own predictable prosodic constraints (they appear before the main-stressed syllable). **Circumfixes** bracket the root with simultaneous prefix and suffix (*ge-...-t* in German past participles). These exceptional cases confirm the rule by showing that deviations are systematic, not random — they follow alternative morphological processes with their own logic. Whenever affix ordering seems irregular, the linguist's task is to identify which alternative process is operating, not to treat the deviation as an unexplained exception.
