---
id: cardiac-arrhythmogenesis-mechanisms
title: Cardiac Arrhythmogenesis Mechanisms
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: action-potential
  type: hard
- id: cardiac-cycle-and-heart-function
  type: hard
builds-toward:
- myocardial-infarction-pathophysiology
tags:
- arrhythmia
- automaticity
- reentry
- early-after-depolarization
stage: expert
status: draft
---

# Cardiac Arrhythmogenesis Mechanisms

## Core Idea
Cardiac arrhythmias result from three mechanisms: abnormal automaticity (ectopic pacemakers firing faster than SA node), triggered activity (early after-depolarization from calcium overload or repolarization abnormalities, delayed after-depolarization from DAD), and reentry (circular conduction around anatomic or functional block). Structural disease (scar, fibrosis) and ion channel dysfunction (congenital long QT, short QT, Brugada) predispose to arrhythmias. Ischemia, acute inflammation, and electrolyte derangements trigger arrhythmias in structurally normal hearts.

## How It's Best Learned
Use action potential diagrams showing early (during repolarization) and delayed (after repolarization complete) after-depolarizations. Understand the reentry circuit requires unidirectional block and slow conduction. Study Vaughan-Williams classification of antiarrhythmic agents by their ion channel targets.

## Common Misconceptions
Automaticity does not require abnormal ion channels—any cell capable of reaching threshold can generate an ectopic rhythm. Reentry requires both unidirectional block AND slow conduction; fast conduction throughout the circuit prevents reentry. Long QT syndrome increases risk of torsade de pointes, not standard VT.

## Questions

```yaml
- question: "A patient's reentrant circuit has two pathways with fast and nearly equal conduction velocities, and neither pathway has unidirectional block. What will most likely happen to the electrical wavefront?"
  type: multiple-choice
  options:
    - "The circuit will sustain itself indefinitely, producing a tachyarrhythmia"
    - "The wavefront will traverse both pathways and collide in the middle, extinguishing the circuit"
    - "The faster pathway will develop unidirectional block, enabling reentry"
    - "The wavefront will conduct only down the slower pathway, creating a bradyarrhythmia"
  answer: 1
  explanation: "Reentry requires two conditions: unidirectional block in one pathway AND slow conduction in the other. Without these, wavefronts traveling down both pathways simultaneously will meet and collide — each wavefront encounters refractory tissue (the other wavefront's wake) and cannot continue. This collision-and-extinction is normal cardiac conduction. Reentry is only possible when these conditions break down specifically: one pathway blocks forward conduction, and the other is slow enough that the blocked pathway recovers before the circling wavefront arrives."

- question: "A patient with congenital long QT syndrome develops a polymorphic ventricular tachycardia that appears to 'twist' around the baseline on the ECG. Which arrhythmia mechanism is most directly responsible?"
  type: multiple-choice
  options:
    - "Delayed after-depolarizations from sarcoplasmic reticulum calcium overload"
    - "Abnormal automaticity in partially depolarized ventricular myocytes"
    - "Early after-depolarizations during prolonged phase 2/3 of the action potential"
    - "Reentry around a fixed anatomic scar"
  answer: 2
  explanation: "This is torsades de pointes, the characteristic arrhythmia of long QT syndrome. EADs occur when repolarization is prolonged — as in long QT — and L-type calcium channels recover and reactivate before the action potential fully repolarizes, creating a secondary upstroke. DADs (option A) occur after repolarization is complete and are associated with calcium overload from digoxin toxicity or catecholamine excess. The common misconception is that long QT causes standard monomorphic VT — it specifically predisposes to torsades via EADs."

- question: "Delayed after-depolarizations (DADs) are generated after repolarization is complete, driven by spontaneous calcium release from the sarcoplasmic reticulum activating the sodium-calcium exchanger."
  type: true-false
  answer: true
  explanation: "DADs arise after the action potential has fully repolarized. When sarcoplasmic calcium is overloaded (as in digoxin toxicity or excess catecholamines), the SR releases calcium spontaneously through ryanodine receptors. The NCX expels this calcium while importing sodium, generating a net inward current that can depolarize the cell to threshold — triggering an ectopic beat. This is distinct from EADs, which interrupt the action potential mid-repolarization."

- question: "Long QT syndrome increases risk of standard monomorphic ventricular tachycardia."
  type: true-false
  answer: false
  explanation: "Long QT syndrome predisposes specifically to torsades de pointes — a polymorphic VT that twists around the isoelectric baseline — via early after-depolarizations. Standard monomorphic VT is more typically associated with reentry around fixed anatomic scars (e.g., post-MI fibrosis). Understanding the specific arrhythmia mechanism matters clinically because treatment differs: QT-prolonging drugs worsen torsades, while antiarrhythmics targeting the reentry circuit address monomorphic VT."

- question: "Why does reentry require both unidirectional block AND slow conduction — why isn't either condition alone sufficient to sustain a reentrant circuit?"
  type: short-answer
  answer: "Unidirectional block alone is not enough because if conduction in the alternate pathway is fast, the circling wavefront arrives at the blocked pathway before it has recovered its excitability — it encounters refractory tissue and dies. Slow conduction alone is not enough because without unidirectional block, wavefronts traveling both directions will meet and extinguish. Both conditions must coexist: the block forces the wavefront to take the detour through the slow pathway, and the slow conduction gives the blocked pathway time to recover and become excitable again by the time the wavefront returns from behind. This timing window is what sustains the circuit indefinitely."
  explanation: "The reentry circuit is essentially a timing problem: the wavefront must arrive at the recovered pathway just as it becomes excitable again. Unidirectional block creates the directional asymmetry that forces the detour; slow conduction creates the time delay that allows recovery. Remove either and the circuit either self-terminates or never starts. This understanding explains why antiarrhythmic drugs that slow conduction or prolong refractoriness can interrupt reentry from two different directions."
```

