---
id: renal-physiology-and-fluid-balance
title: Renal Physiology and Fluid Balance
domain: biology
course: physiology
prerequisites:
- id: homeostasis-and-feedback
  type: hard
- id: active-transport
  type: hard
- id: passive-transport
  type: hard
- id: blood-pressure-regulation
  type: soft
- id: solution-concentration
  type: soft
- id: colligative-properties
  type: soft
- id: capillary-filtration-and-reabsorption
  type: soft
tags:
- kidney
- nephron
- filtration
- reabsorption
- ADH
- aldosterone
- fluid balance
stage: formal-systems
status: validated
---

# Renal Physiology and Fluid Balance

## Core Idea
The kidneys regulate plasma osmolarity, electrolyte concentrations, blood volume, pH, and blood pressure by filtering approximately 180 L of plasma per day at the glomeruli and then selectively reabsorbing and secreting solutes along the nephron tubule. Four sequential segments perform distinct functions: the proximal convoluted tubule handles bulk reabsorption of glucose, amino acids, Na⁺, and bicarbonate with obligate water following; the loop of Henle establishes the medullary osmotic gradient via countercurrent multiplication; the distal convoluted tubule and collecting duct perform fine-tuning under hormonal control (ADH increases water permeability; aldosterone drives Na⁺ reabsorption and K⁺ secretion). The final urine composition reflects the hormonal state — dehydration triggers ADH release, producing small volumes of concentrated urine.

## How It's Best Learned
Trace the fate of three filtered solutes: glucose (completely reabsorbed in the proximal tubule via SGLT2; appears in urine only above the renal threshold of ~180 mg/dL); Na⁺ (reabsorbed throughout, with the final 2% controlled by aldosterone); K⁺ (filtered, mostly reabsorbed, then secreted under aldosterone in the collecting duct). Predict the urine profile in diabetes insipidus (absent ADH): large volume, very dilute, low osmolarity.

## Common Misconceptions
- The kidneys do not simply 'filter out' toxins; they maintain composition by retaining what is valuable (glucose, amino acids) and excreting what is excess or foreign.
- Glycosuria (glucose in urine) indicates that blood glucose exceeded the transport maximum of SGLT2, not that the kidneys are damaged.
- Aldosterone acts primarily on the collecting duct to increase Na⁺ reabsorption and K⁺ excretion; it does not directly control water reabsorption — ADH does that.

## Questions

```yaml
- question: "A patient with elevated blood osmolarity will experience which hormonal response to restore fluid balance?"
  type: multiple-choice
  options: ["Aldosterone release, causing Na⁺ reabsorption and water retention", "ADH release, increasing water permeability of the collecting duct", "Aldosterone release, causing K⁺ reabsorption in the distal tubule", "ADH release, increasing Na⁺ secretion in the proximal tubule"]
  answer: 1
  explanation: "High plasma osmolarity triggers ADH (antidiuretic hormone) release from the posterior pituitary. ADH inserts aquaporin channels into the collecting duct, increasing water reabsorption and producing small volumes of concentrated urine. Aldosterone responds to low blood pressure or low Na⁺ — not directly to osmolarity."

- question: "Aldosterone directly controls water reabsorption in the collecting duct."
  type: true-false
  answer: false
  explanation: "This is a common misconception. Aldosterone drives Na⁺ reabsorption and K⁺ secretion in the distal convoluted tubule and collecting duct, but water follows Na⁺ passively only when water channels are present. ADH controls water permeability by regulating aquaporin insertion. The two hormones are complementary but distinct in their primary targets."

- question: "Why does glucose appear in the urine of a patient with uncontrolled diabetes mellitus, even though the kidneys are structurally normal?"
  type: short-answer
  answer: "Blood glucose exceeds the transport maximum (Tmax) of the SGLT2 cotransporter in the proximal convoluted tubule. When the filtered glucose load surpasses ~180 mg/dL, the carriers are saturated and the excess glucose cannot be reabsorbed, so it passes into the urine."
  explanation: "Glycosuria reflects transporter saturation, not kidney damage. The proximal tubule normally reabsorbs 100% of filtered glucose via SGLT2 cotransporters, but these have finite capacity. Above the renal threshold (~180 mg/dL plasma glucose), the filtered load overwhelms transport capacity and glucose spills into the urine."
```

## Explainer

The kidneys are not simple filters that remove waste — they are precision regulators that filter an enormous volume (about 180 L of plasma per day) and then recover most of what the body needs. Understanding this begins with the nephron, the functional unit of the kidney, where filtration and selective recovery happen in sequential stages.

At the glomerulus, blood pressure forces water and small solutes (glucose, amino acids, Na⁺, K⁺, urea, bicarbonate) into the tubule. Larger molecules like proteins stay in the blood. The proximal convoluted tubule then performs bulk recovery: Na⁺ enters tubule cells via cotransporters that carry glucose and amino acids along with it, and water follows osmotically. About 65% of filtered water and Na⁺ is recovered here. Because transport capacity is finite, solutes like glucose only appear in urine when plasma concentrations exceed the transporter maximum — which is why glycosuria signals hyperglycemia, not kidney failure.

The loop of Henle creates the medullary osmotic gradient that makes concentrated urine possible. The descending limb is permeable to water but not salt, so water leaves as tubular fluid descends into the increasingly salty medulla. The ascending limb is impermeable to water but actively pumps Na⁺ and Cl⁻ out, building up medullary concentration. This countercurrent arrangement means the deeper you go, the more concentrated the tissue — a gradient that later segments exploit.

The final composition of urine is determined by hormonal fine-tuning in the distal tubule and collecting duct. ADH (antidiuretic hormone), released when plasma osmolarity rises or blood volume falls, inserts aquaporin channels into the collecting duct wall, allowing water to follow the medullary gradient into the bloodstream. The result is small volumes of concentrated urine. Aldosterone, released when blood pressure or Na⁺ is low, stimulates Na⁺ reabsorption and K⁺ secretion in the same segment. These two hormones are independent: ADH controls water; aldosterone controls sodium.

A useful diagnostic exercise: predict urine characteristics in diabetes insipidus, where ADH is absent or ineffective. Without aquaporins in the collecting duct, water cannot be reabsorbed despite the medullary gradient. The result is large volumes (polyuria) of dilute urine with very low osmolarity — a direct demonstration of ADH's essential role in concentrating the final product.
