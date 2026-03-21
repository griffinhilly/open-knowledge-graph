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

## Questions

```yaml
- question: "A patient has a tachycardia that starts and terminates abruptly, is precisely regular, and is permanently cured by catheter ablation of a specific pathway. Which arrhythmia mechanism does this most strongly suggest?"
  type: multiple-choice
  options:
    - "Reentry — a fixed anatomical circuit sustains the arrhythmia, and ablating the circuit eliminates it"
    - "Abnormal automaticity — an ectopic focus fires at a fixed rate and can be destroyed"
    - "Early afterdepolarizations — prolonged action potential duration creates triggered beats"
    - "Delayed afterdepolarizations — calcium overload drives a transient inward current"
  answer: 0
  explanation: "The clinical signature of reentry is abrupt onset and termination (the circuit either sustains or doesn't), precise regularity (the circus movement fires at a fixed rate), and curability by ablating the circuit. Automaticity produces more gradual warm-up and cool-down. Triggered activity requires preceding beats and tends to cluster in bursts rather than sustained regular tachycardia. Catheter ablation targeting a specific pathway is the definitive treatment for reentry, not for automaticity or triggered activity."

- question: "A region of myocardium damaged by scarring conducts impulses slowly but still conducts. An electrical wavefront reaches a fork where one path is healthy (fast conduction) and the damaged path is present. For reentry to be sustained, what must be true?"
  type: multiple-choice
  options:
    - "The damaged path must block the wavefront antegrade but allow retrograde conduction — unidirectional block — and the healthy path must recover before the retrograde wave returns"
    - "Both paths must block the wavefront, forcing it to restart from the SA node"
    - "The healthy path must be permanently refractory so all conduction goes through the slow path"
    - "The wavefront must split evenly between the two paths and collide at the far end"
  answer: 0
  explanation: "Reentry requires exactly two conditions working together: unidirectional block (the damaged path cannot conduct the wavefront in the normal direction) and slow conduction (the path conducts retrogradely slowly enough that the fast pathway has time to recover its excitability). If block were bidirectional, no retrograde conduction occurs. If conduction in the slow path were fast, the retrograde wave would arrive while the fast pathway is still refractory and extinguish. Both conditions must coexist."

- question: "Triggered activity, unlike abnormal automaticity, cannot arise spontaneously from rest — it always requires a preceding action potential to initiate."
  type: true-false
  answer: true
  explanation: "This is the defining mechanistic distinction. Triggered activity arises from afterdepolarizations — oscillations in membrane potential that follow an action potential. Early afterdepolarizations occur during the same action potential; delayed afterdepolarizations occur in phase 4 from calcium overload. Either way, they need a preceding beat to trigger. Automaticity, by contrast, is truly spontaneous: the cell depolarizes on its own during phase 4 without requiring a prior action potential, which is how the SA node normally initiates each heartbeat."

- question: "Abnormal automaticity and reentry share the same underlying mechanism — both arise from circular conduction through a damaged circuit — and therefore respond to the same treatments."
  type: true-false
  answer: false
  explanation: "These are completely different mechanisms. Reentry requires a circuit with unidirectional block and slow conduction; it is a property of tissue architecture and is cured by ablating the circuit. Abnormal automaticity is a property of individual cells that acquire spontaneous phase 4 depolarization — there is no circuit, just an ectopic pacemaker. Because the mechanisms differ, the treatments differ: catheter ablation targeting the circuit works for reentry; rate control, addressing the triggering metabolic state (e.g., correcting hypokalemia, stopping digoxin), or overdrive suppression addresses automaticity."

- question: "Why are both unidirectional block AND slow conduction both required for reentry to sustain, and what would happen if only one condition were present without the other?"
  type: short-answer
  answer: "Unidirectional block alone (without slow conduction): the wavefront would travel retrogradely through the blocked pathway and arrive at the far end before the fast pathway has recovered, finding it still refractory — the wavefront extinguishes. Slow conduction alone (without unidirectional block): the wavefront enters both paths simultaneously in the forward direction, they meet at the far end and collide, both extinguish because the entire circuit is refractory simultaneously. For reentry, unidirectional block ensures the circuit can be entered retrogradely, and slow conduction provides the time window for the previously activated tissue to recover excitability before the retrograde wave returns."
  explanation: "Think of it as a timing puzzle: the wavefront must arrive back at its starting point at exactly the right moment — after the tissue has recovered but before another sinus beat activates it. Unidirectional block creates the one-way entry; slow conduction provides the delay. Remove either and the timing fails."
```

## Explainer

From your cardiac conduction prerequisite, you know that a normal heartbeat starts at the SA node, propagates through the AV node and His-Purkinje system in a coordinated wave, and then the entire system resets before the next beat. An arrhythmia is any disruption of this orderly sequence. The three underlying mechanisms — **reentry**, **abnormal automaticity**, and **triggered activity** — each represent a fundamentally different kind of failure, and distinguishing them matters because they respond to different treatments.

Reentry is the most clinically important mechanism and requires the most careful conceptual work. Imagine the electrical wave reaching a fork in the road where two pathways connect the same two points. Normally the wave travels down both paths, they collide at the far end, and the circuit extinguishes — it cannot circle back because both ends are refractory. Now suppose one pathway has been damaged by scar tissue from a myocardial infarction. The wave travels normally down the fast pathway, reaches the far end, and tries to enter the damaged slow pathway retrogradely. If the slow pathway has recovered by the time the retrograde wave reaches it, the wave travels backward through it and re-excites the tissue it already passed — creating a **circus movement** that sustains itself indefinitely, producing a rapid, regular tachycardia. The two required conditions are **unidirectional block** (the damaged pathway cannot conduct antegrade) and **slow conduction** (enough time for the fast pathway to recover before the returning wave arrives). Ablating the slow pathway interrupts the circuit, which is why catheter ablation is curative for many reentrant arrhythmias.

**Abnormal automaticity** arises when cells that are not supposed to pace begin spontaneously depolarizing. Your action potential prerequisite established that phase 4 spontaneous depolarization is normally unique to SA and AV nodal cells. In pathological states — hypokalemia, ischemia, digitalis toxicity, or catecholamine excess — other cells can acquire this property. A focus in the atrium, ventricle, or AV junction fires at its own rate, competing with or overriding the SA node. Unlike reentry, this mechanism requires no circuit — it is simply an ectopic pacemaker. Rate is typically 60–100 bpm for junctional automaticity, 20–40 bpm for ventricular escape rhythms, and highly variable for accelerated idioventricular rhythms seen after reperfusion.

**Triggered activity** is conceptually distinct from both. It arises from **afterdepolarizations**: membrane potential oscillations that follow an action potential rather than arising independently. **Early afterdepolarizations (EADs)** occur during phase 2 or 3 when channels re-open prematurely from a prolonged action potential duration — the mechanism behind torsades de pointes in the setting of hypokalemia or QT-prolonging drugs. **Delayed afterdepolarizations (DADs)** occur during phase 4 from intracellular calcium overload: the sarcoplasmic reticulum misfires after the action potential, releasing calcium spontaneously, which the Na⁺/Ca²⁺ exchanger extrudes in exchange for inward sodium current — a transient inward current that can depolarize the membrane to threshold. If either type reaches threshold, it triggers a new action potential, which can trigger another, producing a run of tachycardia. The defining feature of triggered activity is that it requires a preceding beat to initiate — it cannot start from rest, unlike automaticity — which is why it is more common at fast rates (EADs) or short-long-short sequences (DADs).
