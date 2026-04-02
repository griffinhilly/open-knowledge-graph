---
id: renal-regulation-acid-base
title: Renal Regulation of Acid-Base Balance
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: acid-base-homeostasis-physiology
  type: hard
- id: renal-filtration-and-tubular-processing
  type: hard
- id: acid-base-chemistry
  type: soft
- id: acid-base-balance-respiratory-renal-compensation
  type: soft
builds-toward:
- metabolic-acidosis-alkalosis-disorders
tags:
- bicarbonate-reabsorption
- acid-secretion
- ammonia-excretion
stage: advanced
status: validated
---
# Renal Regulation of Acid-Base Balance

## Core Idea
The kidney compensates for respiratory acid-base disorders and corrects metabolic disorders through three mechanisms: reabsorption of filtered bicarbonate, secretion of hydrogen ions, and excretion of ammonia (which buffers acid). Proximal tubule reclaims filtered bicarbonate through H⁺ secretion. Distal tubule and collecting duct secrete hydrogen ions to establish larger gradients. Chronic acid-base disorders are primarily corrected by renal mechanisms.

## Questions

```yaml
- question: "A patient has been in chronic metabolic acidosis for 5 days. Which renal mechanism is most responsible for the large increase in net acid excretion observed over this time period?"
  type: multiple-choice
  options:
    - "Increased bicarbonate filtration at the glomerulus, which provides more substrate for H⁺ buffering in the tubule"
    - "Upregulated ammonium (NH₄⁺) production and excretion — proximal tubule cells metabolize glutamine to generate NH₃, which buffers secreted H⁺ and is excreted as NH₄⁺"
    - "Increased respiratory rate, which reduces PCO₂ and allows the kidney to excrete more CO₂"
    - "Increased distal tubule bicarbonate reabsorption, which frees up H⁺ for direct excretion"
  answer: 1
  explanation: "The ammonia pathway is the most flexible and upregulatable mechanism for net acid excretion during sustained acidosis. During chronic acidosis, proximal tubule cells dramatically increase glutamine uptake and metabolism, stripping amino groups as NH₃. NH₃ diffuses into the lumen and combines with secreted H⁺ to form NH₄⁺, which is trapped (charged, membrane-impermeant) and excreted. This mechanism can increase many-fold over days, providing the large, sustained acid excretion capacity needed to correct chronic acidosis."

- question: "In the proximal tubule, H⁺ is actively secreted into the tubular lumen via Na⁺/H⁺ exchangers. What is the primary fate of this secreted H⁺?"
  type: multiple-choice
  options:
    - "It accumulates in the tubular fluid, progressively acidifying the urine along the proximal tubule"
    - "It combines with filtered bicarbonate to form H₂CO₃, which is converted to CO₂ and water — effectively reabsorbing bicarbonate rather than excreting acid"
    - "It directly neutralizes metabolic acids (like lactic acid) filtered at the glomerulus"
    - "It is secreted into the peritubular capillaries to buffer venous blood returning to the heart"
  answer: 1
  explanation: "This is the key distinction between bicarbonate reabsorption and net acid secretion. In the proximal tubule, the secreted H⁺ does not accumulate as free acid — it immediately combines with filtered HCO₃⁻ to form carbonic acid (H₂CO₃), which carbonic anhydrase converts to CO₂ and water. The CO₂ diffuses into the tubular cell, is rehydrated back to H₂CO₃, and the resulting HCO₃⁻ is transported to the blood. The net result: filtered bicarbonate is reclaimed, but no acid is actually excreted. This process does not acidify the urine."

- question: "Proximal tubule H⁺ secretion directly contributes to net acid excretion by lowering urinary pH in the proximal nephron."
  type: true-false
  answer: false
  explanation: "Proximal tubule H⁺ secretion does NOT acidify the urine or constitute net acid excretion. Every H⁺ secreted in the proximal tubule is consumed in the process of reclaiming filtered bicarbonate — the secreted H⁺ combines with HCO₃⁻, forming CO₂ that diffuses back into the cell. The urine remains near-neutral pH throughout the proximal tubule. Net acid secretion — actual elimination of H⁺ from the body — occurs in the distal tubule and collecting duct, where H⁺ is secreted against a steep gradient and buffered by titratable acids and ammonia rather than bicarbonate."

- question: "The kidneys respond more rapidly to acid-base disturbances than the lungs, but the renal correction is less complete."
  type: true-false
  answer: false
  explanation: "The temporal relationship is reversed. Lungs respond within seconds to minutes by adjusting ventilation rate (increasing or decreasing CO₂ elimination). Kidneys respond over hours to days, requiring time to upregulate transporters, enzymes (carbonic anhydrase), and ammonia production pathways. However, the renal correction is more complete and durable: lungs can only partially compensate (they cannot fully normalize pH in metabolic disorders without overshooting respiratory control), while the kidney can precisely adjust bicarbonate reabsorption and acid secretion to fully correct the disturbance over time."

- question: "Distinguish between bicarbonate reabsorption and net acid excretion: where does each occur in the nephron, what is the mechanism, and why does only one of them actually correct an acid-base imbalance?"
  type: short-answer
  answer: "Bicarbonate reabsorption occurs mainly in the proximal tubule: H⁺ is secreted into the lumen, combines with filtered HCO₃⁻, and the resulting CO₂ re-enters the cell to regenerate HCO₃⁻ for the blood. No acid is eliminated — the secreted H⁺ is consumed reclaiming bicarbonate, not added to the urine. Net acid excretion occurs in the distal tubule and collecting duct: alpha-intercalated cells pump H⁺ against a steep gradient, buffered by titratable acids (phosphate) and ammonia (NH₄⁺). This H⁺ leaves the body in the urine, and each excreted H⁺ is matched by a new HCO₃⁻ added to the blood. Only net acid excretion corrects an acid-base imbalance — bicarbonate reabsorption merely prevents bicarbonate loss, maintaining balance, but does not generate new bicarbonate to replace that consumed by buffering acids."
  explanation: "This distinction is the most commonly confused aspect of renal acid-base physiology. Both processes involve H⁺ secretion, but the fate of that H⁺ is completely different: in the proximal tubule it is recycled back into bicarbonate; in the distal nephron it exits the body as buffered acid. Only the distal process actually removes an acid load."
```

