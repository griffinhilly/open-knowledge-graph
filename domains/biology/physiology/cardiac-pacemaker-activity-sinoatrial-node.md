---
id: cardiac-pacemaker-activity-sinoatrial-node
title: Cardiac Pacemaker Activity and the Sinoatrial Node
domain: biology
course: physiology
prerequisites:
- id: action-potential
  type: hard
- id: cardiac-cycle-and-heart-function
  type: hard
builds-toward:
- atrioventricular-conduction-delay
- heart-rate-control-autonomic-modulation
tags:
- cardiac
- electrophysiology
- pacemaker
- automaticity
stage: advanced
status: draft
---

# Cardiac Pacemaker Activity and the Sinoatrial Node

## Core Idea
The sinoatrial (SA) node is the heart's primary pacemaker, capable of spontaneous rhythmic depolarization at 60-100 bpm due to unique ion channel kinetics: funny currents (If) and L-type calcium channels drive diastolic depolarization toward threshold in the absence of external input. SA nodal tissue lacks a stable resting potential; instead, the membrane potential gradually drifts upward until reaching threshold, triggering an action potential and heartbeat. The intrinsic rhythm is modulated by the autonomic nervous system: parasympathetic activation hyperpolarizes and slows the nodal rate, while sympathetic activation depolarizes and accelerates it.

## How It's Best Learned
Study isolated SA node preparations to observe spontaneous depolarization and action potential generation. Use pharmacology (acetylcholine, isoproterenol) to observe autonomic effects on pacemaker rate.

## Common Misconceptions
The SA node is not the only cardiac pacemaker; other regions (AV node, Purkinje fibers) also generate action potentials and can pace the heart if the SA node fails, though at slower intrinsic rates.

## Explainer

From your study of action potentials, you know that most excitable cells maintain a stable resting membrane potential — they sit quietly at around −70 to −90 mV until an external stimulus pushes them to threshold. The **sinoatrial (SA) node** breaks this rule. Its cells never truly rest. Instead, after each action potential repolarizes, the membrane potential immediately begins drifting upward again in a phase called **pacemaker potential** (or Phase 4 depolarization). This spontaneous drift is what makes the heart beat without any external command — no neural input, no hormonal signal, just an intrinsic property of the ion channels in SA nodal cells.

The pacemaker potential is driven by a specific set of ion currents. As the cell repolarizes past about −60 mV, **funny channels** (If) open. These are unusual because they are activated by hyperpolarization rather than depolarization — hence the name "funny." They conduct a mixed Na+/K+ inward current that slowly depolarizes the membrane. As the membrane potential rises past about −50 mV, **T-type calcium channels** open and add more inward current. Finally, near threshold (around −40 mV), **L-type calcium channels** open and drive the rapid upstroke of the SA node action potential. Notice the contrast with ventricular myocytes you studied in the cardiac cycle: ventricular action potentials have a fast sodium-driven upstroke (Phase 0), but SA node action potentials rely on calcium for their upstroke, which is why they rise more slowly and have a rounded shape rather than a sharp spike.

The rate of this pacemaker cycle — and therefore heart rate — depends on three adjustable parameters: the **slope of Phase 4 depolarization** (steeper slope = faster drift to threshold = faster heart rate), the **maximum diastolic potential** (more negative starting point = longer time to reach threshold = slower rate), and the **threshold voltage** itself. The autonomic nervous system modulates all three. Sympathetic stimulation via norepinephrine activates beta-1 adrenergic receptors, which increase funny current and calcium current through cAMP-dependent phosphorylation — the Phase 4 slope steepens, and the cell reaches threshold sooner. Parasympathetic stimulation via acetylcholine activates muscarinic receptors, which open potassium channels (IKACh) that hyperpolarize the cell and also reduce funny current — the starting point becomes more negative and the slope shallows, both slowing the rate.

The SA node normally fires at 60-100 beats per minute, faster than any other cardiac pacemaker tissue. The AV node has an intrinsic rate of 40-60 bpm, and Purkinje fibers fire at 20-40 bpm. This **hierarchy of automaticity** ensures that the fastest pacemaker always captures the heart. If the SA node fails or its impulses are blocked, the next fastest pacemaker takes over as an escape rhythm — slower but life-sustaining. Understanding this hierarchy explains both normal heart rhythm and the clinical logic of pacemaker implantation: an artificial pacemaker replaces the SA node's function when disease disrupts the natural one.
