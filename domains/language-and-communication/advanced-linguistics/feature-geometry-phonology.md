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
stage: expert
status: validated
---

# Feature Geometry in Phonology

## Core Idea
Feature geometry organizes phonological features into hierarchical tree structures where some features dominate others, capturing natural classes and explaining why certain features spread or delete as a unit. Nasal spreading, for instance, spreads the [nasal] node rather than individual features.

## How It's Best Learned
Construct feature-geometric hierarchies for a language's phonological processes; verify that features spreading together share a common dominating node.

## Common Misconceptions
Feature geometry is not universal across all features; its structure may vary by language and is motivated by phonological processes specific to each system.

## Questions

```yaml
- question: "In Language X, an assimilation process copies both [labial] and [round] from one segment to an adjacent one, but never copies [voice] or [nasal] in the same process. In Language Y, a deletion process deletes both [voice] and [spread glottis] together. What does feature geometry predict from these data?"
  type: multiple-choice
  options:
    - "[labial] and [round] should be terminal nodes in the same branch; [voice] and [spread glottis] should be terminal nodes in a different branch"
    - "All four features should be grouped under one Laryngeal node, since they all involve laryngeal activity"
    - "Feature geometry cannot explain these patterns because the features involved cross natural class boundaries"
    - "The two languages have incompatible phonological systems and cannot be compared within a single framework"
  answer: 0
  explanation: "The core insight of feature geometry: features that spread or delete together share a dominating node. [labial] and [round] spreading together in Language X is evidence they are sisters under a shared node (e.g., a Place or sub-Place node). [voice] and [spread glottis] deleting together in Language Y is evidence they are sisters under the Laryngeal node. The fact that [voice] does not copy with [labial] in Language X confirms they belong to different branches."

- question: "What is the primary evidence that motivates the construction of a feature-geometric tree for a particular language?"
  type: multiple-choice
  options:
    - "The universal hierarchy proposed in phonological theory — all languages share the same feature tree structure"
    - "The phoneme inventory of the language — which sounds exist determines which features must be included and how they are related"
    - "Spreading and deletion patterns — which features consistently behave together as a unit in phonological processes"
    - "Acoustic spectrogram analysis showing which features are produced by overlapping articulatory gestures"
  answer: 2
  explanation: "Feature geometry is built from phonological behavior, not imposed top-down from a universal template. If processes in a language consistently spread features X and Y together but never X and Z, the tree groups X and Y under a shared node. This makes the tree structure an empirical hypothesis — testable by additional processes discovered in the language — rather than a given."

- question: "The fact that nasal assimilation in English (in- → im- before bilabials, iŋ- before velars) can be described as a single rule spreading the Place node — rather than three separate rules — is evidence for organizing place features under a dominating node."
  type: true-false
  answer: true
  explanation: "Without hierarchical organization, three separate rules would be required: one for labial assimilation, one for coronal, one for dorsal. Feature geometry reduces these to one rule (spread the Place node of the following consonant) applied to one structural node — explanatory parsimony that follows directly from the hierarchical grouping of place features. The unification of these patterns is the empirical argument for the Place node."

- question: "Feature geometry proposes a single universal tree structure that applies to most human languages, with nearly every language sharing the same hierarchy of nodes and terminal features."
  type: true-false
  answer: false
  explanation: "This is the key misconception. Feature geometry is a framework, not a universal blueprint. The structure must be motivated language by language — the tree is a hypothesis about which features pattern together as units, based on the spreading and deletion processes actually observed in that language's phonology. Some structures (like a Place node) may recur widely, but their justification must come from language-specific phonological evidence."

- question: "Why is evidence from phonological spreading processes more useful for motivating feature-geometric structure than evidence from the phoneme inventory alone?"
  type: short-answer
  answer: "The phoneme inventory tells you which features a language uses, but not how those features are organized relative to each other. Spreading processes reveal behavioral dependencies — when feature A spreads, do features B and C always accompany it? If they do, that is evidence B and C are dominated by the same node as A. The inventory might include [labial], [voice], and [nasal], but only spreading data can reveal that [labial] and [round] pattern together while [voice] does not. Feature-geometric structure is a claim about phonological constituency, and constituency is only visible through behavior."
  explanation: "This is analogous to discovering syntactic constituency through movement and deletion tests rather than from the sequence of words alone. The geometric structure is an abstract representation motivated by phonological behavior — it cannot be read off the surface inventory, only inferred from how features co-vary across phonological processes."
```

## Explainer

From your study of autosegmental phonology, you know that phonological features are not bundled inseparably to segments but can spread, delete, and associate independently across a timeline. From your study of phonological features, you know that sounds are analyzed as matrices of binary features — [+nasal], [−voice], [+labial] and so on — that capture the natural classes that participate in phonological rules. Feature geometry asks a deeper question: are all features equal, or are some features organized into hierarchical relationships that explain *why* certain subsets of features systematically behave together?

The core insight of **feature geometry** is that features are not a flat list but a **tree structure** — features are organized into constituent nodes, where some features are dominated by (grouped under) a higher node. The evidence for this comes from **spreading and deletion patterns**: when a phonological process spreads a group of features to an adjacent segment, the features that spread together reliably are those that share a common dominating node. A process that spreads nasality does not simultaneously spread voicing or place of articulation — these features belong to different branches of the tree. Conversely, place features (labial, coronal, dorsal) often spread as a unit: an assimilation process targeting place of articulation will copy all the place features of a segment at once, not pick one arbitrarily. This is explained by grouping all place features under a single **Place node** — spreading the Place node spreads all its daughters.

Consider the classic example of **nasal assimilation** in languages like English: the prefix *in-* surfaces as *im-* before bilabials (*impossible*), *in-* before coronals (*incredible*), and *iŋ-* before velars (*incongruous*). The nasal assimilates in place of articulation to the following consonant, copying its labial, coronal, or dorsal specification. Feature geometry represents this as spreading the Place node of the following consonant onto the nasal — a single spreading rule, applied to a single node, producing all the surface variations. Without feature geometry, you would need three separate rules; with it, one rule and a structured tree.

The **feature-geometric tree** as developed by researchers like Elizabeth Clements and Elizabeth Hume typically organizes features under several intermediate nodes: a **Laryngeal node** (grouping voice, spread glottis, constricted glottis), a **Place node** (grouping labial, coronal, dorsal), and sometimes a **Manner** node. The exact structure is not universal and must be motivated language by language — this is the key methodological point. Feature geometry is not a rigid universal blueprint but a framework: you build the tree that explains the spreading and deletion patterns you observe in a specific language's phonology, and the tree you construct is a hypothesis about which features pattern together as units. When a language's processes consistently treat [labial] and [round] as a unit that spreads together, you have evidence for a node dominating both. Feature geometry thus makes the abstract structure of phonological representations empirically testable through the evidence of phonological behavior.
