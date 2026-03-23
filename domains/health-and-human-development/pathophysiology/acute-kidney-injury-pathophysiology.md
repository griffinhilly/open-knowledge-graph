---
id: acute-kidney-injury-pathophysiology
title: Acute Kidney Injury
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: renal-physiology-and-fluid-balance
  type: hard
- id: glomerular-filtration-rate
  type: hard
- id: tubular-function-and-reabsorption
  type: soft
builds-toward:
- chronic-kidney-disease-progression
- acute-tubular-necrosis
tags:
- acute-kidney-injury
- renal-dysfunction
- azotemia
stage: expert
status: validated
---

# Acute Kidney Injury

## Core Idea
Acute kidney injury is sudden loss of GFR function caused by prerenal hypoperfusion, intrinsic kidney damage, or postrenal obstruction. Acute tubular necrosis is the most common pathology, characterized by epithelial cell injury and loss of barrier function.

## How It's Best Learned
Use BUN/Creatinine ratio to distinguish prerenal from intrinsic AKI. Examine urinalysis (muddy casts in ATN, proteinuria in glomerulonephritis). Understand RIFLE and KDIGO criteria for severity staging.

## Common Misconceptions
Mild serum creatinine elevation does not exclude severe AKI—the rate of rise matters. Oliguria is not required for AKI diagnosis; non-oliguric AKI has better prognosis.

## Questions

```yaml
- question: "A patient presents after prolonged vomiting with dehydration. Labs show BUN 42 mg/dL, creatinine 1.8 mg/dL (BUN/Cr ratio ≈ 23:1). Which diagnosis best fits, and why?"
  type: multiple-choice
  options:
    - "Acute tubular necrosis, because high BUN indicates tubular damage from volume depletion"
    - "Prerenal AKI, because the elevated BUN/Cr ratio reflects intact tubules avidly reabsorbing urea to conserve volume"
    - "Postrenal AKI, because dehydration causes downstream obstruction"
    - "Intrinsic renal AKI, because dehydration directly injures glomeruli"
  answer: 1
  explanation: "In prerenal AKI, kidney tissue is structurally intact but hypoperfused. The tubules continue reabsorbing urea (BUN) efficiently in an attempt to conserve fluid, so BUN rises disproportionately to creatinine — producing a BUN/Cr ratio >20:1. In ATN, tubular reabsorption is impaired, so BUN does not accumulate disproportionately and the ratio is typically <20:1. The ratio is thus a first-pass tool for distinguishing functional (prerenal) from structural (intrinsic) injury."

- question: "Patient A has creatinine rising from 1.0 to 2.2 mg/dL over 36 hours. Patient B has a stable creatinine of 3.5 mg/dL (their baseline for months). Which patient more likely has acute kidney injury?"
  type: multiple-choice
  options:
    - "Patient B, because their absolute creatinine level is higher and indicates worse kidney function"
    - "Patient A, because the rapid rate of rise reflects acute GFR decline even though the absolute value is lower"
    - "Both are equivalent — creatinine level directly mirrors GFR regardless of trajectory"
    - "Neither qualifies as AKI without urine output data"
  answer: 1
  explanation: "AKI is defined by rate of change, not absolute value. Creatinine must accumulate in a large volume of distribution, so the absolute level lags behind actual GFR decline. A rapidly rising creatinine (1.0→2.2 in 36 hours) meets KDIGO Stage 2 criteria and signals acute injury, while a stable creatinine of 3.5 in a patient with chronic kidney disease reflects a new steady state. This is the key clinical nuance: a modest but rising creatinine can represent more acute danger than a higher but stable level."

- question: "Oliguria (urine output <0.5 mL/kg/hr) is a required criterion for diagnosing acute kidney injury."
  type: true-false
  answer: false
  explanation: "Non-oliguric AKI is well recognized and actually carries a better prognosis than oliguric AKI. KDIGO criteria allow diagnosis based on either a creatinine rise ≥0.3 mg/dL within 48 hours or ≥1.5× baseline within 7 days, OR urine output <0.5 mL/kg/hr for ≥6 hours. Either criterion suffices; neither is required. Clinicians who anchor on oliguria may miss non-oliguric AKI until it progresses."

- question: "In prerenal AKI, the structural integrity of kidney tissue is preserved; the primary defect is inadequate renal perfusion pressure to drive glomerular filtration."
  type: true-false
  answer: true
  explanation: "This is the defining feature of prerenal AKI and is what makes it potentially reversible with volume resuscitation or treatment of the underlying cause (e.g., heart failure, sepsis, hemorrhage). Because tubular cells are not injured, the kidney still concentrates urine appropriately and reabsorbs urea avidly — hence the BUN/Cr >20:1. If hypoperfusion is prolonged or severe, it can progress to intrinsic ATN, at which point tubular cells are damaged and the prognosis worsens."

- question: "Why does the BUN-to-creatinine ratio differ between prerenal AKI and acute tubular necrosis, and what is the diagnostic significance of this difference?"
  type: short-answer
  answer: "Both BUN and creatinine rise when GFR falls. But BUN is also regulated by tubular reabsorption: in prerenal AKI, intact tubules avidly reabsorb urea as part of volume-conservation reflexes, so BUN rises disproportionately to creatinine, giving a ratio >20:1. In ATN, tubular cells are damaged and cannot reabsorb urea normally, so the BUN/Cr ratio stays closer to 10-15:1. The ratio therefore reveals not just that GFR is reduced but whether the tubules themselves are functioning — distinguishing a perfusion problem (treat with fluids or addressing the cause) from a structural injury (supportive care, avoid nephrotoxins, consider renal replacement therapy)."
  explanation: "Creatinine is freely filtered and neither significantly secreted nor reabsorbed in the tubule, making it a reliable GFR marker. BUN is filtered but subject to significant tubular reabsorption. This difference in tubular handling is what makes the ratio clinically informative."
```

