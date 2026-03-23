---
id: cardiac-output-stroke-volume-regulation
title: Cardiac Output and Stroke Volume Regulation
domain: biology
course: physiology
prerequisites:
- id: cardiac-cycle-and-heart-function
  type: hard
- id: heart-rate-control-autonomic-modulation
  type: soft
builds-toward:
- coronary-circulation-myocardial-oxygen
- blood-pressure-regulation
tags:
- cardiac
- hemodynamics
- output
- regulation
stage: formal-systems
status: draft
---

# Cardiac Output and Stroke Volume Regulation

## Core Idea
Cardiac output (CO = heart rate × stroke volume) must be continuously adjusted to maintain adequate blood pressure and match metabolic demands. Stroke volume is determined by three physiological factors: preload (the degree of ventricular filling and stretch), contractility (the intrinsic force of contraction independent of loading), and afterload (the resistance against which the ventricle ejects blood). The Frank-Starling mechanism states that within physiological ranges, increased preload increases stroke volume by optimizing sarcomere length and cross-bridge overlap. Sympathetic stimulation increases contractility by enhancing intracellular calcium handling.

## How It's Best Learned
Use echocardiography or cardiac catheterization to measure stroke volume and observe how controlled changes in preload (fluid administration or withdrawal), afterload (vasopressor or vasodilator drugs), or contractility (dobutamine or esmolol) affect it.

## Common Misconceptions
Cardiac output is not simply determined by heart rate; stroke volume changes are equally important, especially during exercise where both increase to produce large increases in CO.

## Questions

```yaml
- question: "An athlete's cardiac output increases fourfold from 5 L/min at rest to 20 L/min during intense exercise. Their heart rate doubles from 70 to 140 bpm. What must be true about stroke volume?"
  type: multiple-choice
  options:
    - "Stroke volume stayed the same at about 71 mL — doubling heart rate alone explains the fourfold increase in CO"
    - "Stroke volume decreased to about 35 mL, because faster heart rates reduce ventricular filling time"
    - "Stroke volume approximately doubled to about 143 mL, contributing equally with heart rate to the fourfold increase"
    - "Stroke volume quadrupled to about 285 mL, since cardiac output quadrupled"
  answer: 2
  explanation: "CO = HR × SV. At rest: 5,000 mL/min = 70 bpm × ~71 mL. During exercise: 20,000 mL/min = 140 bpm × SV, so SV ≈ 143 mL — roughly double. Both HR and SV approximately doubled. This illustrates the core misconception identified in the file: CO is not 'just heart rate.' A student who ignores SV would predict CO should only double (to ~10 L/min). During exercise, enhanced venous return (Frank-Starling), sympathetic contractility, and reduced afterload all simultaneously increase SV, contributing equally with heart rate to the fourfold rise."

- question: "A drug increases venous return by promoting venoconstriction. According to the Frank-Starling mechanism, what is the direct effect on stroke volume?"
  type: multiple-choice
  options:
    - "Stroke volume decreases, because higher venous pressure makes it harder for the ventricle to fill"
    - "Stroke volume increases, because greater ventricular stretch at end-diastole produces more forceful contraction"
    - "Stroke volume is unchanged; the heart compensates by slowing its rate to handle the extra volume"
    - "Stroke volume increases only if the sympathetic nervous system is simultaneously activated"
  answer: 1
  explanation: "The Frank-Starling mechanism is intrinsic to cardiac muscle: within physiological ranges, greater ventricular stretch at end-diastole (more preload) increases force of contraction and therefore stroke volume. More blood returning to the heart stretches the ventricular wall to a more optimal sarcomere length, enabling more actin-myosin cross-bridge formation. This is a built-in feedback loop — the heart automatically adjusts output to match venous return without any neural input. Option D is wrong: Frank-Starling operates intrinsically, independent of sympathetic activation (though sympathetic input can shift the Frank-Starling curve upward)."

- question: "The Frank-Starling mechanism operates intrinsically within cardiac muscle, allowing the heart to automatically match its output to venous return without neural or hormonal signals."
  type: true-false
  answer: true
  explanation: "Yes — this intrinsic property distinguishes Frank-Starling from contractility changes driven by sympathetic stimulation. A completely denervated (transplanted) heart still exhibits Frank-Starling behavior: greater end-diastolic stretch produces stronger contraction. The mechanism works at the sarcomere level: more stretch means more optimal overlap between actin and myosin filaments, producing more force per contraction. This automatic matching of output to input is also critical for equalizing left and right ventricular output — if one side pumps more than the other, the other side's preload rises and Frank-Starling brings it back into balance."

- question: "Because cardiac output equals heart rate multiplied by stroke volume, any increase in heart rate will necessarily increase cardiac output proportionally."
  type: true-false
  answer: false
  explanation: "This ignores the effect of heart rate on stroke volume. At very high heart rates (e.g., >180 bpm in certain arrhythmias), diastolic filling time is so shortened that the ventricle cannot fill adequately, and preload drops. By the Frank-Starling mechanism, reduced preload means reduced stroke volume. At extreme rates, the fall in SV can outweigh the HR increase, and CO actually declines despite the higher rate. In clinical practice, tachydysrhythmias can cause hemodynamic collapse precisely because CO falls when the heart rate is too high for adequate filling — the heart 'spins its wheels' without pumping effectively."

- question: "A patient with uncontrolled hypertension develops progressive heart failure over several years. Using preload, afterload, and contractility, explain the chain of events linking chronic hypertension to heart failure."
  type: short-answer
  answer: "Elevated blood pressure means chronically elevated afterload — the left ventricle must overcome higher aortic pressure with every beat. Initially the heart compensates by hypertrophy (thickening of the ventricular wall), which maintains stroke volume despite high afterload. However, hypertrophy becomes maladaptive: the thickened, stiff ventricle fills poorly during diastole (impaired relaxation reduces end-diastolic volume, decreasing preload and therefore SV via Frank-Starling). Meanwhile, myocardial remodeling impairs contractility — fewer functional sarcomeres, abnormal calcium handling, and interstitial fibrosis reduce intrinsic force of contraction. The result is a heart facing high afterload with diminished contractility and reduced preload-based reserve, failing to maintain adequate CO."
  explanation: "This sequence — pressure overload → hypertrophy → diastolic dysfunction → systolic dysfunction — is one of the most important disease mechanisms in cardiology. Treatment targets all three SV determinants: afterload reduction (ACE inhibitors, ARBs), preload optimization (diuretics), and contractility modulation (beta-blockers paradoxically, or digoxin). Each intervention corresponds directly to one leg of the preload-afterload-contractility triad."
```

