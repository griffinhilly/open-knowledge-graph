---
id: bacterial-flagella-and-chemotaxis
title: Bacterial Flagella, Motility, and Chemotaxis
domain: biology
course: microbiology
prerequisites:
- id: bacterial-cell-structure
  type: hard
- id: cell-signaling-intro
  type: soft
builds-toward:
- bacterial-virulence-and-disease-mechanisms
- microbial-ecology-biogeochemical-cycling
tags:
- motility
- flagella
- chemotaxis
- cell-signaling
stage: advanced
status: draft
---

# Bacterial Flagella, Motility, and Chemotaxis

## Core Idea
Bacterial flagella are rigid, helical protein filaments composed of flagellin that rotate at speeds up to 100,000 rpm, powered by a proton gradient across the cell membrane. This flagellar motor enables bacterial movement up to 60 μm/s. Chemotaxis allows bacteria to navigate chemical gradients by modulating rotation direction: tumbling (counterclockwise rotation) for random reorientation and smooth runs (clockwise) toward attractants.

## Explainer

From your study of bacterial cell structure, you know that bacteria possess a variety of surface appendages — pili for attachment, capsules for protection, and flagella for motility. The **bacterial flagellum** is one of the most remarkable molecular machines in biology. Unlike eukaryotic flagella (which bend and undulate), the bacterial flagellum is a rigid, corkscrew-shaped filament that literally rotates like a propeller. The filament is made of thousands of copies of the protein **flagellin**, assembled into a hollow helix that extends several cell lengths from the surface. At its base sits a rotary motor embedded in the cell envelope — a structure with a rotor, stator, and drive shaft, functionally analogous to an electric motor but only about 45 nanometers in diameter.

The energy source for this motor is the **proton motive force** — the same electrochemical gradient across the inner membrane that drives ATP synthesis. Protons flowing through the stator proteins (MotA/MotB) exert force on the rotor ring, spinning it at extraordinary speeds. In *E. coli*, the motor turns at roughly 300 revolutions per second; in some marine bacteria like *Vibrio*, it exceeds 1,000 rps. The hook, a flexible coupling between the motor and the filament, transmits this rotation to the rigid flagellar helix. When all flagella on a peritrichous bacterium (one with flagella distributed around the cell) rotate counterclockwise, they bundle together into a single coherent propeller that pushes the cell forward in a straight **run**. When one or more motors switch to clockwise rotation, the bundle flies apart and the cell **tumbles** — reorienting randomly before the next run.

**Chemotaxis** is the signaling system that biases this random walk toward favorable environments. The key insight is that bacteria are too small to sense a spatial gradient across their body length — instead, they sense changes in chemical concentration over time as they swim. Chemoreceptors (methyl-accepting chemotaxis proteins, or MCPs) in the cell membrane detect attractants like sugars and amino acids or repellents like toxins. When an attractant concentration is increasing (meaning the cell is swimming in the right direction), the signaling pathway suppresses tumbling, so the cell continues its run for longer. When the concentration decreases, tumbling frequency increases, causing random reorientation until the cell happens to head up the gradient again. The molecular mechanism involves the kinase **CheA**, which phosphorylates **CheY**; phospho-CheY binds the flagellar motor switch and promotes clockwise rotation (tumbling). Attractant binding inhibits CheA, reducing phospho-CheY, and the cell runs longer.

An elegant feature of this system is **adaptation** through receptor methylation. The enzyme CheR continuously adds methyl groups to the MCPs, while CheB (activated by CheA phosphorylation) removes them. This creates a feedback loop that resets the signaling baseline after a few seconds, regardless of the absolute concentration of attractant. The result is that bacteria respond to *changes* in concentration rather than absolute levels — they are always comparing "now" to "a moment ago." This temporal comparison strategy allows bacteria to navigate gradients efficiently despite their microscopic size, and it represents one of the simplest and best-understood examples of signal transduction and behavioral decision-making in any organism.
