---
id: heart-rate-control-autonomic-modulation
title: Heart Rate Control and Autonomic Modulation
domain: biology
course: physiology
prerequisites:
- id: autonomic-nervous-system
  type: hard
- id: cardiac-pacemaker-activity-sinoatrial-node
  type: hard
- id: atrioventricular-conduction-delay
  type: soft
builds-toward:
- cardiac-output-stroke-volume-regulation
- blood-pressure-regulation
tags:
- cardiac
- autonomic
- heart rate
- regulation
stage: advanced
status: draft
---

# Heart Rate Control and Autonomic Modulation

## Core Idea
The intrinsic SA node firing rate is continuously modulated by parasympathetic (vagal) and sympathetic innervation acting on both SA and AV nodes through muscarinic and beta-adrenergic receptors. Parasympathetic activation via acetylcholine increases potassium conductance, hyperpolarizing the membrane and slowing pacemaker depolarization, thereby decreasing heart rate. Sympathetic activation via norepinephrine increases calcium and sodium conductances, accelerating pacemaker depolarization and increasing heart rate. These opposing influences allow heart rate to be adjusted from rest (~60 bpm) to maximal exercise (>180 bpm), maintaining cardiac output appropriate to metabolic demands.

## Common Misconceptions
Acetylcholine and norepinephrine do not produce identical effects throughout the heart; parasympathetic effects dominate at the SA and AV nodes, while sympathetic effects are more pronounced on ventricular contractility.

## Explainer

You already know from cardiac pacemaker physiology that the SA node generates spontaneous action potentials at an intrinsic rate of about 100 beats per minute in a denervated heart. Yet resting heart rate in a healthy person is only about 60-70 bpm. The difference is due to **vagal tone** — a continuous stream of parasympathetic input from the vagus nerve that actively slows the heart below its intrinsic rate. This means the default state of the heart is not neutrally balanced between two opposing inputs; it is being held back by the parasympathetic brake. Understanding this baseline is essential: when you see heart rate increase, it often reflects withdrawal of vagal tone rather than (or in addition to) sympathetic activation.

The parasympathetic pathway works through the **vagus nerve (cranial nerve X)**, which releases **acetylcholine (ACh)** at postganglionic terminals on the SA and AV nodes. ACh binds **M2 muscarinic receptors**, which activate an inhibitory G-protein (Gi). This has two effects: it opens **GIRK potassium channels** (IKACh), hyperpolarizing the pacemaker cell so it starts each cycle from a more negative membrane potential, and it reduces the funny current (If) and L-type calcium current by lowering intracellular cAMP. Both effects slow the pacemaker potential slope and delay the time to threshold, reducing heart rate — a response called **negative chronotropy**. Vagal effects are rapid because ACh is quickly hydrolyzed by acetylcholinesterase, allowing beat-to-beat modulation of heart rate.

The sympathetic pathway releases **norepinephrine (NE)** from postganglionic sympathetic fibers (and epinephrine from the adrenal medulla) that bind **beta-1 adrenergic receptors** on cardiac cells. Beta-1 activation stimulates Gs proteins, increasing adenylyl cyclase activity and raising cAMP levels. In pacemaker cells, cAMP directly opens funny channels and enhances L-type calcium current, steepening the Phase 4 depolarization slope and accelerating heart rate (**positive chronotropy**). At the AV node, sympathetic stimulation increases conduction velocity (**positive dromotropy**), allowing faster transmission of impulses to the ventricles. Unlike parasympathetic effects, sympathetic effects are slower in onset (seconds rather than milliseconds) because norepinephrine is removed by reuptake rather than enzymatic degradation.

The interplay between these two branches allows heart rate to be tuned across a wide range. During sudden standing, the baroreceptor reflex detects the drop in blood pressure and triggers both vagal withdrawal and sympathetic activation, rapidly increasing heart rate to maintain cerebral perfusion. During maximal exercise, vagal tone is essentially eliminated and sympathetic drive is maximal, pushing heart rate above 180 bpm. During sleep, vagal tone dominates, and heart rate may drop below 50 bpm. This dual-control architecture — one branch that slows and one that accelerates, each with different kinetics and receptor mechanisms — gives the cardiovascular system the flexibility to match cardiac output precisely to the body's metabolic demands moment by moment.
