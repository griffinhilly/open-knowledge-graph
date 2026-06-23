---
id: cholesterol-metabolism-and-regulation
title: Cholesterol Metabolism and Regulation
domain: biology
course: biochemistry
prerequisites:
- id: cholesterol-synthesis
  type: hard
- id: organic-chemistry-intro
  type: soft
builds-toward:
- lipoproteins-structure-and-transport
tags:
- cholesterol
- HMG-CoA-reductase
- sterol-regulation
stage: formal-systems
status: validated
---

# Cholesterol Metabolism and Regulation

## Core Idea
Cholesterol synthesis is tightly regulated by SREBP (sterol regulatory element binding protein) signaling: high cholesterol represses HMG-CoA reductase expression, lowering synthesis. LDL-mediated uptake and esterification by ACAT also suppress synthesis. Cholesterol balance is maintained by controlling synthesis, absorption, and excretion via bile acids.

## Questions

```yaml
- question: "A patient takes a statin, which inhibits HMG-CoA reductase. Serum LDL cholesterol falls significantly. What is the primary mechanism by which statins lower blood LDL levels?"
  type: multiple-choice
  options:
    - "Statins directly block LDL particles from binding their receptors in the bloodstream"
    - "Inhibiting HMG-CoA reductase lowers intracellular cholesterol, activating SREBP, which upregulates LDL receptor expression, pulling more LDL from the blood"
    - "Statins stimulate bile acid synthesis, converting more cholesterol to bile acids that are then excreted"
    - "Statins block ACAT, preventing cholesterol esterification and forcing cells to export excess cholesterol as LDL"
  answer: 1
  explanation: "The mechanism is indirect and counterintuitive: statins inhibit synthesis, which lowers intracellular cholesterol, which activates the SCAP-SREBP pathway, which upregulates both HMG-CoA reductase and LDL receptor expression. The LDL receptor upregulation is the key effect — more receptors on cell surfaces capture more LDL from the blood. Statins lower serum LDL not by blocking it directly, but by making cells more hungry for it through the feedback regulatory system."

- question: "Under normal cellular conditions, SCAP is bound to Insig in the ER and the SREBP pathway is inactive. What change triggers SREBP activation and movement to the Golgi?"
  type: multiple-choice
  options:
    - "High intracellular cholesterol causes SCAP to release Insig and escort SREBP to the Golgi"
    - "Low intracellular cholesterol causes SCAP to release Insig, allowing the SCAP-SREBP complex to travel to the Golgi"
    - "SREBP is cleaved directly in the ER by Site-1 protease when cholesterol falls below a threshold"
    - "LDL receptor activation signals back to the nucleus to release SREBP from its precursor form"
  answer: 1
  explanation: "The system is a negative feedback loop: low cholesterol releases the brake. When cholesterol in the ER membrane drops, cholesterol dissociates from SCAP's sterol-sensing domain, SCAP releases Insig, and the SCAP-SREBP complex travels to the Golgi. There, Site-1 and Site-2 proteases cleave SREBP, releasing its active transcription factor fragment. High cholesterol does the opposite — it locks SCAP-SREBP in the ER by promoting the SCAP-Insig interaction."

- question: "When intracellular cholesterol is low, SREBP activation upregulates both HMG-CoA reductase (increasing synthesis) and LDL receptor expression (increasing uptake)."
  type: true-false
  answer: true
  explanation: "SREBP is a transcription factor that drives expression of multiple genes in the cholesterol homeostasis network, including HMG-CoA reductase (the rate-limiting synthesis enzyme) and the LDL receptor (which imports cholesterol from the blood). This dual upregulation makes the response to low cholesterol more powerful: the cell simultaneously increases its own production and its ability to scavenge cholesterol from circulation."

- question: "Statins lower blood cholesterol primarily by blocking intestinal absorption of dietary cholesterol."
  type: true-false
  answer: false
  explanation: "Statins inhibit HMG-CoA reductase, the rate-limiting enzyme in the mevalonate pathway of cholesterol *synthesis* — not absorption. Drugs that block intestinal absorption (such as ezetimibe) work by a different mechanism. Statins reduce intracellular cholesterol in liver cells, which activates SREBP, which upregulates LDL receptors, which then clear LDL from the blood. The serum LDL reduction comes primarily from increased receptor-mediated uptake, not from blocking absorption."

- question: "Explain how the SCAP-SREBP-Insig system functions as a feedback sensor for cholesterol homeostasis."
  type: short-answer
  answer: "SCAP has a sterol-sensing domain that directly binds cholesterol. When cholesterol is abundant, cholesterol-bound SCAP is retained in the ER by interaction with Insig, keeping SREBP inactive. When cholesterol is scarce, SCAP releases Insig, escorts SREBP to the Golgi, where proteases cleave it and release its active transcription factor fragment. This fragment enters the nucleus and upregulates cholesterol synthesis and LDL receptor genes. High cholesterol thus suppresses the pathway that makes more cholesterol — a classic negative feedback loop."
  explanation: "The elegance of this system is that cholesterol itself is the signal: it acts directly on SCAP's sterol-sensing domain, with no intermediary second messengers needed. This allows the cell to respond immediately to changes in membrane cholesterol levels. The system is also graded — partial cholesterol depletion produces partial SREBP activation — allowing fine-tuned homeostatic control rather than an all-or-nothing switch."
```

