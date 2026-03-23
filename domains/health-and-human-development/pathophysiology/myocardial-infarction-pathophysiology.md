---
id: myocardial-infarction-pathophysiology
title: Myocardial Infarction and Ischemia-Reperfusion Injury
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: atherosclerosis-pathophysiology
  type: hard
- id: coronary-circulation-anatomy
  type: hard
- id: necrosis-vs-apoptosis
  type: soft
- id: myocardial-contractility-mechanisms
  type: soft
builds-toward:
- post-infarction-ventricular-remodeling
- cardiogenic-shock
tags:
- myocardial-infarction
- acute-coronary-syndrome
- cardiac-ischemia
stage: expert
status: draft
---

# Myocardial Infarction and Ischemia-Reperfusion Injury

## Core Idea
Myocardial infarction results from acute coronary occlusion causing transmural or subendocardial necrosis. Ischemia initiates a cascade of metabolic derangement, calcium overload, and reactive oxygen species production; reperfusion paradoxically accelerates cell death through inflammation and apoptosis.

## How It's Best Learned
Study the temporal progression of necrosis (12–24 hours for full transmural involvement) and correlate with biomarker rise (troponin, CK-MB). Understand reperfusion injury as a distinct mechanism from ischemic injury.

## Common Misconceptions
Troponin elevation begins 2–4 hours post-infarction, not immediately—early angiography shows no enzyme change. Reperfusion is not uniformly beneficial; it can paradoxically increase mortality in certain settings.

## Questions

```yaml
- question: "A patient arrives in the emergency department 30 minutes after sudden-onset chest pain. Their initial troponin level is within normal limits. What is the correct clinical interpretation?"
  type: multiple-choice
  options:
    - "Acute MI is ruled out — troponin is the gold-standard biomarker and would be elevated immediately if significant necrosis were occurring"
    - "Acute MI cannot be ruled out — troponin typically rises 2–4 hours after infarct onset, so a normal value at 30 minutes is expected even with ongoing necrosis; serial troponins and ECG are required"
    - "The patient likely has unstable angina without infarction, since true MI always elevates troponin within 60 minutes of coronary occlusion"
    - "Normal troponin at 30 minutes confirms that any ischemia resolved before irreversible necrosis began"
  answer: 1
  explanation: "Troponin I and T are structural proteins bound to the cardiac contractile apparatus. When cardiomyocytes die by coagulative necrosis, these proteins must diffuse out of destroyed cells, through the interstitium, into lymphatics, and finally into the bloodstream. This process takes time — troponin typically becomes detectable 2–4 hours after infarct onset and peaks around 24 hours. A patient 30 minutes into an MI may have irreversible necrosis already underway but a completely normal initial troponin. Ruling out MI requires serial troponin measurements (at 0, 3, and 6 hours) plus clinical and ECG assessment."

- question: "What is the primary molecular mechanism by which reperfusion of ischemic myocardium causes additional cardiomyocyte death?"
  type: multiple-choice
  options:
    - "Re-oxygenation stops anaerobic glycolysis, suddenly depleting ATP and triggering a secondary energy crisis more severe than during ischemia"
    - "Re-oxygenation generates a burst of reactive oxygen species and triggers opening of the mitochondrial permeability transition pore (mPTP), collapsing the mitochondrial membrane potential and releasing cytochrome c to initiate apoptosis"
    - "Restored blood flow mechanically disrupts fragile cell membranes that were weakened by ischemic swelling, releasing DAMPs that amplify sterile inflammation"
    - "Reperfusion causes coronary vasospasm that re-occludes the infarct vessel within minutes, producing a second wave of ischemia"
  answer: 1
  explanation: "Ischemia allows Ca²⁺ to accumulate inside mitochondria. When oxygen is suddenly restored, ischemic mitochondria resume electron transport but generate a burst of reactive oxygen species (ROS) in the process. This ROS surge, combined with high mitochondrial Ca²⁺, triggers the mitochondrial permeability transition pore (mPTP) to open irreversibly. The mPTP collapses the proton gradient across the inner mitochondrial membrane, halting ATP synthesis and causing mitochondrial swelling. Cytochrome c is released into the cytoplasm, activating the caspase cascade and apoptosis. Cells viable at the moment of reperfusion die in the subsequent hours through this mechanism."

- question: "Restoring coronary blood flow (reperfusion) can cause death of cardiomyocytes that were still viable at the moment when flow was restored, through molecular mechanisms distinct from the original ischemic injury."
  type: true-false
  answer: true
  explanation: "This is the ischemia-reperfusion paradox. The net effect of reperfusion is almost always beneficial — salvaging far more myocardium than it kills. But a subset of cells that survived the ischemic period — stunned but not yet dead — are then killed by reperfusion itself. The mechanisms are distinct: ischemia kills primarily through ATP depletion and calcium overload causing coagulative necrosis. Reperfusion injury kills through ROS bursts, mPTP opening, and neutrophil-mediated inflammation causing apoptosis. This is why therapeutic strategies to block mPTP opening or scavenge ROS at the time of reperfusion (reperfusion cardioprotection) are an active research area."

- question: "Troponin begins to rise in the bloodstream within 10–15 minutes of coronary occlusion because cardiomyocyte membranes are disrupted as soon as ischemia begins."
  type: true-false
  answer: false
  explanation: "Troponin elevation is substantially delayed despite the fact that ischemia begins immediately and irreversible necrosis starts within 20–40 minutes. The delay occurs because troponin is a structural protein physically bound to the contractile apparatus inside the myocyte. Even after membrane disruption, troponin must diffuse through the cell, cross the interstitium, enter lymphatic channels, and then reach the venous circulation before becoming measurable in a blood sample. This diffusion takes 2–4 hours. Early normal troponin does not mean the heart is not infarcting — it means the necrosis products have not yet reached the bloodstream in detectable quantities."

- question: "Explain the ischemia-reperfusion paradox: why does restoring coronary blood flow cause additional cardiomyocyte death, and what are the key molecular mechanisms involved?"
  type: short-answer
  answer: "During ischemia, Ca²⁺ accumulates in cardiomyocytes and especially in mitochondria as the Na⁺/Ca²⁺ exchanger reverses and ATP-dependent pumps fail. When blood flow is restored, re-oxygenation of calcium-loaded mitochondria generates a burst of reactive oxygen species. High mitochondrial Ca²⁺ combined with ROS triggers the mitochondrial permeability transition pore (mPTP) to open irreversibly, collapsing the proton gradient and releasing cytochrome c to activate apoptosis. Additionally, neutrophils flooding the area with reperfusion add inflammatory injury. Cells that survived the ischemic period — still viable at the moment of reperfusion — die in subsequent hours through these mechanisms."
  explanation: "The paradox matters clinically because it sets a ceiling on how much reperfusion can help and motivates 'cardioprotection' strategies applied at the moment of reperfusion (e.g., ischemic postconditioning, cyclosporine to block mPTP). The key concept is that the same reoxygenation that rescues ATP production also triggers a burst of ROS from electron transport chains that have built up reduced intermediates during ischemia. The mitochondria are the site of both the problem (mPTP) and the solution (ATP restoration), which is why this injury is hard to prevent without also blocking beneficial reperfusion effects."
```

