---
id: phonological-rules-derivation
title: Phonological Rules and Derivation
domain: language-and-communication
course: linguistics
prerequisites:
- id: phoneme-inventory-analysis
  type: hard
- id: phonological-features
  type: hard
builds-toward:
- stress-assignment-rules
- morphology-phonology-interface
tags:
- phonology
- rules
- derivation
- underlying-representation
stage: formal-systems
status: validated
---

# Phonological Rules and Derivation

## Core Idea
Phonological rules systematically derive surface pronunciations from underlying representations. A rule specifies the conditions under which a sound changes—for example, nasals assimilate to the point of articulation of an adjacent consonant. Rules are ordered and apply cyclically to produce final outputs that speakers pronounce.

## How It's Best Learned
Write rules using formal notation (SPE conventions), apply them step-by-step to derive outputs from inputs, then compare predicted outputs to actual pronunciation in natural speech.

## Common Misconceptions
- Assuming rules are unidirectional; a rule A→B does not mean B→A also applies. - Confusing the order of rules; rule order matters and produces different results. - Thinking rules are universal; rules are language-specific.

## Questions

```yaml
- question: "English speakers say 'impossible,' 'incomplete,' and 'inhuman' rather than 'inpossible,' 'incomplete,' and 'inhuman' (with the same nasal). What does this pattern demonstrate about phonological rules?"
  type: multiple-choice
  options:
    - "English stores three separate underlying prefix morphemes that are selected based on the following consonant"
    - "A single underlying representation /in-/ surfaces differently through a nasal assimilation rule that changes the nasal to match the place of articulation of the following consonant"
    - "Phonological rules only apply to vowels; the variation in nasals is learned separately as vocabulary"
    - "Rules are universal, so this same pattern should apply identically in all languages"
  answer: 1
  explanation: "The prefix has one underlying representation /in-/. A nasal assimilation rule changes it: before bilabial /p/, the alveolar /n/ becomes bilabial [m] ('impossible'); before velar /k/, it becomes velar [ŋ] ('incomplete' → [ɪŋkəmpliːt]); before vowels and alveolars the underlying /n/ surfaces unchanged. The variation is not memorized entry by entry — it is derived from a single UR by a productive rule. Rules are language-specific, not universal."

- question: "Two phonological rules could apply to the same form. Rule A creates the phonological environment that Rule B needs in order to apply. What is this relationship called, and why does rule ordering matter?"
  type: multiple-choice
  options:
    - "Bleeding order — Rule A destroys the environment Rule B would have applied to, preventing B from applying"
    - "Feeding order — Rule A creates an environment for Rule B, so applying A before B produces a different (and often more accurate) output than B before A"
    - "Cyclic order — both rules apply simultaneously in a single pass"
    - "Free variation — when two rules could both apply, either ordering produces the same surface form"
  answer: 1
  explanation: "In feeding order, Rule A 'feeds' Rule B by creating the environment Rule B needs. If you apply B before A, B has no environment to apply to and produces the wrong output. This shows why rule ordering is not arbitrary: the derivation is a sequence, and the order determines what output is predicted. Bleeding order is the opposite — Rule A removes the environment Rule B would have used, so applying A first prevents B from applying."

- question: "The same morpheme can have multiple surface pronunciations, all derived from a single underlying representation through the application of phonological rules."
  type: true-false
  answer: true
  explanation: "This is the central insight of derivational phonology. The English plural morpheme has one underlying representation /z/, which surfaces as [s] after voiceless consonants ('cats'), [z] after voiced consonants and vowels ('dogs'), and [ɪz] after sibilants ('buses'). The three pronunciations are not stored separately — they are predicted by rules. The UR/SR distinction explains why apparent pronunciation irregularity is actually systematic."

- question: "Because a phonological rule specifies that sound A changes to B in a given context, the reverse rule (B → A in the same context) is also valid in that language."
  type: true-false
  answer: false
  explanation: "Phonological rules are directional — A→B does not imply B→A. Rules specify one-way changes in defined contexts; the reverse rule would be a separate, independent rule that may or may not exist in the language. This is one of the most common misconceptions in phonology: confusing the asymmetry of rules with symmetry. Rule direction reflects specific articulatory or historical processes, not bidirectional relationships."

- question: "What is the difference between an underlying representation (UR) and a surface representation (SR), and why does this distinction matter for understanding phonological variation in natural languages?"
  type: short-answer
  answer: "The UR is the abstract stored form of a morpheme as it exists in the mental lexicon — what the morpheme looks like before any rules apply. The SR is what speakers actually pronounce in a specific phonological context, after all applicable rules have applied in order. The distinction matters because it explains why the same morpheme surfaces differently in different environments without requiring speakers to memorize every variant separately. Rules apply to the UR to derive the SR, and apparent pronunciation irregularity turns out to be predictable once you know the rules."
  explanation: "Without the UR/SR distinction, you would need to treat 'cats,' 'dogs,' and 'buses' as having three different plural morphemes — losing the insight that they are the same underlying morpheme in different environments. The framework reveals systematicity behind apparent variation, which is what makes it linguistically powerful. It also enables the formal testing of whether a proposed rule system correctly predicts the pronunciations speakers actually produce."
```

