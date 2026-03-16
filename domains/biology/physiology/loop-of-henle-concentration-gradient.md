---
id: loop-of-henle-concentration-gradient
title: Loop of Henle and Osmotic Gradient Generation
domain: biology
course: physiology
prerequisites:
- id: proximal-tubule-reabsorption-secretion
  type: hard
- id: osmosis-and-water-movement
  type: soft
builds-toward:
- collecting-duct-water-reabsorption
tags:
- countercurrent-multiplier
- osmotic-gradient
- medullary-osmolarity
stage: formal-systems
status: draft
---

# Loop of Henle and Osmotic Gradient Generation

## Core Idea
The loop of Henle operates as a countercurrent multiplier to generate an osmotic gradient in the medullary interstitium, with the thick ascending limb actively pumping out sodium and chloride while remaining impermeable to water, establishing a medullary osmolarity of ~1200 mOsm/L. This gradient enables the collecting duct to regulate urine osmolarity from 50 to 1200 mOsm/L.

## Explainer

From the proximal tubule, you know that about 65% of filtered water and solutes are reabsorbed before fluid reaches the loop of Henle. From osmosis, you know that water flows passively from regions of low solute concentration to regions of high solute concentration. The loop of Henle's job is to build the osmotic gradient that makes it possible for the kidney to produce urine that is either much more dilute or much more concentrated than plasma — a feat essential for surviving both desert dehydration and excessive water intake.

The loop has two limbs with fundamentally different properties. The **descending limb** is permeable to water but relatively impermeable to solutes. As filtrate flows down into the increasingly salty medullary interstitium, water is drawn out by osmosis, and the tubular fluid becomes progressively more concentrated — reaching roughly 1200 mOsm/L at the hairpin turn in long-looped nephrons. The **thick ascending limb** has the opposite profile: it is impermeable to water but actively pumps sodium, potassium, and chloride out of the tubular fluid via the **Na⁺/K⁺/2Cl⁻ cotransporter (NKCC2)**. Because water cannot follow these ions, the tubular fluid becomes progressively more dilute as it ascends — dropping to about 100 mOsm/L by the time it reaches the distal convoluted tubule. This is why the ascending limb is called the **diluting segment**.

The ingenious feature is that the two limbs work together as a **countercurrent multiplier**. The ascending limb pumps salt into the interstitium, which raises the interstitial osmolarity. This increased osmolarity draws more water out of the adjacent descending limb, which concentrates the descending fluid further. That more concentrated fluid then rounds the hairpin turn and enters the ascending limb, delivering an even saltier load for the ascending limb to pump out. Each cycle amplifies the gradient slightly. The net effect is that a modest single transporter effect (~200 mOsm/L difference at any one horizontal level) is multiplied along the length of the loop into a massive gradient — from 300 mOsm/L at the cortex to roughly 1200 mOsm/L at the papilla tip. The **vasa recta** (hairpin capillaries running parallel to the loop) preserve this gradient by operating as countercurrent exchangers rather than washing it away.

This medullary gradient is the kidney's master tool for controlling urine concentration. On its own, the loop of Henle does not decide how much water the body retains — it simply builds and maintains the osmotic landscape. The actual decision is made downstream in the collecting duct, where antidiuretic hormone controls water permeability. But without the loop's gradient, the collecting duct would have nothing to work with. Loop diuretics like **furosemide** block the NKCC2 transporter in the thick ascending limb, collapsing the medullary gradient and producing copious dilute urine — which is why they are among the most powerful diuretics in clinical medicine.
