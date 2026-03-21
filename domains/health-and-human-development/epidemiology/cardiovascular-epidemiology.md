---
id: cardiovascular-epidemiology
title: Cardiovascular Disease Epidemiology
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: chronic-disease-epidemiology
  type: hard
- id: epidemiologic-study-designs
  type: soft
- id: disease-frequency-measures
  type: soft
tags:
- cardiovascular-disease
- risk-prediction
- prevention
stage: advanced
status: draft
---

# Cardiovascular Disease Epidemiology

## Core Idea
Cardiovascular disease epidemiology focuses on distinct subtypes (coronary heart disease, stroke, heart failure) with different etiologies, pathways, and prevention strategies. Risk prediction models integrate multiple risk factors (hypertension, lipids, smoking, diabetes) and population-specific baseline risks. Biomarkers (troponin, natriuretic peptides, C-reactive protein) improve risk stratification. Prevention emphasizes modifiable risk factors with strong dose-response relationships. Surveillance of CVD incidence and mortality tracks temporal trends and disparities to guide population health strategies.

## Questions

```yaml
- question: "A new blood biomarker strongly predicts cardiovascular events in a large cohort study (p < 0.001, hazard ratio 2.4). A hospital committee concludes it should be added to routine screening. Which response best identifies the flaw in this reasoning?"
  type: multiple-choice
  options:
    - "The hazard ratio is too small to be clinically meaningful"
    - "A p-value below 0.001 does not indicate statistical significance"
    - "Statistical association with outcomes does not prove the biomarker improves risk classification beyond existing models"
    - "Cohort studies cannot be used to validate biomarkers because they lack randomization"
  answer: 2
  explanation: "The key distinction is between statistical association and clinical utility. A biomarker can strongly predict outcomes yet add nothing beyond what the Framingham Risk Score or Pooled Cohort Equations already classify. Clinical usefulness requires demonstrating discrimination (correctly separating high-risk from low-risk patients) and reclassification improvement — moving people into different risk categories in ways that change management. Many biomarkers that looked promising on hazard ratios failed this more demanding test."

- question: "A 35-year-old and a 65-year-old both have a relative risk of 3.0 for coronary heart disease due to hypertension. For which patient does treating the hypertension prevent more absolute events per 100 people treated?"
  type: multiple-choice
  options:
    - "The 35-year-old, because they have more life-years ahead"
    - "The 65-year-old, because their higher baseline risk means the same relative elevation represents far more absolute events"
    - "Both equally, because the relative risk is identical"
    - "The 35-year-old, because hypertension does more cumulative damage in young arteries"
  answer: 1
  explanation: "This is the crucial distinction between relative and absolute risk. If the 35-year-old has a 10-year baseline CHD risk of 2%, a relative risk of 3.0 raises that to 6% — an absolute increase of 4 percentage points. If the 65-year-old has a baseline risk of 20%, the same relative risk of 3.0 raises that to 60% — an absolute increase of 40 percentage points. Treating 100 people in the first group prevents ~4 events; treating 100 in the second prevents ~40. Absolute risk, not relative risk, determines the cost-benefit calculus of clinical intervention."

- question: "A researcher studying 'cardiovascular disease' mortality should ideally analyze coronary heart disease, stroke, and heart failure as a single combined outcome to maximize statistical power."
  type: true-false
  answer: false
  explanation: "Lumping CVD subtypes obscures important subtype-specific differences. Atrial fibrillation is a powerful stroke risk factor but weakly linked to CHD; LDL cholesterol strongly predicts CHD but is a weaker predictor of hemorrhagic stroke; heart failure often occurs downstream of prior CHD or hypertension. Combining these into one outcome can mask heterogeneous associations and lead to incorrect conclusions about which risk factors matter for which diseases."

- question: "Atrial fibrillation is a stronger independent risk factor for ischemic stroke than for coronary heart disease."
  type: true-false
  answer: true
  explanation: "Atrial fibrillation causes cardioembolic stroke — irregular electrical activity leads to blood pooling and clot formation in the atria, which can travel to cerebral arteries. This mechanism is specific to the stroke pathway. While AF can contribute to heart failure, it is not a major independent risk factor for atherosclerotic coronary disease in the same way. This is why stroke risk assessment tools (CHA₂DS₂-VASc) weight AF heavily, while Framingham CHD scores do not include it as a primary input."

- question: "Why must cardiovascular epidemiologists analyze CVD subtypes separately rather than treating cardiovascular disease as a single unified disease category?"
  type: short-answer
  answer: "CVD subtypes have distinct etiologies, risk factor profiles, and pathophysiological mechanisms. Coronary heart disease is driven by atherosclerotic plaque in coronary arteries; ischemic stroke by thromboembolic events in cerebral vasculature; hemorrhagic stroke by vessel rupture; heart failure often by downstream effects of prior CHD or hypertension. Risk factors like LDL cholesterol, atrial fibrillation, and hypertension have different magnitudes of effect across subtypes. Pooling them hides these differences and can produce misleading estimates of which exposures matter — and for whom."
  explanation: "Subtype-specific analysis is essential because an intervention optimized against 'CVD' might be excellent for one subtype and harmful or irrelevant for another. Statins markedly reduce CHD and ischemic stroke risk but have little effect on hemorrhagic stroke. Blood thinners for AF dramatically cut stroke risk but add bleeding risk. Epidemiological rigor requires matching the outcome to the mechanism being studied."
```

