---
id: saltatory-conduction
title: 'Saltatory Conduction: Rapid Propagation in Myelinated Axons'
domain: biology
course: neuroscience
prerequisites:
- id: action-potential-repolarization
  type: hard
builds-toward:
- descending-motor-pathways
tags:
- action-potential-propagation
- myelin
- efficiency
stage: advanced
status: validated
---

# Saltatory Conduction: Rapid Propagation in Myelinated Axons

## Core Idea
Myelinated axons achieve conduction velocities 50–100 times faster than unmyelinated axons through saltatory conduction: action potentials regenerate at nodes of Ranvier where ion channels are clustered, while insulating myelin prevents current leakage along internodes. This arrangement provides both rapid signaling and energy efficiency.

## Questions

```yaml
- question: "A patient with multiple sclerosis experiences a relapse affecting the optic nerve, causing temporary vision loss. An MRI shows demyelinating plaques along optic nerve axons. What is the immediate electrophysiological consequence of losing myelin from these axons?"
  type: multiple-choice
  options:
    - "Voltage-gated sodium channels are destroyed at the nodes of Ranvier, preventing action potential generation"
    - "The action potential can no longer jump between nodes because the internodal membrane, now exposed, lacks sufficient ion channels to regenerate the signal, causing conduction block or severe slowing"
    - "The axon diameter shrinks, reducing cytoplasmic resistance and slowing conduction"
    - "Potassium channels in the myelinated segments open constitutively, hyperpolarizing the axon"
  answer: 1
  explanation: "Myelin enables saltatory conduction by ensuring that passive current from one node spreads through the insulated internode with minimal leakage, reaching the next node with enough charge to trigger a new action potential. When myelin is lost, the internodal membrane is exposed — but it lacks the high density of voltage-gated sodium channels found at nodes. The exposed membrane has high capacitance and low resistance, so passive current dissipates rapidly and cannot reliably depolarize the next node to threshold. The result is conduction block (no signal propagates) or dramatic slowing, directly causing the neurological symptoms MS patients experience. The nodes themselves are initially intact; the problem is the inability to transmit current efficiently between them."

- question: "How does myelin increase the speed of action potential propagation compared to an unmyelinated axon of the same diameter?"
  type: multiple-choice
  options:
    - "Myelin adds sodium channels along the entire axon, allowing more simultaneous depolarization"
    - "Myelin increases the diameter of the axon, reducing axoplasmic resistance so current flows faster"
    - "Myelin increases internodal membrane resistance and decreases capacitance, allowing passive current to travel long distances with minimal decay — so the signal jumps from node to node rather than propagating continuously"
    - "Myelin provides metabolic energy directly to the axon, accelerating the Na⁺/K⁺-ATPase pump cycle"
  answer: 2
  explanation: "Myelin's electrical effect is to make the internode behave like a well-insulated wire: high membrane resistance (ions cannot leak out) and low capacitance (little charge is needed to change voltage). Together, these properties allow the local current generated at one node to spread passively through the internode with very little attenuation — enough current arrives at the next node to trigger a fresh action potential. Rather than depolarizing every patch of membrane (slow, continuous conduction), the signal jumps between nodes spaced ~1mm apart. This saltatory mode achieves velocities of 80-120 m/s vs. 0.5-2 m/s for unmyelinated fibers. Options A and B are wrong — myelin does not add channels or change axon diameter."

- question: "In myelinated axons, voltage-gated sodium channels are concentrated at nodes of Ranvier rather than distributed uniformly along the axon membrane."
  type: true-false
  answer: true
  explanation: "This is the structural basis of saltatory conduction. Nodes of Ranvier are the ~1 μm gaps between myelin segments where the axon membrane is exposed. These nodes contain extremely high densities of voltage-gated Na⁺ channels — the entire machinery for action potential regeneration is clustered here. The internodal membrane, covered by myelin, has very few voltage-gated channels; it is electrically passive and serves only as a conduit for the spread of current from node to node. This arrangement means ion exchange (and the metabolic cost of restoring gradients) occurs only at nodes, which make up less than 1% of the axon's surface area, dramatically reducing energy expenditure."

- question: "Saltatory conduction is faster than continuous conduction because action potentials travel through the myelinated internode at higher speed, like a signal through a copper wire."
  type: true-false
  answer: false
  explanation: "Action potentials do not 'travel' through myelinated internodes at all — there are no voltage-gated channels in the internode to regenerate the signal. What propagates through the internode is passive electrical current spreading from the active node, exactly like current through a cable. This passive spread is fast because myelin's high resistance and low capacitance minimize leakage and charge requirements. The 'speed' of saltatory conduction comes from skipping large stretches of membrane — regenerating only at widely spaced nodes — rather than from any faster travel through internodes. The distinction matters: it's about reducing the number of regeneration events, not the speed of any individual event."

- question: "What electrical properties does myelin confer on the internodal axon membrane, and how do these properties allow current to reach the next node of Ranvier without triggering an action potential along the way?"
  type: short-answer
  answer: "Myelin dramatically increases the electrical resistance of the internodal membrane (by providing a thick insulating barrier through which ions cannot easily flow) and decreases its capacitance (by increasing the distance between the conducting axoplasm and the extracellular fluid, reducing the membrane's ability to store charge). High resistance means very little current leaks out through the internode; low capacitance means little charge is needed to change the voltage. Together, these properties allow the local circuit current generated at an active node to flow passively through the axoplasm and spread to the next node with minimal decay — arriving with enough charge to depolarize the node to threshold. No action potential fires along the way because the internodal membrane lacks the voltage-gated sodium channels required for regeneration; those channels are clustered exclusively at nodes."
  explanation: "Students often describe saltatory conduction correctly (jumps from node to node) without understanding the mechanism (why current doesn't decay along the way). The two-part answer — high resistance prevents leakage, low capacitance reduces the charge needed — is the complete explanation. Both properties together make the internode a good passive cable; either alone would be insufficient."
```

