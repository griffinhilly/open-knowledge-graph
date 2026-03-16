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
stage: advanced
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

## Explainer

Before feature geometry, phonological features were organized as **flat matrices**: every segment (consonant or vowel) was represented as a bundle of feature values, with each feature sitting at the same level, independent of the others. You already know from studying phonological features that these features encode real phonetic properties — [nasal], [voiced], [labial], and so on. The flat-matrix approach worked for basic segment descriptions but struggled with a recurring empirical observation: certain features behave as natural classes, changing together or blocking each other's application in systematic ways that an unstructured list cannot explain.

The key insight of feature geometry is **hierarchical organization**. Rather than all features sitting at the same level, they are grouped under intermediate nodes that represent natural classes reflecting articulation. The **Place node**, for example, dominates features like [labial], [coronal], and [dorsal] — the features that specify where in the mouth a consonant is produced. When assimilation occurs (a consonant taking on the place of articulation of its neighbor), the process applies to the Place node as a whole, automatically moving all features beneath it simultaneously. This explains why assimilation processes are holistic — you don't find phonological rules that spread [labial] but leave [dorsal] behind, because they are dominated by the same node. The geometry encodes the dependencies that articulatory phonetics reveals.

**Underspecification** adds a second level of economy to underlying representations. The core claim is that not all feature values need to be stored in the mental lexicon: many that appear in surface forms are entirely predictable and can be filled in later by rules or default processes. Consider voicing in obstruents: in a language where voicing is the default and only a subset of obstruents are underlyingly voiceless, storing [+voiced] for every voiced obstruent is redundant. You mark only the exceptions ([−voiced]) and let the rest fill in. **Radical underspecification** extends this principle even to features that contrast in the phonology, leaving them unvalued underlyingly when their surface values are predictable from context or position.

These two ideas work together to explain several otherwise puzzling phenomena. **Spreading** — where a feature copies from one segment to adjacent ones — is modeled as the association of a feature node across the tier, rather than a feature-changing rule applied segment by segment: the feature doesn't transform its neighbors, it extends its own domain. **Co-occurrence restrictions** — why certain feature combinations never occur in any language — follow naturally from the geometry: features dominated by the same node cannot independently take on conflicting values without violating the tree's structure. And underspecification explains why phonological rules can target the *absence* of a specification: a segment with no Place value can assimilate freely to its neighbor precisely because it has no place feature to preserve. Together, feature geometry and underspecification replace an arbitrary list with a structured representation that encodes what phonetics already knew — that speech sounds are built from organized, hierarchically dependent articulatory properties.
