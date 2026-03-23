---
id: cardiac-electromechanics-and-performance
title: Cardiac Electromechanics and Performance
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: cardiac-anatomy-and-conduction
  type: hard
- id: cardiac-muscle-anatomy-and-properties
  type: hard
- id: action-potential
  type: hard
builds-toward:
- cardiac-cycle-mechanics-and-function
- cardiac-output-regulation
tags:
- cardiac-cycle
- electrophysiology
- contraction
- coronary-perfusion
stage: formal-systems
status: draft
---

# Cardiac Electromechanics and Performance

## Core Idea
The heartbeat couples electrical excitation to mechanical contraction: sinoatrial node pacing spreads through atria, atrioventricular node delay allows atrial filling, then rapid conduction through His bundle enables synchronized ventricular contraction. The cardiac action potential has a prolonged plateau due to calcium influx, ensuring complete ventricular emptying before repolarization.

## Questions

```yaml
- question: "A researcher applies rapid electrical stimuli to cardiac muscle at a frequency that would cause skeletal muscle to enter sustained tetanic contraction. What happens to the cardiac muscle?"
  type: multiple-choice
  options:
    - "The heart tetanizes, producing a sustained contraction that maximizes blood ejection"
    - "The heart cannot be tetanized because the absolute refractory period lasts nearly as long as each contraction"
    - "The heart rate increases proportionally with stimulus frequency, improving cardiac output"
    - "The plateau phase shortens to accommodate the higher stimulation rate"
  answer: 1
  explanation: "The cardiac action potential's prolonged plateau phase creates an absolute refractory period that lasts nearly as long as the mechanical contraction itself. The heart physically cannot be re-excited until relaxation is nearly complete, making tetanic contraction impossible. Unlike skeletal muscle, which can be summated into tetanus, the heart has a mandatory relaxation (and therefore filling) phase built into every beat. Option A is the key misconception: sustained contraction would stop circulation entirely, not enhance it."

- question: "If the AV node delay were eliminated and the electrical signal traveled from the SA node directly to the ventricles without slowing, what would be the primary consequence?"
  type: multiple-choice
  options:
    - "Cardiac output would increase because faster conduction would allow a higher heart rate"
    - "The ECG waveform would change, but mechanical performance would be unaffected"
    - "Ventricular contraction would begin before the atria finish filling the ventricles, reducing stroke volume"
    - "The SA node would compensate by slowing its firing rate to restore normal timing"
  answer: 2
  explanation: "The ~100 ms AV node delay is a deliberate design feature that gives the atria time to complete their contraction and push blood through the mitral and tricuspid valves before the ventricles activate. Without this delay, ventricular contraction would begin prematurely—before atrial emptying is complete—reducing ventricular end-diastolic volume and therefore stroke volume. The AV node delay is not a conduction flaw to be overcome; it is a functional necessity for coordinated chamber sequencing."

- question: "The prolonged plateau phase of the cardiac action potential is caused primarily by sustained calcium influx through L-type voltage-gated calcium channels."
  type: true-false
  answer: true
  explanation: "Correct. After the initial rapid depolarization driven by sodium influx, L-type (long-lasting) voltage-gated calcium channels open and remain open for 200–300 milliseconds, sustaining a positive membrane voltage far longer than in neurons or skeletal muscle. This calcium influx serves a dual purpose: it directly triggers calcium-induced calcium release (CICR) from the sarcoplasmic reticulum, and by prolonging the action potential, it creates the long absolute refractory period that prevents tetanic contraction."

- question: "Cardiac muscle cells can be driven into sustained tetanic contractions by applying electrical stimuli at sufficiently high frequency, just as skeletal muscle can."
  type: true-false
  answer: false
  explanation: "False—and the difference is physiologically critical. Skeletal muscle can be summated into tetanus because its action potential is brief and repolarization occurs well before the mechanical contraction ends, allowing re-excitation before relaxation. Cardiac muscle's absolute refractory period lasts nearly as long as the contraction itself because the plateau phase keeps the membrane depolarized until the muscle is nearly finished contracting. The heart cannot be re-excited early enough to summate contractions, and tetanus would be immediately fatal by stopping ventricular filling."

- question: "Why does the cardiac action potential have a plateau phase, and what two functional consequences does this plateau produce for cardiac performance?"
  type: short-answer
  answer: "The plateau is caused by sustained opening of L-type calcium channels, which maintain a positive membrane potential for 200–300 ms after initial depolarization. Two functional consequences: (1) excitation-contraction coupling—calcium entering via L-type channels triggers CICR from the sarcoplasmic reticulum, flooding the cytoplasm with calcium that enables cross-bridge formation and forceful contraction; (2) a long absolute refractory period that prevents tetanic contraction, ensuring the heart relaxes and refills with blood between every beat."
  explanation: "Students often name the plateau without recognizing it serves both purposes simultaneously. The calcium influx IS the trigger for mechanical contraction via CICR. The prolonged depolarization IS the mechanism that makes cardiac muscle incapable of tetanus. Both consequences follow from the same plateau, which is why the cardiac action potential is so different from the brief spikes in neurons or skeletal muscle."
```

## Explainer

You already know that the action potential is a rapid, stereotyped change in membrane voltage driven by ion channel opening — first sodium rushes in, then potassium rushes out, restoring the resting potential. The cardiac action potential follows the same basic logic, but with one crucial difference: the **plateau phase**. After initial depolarization, L-type voltage-gated calcium channels open and remain open for 200–300 milliseconds, sustaining a positive membrane voltage much longer than in neurons or skeletal muscle. This plateau is what couples electricity to mechanics and, just as importantly, prevents the heart from going into tetanic (sustained) contraction.

The electrical signal originates in the **sinoatrial (SA) node**, a cluster of cells in the right atrium that depolarize spontaneously — they are the heart's pacemaker. The signal spreads through the atria via gap junctions, reaching the **atrioventricular (AV) node**, where conduction slows dramatically. This ~100 ms delay is not a flaw; it is a design feature. It gives the atria time to complete their contraction and push blood through the mitral and tricuspid valves into the ventricles before the ventricles themselves activate. After the AV node, the signal accelerates through the **Bundle of His** and its branches into the **Purkinje fiber** network, which distributes the signal rapidly across the ventricular walls. This ensures the ventricles contract nearly simultaneously, starting at the apex (bottom) and sweeping upward — a wringing motion that efficiently ejects blood into the aorta and pulmonary artery.

**Excitation-contraction coupling** is the bridge between the action potential and muscle shortening. As your study of cardiac muscle properties prepared you to understand, cardiomyocytes rely on **calcium-induced calcium release (CICR)**: calcium entering through the L-type channels during the plateau triggers the ryanodine receptors on the sarcoplasmic reticulum to release a much larger calcium flood into the cytoplasm. This cytoplasmic calcium binds troponin C, unblocking tropomyosin and allowing myosin heads to form cross-bridges with actin filaments. The more calcium released, the more cross-bridges form and the greater the force of contraction — a relationship called the **Frank-Starling mechanism** at the cellular level.

The prolonged plateau has an important protective consequence: the **absolute refractory period** lasts almost as long as the contraction itself. Unlike skeletal muscle, which can be summated into tetanus with rapid stimulation, the heart cannot be re-excited until relaxation is nearly complete. This means the heart has a mandatory filling phase between every beat, preventing the catastrophic scenario of sustained contraction that would stop blood from circulating. Understanding this coupling from electrical event to mechanical output — and the safeguards built into it — forms the conceptual foundation for everything you will learn about the cardiac cycle, output regulation, and arrhythmias.
