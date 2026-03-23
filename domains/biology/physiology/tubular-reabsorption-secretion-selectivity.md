---
id: tubular-reabsorption-secretion-selectivity
title: Tubular Reabsorption, Secretion, and Selective Transport
domain: biology
course: physiology
prerequisites:
- id: glomerular-filtration-rate-autoregulation
  type: hard
- id: active-transport
  type: hard
builds-toward:
- loop-of-henle-countercurrent-concentration
- electrolyte-balance-renal-hormonal-control
tags:
- renal
- transport
- reabsorption
- secretion
stage: formal-systems
status: validated
---

# Tubular Reabsorption, Secretion, and Selective Transport

## Core Idea
Following glomerular ultrafiltration of ~180 L/day, the nephron selectively reabsorbs useful substances and secretes additional waste to produce final urine (~1.5 L/day). The proximal tubule reabsorbs ~65% of filtered water, sodium, glucose, amino acids, and other nutrients via active transport (Na-K-ATPase on the basolateral membrane) and aquaporin water channels. Tubular secretion actively pumps substances (H+, K+, ammonia, drugs, organic acids) into the tubule lumen from the blood, enhancing excretion beyond filtration. The proximal tubule epithelium is specialized for this selective reabsorption with abundant mitochondria, extensive brush border, and polarized transport proteins.

## How It's Best Learned
Study microperfusion of isolated tubule segments to observe specific transport processes. Compare plasma filtrate and final urine composition to determine what is reabsorbed and secreted. Use tracers to follow specific substances.

## Common Misconceptions
All filtered substances are not reabsorbed equally; glucose and amino acids are normally completely reabsorbed (threshold absorbed before excretion appears), while creatinine and inulin are normally not reabsorbed.

## Questions

```yaml
- question: "A patient with uncontrolled diabetes has a blood glucose of 250 mg/dL, and glucose appears in their urine. What is the correct explanation?"
  type: multiple-choice
  options:
    - "Glomerular filtration is impaired in diabetics, allowing glucose to leak into the filtrate"
    - "Glucose is actively secreted into the tubule lumen in diabetic patients"
    - "The filtered glucose load exceeds the transport maximum of SGLT cotransporters — all carriers are saturated and excess glucose passes unreabsorbed into the urine"
    - "The kidneys cannot detect glucose as a useful substance above a certain plasma concentration"
  answer: 2
  explanation: "SGLT2 and SGLT1 transporters in the proximal tubule reabsorb glucose by active transport, but they have a finite number of binding sites (the transport maximum, Tm). At normal blood glucose, the filtered load is below Tm and all glucose is reabsorbed — none appears in urine. At 250 mg/dL, the filtered load exceeds Tm (~180 mg/dL threshold); all carriers are saturated, and the surplus glucose passes through unreabsorbed as glucosuria. Glomerular filtration is not impaired in typical type 2 diabetes — the problem is at the tubular reabsorption step, not filtration."

- question: "A researcher measures the clearance of substance X and finds it equals three times the glomerular filtration rate. What must be true about how the nephron handles substance X?"
  type: multiple-choice
  options:
    - "X is completely reabsorbed — high clearance reflects high plasma concentration causing more filtration"
    - "X is only filtered at the glomerulus and not reabsorbed or secreted; its clearance exceeds GFR by chance"
    - "X is filtered at the glomerulus and then actively secreted into the tubule lumen by proximal tubule cells, adding substance from peritubular blood to the filtrate"
    - "X must be an endogenous waste product like creatinine that bypasses the glomerulus"
  answer: 2
  explanation: "Clearance of a substance exceeds GFR only when the nephron adds the substance to the filtrate beyond what was filtered — that is, by secretion. If clearance = GFR, the substance is filtered and not reabsorbed or secreted (like inulin). If clearance < GFR, the substance is net-reabsorbed. If clearance > GFR, the substance must be secreted. PAH is the classic example: at low plasma concentrations, PAH clearance approaches renal plasma flow because virtually all PAH is removed from blood in a single pass through filtration plus secretion."

- question: "All useful substances that pass through the glomerular filter are eventually reabsorbed by the tubule, because the kidney's primary function is conservation."
  type: true-false
  answer: false
  explanation: "Inulin, creatinine, and various organic acids pass through the filter but are only minimally reabsorbed or not reabsorbed at all — and PAH is actively secreted, making its clearance far exceed GFR. The kidney's function is not blanket conservation but selective handling: each substance has a characteristic profile determined by its transport proteins and their maxima. Useful substances like glucose and amino acids are fully reabsorbed under normal conditions, but the same carrier-mediated system means they can spill when concentrations are high. Waste products may be neither reabsorbed nor secreted (creatinine) or actively secreted (PAH, drugs, organic acids)."

- question: "A substance whose renal clearance exactly equals the glomerular filtration rate is neither reabsorbed nor secreted by the tubule."
  type: true-false
  answer: true
  explanation: "This is the defining property of inulin and the basis for using inulin clearance to measure GFR. If clearance = GFR, then the amount excreted in urine equals exactly the amount filtered — no tubular reabsorption or secretion has occurred. This relationship (clearance = GFR ↔ no net tubular handling) is the reference standard for inferring what happens to other substances: clearance below GFR means net reabsorption, clearance above GFR means net secretion. Creatinine is a practical clinical approximation to inulin, with minimal secretion making its clearance a slight overestimate of GFR."

- question: "How does the transport maximum (Tm) explain why glucose appears in the urine of diabetic patients but not in healthy individuals, even though both use the same carrier-mediated reabsorption system?"
  type: short-answer
  answer: "Both healthy and diabetic kidneys use SGLT2/SGLT1 transporters with the same Tm. The difference is the filtered load. In healthy individuals, blood glucose (~90 mg/dL) × GFR produces a filtered load well below the Tm — all glucose can be bound by available transporters and reabsorbed. In uncontrolled diabetes, high blood glucose (>180 mg/dL) × GFR generates a filtered load that saturates all available transporters. Once every SGLT binding site is occupied, no additional glucose can be reabsorbed regardless of how much remains in the tubule lumen. The excess passes into the urine. The Tm defines a threshold: below it, complete reabsorption; above it, spillage proportional to the excess load."
  explanation: "This Tm threshold concept generalizes to any carrier-transported substance. Amino acids, phosphate, and bicarbonate each have their own Tm, and each can spill into urine when plasma concentrations are pathologically elevated (aminoaciduria in Fanconi syndrome, phosphaturia in certain kidney diseases). Understanding the Tm framework — finite transport capacity, saturation kinetics, threshold phenomenon — is more powerful than memorizing which substances are reabsorbed, because it predicts behavior under any condition once you know the Tm and the filtered load."
```

