---
id: renal-filtration-and-tubular-processing
title: Renal Filtration and Tubular Processing
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: kidney-anatomy-and-urine-formation
  type: hard
- id: glomerular-filtration-barrier-and-proteinuria
  type: hard
- id: vascular-physiology-and-hemodynamics
  type: hard
builds-toward:
- fluid-electrolyte-regulation-and-osmolarity
- renal-regulation-acid-base
tags:
- glomerular-filtration
- tubular-reabsorption
- selectivity
- gfr
stage: formal-systems
status: validated
---

# Renal Filtration and Tubular Processing

## Core Idea
The kidney filters ~180 liters of plasma daily at the glomerulus, reabsorbing 99% while selectively excreting wastes. Glomerular filtration is driven by Starling forces and limited by the filtration barrier's selective permeability. Proximal tubule reabsorbs glucose, amino acids, and water through active transport and osmosis. The loop of Henle multiplies osmolarity through countercurrent multiplication, allowing the kidney to produce urine more concentrated than plasma.

## Questions

```yaml
- question: "A patient receives a drug that completely blocks NKCC2 (the Na-K-2Cl cotransporter in the ascending limb of the loop of Henle). Even with normal ADH levels, the patient fails to concentrate urine above plasma osmolarity. Why?"
  type: multiple-choice
  options:
    - "NKCC2 blockade prevents water reabsorption in the proximal tubule, flooding the collecting duct"
    - "Without NKCC2 activity, the medullary concentration gradient cannot be established, so ADH has no osmotic gradient to exploit when it opens aquaporins in the collecting duct"
    - "NKCC2 is required for ADH to bind its receptor in the collecting duct principal cells"
    - "Blocking NKCC2 prevents filtrate from entering the descending limb of the loop of Henle"
  answer: 1
  explanation: "NKCC2 is the molecular engine of countercurrent multiplication: by actively pumping solute out of the impermeable ascending limb, it loads the medullary interstitium and establishes the osmolarity gradient (~300 to ~1200 mOsm/kg from cortex to papilla). ADH works by inserting aquaporin channels in the collecting duct, allowing water to follow this gradient into the hypertonic medulla. Without the gradient (NKCC2 blocked), there is nothing for water to follow regardless of how much ADH is present. This is precisely the mechanism of loop diuretics (furosemide), which block NKCC2 clinically."

- question: "What is the approximate osmolarity of the tubular fluid leaving the thick ascending limb of the loop of Henle and entering the distal tubule?"
  type: multiple-choice
  options:
    - "~1200 mOsm/kg — highly concentrated after traversing the hypertonic medulla"
    - "~300 mOsm/kg — isosmotic with plasma, unchanged from the proximal tubule"
    - "~100 mOsm/kg — hypotonic, because the ascending limb pumped out solute without allowing water to follow"
    - "~600 mOsm/kg — intermediate, reflecting partial concentration by the loop"
  answer: 2
  explanation: "The ascending limb actively pumps NaCl out via NKCC2 but is impermeable to water — so solute leaves but water cannot follow. The tubular fluid becomes progressively diluted as it ascends. By the time it exits at the cortex, the fluid is actually hypotonic (~100 mOsm/kg), less concentrated than plasma. This is counterintuitive but critical: the loop is a concentration-gradient generator for the medullary interstitium, not for the tubular fluid itself. The hypotonic fluid then passes to the collecting duct, where ADH determines final concentration by allowing water to flow out into the hypertonic medulla."

- question: "The ascending limb of the loop of Henle is impermeable to water while actively transporting solutes outward — this asymmetry is what allows countercurrent multiplication to work."
  type: true-false
  answer: true
  explanation: "Countercurrent multiplication requires the functional asymmetry between the two limbs. The descending limb is water-permeable but solute-impermeable: descending into the hypertonic medulla, water exits and solute enters, concentrating tubular fluid. The ascending limb is the opposite: NKCC2 pumps solute out but water cannot follow, loading the interstitium and diluting the tubular fluid simultaneously. If the ascending limb were water-permeable, water would follow transported solute into the interstitium, dissipating the gradient — countercurrent multiplication would fail entirely."

- question: "Under normal conditions, glucose is present in urine because the proximal tubule can only reabsorb approximately 80% of filtered glucose."
  type: true-false
  answer: false
  explanation: "Under normal conditions, essentially 100% of filtered glucose is reabsorbed in the proximal tubule via SGLT2 (and SGLT1 distally). Glucose does not appear in urine under normal physiological conditions. Glucosuria occurs only when plasma glucose is so high that the filtered load exceeds the transport maximum of the SGLT transporters — classically in uncontrolled diabetes mellitus (plasma glucose above ~180–200 mg/dL). Detecting glucose in urine is a reliable indicator of hyperglycemia precisely because normal renal glucose reabsorption is essentially complete."

- question: "Explain why the loop of Henle is essential for producing concentrated urine, even though ADH acts on the collecting duct, not the loop itself."
  type: short-answer
  answer: "The loop of Henle builds the medullary osmolarity gradient through countercurrent multiplication — pumping solute into the medullary interstitium against a water-impermeable barrier. This pre-established gradient is what ADH exploits: when ADH inserts aquaporins in the collecting duct, water flows out passively along the osmotic gradient into the hypertonic medulla. Without the loop's gradient, ADH has no osmotic force to drive water reabsorption and concentrated urine cannot be produced."
  explanation: "The loop and the collecting duct perform complementary, interdependent functions: the loop creates the gradient (active, energy-requiring, ADH-independent); the collecting duct exploits it (passive water flow, gated by ADH). Neither alone can produce concentrated urine. This is also why loop diuretics (furosemide) are so potent: blocking NKCC2 erases the medullary gradient, preventing any urinary concentration regardless of ADH levels — demonstrating that the gradient, not ADH alone, is the rate-limiting factor."
```