## Explainer

From your study of acid-base homeostasis, you know that blood pH is maintained near 7.4 by the carbonic acid–bicarbonate buffer system, with the lungs controlling CO₂ and the kidneys controlling bicarbonate (HCO₃⁻). The lungs respond to pH changes within seconds to minutes by adjusting ventilation; the kidneys respond over hours to days but produce lasting corrections. Understanding how the kidney does this requires tracking protons (H⁺) through the nephron.

The first and quantitatively largest mechanism is **bicarbonate reabsorption** in the proximal tubule. About 180 liters of plasma are filtered daily, containing roughly 4,500 mEq of bicarbonate that must be reclaimed or it would be lost in urine. Tubular cells secrete H⁺ into the lumen (via Na⁺/H⁺ exchangers), where it combines with filtered HCO₃⁻ to form H₂CO₃, which carbonic anhydrase rapidly converts to CO₂ and water. The CO₂ diffuses into the tubular cell, where it is re-converted to HCO₃⁻ and transported back to blood. This process does not acidify the urine — the secreted H⁺ is consumed reclaiming bicarbonate rather than accumulating as free acid.

**Net acid secretion** — the actual elimination of acid from the body — occurs in the distal tubule and collecting duct. Here, specialized alpha-intercalated cells pump H⁺ against a steep gradient (urine can reach pH 4.5, meaning H⁺ concentration 1,000× higher than blood). This H⁺ is buffered in the tubular lumen primarily by **titratable acids** (especially phosphate) and by **ammonium (NH₄⁺)**. The ammonium pathway is particularly important during chronic acidosis: glutamine released from muscle is taken up by proximal tubule cells, which strip off amino groups as ammonia (NH₃). NH₃ diffuses into the lumen and accepts a proton to become NH₄⁺, which is trapped in the urine and excreted. This mechanism can be upregulated many-fold during sustained acidosis, providing a large and flexible acid-excretion capacity.

The renal response to respiratory disorders illustrates the compensation principle you learned earlier. In respiratory acidosis (high PCO₂, low pH), the kidneys compensate by increasing H⁺ secretion and HCO₃⁻ retention — raising plasma bicarbonate to restore the ratio [HCO₃⁻]/[CO₂] and partially normalize pH. In respiratory alkalosis (low PCO₂, high pH), the kidneys reduce HCO₃⁻ reabsorption, letting more bicarbonate escape in urine. These compensations develop over 2–5 days. In metabolic disorders, the kidney is not compensating for something else — it is the primary site of pathology or correction. Metabolic acidosis (low bicarbonate) prompts maximum acid excretion and bicarbonate regeneration; metabolic alkalosis (high bicarbonate) prompts bicarbonate excretion. The kidney's power over long-term acid-base balance is unmatched: respiratory compensation is faster, but renal correction is more complete and more durable.
