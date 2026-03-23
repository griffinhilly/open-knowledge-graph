---
id: faithfulness-constraints-phonology
title: Faithfulness Constraints in Optimality Theory
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: optimality-theory-introduction
  type: hard
- id: phonological-features
  type: hard
builds-toward:
- constraint-ranking-optimality-theory
tags:
- faithfulness
- optimality-theory
- phonology
stage: expert
status: draft
---

# Faithfulness Constraints in Optimality Theory

## Core Idea
Faithfulness constraints in Optimality Theory require that underlying representations be preserved in surface forms: DEP prohibits epenthesis, MAX prohibits deletion, IDENT prohibits feature changes. The ranking of faithfulness constraints relative to markedness constraints determines which phonological processes occur. High-ranked faithfulness constraints block alterations; low-ranked constraints allow them when required by markedness.

## How It's Best Learned
Build constraint tableaux comparing candidates with different degrees of deviation from underlying form (insertions, deletions, substitutions). Observe how constraint ranking predicts which processes are active or inactive in a language.

## Common Misconceptions
- Faithfulness constraints do not mean phonological processes never occur; they define when processes are blocked or permitted.
- FAITHFULNESS is not monolithic; distinct constraints govern different phonological dimensions (features, segments, prosody).

## Questions

```yaml
- question: "German surfaces /hʊnd/ (Hund, 'dog') as [hʊnt] with a voiceless final consonant. In OT terms, which ranking produces this outcome?"
  type: multiple-choice
  options:
    - "IDENT[voice] >> *VOICED-CODA — faithfulness dominates markedness, so voicing is preserved"
    - "*VOICED-CODA >> IDENT[voice] — markedness dominates faithfulness, so voicing is neutralized"
    - "MAX >> *VOICED-CODA — the segment is preserved but its features are changed"
    - "DEP >> IDENT[voice] — epenthesis is blocked, forcing a feature change instead"
  answer: 1
  explanation: "Coda devoicing (underlying /d/ → surface [t]) means the markedness constraint *VOICED-CODA (no voiced obstruents in coda position) wins against the faithfulness constraint IDENT[voice] (preserve voicing). When markedness dominates faithfulness, phonological processes occur. English lacks coda devoicing because IDENT[voice] outranks *VOICED-CODA in English — the same constraints, different ranking, different output. Options C and D misapply MAX (which governs deletion) and DEP (which governs epenthesis) — neither is violated here."

- question: "A language freely deletes vowels in unstressed syllables but never inserts vowels to break up consonant clusters. Which constraint ranking is consistent with this pattern?"
  type: multiple-choice
  options:
    - "DEP >> MAX — epenthesis is blocked by high DEP, while MAX (preventing deletion) is lower-ranked"
    - "MAX >> DEP — deletion is blocked by high MAX, while epenthesis is freely permitted"
    - "IDENT >> MAX >> DEP — feature changes are blocked but both deletion and insertion occur"
    - "MAX >> IDENT >> DEP — deletion and feature change are blocked, only epenthesis occurs"
  answer: 0
  explanation: "The pattern — deletion occurs, epenthesis doesn't — means MAX (which prohibits deletion) is ranked below whatever markedness constraints drive deletion, while DEP (which prohibits epenthesis) is ranked above the markedness constraints that would trigger insertion. High DEP blocks all vowel insertion; low MAX allows deletion when markedness demands it. This illustrates a core OT principle: each faithfulness constraint has an independent ranking, and each governs a different type of input-output correspondence."

- question: "In Optimality Theory, a language with high-ranked faithfulness constraints will never exhibit any phonological processes."
  type: true-false
  answer: false
  explanation: "Faithfulness constraints are ranked relative to markedness constraints — there is no such thing as globally 'high-ranked' faithfulness. A language can have IDENT[voice] ranked very high (blocking voicing alternations) while MAX is ranked lower (allowing deletions). Only the specific faithfulness constraints that outrank the competing markedness constraints block those specific processes. A language can simultaneously have many active phonological processes in dimensions where faithfulness loses and blocked processes in dimensions where faithfulness wins."

- question: "The constraints MAX, DEP, and IDENT each penalize the same kind of input-output discrepancy — any deviation from the underlying form."
  type: true-false
  answer: false
  explanation: "MAX, DEP, and IDENT penalize three distinct types of deviation. MAX penalizes deletion: an input segment has no correspondent in the output. DEP penalizes epenthesis: an output segment has no correspondent in the input. IDENT penalizes featural change: corresponding segments differ in some feature value (e.g., voiced in input, voiceless in output). This decomposition matters because each constraint can be ranked independently — a language can allow deletion (low MAX) while blocking epenthesis (high DEP) and allowing feature changes (low IDENT)."

- question: "Explain why the same two competing constraints — say, *VOICED-CODA and IDENT[voice] — can produce different phonological patterns in different languages, according to Optimality Theory."
  type: short-answer
  answer: "OT proposes that all constraints are universal and present in every grammar, but languages differ in how they rank those constraints. When *VOICED-CODA outranks IDENT[voice], coda devoicing occurs (German, Russian). When IDENT[voice] outranks *VOICED-CODA, voicing is preserved in coda position (English). The input-output mapping selected as optimal is always the one that best satisfies the constraints in their language-specific ranking order. Languages share constraints but differ in rankings, and ranking differences generate different surface patterns."
  explanation: "This is the core claim of OT: phonological typology — the space of possible patterns across languages — is generated by permuting constraint rankings, not by listing language-specific rules. The insight is that cross-linguistic variation is not arbitrary but constrained by the set of universal constraints and the mathematics of ranking. The same two constraints, ranked in opposite orders, produce mirror-image grammars."
```

