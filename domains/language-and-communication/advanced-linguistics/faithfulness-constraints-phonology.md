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
stage: advanced
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

## Explainer

In Optimality Theory, as you know from your introduction to the framework, phonological outputs are selected by ranking competing universal constraints against each other. Markedness constraints define what surface forms are structurally preferred — no complex onsets, no nasalized vowels, no final obstruents, and so on. But if markedness constraints alone determined outputs, every language would converge on the same highly unmarked forms, which is obviously wrong. **Faithfulness constraints** are the counterweight: they require that outputs preserve the properties of underlying inputs. The tension between markedness and faithfulness is where phonological variation lives.

The three core families of faithfulness constraints map onto the three ways an output can differ from an input. **MAX** requires that every element in the input has a correspondent in the output — it is violated by deletion (a segment in the input has no correspondent in the output). **DEP** requires that every element in the output has a correspondent in the input — it is violated by epenthesis (a segment in the output appears from nowhere, with no input correspondent). **IDENT** requires that corresponding elements share feature values — it is violated by any featural change between input and output, such as a [+voice] segment surfacing as [-voice]. A useful mnemonic: MAX prevents *loss* (max out what you have), DEP prevents *gain* (be dependent on the input), and IDENT prevents *change* (stay identical).

The power of the faithfulness framework lies in how constraint ranking generates typological predictions. Consider **coda obstruent devoicing** — the process in German and Russian where /d/ becomes [t] at the end of a syllable. In OT terms, this means the markedness constraint *VOICED-CODA (no voiced obstruents in coda position)* outranks IDENT[voice]. German speakers produce [hʊnt] for underlying /hʊnd/ (Hund, "dog") because the markedness constraint dominates. English speakers preserve the voicing — /hʌnd/ surfaces as [hʌnd] — because IDENT[voice] outranks *VOICED-CODA. The same constraints, different rankings, different outputs. This is the standard OT analysis of phonological typology: languages share constraints but differ in how they rank them.

Because faithfulness is not monolithic, different phonological dimensions are governed by distinct constraints that can be ranked independently. IDENT[voice] can be dominated by a markedness constraint while IDENT[nasal] is undominated, producing a language that freely alternates voicing but never changes nasality. The specific phonological features you studied — place, manner, voicing, nasality, and so on — each have their own IDENT constraint, which means the grammar can be fine-grained in exactly the way languages actually are. This decomposition also handles classic cases like vowel harmony and consonant assimilation, where features spread from one segment to adjacent ones: the spreading segment has a correspondent, but its IDENT constraint on the affected feature is dominated by a constraint demanding agreement within a domain. Faithfulness constraints, in short, set the limits of how much phonology can reshape underlying forms — and by varying those limits, OT generates the space of possible human phonologies.
