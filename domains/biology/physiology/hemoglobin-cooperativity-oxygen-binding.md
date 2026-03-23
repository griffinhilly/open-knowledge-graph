---
id: hemoglobin-cooperativity-oxygen-binding
title: Hemoglobin Cooperativity and the Oxygen-Hemoglobin Dissociation Curve
domain: biology
course: physiology
prerequisites:
- id: blood-composition-and-function
  type: hard
- id: protein-quaternary-structure
  type: soft
- id: equilibrium-expression-kc-kp-constants
  type: soft
builds-toward:
- carbon-dioxide-transport-and-buffering
tags:
- cooperativity
- sigmoidal-binding
- allosteric
stage: formal-systems
status: validated
---

# Hemoglobin Cooperativity and the Oxygen-Hemoglobin Dissociation Curve

## Core Idea
Hemoglobin's sigmoidal oxygen binding curve results from cooperative allosteric interactions between its four subunits: when one subunit binds oxygen, it enhances oxygen affinity in the others (T→R state transition), creating a steep binding curve that efficiently loads oxygen in the lungs and releases it in tissues.

## How It's Best Learned
Plot the oxygen-hemoglobin dissociation curve and compare to a hyperbolic myoglobin binding curve. Discuss how pH, PCO2, temperature, and 2,3-BPG shift the curve leftward (increased affinity) or rightward (decreased affinity).

## Questions

```yaml
- question: "Myoglobin (a single-subunit oxygen-binding protein in muscle) has a hyperbolic binding curve. Hemoglobin has a sigmoidal curve. At the PO₂ of resting tissue (~40 mmHg), which protein releases more oxygen, and why?"
  type: multiple-choice
  options:
    - "Myoglobin, because its higher oxygen affinity means it can hold and release more oxygen under any conditions"
    - "Hemoglobin, because its sigmoidal curve has a steep drop in saturation between lung PO₂ (~100 mmHg) and tissue PO₂ (~40 mmHg), releasing a large fraction of its load"
    - "They release the same amount because both proteins are designed for oxygen transport"
    - "Hemoglobin, because having four subunits gives it more total binding sites and therefore more oxygen to release"
  answer: 1
  explanation: "At lung PO₂ (~100 mmHg), hemoglobin is ~98% saturated. At tissue PO₂ (~40 mmHg), it falls to ~75% — releasing roughly 25% of its oxygen load per circulation. Myoglobin's hyperbolic curve means it is still ~90% saturated at 40 mmHg, releasing very little. The sigmoidal curve's steep middle section falls precisely in the physiological PO₂ range, making hemoglobin an efficient oxygen deliverer. Myoglobin holds onto oxygen at tissue PO₂ — it is designed for intracellular oxygen storage and release only at very low PO₂ inside working muscle cells."

- question: "During intense exercise, active muscles produce more CO₂ and lactic acid (lowering pH) and generate heat. What happens to hemoglobin's oxygen affinity, and what is the physiological consequence?"
  type: multiple-choice
  options:
    - "Oxygen affinity increases (curve shifts left), so hemoglobin loads more oxygen in the muscles to meet demand"
    - "Oxygen affinity decreases (curve shifts right via the Bohr effect), so hemoglobin releases more oxygen to the active tissue that needs it most"
    - "Oxygen affinity is unchanged because temperature and pH affect myoglobin but not hemoglobin"
    - "Oxygen affinity increases (curve shifts left) due to release of 2,3-BPG from red blood cells in acidic conditions"
  answer: 1
  explanation: "The Bohr effect: decreased pH and increased PCO₂ shift the oxygen-hemoglobin curve rightward, reducing oxygen affinity. At the same PO₂, hemoglobin unloads more oxygen when pH is lower. Elevated temperature has the same effect. This is a feedback loop: the metabolic products of active tissue (CO₂, lactic acid, heat) trigger greater oxygen delivery precisely where it is needed. Option 3 gets the 2,3-BPG direction backward — 2,3-BPG shifts the curve rightward (reduces affinity), not leftward."

- question: "Hemoglobin's cooperative binding means that the first oxygen molecule binds with lower affinity than subsequent ones, producing a sigmoidal rather than hyperbolic binding curve."
  type: true-false
  answer: true
  explanation: "In the T (tense) state, hemoglobin has low oxygen affinity — the first O₂ is hardest to bind. Each successive binding event shifts the tetramer progressively toward the R (relaxed) state of higher affinity. The fourth O₂ binds most readily. This progressive affinity increase is positive cooperativity, and it is what generates the S-shaped curve. A non-cooperative monomer like myoglobin has constant affinity at every binding step, producing a hyperbolic curve."

- question: "Fetal hemoglobin (HbF) has a rightward-shifted oxygen dissociation curve compared to adult hemoglobin (HbA), allowing it to offload oxygen more efficiently to fetal tissues."
  type: true-false
  answer: false
  explanation: "Fetal hemoglobin has a LEFT-shifted curve (higher oxygen affinity) compared to adult hemoglobin — not rightward. HbF's gamma subunits bind 2,3-BPG less tightly than adult beta subunits, so 2,3-BPG cannot stabilize the low-affinity T state as effectively, leaving HbF in a relatively higher-affinity state. This left shift allows fetal hemoglobin to extract oxygen from maternal hemoglobin across the placenta: at the same PO₂, HbF holds more oxygen than HbA, creating the affinity gradient that drives oxygen transfer from mother to fetus."

- question: "How does cooperativity allow hemoglobin to function as both an efficient oxygen loader in the lungs and an efficient oxygen unloader in tissues — in a way that a non-cooperative oxygen carrier could not?"
  type: short-answer
  answer: "Cooperativity creates a sigmoidal binding curve with a steep middle section that falls precisely in the physiological PO₂ range between lungs (~100 mmHg) and tissues (~40 mmHg). At lung PO₂, hemoglobin sits near the top of the steep section — nearly fully saturated. At tissue PO₂, it has descended through the steep section — releasing a large fraction of its oxygen. A non-cooperative carrier with a hyperbolic curve would either have such high affinity that it loads well but releases poorly, or such low affinity that it releases well but loads poorly. The sigmoidal shape uniquely enables large oxygen delivery across the physiological PO₂ range."
  explanation: "This is why cooperativity is not a molecular curiosity but a physiological necessity. Without it, hemoglobin would need to be present at far higher concentrations (increasing blood viscosity dangerously) or would fail to deliver adequate oxygen to active tissues. The four-subunit, cooperative architecture of hemoglobin is a precisely tuned solution to the problem of oxygen transport across a narrow PO₂ gradient."
```

