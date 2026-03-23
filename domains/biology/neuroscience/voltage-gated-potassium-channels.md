---
id: voltage-gated-potassium-channels
title: Voltage-Gated Potassium Channels
domain: biology
course: neuroscience
prerequisites:
- id: resting-membrane-potential
  type: hard
- id: ligand-gated-ion-channels
  type: soft
builds-toward:
- action-potential-depolarization-repolarization
tags:
- ion-channels
- repolarization
stage: expert
status: validated
---

# Voltage-Gated Potassium Channels

## Core Idea
Open more slowly than Na+ channels during depolarization, allowing K+ efflux that repolarizes membrane. Lack fast inactivation, determining action potential duration.

## Questions

```yaml
- question: "A toxin selectively and completely blocks voltage-gated K⁺ channels without affecting voltage-gated Na⁺ channels. What effect would this have on neuronal action potentials?"
  type: multiple-choice
  options:
    - "Depolarization would be blocked because K⁺ influx normally drives the rising phase of the action potential"
    - "Action potentials would be broader and prolonged, with repolarization severely impaired or absent"
    - "The resting membrane potential would immediately become more positive due to loss of K⁺ permeability"
    - "Na⁺ channels would fail to open because they require K⁺ channel co-activation"
  answer: 1
  explanation: "Voltage-gated K⁺ channels are responsible for repolarization — their opening drives K⁺ out of the cell, rapidly restoring the negative membrane potential. If they are blocked, the depolarization caused by Na⁺ influx cannot be reversed efficiently, causing the action potential to broaden dramatically or plateau. Option A reverses the ionic flows: Na⁺ (not K⁺) drives depolarization. Option C is wrong because voltage-gated K⁺ channels are largely closed at rest — resting potential is set by constitutive leak channels, not voltage-gated ones."

- question: "What is the primary reason voltage-gated K⁺ channels cause afterhyperpolarization — a brief dip in membrane voltage below the resting potential?"
  type: multiple-choice
  options:
    - "They lack fast inactivation, so they continue conducting K⁺ outward even after the membrane passes through the resting potential, pulling voltage below rest"
    - "They have a fast inactivation gate that closes precisely at -70 mV, causing a brief overshoot below rest"
    - "K⁺ rushes inward at negative voltages, hyperpolarizing the cell below its equilibrium potential"
    - "Na⁺ channels reopen at voltages below -70 mV, producing an inward current that causes undershoot"
  answer: 0
  explanation: "Voltage-gated K⁺ channels lack the fast inactivation gate that Na⁺ channels possess. They stay open as long as the membrane is depolarized. As repolarization proceeds and the membrane voltage drops back through -70 mV toward the K⁺ equilibrium potential (~-90 mV), the channels are still open and still conducting K⁺ outward, continuing to pull the voltage more negative. Only once the membrane is sufficiently negative do the channels slowly close, allowing the resting potential to be re-established. Option B is wrong because K⁺ channels lack fast inactivation entirely — this is a defining feature distinguishing them from Na⁺ channels."

- question: "The delay in voltage-gated K⁺ channel opening relative to Na⁺ channel opening is essential for the action potential to reach its positive peak before repolarization begins."
  type: true-false
  answer: true
  explanation: "If K⁺ channels opened as rapidly as Na⁺ channels, K⁺ efflux would immediately counteract Na⁺ influx, preventing the membrane from depolarizing to its characteristic peak near +30 mV. The delayed opening means that the Na⁺ channels have time to drive the membrane strongly positive before K⁺ channels begin their repolarizing current. This timing is not accidental — it results from the slower conformational rearrangement required to open K⁺ channel pores."

- question: "Like voltage-gated Na⁺ channels, voltage-gated K⁺ channels possess a fast inactivation gate that closes the channel within milliseconds of opening, regardless of membrane voltage."
  type: true-false
  answer: false
  explanation: "This is the key structural difference between the two channel types. Voltage-gated Na⁺ channels have a fast inactivation mechanism (the 'ball and chain' inactivation gate) that closes the channel within ~1 ms of opening, independent of whether the membrane is still depolarized. Voltage-gated K⁺ channels (delayed rectifiers) lack this fast inactivation gate — they remain open as long as the membrane stays depolarized. This difference is what causes afterhyperpolarization and makes K⁺ channels the primary determinant of action potential duration."

- question: "Why do voltage-gated K⁺ channels cause afterhyperpolarization, and what does this reveal about their gating mechanism compared to voltage-gated Na⁺ channels?"
  type: short-answer
  answer: "Afterhyperpolarization occurs because voltage-gated K⁺ channels lack fast inactivation. Na⁺ channels have an inactivation gate that closes the channel within ~1 ms of opening regardless of membrane voltage, automatically terminating Na⁺ influx. K⁺ channels have no equivalent mechanism — they stay open as long as the membrane remains depolarized. As repolarization proceeds and the voltage passes through -70 mV, K⁺ channels are still open and still driving K⁺ outward toward the ~-90 mV equilibrium potential, pulling the voltage below rest. Only when the membrane becomes sufficiently negative do the channels finally close, allowing leak channels to restore the resting potential. The afterhyperpolarization is therefore a direct consequence of K⁺ channels' inability to self-terminate — their open duration is set by the voltage, not by an intrinsic timer."
  explanation: "This question tests whether students understand that the gating properties of K⁺ channels — specifically the absence of fast inactivation — have direct functional consequences for action potential shape. Students who know only that 'K⁺ channels repolarize the membrane' without understanding this distinction cannot explain why the membrane briefly overshoots below rest."
```

