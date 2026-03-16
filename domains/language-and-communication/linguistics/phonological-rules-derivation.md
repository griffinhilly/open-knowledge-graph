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
status: draft
---

# Phonological Rules and Derivation

## Core Idea
Phonological rules systematically derive surface pronunciations from underlying representations. A rule specifies the conditions under which a sound changes—for example, nasals assimilate to the point of articulation of an adjacent consonant. Rules are ordered and apply cyclically to produce final outputs that speakers pronounce.

## How It's Best Learned
Write rules using formal notation (SPE conventions), apply them step-by-step to derive outputs from inputs, then compare predicted outputs to actual pronunciation in natural speech.

## Common Misconceptions
- Assuming rules are unidirectional; a rule A→B does not mean B→A also applies. - Confusing the order of rules; rule order matters and produces different results. - Thinking rules are universal; rules are language-specific.

## Explainer

You've already mapped a language's phoneme inventory — the set of contrastive sound categories — and analyzed the phonological features that define them (voicing, place of articulation, manner, nasality, etc.). Phonological rules and derivation build directly on that foundation: they explain why the phonemes you identified in underlying forms don't always surface as you'd expect in actual pronunciations. The gap between what a morpheme "looks like" in storage and what speakers actually pronounce is systematic, and rules are the mechanism that bridges the two.

The central distinction is between **underlying representation (UR)** and **surface representation (SR)**. The UR is the abstract, stored form of a morpheme — what it looks like when you pull it from the mental lexicon in isolation. The SR is what speakers actually pronounce in a given phonological context. In English, the plural morpheme has a single UR: something like /z/. But it surfaces as [s] after voiceless consonants ("cats"), [z] after voiced consonants and vowels ("dogs," "bees"), and [ɪz] after sibilants ("buses," "matches"). These three surface forms are not stored separately — they are derived from the single underlying /z/ by phonological rules.

A **phonological rule** specifies a change in the form A → B / X __ Y, which reads: "A becomes B when it appears in the context X before Y." Rules can change a feature (voicing), add a segment (epenthesis), delete a segment (syncope), or move a segment (metathesis). The English plural rule is a **voicing assimilation rule**: /z/ becomes [s] when it follows a voiceless segment. The operation is local and feature-based — the output shares the voicing value of the adjacent consonant. This is not a quirk of English; assimilation rules (where a sound takes on a feature from its neighbor) are among the most common phonological rules cross-linguistically, because they reduce the articulatory effort required to transition between adjacent sounds.

**Rule ordering** is where derivation gets genuinely complex. When multiple rules apply to the same form, the order in which they apply can produce different outputs. Classic examples from Turkish or Slavic languages show **feeding order** (where rule A creates an environment that rule B can then apply to) and **bleeding order** (where rule A eliminates an environment that rule B would have applied to). Getting the order wrong produces a derivation that predicts the wrong surface form. Step-by-step derivation — starting with the UR, applying rules in sequence, and arriving at the SR — is not just a classroom exercise; it is how linguists test whether their rule system correctly predicts the pronunciations speakers actually produce.

The payoff of this framework is that it reveals the underlying systematicity behind what sounds like arbitrary pronunciation variation. When English speakers say "impossible" rather than "inpossible," that is not random; it is the nasal assimilation rule changing /n/ to [m] before a bilabial /p/. When they say "sandwich" as "samwich," that is the same class of rule operating in casual speech. Phonological rules are the grammar's instructions for converting stored morphemes into the smooth, articulatorily efficient sound sequences that speakers actually produce — and once you can write and apply them formally, apparent irregularities become predictable patterns.
