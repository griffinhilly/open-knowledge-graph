---
id: neuromodulation-presynaptic
title: Neuromodulation and Presynaptic Dynamics
domain: biology
course: neuroscience
prerequisites:
- id: short-term-plasticity-presynaptic
  type: hard
- id: gpcr-metabotropic-signaling
  type: soft
builds-toward:
- synaptic-computation
- network-filtering
tags:
- neuromodulation
- presynaptic
- facilitation
- depression
stage: advanced
status: draft
---

# Neuromodulation and Presynaptic Dynamics

## Core Idea
Neuromodulation involves changes in synaptic strength over milliseconds to minutes through presynaptic mechanisms. Paired-pulse facilitation (increased release with repeated stimulation) and depression (decreased release) depend on presynaptic calcium accumulation and autoreceptor activation. Different synapses exhibit distinct profiles that filter information.

## How It's Best Learned
Record paired-pulse responses at different intervals. Fit exponential time constants and simulate using Tsodyks-Markram model.

## Common Misconceptions
Short-term plasticity is malfunctioning—it's an information filter. All synapses have identical time constants—these vary widely across circuits.

## Explainer

From your study of short-term presynaptic plasticity and GPCR/metabotropic signaling, you know that synaptic strength is not fixed — it fluctuates on short timescales depending on recent activity, and that metabotropic receptors can modulate cellular function through second messenger cascades. **Neuromodulation and presynaptic dynamics** unify these ideas: the probability that a presynaptic terminal releases neurotransmitter changes from moment to moment based on the recent history of action potentials arriving at that terminal and on modulatory signals from other neurons.

The two most fundamental forms of short-term presynaptic plasticity are **paired-pulse facilitation** and **paired-pulse depression**. Imagine stimulating a presynaptic axon twice in rapid succession. In facilitation, the second response is *larger* than the first. The mechanism is residual calcium: after the first action potential, calcium ions that entered through voltage-gated calcium channels linger in the terminal for tens to hundreds of milliseconds. When the second action potential arrives before this residual calcium has been fully cleared, the total calcium concentration is higher, and more vesicles fuse with the membrane, releasing more neurotransmitter. In depression, the opposite occurs — the second response is *smaller*. Here, the first stimulus depletes the **readily releasable pool** of synaptic vesicles faster than they can be replenished, so fewer vesicles are available for the second release event.

Whether a given synapse shows facilitation or depression depends on its initial **release probability**. Synapses with low initial release probability (only a small fraction of available vesicles fuse per action potential) tend to facilitate — there is plenty of reserve vesicle capacity, so the calcium boost from rapid firing recruits additional vesicles. Synapses with high initial release probability tend to depress — they are already releasing near their maximum, so rapid firing exhausts the vesicle pool. This is not a defect but a **computational feature**. Facilitating synapses act as high-pass filters: they respond weakly to isolated spikes but strongly to bursts, effectively detecting sudden increases in presynaptic firing rate. Depressing synapses act as low-pass filters: they respond strongly to the onset of activity but attenuate sustained input, making them sensitive to changes rather than steady states.

Layered on top of this activity-dependent dynamics are modulatory influences from **neuromodulators** — substances like dopamine, norepinephrine, serotonin, and acetylcholine that act through presynaptic metabotropic receptors (GPCRs) to tune release probability up or down. Many presynaptic terminals also express **autoreceptors** — receptors for their own neurotransmitter that provide negative feedback. For example, presynaptic GABA_B autoreceptors on GABAergic terminals detect accumulating GABA in the synaptic cleft and reduce further release, preventing excessive inhibition. These modulatory inputs can shift a synapse's entire operating point: a neuromodulator that increases release probability converts a facilitating synapse into a depressing one, fundamentally changing how that synapse filters information. The result is that the same anatomical connection can process information differently depending on the animal's behavioral state — alert versus drowsy, stressed versus calm — because neuromodulatory tone reshapes the dynamics of every synapse it touches.
