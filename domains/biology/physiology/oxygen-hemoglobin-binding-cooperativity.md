---
id: oxygen-hemoglobin-binding-cooperativity
title: Oxygen-Hemoglobin Binding Cooperativity and the Oxygen Dissociation Curve
domain: biology
course: physiology
prerequisites:
- id: blood-composition-and-function
  type: hard
- id: protein-quaternary-structure
  type: soft
- id: equilibrium-expression-kc-kp-constants
  type: soft
- id: coordination-chemistry-basics
  type: soft
- id: chemical-equilibrium
  type: soft
builds-toward:
- oxygen-delivery-tissue-extraction-consumption
tags:
- oxygen transport
- hemoglobin
- binding
- cooperativity
stage: formal-systems
status: draft
---

# Oxygen-Hemoglobin Binding Cooperativity and the Oxygen Dissociation Curve

## Core Idea
Hemoglobin's oxygen binding exhibits positive cooperativity: binding of one oxygen molecule to a subunit increases the affinity of remaining subunits for oxygen, producing the characteristic sigmoid (S-shaped) oxygen dissociation curve rather than a hyperbolic relationship. This cooperativity ensures efficient oxygen loading in the pulmonary capillaries (where PO2 is high, steep portion of curve) and efficient unloading in tissue capillaries (where PO2 is lower, steep portion of curve). The dissociation curve is rightward-shifted (decreased affinity, enhanced unloading) by decreases in pH, increases in PCO2, increases in temperature, and increases in 2,3-diphosphoglycerate—all conditions present in metabolically active tissue.

## Explainer

From your study of protein quaternary structure, you know that hemoglobin is a tetramer — four subunits (two α, two β), each carrying one heme group with an iron atom that can bind one oxygen molecule. A simple prediction might be that each subunit binds oxygen independently, like four separate myoglobin molecules. If that were true, the oxygen dissociation curve would be a simple hyperbola: saturation would rise steeply at low PO₂ and then flatten, with half-saturation occurring at a single fixed PO₂. Instead, hemoglobin produces a **sigmoid (S-shaped) curve**, and the reason is **positive cooperativity** — a conformational communication between subunits that makes each successive oxygen molecule easier to bind than the last.

The mechanism works through two quaternary conformations: the **T (tense) state** and the **R (relaxed) state**. Deoxyhemoglobin sits in the T state, where salt bridges and hydrogen bonds between subunits hold the molecule in a conformation with low oxygen affinity. When the first O₂ binds to a heme iron, it pulls the iron into the plane of the porphyrin ring, tugging on the attached histidine and shifting that subunit's geometry. This local change propagates through the subunit interfaces, partially disrupting the stabilizing bonds of the T state and nudging the entire tetramer toward the R state. Each subsequent O₂ binding further destabilizes the T state, so the second O₂ binds more easily than the first, the third more easily than the second, and the fourth most easily of all. The result is the sigmoid curve: initially flat (T-state hemoglobin resists binding), then steeply rising (cooperativity kicks in as the molecule transitions toward R state), then flattening again as saturation approaches 100%.

The physiological brilliance of this sigmoid shape becomes clear when you look at where on the PO₂ scale the lungs and tissues operate. In the pulmonary capillaries, alveolar PO₂ is about 100 mmHg — firmly on the upper plateau of the curve, where hemoglobin is ~98% saturated. Even if PO₂ drops somewhat (say, at altitude), hemoglobin remains nearly fully loaded because the plateau is forgiving. In the tissue capillaries, PO₂ drops to around 40 mmHg at rest — right in the steep portion of the curve — and hemoglobin saturation falls to about 75%. A small further drop in tissue PO₂ (as occurs during exercise) causes a large additional release of O₂. If the curve were hyperbolic instead, hemoglobin would release oxygen too readily in the lungs and not release enough in the tissues, because the gradual slope would not create the same differential between loading and unloading zones.

The curve's position can shift leftward or rightward, modulating oxygen delivery to match metabolic demand. The **Bohr effect** describes rightward shifts caused by decreased pH and increased CO₂ — both products of active metabolism. When working muscle produces CO₂ and lactic acid, the local drop in pH stabilizes the T state, reducing hemoglobin's oxygen affinity and promoting unloading exactly where oxygen is needed most. Rising temperature and **2,3-diphosphoglycerate (2,3-DPG)** — a glycolytic intermediate that accumulates in red blood cells during chronic hypoxia — also shift the curve rightward. Conversely, in the lungs, where CO₂ is exhaled, pH rises, and hemoglobin shifts back toward the R state, facilitating oxygen loading. The system is self-adjusting: tissues that consume the most oxygen create the strongest unloading signals, ensuring that oxygen delivery tracks metabolic demand without any central controller.
