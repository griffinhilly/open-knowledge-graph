---
id: autonomic-nervous-system-organ-effects
title: Autonomic Nervous System Organization and Organ Effects
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: neural-anatomy-and-organization
  type: hard
- id: endocrine-glands-and-hormones
  type: soft
- id: autonomic-nervous-system
  type: hard
- id: synaptic-transmission
  type: soft
builds-toward:
- stress-response-adaptation
tags:
- autonomic-nervous-system
- sympathetic
- parasympathetic
stage: advanced
status: draft
---

# Autonomic Nervous System Organization and Organ Effects

## Core Idea
The autonomic nervous system maintains homeostasis through complementary sympathetic (arousal, metabolic mobilization) and parasympathetic (rest, conservation) divisions. Sympathetic activation increases heart rate, dilates pupils, inhibits digestion, and mobilizes glucose via norepinephrine and epinephrine. Parasympathetic activation decreases heart rate, promotes digestion, and activates bladder via acetylcholine. Most organs receive dual innervation, allowing coordinated control tailored to physiological demands.

## Questions

```yaml
- question: "A researcher administers a drug that blocks all nicotinic acetylcholine receptors at autonomic ganglia. Which ANS division is preferentially impaired?"
  type: multiple-choice
  options:
    - "Parasympathetic only, because it relies on acetylcholine throughout"
    - "Sympathetic only, because postganglionic sympathetic fibers use norepinephrine"
    - "Both divisions equally, because both use acetylcholine at the preganglionic synapse"
    - "Neither division, because ganglionic transmission uses different receptors than organ-level transmission"
  answer: 2
  explanation: "Both sympathetic and parasympathetic divisions use acetylcholine at the preganglionic synapse (on nicotinic receptors in the ganglion). The difference between divisions is only at the postganglionic–organ junction: sympathetic postganglionic fibers release norepinephrine, parasympathetic release acetylcholine. Blocking nicotinic ganglionic receptors therefore disrupts both divisions. The common misconception is that because 'parasympathetic = acetylcholine,' only parasympathetic would be affected — but that only applies to the end-organ synapse."

- question: "An athlete has a resting heart rate of 48 bpm. Which best explains this?"
  type: multiple-choice
  options:
    - "High sympathetic tone accelerates cardiac conduction, which paradoxically lowers resting rate"
    - "High parasympathetic (vagal) tone dominates cardiac pacemaker activity at rest, slowing the SA node"
    - "Low norepinephrine release reduces β₁ stimulation, indicating sympathetic hypoactivity"
    - "The SA node in trained athletes is intrinsically slower due to structural remodeling alone"
  answer: 1
  explanation: "At rest, parasympathetic (vagal) tone dominates cardiac control — the SA node is continuously slowed by acetylcholine acting on muscarinic receptors. Endurance training increases vagal tone, so athletes have a slower resting rate. Option C is partially true (less sympathetic input contributes) but the primary driver is increased parasympathetic dominance, not just sympathetic hypoactivity. This illustrates how the ANS is a continuously modulated dial, not a binary switch."

- question: "The sympathetic and parasympathetic divisions use entirely different neurotransmitters at every synapse in their respective pathways."
  type: true-false
  answer: false
  explanation: "Both divisions use acetylcholine at the preganglionic synapse (acting on nicotinic receptors in the ganglion). The distinction in neurotransmitter only applies postganglionic: sympathetic fibers release norepinephrine onto target organs; parasympathetic fibers release acetylcholine (acting on muscarinic receptors). Knowing this matters pharmacologically — ganglionic blockers affect both divisions, while muscarinic blockers or adrenergic blockers selectively target one division's end-organ effects."

- question: "Dual innervation of an organ allows the nervous system to fine-tune organ function beyond what a single division could achieve alone."
  type: true-false
  answer: true
  explanation: "Most organs receive opposing input from both divisions, enabling continuous bidirectional modulation rather than simple on/off control. The heart, for example, can be sped up by withdrawing parasympathetic tone, increased sympathetic input, or both simultaneously. This reciprocal arrangement also means both overactivation and underactivation of either division can cause distinct pathologies — loss of parasympathetic GI innervation causes ileus; excess sympathetic tone raises cardiovascular risk."

- question: "Why does loss of parasympathetic innervation to the GI tract cause ileus (bowel paralysis), and what does this reveal about the resting state of parasympathetic tone?"
  type: short-answer
  answer: "Parasympathetic tone actively drives GI motility at rest — it promotes peristalsis and secretion via acetylcholine on muscarinic receptors. Removing that input doesn't return the bowel to a neutral state; it removes the drive that keeps it moving. This reveals that parasympathetic activity is not optional or only situational but is the dominant resting input to the GI system. The ANS is always 'on' at some level in both divisions."
  explanation: "This illustrates a key principle: the 'rest-and-digest' label doesn't mean parasympathetic activity is only active during relaxation. It is tonically active in the GI tract under normal conditions. The sympathetic system inhibits digestion during stress by suppressing this ongoing parasympathetic activity — not by imposing paralysis directly. Understanding tonic versus phasic ANS activity is essential for interpreting both normal physiology and drug effects."
```