## Explainer

Your understanding of the cardiac action potential is the foundation for everything here. Normal cardiac rhythm depends on the SA node acting as the dominant pacemaker because it depolarizes faster than any other cardiac tissue — its slope of phase 4 spontaneous depolarization is steepest. Arrhythmias arise when this hierarchy breaks down. The three mechanisms — abnormal automaticity, triggered activity, and reentry — are distinct failure modes of cardiac electrical architecture.

**Abnormal automaticity** arises when ischemia, hypoxia, or electrolyte abnormalities partially depolarize non-pacemaker cells. When the resting membrane potential drifts from −90 mV to approximately −60 mV, the funny current (If) and calcium channels that drive spontaneous depolarization begin to activate even in cells like ventricular myocytes that are normally quiescent. These cells then fire on their own schedule, generating **ectopic beats** that interrupt the SA node's rhythm. Hypercalemia and ischemia are classic triggers: both reduce the magnitude of the resting membrane potential, nudging cells into the range where automaticity is possible.

**Triggered activity** requires a preceding action potential — hence "triggered." It comes in two forms. **Early after-depolarizations (EADs)** occur during phase 2 or 3 of the action potential, when repolarization is prolonged (long QT) and the L-type calcium channels, which inactivated normally, can recover and reactivate before repolarization completes. The result is a secondary upstroke riding on the tail of the first action potential. EADs are the mechanism of **torsades de pointes** — a distinctive polymorphic ventricular tachycardia that "twists" around the baseline. **Delayed after-depolarizations (DADs)** occur after repolarization is complete, driven by calcium overload. When sarcoplasmic reticulum calcium is excessive (as in digoxin toxicity or catecholamine excess), spontaneous calcium release through ryanodine receptors drives the sodium-calcium exchanger to expel calcium while importing sodium, generating an inward current that can reach threshold and fire an ectopic beat.

**Reentry** is geometrically elegant and clinically the most common sustained arrhythmia mechanism. Imagine electrical wavefront traveling down two pathways around an anatomic obstacle (a scar, valve ring, or accessory pathway). In a normal heart, the wavefront meets in the middle after going around both paths and extinguishes — both pathways have similar conduction velocities and refractory periods. Reentry requires two conditions to coexist: **unidirectional block** in one pathway (the wavefront cannot go forward but can be entered from behind) and **slow conduction** in the other pathway (slow enough that by the time the wavefront traverses it, the blocked pathway has recovered its excitability). The wavefront then re-enters the blocked pathway retrograde and circles indefinitely, producing a sustained tachycardia. Ablation therapy destroys the circuit by eliminating one of the pathways; antiarrhythmic drugs interrupt reentry by either slowing conduction further (making the circuit too slow to sustain itself) or prolonging refractoriness (so the circuit never finds excitable tissue to re-enter). Understanding which mechanism underlies a particular arrhythmia directly determines which class of antiarrhythmic therapy is appropriate.
