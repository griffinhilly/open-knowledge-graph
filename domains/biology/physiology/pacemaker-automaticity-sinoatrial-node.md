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
stage: advanced
status: draft
---

# Pacemaker Automaticity and the Sinoatrial Node

## Core Idea
Pacemaker cells in the sinoatrial node generate spontaneous, rhythmic action potentials that drive the heart's contractions without external stimulation. Unlike typical neurons, pacemaker cells lack a stable resting potential and gradually depolarize (Phase 4 diastolic depolarization) until reaching threshold, making them intrinsically rhythmic.

## How It's Best Learned
Examine the pacemaker action potential with particular focus on Phase 4, showing the roles of funny current (HCN channels), L-type calcium current, and potassium current. Trace how autonomic innervation steepens or flattens Phase 4 to increase or decrease heart rate.

## Common Misconceptions
- Thinking pacemaker cells have a stable resting potential like other cells; they actually have a gradual diastolic depolarization.
- Assuming the SA node fires at a fixed intrinsic rate; the rate is modulated by SNS and PNS tone.

## Explainer

From your study of action potentials and resting membrane potential, you know that most excitable cells sit at a stable resting voltage (around −70 to −90 mV) and fire only when an external stimulus pushes them to threshold. Pacemaker cells in the **sinoatrial (SA) node** break this rule entirely. They have no stable resting potential. Instead, after each action potential, they immediately begin drifting back toward threshold on their own — a process called **Phase 4 diastolic depolarization** or the "pacemaker potential." This spontaneous drift is what makes the heart self-starting: it beats without any neural command, hormonal signal, or external stimulus.

The molecular basis of Phase 4 involves three overlapping ion currents. As the cell repolarizes at the end of an action potential, a unique channel opens: the **HCN channel** (hyperpolarization-activated cyclic nucleotide-gated), which conducts the **funny current (If)**. This channel is unusual because it opens at hyperpolarized (negative) potentials — the opposite of most voltage-gated channels. If carries an inward current of sodium and potassium that starts the slow depolarization. As the membrane voltage creeps upward, **T-type calcium channels** open, adding an inward calcium current that accelerates the depolarization. Finally, **L-type calcium channels** open near threshold, producing the rapid upstroke of the pacemaker action potential. Notice what is absent: there is no fast sodium current. Pacemaker action potentials are calcium-driven, which is why they are slower and more gradual than the sharp, sodium-dependent action potentials of ventricular myocytes.

The SA node sets the heart's rhythm because it depolarizes faster than any other pacemaker tissue. Its intrinsic rate is approximately 100 beats per minute, but resting heart rate is typically 60–70 bpm because of tonic **vagal (parasympathetic) inhibition**. Acetylcholine released by vagal nerve endings activates muscarinic receptors on SA node cells, opening potassium channels (IKACh) that hyperpolarize the cell and reducing If by lowering cAMP. Both effects flatten the Phase 4 slope, so it takes longer to reach threshold and heart rate decreases. Conversely, **sympathetic stimulation** releases norepinephrine, which activates beta-1 adrenergic receptors, increases cAMP, enhances If and L-type calcium current, and steepens Phase 4 — the cell reaches threshold faster and heart rate increases.

This autonomic modulation of the pacemaker slope is the primary mechanism for moment-to-moment heart rate control. If the SA node fails, backup pacemakers in the **atrioventricular (AV) node** (intrinsic rate ~40–60 bpm) or the **Purkinje fibers** (intrinsic rate ~20–40 bpm) can take over, but at progressively slower rates because their Phase 4 depolarization is inherently slower. This hierarchy ensures that the fastest pacemaker always drives the heart, and it explains why SA node dysfunction leads to bradycardia rather than cardiac arrest — the backup pacemakers provide a safety net, albeit at a rate that may be insufficient for normal activity.
