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
status: validated
---

# Conduction in Unmyelinated Axons

## Core Idea
Action potentials propagate continuously along entire membrane. Depolarized region passively depolarizes adjacent regions through local current, triggering new action potentials. Slow (~1 m/s), depends on diameter.

## Questions

```yaml
- question: "An action potential is actively propagating down an unmyelinated axon. Which best describes how the adjacent (forward) membrane becomes depolarized?"
  type: multiple-choice
  options:
    - "Voltage-gated sodium channels in the adjacent region open spontaneously after a brief diffusion-based delay"
    - "Neurotransmitters released by the depolarized region diffuse forward and activate receptors on the adjacent membrane"
    - "Positive ions flow through the cytoplasm from the depolarized region toward the more negative adjacent region, bringing it to threshold"
    - "The action potential travels as an electromagnetic wave along the outer axon surface"
  answer: 2
  explanation: "Propagation in unmyelinated axons works through local current (electrotonic spread). The depolarized patch becomes strongly positive inside, creating a voltage gradient with the adjacent resting membrane. Ions flow passively through the cytoplasm from positive to negative, depolarizing the adjacent patch to threshold and triggering a fresh action potential there. Neurotransmitters (option B) are released at synapses, not along the axon membrane. There is no electromagnetic wave mechanism (option D)."

- question: "Why does increasing the diameter of an unmyelinated axon increase its conduction velocity?"
  type: multiple-choice
  options:
    - "Larger axons contain more voltage-gated sodium channels per unit length, enabling faster depolarization"
    - "Larger axons have lower internal (axial) resistance, so local current spreads farther before decaying below threshold"
    - "Larger axons have proportionally less membrane surface area per unit length, reducing current leakage"
    - "Larger axons have lower membrane capacitance, so they require less charge to reach threshold"
  answer: 1
  explanation: "The rate-limiting step in unmyelinated conduction is how far local current can spread before decaying below threshold. A wider axon has more cytoplasm in cross-section, lowering internal resistance: ions flow more easily down the length of the axon, and the current reaches farther before falling below threshold. This is why the squid giant axon (~1 mm diameter) achieves ~25 m/s — not through more channels or less leakage, but through reduced axial resistance. Option C is actually reversed: larger diameter increases membrane surface area, which increases total leakage."

- question: "After generating an action potential, the same patch of membrane can immediately re-fire to propagate the signal back toward the cell body, potentially causing the signal to reverse direction."
  type: true-false
  answer: false
  explanation: "After an action potential, voltage-gated sodium channels enter a refractory period (inactivated state) and cannot open again immediately. This ensures unidirectional propagation: the region that just fired is temporarily inexcitable, so the local current from the advancing action potential can only trigger a new AP in the forward (unexcited) direction. Without the refractory period, action potentials could propagate bidirectionally and re-enter previously fired regions. The refractory period is the mechanism that gives neural signals their directionality."

- question: "Conduction velocity in unmyelinated axons is limited partly because local current decays along the leaky axon membrane before reaching the next patch of excitable membrane."
  type: true-false
  answer: true
  explanation: "Axon membrane is not a perfect insulator — ion channels and other pathways allow current to leak outward across the membrane rather than flowing longitudinally toward the next excitable patch. This decay (described by the axon's length constant λ) means each local current only depolarizes a limited distance before falling below threshold. The action potential must be fully regenerated at every point, and each regeneration depends on the local current from the immediately preceding point. Leakier membranes have shorter length constants and slower conduction."

- question: "Why is conduction in unmyelinated axons described as 'continuous' propagation, and how does this differ mechanistically from saltatory conduction in myelinated axons?"
  type: short-answer
  answer: "In unmyelinated axons, the action potential must be fully regenerated at every point along the membrane — local current decays quickly due to membrane leakage, so the signal creeps forward in tiny increments. In myelinated axons, myelin insulates the internodal membrane and prevents ion leakage, allowing local current to jump the full distance to the next node of Ranvier (saltatory conduction), where the AP is regenerated. The signal skips rather than crawls."
  explanation: "The speed difference is dramatic: unmyelinated C fibers conduct at 0.5–2 m/s; large myelinated Aα fibers reach 70–120 m/s. Saltatory conduction is also more energy-efficient: only the nodes need to pump ions back after each AP, rather than the entire membrane. The evolutionary advantage of myelin was achieving high conduction velocity without maintaining enormous-diameter axons — the squid's 1 mm giant axon achieves ~25 m/s, while a myelinated fiber of ~10 μm diameter (100× thinner) can match or exceed this. Unmyelinated conduction remains functional in C fibers (slow pain, temperature) and autonomic fibers throughout the human body."
```

## Explainer

You already know that an action potential is an all-or-nothing electrical event: voltage-gated sodium channels open, the membrane depolarizes rapidly, and then potassium channels restore the resting potential. In a myelinated axon, this event jumps between nodes, but in an **unmyelinated axon** — the ancestral and simpler case — propagation works differently. The action potential must regenerate at every point along the membrane, and understanding why reveals both the elegance and the limitations of basic neural signaling.

When a patch of membrane fires an action potential, sodium ions rush inward, making the inside of that region strongly positive. This creates a voltage difference between the depolarized patch and the still-resting membrane immediately ahead of it. Ions flow passively through the cytoplasm from the positive region toward the negative region — this is called **local current** (or electrotonic spread). The local current depolarizes the adjacent membrane enough to reach threshold, which opens the voltage-gated sodium channels there, triggering a fresh action potential. The process then repeats: each new action potential generates local current that depolarizes the next patch, creating a continuous wave of depolarization traveling down the axon.

Two features of this mechanism explain why conduction in unmyelinated axons is slow. First, the action potential must be fully regenerated at every point — there is no shortcut or skipping. Second, **local current decays with distance** because the axon membrane is leaky; ions escape across the membrane rather than flowing efficiently down the length of the axon. This means each local current only reaches a short distance ahead before it falls below threshold. The signal creeps forward in tiny increments. Typical conduction velocities in thin unmyelinated axons are around 0.5–2 m/s, compared to 100+ m/s in large myelinated fibers.

One way organisms compensate is by increasing **axon diameter**. A wider axon has lower internal resistance (more cytoplasm for ions to flow through), so local current spreads farther before decaying. The giant axon of the squid, roughly 1 mm in diameter, achieves about 25 m/s — fast for an unmyelinated fiber, but still far slower than vertebrate myelinated axons of much smaller diameter. This is why myelination was such a powerful evolutionary innovation: it achieves the same speed boost without the metabolic cost of maintaining enormous axons. But the unmyelinated mechanism remains fundamental — it is the baseline process that saltatory conduction optimizes, and it still operates in many small-diameter sensory and autonomic fibers throughout the human body, including C fibers that carry dull pain and temperature information.
