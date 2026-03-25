---
id: platelet-function-and-von-willebrand-disease
title: Platelet Function and Von Willebrand Disease
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: hemostasis-pathophysiology
  type: hard
- id: blood-composition-and-function
  type: soft
- id: platelet-activation-and-aggregation-pathophysiology
  type: soft
builds-toward:
- bleeding-disorders-overview
- thrombosis-pathophysiology
tags:
- platelets
- von-willebrand-factor
- adhesion
- activation
- aggregation
stage: expert
status: validated
---
# Platelet Function and Von Willebrand Disease

## Core Idea
Platelets adhere to exposed subendothelium through von Willebrand factor (vWF), a large multimeric adhesive protein that bridges platelets to collagen. Upon activation (by thrombin, ADP, collagen), platelets change shape, secrete granule contents, and expose phosphatidylserine for tenase complex assembly. Platelet aggregation is mediated by fibrinogen bridging across GPIIb/IIIa integrin. Von Willebrand disease results from deficiency or dysfunction of vWF, causing defective adhesion and often factor VIII deficiency (vWF carries factor VIII).

## How It's Best Learned
Study the three phases of platelet activation: adhesion (vWF-mediated), activation (agonist-induced shape change and secretion), and aggregation (fibrinogen-mediated crosslinking). Understand why vWF multimers matter—larger multimers are more thrombotic.

## Common Misconceptions
Platelets are not 'miniature cells'—they lack a nucleus and cannot synthesize proteins de novo. vWF deficiency leads to prolonged bleeding time (not clotting time), reflecting defective primary hemostasis. Type 2 vWD has complex genetics and variable phenotypes.

## Questions

```yaml
- question: "A 24-year-old woman reports frequent nosebleeds, heavy menstrual periods, and prolonged bleeding after dental extractions since childhood. Family history is positive for similar symptoms. Labs show normal PT, slightly prolonged PTT, and a prolonged PFA-100 closure time. What is the most likely diagnosis?"
  type: multiple-choice
  options:
    - "Hemophilia A (Factor VIII deficiency)"
    - "Immune thrombocytopenic purpura (ITP)"
    - "Von Willebrand disease"
    - "Disseminated intravascular coagulation (DIC)"
  answer: 2
  explanation: "The pattern of mucocutaneous bleeding — epistaxis, menorrhagia, prolonged wound bleeding — is the hallmark of a primary hemostasis defect, specifically defective platelet adhesion. The prolonged PFA-100 (a test of platelet plug formation) with normal PT confirms that the coagulation cascade is intact and the defect lies in the platelet plug. The slightly prolonged PTT may reflect reduced factor VIII, since vWF normally carries and protects factor VIII. Hemophilia A causes deep tissue bleeding (hemarthroses, muscle hematomas), not mucocutaneous bleeding — a critical distinguishing feature."

- question: "Why is von Willebrand factor particularly critical for platelet adhesion in arteries compared to veins?"
  type: multiple-choice
  options:
    - "Arteries contain more collagen in the subendothelium, requiring a stronger adhesive bridge"
    - "Arterial blood flows at higher shear stress, which would dislodge platelets before direct collagen binding can occur without a bridging molecule"
    - "Veins produce their own platelet-adhesion molecule that makes vWF redundant in the venous circulation"
    - "vWF is synthesized only by arterial endothelial cells, not venous endothelium"
  answer: 1
  explanation: "At the high shear rates of arterial blood flow, simple diffusion-based platelet-collagen contact would be too slow and too weak — platelets would be swept past before they could adhere. vWF solves this: it unfolds under high shear stress and simultaneously binds exposed collagen and platelet GPIb receptors, physically bridging the gap and decelerating platelets enough for stable adhesion. In the slower-flow venous circulation, direct platelet-collagen binding is sufficient. This explains why vWD causes more arterial-type bleeding problems."

- question: "Von Willebrand disease prolongs the prothrombin time (PT), because vWF deficiency impairs the extrinsic coagulation pathway."
  type: true-false
  answer: false
  explanation: "vWD prolongs the bleeding time and PFA-100 closure time, which are tests of primary hemostasis (platelet plug formation). The PT, which tests the extrinsic coagulation pathway (factor VII, X, V, prothrombin, fibrinogen), is unaffected by vWF deficiency. In severe vWD, the PTT may be prolonged because vWF normally carries and protects factor VIII from proteolytic degradation — but even then, it is the secondary effect on factor VIII that prolongs the PTT, not a direct effect on the coagulation cascade."

- question: "In addition to mediating platelet adhesion, vWF serves as a carrier protein for factor VIII in circulation, protecting it from premature proteolysis."
  type: true-false
  answer: true
  explanation: "This dual role explains why severe vWF deficiency (Type 3 vWD) can cause both primary hemostasis failure and reduced factor VIII levels, leading to a combined bleeding phenotype that partially overlaps with mild hemophilia A. In vWD patients with very low vWF, the factor VIII that is not bound to vWF is rapidly degraded, shortening its half-life and reducing plasma levels below the normal range."

- question: "How does the clinical bleeding pattern of von Willebrand disease differ from that of hemophilia A, and what explains this difference mechanistically?"
  type: short-answer
  answer: "Von Willebrand disease causes mucocutaneous bleeding — nosebleeds, gum bleeding, heavy menstrual periods, and prolonged oozing from minor cuts — because vWF mediates platelet adhesion, which is the first step of primary hemostasis (the platelet plug). Hemophilia A causes deep tissue bleeding — hemarthroses, intramuscular hematomas — because factor VIII is required for tenase complex assembly in the intrinsic coagulation pathway, which is secondary hemostasis (fibrin clot formation). The platelet plug forms normally in hemophilia A and can stop capillary-level bleeding; it is the fibrin reinforcement that fails. In vWD, the platelet plug itself cannot form properly, so even minor trauma causes prolonged surface bleeding."
  explanation: "This distinction is clinically crucial: a patient with joint bleeds after minor trauma likely has a coagulation factor deficiency; a patient with nosebleeds and heavy periods likely has a primary hemostasis defect. The lab also reflects this — vWD prolongs the PFA-100 but not the PT; hemophilia A prolongs the PTT but not the PFA-100."
```