## Explainer

From your study of chronic disease epidemiology, you know that non-communicable diseases are defined by their long latency, multifactorial causation, and preventability — and cardiovascular disease (CVD) is the paradigm case. It is the leading cause of death globally, but it is also the domain where epidemiology has arguably had its greatest public health success: the dramatic decline in CVD mortality in high-income countries over the past five decades tracks almost perfectly with the identification and management of modifiable risk factors that epidemiologists discovered and quantified.

The first conceptual move is to recognize that "cardiovascular disease" is not one disease. **Coronary heart disease (CHD)** — angina, myocardial infarction — results from atherosclerotic obstruction of the coronary arteries. **Stroke** comes in two forms: ischemic (a clot blocks cerebral blood flow) and hemorrhagic (a vessel ruptures). **Heart failure** is a failure of the pump itself, often downstream of prior CHD or hypertension. These subtypes share some risk factors but differ in others — atrial fibrillation is a powerful stroke risk factor but less directly linked to CHD; LDL cholesterol is a strong predictor of CHD but a weaker predictor of hemorrhagic stroke — so lumping them together in an analysis can obscure important subtype-specific patterns.

**Risk prediction models** are the applied translation of CVD epidemiology. Pooling data from large cohort studies, epidemiologists derived multivariate models — the Framingham Risk Score, the Pooled Cohort Equations — that integrate age, sex, blood pressure, cholesterol, smoking status, and diabetes to estimate 10-year absolute risk of a cardiovascular event. These models embody a key lesson from your earlier study of disease frequency measures: absolute risk, not relative risk, drives clinical decisions. A relative risk of 2.0 for a risk factor means something very different in a 30-year-old (whose baseline 10-year risk might be 1%) versus a 60-year-old (whose baseline might be 15%). The same relative elevation doubles to 2% versus 30% — the treatment calculus differs accordingly.

**Biomarkers** refine risk stratification beyond traditional factors. Cardiac troponins are released when myocardial cells are damaged — even subclinical elevations below the diagnostic threshold for myocardial infarction predict future events. Natriuretic peptides (BNP, NT-proBNP) rise when cardiac walls are under stretch, flagging early heart failure. C-reactive protein, a marker of systemic inflammation, improves risk prediction in people with intermediate Framingham scores where the treatment decision is otherwise ambiguous. The epidemiological validation of a biomarker requires demonstrating that it adds **discrimination** (moves people between risk categories) and **reclassification improvement** beyond existing models — not merely that it correlates with outcomes. This is a more demanding standard than simple association, and it highlights the difference between a biomarker that is statistically significant and one that is clinically useful for guiding decisions.