## Explainer

You've already studied how atherosclerotic plaque forms in coronary arteries — a process that narrows the lumen and stiffens the vessel wall over decades. Myocardial infarction is what happens when that slow process suddenly becomes acute. The precipitating event is almost always **plaque rupture or erosion**: the fibrous cap overlying a lipid-rich, necrotic atherosclerotic core tears, exposing the highly thrombogenic subendothelial contents to flowing blood. Within seconds, platelets adhere and activate at the rupture site; within minutes, the coagulation cascade generates fibrin; and within an hour, a fully occlusive thrombus can cut off perfusion to the downstream myocardium.

The **ischemic cascade** begins immediately after occlusion. Cardiomyocytes are obligate aerobic metabolizers with almost no glycogen reserve — they exhaust ATP within seconds to minutes of ischemia. Anaerobic glycolysis acidifies the cell, Na⁺/K⁺-ATPase fails as ATP is depleted, sodium accumulates intracellularly, and osmotic water influx causes cell swelling. The critical step in irreversible injury is **calcium overload**: as Na⁺/K⁺-ATPase fails, the Na⁺/Ca²⁺ exchanger reverses and floods the cell with calcium. Mitochondrial calcium overload activates destructive enzymes — phospholipases, proteases, endonucleases — and triggers mitochondrial permeability transition. Beyond approximately 20–40 minutes of complete ischemia, cardiomyocyte death by **coagulative necrosis** becomes irreversible. The wave of necrosis progresses from the subendocardium outward; complete transmural infarction takes 12–24 hours to develop fully.

**Ischemia-reperfusion injury** is the paradox at the heart of myocardial infarction treatment. When coronary blood flow is restored — by thrombolysis or percutaneous coronary intervention — there is unambiguous net benefit: salvaging living but stunned myocardium. But reperfusion also causes harm. Re-oxygenation of ischemic mitochondria generates a burst of reactive oxygen species. Calcium that accumulated during ischemia now enters mitochondria at high concentrations, triggering the **mitochondrial permeability transition pore (mPTP)** to open permanently, collapsing the proton gradient and releasing cytochrome c to initiate apoptosis. Neutrophil influx with reperfusion adds further inflammatory injury. The result is that some cells — viable at the moment of reperfusion — die in subsequent hours because of the reperfusion process itself, not the original ischemia.

The temporal sequence of **biomarker release** reflects the cellular destruction sequence directly. Troponin I and T are structural proteins bound to the cardiac contractile apparatus; they are released into the bloodstream as the cardiomyocyte membrane is destroyed. Because they must diffuse from dead cells into lymphatics and then blood, they don't rise until 2–4 hours post-infarction and peak at 24 hours. CK-MB (the cardiac isoform of creatine kinase) rises faster and clears faster, making it useful for detecting reinfarction. A patient presenting 30 minutes after chest pain onset may have a normal troponin despite active, ongoing infarction — the evolving troponin trend rather than any single value tells the story of necrosis progressing in real time.
