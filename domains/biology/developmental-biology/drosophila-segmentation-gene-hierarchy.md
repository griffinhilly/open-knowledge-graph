---
id: drosophila-segmentation-gene-hierarchy
title: The Drosophila Segmentation Gene Hierarchy
domain: biology
course: developmental-biology
prerequisites:
- id: axis-formation
  type: hard
- id: morphogen-gradients
  type: hard
- id: enhancers-silencers-eukaryotic
  type: soft
- id: pattern-formation
  type: soft
builds-toward:
- hox-genes-and-body-plan
tags:
- drosophila
- segmentation
- gap-genes
- pair-rule-genes
- segment-polarity
- enhancers
stage: expert
status: validated
---

# The Drosophila Segmentation Gene Hierarchy

## Core Idea
The fruit fly embryo is divided into segments by a cascade of genes that act in sequence, each tier refining the pattern set by the one before. Maternal gradients such as Bicoid and Nanos regulate gap genes, which are expressed in broad bands; gap genes regulate pair-rule genes, expressed in seven stripes; pair-rule genes regulate segment polarity genes, expressed in fourteen stripes, one per segment. Homeotic (Hox) genes then give each segment its identity. Christiane Nüsslein-Volhard and Eric Wieschaus identified many of these genes in a genetic screen published in 1980, and they shared the 1995 Nobel Prize in Physiology or Medicine with Edward B. Lewis.

## How It's Best Learned
Show the expression pattern of each tier on a cartoon embryo, side by side, and then show the larval cuticle of a mutant from each class. Ask students to predict the missing pattern from the expression domain. The even-skipped stripe 2 enhancer makes a good worked example of how broad gradients are converted into a sharp stripe.

## Common Misconceptions
- The seven pair-rule stripes are produced by one enhancer that is read the same way in every stripe. (Pair-rule genes such as even-skipped have several separate enhancers, each responding to a different combination of gap proteins and driving one or two stripes.)
- Segmentation genes decide what each segment becomes, such as a wing-bearing segment. (Segmentation genes set the number and boundaries of segments; Hox genes specify segment identity.)
- Gene products in the early fly embryo must cross cell membranes to signal. (The early embryo is a syncytium, many nuclei in one shared cytoplasm, so transcription factors such as Bicoid diffuse directly between nuclei.)

## Questions

```yaml
- question: "A fly mutant larva is missing every other segment-width region along its body. Which class of gene is most likely mutated?"
  type: multiple-choice
  options: ["A maternal effect gene such as bicoid", "A gap gene", "A pair-rule gene", "A Hox gene"]
  answer: 2
  explanation: "Pair-rule genes are expressed in seven stripes, one in every second segment-width region. Losing a pair-rule gene deletes pattern elements in alternating regions, giving a larva with about half the normal number of segments. Fushi tarazu, Japanese for 'too few segments,' was named for this phenotype."
- question: "The seven stripes of even-skipped expression are all driven by a single enhancer that responds identically in every stripe."
  type: true-false
  answer: false
  explanation: "even-skipped has several modular enhancers. The stripe 2 enhancer is activated by Bicoid and Hunchback and repressed by Giant on its anterior side and Krüppel on its posterior side, which confines expression to a narrow band. Other enhancers drive other stripes, and some drive two stripes each."
- question: "Why can a transcription factor such as Bicoid form a gradient across the early fly embryo without any cell-to-cell signaling?"
  type: short-answer
  answer: "The early Drosophila embryo is a syncytium: its nuclei divide without forming cell membranes, so they all share one cytoplasm. Bicoid protein, translated from mRNA at the anterior pole, diffuses through this shared cytoplasm and enters nuclei directly, forming a concentration gradient from front to back."
  explanation: "Once cell membranes form, at the cellular blastoderm stage, later tiers such as the segment polarity genes must use secreted signals like Wingless and Hedgehog to maintain segment boundaries."
- question: "What is the main job of the gap genes in the segmentation hierarchy?"
  type: multiple-choice
  options: ["To specify the identity of each segment", "To divide the embryo into broad regions by reading maternal gradients and to regulate pair-rule genes", "To form the boundaries within each segment", "To control the dorsal-ventral axis"]
  answer: 1
  explanation: "Gap genes such as hunchback, Krüppel, knirps and giant are expressed in broad, overlapping domains. Their mutants lack a contiguous block of segments, a 'gap' in the pattern. Their proteins then act together on the enhancers of pair-rule genes."
```

## Explainer
A fruit fly larva has a clear series of segments: several head segments fused together, three thoracic segments and eight abdominal segments. How does a single oval egg turn into this repeating pattern? Drosophila provided the first detailed answer.

In the late 1970s Christiane Nüsslein-Volhard and Eric Wieschaus, working in Heidelberg, mutated flies on a large scale and looked for embryos with abnormal segment patterns. They found mutants that fell into a few clear classes, and the classes corresponded to steps in a hierarchy.

The hierarchy begins before fertilization. The mother deposits bicoid mRNA at the anterior pole of the egg and nanos mRNA at the posterior. In the early embryo, nuclei divide many times without forming cell membranes, creating a syncytium. Bicoid protein spreads from the front through the shared cytoplasm, forming a gradient. Nanos protein at the back blocks translation of maternal hunchback mRNA there.

These maternal gradients regulate the gap genes, including hunchback, Krüppel, knirps and giant. Each is expressed in one or two broad bands. A gap mutant lacks several neighboring segments.

Gap proteins regulate the pair-rule genes, such as even-skipped, fushi tarazu and hairy. These are expressed in seven stripes. The stripes arise because the pair-rule genes carry separate enhancers that each read a different local mix of gap proteins. The even-skipped stripe 2 enhancer is a classic case. Bicoid and Hunchback activate it, Giant represses it from the front and Krüppel represses it from behind, so it is active only in a narrow band. Pair-rule mutants lose pattern in alternating segment-width regions.

Pair-rule proteins then regulate the segment polarity genes, such as engrailed, wingless and hedgehog, which form fourteen stripes. By this time cell membranes have formed. Cells expressing engrailed and cells expressing wingless sit next to each other at each boundary and keep each other's expression going through the secreted signals Hedgehog and Wingless. Segment polarity mutants have part of every segment replaced by a mirror-image copy of another part.

With boundaries set, Hox genes, the homeotic selector genes studied by Edward B. Lewis, assign each segment its identity. Their expression is also set by gap and pair-rule proteins.

The fly hierarchy shows a general principle of development: smooth gradients are read by combinations of transcription factors, through modular enhancers, to produce sharp and repeated patterns. Many of these gene families, such as hedgehog and wingless (Wnt), are used in vertebrate development as well.
