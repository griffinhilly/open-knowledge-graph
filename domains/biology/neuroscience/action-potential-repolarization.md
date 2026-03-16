---
id: action-potential-repolarization
title: Action Potential Repolarization and Undershoot
domain: biology
course: neuroscience
prerequisites:
- id: action-potential-initiation
  type: hard
- id: voltage-gated-potassium-channels
  type: hard
builds-toward:
- voltage-clamp-recording
- absolute-refractory-period
tags:
- action-potential
- repolarization
- temporal-dynamics
stage: advanced
status: draft
---

# Action Potential Repolarization and Undershoot

## Core Idea
After reaching peak depolarization, the action potential repolarizes as voltage-gated Na+ channels inactivate while K+ channels (which activated more slowly) reach peak conductance, driving outward K+ current. The delayed peak of K+ conductance often causes undershoot—hyperpolarization beyond resting potential—before the membrane returns to baseline.

## Explainer

You already understand how an action potential begins: depolarization opens voltage-gated Na+ channels, Na+ rushes in, and the membrane potential shoots toward +30 to +40 mV. But what brings the membrane back down? The answer lies in the different timing of two channel populations you have studied — and understanding this timing mismatch is the key to the entire repolarization phase.

**Voltage-gated Na+ channels** open fast but also **inactivate** fast. Within about a millisecond of opening, a ball-and-chain inactivation gate swings into the channel pore, blocking further Na+ influx even though the channel's activation gate is still open. This is not the same as closing — inactivation is a distinct conformational state that cannot be reversed until the membrane repolarizes. So at the peak of the action potential, Na+ entry has already been shut off by inactivation. Meanwhile, **voltage-gated K+ channels** have been responding to the same depolarization, but they activate much more slowly. They are just reaching their peak open probability as the Na+ channels are inactivating. This temporal offset — fast Na+ activation followed by slow K+ activation — is the fundamental mechanism of repolarization.

With Na+ channels inactivated and K+ channels now wide open, the dominant current shifts to outward K+ flow. Potassium ions leave the cell, driven by both the electrical gradient (the interior is still positive) and the concentration gradient (K+ is more concentrated inside). This outward current rapidly pulls the membrane potential back toward the K+ equilibrium potential (around −80 mV). Because K+ conductance peaks *after* the membrane has already started falling from +30 mV, the K+ channels are maximally open at a time when the membrane potential is passing through resting potential. The result is **undershoot** (also called **afterhyperpolarization**): the membrane transiently dips below resting potential, sometimes reaching −80 to −90 mV, before K+ channels finally close and the membrane drifts back to its resting value near −65 to −70 mV.

The undershoot is not a malfunction — it has functional significance. During the undershoot, the membrane is farther from threshold than at rest, making it harder to fire another action potential. This contributes to the **relative refractory period**, during which a stronger-than-normal stimulus is needed to trigger firing. Combined with the absolute refractory period (when Na+ channels are still inactivated and firing is impossible), the undershoot helps enforce unidirectional propagation of action potentials along the axon and sets an upper limit on firing frequency. Think of it as the neuron's built-in cooldown: fast Na+ channels create the spike, slow K+ channels clean it up, and the timing gap between them shapes everything from signal direction to maximum firing rate.
