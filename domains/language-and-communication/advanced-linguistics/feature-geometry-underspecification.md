---
id: feature-geometry-underspecification
title: Feature Geometry and Underspecification
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: phonological-features
  type: hard
- id: phonological-systems
  type: soft
tags:
- feature-geometry
- features
- underspecification
stage: expert
status: draft
---

# Feature Geometry and Underspecification

## Core Idea
Feature geometry organizes phonological features hierarchically rather than as flat matrices, with nodes representing natural classes and feature dependencies. Underspecification proposes that not all features are specified in underlying representations; unspecified features are filled by rules or default processes. This explains why certain feature combinations never occur, why features behave interdependently, and how minimal specification reduces memorization.

## How It's Best Learned
Draw feature geometry trees and show how hierarchical organization predicts which features can undergo independent processes and which must change together. Compare representations under full specification and underspecification.

## Common Misconceptions
- Underspecification does not mean features are absent; unspecified features are present but not valued in underlying form.
- Feature geometry is not a cover for rule-based processes; it reflects structural properties of the phonological system.

## Questions

```yaml
- question: "English nasal assimilation changes 'in-' to 'im-' before bilabials (impossible) and to 'iŋ-' before velars (incomplete). Why does the entire place specification change rather than just one feature?"
  type: multiple-choice
  options:
    - "Each language independently stipulates which features must assimilate together"
    - "All place features are dominated by a single Place node, so assimilation applies to the whole node and moves all dominated features simultaneously"
    - "The nasals /m/, /n/, and /ŋ/ share the same underlying representation and only surface differently"
    - "Assimilation rules operate on segments as units, not on individual features, so all features change"
  answer: 1
  explanation: "In feature geometry, [labial], [coronal], and [dorsal] features are all dominated by the Place node. When place assimilation occurs, it targets the Place node — the nasal's Place specification is replaced by that of the following consonant, automatically including all features beneath it. This is why assimilation is holistic: the geometry encodes the dependency. A flat-matrix approach would need special stipulations; feature geometry makes holistic behavior a structural prediction."

- question: "In a language where all obstruents are voiced by default and only a few are underlyingly voiceless, what does underspecification predict about how voicing is stored in the mental lexicon?"
  type: multiple-choice
  options:
    - "Every voiced obstruent is marked [+voiced] and every voiceless obstruent is marked [−voiced] in the lexicon"
    - "Only the voiceless obstruents are specified as [−voiced]; voiced obstruents are unvalued for voicing and receive [+voiced] by a default rule"
    - "Neither voiced nor voiceless obstruents are specified for voicing; surface values are entirely computed by context"
    - "The lexicon marks all obstruents as [+voiced] since that is the majority pattern"
  answer: 1
  explanation: "Underspecification exploits predictability: when a feature value can be assigned by a rule (voiced is default), it need not be stored. The lexicon marks only the non-default, unpredictable value — [−voiced] for voiceless exceptions. Voiced obstruents are left unvalued; the default rule assigns [+voiced] to all segments lacking a voicing specification. This reduces memorization without losing information. Option D would mean voiced obstruents ARE specified, defeating the economy of underspecification."

- question: "A segment that has no Place specification in its underlying representation is better positioned to undergo place assimilation than a fully specified segment."
  type: true-false
  answer: true
  explanation: "A segment with no underlying Place value has nothing to preserve or conflict with, so it can freely receive the Place node of its neighbor through assimilation. A fully specified segment would create a structural conflict — two Place values competing — which is typically resolved by blocking assimilation or causing deletion. Underspecification thus directly predicts which segments will be 'chameleon-like': those with absent specifications are the most transparent to spreading processes."

- question: "Underspecification proposes that some phonological features are absent from the grammar entirely — they do not exist for sounds that appear to lack them."
  type: true-false
  answer: false
  explanation: "This is a key misconception. Underspecification does not claim features are absent from the phonological system — it claims they are not valued in underlying representations, but remain as structural positions that can be filled by rules, defaults, or assimilation. An 'absent' feature could never be filled in; an 'unspecified' feature is a structural slot waiting to receive a value. Feature geometry and underspecification model how these slots get filled predictably."

- question: "How does hierarchical feature organization explain why phonological rules systematically affect natural classes of sounds rather than arbitrary groupings?"
  type: short-answer
  answer: "In a flat feature matrix, any subset of features could in principle be targeted by a rule, including arbitrary combinations. Feature geometry organizes features into hierarchical nodes corresponding to articulatory groupings — the Place node, the Laryngeal node, the Manner node. A phonological rule can only target a node (a natural class defined by shared hierarchical position) or a feature beneath it. This structural constraint makes it impossible to write a rule targeting an arbitrary mix of features from different nodes. The hierarchy encodes the phonetic knowledge that sounds behave as natural classes — bilabials, velars, nasals — rather than arbitrary feature bundles."
  explanation: "The empirical prediction is that phonological processes respect articulatory organization: you find rules spreading all place features together (targeting the Place node) but not rules spreading [labial] plus [nasal] while leaving other place features alone. Feature geometry converts this observation from an unexplained coincidence into a structural prediction."
```

## Explainer

Before feature geometry, phonological features were organized as **flat matrices**: every segment (consonant or vowel) was represented as a bundle of feature values, with each feature sitting at the same level, independent of the others. You already know from studying phonological features that these features encode real phonetic properties — [nasal], [voiced], [labial], and so on. The flat-matrix approach worked for basic segment descriptions but struggled with a recurring empirical observation: certain features behave as natural classes, changing together or blocking each other's application in systematic ways that an unstructured list cannot explain.

The key insight of feature geometry is **hierarchical organization**. Rather than all features sitting at the same level, they are grouped under intermediate nodes that represent natural classes reflecting articulation. The **Place node**, for example, dominates features like [labial], [coronal], and [dorsal] — the features that specify where in the mouth a consonant is produced. When assimilation occurs (a consonant taking on the place of articulation of its neighbor), the process applies to the Place node as a whole, automatically moving all features beneath it simultaneously. This explains why assimilation processes are holistic — you don't find phonological rules that spread [labial] but leave [dorsal] behind, because they are dominated by the same node. The geometry encodes the dependencies that articulatory phonetics reveals.

**Underspecification** adds a second level of economy to underlying representations. The core claim is that not all feature values need to be stored in the mental lexicon: many that appear in surface forms are entirely predictable and can be filled in later by rules or default processes. Consider voicing in obstruents: in a language where voicing is the default and only a subset of obstruents are underlyingly voiceless, storing [+voiced] for every voiced obstruent is redundant. You mark only the exceptions ([−voiced]) and let the rest fill in. **Radical underspecification** extends this principle even to features that contrast in the phonology, leaving them unvalued underlyingly when their surface values are predictable from context or position.

These two ideas work together to explain several otherwise puzzling phenomena. **Spreading** — where a feature copies from one segment to adjacent ones — is modeled as the association of a feature node across the tier, rather than a feature-changing rule applied segment by segment: the feature doesn't transform its neighbors, it extends its own domain. **Co-occurrence restrictions** — why certain feature combinations never occur in any language — follow naturally from the geometry: features dominated by the same node cannot independently take on conflicting values without violating the tree's structure. And underspecification explains why phonological rules can target the *absence* of a specification: a segment with no Place value can assimilate freely to its neighbor precisely because it has no place feature to preserve. Together, feature geometry and underspecification replace an arbitrary list with a structured representation that encodes what phonetics already knew — that speech sounds are built from organized, hierarchically dependent articulatory properties.