## Explainer

You have studied the kidney's gross anatomy and the selectivity of the glomerular filtration barrier. Now the question is: how does a process that filters 180 liters of plasma per day produce only 1–2 liters of urine? The answer is a precisely orchestrated sequence of reabsorption and secretion across four nephron segments: the **proximal convoluted tubule**, the **loop of Henle**, the **distal convoluted tubule**, and the **collecting duct**.

**Glomerular filtration** is governed by the same Starling forces that drive fluid movement across any capillary — the balance of hydrostatic pressure (pushing fluid out) against oncotic pressure from plasma proteins (pulling fluid back in). In the glomerular capillaries, hydrostatic pressure is unusually high (~55 mmHg) because the afferent arteriole is wider than the efferent arteriole, creating a high-resistance downstream bottleneck. The **glomerular filtration barrier** — fenestrated endothelium, the glomerular basement membrane, and podocyte slit diaphragms — is size- and charge-selective. Small molecules (water, ions, glucose, amino acids, urea, creatinine) freely cross; large proteins and blood cells do not. The resulting **filtrate** is essentially protein-free plasma.

The **proximal tubule** performs the bulk of reabsorption: approximately 65–70% of filtered sodium, water, and chloride, plus nearly 100% of filtered glucose and amino acids. Glucose reabsorption uses sodium-glucose cotransporters (SGLT2) on the luminal membrane — the same cotransport mechanism used in intestinal absorption. The proximal tubule also secretes organic acids, drugs, and metabolic waste products into the lumen. Crucially, water reabsorption here is obligatory and isosmotic — water follows solute proportionally — so the filtrate leaving the PCT has the same osmolarity as plasma (~300 mOsm/kg) but only one-third the original volume.

The **loop of Henle** does something qualitatively different: it creates a concentration gradient in the medullary interstitium without which concentrated urine is impossible. This is **countercurrent multiplication**. The descending limb is water-permeable but poorly permeable to solutes; the ascending limb actively pumps out sodium and chloride but is impermeable to water. As filtrate descends into the progressively hypertonic medullary interstitium, water exits and solute enters, concentrating the tubular fluid. As the fluid then ascends, the sodium-potassium-chloride cotransporter (NKCC2) pumps solute out without water following, diluting the luminal fluid. The net effect: filtrate leaving the ascending limb at the cortex is actually hypotonic (~100 mOsm/kg), but the medullary interstitium has been loaded to ~1200 mOsm/kg at the papillary tip. This medullary gradient is the "potential energy" stored for water reabsorption in the collecting duct when ADH is present — the mechanism you will study next in fluid and electrolyte regulation.
