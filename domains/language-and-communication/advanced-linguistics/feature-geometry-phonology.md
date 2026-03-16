---
id: feature-geometry-phonology
title: Feature Geometry in Phonology
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: autosegmental-phonology
  type: hard
- id: phonological-features
  type: hard
tags:
- phonology
- features
- feature-geometry
stage: advanced
status: draft
---

# Feature Geometry in Phonology

## Core Idea
Feature geometry organizes phonological features into hierarchical tree structures where some features dominate others, capturing natural classes and explaining why certain features spread or delete as a unit. Nasal spreading, for instance, spreads the [nasal] node rather than individual features.

## How It's Best Learned
Construct feature-geometric hierarchies for a language's phonological processes; verify that features spreading together share a common dominating node.

## Common Misconceptions
Feature geometry is not universal across all features; its structure may vary by language and is motivated by phonological processes specific to each system.

## Explainer

From your study of autosegmental phonology, you know that phonological features are not bundled inseparably to segments but can spread, delete, and associate independently across a timeline. From your study of phonological features, you know that sounds are analyzed as matrices of binary features — [+nasal], [−voice], [+labial] and so on — that capture the natural classes that participate in phonological rules. Feature geometry asks a deeper question: are all features equal, or are some features organized into hierarchical relationships that explain *why* certain subsets of features systematically behave together?

The core insight of **feature geometry** is that features are not a flat list but a **tree structure** — features are organized into constituent nodes, where some features are dominated by (grouped under) a higher node. The evidence for this comes from **spreading and deletion patterns**: when a phonological process spreads a group of features to an adjacent segment, the features that spread together reliably are those that share a common dominating node. A process that spreads nasality does not simultaneously spread voicing or place of articulation — these features belong to different branches of the tree. Conversely, place features (labial, coronal, dorsal) often spread as a unit: an assimilation process targeting place of articulation will copy all the place features of a segment at once, not pick one arbitrarily. This is explained by grouping all place features under a single **Place node** — spreading the Place node spreads all its daughters.

Consider the classic example of **nasal assimilation** in languages like English: the prefix *in-* surfaces as *im-* before bilabials (*impossible*), *in-* before coronals (*incredible*), and *iŋ-* before velars (*incongruous*). The nasal assimilates in place of articulation to the following consonant, copying its labial, coronal, or dorsal specification. Feature geometry represents this as spreading the Place node of the following consonant onto the nasal — a single spreading rule, applied to a single node, producing all the surface variations. Without feature geometry, you would need three separate rules; with it, one rule and a structured tree.

The **feature-geometric tree** as developed by researchers like Elizabeth Clements and Elizabeth Hume typically organizes features under several intermediate nodes: a **Laryngeal node** (grouping voice, spread glottis, constricted glottis), a **Place node** (grouping labial, coronal, dorsal), and sometimes a **Manner** node. The exact structure is not universal and must be motivated language by language — this is the key methodological point. Feature geometry is not a rigid universal blueprint but a framework: you build the tree that explains the spreading and deletion patterns you observe in a specific language's phonology, and the tree you construct is a hypothesis about which features pattern together as units. When a language's processes consistently treat [labial] and [round] as a unit that spreads together, you have evidence for a node dominating both. Feature geometry thus makes the abstract structure of phonological representations empirically testable through the evidence of phonological behavior.