## Explainer

You've already mapped a language's phoneme inventory — the set of contrastive sound categories — and analyzed the phonological features that define them (voicing, place of articulation, manner, nasality, etc.). Phonological rules and derivation build directly on that foundation: they explain why the phonemes you identified in underlying forms don't always surface as you'd expect in actual pronunciations. The gap between what a morpheme "looks like" in storage and what speakers actually pronounce is systematic, and rules are the mechanism that bridges the two.

The central distinction is between **underlying representation (UR)** and **surface representation (SR)**. The UR is the abstract, stored form of a morpheme — what it looks like when you pull it from the mental lexicon in isolation. The SR is what speakers actually pronounce in a given phonological context. In English, the plural morpheme has a single UR: something like /z/. But it surfaces as [s] after voiceless consonants ("cats"), [z] after voiced consonants and vowels ("dogs," "bees"), and [ɪz] after sibilants ("buses," "matches"). These three surface forms are not stored separately — they are derived from the single underlying /z/ by phonological rules.

A **phonological rule** specifies a change in the form A → B / X __ Y, which reads: "A becomes B when it appears in the context X before Y." Rules can change a feature (voicing), add a segment (epenthesis), delete a segment (syncope), or move a segment (metathesis). The English plural rule is a **voicing assimilation rule**: /z/ becomes [s] when it follows a voiceless segment. The operation is local and feature-based — the output shares the voicing value of the adjacent consonant. This is not a quirk of English; assimilation rules (where a sound takes on a feature from its neighbor) are among the most common phonological rules cross-linguistically, because they reduce the articulatory effort required to transition between adjacent sounds.

**Rule ordering** is where derivation gets genuinely complex. When multiple rules apply to the same form, the order in which they apply can produce different outputs. Classic examples from Turkish or Slavic languages show **feeding order** (where rule A creates an environment that rule B can then apply to) and **bleeding order** (where rule A eliminates an environment that rule B would have applied to). Getting the order wrong produces a derivation that predicts the wrong surface form. Step-by-step derivation — starting with the UR, applying rules in sequence, and arriving at the SR — is not just a classroom exercise; it is how linguists test whether their rule system correctly predicts the pronunciations speakers actually produce.

The payoff of this framework is that it reveals the underlying systematicity behind what sounds like arbitrary pronunciation variation. When English speakers say "impossible" rather than "inpossible," that is not random; it is the nasal assimilation rule changing /n/ to [m] before a bilabial /p/. When they say "sandwich" as "samwich," that is the same class of rule operating in casual speech. Phonological rules are the grammar's instructions for converting stored morphemes into the smooth, articulatorily efficient sound sequences that speakers actually produce — and once you can write and apply them formally, apparent irregularities become predictable patterns.
