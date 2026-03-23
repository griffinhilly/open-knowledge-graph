---
id: cardiac-anatomy-and-conduction
title: Cardiac Anatomy and the Electrical Conduction System
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: body-organization-and-terminology
  type: hard
- id: cardiac-cycle-and-heart-function
  type: hard
- id: action-potential
  type: hard
- id: cardiac-electrophysiology-action-potentials
  type: hard
builds-toward:
- blood-vessels-and-circulation
tags:
- heart
- conduction
- SA-node
- AV-node
- ECG
- chambers
- valves
stage: formal-systems
status: validated
---

# Cardiac Anatomy and the Electrical Conduction System

## Core Idea
The heart has four chambers (right and left atria and ventricles) separated by the AV valves (tricuspid and mitral) and semilunar valves (pulmonary and aortic), which enforce unidirectional blood flow through the pulmonary and systemic circuits. The intrinsic conduction system — sinoatrial (SA) node, atrioventricular (AV) node, bundle of His, bundle branches, and Purkinje fibers — generates and propagates action potentials that coordinate atrial and ventricular contraction. Cardiac muscle cells are connected by gap junctions at intercalated discs, allowing the myocardium to act as a functional syncytium. The ECG waveform (P, QRS, T) maps to specific events in the conduction cycle.

## How It's Best Learned
Trace the path of a single action potential through the conduction system and match each step to its ECG waveform. Use a cross-sectional heart diagram to identify chambers, valves, and great vessels simultaneously.

## Common Misconceptions
- The heart is not purely left-sided — it sits in the mediastinum with the apex tilted left but the base toward the right.
- The AV valves do not open 'actively'; they are pushed open and closed passively by pressure differentials.

## Questions

```yaml
- question: "Why does the AV node deliberately slow conduction before passing the impulse to the ventricles?"
  type: multiple-choice
  options:
    - "To prevent the ventricles from receiving too many electrical impulses per minute"
    - "To allow the atria time to finish contracting and push blood into the ventricles before ventricular contraction begins"
    - "Because the AV node is smaller than the SA node and physically conducts more slowly as a structural limitation"
    - "To allow the semilunar valves time to open before ventricular depolarization reaches them"
  answer: 1
  explanation: "The AV node delay (~0.1 seconds) is functionally critical: it gives the atria time to complete their contraction and deliver their final 'top-off' of blood into the ventricles before ventricular systole begins. If conduction were instantaneous, atria and ventricles would contract simultaneously, and atrial contraction would add little to ventricular filling. The fibrous skeleton forces all conduction through the AV node, making this delay non-bypassable — a design feature, not a limitation."

- question: "A patient's ECG shows a prolonged PR interval (0.28 s, normal < 0.20 s). This most likely indicates a problem at which anatomical location?"
  type: multiple-choice
  options:
    - "SA node — it is firing too slowly, lengthening the time between beats"
    - "AV node — conduction through it is delayed, prolonging the time from atrial to ventricular depolarization"
    - "Purkinje fibers — they are distributing ventricular depolarization too slowly"
    - "Ventricular myocardium — hypertrophy is slowing the spread of depolarization through the walls"
  answer: 1
  explanation: "The PR interval measures the time from the start of atrial depolarization (start of P wave) to the start of ventricular depolarization (start of QRS) — this interval spans the AV node delay. A prolonged PR interval means conduction through the AV node is slowed (first-degree AV block). SA node firing rate affects beat frequency, not the PR interval. A Purkinje problem would widen the QRS complex. This illustrates the diagnostic power of ECG anatomy: each interval maps to a specific structure."

- question: "The P wave on an ECG represents ventricular depolarization spreading rapidly through the Purkinje fiber network."
  type: true-false
  answer: false
  explanation: "The P wave represents atrial depolarization spreading from the SA node across the atrial muscle. Ventricular depolarization via the Purkinje network produces the QRS complex — its sharp, brief morphology reflects how efficiently the Purkinje system distributes the signal simultaneously across the ventricular walls. A wider-than-normal QRS indicates slower ventricular depolarization (e.g., bundle branch block), showing the direct relationship between conduction anatomy and ECG morphology."

- question: "The QRS complex is normally very brief because ventricular depolarization happens almost simultaneously throughout the ventricular walls, driven by the Purkinje fiber system."
  type: true-false
  answer: true
  explanation: "The Purkinje fiber network distributes depolarization rapidly and simultaneously to the entire endocardial surface of both ventricles. This near-simultaneous activation is what produces a brief, sharp QRS complex. When bundle branches are blocked, depolarization must spread cell-to-cell more slowly through ventricular muscle, producing a broader QRS. The width of the QRS is a direct ECG marker of how efficiently the Purkinje system distributes the impulse."

- question: "Explain why the heart beats in a coordinated sequence — atria first, then ventricles — and what structural feature enforces this timing."
  type: short-answer
  answer: "The fibrous skeleton of connective tissue electrically insulates the atria from the ventricles everywhere except the AV node. This forces all electrical conduction through the AV node, which introduces a deliberate ~0.1-second delay. The SA node fires first, spreading depolarization through the atria via gap junctions (P wave). The signal reaches the AV node, which delays before passing it down the bundle of His, bundle branches, and Purkinje fibers for rapid ventricular activation (QRS complex). This sequential architecture ensures atria contract first to fill ventricles, then ventricles contract to eject blood."
  explanation: "Without the insulating fibrous skeleton, depolarization could spread directly from atria to ventricles at any point, causing simultaneous contraction and defeating the purpose of separate chambers. The AV node is not merely a relay — it is the only gap in an otherwise insulating wall, and the delay it imposes is an essential functional feature."
```