## Explainer

From your study of protein quaternary structure, you know that hemoglobin is a tetramer — four polypeptide subunits (two alpha, two beta), each carrying an iron-containing heme group capable of binding one molecule of O2. What makes hemoglobin remarkable is not that it binds oxygen, but *how* the binding of oxygen to one subunit changes the behavior of the others. This phenomenon, **cooperativity**, produces the characteristic sigmoidal (S-shaped) oxygen-hemoglobin dissociation curve and is the key to hemoglobin's physiological superiority over a simple oxygen carrier.

In its deoxygenated state, hemoglobin exists in the **T (tense) state**, a conformation held together by salt bridges and hydrogen bonds between subunits that constrain the heme pockets and make oxygen binding difficult. When the first O2 molecule binds to a heme iron, it pulls the iron atom into the plane of the porphyrin ring, tugging the attached histidine residue and triggering a conformational shift in that subunit. This local change propagates through subunit interfaces, breaking stabilizing contacts and progressively shifting the entire tetramer toward the **R (relaxed) state**, which has much higher oxygen affinity. The result is that the first oxygen is hardest to bind, the second and third are progressively easier, and the fourth binds most readily. On a binding curve, this produces the steep middle section of the sigmoid — a small increase in oxygen partial pressure causes a large jump in saturation.

The physiological payoff of cooperativity becomes clear when you compare hemoglobin to **myoglobin**, a monomeric oxygen-binding protein in muscle. Myoglobin has a hyperbolic binding curve: it loads oxygen readily at low partial pressures but releases it reluctantly. Hemoglobin's sigmoidal curve means it is nearly fully saturated (~98%) at the high PO2 found in the lungs (~100 mmHg) but releases a large fraction of its oxygen at the lower PO2 of metabolically active tissues (~40 mmHg). The steep portion of the curve falls exactly in the physiological range, making hemoglobin an efficient oxygen delivery system rather than merely a storage molecule.

Several factors fine-tune this delivery by shifting the dissociation curve. The **Bohr effect** describes how increased H+ concentration (lower pH) and increased PCO2 — both signals of active metabolism — shift the curve rightward, decreasing hemoglobin's oxygen affinity and promoting O2 release precisely where it is needed most. Elevated temperature has the same rightward-shifting effect. **2,3-Bisphosphoglycerate (2,3-BPG)**, produced by red blood cells during glycolysis, binds in the central cavity of deoxyhemoglobin and stabilizes the T state, further reducing oxygen affinity. At high altitude, 2,3-BPG levels increase as an adaptive response, facilitating oxygen unloading to tissues despite lower arterial PO2. Conversely, fetal hemoglobin (HbF) has gamma subunits that bind 2,3-BPG less tightly, giving it a left-shifted curve and higher oxygen affinity — essential for extracting oxygen from maternal blood across the placenta.
