---
id: pacemaker-automaticity-sinoatrial-node
title: Pacemaker Automaticity and the Sinoatrial Node
domain: biology
course: physiology
prerequisites:
- id: cardiac-electrophysiology-action-potentials
  type: hard
- id: resting-membrane-potential
  type: hard
builds-toward:
- electrocardiogram-and-heart-rhythm
- autonomic-nervous-system
tags:
- pacemaker
- automaticity
- sinoatrial-node
stage: formal-systems
status: validated
---

# Pacemaker Automaticity and the Sinoatrial Node

## Core Idea
Pacemaker cells in the sinoatrial node generate spontaneous, rhythmic action potentials that drive the heart's contractions without external stimulation. Unlike typical neurons, pacemaker cells lack a stable resting potential and gradually depolarize (Phase 4 diastolic depolarization) until reaching threshold, making them intrinsically rhythmic.

## How It's Best Learned
Examine the pacemaker action potential with particular focus on Phase 4, showing the roles of funny current (HCN channels), L-type calcium current, and potassium current. Trace how autonomic innervation steepens or flattens Phase 4 to increase or decrease heart rate.

## Common Misconceptions
- Thinking pacemaker cells have a stable resting potential like other cells; they actually have a gradual diastolic depolarization.
- Assuming the SA node fires at a fixed intrinsic rate; the rate is modulated by SNS and PNS tone.

## Questions

```yaml
- question: "A new drug completely blocks HCN channels (the funny current, If) in SA node cells. What would you predict about heart rate?"
  type: multiple-choice
  options:
    - "Heart rate would increase, because removing the inward funny current eliminates an inhibitory influence on SA node firing"
    - "Heart rate would decrease, because If contributes to the initial slow Phase 4 depolarization — without it, the pacemaker potential rises more slowly, delaying threshold and slowing the firing rate"
    - "Heart rate would be unaffected because T-type and L-type Ca²⁺ channels would fully compensate"
    - "The heart would stop entirely because HCN channels generate the action potential upstroke"
  answer: 1
  explanation: "The funny current (If) is the first ion current to activate during Phase 4, initiating the slow depolarization that eventually triggers the action potential. Blocking If slows the rate at which Phase 4 voltage rises, so it takes longer to reach threshold — heart rate decreases. This is actually the mechanism of action of ivabradine, an HCN channel blocker used clinically to reduce heart rate in heart failure patients. The heart doesn't stop (T-type and L-type Ca²⁺ channels still drive depolarization) but it slows. HCN channels don't generate the upstroke — L-type Ca²⁺ channels do."

- question: "What drives the rapid upstroke (Phase 0) of the action potential in SA node pacemaker cells?"
  type: multiple-choice
  options:
    - "Fast voltage-gated sodium channels (Nav1.5), identical to the mechanism in ventricular cardiomyocytes"
    - "L-type (slow) calcium channels — SA node cells lack the fast sodium current, so their upstroke is calcium-driven, slower, and more gradual than in ventricular cells"
    - "The funny current (If) through HCN channels, which accumulates during Phase 4 and then produces the upstroke"
    - "Rapid potassium channel closure, which by removing the repolarizing current, passively creates a voltage rise"
  answer: 1
  explanation: "This is a key mechanistic difference between pacemaker and working cardiomyocyte action potentials. Ventricular cells have abundant Nav1.5 channels that open explosively at threshold to produce a fast, sharp upstroke. SA node cells lack this fast sodium current. Their Phase 0 upstroke is driven by L-type Ca²⁺ channels, which are slower — producing a more gradual, rounded upstroke with slower conduction velocity. This calcium-dependent AP explains why the SA node propagates slowly and why calcium channel blockers (verapamil, diltiazem) are so effective at controlling SA node and AV node firing rates."

- question: "The SA node fires at its intrinsic rate of approximately 60–70 beats per minute during normal rest."
  type: true-false
  answer: false
  explanation: "The SA node's intrinsic firing rate is approximately 100 beats per minute — the rate it fires when isolated from all neural input. Resting heart rate of 60–70 bpm is lower than this because of tonic vagal (parasympathetic) inhibition. Acetylcholine from vagal nerve endings activates muscarinic receptors, opening IKACh potassium channels (which hyperpolarize the cell) and reducing cAMP (which decreases If). Both effects flatten the Phase 4 slope, slowing the rate. This is why cutting the vagus nerve in an anesthetized animal causes heart rate to jump to ~100 bpm."

- question: "If the SA node fails, the heart will stop beating because no other cardiac tissue has pacemaker automaticity."
  type: true-false
  answer: false
  explanation: "The heart has a hierarchy of backup pacemakers. The AV node has an intrinsic rate of ~40–60 bpm, and Purkinje fibers have a rate of ~20–40 bpm. Both have Phase 4 diastolic depolarization; they are simply slower than the SA node, which is why the SA node normally dominates (the fastest pacemaker drives the heart). When the SA node fails, the AV node or Purkinje fibers take over — the heart still beats, just more slowly. This explains why SA node dysfunction causes bradycardia rather than sudden cardiac arrest, and why patients with sick sinus syndrome can often tolerate the condition before requiring a pacemaker."

- question: "What is Phase 4 diastolic depolarization, and why does it make SA node pacemaker cells fundamentally different from other excitable cells in the body?"
  type: short-answer
  answer: "Phase 4 diastolic depolarization is the spontaneous, gradual rise in membrane potential that occurs after each action potential in pacemaker cells. Unlike neurons, skeletal muscle, or ventricular cardiomyocytes — which maintain a stable resting membrane potential and fire only when an external stimulus depolarizes them to threshold — SA node cells have no stable resting potential. Immediately after repolarization, three overlapping ion currents (If via HCN channels, T-type Ca²⁺ current, and progressively more L-type Ca²⁺ current) drive the membrane voltage steadily upward until threshold is reached and the next action potential fires. This process is entirely intrinsic — no external stimulus is required. It makes the heart self-starting and rhythmically automatic."
  explanation: "The distinction from other excitable cells is fundamental: most excitable cells are reactive (they fire in response to input); pacemaker cells are spontaneous (they fire on their own schedule). The ion channels driving Phase 4 are unusual because they activate at hyperpolarized potentials — the HCN channel is literally named for this (hyperpolarization-activated). This inversion of normal voltage-gating logic is the molecular basis for pacemaker automaticity and is what allows the SA node to generate a heartbeat without any command from the brain or any other external source."
```

