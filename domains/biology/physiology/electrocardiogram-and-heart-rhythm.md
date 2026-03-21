---
id: electrocardiogram-and-heart-rhythm
title: Electrocardiogram and Cardiac Rhythm
domain: biology
course: physiology
prerequisites:
- id: cardiac-electrophysiology-action-potentials
  type: hard
- id: pacemaker-automaticity-sinoatrial-node
  type: soft
tags:
- ecg
- arrhythmia
- cardiac-conduction
stage: advanced
status: draft
---

# Electrocardiogram and Cardiac Rhythm

## Core Idea
The electrocardiogram (ECG) records the electrical activity of the heart on the body surface, translating the heart's electrical signals into a standardized waveform of P waves, QRS complexes, and T waves. Deviations from the normal ECG pattern reveal arrhythmias, conduction blocks, myocardial infarction, and electrolyte abnormalities.

## Questions

```yaml
- question: "A student describes the ECG as 'measuring the action potential of heart muscle cells.' What is the more accurate description?"
  type: multiple-choice
  options:
    - "The ECG measures the action potential of the SA node specifically, since it initiates each heartbeat"
    - "The ECG detects the sum of electrical activity across millions of cardiac cells, projected onto different lead axes on the body surface"
    - "The ECG measures the mechanical contraction force of the ventricles at each heartbeat"
    - "The ECG directly measures membrane potential changes in individual Purkinje fiber cells"
  answer: 1
  explanation: "No electrode on the body surface can detect the action potential of a single cell. The ECG records the vector sum of all simultaneous electrical activity across the entire heart, projected onto the axis of each lead. This is why a 12-lead ECG provides 12 different views of the same electrical events — each lead axis captures a different projection of the same summed activity. Understanding this prevents a common error: the ECG does not show what any single cell is doing, but what the whole heart is doing electrically at every instant."

- question: "A patient's ECG shows a PR interval of 280 ms (normal range: 120–200 ms). What does this most likely indicate?"
  type: multiple-choice
  options:
    - "The SA node is firing too rapidly, shortening the time for atrial conduction"
    - "There is a conduction delay at the AV node, slowing transmission of the impulse from atria to ventricles"
    - "The QRS complex is widened, indicating that ventricular depolarization is taking an abnormal pathway"
    - "Atrial fibrillation is present, causing chaotic P waves and irregular RR intervals"
  answer: 1
  explanation: "The PR interval measures the time from the onset of atrial depolarization (start of P wave) to the onset of ventricular depolarization (start of QRS). Most of this time reflects the deliberate delay in the AV node, which allows the atria to finish contracting and fill the ventricles before ventricular activation begins. A prolonged PR interval (> 200 ms) indicates first-degree AV block — slowed conduction through the AV node. Options C and D describe completely different ECG abnormalities: bundle branch block affects QRS duration, and atrial fibrillation produces no organized P waves at all."

- question: "The QRS complex is larger in amplitude than the P wave on the ECG because ventricular muscle mass is much greater than atrial muscle mass."
  type: true-false
  answer: true
  explanation: "The amplitude of an ECG deflection reflects the magnitude of the electrical dipole created by depolarizing myocardium. The ventricles, which must pump blood to the lungs and systemic circulation, have walls far thicker and more muscular than the atria. The QRS represents the simultaneous depolarization of this large ventricular mass, generating a much larger electrical signal than atrial depolarization. This anatomical relationship is why the QRS complex is the most prominent feature on the normal ECG."

- question: "Atrial repolarization produces a visible wave on the normal ECG, appearing between the T wave of one beat and the P wave of the next."
  type: true-false
  answer: false
  explanation: "Atrial repolarization does occur, but it is not normally visible on the ECG because it happens at the same time as ventricular depolarization — the QRS complex. The much larger electrical signal of ventricular depolarization completely obscures the much smaller atrial repolarization signal. This is an important distinction: the ECG does not show every electrical event in isolation; large signals mask coincident smaller ones. The T wave represents ventricular repolarization, not atrial."

- question: "Explain what each of the three main ECG deflections — the P wave, QRS complex, and T wave — represents in terms of the cardiac conduction sequence, and why the QRS complex is so much larger than the other deflections."
  type: short-answer
  answer: "The P wave represents atrial depolarization — the electrical wave spreading from the SA node across both atria, triggering atrial contraction. The QRS complex represents ventricular depolarization — the rapid propagation of the impulse through the bundle of His, bundle branches, and Purkinje fibers to activate the ventricular muscle, triggering the main pumping contraction. The T wave represents ventricular repolarization — ventricular cells returning to their resting membrane potential, resetting the myocardium for the next beat. The QRS is much larger than the P wave and T wave because the ventricular muscle mass is vastly greater than the atrial muscle mass; more cells depolarizing simultaneously create a larger summed electrical signal detectable at the body surface."
  explanation: "Note what is missing: there is no separate wave for atrial repolarization because it occurs simultaneously with ventricular depolarization (QRS) and is masked by the much larger ventricular signal. This illustrates a key principle: the ECG records the vector sum of all simultaneous activity, so large events obscure coincident small ones. Understanding the mapping between waves and conduction events is the foundation for interpreting every ECG abnormality."
```

## Explainer

You already understand that cardiac muscle cells generate action potentials and that these electrical signals propagate through the heart in a coordinated sequence starting from the SA node. The **electrocardiogram** (ECG or EKG) is the clinical tool that lets us observe this electrical activity from outside the body, using electrodes placed on the skin. It does not measure the action potential of any single cell — instead, it detects the sum of all electrical activity across millions of cardiac cells at each instant, projected onto different recording axes called **leads**. The standard 12-lead ECG provides twelve different "viewing angles" of the same electrical events, giving a comprehensive picture of how depolarization and repolarization sweep through the heart.

The normal ECG tracing has three main deflections that map directly onto the conduction sequence you already know. The **P wave** represents atrial depolarization — the electrical wave spreading from the SA node across both atria. The **QRS complex** represents ventricular depolarization — the rapid, powerful wave traveling through the bundle of His, bundle branches, and Purkinje fibers to activate the thick ventricular muscle. The QRS is much larger than the P wave because the ventricular muscle mass is far greater. The **T wave** represents ventricular repolarization — the recovery phase as ventricular cells return to their resting membrane potential. Atrial repolarization also occurs, but it is hidden within the larger QRS complex and is not normally visible.

The intervals between these waves carry critical diagnostic information. The **PR interval** (from the start of the P wave to the start of the QRS) reflects conduction time through the atria and AV node — normally 120–200 ms. A prolonged PR interval indicates a conduction delay at the AV node. The **QRS duration** (normally < 120 ms) reflects how quickly the ventricles depolarize; a widened QRS suggests a bundle branch block or abnormal conduction pathway. The **QT interval** (from QRS onset to the end of the T wave) represents the total time for ventricular depolarization and repolarization; prolongation increases the risk of dangerous arrhythmias.

The power of the ECG lies in pattern recognition. A missing P wave before a QRS complex suggests the impulse did not originate from the SA node — possibly an ectopic ventricular beat or atrial fibrillation. An irregularly irregular rhythm with no identifiable P waves is the hallmark of **atrial fibrillation**, where the atria quiver chaotically instead of contracting in an organized manner. ST segment elevation (the flat segment between the QRS and T wave being pushed upward) is a classic sign of acute **myocardial infarction** — injured ventricular muscle creates abnormal current flow that distorts this baseline. Each deviation from the normal pattern tells a specific physiological story, making the ECG one of the most information-dense diagnostic tools in medicine.
