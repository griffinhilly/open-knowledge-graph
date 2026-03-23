---
id: coronary-circulation-physiology
title: Coronary Circulation Physiology
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: cardiac-cycle-mechanics-and-function
  type: hard
- id: vascular-physiology-and-hemodynamics
  type: hard
builds-toward:
- coronary-artery-disease-acute-events
tags:
- coronary-flow
- autoregulation
- metabolic-demand
- perfusion-pressure
stage: formal-systems
status: validated
---

# Coronary Circulation Physiology

## Core Idea
The coronary circulation supplies oxygen-rich blood to the myocardium. Coronary flow is restricted during systolic compression of vessels and primarily occurs in diastole when ventricular pressure drops. Metabolic autoregulation ensures coronary flow matches the heart's metabolic demand for oxygen, which increases with contractility, heart rate, and wall stress.

## Questions

```yaml
- question: "A patient with significant coronary artery disease develops rapid atrial fibrillation with a ventricular rate of 140 bpm, compared to their resting rate of 70 bpm. Why is this particularly dangerous for coronary perfusion?"
  type: multiple-choice
  options:
    - "Higher heart rates reduce aortic systolic pressure, decreasing the driving force for coronary flow"
    - "Tachycardia both increases myocardial oxygen demand and shortens diastole — the phase when coronary perfusion primarily occurs — simultaneously reducing supply"
    - "Rapid rates cause the coronary arteries to spasm, mechanically obstructing flow independent of the cardiac cycle"
    - "Higher heart rates increase LVEDP, which dilates the ventricle and compresses the coronary arteries from inside"
  answer: 1
  explanation: "Tachycardia creates a double jeopardy for the ischemic heart. First, the increased heart rate elevates myocardial oxygen demand (demand side). Second, when heart rate doubles, the cardiac cycle halves — but systole shortens only slightly, so diastole is disproportionately compressed. Since left coronary flow primarily occurs during diastole (systolic compression restricts subendocardial vessels), less diastolic time means less perfusion time. A diseased vessel that can barely meet resting demand faces both increased need and reduced delivery time simultaneously."

- question: "Which of the following changes would most directly REDUCE coronary perfusion pressure?"
  type: multiple-choice
  options:
    - "An increase in heart rate from 60 to 90 bpm during mild exercise"
    - "A rise in aortic diastolic pressure from 80 to 90 mmHg"
    - "A fall in aortic diastolic pressure combined with a rise in left ventricular end-diastolic pressure (LVEDP)"
    - "An increase in coronary vasodilation driven by adenosine release"
  answer: 2
  explanation: "Coronary perfusion pressure ≈ aortic diastolic pressure − LVEDP. Anything that lowers aortic diastolic pressure (hypotension, aortic regurgitation) or raises LVEDP (heart failure, volume overload) narrows this gradient and reduces coronary flow. Option C describes both changes occurring simultaneously — the worst scenario, which occurs in decompensated heart failure or severe aortic regurgitation. Options A and B do not directly reduce the perfusion pressure gradient. Option D (vasodilation) increases flow by reducing resistance, not by changing pressure."

- question: "Coronary flow reserve refers to the heart's ability to increase coronary blood flow above resting levels in response to increased metabolic demand."
  type: true-false
  answer: true
  explanation: "Coronary flow reserve is the ratio of maximal coronary flow (during peak vasodilation, e.g., during exercise or pharmacologic stress) to resting flow — normally four to five times resting levels. It represents the vasodilatory capacity held in reserve. A significant stenosis may not reduce resting flow (because autoregulatory vasodilation compensates) but will erode coronary flow reserve, producing ischemia only under stress. This is why exercise stress testing can detect coronary disease that is invisible at rest."

- question: "Because both ventricles contract during systole, the right and left coronary arteries are equally compressed during systole and deliver similar flow patterns throughout the cardiac cycle."
  type: true-false
  answer: false
  explanation: "The right and left coronary arteries behave very differently. The left ventricle generates 120 mmHg or more during systole — enough to compress the subendocardial vessels nearly shut, so left coronary flow primarily occurs during diastole. The right ventricle develops much lower pressures (25–30 mmHg), so right coronary vessels are less compressed and receive flow throughout the cardiac cycle. This asymmetry explains why the left ventricular subendocardium is most vulnerable to ischemia, and why conditions that shorten diastole or reduce aortic diastolic pressure affect the left heart disproportionately."

- question: "Why is the left ventricular subendocardium the region most vulnerable to ischemic injury during episodes of reduced coronary perfusion?"
  type: short-answer
  answer: "The subendocardium (innermost layer of the left ventricular wall) is the last region to receive blood and the first to be deprived. During systole, high left ventricular pressure compresses the intramyocardial coronary vessels against the ventricular wall from inside, with the greatest compression in the subendocardium closest to the high-pressure cavity. This means subendocardial vessels are essentially occluded during systole and rely entirely on diastolic flow — a shorter window than the epicardial vessels experience. Additionally, the subendocardium has the highest metabolic demand (it works hardest, stretches most during contraction), so its oxygen extraction is already near maximum. When coronary perfusion pressure drops or diastolic time shortens, the subendocardium loses its supply first and has the least reserve."
  explanation: "This explains the characteristic pattern of ischemia seen on electrocardiograms (subendocardial ST depression) and why conditions like tachycardia, hypotension, and elevated LVEDP produce subendocardial ischemia before transmural infarction. It also explains why the subendocardial zone is the first region affected in demand-ischemia scenarios (e.g., hypertensive hypertrophy, aortic stenosis) — the region with the highest demand and most restricted supply is always the first to fail."
```

