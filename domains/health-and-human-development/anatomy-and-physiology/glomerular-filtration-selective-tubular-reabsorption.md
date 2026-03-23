---
id: glomerular-filtration-selective-tubular-reabsorption
title: Glomerular Filtration and Selective Tubular Reabsorption
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: renal-anatomy-and-filtration
  type: hard
- id: blood-vessels-and-circulation
  type: hard
- id: glomerular-filtration-mechanism
  type: soft
- id: selective-permeability-and-membrane-channels
  type: hard
- id: ion-channels-selectivity
  type: hard
- id: osmosis-and-tonicity
  type: soft
- id: active-transport
  type: soft
- id: capillary-filtration-and-reabsorption
  type: hard
builds-toward:
- fluid-balance-and-electrolytes
- renal-regulation-of-fluid-balance
tags:
- glomerular-filtration
- renal-physiology
- GFR
stage: formal-systems
status: draft
---

# Glomerular Filtration and Selective Tubular Reabsorption

## Core Idea
The kidney produces urine through glomerular filtration driven by Starling forces, generating a protein-free ultrafiltrate at ~180 L/day. Selective reabsorption in the proximal tubule recovers essential solutes (glucose, amino acids) and water, the loop of Henle creates concentration gradients for water reabsorption, and the distal tubule and collecting duct fine-tune electrolyte and water balance under hormonal control. Filtration rate is autoregulated despite changing systemic blood pressure.

## How It's Best Learned
Calculate glomerular filtration pressure using Starling forces. Map each nephron segment to its specific transport mechanisms (active, passive, osmotic). Use clearance equations to quantify filtration and reabsorption.

## Questions

```yaml
- question: "The kidney filters approximately 180 liters of plasma per day — roughly 45 times the entire plasma volume. Why filter such an enormous volume rather than selectively filtering only the waste products that need to be excreted?"
  type: multiple-choice
  options:
    - "The kidney filters large volumes because it cannot distinguish waste molecules from useful ones at the glomerular membrane"
    - "High filtration volume increases blood pressure by removing fluid rapidly, protecting downstream organs"
    - "Mass filtration followed by selective reabsorption is more physiologically efficient than selective filtering because small solutes cannot be specifically targeted at the glomerulus, but specific transporters can reclaim desired solutes in the tubule"
    - "Filtering large volumes is necessary to maintain osmotic balance with the surrounding medullary tissue"
  answer: 2
  explanation: "The glomerular filtration barrier separates based on size and charge — it passes everything below about 70 kDa (excluding proteins and cells) regardless of whether it is waste or essential. Selective filtering at the inlet would require specific receptors for every waste molecule, which is mechanistically impractical. Instead, the kidney filters nearly everything, then uses specific transporters in the tubule to reclaim glucose, amino acids, and other essentials. This 'filter everything, reclaim what's needed' architecture allows precise, regulated recovery of diverse solutes using dedicated tubular transport proteins."

- question: "The ascending limb of the loop of Henle actively pumps Na+ and Cl- into the medullary interstitium but is impermeable to water. Why is this impermeability to water essential for building the medullary osmotic gradient?"
  type: multiple-choice
  options:
    - "Water impermeability prevents dilution of the tubular fluid, keeping it concentrated for delivery to the collecting duct"
    - "If water could follow the salt out of the ascending limb, the osmotic gradient built by salt pumping would immediately be dissipated — water impermeability decouples salt transport from osmotic equilibration, allowing gradient accumulation"
    - "Water impermeability in the ascending limb forces water to be reabsorbed in the descending limb instead"
    - "The ascending limb needs to remain hypotonic to drive water into the descending limb by osmosis"
  answer: 1
  explanation: "This is the critical asymmetry. If the ascending limb were permeable to water, water would follow Na+ and Cl- osmotically as fast as they were pumped out, and no concentration gradient could build in the medullary interstitium. The impermeability to water allows the solutes to accumulate in the medullary interstitium without dilution — this is what makes the medulla progressively hypertonic from cortex to papilla. The descending limb is the opposite: permeable to water but not salt, so it equilibrates osmotically with the increasingly concentrated medulla as it descends, concentrating the tubular fluid."

- question: "Antidiuretic hormone (ADH) increases water reabsorption in the collecting duct by inserting aquaporin water channels into the apical membrane of collecting duct cells."
  type: true-false
  answer: true
  explanation: "ADH (vasopressin) acts on V2 receptors in collecting duct principal cells, activating a cAMP signaling cascade that causes aquaporin-2 (AQP2) vesicles to fuse with the apical membrane. This dramatically increases water permeability, allowing water to follow the osmotic gradient created by the hypertonic medulla — producing concentrated urine. In the absence of ADH (e.g., in diabetes insipidus), AQP2 channels remain in intracellular vesicles, the collecting duct is water-impermeable, and large volumes of dilute urine are produced regardless of the medullary gradient."

- question: "Under normal physiological conditions, glucose appears in urine because the proximal tubule only partially reabsorbs filtered glucose, allowing the excess to pass into the final urine."
  type: true-false
  answer: false
  explanation: "Under normal conditions, virtually all filtered glucose is reabsorbed in the proximal convoluted tubule via sodium-glucose cotransporters (SGLT1 and SGLT2) on the apical membrane. The proximal tubule has sufficient transport capacity to reclaim 100% of the approximately 180 g of glucose filtered daily. Glucose appears in urine (glucosuria) only when plasma glucose exceeds the tubular transport maximum (~180–200 mg/dL in most individuals), overwhelming the transporter capacity. This is the physiological basis of glucosuria in uncontrolled diabetes mellitus."

- question: "Explain why the kidney's 'filter everything, then selectively reclaim' strategy is physiologically superior to attempting to selectively filter only waste products at the glomerulus."
  type: short-answer
  answer: "The glomerular filtration barrier can only discriminate based on molecular size and charge — it passes all small solutes (glucose, amino acids, electrolytes, urea, creatinine) non-selectively and retains only large proteins and cells. There is no mechanism for the glomerulus to 'recognize' waste molecules and exclude useful ones at that stage. In contrast, the renal tubule is lined with specific transport proteins: SGLT cotransporters for glucose, distinct carriers for each amino acid class, Na+/K+-ATPase driving Na+ reabsorption, and so on. These transporters allow precise, regulated, and energy-controlled reclamation of diverse valuable solutes. The architecture exploits the kidney's comparative advantage: bulk size-based filtration at the glomerulus, precision molecular recognition in the tubule."
  explanation: "This design also provides fine-grained hormonal control: aldosterone regulates Na+ reabsorption, ADH regulates water reabsorption, and PTH regulates phosphate handling — all at the tubular level. A selective-filtration architecture would require hormonal regulation at the glomerular barrier, which is far less mechanistically tractable than modulating tubular transporter expression and activity."
```

