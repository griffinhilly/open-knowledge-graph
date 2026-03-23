---
id: collecting-duct-water-reabsorption-adh
title: Collecting Duct Water Reabsorption and Antidiuretic Hormone
domain: biology
course: physiology
prerequisites:
- id: loop-of-henle-countercurrent-concentration
  type: hard
- id: hormone-signaling-mechanisms
  type: hard
- id: hypothalamus-pituitary-axis
  type: soft
builds-toward:
- electrolyte-balance-renal-hormonal-control
tags:
- water balance
- ADH
- collecting duct
- homeostasis
stage: formal-systems
status: draft
---

# Collecting Duct Water Reabsorption and Antidiuretic Hormone

## Core Idea
The collecting duct's water permeability is controlled by antidiuretic hormone (ADH/vasopressin), which binds V2 receptors on principal cells and increases the number of aquaporin-2 water channels on the apical membrane via cAMP-dependent translocation. With elevated ADH (dehydration, osmolarity >300 mOsm/kg), the duct becomes permeable to water and reabsorbs water down the osmotic gradient, producing small volumes of concentrated urine. With low ADH (overhydration, osmolarity <280 mOsm/kg), the duct remains impermeable to water and produces large volumes of dilute urine. Osmoreceptors in the hypothalamus continuously sense plasma osmolarity and adjust ADH secretion, maintaining homeostasis within narrow limits.

## How It's Best Learned
Measure plasma osmolarity, ADH, and urine osmolarity in response to hypertonic saline (osmotic challenge) or water loading. Understand nephrogenic diabetes insipidus as loss of aquaporin-2 responsiveness and central diabetes insipidus as ADH deficiency.

## Common Misconceptions
ADH does not increase sodium reabsorption in the collecting duct; it specifically affects water permeability. Hypernatremia with elevated ADH (nephrogenic DI) differs from hypernatremia with low ADH (central DI) in cause and treatment.

## Questions

```yaml
- question: "A patient produces massive volumes of very dilute urine. Laboratory testing shows plasma ADH levels are markedly elevated. What is the most likely diagnosis, and what does the molecular defect involve?"
  type: multiple-choice
  options:
    - "Central diabetes insipidus — the hypothalamus is not producing adequate ADH"
    - "Syndrome of inappropriate ADH — too much ADH is causing water retention and dilute urine"
    - "Nephrogenic diabetes insipidus — the collecting duct is unable to respond to ADH, likely due to defective V2 receptors or aquaporin-2 channels"
    - "Normal physiology — high ADH with dilute urine occurs after large water intake"
  answer: 2
  explanation: "Elevated ADH with continued production of dilute urine is the hallmark of nephrogenic diabetes insipidus (NDI). ADH is present and secreted normally (ruling out central DI), but the collecting duct cannot respond — either because V2 receptors are defective and cannot transduce the signal, or because aquaporin-2 channels are absent or cannot be trafficked to the apical membrane. The medullary osmotic gradient exists, but without functional aquaporins, the collecting duct is waterproof regardless of how much ADH circulates."

- question: "A researcher adds ADH to isolated collecting duct cells but simultaneously blocks the cAMP signaling pathway. What happens to aquaporin-2 trafficking and water permeability?"
  type: multiple-choice
  options:
    - "AQP2 channels are still inserted into the apical membrane because ADH binds directly to aquaporin-2"
    - "Water permeability increases via an alternative cAMP-independent pathway activated by ADH"
    - "AQP2 channels remain in intracellular vesicles and water permeability stays low, because cAMP is required for the vesicle fusion that inserts AQP2 into the apical membrane"
    - "ADH cannot bind V2 receptors without cAMP present, so no signaling occurs at all"
  answer: 2
  explanation: "ADH acts by binding V2 receptors on the basolateral membrane, which activates adenylate cyclase and raises intracellular cAMP. The cAMP-dependent protein kinase A then phosphorylates targets that drive vesicle fusion, inserting AQP2-containing vesicles into the apical membrane. If cAMP is blocked, this phosphorylation cascade cannot proceed, and AQP2 channels stay sequestered in intracellular vesicles — the apical membrane remains effectively waterproof. This is why cAMP is the essential intermediate between ADH binding and aquaporin insertion."

- question: "ADH increases both water reabsorption and sodium reabsorption in the collecting duct, making it a general antidiuretic agent."
  type: true-false
  answer: false
  explanation: "ADH acts specifically on water permeability through aquaporin-2 channel insertion — it does not increase sodium reabsorption in the collecting duct. Sodium transport in the collecting duct is primarily regulated by aldosterone, which acts on principal cells to increase ENaC (epithelial sodium channel) activity and Na⁺/K⁺-ATPase expression. Conflating ADH with aldosterone is a common error. ADH's name ('antidiuretic hormone') refers specifically to its ability to reduce urine volume by increasing water reabsorption, not by altering sodium handling."

- question: "Without ADH, the medullary osmotic gradient built by the loop of Henle cannot drive water reabsorption from the collecting duct, because the collecting duct is essentially impermeable to water in the absence of aquaporin-2 channels on the apical membrane."
  type: true-false
  answer: true
  explanation: "This is the key insight of the collecting duct system. The loop of Henle creates the osmotic gradient (300–1200 mOsm from cortex to medulla) that provides the thermodynamic driving force for water reabsorption. But having a concentration gradient is not sufficient — the membrane must also be permeable for osmosis to occur. Without ADH, AQP2 channels are sequestered in intracellular vesicles and absent from the apical membrane. The collecting duct epithelium is effectively waterproof, and the gradient is wasted. ADH is the gatekeeper that determines whether the gradient can actually drive water reabsorption."

- question: "Why is the medullary osmotic gradient necessary but not sufficient for the kidney to produce concentrated urine? What is the other essential component, and what physiological signal controls it?"
  type: short-answer
  answer: "The medullary osmotic gradient (built by the loop of Henle and vasa recta) provides the thermodynamic driving force for water reabsorption — concentrated interstitium relative to tubular fluid creates the osmotic pressure that would pull water out. But this force is useless unless the collecting duct membrane is permeable to water. The essential second component is aquaporin-2 (AQP2) water channel expression on the apical membrane of collecting duct principal cells. Without these channels, the epithelium is impermeable regardless of how large the gradient is. ADH (vasopressin) controls aquaporin-2 insertion: when plasma osmolarity rises above ~285–295 mOsm/kg, osmoreceptors in the hypothalamus trigger ADH release from the posterior pituitary, which binds V2 receptors on principal cells, raises cAMP, and drives AQP2 vesicle fusion with the apical membrane — opening the gates for water to follow the gradient."
  explanation: "This two-component logic — gradient plus permeability gate — explains why both central and nephrogenic diabetes insipidus produce dilute urine despite having a normal medullary gradient: central DI lacks the signal (ADH), nephrogenic DI lacks the response (aquaporin insertion). Treating them requires targeting the deficient component: ADH replacement for central DI, strategies that bypass the V2 receptor/cAMP pathway for nephrogenic DI."
```