## Explainer

From your study of action potentials and resting membrane potential, you know that most excitable cells sit at a stable resting voltage (around −70 to −90 mV) and fire only when an external stimulus pushes them to threshold. Pacemaker cells in the **sinoatrial (SA) node** break this rule entirely. They have no stable resting potential. Instead, after each action potential, they immediately begin drifting back toward threshold on their own — a process called **Phase 4 diastolic depolarization** or the "pacemaker potential." This spontaneous drift is what makes the heart self-starting: it beats without any neural command, hormonal signal, or external stimulus.

The molecular basis of Phase 4 involves three overlapping ion currents. As the cell repolarizes at the end of an action potential, a unique channel opens: the **HCN channel** (hyperpolarization-activated cyclic nucleotide-gated), which conducts the **funny current (If)**. This channel is unusual because it opens at hyperpolarized (negative) potentials — the opposite of most voltage-gated channels. If carries an inward current of sodium and potassium that starts the slow depolarization. As the membrane voltage creeps upward, **T-type calcium channels** open, adding an inward calcium current that accelerates the depolarization. Finally, **L-type calcium channels** open near threshold, producing the rapid upstroke of the pacemaker action potential. Notice what is absent: there is no fast sodium current. Pacemaker action potentials are calcium-driven, which is why they are slower and more gradual than the sharp, sodium-dependent action potentials of ventricular myocytes.

The SA node sets the heart's rhythm because it depolarizes faster than any other pacemaker tissue. Its intrinsic rate is approximately 100 beats per minute, but resting heart rate is typically 60–70 bpm because of tonic **vagal (parasympathetic) inhibition**. Acetylcholine released by vagal nerve endings activates muscarinic receptors on SA node cells, opening potassium channels (IKACh) that hyperpolarize the cell and reducing If by lowering cAMP. Both effects flatten the Phase 4 slope, so it takes longer to reach threshold and heart rate decreases. Conversely, **sympathetic stimulation** releases norepinephrine, which activates beta-1 adrenergic receptors, increases cAMP, enhances If and L-type calcium current, and steepens Phase 4 — the cell reaches threshold faster and heart rate increases.

This autonomic modulation of the pacemaker slope is the primary mechanism for moment-to-moment heart rate control. If the SA node fails, backup pacemakers in the **atrioventricular (AV) node** (intrinsic rate ~40–60 bpm) or the **Purkinje fibers** (intrinsic rate ~20–40 bpm) can take over, but at progressively slower rates because their Phase 4 depolarization is inherently slower. This hierarchy ensures that the fastest pacemaker always drives the heart, and it explains why SA node dysfunction leads to bradycardia rather than cardiac arrest — the backup pacemakers provide a safety net, albeit at a rate that may be insufficient for normal activity.