## Explainer

From your study of glomerular filtration and active transport, you know that the glomerulus produces a protein-free ultrafiltrate of plasma, and that cells can move substances against concentration gradients using energy-dependent carrier proteins. The nephron's task is then to sort through that filtrate — reclaiming valuable substances and discarding waste — using the selective properties of transport proteins along the tubule. The key insight is that **selectivity is not all-or-nothing**: different substances are handled with different efficiencies, and the transport maximum of each carrier determines whether and when a substance "spills" into the urine.

Consider **glucose reabsorption** as the clearest example. Under normal conditions, all filtered glucose is reabsorbed in the proximal tubule by SGLT2 and SGLT1 cotransporters — zero glucose appears in the urine. But these transporters have a finite number of binding sites. As plasma glucose rises (as in uncontrolled diabetes), the filtered load of glucose increases proportionally. At a plasma concentration of roughly 180 mg/dL, the filtered load exceeds the **transport maximum (Tm)** — all available carriers are saturated, and the excess glucose passes through unreabsorbed, appearing in the urine as **glucosuria**. This threshold concept applies to any substance reabsorbed by carrier-mediated transport: there is a plasma concentration below which the substance is completely recovered, and above which it spills into the urine. Amino acids, phosphate, and bicarbonate all have their own transport maxima.

Secretion follows a mirror-image logic. Substances like **para-aminohippuric acid (PAH)**, organic acids, and many drugs are both filtered at the glomerulus and actively secreted by the proximal tubule from peritubular blood into the lumen. This double mechanism — filtration plus secretion — means the kidney can clear these substances from the blood much more efficiently than filtration alone would allow. PAH, in fact, is so efficiently secreted that at low plasma concentrations, nearly all PAH is removed from renal plasma in a single pass — which is why PAH clearance is used to estimate renal plasma flow. But secretory transporters also saturate at a Tm, so at high PAH concentrations, the extraction efficiency falls.

The selectivity of renal transport creates a spectrum of handling. At one extreme, **glucose and amino acids** are completely reabsorbed — none appears in normal urine. At the other extreme, **inulin** (a plant polysaccharide used experimentally) is freely filtered but neither reabsorbed nor secreted, so its clearance exactly equals the glomerular filtration rate. **Creatinine**, an endogenous muscle metabolite, is close to inulin — it is filtered and only minimally secreted, making it a practical clinical estimate of GFR. **Urea** is partially reabsorbed (about 50%), and its handling varies with hydration status. **PAH and penicillin** are filtered and aggressively secreted, giving them clearances that exceed GFR. By comparing a substance's clearance to the GFR (inulin clearance), you can determine whether the nephron is a net reabsorber or a net secretor of that substance — a principle that underlies much of renal physiology and pharmacology.
