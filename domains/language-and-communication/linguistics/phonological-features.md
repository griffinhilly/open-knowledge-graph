---
id: phonological-features
title: Phonological Features
domain: language-and-communication
course: linguistics
prerequisites:
- id: phonological-systems
  type: hard
- id: articulatory-phonetics
  type: hard
tags:
- distinctive features
- natural classes
- feature geometry
- voicing
- place
- manner
stage: formal-systems
status: draft
---

# Phonological Features

## Core Idea
Phonological features are the sub-segmental properties (such as [+voice], [+nasal], [+continuant]) that decompose speech sounds into their component articulatory and acoustic dimensions. Rather than treating phonemes as unanalyzable atoms, feature theory reveals that sounds sharing features form natural classes — groups that behave uniformly in phonological rules. For example, all nasals ([+nasal]: /m, n, ng/) pattern together in assimilation processes across unrelated languages because they share a feature specification. Feature geometry extends this by organizing features into a hierarchical tree structure, where nodes represent articulatory regions (laryngeal, place, manner), predicting which features can spread, delink, or assimilate independently and which must move as a unit.

## How It's Best Learned
Classify all English consonants by their feature specifications and then identify which natural classes are needed to state common phonological rules (e.g., aspiration of voiceless stops, nasalization of vowels before nasals). Work through assimilation processes in a language like Turkish or Sanskrit to see how feature spreading operates over natural classes. Draw feature geometry trees for a set of segments and practice delinking and spreading nodes to model observed alternations.

## Common Misconceptions
- Features are not just labels for convenience — they are theoretical primitives that make empirical predictions about which sounds should pattern together and which rules are possible in human languages.
- Not every phonetic property is a distinctive feature; only those properties that create meaning-distinguishing contrasts in at least some languages qualify.
- Binary features ([+/-voice]) do not mean sounds are either fully voiced or fully voiceless — they capture phonological contrasts that may be realized as a gradient continuum in phonetics.

## Questions

```yaml
- question: "A phonologist wants to write a single rule that applies to all nasal consonants (/m/, /n/, /ŋ/) but no other sounds. What property of feature theory makes this possible?"
  type: multiple-choice
  options:
    - "Each phoneme is treated as an unanalyzable atom, so the rule can simply list the three phonemes"
    - "The sounds /m/, /n/, /ŋ/ form a natural class defined by sharing the feature [+nasal], allowing one rule to reference the whole group"
    - "Phonological rules always apply to exactly three sounds at a time"
    - "Feature geometry predicts that only three nasals can exist in any language"
  answer: 1
  explanation: "Natural classes are the key motivation for feature theory. Instead of listing /m/, /n/, /ŋ/ individually (which would be stipulative and miss the generalization), the feature [+nasal] picks out exactly these sounds as a class. A single rule referencing [+nasal] then applies to all of them — and will automatically extend to any additional nasal phonemes a language might have. This is a genuine empirical prediction, not just shorthand."

- question: "A binary feature like [+voice] means that sounds are either completely voiced or completely voiceless, with no gradient realization possible."
  type: true-false
  answer: false
  explanation: "This confuses the phonological level with the phonetic level. At the phonological level, [+/-voice] is a categorical, discrete distinction used to contrast phonemes (e.g., /p/ vs /b/ in English). At the phonetic level, voicing is a continuous acoustic and articulatory property — the same speaker may produce /b/ with varying degrees of voicing depending on position in a word, speaking rate, and surrounding sounds. Features capture categorical phonological contrasts; phonetics captures gradient realization."

- question: "Why do phonologists analyze phonemes into sub-segmental features rather than treating each phoneme as an unanalyzable primitive?"
  type: short-answer
  answer: "Features allow phonologists to capture generalizations about which sounds pattern together in phonological rules. If phonemes were atoms, rules that apply to natural classes (all nasals, all voiceless stops) would require listing each member individually and would miss the fact that membership is predicted by shared properties. Features make those shared properties explicit and allow a single rule to cover the whole class, making the theory both more concise and more explanatory."
  explanation: "The deeper point is predictive power: feature theory predicts that only certain groupings of sounds should behave uniformly in phonological rules — those defined by a shared feature value. If we observe that a rule applies to /p/, /t/, /k/ (all voiceless stops) but not /b/, /d/, /g/, feature theory explains this with [+consonantal, -voice, -continuant]. Treating phonemes as atoms would make it coincidental rather than principled."
```

## Explainer

When you studied phonological systems, you learned that languages select a subset of all possible sounds — phonemes — and use contrasts between them to distinguish words. But what makes two sounds contrast? What makes /p/ and /b/ different in a way that matters, while many other sound differences are ignored by the phonological system? Feature theory answers this by decomposing phonemes into smaller, independently meaningful components called **distinctive features**.

The intuition is that phonemes are not atoms — they are bundles of properties. The phonemes /p/ and /b/ are nearly identical: both are bilabial stops, formed by closing both lips and releasing a burst of air. The single difference is voicing: /b/ is produced with the vocal folds vibrating ([+voice]), and /p/ is not ([-voice]). Feature theory represents this as the only difference in their feature specifications. This is more than notational convenience — it makes a testable prediction: any phonological rule that affects /b/ for voicing-related reasons should also affect /d/ and /g/, since they share the feature [+voice]. Cross-linguistic evidence overwhelmingly confirms these predictions.

The concept of **natural classes** follows directly. A natural class is a set of sounds that share at least one feature value and that behave as a unit in phonological rules. The nasals /m/, /n/, and /ŋ/ all carry the feature [+nasal]. In language after language — English, Japanese, Swahili — vowels nasalize before nasals, nasals assimilate to adjacent places of articulation, and nasals pattern together in ways that non-nasal consonants do not. Feature theory predicts exactly which classes should appear as natural classes, and which groupings (say, /p/, /r/, and /ŋ/) should not pattern together — because they share no defining feature.

**Feature geometry** extends the theory by organizing features into a hierarchical tree rather than a flat list. Not all features behave independently: place features (where in the mouth the articulation happens — labial, coronal, dorsal) can spread as a unit in assimilation without affecting laryngeal features (voicing). Feature geometry captures this by grouping place features under a single dominating node; spreading that node moves all place features together. This predicts which assimilation patterns are possible and which would be typologically unnatural.

A critical distinction to carry forward is that features operate at the **phonological** level, not the phonetic level. [+/-voice] is a categorical contrast used to distinguish phonemes; in actual speech, voicing is a continuous acoustic property that varies with context, speaker, and rate. Feature theory is a model of the grammar, not a direct description of acoustics. This is the same distinction as the phoneme/allophone distinction you encountered in phonological systems, now extended downward to the sub-segmental level.