## Explainer

The heart faces a paradox that no other organ encounters: during systole, when ventricular muscle contracts most forcefully and needs oxygen most urgently, the pressure it generates simultaneously squeezes its own blood supply nearly shut. From your study of the cardiac cycle, you know that the left ventricle develops 120 mmHg or more during systole — enough to compress the subendocardial coronary vessels against the ventricular wall. This means the left coronary artery does most of its work during **diastole**, when ventricular pressure drops and the vessels can open. The right ventricle, which develops much lower pressures, has less of this problem and receives flow throughout the cycle.

This diastolic dependence has an important clinical consequence: **heart rate directly steals diastolic time**. When heart rate rises from 70 to 140 beats per minute, the cardiac cycle halves — but systole shortens only a little, so most of the time lost comes from diastole. Less diastole means less filling time and, critically, less coronary perfusion time. This is why tachycardia is particularly dangerous in patients with coronary artery disease: the heart demands more oxygen (higher rate) at the same moment it receives less delivery (shorter diastole).

The coronary vasculature responds to this changing demand through **metabolic autoregulation**. When myocardial oxygen extraction rises — which happens whenever contractility increases, wall stress rises, or heart rate climbs — local metabolic byproducts (adenosine, CO₂, H⁺, K⁺) accumulate and trigger **coronary vasodilation**. The vessels dilate in proportion to metabolic need, increasing flow up to four or five times resting levels during peak exercise. This is called **coronary flow reserve**, and its erosion is an early sign of disease: a vessel with 70% stenosis may deliver adequate flow at rest but cannot vasodilate sufficiently during exercise, producing ischemia under stress.

**Perfusion pressure** is the final piece. Coronary perfusion pressure is roughly aortic diastolic pressure minus left ventricular end-diastolic pressure (LVEDP). From your vascular physiology prerequisite, recall that flow depends on the pressure gradient across a vessel. If aortic diastolic pressure falls (hypotension, aortic regurgitation) or LVEDP rises (heart failure, volume overload), the gradient narrows and coronary flow falls. This is why hypotension is immediately dangerous in coronary artery disease, and why elevated filling pressures in heart failure compound myocardial ischemia — the heart is both volume-overloaded and underperfused simultaneously.