## Explainer

From your study of the loop of Henle, you know that the kidney builds a steep osmotic gradient in the medullary interstitium — ranging from about 300 mOsm/L at the cortex to 1200 mOsm/L at the inner medulla. From hormone signaling, you know that hormones bind receptors and activate intracellular cascades that change cell behavior. The collecting duct is where these two concepts converge: the medullary gradient provides the driving force for water reabsorption, and **antidiuretic hormone (ADH)** — also called vasopressin — controls whether the collecting duct actually allows water to follow that gradient.

The collecting duct runs from the cortex deep into the medulla, passing through progressively more concentrated interstitial fluid. When ADH is present, it binds to **V2 receptors** on the basolateral membrane of principal cells lining the duct. This triggers a cAMP-dependent signaling cascade that causes intracellular vesicles containing **aquaporin-2 (AQP2)** water channels to fuse with the apical (luminal) membrane. With aquaporin-2 channels inserted, the luminal membrane becomes permeable to water. Water then flows by osmosis from the tubular fluid (which is dilute, around 100–150 mOsm/L after processing by the diluting segment) into the hypertonic medullary interstitium, and from there into the vasa recta capillaries. The result is a small volume of highly concentrated urine — up to 1200 mOsm/L.

When ADH levels are low — as occurs after drinking a large volume of water — the aquaporin-2 channels are removed from the apical membrane by endocytosis and stored in intracellular vesicles. Without these channels, the collecting duct epithelium is essentially waterproof. The dilute tubular fluid passes straight through the duct without being concentrated, and the kidney produces large volumes of dilute urine (as low as 50 mOsm/L). This is the mechanism behind the familiar experience of frequent, clear urination after drinking excess water.

The control loop is elegantly simple. **Osmoreceptors** in the hypothalamus continuously monitor plasma osmolarity. When osmolarity rises above the set point (roughly 285–295 mOsm/kg), these neurons shrink slightly due to water loss, which increases their firing rate and stimulates ADH release from the posterior pituitary. ADH circulates to the kidney and opens the aquaporin gates, water is reabsorbed, plasma osmolarity falls, and ADH secretion decreases — a classic negative feedback loop. Disease can break this loop at two points: **central diabetes insipidus** results from insufficient ADH production (damaged hypothalamus or pituitary), while **nephrogenic diabetes insipidus** results from the collecting duct failing to respond to ADH (defective V2 receptors or aquaporin-2 channels). Both produce the same symptom — massive output of dilute urine — but they differ fundamentally in mechanism and treatment.
