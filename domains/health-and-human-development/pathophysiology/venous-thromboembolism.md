---
id: venous-thromboembolism
title: 'Venous Thromboembolism: DVT and Pulmonary Embolism'
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: thrombosis-pathophysiology
  type: hard
- id: respiratory-system-overview
  type: soft
builds-toward:
- post-thrombotic-syndrome
tags:
- venous-thromboembolism
- dvt
- pulmonary-embolism
stage: expert
status: draft
---

# Venous Thromboembolism: DVT and Pulmonary Embolism

## Core Idea
Venous thromboembolism encompasses deep venous thrombosis (DVT) and pulmonary embolism (PE). Virchow's triad—venous stasis, endothelial injury, hypercoagulability—drives pathogenesis. Risk factors include immobility, surgery, malignancy, and thrombophilia.

## How It's Best Learned
Understand why PE mortality is high: acute right ventricular strain from sudden increase in afterload. Study Wells criteria and D-dimer for diagnostic stratification. Review thrombophilia screening and when to recommend.

## Common Misconceptions
Not all elevated D-dimer indicates thrombosis—infection, malignancy, and trauma elevate it. Negative compression ultrasound does not exclude PE; PE can occur without DVT. Anticoagulation duration depends on provocation (transient vs. unprovoked).

## Questions

```yaml
- question: "A 65-year-old patient is 5 days post-abdominal surgery with a D-dimer of 2.8 µg/mL (elevated). The most appropriate clinical interpretation is:"
  type: multiple-choice
  options:
    - "This confirms DVT or PE; anticoagulation should begin immediately."
    - "This strongly suggests active thrombosis, warranting urgent imaging and likely treatment."
    - "Elevated D-dimer in this postoperative context is non-specific; imaging is required to diagnose or exclude VTE."
    - "This is a normal postoperative finding and requires no further evaluation."
  answer: 2
  explanation: "D-dimer has poor specificity — surgery, infection, trauma, and malignancy all elevate it without VTE. In a postoperative patient, an elevated D-dimer is expected and provides almost no diagnostic information. The asymmetry is critical: D-dimer is useful for *ruling out* VTE in low-probability outpatient patients (high sensitivity), but a positive result in hospitalized patients is nearly meaningless. Imaging is required to diagnose VTE regardless of D-dimer level in this context."

- question: "A patient presents with acute pleuritic chest pain and hemoptysis. Compression ultrasound of both legs is negative. The correct interpretation is:"
  type: multiple-choice
  options:
    - "PE is excluded, because PE arises from DVT and the negative leg ultrasound would have detected it."
    - "The absence of leg symptoms makes PE very unlikely, and further workup can be deferred."
    - "PE remains possible; a significant proportion of PEs occur without a detectable DVT on ultrasound."
    - "A negative leg ultrasound is sufficient to exclude PE without CT pulmonary angiography."
  answer: 2
  explanation: "The common misconception is that PE always follows from detectable DVT. In practice, a substantial minority of PE cases occur without detectable DVT — the thrombus may have fully embolized, originated in pelvic veins not imaged by leg ultrasound, or been too small to detect. A negative compression ultrasound does not exclude PE, and clinical suspicion with appropriate Wells scoring should guide whether CT pulmonary angiography is needed."

- question: "In massive pulmonary embolism, right ventricular failure occurs because the normal RV is a thin-walled, low-pressure chamber not equipped to compensate for sudden, severe increases in afterload."
  type: true-false
  answer: true
  explanation: "The normal RV is adapted to the low-resistance pulmonary circulation. When large central emboli obstruct main pulmonary arteries, afterload doubles or triples acutely. The thin-walled RV cannot generate the pressure needed to push blood through, dilates, and fails. The dilating RV shifts the interventricular septum leftward (D-sign on echocardiography), compromises LV filling, and produces obstructive shock. This cascade explains the high mortality (>30% at 30 days) of massive PE."

- question: "D-dimer testing is equally useful for diagnosing (ruling in) and excluding (ruling out) venous thromboembolism in clinical practice."
  type: true-false
  answer: false
  explanation: "D-dimer has very high sensitivity (>97%) but very poor specificity for VTE. This asymmetry makes it a reliable rule-out test — a negative result in a low-probability patient safely excludes VTE without imaging. But a positive result is nearly uninformative, because many common conditions (surgery, infection, malignancy, trauma, pregnancy) elevate D-dimer without VTE. The rule is: D-dimer is for ruling out, not ruling in."

- question: "Explain the clinical asymmetry between a negative D-dimer result and a positive D-dimer result when evaluating for VTE."
  type: short-answer
  answer: "D-dimer has very high sensitivity (>97%) for active thrombosis — it is almost always elevated when VTE is present. Therefore, a negative result reliably excludes VTE in low-pretest-probability patients: if VTE were present, D-dimer would almost certainly be elevated. A positive result, however, has very poor specificity — infection, surgery, malignancy, trauma, and pregnancy all elevate D-dimer without any thrombosis. Positive D-dimer tells you little in most clinical settings. The asymmetry: negative = useful (rules out); positive = often uninformative (does not rule in)."
  explanation: "This asymmetry is a direct consequence of the sensitivity/specificity tradeoff. D-dimer is most useful precisely in the population where you might think it matters least: the low-probability outpatient where imaging would otherwise be needed."
```

