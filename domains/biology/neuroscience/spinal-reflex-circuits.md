---
id: spinal-reflex-circuits
title: Spinal Reflex Circuits
domain: biology
course: neuroscience
prerequisites:
- id: neuromuscular-junction
  type: hard
- id: gaba-systems
  type: soft
tags:
- motor-systems
- reflexes
stage: expert
status: draft
---

# Spinal Reflex Circuits

## Core Idea
Monosynaptic stretch reflex provides stability. Polysynaptic reflexes coordinate muscles. Central pattern generators produce rhythmic locomotor patterns with minimal descending input.

## Questions

```yaml
- question: "A patient with a complete spinal cord injury at the thoracic level — severing all descending connections from the brain — is supported on a treadmill. Under what circumstances might rhythmic stepping movements appear in the legs?"
  type: multiple-choice
  options:
    - "Never — voluntary locomotion requires intact corticospinal tracts from the motor cortex to the spinal cord"
    - "Only if sensory feedback from the legs is artificially eliminated, removing inhibitory input"
    - "Rhythmic stepping can occur because central pattern generators in the lumbar spinal cord can generate locomotor rhythms intrinsically, without descending commands"
    - "Only with electrical stimulation of the motor cortex, which can bypass the injury and trigger spinal circuits"
  answer: 2
  explanation: "Central pattern generators (CPGs) are spinal interneuron networks that generate rhythmic, alternating motor patterns without requiring continuous commands from the brain. This has been demonstrated directly in isolated spinal cord preparations — the rhythm is intrinsic to the spinal circuitry. The brain normally modulates CPG output (initiating walking, adjusting speed and gait) but does not generate the fundamental pattern. After spinal cord injury above the lumbar CPG, rhythmic stepping can sometimes be elicited by treadmill loading and sensory input to the spinal cord alone."

- question: "When you step on a sharp object, your foot jerks away and your opposite leg simultaneously stiffens. What spinal circuit mechanism produces the stiffening of the opposite leg?"
  type: multiple-choice
  options:
    - "The pain signal travels to the brain, which sends a rapid descending command to stiffen the opposite leg"
    - "Crossed-extension: spinal interneurons simultaneously activate extensors and inhibit flexors in the contralateral limb, coordinated at the spinal level"
    - "The stretch reflex in the opposite leg is triggered automatically by the sudden shift in body weight"
    - "GABAergic interneurons suppress the crossed-extension response on the ipsilateral side, disinhibiting the opposite leg"
  answer: 1
  explanation: "Crossed-extension is a polysynaptic spinal reflex requiring no brain involvement. Pain afferents activate interneurons that drive ipsilateral flexors (pulling the foot away) and inhibit ipsilateral extensors, while simultaneously crossing the midline via commissural interneurons to activate contralateral extensors and inhibit contralateral flexors. The result is the opposite leg stiffening to bear weight, preventing a fall. This coordinated bilateral response demonstrates that spinal circuits can integrate information across both sides of the body to produce functionally coherent behavior."

- question: "Central pattern generators can produce coordinated rhythmic motor patterns even in isolated spinal cord preparations with all descending input from the brain removed."
  type: true-false
  answer: true
  explanation: "This has been demonstrated experimentally in cats, lampreys, and other animals: an isolated spinal cord (or even a section of it) bath-applied with neuromodulators like dopamine or NMDA can produce rhythmic, alternating patterns of motor activity resembling locomotion, with no input from supraspinal structures. The CPG rhythm is intrinsic to the spinal interneuron network. This finding fundamentally changed the understanding of locomotion: the brain initiates and modulates walking, but the basic stepping pattern is generated locally."

- question: "The knee-jerk reflex (patellar tendon reflex) is a polysynaptic reflex because it involves rapid coordination of multiple muscles."
  type: true-false
  answer: false
  explanation: "The knee-jerk reflex is the canonical example of a *monosynaptic* reflex. Ia afferent fibers from muscle spindles in the quadriceps enter the spinal cord and synapse directly onto alpha motor neurons — just one synapse. This is why it is so fast (~30 ms). Polysynaptic reflexes, like the flexor withdrawal reflex, interpose interneurons between sensory input and motor output, which allows for more complex coordination (including reciprocal inhibition and crossed-extension) but introduces additional synaptic delays."

- question: "What does the existence of central pattern generators reveal about the relationship between the brain and spinal cord in generating locomotion?"
  type: short-answer
  answer: "CPGs demonstrate that the spinal cord is not a passive relay of brain commands but an active computational structure capable of generating complex, rhythmically coordinated motor patterns on its own. The brain's role in locomotion is modulatory and supervisory — it initiates walking, selects gait, and makes real-time adjustments — but the fundamental rhythm of alternating flexion and extension is generated by spinal interneuron circuits. This division of labor means locomotion can persist (in altered form) after spinal injury, and that the spinal cord encodes substantial motor 'knowledge' independently."
  explanation: "This insight has significant clinical implications. Rehabilitation strategies after spinal cord injury now target CPG reactivation through treadmill training and epidural stimulation, exploiting the spinal cord's intrinsic locomotor circuitry. It also explains why decerebrate cats can still walk on a treadmill and why premature infants show stepping movements — the spinal circuitry for locomotion develops and functions before cortical control is fully established."
```