## Explainer

Your prerequisite in cardiac electrophysiology established how individual cardiac muscle cells generate action potentials with a prolonged plateau phase that prevents tetanus and ensures a full mechanical contraction before the cell can be restimulated. Now the question is: how does a heart composed of billions of such cells beat in coordinated sequence rather than as a chaotic, independent riot of depolarizations? The answer is architectural — the heart is wired with a specialized **conduction system** that functions simultaneously as a pacemaker, a relay station with a deliberate delay, and a rapid distribution network.

The **sinoatrial (SA) node**, embedded in the right atrial wall near the superior vena cava, is the intrinsic pacemaker. It spontaneously depolarizes at 60–100 times per minute — faster than any other cardiac tissue — and therefore normally dictates heart rate. From the SA node, depolarization spreads through atrial muscle via **gap junctions at intercalated discs**, the structures that make the myocardium a **functional syncytium**: electrically coupled cardiomyocytes propagate the action potential cell-to-cell without synaptic delay, so the entire atrial mass contracts as a single coordinated unit. The resulting wave of atrial contraction sweeps inward and downward, pushing blood through the open AV valves — the **tricuspid** on the right and the **mitral** (bicuspid) on the left — into the ventricles. These valves open passively when atrial pressure exceeds ventricular pressure and close passively when the gradient reverses; no active mechanism is needed.

The depolarization wave cannot jump directly from atria to ventricles — a **fibrous skeleton** of connective tissue electrically insulates the two chambers except at one point: the **atrioventricular (AV) node**. This creates a deliberate delay of roughly 0.1 seconds, giving the atria time to fully contract and top off ventricular filling before ventricular contraction begins. The AV node passes the signal into the **bundle of His**, which splits into right and left **bundle branches** coursing down the interventricular septum. These terminate in the **Purkinje fiber** network, which fans rapidly across the endocardial surface of both ventricles. The Purkinje system distributes depolarization simultaneously to the entire ventricular wall, producing the coordinated, apex-to-base squeeze that ejects blood efficiently into the aorta and pulmonary trunk past the closed, then forcibly opened, **semilunar valves** (aortic and pulmonary).

The ECG maps each stage onto a waveform in real time. The **P wave** reflects atrial depolarization spreading from the SA node. The **PR interval** spans from atrial depolarization through the AV nodal delay — its duration reflects how long conduction through the AV node takes. The sharp, brief **QRS complex** reflects rapid ventricular depolarization via the Purkinje system; its brevity indicates how efficiently the conduction network distributes the signal. The **T wave** reflects ventricular repolarization. (Atrial repolarization occurs during this interval but is electrically masked by the QRS.) When any component of this system fails — SA node suppression causing an escape rhythm, AV nodal block lengthening the PR interval or causing dropped beats, bundle branch block broadening the QRS — the ECG waveform deforms in ways that map precisely back to the anatomy. Reading an ECG is, at bottom, reading the conduction system's anatomy through the electrical footprint it leaves on the body surface.