## Explainer

From your study of cholesterol synthesis, you know that the mevalonate pathway builds cholesterol from acetyl-CoA through a long series of reactions, with **HMG-CoA reductase** catalyzing the committed, rate-limiting step. The question this topic answers is: how does the cell know when it has enough cholesterol and needs to stop making more? The answer is an elegant feedback system centered on a transcription factor called **SREBP** (sterol regulatory element binding protein) that directly senses cholesterol levels in the endoplasmic reticulum membrane.

Here is the mechanism in simplified form. SREBP is synthesized as an inactive precursor embedded in the ER membrane, where it is held in place by an escort protein called **SCAP** (SREBP cleavage-activating protein). SCAP has a sterol-sensing domain — a region that physically binds cholesterol. When cholesterol levels in the ER membrane are high, cholesterol binds to SCAP and locks the SCAP-SREBP complex in the ER by promoting its interaction with an anchor protein called **Insig**. When cholesterol levels drop, SCAP's conformation changes, releasing it from Insig, and the SCAP-SREBP complex travels to the Golgi apparatus. There, two proteases (Site-1 and Site-2 proteases) cleave SREBP, releasing its active fragment, which enters the nucleus and turns on genes for cholesterol synthesis — including HMG-CoA reductase — and for LDL receptor expression. The result is a clean negative feedback loop: low cholesterol activates synthesis, and high cholesterol shuts it down.

But synthesis is only one of three levers the body uses to maintain cholesterol balance. The second is **uptake** via LDL receptors. Cells can import cholesterol by capturing LDL particles from the bloodstream, internalizing them through receptor-mediated endocytosis, and releasing the cholesterol in lysosomes. The SREBP system controls this too — when intracellular cholesterol is low, SREBP upregulates LDL receptor expression, pulling more cholesterol in from the blood. When cholesterol is abundant, excess free cholesterol is converted to **cholesteryl esters** by the enzyme **ACAT** (acyl-CoA:cholesterol acyltransferase) and stored in lipid droplets, keeping the free cholesterol concentration in membranes from rising to toxic levels.

The third lever is **excretion**. The liver converts cholesterol into **bile acids**, which are secreted into the intestine to aid fat digestion. Some bile acids are reabsorbed (enterohepatic circulation) and recycled, but a fraction is lost in feces — this is the body's primary route for eliminating cholesterol. Drugs like statins exploit this system: by inhibiting HMG-CoA reductase, they lower intracellular cholesterol, which activates SREBP, which upregulates LDL receptors, which pulls LDL cholesterol out of the blood — lowering serum LDL levels. Understanding the regulatory logic — the interplay between synthesis, uptake, storage, and excretion — is essential for grasping why cholesterol homeostasis fails in disease and how pharmacological interventions work.