## Explainer

From your study of action potential repolarization, you understand how voltage-gated sodium and potassium channels generate a self-regenerating electrical signal that propagates along an axon. In an unmyelinated axon, this propagation is continuous: each patch of membrane depolarizes the next, and the action potential moves forward like a lit fuse. It works, but it is slow — roughly 0.5 to 2 meters per second in thin unmyelinated fibers. **Saltatory conduction** is evolution's solution for speed, and it depends on wrapping the axon in an insulating sheath of **myelin**.

Myelin is produced by **oligodendrocytes** in the central nervous system and **Schwann cells** in the peripheral nervous system. These glial cells wrap their plasma membranes around the axon in tight, concentric layers — sometimes 50 to 100 wraps thick — creating a fatty insulating barrier. This insulation has two critical electrical effects. First, it dramatically increases the **membrane resistance** of the internode (the myelinated segment), meaning ions cannot easily leak out across the membrane. Second, it decreases the **membrane capacitance**, meaning less charge is needed to change the voltage. Together, these properties allow the local current generated by an action potential at one node to spread passively through the myelinated internode with very little loss — like sending current through a well-insulated wire instead of a leaky garden hose.

The action potential does not actually travel through the myelinated segments. Instead, it "jumps" from one **node of Ranvier** to the next. Nodes are short (~1 μm) gaps between myelin segments where the axon membrane is exposed and densely packed with voltage-gated sodium channels. When passive current from the previous node reaches a new node, it depolarizes the membrane to threshold, and a fresh action potential fires. The signal then spreads passively to the next node, where it regenerates again. This jumping pattern — from the Latin *saltare*, meaning "to leap" — is why the process is called **saltatory conduction**. Conduction velocity in myelinated fibers reaches 80 to 120 meters per second, fast enough that a signal from your toe reaches your brain in about 20 milliseconds.

Saltatory conduction also confers a major **energy advantage**. Because ion flux (and therefore ATP-dependent Na⁺/K⁺-ATPase pumping to restore gradients) only occurs at the nodes — which make up less than 1% of the axon's surface area — the metabolic cost of signaling is far lower than in continuous conduction. This matters enormously in the brain, which already consumes about 20% of the body's energy. The clinical consequence of myelin loss is devastating: in diseases like **multiple sclerosis**, autoimmune demyelination exposes internodal membrane that lacks sufficient ion channels, causing conduction block or severe slowing. Symptoms — vision loss, weakness, numbness — directly reflect which axonal tracts have lost their myelin insulation.