## Explainer

From your study of thrombosis pathophysiology, you know that clot formation requires at least one element of **Virchow's triad**: venous stasis, endothelial injury, or hypercoagulability. Venous thromboembolism is the clinical outcome when thrombosis occurs in the deep venous system and the formed clot dislodges. VTE is best understood as a two-event disease: the first event (DVT formation) and the second event (PE, when that thrombus travels to the pulmonary arterial tree).

**Deep venous thrombosis** most commonly begins in the valve pockets of calf veins — regions where blood pools and flow is slowest, creating the stasis element. Red cell-fibrin thrombus propagates proximally toward the popliteal, femoral, and iliac veins. Below-knee DVT carries modest embolism risk; proximal DVT (above the knee) carries substantially higher risk. The endothelial injury element dominates after surgery — especially orthopedic hip and knee replacement, which both traumatizes vessels and immobilizes patients. Hypercoagulability drives DVT in patients with inherited thrombophilias (factor V Leiden, prothrombin G20210A) or acquired states (antiphospholipid syndrome, malignancy). Malignancy deserves emphasis: tumors release tissue factor and other procoagulant mediators that chronically activate coagulation — unprovoked DVT is the presenting sign of occult malignancy in roughly 10% of cases and warrants cancer screening.

**Pulmonary embolism** occurs when a thrombus fragment breaks free and lodges in the pulmonary arterial tree. The physiological consequence scales with embolus size and the patient's cardiopulmonary reserve. Small peripheral emboli may cause **pleuritis** — chest pain and hemoptysis from pulmonary infarction in the lung tissue — without hemodynamic compromise. Large central emboli obstruct main pulmonary arteries, creating sudden **right ventricular (RV) pressure overload**. The normal RV is a thin-walled, low-pressure chamber adapted to the low-resistance pulmonary circulation. When resistance suddenly doubles or triples, the RV cannot generate enough pressure to push blood through, dilates, and fails. The dilating RV shifts the interventricular septum leftward (visible on echocardiography as the "D-sign"), compromising LV filling and producing systemic hypotension — the picture of **obstructive cardiogenic shock**. Stretched RV myocardium releases troponin and BNP. Massive PE carries 30-day mortality exceeding 30% precisely because this RV failure cascade is rapid.

Risk stratification drives clinical decision-making. The **Wells score** formalizes clinical probability by assigning points for signs of DVT, PE as the most likely diagnosis, immobilization, cancer, prior VTE, hemoptysis, and tachycardia. In low-probability patients, a negative **D-dimer** (a fibrin degradation product) safely excludes VTE without imaging — because D-dimer sensitivity exceeds 97%, so a negative result reliably rules out active thrombosis. However, D-dimer has poor specificity: infection, trauma, surgery, and malignancy all elevate it, making a positive result nearly meaningless in hospitalized patients. The asymmetry is the key rule: D-dimer is for ruling out, not ruling in. Once VTE is confirmed, anticoagulation duration depends critically on whether the episode was provoked by a transient reversible risk factor (surgery, immobilization, estrogen therapy — typically 3 months of anticoagulation) or unprovoked (idiopathic — high recurrence risk favoring extended therapy), a distinction that requires explicit assessment at every VTE diagnosis.
