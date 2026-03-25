---
id: case-systems-typology
title: Case Systems and Their Typological Variation
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: linguistic-typology
  type: hard
- id: grammaticalization-mechanisms
  type: soft
- id: case-theory-and-abstract-case
  type: soft
- id: ergative-absolutive-alignment
  type: soft
- id: alignment-systems-typology
  type: soft
tags:
- case
- typology
- morphology
stage: expert
status: validated
---
# Case Systems and Their Typological Variation

## Core Idea
Case systems mark grammatical and semantic relationships through morphological forms on nouns and modifiers. Languages vary enormously: English has minimal case (he/him), while Finnish has 15 cases. Cases encode grammatical function (nominative for agents, accusative for patients) and semantic relations (locative, instrumental, comitative). The inventory and functions of cases correlate with word order and other morphosyntactic properties.

## How It's Best Learned
Map case systems across several languages, identifying the semantic and grammatical functions of each case. Examine how case systems relate to word-order properties and other morphological systems.

## Common Misconceptions
- Case systems are not static; cases grammaticalize and change over time.
- A single case form may express multiple functions; polyfunctionality is common.

## Questions

```yaml
- question: "In an ergative-absolutive language, how is the subject of an intransitive verb marked relative to the object of a transitive verb?"
  type: multiple-choice
  options:
    - "The intransitive subject takes the ergative case; the transitive object takes the absolutive case"
    - "Both take the absolutive case — ergative-absolutive groups these 'affected' participants together"
    - "Both take the nominative case, just as in nominative-accusative languages"
    - "The intransitive subject takes the absolutive; the transitive object takes the ergative"
  answer: 1
  explanation: "Ergative-absolutive alignment groups the subject of intransitive verbs and the object of transitive verbs into the absolutive case, while the subject of a transitive verb (the agent) takes the ergative. The conceptual logic is that both the intransitive subject and the transitive object are 'undergoers' or less-agentive participants — the system groups by participant role rather than by syntactic subjecthood. This is the opposite of nominative-accusative, which groups both transitive and intransitive subjects (regardless of agentivity) under nominative."

- question: "Why do languages with richer case systems tend to have freer word order?"
  type: multiple-choice
  options:
    - "Languages with many cases have smaller vocabularies and therefore need word order variation to express nuance"
    - "Because case suffixes carry the relational information (who is agent, who is patient), word position can vary without creating ambiguity"
    - "Richer case systems arise only in head-final languages, which happen to have freer ordering by coincidence"
    - "Free word order makes case necessary as a compensatory strategy; case richness follows from word-order freedom, not the reverse"
  answer: 1
  explanation: "Case marking encodes the grammatical and semantic relationships between noun phrases. When a suffix reliably signals 'this NP is the agent' regardless of its position in the sentence, scrambling word order does not produce ambiguity. English, which has almost no case marking, relies heavily on fixed SVO order to signal these relations — 'the dog bit the man' vs. 'the man bit the dog' differ only in position. Latin, with its rich case system, allowed essentially free ordering of major constituents without loss of clarity. This is one of the cleaner typological correlations in the literature."

- question: "A single case form in a language can legitimately encode multiple distinct semantic functions — for example, instrument, agent, source, and location."
  type: true-false
  answer: true
  explanation: "Polyfunctionality is the norm, not the exception. The Latin ablative is the textbook example: it serves as an instrument ('with a sword'), passive agent ('by Caesar'), source ('from Rome'), location ('in the forum'), and comparative ('better than gold'). These functions are semantically related through grammaticalization history but are not reducible to a single primitive meaning. This has an important implication: parsing a case form correctly requires knowing the surrounding clause structure and lexical semantics — not just the case label. Students who learn 'ablative = instrument' miss this polyfunctional reality."

- question: "In an ergative-absolutive language, the subject of a transitive verb and the subject of an intransitive verb are marked with the same case form."
  type: true-false
  answer: false
  explanation: "This is the nominative-accusative pattern, not the ergative-absolutive pattern. In ergative-absolutive languages, the subject of a transitive verb (the agent) takes the *ergative* case — a special form reserved for agents of transitive actions — while the subject of an intransitive verb takes the *absolutive*, grouping it with the transitive object. This is the defining feature of ergative alignment and represents a fundamentally different way of grammatically categorizing participants in events. The confusion arises from applying nominative-accusative intuitions to all case systems."

- question: "What is the key conceptual difference between nominative-accusative and ergative-absolutive alignment, and what does each system group together?"
  type: short-answer
  answer: "Nominative-accusative alignment groups subjects together regardless of transitivity: both the subject of a transitive verb ('she saw him') and the subject of an intransitive verb ('she ran') take nominative case. The object of a transitive verb takes accusative. Ergative-absolutive alignment instead groups 'undergoer' participants: the subject of an intransitive verb and the object of a transitive verb both take absolutive, while only the agent of a transitive verb takes the special ergative form. Nom-acc groups by subjecthood; erg-abs groups by agentivity and affectedness."
  explanation: "The typological significance is that these two systems represent different cognitive or grammatical stances toward event structure. Nom-acc treats subjecthood as the primary grammatical category; erg-abs treats agentivity in a transitive event as the marked category requiring special morphological recognition. Neither system is more 'logical' than the other — they are alternative solutions to the same problem of encoding participant roles."
```

