---
id: relative-clause-formation
title: Relative Clause Formation (Mechanisms and Strategies)
domain: language-and-communication
course: linguistics
prerequisites:
- id: relative-clauses
  type: hard
- id: syntactic-structure
  type: hard
- id: wh-movement-operator-quantification
  type: hard
builds-toward:
- long-distance-extraction
tags:
- syntax
- clauses
- typology
- relative-clauses
stage: advanced
status: draft
---

# Relative Clause Formation (Mechanisms and Strategies)

## Core Idea
Relative clause formation encompasses diverse grammatical strategies: wh-movement and relative pronouns, resumptive pronouns, headless/free relatives, and correlative constructions. The choice of strategy interacts with the Accessibility Hierarchy, island constraints, and language-specific morphosyntax.

## Questions

```yaml
- question: "A linguist studies a language that can relativize subjects, direct objects, and indirect objects, but not obliques (e.g., 'the man that I gave the book to' is ungrammatical). Based on the Accessibility Hierarchy, which positions should also be ungrammatical in this language?"
  type: multiple-choice
  options:
    - "Direct objects only, since indirect objects are already at the limit"
    - "Subjects, since they are the most basic position to relativize"
    - "Genitives and objects of comparison, since they are lower on the hierarchy than obliques"
    - "Indirect objects, since the language cannot handle obliques"
  answer: 2
  explanation: "The Accessibility Hierarchy is an implicational universal: if a language can relativize a position, it can also relativize every higher position, but not necessarily lower ones. Since obliques rank below indirect objects, and the language can't relativize obliques, it also cannot relativize genitives or objects of comparison (which are below obliques). Subjects, direct objects, and indirect objects — all above obliques — remain grammatical. The hierarchy makes precise, cross-linguistically testable predictions in exactly this form."

- question: "In Hebrew, the construction 'the man that I saw him' (with an overt pronoun 'him' in the object position) represents:"
  type: multiple-choice
  options:
    - "A grammatical error in which the speaker forgot to delete the pronoun"
    - "An ungrammatical structure that native speakers would correct to 'the man that I saw'"
    - "A resumptive pronoun strategy — the grammatically regular way to form relative clauses in Hebrew"
    - "A disfluency that arises when speakers are uncertain how to construct relative clauses"
  answer: 2
  explanation: "Resumptive pronouns are not errors — in Hebrew, Arabic, and many West African and Bantu languages, they are the grammatically regular strategy for relative clause formation. Rather than leaving a silent gap where the head noun's role is interpreted, the language uses an overt coreferential pronoun. English speakers learning about resumptives often assume they are repairs or mistakes, because English suppresses them under normal conditions — but they are fully grammatical strategies in the languages that use them systematically."

- question: "In languages that use resumptive pronouns to form relative clauses, the resumptive fills the same grammatical function as the silent gap in English-style gap relatives."
  type: true-false
  answer: true
  explanation: "Both the gap strategy (English) and the resumptive strategy (Hebrew, Arabic, many others) solve the same semantic problem: how to indicate the grammatical role that the head noun plays inside the relative clause. In English, 'the man [who I saw _]' uses a silent gap to mark the object position. In Hebrew, 'the man [that I saw him]' uses an overt coreferential pronoun in the same position. The semantic function is identical; only the phonological strategy (silence vs. overt pronoun) differs."

- question: "According to the Accessibility Hierarchy, if a language can relativize obliques, it must also be able to relativize subjects."
  type: true-false
  answer: true
  explanation: "The Accessibility Hierarchy is a strict implicational universal: ability to relativize a lower-ranked position implies ability to relativize all higher-ranked ones. Since subjects are at the top of the hierarchy (subject > direct object > indirect object > oblique > genitive > object of comparison), any language that can relativize obliques must be able to relativize subjects, direct objects, and indirect objects as well. A language cannot skip levels — this is what makes the hierarchy predictive rather than merely descriptive."

- question: "Why do resumptive pronouns appear in relative clauses in English in some contexts, even though English normally uses the gap strategy?"
  type: short-answer
  answer: "Resumptives surface in English in long-distance extraction contexts where gap-formation is blocked or extremely demanding — when the gap would be deeply embedded or would violate extraction constraints. This suggests that resumptive pronouns are a universal grammatical option available across languages, and English merely suppresses them under ordinary conditions in favor of gaps. When gap-formation becomes too difficult (due to island constraints or processing load), the universal resumptive option surfaces even in English, indicating that the choice between strategies reflects gradient grammatical pressures, not a categorical either/or."
  explanation: "This finding — that English allows resumptives in sufficiently complex structures — supports the view that the gap/resumptive distinction is not a binary typological parameter but a spectrum of preferences modulated by syntactic and processing constraints. Languages differ in where they set the threshold at which resumptives become the preferred or required strategy."
```

## Explainer

You have studied relative clauses as a grammatical category — structures that modify nouns by embedding a dependent clause — and you've worked with the syntactic machinery of wh-movement. Now the question shifts from *what* relative clauses are to *how* different languages build them, and what that variation reveals about the underlying grammar. Languages do not all use the same strategy to form relative clauses, and understanding the range of strategies illuminates both typological universals and language-specific constraints.

The strategy you know best is **wh-movement**: a relative pronoun (who, which, that) moves from its underlying position in the embedded clause to the front of the relative clause, leaving a **gap** — an empty position where the head noun's role is interpreted. "The student [who_i I recommended t_i]" — the relative pronoun *who* has moved from the object position (the gap *t_i*) to the clause-initial position. English and most European languages use this gap strategy. The key property is that the extraction site is phonologically silent; the moved element encodes the grammatical relation. Island constraints, which you've seen in the context of wh-movement generally, restrict which positions can be relativized this way — you cannot extract out of a subject island or a complex noun phrase island without producing ungrammaticality.

When wh-movement is blocked or disallowed, some languages use a **resumptive pronoun** strategy instead: rather than leaving a silent gap, the extraction site contains an overt pronoun that is coreferential with the head noun. Hebrew, Arabic, and many West African and Bantu languages employ resumptives systematically. "The man [that I saw *him*]" — the pronoun *him* is the resumptive, filling the position where a gap would appear in English. Resumptives are not errors or awkward repairs; they are the grammatically regular strategy in these languages. Interestingly, even in English, resumptive pronouns appear in long-distance contexts where speakers feel gap-formation is too demanding — suggesting that resumptives may be a universal option that is simply suppressed in English under normal conditions.

The **Accessibility Hierarchy** (Keenan & Comrie, 1977) is the key typological universal in this domain. It ranks grammatical positions by how easily they can be relativized: subject > direct object > indirect object > oblique > genitive > object of comparison. The universal is that if a language can relativize a lower position on the hierarchy, it can also relativize every higher position — but not vice versa. Some languages relativize only subjects; some add direct objects; English and many others go all the way down. This hierarchy makes precise, cross-linguistically testable predictions. **Correlative relative clauses** — found in Sanskrit, Hindi, and Turkish — represent yet another strategy: rather than embedding the clause inside the noun phrase, the relative clause appears as a separate left-peripheral clause and is linked to the main clause through a correlative pronoun. These are not subordinate in the traditional sense but are biclausal structures where a demonstrative in the main clause picks up the reference established in the correlative. Together, these strategies show that the semantic function of relativization is universal, but the syntactic machinery for achieving it varies along principled, constrained dimensions.

