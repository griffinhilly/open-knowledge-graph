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
- id: bacterial-flagella-and-chemotaxis
  type: soft
builds-toward:
- quorum-sensing
tags:
- chemotaxis
- signal-transduction
- two-component
stage: advanced
status: validated
---
# Bacterial Chemotaxis and Two-Component Signal Transduction

## Core Idea
Bacteria detect chemical gradients through transmembrane receptor proteins that activate a two-component regulatory system: a histidine kinase sensor (CheA) phosphorylates a response regulator (CheY), which diffuses to the flagellar motor to control rotation direction. Rapid adaptation allows sustained response to changing conditions.

## Questions

```yaml
- question: "An E. coli bacterium swims into a region with uniformly very high attractant concentration and remains there. After the adaptation mechanism has fully reset, what happens to the bacterium's tumbling frequency?"
  type: multiple-choice
  options:
    - "Tumbling frequency remains permanently suppressed because the high attractant concentration continuously inhibits CheA"
    - "Tumbling frequency returns to its pre-stimulus baseline, because methylation has restored CheA activity despite the high attractant"
    - "Tumbling frequency increases above baseline because high attractant saturates the receptors and disrupts normal signaling"
    - "Tumbling frequency stays low only if the bacterium continues to move — once it stops, adaptation occurs"
  answer: 1
  explanation: "This is the key test of whether a student understands adaptation. The bacterium senses the *gradient* (rate of change in concentration), not the absolute concentration. When it enters high attractant, tumbling suppresses. But then CheR continues methylating the MCPs, gradually restoring CheA activity to baseline — and with it, the normal tumbling frequency. After full adaptation, the bacterium behaves exactly as if it were in the original low-attractant environment: it has 'forgotten' the new baseline. Option A (the most tempting wrong answer) confuses maintained inhibition with adaptation — it would predict bacteria can never tumble in high attractant, which would trap them in place rather than allowing continued gradient-following."

- question: "In the E. coli chemotaxis system, what is the direct effect of phosphorylated CheY (CheY-P) on flagellar rotation?"
  type: multiple-choice
  options:
    - "CheY-P binds the flagellar motor switch complex and promotes counterclockwise rotation, extending runs"
    - "CheY-P inhibits CheA autophosphorylation, creating a negative feedback loop that prevents over-tumbling"
    - "CheY-P diffuses to the flagellar motor, binds the switch complex, and promotes clockwise rotation, causing tumbling"
    - "CheY-P activates CheR to add methyl groups to the MCPs, resetting receptor sensitivity"
  answer: 2
  explanation: "CheY-P is the signal that connects receptor activation to flagellar behavior. When CheA is active (no attractant bound), it phosphorylates CheY; CheY-P diffuses to the flagellar motor switch and promotes clockwise (CW) rotation, causing the flagella to fly apart and the cell to tumble. When attractant binds and inhibits CheA, CheY-P levels drop, and the motor defaults to counterclockwise (CCW) rotation — the run state. The direction of the causal chain is: attractant → inhibit CheA → less CheY-P → CCW rotation → run. Option A reverses the rotational direction. Option D confuses CheY with CheB (which IS activated by phosphorylation and DOES regulate methylation, but as CheB, not CheY)."

- question: "Bacteria navigate chemical gradients by sensing the rate of change (gradient) in attractant concentration rather than its absolute value."
  type: true-false
  answer: true
  explanation: "This is the core insight of bacterial chemotaxis. If bacteria sensed absolute concentration, they would stop tumbling as soon as they entered a favorable zone and would be unable to detect further improvements. Instead, the methylation-based adaptation system allows the bacterium to continuously reset its 'baseline' to the current concentration, so it always compares what it senses now to what it sensed a moment ago. A run is extended when concentration is increasing (getting better); tumbling resumes when concentration plateaus or decreases. This temporal comparison mechanism works over a concentration range spanning five orders of magnitude — far greater than any system based on absolute concentration would achieve."

- question: "Attractant binding to chemoreceptors directly activates CheA, which then phosphorylates CheY to promote running behavior."
  type: true-false
  answer: false
  explanation: "The logic is inverted. In the *absence* of attractant, CheA is constitutively active, autophosphorylates, and transfers phosphate to CheY — CheY-P promotes clockwise rotation and tumbling. When attractant binds the MCP receptor, a conformational change *inhibits* CheA, reducing CheY-P levels and allowing the motor to default to counterclockwise rotation (running). So attractant → inhibit CheA → less CheY-P → run. This counterintuitive arrangement (the default state is tumbling, not running) is important: it means the system is optimally sensitive to improvements from a baseline of uncertainty, rather than requiring an active 'start moving' signal."

- question: "How does the methylation-based adaptation mechanism allow bacteria to detect chemical gradients over a concentration range spanning five orders of magnitude?"
  type: short-answer
  answer: "The methylation system acts as a continuously adjustable gain control. CheR constantly adds methyl groups to the MCPs, which gradually restores CheA activity regardless of attractant concentration. CheB (activated by CheA phosphorylation) removes methyl groups. In equilibrium at any given concentration, methylation level reflects the current background — the receptor is effectively 'zeroed out' to the ambient concentration. When concentration suddenly increases (attractant binds), CheA is inhibited, CheY-P drops, and the cell runs. As methyl groups accumulate (CheB is now less active), CheA activity restores and tumbling resumes at the new baseline. Because the reset mechanism is concentration-independent, the system can operate equally well whether the background concentration is 10 nM or 1 mM — it always senses changes relative to the current baseline."
  explanation: "The adaptation mechanism transforms what could only be an absolute-concentration detector into a gradient detector. This is analogous to how the eye adapts to bright or dim light: dark adaptation and light adaptation allow photoreceptors to operate over a ~12-log range of light intensities by continuously adjusting their gain. Chemotaxis achieves the same trick through receptor methylation, and the resulting 5-order-of-magnitude dynamic range is far greater than any simple receptor-ligand system could provide. This is why chemotaxis is described as a nearly perfect sensory system and a model for understanding sensory adaptation in all of biology."
```

