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
- steroid-hormone-synthesis
- lipoproteins-structure-and-transport
tags:
- cholesterol
- HMG-CoA-reductase
- sterol-regulation
stage: advanced
status: draft
---

# Cholesterol Metabolism and Regulation

## Core Idea
Cholesterol synthesis is tightly regulated by SREBP (sterol regulatory element binding protein) signaling: high cholesterol represses HMG-CoA reductase expression, lowering synthesis. LDL-mediated uptake and esterification by ACAT also suppress synthesis. Cholesterol balance is maintained by controlling synthesis, absorption, and excretion via bile acids.

## Explainer

From your study of cholesterol synthesis, you know that the mevalonate pathway builds cholesterol from acetyl-CoA through a long series of reactions, with **HMG-CoA reductase** catalyzing the committed, rate-limiting step. The question this topic answers is: how does the cell know when it has enough cholesterol and needs to stop making more? The answer is an elegant feedback system centered on a transcription factor called **SREBP** (sterol regulatory element binding protein) that directly senses cholesterol levels in the endoplasmic reticulum membrane.

Here is the mechanism in simplified form. SREBP is synthesized as an inactive precursor embedded in the ER membrane, where it is held in place by an escort protein called **SCAP** (SREBP cleavage-activating protein). SCAP has a sterol-sensing domain — a region that physically binds cholesterol. When cholesterol levels in the ER membrane are high, cholesterol binds to SCAP and locks the SCAP-SREBP complex in the ER by promoting its interaction with an anchor protein called **Insig**. When cholesterol levels drop, SCAP's conformation changes, releasing it from Insig, and the SCAP-SREBP complex travels to the Golgi apparatus. There, two proteases (Site-1 and Site-2 proteases) cleave SREBP, releasing its active fragment, which enters the nucleus and turns on genes for cholesterol synthesis — including HMG-CoA reductase — and for LDL receptor expression. The result is a clean negative feedback loop: low cholesterol activates synthesis, and high cholesterol shuts it down.

But synthesis is only one of three levers the body uses to maintain cholesterol balance. The second is **uptake** via LDL receptors. Cells can import cholesterol by capturing LDL particles from the bloodstream, internalizing them through receptor-mediated endocytosis, and releasing the cholesterol in lysosomes. The SREBP system controls this too — when intracellular cholesterol is low, SREBP upregulates LDL receptor expression, pulling more cholesterol in from the blood. When cholesterol is abundant, excess free cholesterol is converted to **cholesteryl esters** by the enzyme **ACAT** (acyl-CoA:cholesterol acyltransferase) and stored in lipid droplets, keeping the free cholesterol concentration in membranes from rising to toxic levels.

The third lever is **excretion**. The liver converts cholesterol into **bile acids**, which are secreted into the intestine to aid fat digestion. Some bile acids are reabsorbed (enterohepatic circulation) and recycled, but a fraction is lost in feces — this is the body's primary route for eliminating cholesterol. Drugs like statins exploit this system: by inhibiting HMG-CoA reductase, they lower intracellular cholesterol, which activates SREBP, which upregulates LDL receptors, which pulls LDL cholesterol out of the blood — lowering serum LDL levels. Understanding the regulatory logic — the interplay between synthesis, uptake, storage, and excretion — is essential for grasping why cholesterol homeostasis fails in disease and how pharmacological interventions work.