## Explainer

You already know that the resting membrane potential sits near −70 mV because potassium leak channels hold the membrane close to the K⁺ equilibrium potential. During an action potential, voltage-gated sodium channels snap open first, flooding the cell with Na⁺ and driving the membrane toward +30 mV. But something has to bring the membrane back down. That job belongs to **voltage-gated potassium channels** (often called **delayed rectifier channels**), and their defining feature is their timing: they respond to the same depolarization that opens Na⁺ channels, but they open with a measurable delay — typically a fraction of a millisecond later. This delay is what makes the action potential a spike rather than a sustained plateau.

The molecular basis of this delay lies in the channel's **activation gate**. Like voltage-gated Na⁺ channels, K⁺ channels have voltage-sensing domains that respond to depolarization by undergoing conformational changes. But the structural rearrangement required to open the K⁺ channel pore takes longer. By the time K⁺ channels reach their fully open state, Na⁺ channels are already inactivating through their fast inactivation gate. The result is a handoff: Na⁺ influx drives depolarization upward, and then K⁺ efflux drives **repolarization** back toward the resting potential. Because the electrochemical gradient for K⁺ points outward (high K⁺ inside, low outside, and the membrane is now positive), opening these channels produces a large outward K⁺ current that rapidly pulls the voltage negative again.

A critical difference from Na⁺ channels is that voltage-gated K⁺ channels **lack a fast inactivation gate**. Na⁺ channels have a built-in timer — the inactivation ball that swings into the pore within a millisecond of opening, shutting the channel regardless of whether the membrane is still depolarized. K⁺ channels stay open as long as the membrane remains depolarized. This means they keep conducting K⁺ outward even as the membrane passes through the resting potential, often driving the voltage briefly more negative than rest — a phenomenon called **afterhyperpolarization** or undershoot. The membrane only returns to resting potential once the K⁺ channels close in response to the now-negative voltage and the leak channels re-establish equilibrium.

This absence of fast inactivation has a direct consequence for action potential duration. In neurons with more delayed rectifier channels or channels that open faster, the action potential is briefer because repolarization begins sooner and proceeds more forcefully. In cardiac muscle, by contrast, a different set of K⁺ channel subtypes opens much more slowly, which is one reason the cardiac action potential lasts hundreds of milliseconds instead of one or two. The density, subtype distribution, and kinetics of voltage-gated K⁺ channels are therefore a primary determinant of how long any excitable cell stays depolarized — and by extension, how frequently it can fire.
