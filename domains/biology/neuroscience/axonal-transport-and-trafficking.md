---
id: axonal-transport-and-trafficking
title: Axonal Transport and Vesicular Trafficking
domain: biology
course: neuroscience
prerequisites:
- id: neuron-structure-and-function
  type: hard
- id: protein-targeting-and-subcellular-localization
  type: soft
builds-toward:
- synaptic-transmission
- synaptogenesis-and-circuit-development
tags:
- transport
- kinesin
- dynein
- vesicles
stage: advanced
status: draft
---

# Axonal Transport and Vesicular Trafficking

## Core Idea
Neurons transport proteins, lipids, and organelles across distances up to 1 meter using molecular motor proteins (kinesins and dynein) along microtubule tracks. Fast anterograde transport moves vesicles outward at ~100 µm/s; fast retrograde transport returns materials at ~200 µm/s. Transport machinery is activity-dependent and disrupted in neurodegenerative disease.

## How It's Best Learned
Use live-cell microscopy to track labeled organelles. Model transport velocity using motor protein parameters.

## Common Misconceptions
All axonal proteins are synthesized at soma and transported distally. Local protein synthesis occurs throughout axons.

## Explainer

From your study of neuron structure, you know that neurons are extraordinarily elongated cells — a motor neuron's axon can stretch from the spinal cord to your toes, a distance of roughly one meter. Yet the cell body, where most protein synthesis occurs, is only about 20 micrometers across. This creates a logistical problem unlike anything other cells face: how do you deliver freshly made proteins, vesicles full of neurotransmitter, and mitochondria to a synapse that is fifty thousand cell-body-diameters away? The answer is **axonal transport**, a system of molecular motor proteins running along cytoskeletal tracks.

The tracks are **microtubules** — the same polarized polymers you encountered in cell biology, but with a critical organizational feature in neurons. In axons, microtubules are uniformly oriented with their plus-ends pointing away from the cell body toward the synapse. This polarity creates a one-way street system. **Kinesin** motor proteins walk toward the plus-end (away from the soma), carrying cargo in the **anterograde** direction — outward to the synapse. This is how synaptic vesicle precursors, membrane proteins, and mitochondria reach the nerve terminal. **Dynein** motors walk toward the minus-end, carrying cargo in the **retrograde** direction — back toward the cell body. Retrograde transport returns used vesicle components for recycling, carries signaling endosomes that inform the nucleus about conditions at the synapse, and unfortunately also provides a highway for pathogens like rabies virus and herpes simplex to travel from the periphery to the nervous system.

Transport occurs at two distinct speeds. **Fast axonal transport** (up to 400 mm/day for anterograde, even faster for retrograde) moves membrane-bound organelles — synaptic vesicles, mitochondria, and endosomes. Each motor protein takes discrete 8-nanometer steps along the microtubule, hydrolyzing one ATP per step, with multiple motors cooperating to haul each cargo. **Slow axonal transport** (0.2–8 mm/day) moves cytoskeletal components and soluble proteins. Despite the name, slow transport is not driven by a different, slower motor — it results from the same kinesin and dynein motors moving cargo in frequent start-stop bursts with long pauses, so the average velocity is much lower even though instantaneous movement speed is similar.

When axonal transport fails, the consequences are severe and illuminate why this system matters clinically. In **amyotrophic lateral sclerosis** (ALS), mutations in dynein and transport-associated proteins contribute to motor neuron degeneration. In **Alzheimer's disease**, hyperphosphorylated tau protein dissociates from microtubules, destabilizing the tracks themselves and causing transport jams that starve synapses of essential supplies. Hereditary spastic paraplegia, Charcot-Marie-Tooth disease, and Huntington's disease all involve transport disruption. The longest neurons are the most vulnerable, which is why these diseases often begin with weakness or sensory loss in the feet and hands — the terminals farthest from the cell body are the first to be cut off from supply.