## Explainer

The kidney solves a logistical problem that would be impossible to manage with selective filtering at the inlet: it filters almost everything first, then carefully reclaims what the body needs. Your prior study of capillary filtration introduced the Starling forces — hydrostatic pressure pushing fluid out of capillaries, oncotic pressure pulling it back in. The **glomerulus** is a specialized capillary tuft where this balance is deliberately skewed toward filtration. Glomerular capillary pressure (~55 mmHg) far exceeds the oncotic pressure (~30 mmHg) and the opposing pressure in Bowman's capsule (~15 mmHg), yielding a net filtration pressure of ~10 mmHg. The result: roughly 180 liters of plasma water pass into the nephron every day — about 45 times the entire plasma volume.

That filtrate is not urine; it is a nearly perfect copy of plasma minus proteins and cells. The **proximal convoluted tubule** recovers the bulk of it: ~67% of filtered sodium (via Na⁺/K⁺-ATPase on the basolateral membrane creating a gradient that drives apical uptake), virtually all glucose and amino acids (via sodium-coupled cotransporters you studied in active transport), and water following by osmosis. The tubule cells are packed with mitochondria specifically to power this energy-intensive reclamation. From your work on selective permeability and membrane channels, you can recognize that each transport protein is specific to particular solutes — glucose transporters do not move amino acids; different carriers handle different substrates.

The **loop of Henle** creates the osmotic gradient in the medulla that enables concentrated urine. The descending limb is permeable to water but not salt — water leaves by osmosis as the medulla becomes progressively hypertonic. The ascending limb actively pumps Na⁺ and Cl⁻ out but is impermeable to water — this is the critical asymmetry that builds the gradient. The countercurrent arrangement of the two limbs means the bottom of the loop sits in the most concentrated medullary tissue, maximizing the driving force for concentration. Without this mechanism, the deepest part of the nephron would equilibrate with cortical fluid and lose the gradient.

The **distal tubule and collecting duct** perform fine-tuning under hormonal control. **Antidiuretic hormone (ADH)** inserts aquaporin water channels into the collecting duct, making it permeable to water and allowing the medullary gradient to concentrate urine when the body is dehydrated. Without ADH, the collecting duct remains water-impermeable and dilute urine is produced. **Aldosterone** acts on the distal tubule to upregulate Na⁺ reabsorption (retaining volume) and K⁺ secretion. These hormonal controls are what allow the same nephron architecture to produce urine ranging from very dilute (~50 mOsm) to very concentrated (~1200 mOsm) depending on hydration state.

**Autoregulation** keeps the glomerular filtration rate (GFR) remarkably stable despite swings in systemic blood pressure. The myogenic response constricts the afferent arteriole when pressure rises, protecting glomerular capillaries. Tubuloglomerular feedback detects changes in tubular NaCl delivery at the macula densa and adjusts afferent arteriole tone accordingly — a local feedback loop that couples filtration rate to tubular processing capacity. Together these mechanisms hold GFR near 125 mL/min across a wide range of arterial pressures, ensuring that the downstream reclamation machinery is never overwhelmed.
