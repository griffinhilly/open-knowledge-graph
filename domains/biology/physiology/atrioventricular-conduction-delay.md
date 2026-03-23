---
id: atrioventricular-conduction-delay
title: Atrioventricular Node Conduction and Physiological Delay
domain: biology
course: physiology
prerequisites:
- id: cardiac-pacemaker-activity-sinoatrial-node
  type: hard
- id: action-potential-initiation
  type: soft
builds-toward:
- heart-rate-control-autonomic-modulation
- cardiac-output-stroke-volume-regulation
tags:
- cardiac
- conduction
- delay
- electrophysiology
stage: formal-systems
status: draft
---

# Atrioventricular Node Conduction and Physiological Delay

## Core Idea
The atrioventricular (AV) node introduces a critical ~0.1-second (100 ms) physiological delay in electrical conduction between atrial and ventricular depolarization. This delay exists because AV nodal cells have fewer fast sodium channels than ventricular myocytes and conduct action potentials much more slowly (~0.05 m/s vs. 1 m/s in ventricles). This delay is essential: it allows atrial contraction to complete and fully fill the ventricles before ventricular activation, optimizing ventricular preload and cardiac output. Pathological delays in AV conduction (first, second, or third-degree AV block) result in incomplete or absent ventricular depolarization and reduced cardiac output.

## How It's Best Learned
Observe the PR interval on electrocardiograms as the reflection of AV nodal conduction time. Study how drugs (digoxin, beta-blockers, calcium channel blockers) that slow AV conduction affect PR interval. Examine electrophysiology tracings showing slow conduction velocity in AV node tissue.

## Questions

```yaml
- question: "A patient's ECG shows a PR interval of 280 ms (normal < 200 ms) with every P wave followed by a QRS complex. Which condition does this most likely indicate, and what is its hemodynamic significance?"
  type: multiple-choice
  options:
    - "Third-degree AV block — atrial impulses are not reaching the ventricles, causing independent rhythms"
    - "First-degree AV block — conduction from atria to ventricles is prolonged but intact; usually hemodynamically benign"
    - "Bundle branch block — delayed conduction within the ventricles widens the PR interval"
    - "Wolff-Parkinson-White syndrome — accessory pathway shortens the PR interval"
  answer: 1
  explanation: "A prolonged PR interval with every P wave followed by a QRS indicates first-degree AV block: the impulse traverses the AV node slowly but eventually reaches the ventricles every time. This is generally benign because ventricular filling and cardiac output are not significantly impaired — the delay simply extends the PR interval beyond 200 ms. In third-degree block, P waves and QRS complexes are dissociated (no consistent relationship), not just delayed. Bundle branch block prolongs the QRS complex (intraventricular delay), not the PR interval. WPW actually shortens the PR interval via an accessory pathway."

- question: "Why does the AV node conduct action potentials at ~0.05 m/s — roughly twenty times slower than ventricular muscle — and why is this physiologically beneficial rather than a design flaw?"
  type: multiple-choice
  options:
    - "AV nodal cells lack mitochondria, reducing the energy available for rapid ion pumping"
    - "AV nodal cells use calcium-dependent action potentials rather than fast sodium channels, producing slow depolarization that creates a deliberate delay allowing atrial contraction to complete before ventricular activation"
    - "Slow AV conduction protects against arrhythmias by preventing re-entry into the atria"
    - "The AV node is anatomically narrow, and narrow pathways physically restrict conduction velocity"
  answer: 1
  explanation: "AV nodal cells have few fast voltage-gated sodium channels; their action potentials are primarily driven by L-type calcium channels, which open and close more slowly. This produces an intrinsically slow conduction velocity — a built-in physiological bottleneck. The benefit is precise timing: the ~100 ms pause ensures that the atria fully complete their contraction and deliver the 'atrial kick' (15–25% of end-diastolic volume) into the ventricles before ventricular depolarization begins. Without this delay, the ventricles would begin contracting before the atria finish filling them, wasting the contribution of atrial systole and reducing stroke volume."

- question: "The AV node delay is a mechanical limitation of cardiac tissue that evolution has failed to eliminate because it has no functional consequence for cardiac output."
  type: true-false
  answer: false
  explanation: "The AV delay is not an imperfection — it is functionally essential. The ~100 ms pause between atrial and ventricular depolarization allows the atria to complete their contraction and push the final portion of blood (the 'atrial kick') into the ventricles before the ventricles begin squeezing. This maximizes ventricular preload and, through the Frank-Starling mechanism, optimizes stroke volume and cardiac output. Elimination of this delay would cause the atria and ventricles to contract nearly simultaneously, wasting the atrial contribution to filling. The slow calcium-dependent conduction of AV nodal cells is the evolved mechanism that produces this beneficial delay."

- question: "In complete (third-degree) AV block, the atria and ventricles beat independently because no atrial impulses conduct through the AV node to the ventricles."
  type: true-false
  answer: true
  explanation: "In complete AV block, all atrial impulses are blocked at the AV node — none propagate to the ventricles. The ventricles then rely on an escape rhythm generated by cells in the bundle of His or below, which fire at an intrinsically slow rate (typically 30–50 bpm). The ECG shows P waves and QRS complexes that are completely dissociated — P waves march through at the atrial rate while QRS complexes occur at the much slower ventricular escape rate, with no consistent PR relationship. This dramatically reduces heart rate and cardiac output and typically requires permanent pacemaker implantation."

- question: "Explain why the 'atrial kick' requires the AV node delay in order to contribute meaningfully to ventricular filling."
  type: short-answer
  answer: "The atrial kick is the final surge of blood pushed into the ventricle when the atrium contracts. For this to increase ventricular preload, two conditions must be met simultaneously: the atrioventricular valves must still be open (so blood can flow from atria to ventricles), and the ventricles must not yet have begun contracting (so the incoming blood can actually increase end-diastolic volume rather than meeting a rising ventricular pressure). The AV node delay creates this window. After atrial depolarization, the electrical impulse slows to ~0.05 m/s in the AV node, taking ~100 ms to traverse it. During this pause, the atria complete their mechanical contraction and the additional blood enters the ventricles. Only after the signal passes through the AV node, bundle of His, and Purkinje fibers does ventricular contraction begin — by which time the atria are done and the ventricles are maximally filled. Without the delay, ventricular systole would begin during atrial contraction, closing the AV valves prematurely and eliminating the atrial kick's benefit."
```

