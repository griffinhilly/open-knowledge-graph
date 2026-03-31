---
id: induction-and-competence
title: Induction and Competence
domain: biology
course: developmental-biology
prerequisites:
- id: germ-layer-formation
  type: hard
- id: morphogen-gradients
  type: hard
builds-toward:
- cell-fate-determination
- organogenesis-basics
tags:
- embryonic-induction
- competence
- tissue-interaction
- Spemann-organizer
stage: advanced
status: validated
---
# Induction and Competence

## Core Idea
Embryonic induction is the process by which one group of cells (the inducer) signals to an adjacent group (the responder), changing the responder's developmental fate. Induction requires that the responding tissue be competent — expressing the appropriate receptors and intracellular signal transduction machinery to respond to the inductive signal. Competence is temporally restricted: tissues can respond to inductive signals only during specific developmental windows, after which they lose responsiveness regardless of signal strength. Virtually every organ in the body is formed through a cascade of sequential inductive interactions, where the product of one induction becomes the inducer for the next.

## Questions

```yaml
- question: "Spemann showed that the dorsal lip of the blastopore (organizer) can induce a second neural axis when transplanted to the ventral side. If the same transplant is performed at a much later stage (after neural tube closure), no second axis forms. Why?"
  type: multiple-choice
  options:
    - "The organizer loses its ability to secrete signals at later stages"
    - "The ventral ectoderm has lost its competence to respond to neural-inducing signals — the temporal window during which ectoderm can be redirected from epidermal to neural fate has closed"
    - "The transplanted cells are rejected by the immune system at later stages"
    - "Neural induction only works in one specific species of frog"
  answer: 1
  explanation: "Competence is time-limited. During gastrulation, ventral ectoderm expresses the receptors and downstream transcription factors needed to respond to neural-inducing signals (BMP inhibitors from the organizer). After the competence window closes, the ectoderm's chromatin state changes — neural gene promoters become inaccessible, epidermal commitment is locked in, and the same signals no longer elicit a neural response. This temporal restriction of competence ensures that inductive events occur in the correct developmental sequence and prevents aberrant tissue formation at inappropriate stages."

- question: "Induction is a one-directional process: the inducer signals and the responder responds, with no feedback from responder to inducer."
  type: true-false
  answer: false
  explanation: "Many inductive interactions are reciprocal — the responder signals back to the inducer, modifying its behavior. A classic example is kidney development: the ureteric bud (inducer) signals to the metanephric mesenchyme (responder) to form nephrons, but the mesenchyme simultaneously signals back to the ureteric bud to promote its branching. Without reciprocal signaling, neither tissue develops properly. This reciprocal induction is common in organogenesis and creates interdependent tissue interactions where each tissue requires signals from the other."

- question: "What molecular changes underlie the loss of competence in a responding tissue?"
  type: short-answer
  answer: "Loss of competence involves changes at multiple levels: downregulation of receptors for the inductive signal (the tissue can no longer detect the signal), changes in intracellular signaling components (even if some signal reaches the cell, it cannot be transduced), and epigenetic changes in chromatin state (target gene promoters become inaccessible through histone modification or DNA methylation, making them unresponsive even if the upstream signaling pathway is activated). The responding tissue essentially closes the molecular doors through which the inductive signal would act, committing irreversibly to its current fate. Competence is thus a property of the entire signal-reception-to-gene-activation chain, not just receptor availability."
  explanation: "This multi-level restriction of competence makes developmental transitions robust — once a tissue passes the competence window, it cannot be redirected by aberrant signals. This is functionally important for preventing teratomas and ensuring orderly sequential development."
```

## Explainer

Development does not unfold from a pre-existing blueprint encoded in the genome. Instead, it proceeds through a cascade of **inductive interactions** — one tissue signals to another, changing its fate, and the newly induced tissue then signals to its neighbors, changing their fate in turn. Each organ in the body is the product of multiple sequential inductions, each requiring the right signal, the right receiving tissue, and the right developmental timing.

The concept of **embryonic induction** was established by Spemann and Mangold's organizer transplant experiment. When the dorsal lip of the blastopore (the organizer) was grafted to the ventral side of a host embryo, it induced the host's ventral ectoderm to form a second nervous system and body axis. The key insight was that the host cells, not the transplanted cells, formed most of the induced structures — meaning the organizer was not simply contributing cells, but was changing the fate of neighboring host cells through signaling. The molecular basis, elucidated decades later, is that the organizer secretes BMP antagonists (Chordin, Noggin, Follistatin), creating a local environment of low BMP signaling in which ectoderm adopts neural rather than epidermal fate.

But the organizer's signal only works if the responding tissue is **competent** to respond. Competence means having the complete molecular machinery — receptors, signal transduction components, accessible target gene chromatin — to convert the inductive signal into a transcriptional response. Competence is **temporally restricted**: ectoderm can be induced to become neural tissue only during a specific developmental window (roughly corresponding to gastrulation). Before the window, the tissue may lack the necessary receptors. After the window, chromatin remodeling has closed the neural gene promoters, and the tissue is committed to its current fate regardless of what signals it receives. This temporal restriction of competence is why timing is so critical in development — the same signal at different times can have completely different (or no) effect.

Sequential, cascading inductions build the embryo step by step. The organizer induces neural tissue. Neural tissue induces the lens of the eye from overlying ectoderm. The lens induces the cornea from the ectoderm covering it. Each induction depends on the product of the previous one, creating a chain of dependencies that ensures organs form in the right place, at the right time, in the right sequence. Reciprocal inductions — where the inducer and responder signal back and forth — add another layer: in kidney development, the ureteric bud and metanephric mesenchyme each require signals from the other, ensuring that the two tissues develop in coordination. This interplay of induction and competence is the fundamental mechanism by which a single fertilized egg builds a complex, precisely organized organism.