## Explainer

From your study of hemostasis, you know that stopping bleeding requires two sequential processes: **primary hemostasis** (the platelet plug) and **secondary hemostasis** (the coagulation cascade producing fibrin). Platelet function sits entirely within primary hemostasis, but it is not a single step — it is a coordinated three-phase program: adhesion, activation, and aggregation.

**Adhesion** is the problem-solving phase. Resting platelets do not stick to intact endothelium — the endothelial surface actively repels them through nitric oxide and prostacyclin (PGI2) secretion. When a vessel is damaged, subendothelial collagen and **von Willebrand factor (vWF)** are exposed. At the high shear stress of arterial flow, free vWF unfolds and changes conformation, binding collagen on one end and platelet GPIb receptors on the other. This bridging function is the reason vWF exists: simple diffusion-based collagen-platelet interactions would be too slow and too weak at arterial flow rates. vWF's effectiveness scales with its size — the largest **ultra-large multimers** (ULvWF, released from Weibel-Palade bodies during endothelial activation) are the most thrombogenic, and the ADAMTS13 enzyme that cleaves them into smaller forms is an important regulatory brake. When ADAMTS13 fails, ULvWF accumulates and drives pathological microvascular thrombosis — the mechanism of thrombotic thrombocytopenic purpura (TTP).

**Activation** transforms the adherent platelet from a passive disc into an active signaling cell. Collagen, thrombin, ADP, and TXA2 all converge on intracellular signaling cascades that produce three simultaneous outputs: shape change (the platelet extends pseudopods, dramatically increasing surface area), **degranulation** (alpha granules releasing fibrinogen, vWF, factor V, and P-selectin; dense granules releasing ADP, serotonin, and calcium to recruit more platelets), and **phosphatidylserine (PS) flip** (the inner leaflet phospholipid migrates to the outer leaflet, providing the anionic surface required for the tenase and prothrombinase complexes of the coagulation cascade). The last step is the molecular bridge between primary and secondary hemostasis — platelet activation directly enables coagulation by providing the phospholipid scaffold.

**Von Willebrand disease (vWD)** is the most common inherited bleeding disorder, and its clinical presentation illustrates which hemostatic system is affected. Because vWF mediates the initial adhesion step of primary hemostasis, vWD patients present with **mucocutaneous bleeding** — nosebleeds, gum bleeding, heavy menstrual periods, and prolonged bleeding from minor cuts. This is the classic presentation of a platelet plug defect, in contrast to coagulation factor deficiencies (hemophilia A/B) which present with **deep tissue bleeding** — hemarthroses, intramuscular hematomas. Laboratory testing reflects this: vWD prolongs the **bleeding time and PFA-100 closure time** (tests of primary hemostasis) but initially leaves the PT and PTT normal — unless the vWF deficiency is severe enough to reduce factor VIII levels, since vWF normally carrier-protects factor VIII from premature proteolysis. Type 1 vWD (partial quantitative deficiency) is mild and common; Type 3 (near-absent vWF) is severe and rare; Type 2 involves qualitative defects with variable clinical severity depending on which aspect of vWF function is disrupted.