## Explainer

You already know that the sinoatrial (SA) node generates the electrical impulse that initiates each heartbeat and that action potentials propagate through excitable tissue. The next critical question is: what happens between the moment the atria depolarize and the moment the ventricles contract? The answer is a deliberate bottleneck — the **atrioventricular (AV) node** — a small cluster of specialized cells at the junction between atria and ventricles that slows conduction to approximately 0.05 m/s, roughly twenty times slower than conduction through ventricular muscle. This produces the characteristic ~100 millisecond pause between atrial and ventricular activation.

The slow conduction exists because AV nodal cells rely primarily on **calcium channels** rather than the fast sodium channels that drive rapid depolarization in atrial and ventricular myocytes. Calcium-dependent action potentials rise more slowly and propagate with less velocity, creating a natural speed bump in the conduction pathway. Think of it like a highway narrowing to a single lane at a toll plaza: traffic (the electrical wave) must slow down before it can proceed. This is not a design flaw — it is precisely the point. Without this delay, the atria and ventricles would contract nearly simultaneously, and the atrial contraction that tops off ventricular filling would be wasted because the ventricles would already be squeezing.

The physiological payoff of this delay is **optimized ventricular preload**. During the pause, the atria complete their contraction and push the final 15–25% of blood into the ventricles — the so-called "atrial kick." By the time the electrical signal passes through the AV node and reaches the ventricles via the bundle of His and Purkinje fibers, the ventricles are maximally filled and ready to generate their most forceful contraction. This coordination directly increases stroke volume and therefore cardiac output, connecting the AV delay to the mechanical efficiency of every heartbeat.

When AV conduction becomes pathologically slow or blocked, the consequences are predictable from this framework. In **first-degree AV block**, every impulse still gets through but the delay is prolonged (PR interval > 200 ms) — usually benign. In **second-degree block**, some impulses fail to reach the ventricles entirely, producing dropped beats. In **third-degree (complete) block**, no atrial impulses conduct to the ventricles at all, and the ventricles must rely on a slow escape rhythm from cells below the block — a dangerous situation that often requires a pacemaker. Each degree of block represents progressive failure of the AV node's gating function, and the clinical severity maps directly to how much ventricular filling and cardiac output are compromised.
