---
id: absolute-refractory-period
title: 'Absolute and Relative Refractory Periods: Neuronal Timing Constraints'
domain: biology
course: neuroscience
prerequisites:
- id: voltage-gated-sodium-channels
  type: hard
- id: action-potential-repolarization
  type: hard
tags:
- action-potential
- refractoriness
- firing-frequency
stage: advanced
status: draft
---

# Absolute and Relative Refractory Periods: Neuronal Timing Constraints

## Core Idea
The absolute refractory period (1–2 ms in mammalian neurons) is when no new action potential can be initiated because Na+ channels are inactivated. The relative refractory period follows, when stronger-than-normal stimuli can trigger spikes because K+ conductance is elevated and the membrane is hyperpolarized. These refractory periods set an upper limit on spike frequency and prevent backward propagation.

## Explainer

You already understand how voltage-gated sodium channels drive the rising phase of an action potential and how repolarization restores the membrane to its resting state. Refractory periods are a direct consequence of the molecular states these channels pass through — and they impose fundamental timing constraints on everything neurons can do.

Recall that voltage-gated Na+ channels exist in three conformational states: **closed** (resting, ready to open), **open** (conducting Na+ inward), and **inactivated** (blocked by the inactivation gate, unable to open regardless of voltage). During the peak and early falling phase of an action potential, nearly all Na+ channels in that patch of membrane are inactivated. This is the **absolute refractory period** — typically lasting 1–2 milliseconds in mammalian neurons. No matter how strong a stimulus you apply during this window, you cannot trigger another action potential because the channels physically cannot reopen. The inactivation gate, a molecular "ball and chain" structure on the channel's intracellular side, is plugged into the pore and must be removed before the channel can return to its closed-but-ready state.

As repolarization continues and the membrane approaches or overshoots resting potential (due to sustained K+ efflux), Na+ channels progressively recover from inactivation — transitioning back to the closed state. During this transitional window, called the **relative refractory period**, some fraction of Na+ channels are available again, but the membrane is hyperpolarized below its normal resting potential because voltage-gated K+ channels are still open. A stimulus during this period *can* trigger an action potential, but it must be stronger than normal to overcome the extra K+ conductance pulling the membrane negative. The resulting action potential may also be slightly smaller in amplitude because fewer Na+ channels are available.

These refractory periods have three crucial functional consequences. First, they set a **maximum firing rate** — if the absolute refractory period is 1 ms, the theoretical ceiling is about 1,000 action potentials per second, though most neurons fire well below this. Second, they ensure **unidirectional propagation**: once an action potential has passed a point on the axon, that region is refractory and cannot be re-excited by the depolarization spreading backward from the advancing wavefront. The spike can only move forward into resting membrane. Third, the relative refractory period introduces **frequency coding** — a neuron receiving a sustained, strong input will fire at high frequency because each stimulus easily exceeds the elevated threshold, while a weaker input produces lower-frequency firing because it fails during early parts of the relative refractory period. This is how stimulus intensity gets translated into spike rate, the basic language of neural coding.