## Explainer

In Optimality Theory, as you know from your introduction to the framework, phonological outputs are selected by ranking competing universal constraints against each other. Markedness constraints define what surface forms are structurally preferred — no complex onsets, no nasalized vowels, no final obstruents, and so on. But if markedness constraints alone determined outputs, every language would converge on the same highly unmarked forms, which is obviously wrong. **Faithfulness constraints** are the counterweight: they require that outputs preserve the properties of underlying inputs. The tension between markedness and faithfulness is where phonological variation lives.

The three core families of faithfulness constraints map onto the three ways an output can differ from an input. **MAX** requires that every element in the input has a correspondent in the output — it is violated by deletion (a segment in the input has no correspondent in the output). **DEP** requires that every element in the output has a correspondent in the input — it is violated by epenthesis (a segment in the output appears from nowhere, with no input correspondent). **IDENT** requires that corresponding elements share feature values — it is violated by any featural change between input and output, such as a [+voice] segment surfacing as [-voice]. A useful mnemonic: MAX prevents *loss* (max out what you have), DEP prevents *gain* (be dependent on the input), and IDENT prevents *change* (stay identical).

The power of the faithfulness framework lies in how constraint ranking generates typological predictions. Consider **coda obstruent devoicing** — the process in German and Russian where /d/ becomes [t] at the end of a syllable. In OT terms, this means the markedness constraint *VOICED-CODA (no voiced obstruents in coda position)* outranks IDENT[voice]. German speakers produce [hʊnt] for underlying /hʊnd/ (Hund, "dog") because the markedness constraint dominates. English speakers preserve the voicing — /hʌnd/ surfaces as [hʌnd] — because IDENT[voice] outranks *VOICED-CODA. The same constraints, different rankings, different outputs. This is the standard OT analysis of phonological typology: languages share constraints but differ in how they rank them.

Because faithfulness is not monolithic, different phonological dimensions are governed by distinct constraints that can be ranked independently. IDENT[voice] can be dominated by a markedness constraint while IDENT[nasal] is undominated, producing a language that freely alternates voicing but never changes nasality. The specific phonological features you studied — place, manner, voicing, nasality, and so on — each have their own IDENT constraint, which means the grammar can be fine-grained in exactly the way languages actually are. This decomposition also handles classic cases like vowel harmony and consonant assimilation, where features spread from one segment to adjacent ones: the spreading segment has a correspondent, but its IDENT constraint on the affected feature is dominated by a constraint demanding agreement within a domain. Faithfulness constraints, in short, set the limits of how much phonology can reshape underlying forms — and by varying those limits, OT generates the space of possible human phonologies.
