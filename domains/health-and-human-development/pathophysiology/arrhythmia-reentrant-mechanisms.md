---
id: arrhythmia-reentrant-mechanisms
title: 'Cardiac Arrhythmias: Reentry, Automaticity, and Triggered Activity'
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: cardiac-anatomy-and-conduction
  type: hard
- id: action-potential-initiation
  type: hard
builds-toward:
- atrial-fibrillation-pathophysiology
- sudden-cardiac-death-pathophysiology
tags:
- arrhythmia
- reentry
- automaticity
- triggered-activity
stage: advanced
status: draft
---

# Cardiac Arrhythmias: Reentry, Automaticity, and Triggered Activity

## Core Idea
Arrhythmias arise from three mechanisms: reentry (circular conduction block and recovery), abnormal automaticity (ectopic pacing), and triggered activity (afterdepolarizations). Reentry requires unidirectional block and slow conduction, often in scarred tissue; afterdepolarizations occur from calcium overload or hypokalemia.

## Explainer

From your cardiac conduction prerequisite, you know that a normal heartbeat starts at the SA node, propagates through the AV node and His-Purkinje system in a coordinated wave, and then the entire system resets before the next beat. An arrhythmia is any disruption of this orderly sequence. The three underlying mechanisms — **reentry**, **abnormal automaticity**, and **triggered activity** — each represent a fundamentally different kind of failure, and distinguishing them matters because they respond to different treatments.

Reentry is the most clinically important mechanism and requires the most careful conceptual work. Imagine the electrical wave reaching a fork in the road where two pathways connect the same two points. Normally the wave travels down both paths, they collide at the far end, and the circuit extinguishes — it cannot circle back because both ends are refractory. Now suppose one pathway has been damaged by scar tissue from a myocardial infarction. The wave travels normally down the fast pathway, reaches the far end, and tries to enter the damaged slow pathway retrogradely. If the slow pathway has recovered by the time the retrograde wave reaches it, the wave travels backward through it and re-excites the tissue it already passed — creating a **circus movement** that sustains itself indefinitely, producing a rapid, regular tachycardia. The two required conditions are **unidirectional block** (the damaged pathway cannot conduct antegrade) and **slow conduction** (enough time for the fast pathway to recover before the returning wave arrives). Ablating the slow pathway interrupts the circuit, which is why catheter ablation is curative for many reentrant arrhythmias.

**Abnormal automaticity** arises when cells that are not supposed to pace begin spontaneously depolarizing. Your action potential prerequisite established that phase 4 spontaneous depolarization is normally unique to SA and AV nodal cells. In pathological states — hypokalemia, ischemia, digitalis toxicity, or catecholamine excess — other cells can acquire this property. A focus in the atrium, ventricle, or AV junction fires at its own rate, competing with or overriding the SA node. Unlike reentry, this mechanism requires no circuit — it is simply an ectopic pacemaker. Rate is typically 60–100 bpm for junctional automaticity, 20–40 bpm for ventricular escape rhythms, and highly variable for accelerated idioventricular rhythms seen after reperfusion.

**Triggered activity** is conceptually distinct from both. It arises from **afterdepolarizations**: membrane potential oscillations that follow an action potential rather than arising independently. **Early afterdepolarizations (EADs)** occur during phase 2 or 3 when channels re-open prematurely from a prolonged action potential duration — the mechanism behind torsades de pointes in the setting of hypokalemia or QT-prolonging drugs. **Delayed afterdepolarizations (DADs)** occur during phase 4 from intracellular calcium overload: the sarcoplasmic reticulum misfires after the action potential, releasing calcium spontaneously, which the Na⁺/Ca²⁺ exchanger extrudes in exchange for inward sodium current — a transient inward current that can depolarize the membrane to threshold. If either type reaches threshold, it triggers a new action potential, which can trigger another, producing a run of tachycardia. The defining feature of triggered activity is that it requires a preceding beat to initiate — it cannot start from rest, unlike automaticity — which is why it is more common at fast rates (EADs) or short-long-short sequences (DADs).
