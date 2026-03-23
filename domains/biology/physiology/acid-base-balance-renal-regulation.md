---
id: acid-base-balance-renal-regulation
title: Acid-Base Balance and Renal Regulation
domain: biology
course: physiology
prerequisites:
- id: collecting-duct-water-reabsorption
  type: hard
- id: carbon-dioxide-transport-and-buffering
  type: soft
- id: acid-base-chemistry
  type: soft
- id: buffer-solutions
  type: soft
tags:
- acid-base
- pH-regulation
- compensatory-responses
stage: formal-systems
status: draft
---

# Acid-Base Balance and Renal Regulation

## Core Idea
The kidneys regulate acid-base balance through reabsorption of filtered bicarbonate (proximal tubule), secretion of hydrogen ions (distal tubule and collecting duct), and excretion of non-volatile acids, with the distal segments as primary fine-tuning sites. Chronic respiratory acidosis or alkalosis triggers renal compensatory responses over days to restore pH toward normal.

## Questions

```yaml
- question: "A patient with chronic obstructive pulmonary disease (COPD) has persistently elevated arterial PCO₂. After 5 days, a blood gas shows elevated plasma [HCO₃⁻] alongside the high PCO₂. What explains the elevated bicarbonate?"
  type: multiple-choice
  options:
    - "The lungs are retaining bicarbonate to compensate for the elevated CO₂"
    - "The kidneys have increased H⁺ secretion and ammoniagenesis, generating new HCO₃⁻ to compensate for the respiratory acidosis"
    - "The elevated bicarbonate is a primary metabolic alkalosis occurring simultaneously with the respiratory acidosis"
    - "Bicarbonate spontaneously rises when CO₂ is high because of the equilibrium CO₂ + H₂O ⇌ H⁺ + HCO₃⁻"
  answer: 1
  explanation: "Chronically elevated PCO₂ (respiratory acidosis) drives pH down. Over 3–5 days, the kidneys respond by increasing distal H⁺ secretion via H⁺-ATPase and increasing ammoniagenesis, trapping more H⁺ as NH₄⁺ in the urine. Each H⁺ secreted distally generates one new HCO₃⁻ returned to blood, raising plasma [HCO₃⁻]. This renal compensation improves but does not normalize pH. Option D is superficially plausible — the equilibrium does shift — but this is a short-term chemical effect, not the sustained elevation seen days later. The lungs (option A) do not handle bicarbonate directly; they regulate CO₂. Option C would be an independent primary disorder."

- question: "What is the primary function of H⁺ secretion in the proximal tubule in the context of acid-base balance?"
  type: multiple-choice
  options:
    - "To excrete acid from the body, reducing the body's total acid load"
    - "To generate new bicarbonate that is added to the blood as a buffer"
    - "To reclaim filtered bicarbonate before it is lost in the urine, preserving the existing buffer reservoir"
    - "To acidify the urine so that phosphate and ammonia can serve as urinary buffers"
  answer: 2
  explanation: "Proximal tubule H⁺ secretion drives the reaction HCO₃⁻ + H⁺ → CO₂ + H₂O in the tubular lumen. The CO₂ diffuses into the proximal tubule cell, is reconverted to HCO₃⁻ by carbonic anhydrase, and is returned to the blood. Net effect: filtered bicarbonate is reclaimed — this is bicarbonate recovery, not net acid excretion. The body's total H⁺ load is unchanged. Net acid excretion (and new bicarbonate generation) happens in the distal tubule and collecting duct, where secreted H⁺ is buffered by titratable acid and ammonium and permanently removed in the urine."

- question: "When the proximal tubule reabsorbs bicarbonate by secreting H⁺ into the tubular lumen, this represents net excretion of acid from the body."
  type: true-false
  answer: false
  explanation: "Proximal tubule bicarbonate reabsorption is not net acid excretion — it is recovery of filtered buffer. The secreted H⁺ combines with filtered HCO₃⁻ to form CO₂ and water in the lumen; this CO₂ re-enters the cell and is reconverted to HCO₃⁻, which returns to the blood. No H⁺ is permanently removed from the body by this process. Net acid excretion — actually reducing the body's acid burden — occurs only in the distal nephron, where H⁺ is trapped in the urine as titratable acid (H₂PO₄⁻) or ammonium (NH₄⁺) and cannot re-enter circulation. Each such H⁺ excreted distally corresponds to one new HCO₃⁻ generated."

- question: "Renal compensation for a chronic respiratory acid-base disorder improves blood pH but typically does not restore it fully to the normal range of 7.35–7.45."
  type: true-false
  answer: true
  explanation: "Renal compensation adjusts plasma [HCO₃⁻] to shift the [HCO₃⁻]/[CO₂] ratio back toward normal, improving pH toward — but not to — the normal range. This is because the renal response is calibrated to compensate, not to correct: if bicarbonate were raised enough to fully normalize pH in the presence of elevated CO₂, the set point driving continued H⁺ secretion would be removed, halting further compensation. In clinical interpretation, a fully normalized pH despite abnormal PCO₂ and HCO₃⁻ suggests a mixed disorder, not simple compensation."

- question: "Explain the difference between bicarbonate reabsorption in the proximal tubule and actual acid excretion in the distal nephron, and why both processes are necessary for acid-base homeostasis."
  type: short-answer
  answer: "The proximal tubule reclaims the ~4,300 mEq of bicarbonate filtered daily — without this, the buffer reservoir would be lost in the urine within hours. But this is not acid excretion; no net H⁺ leaves the body. Actual acid excretion occurs in the distal tubule and collecting duct, where intercalated cells secrete H⁺ that is permanently trapped in the urine by titratable acid buffers (phosphate) and ammonium. Each H⁺ excreted this way generates a new HCO₃⁻ returned to the blood, replenishing the bicarbonate consumed by daily metabolic acid production (~70 mEq/day). Both processes are necessary: the proximal step preserves existing buffer; the distal step generates new buffer to replace what acid load has consumed."
  explanation: "The distinction matters clinically: a drug that blocks proximal carbonic anhydrase (like acetazolamide) causes bicarbonate wasting and metabolic acidosis not by failing to excrete acid but by failing to reabsorb buffer. Conversely, a defect in distal H⁺ secretion (as in distal renal tubular acidosis) prevents acid excretion and new bicarbonate generation, also producing metabolic acidosis — but via a completely different mechanism. The two processes address different parts of the acid-base problem and can fail independently."
```

