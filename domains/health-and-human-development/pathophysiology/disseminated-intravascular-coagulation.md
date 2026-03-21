---
id: disseminated-intravascular-coagulation
title: Disseminated Intravascular Coagulation (DIC)
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: hemostasis-pathophysiology
  type: hard
- id: thrombosis-pathophysiology
  type: hard
tags:
- dic
- coagulopathy
- systemic-thrombosis
stage: advanced
status: draft
---

# Disseminated Intravascular Coagulation (DIC)

## Core Idea
DIC is widespread intravascular fibrin deposition causing simultaneous thrombosis and consumption coagulopathy. Tissue factor release (sepsis, trauma, malignancy) triggers thrombin generation, platelet depletion, and fibrinogen consumption, culminating in bleeding and multi-organ failure.

## How It's Best Learned
Study laboratory findings: low platelet count, low fibrinogen, elevated PT/aPTT, elevated D-dimer, schistocytes on smear. Understand the vicious cycle: thrombosis → fibrinolysis → bleeding. Recognize precipitating conditions: DIC is not a primary disease.

## Common Misconceptions
DIC is not synonymous with consumption coagulopathy—other conditions (massive transfusion, liver disease) cause similar laboratory abnormalities. Treatment is management of the underlying trigger, not anticoagulation or platelet transfusion in most cases.

## Questions

```yaml
- question: "A septic patient develops DIC with active bleeding from IV sites. The physician administers platelet transfusions and fresh frozen plasma. Which outcome is most consistent with the pathophysiology of DIC?"
  type: multiple-choice
  options:
    - "Sustained improvement — replacing consumed factors stops the coagulopathy"
    - "Temporary improvement followed by resumed consumption, because the underlying trigger has not been addressed"
    - "Worsening — platelet transfusions accelerate thrombin generation and worsen thrombosis"
    - "No effect — in late DIC, laboratory values no longer respond to factor replacement"
  answer: 1
  explanation: "The key therapeutic insight is that DIC is a secondary syndrome — the consumption continues as long as the underlying source of tissue factor exposure persists. Platelet transfusions and FFP temporarily replenish substrates but do not stop the pathological process driving their consumption. The infection must be treated; only then will the TF exposure stop and the coagulopathy resolve. Treating the coagulopathy in isolation is a fundamental error that the mechanism predicts will fail."

- question: "In DIC, elevated D-dimer most directly reflects which part of the pathophysiological sequence?"
  type: multiple-choice
  options:
    - "Active thrombin generation converting fibrinogen to fibrin"
    - "Platelet activation and consumption by systemic thrombin"
    - "Compensatory fibrinolysis breaking down fibrin clots to produce degradation products"
    - "Antithrombin depletion allowing unregulated coagulation cascade activation"
  answer: 2
  explanation: "D-dimer is a specific fibrin degradation product released when plasmin degrades cross-linked fibrin. Its elevation in DIC reflects the compensatory fibrinolytic response to massive fibrin deposition — plasmin is generated in response to the clots being formed throughout the microcirculation. D-dimer does not directly measure thrombin generation (that's reflected in fibrinogen consumption and PT/aPTT prolongation) nor platelet loss."

- question: "A patient in early DIC is more likely to present with bleeding than with organ dysfunction due to microvascular thrombosis."
  type: true-false
  answer: false
  explanation: "This reverses the clinical timeline. Early DIC manifests as thrombosis — microthrombi in capillaries causing organ dysfunction (renal failure, respiratory distress, altered consciousness). Bleeding is a late manifestation, occurring after coagulation factors and platelets have been exhausted by the thrombotic process. The sequence is: thrombosis first, then consumption, then bleeding. Thinking that DIC always presents primarily with bleeding misses the early thrombotic phase where intervention can be most effective."

- question: "The presence of schistocytes on peripheral blood smear in DIC reflects mechanical injury to red blood cells by fibrin strands deposited in small vessels."
  type: true-false
  answer: true
  explanation: "Schistocytes (fragmented erythrocytes) form when red blood cells are sheared by fibrin strands deposited across the lumen of small vessels — a direct consequence of microvascular thrombosis. Their presence is a morphological hallmark of microangiopathic hemolytic anemia and confirms that fibrin deposition in the microvasculature is occurring. This connects the laboratory finding directly to the pathophysiological mechanism of DIC."

- question: "Explain why DIC presents with both clotting and bleeding simultaneously — what is the pathophysiological mechanism that creates this apparent paradox?"
  type: short-answer
  answer: "Systemic tissue factor exposure triggers thrombin generation throughout the entire vascular tree, causing widespread fibrin deposition and platelet activation (thrombosis). This massive activation consumes platelets and clotting factors faster than they can be replenished, depleting the raw materials needed for hemostasis (consumption coagulopathy). The clotting and the bleeding are not two separate processes but one process viewed at different time points: early DIC manifests as thrombosis; late DIC manifests as hemorrhage from exhausted substrates."
  explanation: "The paradox resolves when you follow the timeline. Both thrombosis and bleeding are driven by the same root cause — systemic TF-driven thrombin generation — just observed at different stages. This is why treating only the bleeding (with factor replacement) without addressing the trigger is insufficient: the consumption continues as long as the source of TF exposure persists."
```

