---
id: gene-regulation-prokaryotes
title: Gene Regulation in Prokaryotes
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: transcription
  type: hard
- id: gene-expression-overview
  type: hard
- id: prokaryotic-cells
  type: soft
- id: translation
  type: soft
builds-toward:
- gene-regulation-eukaryotes
tags:
- operon
- lac operon
- trp operon
- repressor
- promoter
- transcription factor
stage: advanced
status: validated
---
# Gene Regulation in Prokaryotes

## Core Idea
Prokaryotic gene regulation is primarily achieved at the level of transcription initiation through operons — clusters of co-regulated genes sharing a single promoter and operator. In the lac operon, the repressor protein binds the operator to block RNA polymerase access in the absence of lactose; allolactose (a lactose derivative) acts as an inducer that releases the repressor, enabling transcription. Positive regulation by catabolite activator protein (CAP) additionally responds to glucose availability. The trp operon uses attenuation and a repressor activated by the end product tryptophan, illustrating feedback repression.

## How It's Best Learned
Work through the lac operon under four conditions (±lactose, ±glucose) and predict transcription level for each. Draw diagrams showing repressor, operator, and RNA polymerase interactions.

## Common Misconceptions
- In an inducible operon like lac, the default state is OFF; in a repressible operon like trp, the default state is ON.
- The inducer does not directly activate RNA polymerase; it relieves repression by binding the repressor.

## Questions

```yaml
- question: "In a bacterium growing in a medium that contains lactose but no glucose, what is the transcriptional state of the lac operon?"
  type: multiple-choice
  options: ["Off — the repressor is bound to the operator because lactose is present", "Off — CAP cannot bind without glucose, so transcription is fully blocked", "High — both repression is relieved (allolactose present) and CAP is activated (low glucose)", "Low — the operon is transcribed at basal level because neither signal is optimal"]
  answer: 2
  explanation: "When lactose is present, allolactose (a derivative) binds the lac repressor, causing it to release the operator — this relieves negative regulation. When glucose is absent, cAMP levels rise, activating CAP (catabolite activator protein), which binds upstream of the promoter and strongly stimulates RNA polymerase binding — this is positive regulation. Both conditions favor maximal transcription, making this the highest-expression scenario."

- question: "When allolactose binds the lac repressor, it directly activates RNA polymerase to begin transcription of the lac genes."
  type: true-false
  answer: false
  explanation: "Allolactose (the inducer) does not touch RNA polymerase. It binds the repressor protein and causes a conformational change that makes the repressor release the operator sequence. This simply removes a roadblock that was preventing RNA polymerase from proceeding. RNA polymerase was already capable of transcribing — the repressor was blocking it. This distinction matters because it reveals the logic of negative regulation: the default is blocked, and the inducer derepresses rather than activates."

- question: "What is the fundamental difference between an inducible operon (like lac) and a repressible operon (like trp) in terms of their default transcriptional state?"
  type: short-answer
  answer: "An inducible operon is OFF by default — transcription is blocked by a constitutively active repressor until an inducer molecule is present to relieve repression. A repressible operon is ON by default — transcription proceeds until the end product of the pathway accumulates and activates a repressor (corepressor), shutting genes off."
  explanation: "This distinction reflects the metabolic logic of each system. The lac operon encodes enzymes for consuming lactose — there is no point making them unless lactose is actually available, so the default state is off. The trp operon encodes enzymes for *synthesizing* tryptophan — production should continue until tryptophan is already abundant (at which point further synthesis would be wasteful), so the default state is on. Operon design matches the metabolic purpose."
```

## Explainer

You already know from studying transcription that RNA polymerase binds a promoter sequence and initiates mRNA synthesis. But a bacterium producing every protein it encodes at full blast all the time would waste enormous energy. Prokaryotic gene regulation is the cell's solution: transcription of specific genes is switched on or off in response to environmental signals, primarily through the **operon** system.

An **operon** is a cluster of functionally related genes under the control of a single promoter and operator. The **operator** is a DNA sequence between the promoter and the protein-coding genes; when a **repressor** protein binds it, RNA polymerase cannot pass, and transcription is blocked. This is *negative regulation* — a protein physically prevents gene expression.

The **lac operon** is the textbook example of an *inducible* system. Its three genes encode enzymes for importing and metabolizing lactose. In the absence of lactose, the lac repressor binds the operator and blocks transcription — making the system OFF by default. When lactose is present, some of it is converted to allolactose, which binds the repressor and causes it to release the operator. Transcription can now proceed. But there is a second layer: even with the repressor gone, transcription is only vigorous if glucose is *also* absent. Low glucose causes cAMP to accumulate, activating the **CAP** protein, which binds upstream of the promoter and dramatically enhances RNA polymerase recruitment. This positive regulatory layer ensures the cell only makes lactose-metabolizing enzymes when it actually needs them (lactose present) and when doing so is metabolically worthwhile (glucose, the preferred fuel, is scarce).

The **trp operon** illustrates the opposite logic — a *repressible* system that is ON by default. It encodes enzymes for synthesizing tryptophan. Transcription proceeds until tryptophan accumulates; excess tryptophan binds the trp repressor (acting as a corepressor), activating it to bind the operator and shut off transcription. The end product of the pathway feeds back to halt its own synthesis — an elegant feedback loop. The trp operon also uses **attenuation**, a secondary mechanism where the ribosome's speed of translating a leader sequence signals tRNA availability and terminates transcription early when tryptophan is abundant.

Together, the lac and trp operons illustrate a key design principle: regulatory logic matches metabolic purpose. Genes for consuming a substrate are off until the substrate appears (inducible). Genes for synthesizing a molecule are on until the product is abundant (repressible). Understanding these two archetypes gives you the conceptual framework for understanding the far more complex (but analogous) gene regulatory networks in eukaryotes.