## Explainer

You already know that bacterial flagella can rotate in two directions — counterclockwise (bundling the flagella for smooth swimming, called a "run") and clockwise (causing the flagella to fly apart, producing a random "tumble"). In the absence of any chemical signal, bacteria alternate between runs and tumbles randomly, executing a three-dimensional random walk. **Chemotaxis** is the system that biases this random walk, extending runs when the bacterium is moving toward attractants (like sugars or amino acids) and increasing tumbles when it is moving toward repellents. The result is net movement up a favorable gradient — not by steering like a car, but by suppressing random direction changes when things are getting better.

The molecular machinery behind this behavior is a **two-component signal transduction system**, one of the most widespread signaling architectures in prokaryotes. The first component is a **histidine kinase sensor** called **CheA**, which is bound to transmembrane chemoreceptors (methyl-accepting chemotaxis proteins, or MCPs). When no attractant is bound to the receptor, CheA is active and autophosphorylates on a conserved histidine residue. It then transfers this phosphate group to the second component, the **response regulator CheY**. Phosphorylated CheY (CheY-P) diffuses through the cytoplasm to the flagellar motor, where it binds the switch complex and promotes clockwise rotation — causing a tumble. When attractant molecules bind to the MCPs, a conformational change is transmitted through the receptor to inhibit CheA, reducing CheY-P levels and allowing the motor to default to counterclockwise rotation — extending the run.

What makes chemotaxis remarkably sophisticated is its **adaptation** mechanism. If a bacterium simply responded to absolute concentrations of attractant, it would stop tumbling as soon as it entered a favorable zone and lose the ability to detect further improvements. Instead, the system resets itself through **methylation**. The enzyme **CheR** continuously adds methyl groups to the MCPs, while **CheB** (activated by phosphorylation from CheA) removes them. When attractant binds and inhibits CheA, CheB becomes less active, allowing methyl groups to accumulate on the receptor. This methylation gradually restores CheA activity to its baseline level, resetting the system. The bacterium is now adapted to the current concentration and can detect further changes — it senses the gradient, not the absolute concentration. This elegant feedback loop allows bacteria to navigate chemical gradients over a concentration range spanning five orders of magnitude, making chemotaxis one of the best-understood examples of signal transduction and sensory adaptation in all of biology.
