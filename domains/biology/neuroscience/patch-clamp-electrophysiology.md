---
id: patch-clamp-electrophysiology
title: Patch Clamp Recording Technique
domain: biology
course: neuroscience
prerequisites:
- id: voltage-gated-sodium-channels
  type: hard
- id: voltage-gated-potassium-channels
  type: hard
builds-toward:
- ligand-gated-ion-channels
- receptor-kinetics
tags:
- patch-clamp
- single-channel
- whole-cell
stage: advanced
status: draft
---

# Patch Clamp Recording Technique

## Core Idea
Patch clamp uses a glass micropipette (1 µm tip) sealed to the cell membrane (gigaohm seal) to measure single-channel currents in the picoampere range. Configurations include cell-attached, whole-cell, inside-out, and outside-out patches. This technique enabled characterization of virtually every ion channel type.

## How It's Best Learned
Watch video demonstrations of seal-formation. Analyze single-channel traces for open/closed dwell times.

## Common Misconceptions
Patch clamp only records single channels. Whole-cell patch clamp measures total membrane current from all channels.

## Explainer

From your study of voltage-gated sodium and potassium channels, you understand that ion channels open and close in response to membrane voltage changes, producing the currents that underlie action potentials. But how were these channels actually characterized? How do we know their conductance, gating kinetics, and pharmacology? The answer is the **patch clamp technique**, developed by Erwin Neher and Bert Sakmann in the late 1970s (earning them the 1991 Nobel Prize), which made it possible to measure the electrical current flowing through individual ion channels in real time.

The basic setup involves pulling a glass micropipette to a very fine tip (about **1 micrometer** in diameter), filling it with an electrolyte solution, and pressing it gently against the surface of a living cell. By applying slight suction, the glass forms an extraordinarily tight seal with the cell membrane — a **gigaohm seal** (gigaseal), meaning the electrical resistance between the pipette interior and the bath solution exceeds 10⁹ ohms. This seal is critical because the currents flowing through a single ion channel are tiny — on the order of **picoamperes** (10⁻¹² A). Without the gigaseal's enormous resistance, these minuscule currents would leak around the pipette rim and be lost in background noise. The gigaseal essentially forces all current to flow either through the ion channels in the patch of membrane beneath the pipette or through the amplifier — nowhere else.

The technique's power comes from its multiple **configurations**, each suited to different experimental questions. In the **cell-attached** configuration, the pipette seals onto the intact cell, and you record from whatever channels happen to be in the small membrane patch under the tip — perfect for studying channels in their native cellular environment. To access the whole cell, you apply a brief pulse of suction or voltage that ruptures the membrane patch, creating the **whole-cell** configuration. Now the pipette interior is continuous with the cell's cytoplasm, and your amplifier measures the summed current from every channel in the entire cell membrane. This configuration is used to characterize the total sodium or potassium current during an action potential. Two additional configurations are obtained by pulling the pipette away from the cell after establishing a seal: pulling from cell-attached creates an **inside-out patch** (cytoplasmic face exposed to the bath), while pulling from whole-cell creates an **outside-out patch** (extracellular face exposed to the bath). Inside-out patches let you manipulate the intracellular environment — changing calcium concentration, adding second messengers — to study how cytoplasmic factors regulate channel gating. Outside-out patches let you apply drugs or neurotransmitters to the extracellular face with precise concentration control.

Single-channel recordings from patch clamp experiments revealed that ion channels are not rheostats — they do not pass graded amounts of current. Instead, individual channels switch abruptly between **open** and **closed** states, producing rectangular current pulses of uniform amplitude. The macroscopic currents recorded from whole cells (which appear smooth and graded) emerge from the summed activity of thousands of channels, each independently flickering open and closed with a certain probability. This stochastic gating behavior was a fundamental discovery that reshaped how neuroscientists think about electrical signaling: the "deterministic" action potential is actually the statistical average of thousands of probabilistic molecular events. Patch clamp remains the gold standard for studying ion channels and is essential for drug development — nearly every new cardiac, neurological, or anesthetic drug is screened for effects on ion channel currents using this technique.
