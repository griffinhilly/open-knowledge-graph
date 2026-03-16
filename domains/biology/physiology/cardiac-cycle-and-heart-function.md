---
id: cardiac-cycle-and-heart-function
title: Cardiac Cycle and Heart Function
domain: biology
course: physiology
prerequisites:
- id: cardiovascular-system-overview
  type: hard
- id: action-potential
  type: soft
builds-toward:
- blood-pressure-regulation
tags:
- cardiac cycle
- systole
- diastole
- cardiac output
- conduction system
stage: abstract-reasoning
status: validated
---

# Cardiac Cycle and Heart Function

## Core Idea
The cardiac cycle is the sequence of mechanical events — ventricular contraction (systole) and relaxation (diastole) — constituting one heartbeat. Electrical conduction begins at the sinoatrial (SA) node in the right atrium, which spontaneously depolarizes (~70 times per minute), spreading excitation across the atria. The signal slows at the atrioventricular (AV) node (allowing atrial emptying), then accelerates through the bundle of His and Purkinje fibers to synchronize ventricular contraction from apex to base. Cardiac output (CO = stroke volume × heart rate) is regulated by the autonomic nervous system and circulating catecholamines to match metabolic demand. Frank-Starling's law states that greater end-diastolic filling stretches the myocardium and increases stroke volume.

## How It's Best Learned
Study the Wiggers diagram: plot atrial pressure, ventricular pressure, aortic pressure, ventricular volume, and ECG on a shared time axis. Identify exactly when the mitral and aortic valves open and close, when systole begins and ends, and how to read stroke volume from the volume curve. Trace the conduction pathway: SA node → AV node → bundle of His → left/right bundle branches → Purkinje fibers.

## Common Misconceptions
- Heart sounds ('lub-dub') are produced by valve closure, not by myocardial contraction — the first sound is mitral/tricuspid closure; the second is aortic/pulmonic closure.
- At very high heart rates, diastolic filling time shortens so severely that stroke volume falls, potentially reducing overall cardiac output despite faster rate.

## Questions

```yaml
- question: "During a stethoscope exam you hear two sounds: 'lub' and 'dub'. What physical events produce these sounds?"
  type: multiple-choice
  options: ["Ventricular contraction followed by ventricular relaxation", "Atrial contraction followed by ventricular contraction", "Closure of the mitral/tricuspid valves followed by closure of the aortic/pulmonic valves", "Opening of the AV valves followed by opening of the semilunar valves"]
  answer: 2
  explanation: "Heart sounds are caused by valve closure, not muscle contraction. S1 ('lub') is produced when the mitral and tricuspid valves close at the start of ventricular systole. S2 ('dub') is produced when the aortic and pulmonic valves close at the end of systole. This is a classic misconception: it feels intuitive that 'the heartbeat sound' comes from the heart muscle contracting, but the sounds come from the hydraulic snap of the valves."

- question: "Increasing heart rate always increases cardiac output."
  type: true-false
  answer: false
  explanation: "Cardiac output = stroke volume × heart rate. At very high heart rates, diastole is shortened so severely that the ventricles do not fill adequately, causing stroke volume to fall. If stroke volume decreases faster than heart rate increases, cardiac output can actually decline. This is why extreme tachycardia can be hemodynamically dangerous."

- question: "State Frank-Starling's law and explain why it is useful for matching cardiac output to metabolic demand."
  type: short-answer
  answer: "Frank-Starling's law states that the more the ventricle is stretched during diastolic filling (greater end-diastolic volume), the greater the force of the subsequent contraction and the larger the stroke volume."
  explanation: "This intrinsic mechanism means the heart automatically pumps out more blood when more returns to it — without requiring nervous system input. For example, during exercise, increased venous return stretches the myocardium, increasing stroke volume and therefore cardiac output. It also ensures the left and right ventricles remain balanced: if the right side pumps slightly more, the left receives more filling and responds with greater output."
```

## Explainer

You already know that action potentials drive muscle contraction. The heart is a specialized muscle, but it adds an important twist: it generates its own electrical impulses rather than waiting for orders from the brain. Understanding the cardiac cycle means following both the electrical events that trigger contraction and the mechanical events — pressure and volume changes — that actually move blood.

The cycle begins at the **sinoatrial (SA) node**, a cluster of pacemaker cells in the right atrium wall that spontaneously depolarize roughly 70 times per minute. The depolarization wave spreads across both atria, causing them to contract and push blood into the ventricles. The signal then converges on the **atrioventricular (AV) node**, which introduces a brief delay — critical because it allows the atria to finish contracting before the ventricles activate. From the AV node, the impulse travels rapidly down the bundle of His, splits into left and right bundle branches, and fans out through **Purkinje fibers** across the ventricular walls. This wiring ensures the ventricles contract from apex to base, efficiently squeezing blood upward into the aorta and pulmonary artery.

The mechanical events are best understood through the **Wiggers diagram**, which plots ventricular pressure, aortic pressure, ventricular volume, and the ECG on a shared timeline. **Systole** is the contraction phase: ventricular pressure rises, the aortic valve opens when ventricular pressure exceeds aortic pressure, and blood is ejected. **Diastole** is the relaxation phase: ventricular pressure falls, the aortic valve snaps shut (producing the second heart sound), and the ventricle refills. The volume difference between end-diastolic volume and end-systolic volume is the **stroke volume** — the amount ejected per beat. Multiply stroke volume by heart rate and you get **cardiac output**.

Two control mechanisms deserve emphasis. First, the **autonomic nervous system** modulates both rate and contractility: sympathetic stimulation (epinephrine) increases heart rate and force; parasympathetic stimulation (acetylcholine via the vagus nerve) slows the SA node. Second, the intrinsic **Frank-Starling mechanism** means the heart is self-regulating: the more blood returning from the veins stretches the ventricle during diastole, the harder the ventricle contracts on the next beat. This passive, muscle-length-dependent response ensures cardiac output automatically scales with venous return, without needing external signals.

The heart sounds — heard through a stethoscope — reflect valve mechanics, not the contractions themselves. The first sound ('lub', S1) is the snap of the mitral and tricuspid valves closing at the onset of systole. The second sound ('dub', S2) is the closure of the aortic and pulmonic valves at the end of systole. Abnormal sounds (murmurs) arise when valves leak or fail to open fully, creating turbulent flow that a trained clinician can interpret diagnostically.
