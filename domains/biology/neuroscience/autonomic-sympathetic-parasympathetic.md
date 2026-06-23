---
id: autonomic-sympathetic-parasympathetic
title: 'Autonomic Nervous System: Sympathetic and Parasympathetic Physiology'
domain: biology
course: neuroscience
prerequisites:
- id: synaptic-transmission
  type: soft
- id: dopamine-reward-system
  type: soft
- id: acetylcholine-system
  type: soft
tags:
- autonomic-nervous-system
- sympathetic
- parasympathetic
- homeostasis
stage: formal-systems
status: validated
---

# Autonomic Nervous System: Sympathetic and Parasympathetic Physiology

## Core Idea
The autonomic nervous system controls involuntary functions (heart rate, digestion, pupil size) through sympathetic (fight-or-flight) and parasympathetic (rest-and-digest) divisions with opposing effects on most organs. Sympathetic neurons release norepinephrine; parasympathetic neurons release acetylcholine. The balance between these divisions maintains homeostatic stability.

## Questions

```yaml
- question: "A pharmacologist administers a drug that blocks all muscarinic acetylcholine receptors. Which of the following effects would you expect?"
  type: multiple-choice
  options:
    - "Decreased heart rate — blocking muscarinic receptors reduces sympathetic drive to the heart"
    - "Increased heart rate — blocking muscarinic receptors removes tonic parasympathetic slowing of the heart"
    - "No change in heart rate — muscarinic receptors are only found in skeletal muscle"
    - "Decreased heart rate — the drug enhances norepinephrine release by eliminating cholinergic competition"
  answer: 1
  explanation: "Parasympathetic postganglionic neurons release acetylcholine at muscarinic receptors on target organs. The vagus nerve continuously delivers tonic parasympathetic slowing to the heart — without this, the intrinsic pacemaker rate is ~100 bpm. Blocking muscarinic receptors (with atropine, for example) removes this parasympathetic brake, and heart rate rises. This reveals that resting heart rate (~70 bpm) is not the heart's intrinsic rate but the result of active parasympathetic inhibition."

- question: "What neurotransmitter do preganglionic sympathetic neurons release at the sympathetic ganglion?"
  type: multiple-choice
  options:
    - "Norepinephrine — sympathetic neurons always use norepinephrine"
    - "Acetylcholine at nicotinic receptors — both sympathetic and parasympathetic preganglionic neurons use acetylcholine"
    - "Dopamine — the ganglionic synapse uses dopamine as an intermediate signal"
    - "Acetylcholine at muscarinic receptors — the same receptors used by the parasympathetic postganglionic neurons"
  answer: 1
  explanation: "Both sympathetic and parasympathetic preganglionic neurons release acetylcholine at nicotinic receptors in their respective ganglia. The key pharmacological distinction comes AFTER the ganglion: parasympathetic postganglionic neurons release ACh at muscarinic receptors on target organs, while sympathetic postganglionic neurons release norepinephrine at adrenergic receptors. The 'sympathetic = norepinephrine' rule applies to the terminal organ synapse, not to the ganglionic synapse."

- question: "Sympathetic postganglionic neurons release acetylcholine at target organs."
  type: true-false
  answer: false
  explanation: "False. Sympathetic postganglionic neurons release norepinephrine (NE) at adrenergic receptors on target organs — this drives the fight-or-flight responses (increased heart rate, vasoconstriction in gut, bronchodilation, etc.). It is the parasympathetic postganglionic neurons that release acetylcholine, at muscarinic receptors. The exception is sympathetic innervation of sweat glands and some blood vessels, which do use ACh, but the dominant sympathetic terminal transmitter is norepinephrine."

- question: "Both sympathetic and parasympathetic divisions use acetylcholine at their preganglionic synapses."
  type: true-false
  answer: true
  explanation: "True. The two-neuron architecture is shared: preganglionic neuron (CNS) → ganglion → postganglionic neuron (organ). In both divisions, the preganglionic-to-postganglionic synapse in the ganglion uses acetylcholine at nicotinic receptors. The divisions diverge at the second synapse: parasympathetic postganglionic neurons use ACh at muscarinic receptors; sympathetic postganglionic neurons use norepinephrine at adrenergic receptors. This shared preganglionic neurotransmitter is why nicotinic blockers affect both divisions simultaneously."

- question: "Why do atropine (a muscarinic blocker) and beta-blockers have opposite effects on heart rate, and what does this reveal about how the ANS controls the heart?"
  type: short-answer
  answer: "Atropine blocks muscarinic receptors, eliminating parasympathetic signaling to the heart, so heart rate rises toward the intrinsic pacemaker rate (~100 bpm). Beta-blockers block adrenergic (β1) receptors, reducing sympathetic drive to the heart, so heart rate falls. Both drugs act on the same organ but via different receptor systems representing opposite divisions. This reveals that resting heart rate is a dynamic balance: tonic parasympathetic tone is continuously slowing the heart while sympathetic tone modulates it upward. The heart rate at any moment reflects competition between both divisions, not the activation of just one."
  explanation: "This question tests whether students understand the heart as a system under dual control, not simply 'sympathetic speeds it up, parasympathetic slows it down in isolation.' The pharmacology makes the underlying physiology concrete and reveals that both divisions are tonically active at rest."
```