## Explainer

You already know that the kidney maintains fluid balance and excretes waste by filtering blood through glomeruli, reabsorbing what the body needs in the tubules, and excreting the rest as urine. The key measure of this work is **glomerular filtration rate (GFR)** — roughly 120 mL/min in a healthy adult. **Acute kidney injury (AKI)** is a sudden, sustained fall in GFR, defined operationally by a rise in serum creatinine or a fall in urine output. Because creatinine is normally excreted entirely by the kidney, any reduction in filtration causes it to accumulate in the blood — making it a convenient biomarker of kidney function.

Clinicians organize the causes of AKI into three anatomical categories based on where the problem originates. **Prerenal AKI** is the most common: reduced blood flow to the kidney — from dehydration, hemorrhage, heart failure, or sepsis — drops the perfusion pressure that drives filtration. The kidney itself is structurally normal; it simply isn't getting enough blood. **Intrinsic renal AKI** involves damage to kidney tissue itself. The most common cause is **acute tubular necrosis (ATN)**, in which prolonged ischemia or nephrotoxins (contrast agents, aminoglycoside antibiotics, myoglobin from rhabdomyolysis) injure the tubular epithelial cells, causing them to slough into the tubule lumen and obstruct flow. **Postrenal AKI** results from obstruction downstream of the kidney — a kidney stone, enlarged prostate, or tumor blocking urinary drainage; back-pressure builds up and impairs filtration.

Distinguishing these categories determines treatment. The **BUN-to-creatinine ratio** is a first-pass tool: in prerenal AKI, the kidney is intact and over-reabsorbs urea (BUN) in its attempt to conserve volume, so BUN rises disproportionately to creatinine, giving a ratio >20:1. In ATN, tubular reabsorption is impaired, so BUN does not accumulate as disproportionately. **Urinalysis** adds specificity: ATN produces pathognomonic "muddy brown" granular casts from sloughed tubular cells; glomerulonephritis produces red blood cell casts; prerenal AKI typically shows bland urine with hyaline casts.

AKI severity is staged using **KDIGO criteria**: Stage 1 is a creatinine rise of 0.3 mg/dL within 48 hours or 1.5–1.9× baseline; Stage 2 is 2–2.9× baseline; Stage 3 is 3× baseline, creatinine ≥4 mg/dL, or requirement for renal replacement therapy. The critical clinical insight — captured in the Common Misconceptions — is that even modest creatinine elevations can mask severe injury: because creatinine must accumulate in a large volume of distribution, the absolute creatinine level lags behind the rate of GFR decline. A rapidly rising creatinine from 1.0 to 2.0 mg/dL may represent more acute injury than a stable creatinine of 3.0 mg/dL in a patient with chronic kidney disease.