## Explainer

Disseminated intravascular coagulation is one of the most counterintuitive syndromes in medicine: the patient is simultaneously clotting everywhere and bleeding uncontrollably. To make sense of this, start with what you already know about hemostasis. Normal clot formation is tightly localized and regulated — tissue factor (TF) is exposed only at a wound site, thrombin generation is amplified locally, and natural anticoagulants like antithrombin and protein C keep the process contained. DIC is what happens when this localization fails completely.

The trigger is systemic **tissue factor exposure**. In sepsis, endotoxin and cytokines cause endothelial cells and monocytes to express TF throughout the vasculature. In trauma, massive tissue destruction releases TF directly into the circulation. Malignancies (particularly acute promyelocytic leukemia) shed procoagulant material continuously. Obstetric catastrophes like amniotic fluid embolism introduce TF into the pulmonary circulation. In each case, TF encounters circulating factor VII and ignites the **extrinsic coagulation cascade** — not at one wound site, but simultaneously across the entire vascular tree. Thrombin is generated in enormous quantities, converting fibrinogen to fibrin and activating platelets systemically. Fibrin strands deposit in small vessels throughout the body, causing **microvascular thrombosis** and the mechanical shearing of red blood cells (producing **schistocytes** on blood smear — a hallmark finding). Organ ischemia follows in the kidneys, lungs, liver, and brain.

Here is the paradox: the same thrombin that causes clotting also triggers consumption. Every platelet activated is one removed from the circulating pool. Every fibrinogen molecule converted to fibrin is one no longer available for the next clot. Antithrombin and protein C, the natural brakes on coagulation, become depleted trying to contain the runaway activation. Meanwhile, the massive fibrin deposition triggers a compensatory surge in **fibrinolysis**: plasmin is generated to break down clots, producing fibrin degradation products (particularly **D-dimer**, another diagnostic hallmark). By the time a patient presents clinically, platelet count is crashing, fibrinogen is depleted, PT and aPTT are prolonged (clotting factors exhausted), and D-dimer is elevated — a laboratory picture that directly reflects the thrombosis-then-consumption sequence.

The clinical paradox resolves when you follow the timeline. Early DIC manifests as thrombosis — microthrombi in capillaries, organ dysfunction. Late DIC manifests as bleeding — from IV sites, mucous membranes, surgical wounds — because the raw materials for clotting have been exhausted. Both are the same process at different stages. The treatment principle follows from the mechanism: **address the trigger**. The consumption will stop only when the source of TF exposure is controlled — the infection treated, the malignancy addressed, the obstetric complication resolved. Treating the coagulopathy in isolation (platelet transfusions, fresh frozen plasma) temporarily replenishes substrates but does nothing to stop the consumption. This is why understanding DIC as a secondary syndrome — always driven by an underlying cause — is not just academic but determines the entire therapeutic strategy.