## Explainer

From your study of the cardiac cycle, you know that the heart fills during diastole and ejects blood during systole. **Cardiac output** is simply the volume of blood the heart pumps per minute, calculated as heart rate multiplied by **stroke volume** — the amount ejected with each beat. A resting heart rate of 70 bpm and a stroke volume of 70 mL gives a cardiac output of about 5 L/min, which is roughly the entire blood volume circulated every minute. The question this topic addresses is: how does the heart adjust this output to match the body's changing metabolic demands?

The answer lies in three determinants of stroke volume. **Preload** is the degree to which the ventricle is stretched by blood at the end of diastole — essentially, how full the chamber is before it contracts. The **Frank-Starling mechanism** explains why preload matters: when more blood fills the ventricle, the cardiac muscle fibers are stretched to a more optimal length, producing more forceful contractions and a larger stroke volume. Think of it like stretching a rubber band — within a physiological range, more stretch means more snap-back force. This mechanism is intrinsic to the heart muscle itself and requires no neural input. It is what allows the heart to automatically match its output to venous return: if more blood flows back to the heart, the heart pumps more out.

**Contractility** (also called inotropy) is the force of contraction independent of how much the ventricle is stretched. Two hearts can have the same preload but different contractility. Sympathetic stimulation increases contractility by triggering norepinephrine release, which activates beta-1 adrenergic receptors on cardiac myocytes. This increases intracellular calcium availability during each contraction cycle — more calcium means more cross-bridge cycling between actin and myosin, producing a stronger contraction. The Frank-Starling curve effectively shifts upward: at the same preload, the heart ejects more blood. Conversely, heart failure is a state of reduced contractility where the curve shifts downward.

**Afterload** is the resistance the ventricle must overcome to eject blood, determined primarily by arterial blood pressure and vascular resistance. Higher afterload means the ventricle must generate more pressure before the aortic valve opens, leaving less energy for ejection and reducing stroke volume. Think of afterload as pushing against a heavy door — the harder it is to open, the less you get through. In clinical practice, chronically elevated afterload (as in uncontrolled hypertension) forces the heart to work harder with every beat, eventually leading to pathological hypertrophy. During exercise, cardiac output can increase four- to fivefold through the coordinated increase of heart rate (sympathetic activation and vagal withdrawal), preload (increased venous return from the muscle pump and venoconstriction), and contractility (sympathetic drive), while afterload may actually decrease slightly as skeletal muscle vasodilation reduces total peripheral resistance.
