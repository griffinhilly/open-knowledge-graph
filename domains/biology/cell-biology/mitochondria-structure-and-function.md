---
id: mitochondria-structure-and-function
title: 'Mitochondria: Structure and Function'
domain: biology
course: cell-biology
prerequisites:
- id: organelles-overview
  type: hard
- id: enzyme-structure-and-function
  type: soft
- id: kinetochore-structure-and-function
  type: soft
- id: cell-structure-organelles-and-function
  type: soft
builds-toward:
- cellular-respiration-overview
- electron-transport-chain
- atp-synthesis
tags:
- mitochondria
- inner-membrane
- cristae
- matrix
- ATP
stage: formal-systems
status: validated
---
# Mitochondria: Structure and Function

## Core Idea
Mitochondria are double-membrane organelles that serve as the primary site of aerobic cellular respiration in eukaryotes. The outer membrane is smooth and permeable; the inner membrane is folded into cristae, which dramatically increase surface area for ATP synthesis. The matrix (inside the inner membrane) contains enzymes for the Krebs cycle and mitochondrial DNA, reflecting the organelle's endosymbiotic prokaryotic ancestry. The intermembrane space is key for the proton gradient that drives ATP synthesis.

## How It's Best Learned
Draw and label all four compartments (outer membrane, intermembrane space, inner membrane/cristae, matrix) and list which stage of respiration occurs in each. Connect the structure of cristae to the function of the electron transport chain.

## Common Misconceptions
- Mitochondria have their own DNA and ribosomes but cannot live independently — they rely on hundreds of nuclear-encoded proteins.
- Not all cells have the same number of mitochondria; energy-demanding cells (heart muscle, neurons) have far more.

## Questions

```yaml
- question: "Why do mitochondria have an inner membrane folded into cristae rather than a smooth inner membrane?"
  type: multiple-choice
  options: ["Cristae increase mitochondrial volume so more Krebs cycle enzymes fit in the matrix", "Cristae increase the surface area of the inner membrane, accommodating more ATP synthase and ETC complexes", "Cristae protect the mitochondrial DNA from reactive oxygen species", "Cristae separate the Krebs cycle from glycolysis to prevent interference"]
  answer: 1
  explanation: "The ETC complexes and ATP synthase are embedded in the inner membrane. More surface area means more of these complexes can be packed in, dramatically increasing the mitochondrion's ATP output capacity. This is the same design principle as intestinal villi or lung alveoli — folding is a common biological strategy for maximizing functional surface area within a fixed volume."

- question: "A mitochondrion with its own DNA and ribosomes could survive and replicate independently if isolated from the cell."
  type: true-false
  answer: false
  explanation: "Mitochondrial DNA encodes only ~13 proteins (in humans) — a tiny fraction of the ~1,500 proteins mitochondria require. The vast majority are encoded in the nuclear genome, synthesized by cytoplasmic ribosomes, and imported into the mitochondrion via translocase complexes. Mitochondria are fundamentally dependent on the cell's protein-import machinery and cannot replicate or function independently. Their genome is a vestige of their prokaryotic ancestor, substantially reduced over ~2 billion years of endosymbiosis."

- question: "Why is the intermembrane space specifically important for ATP synthesis, rather than just any compartment outside the inner membrane?"
  type: short-answer
  answer: "The ETC pumps protons from the matrix into the intermembrane space, creating a concentrated reservoir of H⁺. Because the intermembrane space is enclosed by the outer membrane, the protons cannot simply diffuse away — they are trapped at a high concentration. ATP synthase spans the inner membrane, and those trapped protons flow back through it into the matrix, driving ATP production."
  explanation: "ATP synthesis depends on maintaining a proton concentration difference (gradient) across the inner membrane. The intermembrane space acts as a holding chamber: the outer membrane is permeable to small ions (via porins) but the enclosed geometry keeps the proton-motive force intact long enough for ATP synthase to harvest it. If the outer membrane were absent, protons would equilibrate with the cytoplasm and the gradient would collapse."
```

## Explainer

From your study of organelles, you know that mitochondria are membrane-bound compartments in eukaryotic cells. What makes them distinctive — and worth understanding in structural detail — is that their internal architecture is directly engineered for a specific job: capturing energy from fuel molecules and converting it into ATP.

A mitochondrion has not one but two membranes. The outer membrane is smooth and studded with porins, protein channels that allow ions and small molecules to pass freely between the cytoplasm and the intermembrane space. This makes the intermembrane space chemically similar to the cytoplasm in many respects. The inner membrane is structurally very different: it is folded repeatedly into deep protrusions called cristae, it is largely impermeable (almost nothing crosses it without a specific transporter), and it is densely packed with the protein complexes of the electron transport chain and ATP synthase. The folding dramatically increases surface area — think of how much more paper fits in a crumpled ball versus a flat sheet — which means more ETC complexes and more ATP production per mitochondrion.

Inside the inner membrane is the matrix, a gel-like space containing a high concentration of enzymes, including those for the Krebs cycle. The matrix is also where mitochondrial DNA and ribosomes reside — a clue to the organelle's evolutionary origin. The endosymbiotic theory holds that mitochondria descend from free-living alpha-proteobacteria engulfed by an ancestral eukaryote roughly 1.5–2 billion years ago. Over time, most bacterial genes were transferred to the host nucleus, which is why modern mitochondria cannot live independently despite retaining traces of their prokaryotic past.

The four compartments — outer membrane, intermembrane space, inner membrane/cristae, matrix — each have distinct functional roles. Glycolysis happens in the cytoplasm (outside the mitochondrion entirely). The Krebs cycle runs in the matrix. The electron transport chain is embedded in the inner membrane. The intermembrane space is the reservoir where protons are pumped and held under pressure, ready to drive ATP synthase. Understanding this spatial organization is the key to understanding why the process works: it is essentially a biological battery where charge is separated across the inner membrane and then discharged through a molecular turbine.

