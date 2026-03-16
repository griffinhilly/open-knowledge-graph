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
stage: advanced
status: draft
---

# Voltage-Gated Potassium Channels

## Core Idea
Open more slowly than Na+ channels during depolarization, allowing K+ efflux that repolarizes membrane. Lack fast inactivation, determining action potential duration.

## Explainer

You already know that the resting membrane potential sits near −70 mV because potassium leak channels hold the membrane close to the K⁺ equilibrium potential. During an action potential, voltage-gated sodium channels snap open first, flooding the cell with Na⁺ and driving the membrane toward +30 mV. But something has to bring the membrane back down. That job belongs to **voltage-gated potassium channels** (often called **delayed rectifier channels**), and their defining feature is their timing: they respond to the same depolarization that opens Na⁺ channels, but they open with a measurable delay — typically a fraction of a millisecond later. This delay is what makes the action potential a spike rather than a sustained plateau.

The molecular basis of this delay lies in the channel's **activation gate**. Like voltage-gated Na⁺ channels, K⁺ channels have voltage-sensing domains that respond to depolarization by undergoing conformational changes. But the structural rearrangement required to open the K⁺ channel pore takes longer. By the time K⁺ channels reach their fully open state, Na⁺ channels are already inactivating through their fast inactivation gate. The result is a handoff: Na⁺ influx drives depolarization upward, and then K⁺ efflux drives **repolarization** back toward the resting potential. Because the electrochemical gradient for K⁺ points outward (high K⁺ inside, low outside, and the membrane is now positive), opening these channels produces a large outward K⁺ current that rapidly pulls the voltage negative again.

A critical difference from Na⁺ channels is that voltage-gated K⁺ channels **lack a fast inactivation gate**. Na⁺ channels have a built-in timer — the inactivation ball that swings into the pore within a millisecond of opening, shutting the channel regardless of whether the membrane is still depolarized. K⁺ channels stay open as long as the membrane remains depolarized. This means they keep conducting K⁺ outward even as the membrane passes through the resting potential, often driving the voltage briefly more negative than rest — a phenomenon called **afterhyperpolarization** or undershoot. The membrane only returns to resting potential once the K⁺ channels close in response to the now-negative voltage and the leak channels re-establish equilibrium.

This absence of fast inactivation has a direct consequence for action potential duration. In neurons with more delayed rectifier channels or channels that open faster, the action potential is briefer because repolarization begins sooner and proceeds more forcefully. In cardiac muscle, by contrast, a different set of K⁺ channel subtypes opens much more slowly, which is one reason the cardiac action potential lasts hundreds of milliseconds instead of one or two. The density, subtype distribution, and kinetics of voltage-gated K⁺ channels are therefore a primary determinant of how long any excitable cell stays depolarized — and by extension, how frequently it can fire.
