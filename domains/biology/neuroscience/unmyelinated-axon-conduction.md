---
id: unmyelinated-axon-conduction
title: Conduction in Unmyelinated Axons
domain: biology
course: neuroscience
prerequisites:
- id: action-potential-depolarization-repolarization
  type: hard
- id: neuron-structure-and-function
  type: hard
builds-toward:
- myelinated-axon-saltatory-conduction
tags:
- conduction-velocity
- propagation
stage: advanced
status: draft
---

# Conduction in Unmyelinated Axons

## Core Idea
Action potentials propagate continuously along entire membrane. Depolarized region passively depolarizes adjacent regions through local current, triggering new action potentials. Slow (~1 m/s), depends on diameter.

## Explainer

You already know that an action potential is an all-or-nothing electrical event: voltage-gated sodium channels open, the membrane depolarizes rapidly, and then potassium channels restore the resting potential. In a myelinated axon, this event jumps between nodes, but in an **unmyelinated axon** — the ancestral and simpler case — propagation works differently. The action potential must regenerate at every point along the membrane, and understanding why reveals both the elegance and the limitations of basic neural signaling.

When a patch of membrane fires an action potential, sodium ions rush inward, making the inside of that region strongly positive. This creates a voltage difference between the depolarized patch and the still-resting membrane immediately ahead of it. Ions flow passively through the cytoplasm from the positive region toward the negative region — this is called **local current** (or electrotonic spread). The local current depolarizes the adjacent membrane enough to reach threshold, which opens the voltage-gated sodium channels there, triggering a fresh action potential. The process then repeats: each new action potential generates local current that depolarizes the next patch, creating a continuous wave of depolarization traveling down the axon.

Two features of this mechanism explain why conduction in unmyelinated axons is slow. First, the action potential must be fully regenerated at every point — there is no shortcut or skipping. Second, **local current decays with distance** because the axon membrane is leaky; ions escape across the membrane rather than flowing efficiently down the length of the axon. This means each local current only reaches a short distance ahead before it falls below threshold. The signal creeps forward in tiny increments. Typical conduction velocities in thin unmyelinated axons are around 0.5–2 m/s, compared to 100+ m/s in large myelinated fibers.

One way organisms compensate is by increasing **axon diameter**. A wider axon has lower internal resistance (more cytoplasm for ions to flow through), so local current spreads farther before decaying. The giant axon of the squid, roughly 1 mm in diameter, achieves about 25 m/s — fast for an unmyelinated fiber, but still far slower than vertebrate myelinated axons of much smaller diameter. This is why myelination was such a powerful evolutionary innovation: it achieves the same speed boost without the metabolic cost of maintaining enormous axons. But the unmyelinated mechanism remains fundamental — it is the baseline process that saltatory conduction optimizes, and it still operates in many small-diameter sensory and autonomic fibers throughout the human body, including C fibers that carry dull pain and temperature information.