## Explainer

From your study of neural anatomy and synaptic transmission, you already know the basic wiring: neurons release neurotransmitters that bind receptors, causing target cells to depolarize or hyperpolarize. The autonomic nervous system applies this machinery to involuntary control of the body's internal organs. What makes the ANS distinctive is its two-neuron chain. Rather than a single neuron running from the spinal cord to the target organ, the ANS uses a **preganglionic neuron** that synapses in a peripheral **ganglion**, where a **postganglionic neuron** then projects to the organ. This relay architecture allows divergence — one preganglionic neuron can branch to synapse onto many postganglionic neurons, enabling coordinated, body-wide responses.

The two divisions differ in both anatomy and chemistry. The **sympathetic** division has short preganglionic fibers (synapsing in paravertebral ganglia near the spine) and long postganglionic fibers that release **norepinephrine** onto target organs. The **parasympathetic** division has long preganglionic fibers (traveling all the way to ganglia embedded in or near target organs) and short postganglionic fibers that release **acetylcholine**. Both divisions use acetylcholine at the preganglionic synapse — it is the postganglionic transmitter that differs. This distinction is pharmacologically critical: drugs targeting adrenergic receptors (norepinephrine) selectively affect sympathetic end-organ effects, while muscarinic blockers (blocking ACh receptors) selectively affect parasympathetic effects.

The simplest organizing framework is **"fight-or-flight" versus "rest-and-digest."** Sympathetic activation prepares the body for action: heart rate and contractility increase (↑ cardiac output), bronchioles dilate (↑ airflow), pupils dilate (↑ visual field), blood is redirected from the gut to skeletal muscle, and the liver mobilizes glucose. Parasympathetic activation reverses these priorities: heart rate decreases, digestion is promoted (↑ peristalsis, ↑ secretion), glands secrete, the bladder contracts, and the pupils constrict. The mnemonic **SLUDD** captures the parasympathetic end-organ effects: **S**alivation, **L**acrimation, **U**rination, **D**efecation, **D**igestion.

The functional significance of **dual innervation** is that most organs receive both sympathetic and parasympathetic input with opposing effects, allowing fine-tuned regulation. Consider the heart: sympathetic stimulation increases heart rate via β₁ adrenergic receptors; parasympathetic stimulation decreases it via muscarinic receptors on the SA node. At rest, parasympathetic tone dominates — which is why athletes with high vagal tone have slow resting heart rates. Under stress, sympathetic tone overrides this. This reciprocal arrangement is also why both overactivation and underactivation of either division can cause pathology: excessive sympathetic tone raises blood pressure and increases cardiovascular risk; loss of parasympathetic innervation to the GI tract produces ileus (bowel paralysis). The ANS is not simply an on/off switch but a continuously modulated dial with two opposing hands.
