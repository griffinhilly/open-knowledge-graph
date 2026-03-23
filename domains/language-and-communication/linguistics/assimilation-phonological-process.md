---
id: assimilation-phonological-process
title: Assimilation (Phonological Process)
domain: language-and-communication
course: linguistics
prerequisites:
- id: phonological-rules-derivation
  type: hard
- id: phonological-features
  type: hard
tags:
- phonology
- sound-change
- phonological-processes
stage: formal-systems
status: validated
---

# Assimilation (Phonological Process)

## Core Idea
Assimilation is a phonological process in which a sound becomes more similar to a neighboring sound, copying features of place, manner, or voicing. Examples include nasal assimilation (input /n/ becomes [m] before /p/) and voicing assimilation. Assimilation may be progressive, regressive, or mutual, and can be context-restricted.

## Questions

```yaml
- question: "The English prefix 'in-' (meaning 'not') surfaces as 'im-' in 'impossible' and 'il-' in 'illegal,' but remains 'in-' in 'indirect.' What type of assimilation is operating, and in which direction?"
  type: multiple-choice
  options:
    - "Progressive assimilation — the nasal copies features from the preceding vowel /ɪ/"
    - "Regressive assimilation — the nasal copies the place of articulation of the following consonant"
    - "Total assimilation — the nasal becomes completely identical to the following consonant in all features"
    - "Progressive assimilation — the following consonant copies the nasality feature from the prefix nasal"
  answer: 1
  explanation: "This is regressive (anticipatory) assimilation: the *following* sound influences the *preceding* sound. The underlying nasal /n/ is coronal (alveolar), but before the bilabial /p/ in 'impossible,' it assimilates to labial place, becoming [m]. Before the lateral /l/ in 'illegal,' it assimilates fully to lateral. The nasal 'looks ahead' at the upcoming consonant and borrows its place feature — regressive because the influence flows backward (right to left). Before /d/ in 'indirect,' /d/ is also coronal, so /n/ stays [n] — no change is needed. Option C (total assimilation) would require the nasal to become identical in *all* features, not just place."

- question: "In English, the plural suffix has an underlying form /z/, but surfaces as [s] in 'cats' and [z] in 'dogs.' What phonological process is operating?"
  type: multiple-choice
  options:
    - "Regressive place assimilation — the suffix borrows the place of articulation of the final root consonant"
    - "Progressive voicing assimilation — the suffix adopts the voicing specification of the final consonant of the root"
    - "Total assimilation — the suffix becomes fully identical to the final consonant of the root in all features"
    - "Dissimilation — the suffix contrasts with the voicing of the root's final consonant to avoid repetition"
  answer: 1
  explanation: "This is progressive voicing assimilation: the *preceding* sound influences the *following* one. The root-final consonant /t/ in 'cat' is [-voice], and this voicing value spreads forward onto the suffix, making /z/ surface as [s]. The root-final /g/ in 'dog' is [+voice], so the suffix remains [z]. The direction is progressive (left to right): the preceding segment's feature propagates onto the following one. Note this is specifically voicing (not place), so option A is wrong — the place of /t/ is not copied. Option C (total assimilation) would require the suffix to become identical to /t/ in every feature, producing /tts/, which doesn't happen."

- question: "In regressive assimilation, the preceding (earlier) sound influences the following (later) sound."
  type: true-false
  answer: false
  explanation: "This is the most common direction-of-assimilation confusion. Regressive assimilation means the *following* sound influences the *preceding* one — the influence flows backward (right to left). The term 'regressive' refers to the direction of influence: the cause is downstream and the effect is upstream. This is also called *anticipatory* assimilation — the preceding sound anticipates features of the upcoming sound. Progressive assimilation is the reverse: the preceding sound influences the following one, with influence flowing forward (left to right). The English plural example ([kæts] vs [dɒgz]) is progressive; the 'in-/im-/il-' example is regressive."

- question: "Assimilation is a regular, rule-governed phonological process that applies predictably based on the phonological context of neighboring sounds."
  type: true-false
  answer: true
  explanation: "Assimilation is systematic, not random. The 'in-' prefix always surfaces as [m] before bilabials and always as [n] before coronals — with no exceptions in native English vocabulary. The English plural suffix always devoices after voiceless consonants and remains voiced after voiced ones. These patterns can be stated as formal phonological rules of the form A → B / C __ D ('sound A becomes B when preceded by C and followed by D'). The fact that assimilation is regular is what allows it to extend automatically to new words — a nonce word ending in /p/ will automatically take the plural [s], not [z], because the rule applies productively."

- question: "What articulatory motivation underlies assimilation, and how does this motivation help explain why regressive (anticipatory) assimilation tends to be more common across the world's languages than progressive assimilation?"
  type: short-answer
  answer: "Assimilation is motivated by articulatory efficiency: producing two adjacent sounds requires transitioning between different articulatory configurations, and that transition costs muscular effort. If neighboring sounds share features (e.g., both bilabial, or both voiced), the tongue and lips do not need to change position between them, reducing the physical cost of articulation. Regressive assimilation tends to be more common because speakers plan upcoming sounds in advance — the articulatory system begins preparing for the next sound before the current one is finished. This anticipatory co-articulation means the features of the upcoming sound 'bleed back' into the current sound during its production. Progressive assimilation does occur (as in the English plural), but the forward-planning nature of speech production makes anticipation of future sounds the more natural direction."
  explanation: "This articulatory efficiency account explains not just assimilation but many other phonological processes: deletion of difficult consonant clusters, vowel harmony in Turkish and Finnish (vowels throughout a word share front/back features), and nasal spread in some languages. The common thread is reduction of articulatory cost. Understanding the phonetic motivation helps you predict which features are most likely to assimilate (place and voicing are common; manner features less so) and in which contexts."
```