## Explainer

Your understanding of buffer solutions tells you that pH stability depends on having a reservoir of weak acid and its conjugate base to absorb excess H⁺ or OH⁻. In the body, the dominant extracellular buffer is the **bicarbonate buffer system**: CO₂ + H₂O ⇌ H₂CO₃ ⇌ H⁺ + HCO₃⁻. The lungs regulate the CO₂ side of this equation within minutes by adjusting ventilation, but the kidneys control the bicarbonate side — and this is what gives the body its long-term acid-base stability. Without renal regulation, the bicarbonate reservoir would be steadily depleted by the ~70 mEq of non-volatile acid the body produces daily from protein metabolism and other sources.

The kidneys defend pH through three coordinated mechanisms. First, the **proximal tubule reclaims filtered bicarbonate** — roughly 4,300 mEq per day — by secreting H⁺ into the tubular lumen, where it combines with filtered HCO₃⁻ to form CO₂ and water. The CO₂ diffuses back into the cell, is reconverted to HCO₃⁻ by carbonic anhydrase, and is returned to the blood. This is not net acid excretion; it is bicarbonate recovery. Think of it as the kidney catching the bicarbonate before it escapes in the urine, preserving the buffer reservoir you already have.

The actual fine-tuning of acid-base balance happens in the **distal tubule and collecting duct**, where **intercalated cells** secrete H⁺ via H⁺-ATPase pumps. This secreted hydrogen is buffered in the tubular fluid by two urinary buffers: filtered phosphate (HPO₄²⁻ + H⁺ → H₂PO₄⁻, called **titratable acid**) and ammonia synthesized by proximal tubule cells from glutamine (NH₃ + H⁺ → NH₄⁺). Each hydrogen ion trapped in the urine by these buffers represents one new bicarbonate molecule generated and returned to the blood. This is how the kidney actually replenishes bicarbonate consumed by metabolic acid production.

The power of renal compensation becomes clear in chronic respiratory disorders. If the lungs cannot adequately eliminate CO₂ — say, in chronic obstructive pulmonary disease — arterial PCO₂ rises, pushing the buffer equation toward more H⁺ and driving pH down. The kidneys respond over 3–5 days by increasing H⁺ secretion and ammoniagenesis, generating new bicarbonate to raise the [HCO₃⁻]/[CO₂] ratio back toward normal. The pH improves but does not fully normalize — this is **compensation**, not correction. Conversely, in chronic respiratory alkalosis (sustained hyperventilation lowering PCO₂), the kidneys reduce bicarbonate reabsorption, allowing HCO₃⁻ to spill into the urine and lowering plasma bicarbonate to match the reduced CO₂. The clinical pattern — whether pH, PCO₂, and HCO₃⁻ move in the same or opposite directions — tells you whether you are looking at a primary respiratory or metabolic disturbance and whether compensation has occurred.