## Explainer

From your study of synaptic transmission, you understand how neurons communicate through neurotransmitter release at synapses. The autonomic nervous system (ANS) applies this machinery to control the body's internal organs — heart, lungs, gut, blood vessels, glands — without conscious effort. It is the neural infrastructure of homeostasis, continuously adjusting organ function to match the body's changing demands.

The ANS is organized into two divisions with largely opposing effects. The **sympathetic division** prepares the body for action — the classic "fight-or-flight" response. When activated, it increases heart rate and contractile force, dilates bronchioles to increase airflow, redirects blood from the gut to skeletal muscles, dilates pupils, and triggers glucose release from the liver. The **parasympathetic division** does roughly the opposite — the "rest-and-digest" response. It slows the heart, constricts bronchioles, stimulates digestive secretions and gut motility, and constricts pupils. Most organs receive input from both divisions, and the body's moment-to-moment physiological state reflects the balance between them, not the action of one alone. Your resting heart rate, for example, is not an intrinsic property of the heart — it is set by tonic parasympathetic slowing via the vagus nerve. Block the vagus, and heart rate jumps from ~70 to ~100 beats per minute.

Both divisions share a common two-neuron architecture: a **preganglionic neuron** in the central nervous system synapses onto a **postganglionic neuron** in a peripheral ganglion, which then innervates the target organ. The key pharmacological difference lies in the neurotransmitters used. All preganglionic neurons — both sympathetic and parasympathetic — release **acetylcholine** (ACh) at nicotinic receptors in the ganglion. But the postganglionic neurons differ: parasympathetic postganglionic neurons release ACh at **muscarinic receptors** on target organs, while sympathetic postganglionic neurons release **norepinephrine** (NE) at adrenergic receptors. This distinction explains why drugs targeting these receptor systems have such specific physiological effects — atropine (a muscarinic antagonist) blocks parasympathetic output, causing elevated heart rate and dry mouth, while beta-blockers reduce sympathetic drive to the heart.

The two divisions also differ anatomically. Sympathetic preganglionic neurons originate from the thoracic and lumbar spinal cord and synapse in paravertebral ganglia close to the spine, sending long postganglionic fibers to distant targets — an arrangement that enables rapid, coordinated whole-body activation. Parasympathetic preganglionic neurons originate from brainstem nuclei (via cranial nerves III, VII, IX, and X) and sacral spinal cord, with long preganglionic fibers that synapse in ganglia near or within the target organs, allowing more localized, organ-specific control. This is why sympathetic activation tends to be diffuse — a global alarm signal — while parasympathetic effects are more targeted and graded.