## Explainer

You already know how signals cross the neuromuscular junction to contract a muscle. Spinal reflex circuits are the wiring that decides *when* and *how much* a muscle contracts — often without any input from the brain at all. These circuits are the nervous system's fastest responses, and they reveal fundamental principles about how neural networks coordinate movement.

The simplest reflex is the **monosynaptic stretch reflex**, the circuit behind the knee-jerk test. When a doctor taps your patellar tendon, the quadriceps muscle stretches slightly. Embedded within the muscle, **muscle spindles** — specialized sensory receptors — detect this stretch and fire action potentials along Ia afferent fibers. These fibers enter the spinal cord through the dorsal root and synapse directly onto **alpha motor neurons** in the ventral horn — just one synapse, hence "monosynaptic." The motor neuron fires, the quadriceps contracts, and the leg kicks. The whole loop takes about 30 milliseconds. This reflex acts as an automatic stability system: any unexpected stretch is immediately counteracted by contraction, keeping muscles at their intended length during posture and movement.

Real-world reflexes are rarely this simple. **Polysynaptic reflexes** involve interneurons between the sensory input and motor output, enabling more sophisticated coordination. The **flexor withdrawal reflex** is the classic example: you step on a tack, and your foot yanks away before you consciously feel pain. Pain receptors fire, sensory fibers activate excitatory interneurons that drive flexor motor neurons (pulling the foot up), while simultaneously activating inhibitory interneurons — including GABAergic and glycinergic cells — that suppress extensor motor neurons in the same leg (so the leg does not fight itself). But your body does something even more clever: through **crossed-extension**, the opposite leg's extensors are activated and flexors inhibited, stiffening the other leg so you do not fall over. This coordinated pattern — flexion on one side, extension on the other — requires multiple layers of interneurons organized across both sides of the spinal cord.

The most sophisticated spinal circuits are **central pattern generators (CPGs)** — networks of interneurons that produce rhythmic, alternating motor patterns like walking, swimming, or breathing without requiring continuous commands from the brain. A CPG for locomotion alternates between flexor and extensor activation in each limb, while coordinating left-right and fore-hind limb timing. Remarkably, these patterns can be produced even in isolated spinal cord preparations with no descending brain input, demonstrating that the fundamental rhythm is intrinsic to the spinal circuitry itself. Descending signals from the brainstem and cortex modulate CPG activity — initiating, stopping, or adjusting speed and gait — but the pattern generation is local. This is why spinal cord injury above the CPG can sometimes preserve rhythmic stepping movements even when voluntary control is lost.