## Explainer

From your study of linguistic typology, you know that languages vary systematically in their morphosyntactic strategies — and case systems are one of the most dramatic sites of this variation. A **case system** is a set of morphological forms on nouns (and often adjectives and pronouns) that signal the noun's grammatical role or semantic relationship within the clause. The core function is relational: case tells you how a noun phrase relates to the verb and to other noun phrases. English has almost entirely lost this system — only pronouns still reflect it (*he* vs. *him*, *she* vs. *her*) — but this minimal residue shows you what case does: *he saw her* and *her saw he* are formally distinct because the case forms signal who is the subject (agent) and who is the object (patient).

Languages are classified by which distinctions their case systems mark. The most widely attested case is the **nominative-accusative** alignment: the subject of both transitive and intransitive verbs takes one form (nominative), while the object of a transitive verb takes another (accusative). Latin, German, Russian, and most Indo-European languages with case follow this pattern. A competing pattern is **ergative-absolutive** alignment, found in Basque, Georgian, and many Australian Aboriginal languages: here, the subject of an intransitive verb and the object of a transitive verb take one form (absolutive), while the subject of a transitive verb (the agent doing something to someone) takes a special form (ergative). The conceptual difference is striking — ergative systems group "affected participants" together rather than grouping "subjects" together as nominative-accusative languages do. Your typological background lets you ask: why would languages converge on this alternative grouping? The answer connects to how languages conceptualize events and participants.

Beyond these core structural cases, languages add **semantic cases** encoding spatial and other relations that English expresses with prepositions. Finnish, which you may encounter as a benchmark for case-rich systems, has 15 cases including the *inessive* (inside: "in the house"), *elative* (out of: "from the house"), *illative* (into: "into the house"), *adessive* (on/at: "at the house"), *ablative* (away from surface: "from the house's surface"), and *allative* (toward surface: "to the house"). These are not grammatical cases in the nominative-accusative sense — they are essentially **postpositions** that have been grammaticalized onto the noun, a process your knowledge of grammaticalization mechanisms helps you recognize. This is not random: languages with richer case systems tend to have freer word order, because when case suffixes carry the relational information, word order can vary without ambiguity. The correlation between case richness and word-order freedom is one of the cleaner typological patterns in the literature.

The **polyfunctionality** of case forms is important to internalize. The Latin *ablative* case serves as an instrument ("with a sword"), an agent in passive constructions ("by Caesar"), a source ("from Rome"), a location ("in the forum"), and a comparison ("better than gold"). These functions are semantically related through a family-resemblance logic — many developed through grammaticalization from more specific spatial meanings — but they are not reducible to a single semantic primitive. This polyfunctionality means that case systems require contextual interpretation; the same suffix can only be correctly parsed given knowledge of the surrounding clause structure and the lexical semantics of the noun and verb involved.
