---
id: chemotaxis-signaling-phosphorylation
title: Bacterial Chemotaxis and Two-Component Signal Transduction
domain: biology
course: microbiology
prerequisites:
- id: flagellar-motor-rotation
  type: hard
- id: cell-signaling-receptor-pathways
  type: soft
builds-toward:
- quorum-sensing
tags:
- chemotaxis
- signal-transduction
- two-component
stage: formal-systems
status: draft
---

# Bacterial Chemotaxis and Two-Component Signal Transduction

## Core Idea
Bacteria detect chemical gradients through transmembrane receptor proteins that activate a two-component regulatory system: a histidine kinase sensor (CheA) phosphorylates a response regulator (CheY), which diffuses to the flagellar motor to control rotation direction. Rapid adaptation allows sustained response to changing conditions.

## Explainer

You already know that bacterial flagella can rotate in two directions — counterclockwise (bundling the flagella for smooth swimming, called a "run") and clockwise (causing the flagella to fly apart, producing a random "tumble"). In the absence of any chemical signal, bacteria alternate between runs and tumbles randomly, executing a three-dimensional random walk. **Chemotaxis** is the system that biases this random walk, extending runs when the bacterium is moving toward attractants (like sugars or amino acids) and increasing tumbles when it is moving toward repellents. The result is net movement up a favorable gradient — not by steering like a car, but by suppressing random direction changes when things are getting better.

The molecular machinery behind this behavior is a **two-component signal transduction system**, one of the most widespread signaling architectures in prokaryotes. The first component is a **histidine kinase sensor** called **CheA**, which is bound to transmembrane chemoreceptors (methyl-accepting chemotaxis proteins, or MCPs). When no attractant is bound to the receptor, CheA is active and autophosphorylates on a conserved histidine residue. It then transfers this phosphate group to the second component, the **response regulator CheY**. Phosphorylated CheY (CheY-P) diffuses through the cytoplasm to the flagellar motor, where it binds the switch complex and promotes clockwise rotation — causing a tumble. When attractant molecules bind to the MCPs, a conformational change is transmitted through the receptor to inhibit CheA, reducing CheY-P levels and allowing the motor to default to counterclockwise rotation — extending the run.

What makes chemotaxis remarkably sophisticated is its **adaptation** mechanism. If a bacterium simply responded to absolute concentrations of attractant, it would stop tumbling as soon as it entered a favorable zone and lose the ability to detect further improvements. Instead, the system resets itself through **methylation**. The enzyme **CheR** continuously adds methyl groups to the MCPs, while **CheB** (activated by phosphorylation from CheA) removes them. When attractant binds and inhibits CheA, CheB becomes less active, allowing methyl groups to accumulate on the receptor. This methylation gradually restores CheA activity to its baseline level, resetting the system. The bacterium is now adapted to the current concentration and can detect further changes — it senses the gradient, not the absolute concentration. This elegant feedback loop allows bacteria to navigate chemical gradients over a concentration range spanning five orders of magnitude, making chemotaxis one of the best-understood examples of signal transduction and sensory adaptation in all of biology.