## Explainer

From your study of phonological features and phonological rules, you know that sounds are not atoms — they are bundles of articulatory features like [+voiced], [+nasal], [labial], and [coronal]. You also know that phonological rules operate on these features, changing sounds in systematic, context-sensitive ways. **Assimilation** is the most pervasive class of such rules: a sound becomes more similar to a neighboring sound by copying one or more of its features. The motivation is articulatory efficiency — transitioning between two adjacent sounds is easier when they share properties, reducing the muscular adjustment required at the boundary.

The clearest examples involve **place of articulation**. English has a prefix *in-* meaning "not" (as in *indirect*, *impossible*, *illegal*). Notice what happens: before /d/ we get *in-* (coronal nasal), before /p/ we get *im-* (labial nasal), and before /l/ we get *il-* (lateral). The underlying form is /ɪn/, but the nasal assimilates to the place of articulation of the following consonant. Before /p/ (a bilabial stop), the nasal becomes [m] (also bilabial). Before /l/ (lateral-alveolar), the nasal fully assimilates. The nasal "borrows" the [labial] or [coronal] feature of the upcoming sound. This is **regressive assimilation** (also called anticipatory): the following segment influences the preceding one.

**Progressive assimilation** works in the opposite direction: the preceding sound influences the following one. The English plural suffix provides a classic example. The underlying form is /z/, but after voiceless consonants it surfaces as [s]: *cat-s* [kæts], *dog-z* [dɒgz]. The voicing value of the final consonant in the root propagates forward onto the suffix. You can describe this with a phonological rule you already know how to write: /z/ → [s] / [−voice] ___ (the suffix becomes voiceless when it follows a voiceless segment). This is assimilation of the **voicing** feature.

**Total assimilation** — where a sound becomes completely identical to its neighbor — appears in phrases across many languages and in fast, casual speech. In Latin, *ad-* (toward) became *ac-* before /c/ (*accede*), *ap-* before /p/ (*append*), *af-* before /f/ (*affirm*). The prefix consonant fully copied every feature of the following consonant. You can see the same process in English loanwords and even in rapid speech: "in case" → [ɪŋkeɪs], where the coronal nasal assimilates fully to the velar place of the /k/. Assimilation is not a corruption or irregularity — it is a regular, rule-governed process that operates predictably across contexts, and your ability to write formal phonological rules from the previous topic is exactly the framework needed to describe and predict where it applies.

