---
id: gas-exchange-and-diffusion
title: Gas Exchange and Diffusion
domain: biology
course: physiology
prerequisites:
- id: respiratory-system-overview
  type: hard
- id: diffusion-and-ficks-laws
  type: soft
- id: cardiovascular-system-overview
  type: soft
- id: ph-and-acid-base-calculations
  type: soft
builds-toward:
- respiratory-control-mechanisms
tags:
- gas exchange
- partial pressure
- Fick's law
- hemoglobin
- oxygen dissociation curve
stage: advanced
status: validated
---

# Gas Exchange and Diffusion

## Core Idea
Gas exchange at the alveolar-capillary membrane and at peripheral tissues is governed by Fick's law: diffusion rate is proportional to surface area and partial pressure gradient, and inversely proportional to membrane thickness. Atmospheric O2 (PO2 ~160 mmHg) equilibrates with alveolar air (~104 mmHg) and then diffuses into pulmonary capillary blood (~40 mmHg) until equilibration. Hemoglobin's sigmoidal oxygen-dissociation curve enables cooperative O2 loading in high-PO2 lung capillaries and efficient unloading in low-PO2 tissues. The Bohr effect — increased CO2, acidity, and temperature shift the curve rightward — enhances O2 delivery to metabolically active tissues. CO2 is transported primarily as bicarbonate ion in plasma (70%), with the remainder as dissolved CO2 and carbaminohemoglobin.

## How It's Best Learned
Draw the oxygen dissociation curve and annotate the pulmonary capillary operating point (PO2 ~100 mmHg, near-saturation) and the tissue operating point (PO2 ~40 mmHg, significant unloading). Explain why a rightward shift (Bohr effect) is beneficial in exercising muscle: acidic, warm, high-CO2 environment promotes O2 release exactly where it is most needed.

## Common Misconceptions
- O2 and CO2 move by passive diffusion — no energy expenditure is required for gas exchange itself.
- The hemoglobin curve is sigmoidal, not linear: small PO2 changes near 100 mmHg cause little O2 unloading, but in the 20–60 mmHg range relevant to tissues, the curve is steep and O2 release is large.
- Most CO2 is not carried directly on hemoglobin — bicarbonate formation in red blood cells accounts for the majority of CO2 transport.

## Questions

```yaml
- question: "Which form accounts for the majority of CO2 transport in venous blood?"
  type: multiple-choice
  options: ["Dissolved CO2 in plasma", "Carbaminohemoglobin bound to hemoglobin", "Bicarbonate ion (HCO3-) in plasma", "CO2 bound to plasma albumin"]
  answer: 2
  explanation: "About 70% of CO2 is transported as bicarbonate. CO2 diffuses into red blood cells, where carbonic anhydrase rapidly converts it to H2CO3, which then dissociates to HCO3- and H+. Students often assume hemoglobin carries most CO2, but carbaminohemoglobin accounts for only ~20-23%."

- question: "A rightward shift of the oxygen-dissociation curve (Bohr effect) means hemoglobin releases more O2 at any given PO2, which benefits metabolically active tissues."
  type: true-false
  answer: true
  explanation: "The Bohr effect is triggered by increased CO2, acidity, and temperature — all byproducts of active metabolism. By reducing hemoglobin's O2 affinity, the rightward shift causes more O2 to unload at the same tissue PO2. This is a self-reinforcing delivery mechanism: the more a tissue metabolizes, the more O2 it receives."

- question: "Why does the sigmoidal shape of the oxygen-dissociation curve make hemoglobin more effective than a hypothetical linear O2-binding protein would be?"
  type: short-answer
  answer: "The flat upper region allows near-complete O2 loading in the lungs across a range of alveolar PO2 values, while the steep middle region allows large amounts of O2 to be unloaded in tissues with only small drops in PO2."
  explanation: "A linear binding protein would unload O2 gradually across all PO2 levels, including in the lungs, reducing loading efficiency. Hemoglobin's cooperative binding (sigmoidal kinetics) concentrates loading and unloading in the specific PO2 windows relevant to the lung and tissues, maximizing O2 delivery per unit blood volume."
```

## Explainer

Gas exchange is fundamentally a diffusion problem, and everything about the respiratory and circulatory systems is organized to make diffusion work as efficiently as possible. Fick's law tells you the key variables: diffusion rate increases with surface area and partial pressure gradient, and decreases with membrane thickness. The alveoli provide an enormous surface area (~70 m²), the alveolar-capillary membrane is only ~0.5 µm thick, and the partial pressure gradient between alveolar air (PO2 ~104 mmHg) and incoming venous blood (PO2 ~40 mmHg) is steep. These three factors together make O2 uptake fast enough to nearly fully equilibrate within the brief time a red blood cell spends traversing a pulmonary capillary.

Once O2 crosses into the blood, it faces a transport problem: only ~3 mL of O2 per liter of blood dissolves in plasma — far too little to supply tissues. Hemoglobin solves this by binding O2 cooperatively. The oxygen-dissociation curve is sigmoidal, not linear, because each O2 bound increases the affinity for the next. The flat top of the curve (around PO2 100 mmHg in the lungs) means that hemoglobin remains ~97-98% saturated even if alveolar PO2 drops somewhat. The steep middle portion (PO2 20–60 mmHg) covers the range found in tissues: small drops in PO2 trigger large O2 release. This shape is not accidental — it is precisely the range where delivery is most needed.

The Bohr effect fine-tunes this delivery. In actively metabolizing tissues, CO2 production lowers local pH and raises PCO2 and temperature. Each of these shifts the dissociation curve to the right — hemoglobin's O2 affinity falls, so even more O2 is released at a given PO2. In the lungs, the reverse occurs: CO2 is exhaled, pH rises, and hemoglobin's affinity increases, promoting O2 loading. The system is elegant because the same metabolic signals that create O2 demand also trigger enhanced delivery.

CO2 transport runs in parallel but is mechanistically different. When CO2 enters red blood cells from tissues, carbonic anhydrase converts it to carbonic acid (H2CO3), which dissociates to bicarbonate (HCO3-) and a proton. The bicarbonate exits into plasma in exchange for chloride (the chloride shift), and it is in this bicarbonate form that ~70% of CO2 is carried to the lungs. The proton released in this reaction is buffered largely by hemoglobin itself — and this proton binding is what causes the Bohr effect. The CO2 and O2 transport systems are therefore biochemically coupled: unloading O2 in tissues simultaneously facilitates CO2 loading, and vice versa in the lungs.
