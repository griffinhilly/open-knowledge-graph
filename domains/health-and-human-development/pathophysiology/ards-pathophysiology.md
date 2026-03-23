---
id: ards-pathophysiology
title: Acute Respiratory Distress Syndrome (ARDS)
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: respiratory-system-overview
  type: hard
- id: acute-inflammation-pathophysiology
  type: hard
- id: alveolar-capillary-barrier
  type: soft
builds-toward:
- sepsis-and-sirs-pathophysiology
tags:
- respiratory-distress
- lung-injury
- acute-inflammation
stage: expert
status: draft
---

# Acute Respiratory Distress Syndrome (ARDS)

## Core Idea
ARDS is characterized by increased alveolar-capillary permeability causing pulmonary edema, ventilation-perfusion mismatch, and hypoxemia refractory to supplemental oxygen. Inflammatory mediators (cytokines, complement, neutrophils) damage the epithelial-endothelial barrier.

## How It's Best Learned
Study the Berlin definition (PaO2/FiO2 ratio, imaging, onset timing). Understand exudative and fibroproliferative phases. Review common triggers: sepsis, aspiration, transfusion, trauma.

## Common Misconceptions
ARDS is not a single disease entity—it is a syndrome with heterogeneous causes and trajectories. Low tidal volume ventilation reduces mortality not by improving oxygenation directly but by limiting barotrauma.

## Questions

```yaml
- question: "A patient with ARDS is placed on 100% inspired oxygen (FiO2 = 1.0), but their arterial PaO2 remains critically low, giving a P/F ratio of 120. Why does supplemental oxygen fail to correct the hypoxemia?"
  type: multiple-choice
  options:
    - "High FiO2 worsens inflammation by producing oxygen radicals, directly lowering the PaO2"
    - "The diffusion barrier across the thickened alveolar membrane is too great for oxygen to cross"
    - "Blood flows through fluid-filled, non-ventilated alveoli and returns unoxygenated regardless of FiO2"
    - "ARDS reduces respiratory rate, so total alveolar ventilation is insufficient"
  answer: 2
  explanation: "ARDS hypoxemia is primarily a shunt physiology: fluid-filled alveoli cannot ventilate, but their capillaries still carry blood. That blood returns to the left heart without picking up oxygen — a true shunt. Adding more oxygen to the ventilated alveoli cannot help blood that bypasses those alveoli entirely. Option B (diffusion impairment) would respond somewhat to high FiO2 by increasing the partial pressure gradient; it is the shunt that is truly refractory. Option D is incorrect: ARDS patients typically hyperventilate due to hypoxic drive."

- question: "Why does low tidal volume ventilation (6 mL/kg) reduce mortality in ARDS, rather than larger tidal volumes that would better maintain PaO2?"
  type: multiple-choice
  options:
    - "Small tidal volumes reduce FiO2 requirements, limiting oxygen toxicity to the airway"
    - "Larger tidal volumes cause volutrauma and barotrauma to the remaining aerated lung tissue, worsening injury"
    - "Low tidal volumes allow the inflammatory response to resolve more quickly by reducing lung movement"
    - "Small tidal volumes prevent the fibroproliferative phase from being triggered"
  answer: 1
  explanation: "In ARDS, large portions of the lung are consolidated and non-aerated. The remaining aerated alveoli receive the full tidal volume, overstretching them — this volutrauma (and the resulting barotrauma) perpetuates inflammatory injury in the very tissue needed for gas exchange. Accepting lower PaO2 and higher CO2 (permissive hypercapnia) is the deliberate tradeoff: lung-protective ventilation prioritizes preventing secondary injury over maximizing oxygenation. Options A, C, and D are not the primary mechanisms established in the ARDSNet trial."

- question: "In ARDS, the hypoxemia is primarily caused by intrapulmonary shunting — blood flowing past non-ventilated, fluid-filled alveoli."
  type: true-false
  answer: true
  explanation: "This is the central hemodynamic abnormality in ARDS. Inflammatory barrier breakdown floods alveoli with protein-rich exudate. Perfusion of these non-ventilated alveoli constitutes a shunt (V/Q = 0 regions), returning deoxygenated blood to the arterial circulation. This is confirmed by the failure of high FiO2 to correct the hypoxemia — a hallmark of shunt physiology that distinguishes it from diffusion impairment or hypoventilation."

- question: "Low tidal volume ventilation in ARDS improves oxygenation by recruiting collapsed alveoli through the application of positive pressure."
  type: true-false
  answer: false
  explanation: "Low tidal volume ventilation does NOT directly improve oxygenation — in fact, it accepts lower PaO2 as a deliberate tradeoff. Its purpose is to prevent further lung injury (volutrauma/barotrauma) in the already-compromised tissue. Alveolar recruitment is a goal of PEEP (positive end-expiratory pressure), not reduced tidal volume. The mortality benefit of lung-protective ventilation comes from limiting secondary injury, not from better gas exchange."

- question: "Why does ARDS produce hypoxemia that is 'refractory to supplemental oxygen,' and what does this tell us about the underlying mechanism?"
  type: short-answer
  answer: "ARDS hypoxemia is refractory because the mechanism is true intrapulmonary shunting: a large fraction of cardiac output passes through alveoli that are completely flooded and non-ventilated. No amount of oxygen delivered to ventilated alveoli can oxygenate blood that bypasses them entirely. This contrasts with hypoventilation or mild V/Q mismatch, where increasing FiO2 raises alveolar PO2 and corrects hypoxemia. The refractoriness is the diagnostic signature of shunt physiology."
  explanation: "Understanding why oxygen-unresponsive hypoxemia indicates shunt is clinically critical. It directs treatment toward alveolar recruitment (PEEP), reducing inflammation, and protective ventilation — not simply increasing FiO2, which risks oxygen toxicity without benefit. The Berlin definition's PaO2/FiO2 threshold encodes this: even with maximum FiO2, the ratio remains low because FiO2 gains buy almost nothing against a true shunt."
```

## Explainer

You have already studied the alveolar-capillary barrier — the ultra-thin interface where oxygen crosses from air into blood, and carbon dioxide crosses back. That barrier's integrity depends on tight junctions between type I pneumocytes on the air side and endothelial cells on the blood side. ARDS is what happens when inflammation destroys that barrier. Understanding ARDS means tracing the chain from initial insult to barrier collapse to clinical syndrome.

The trigger can be direct (pneumonia, aspiration, inhalation injury) or indirect (sepsis, trauma, pancreatitis). Either way, the lung mounts an acute inflammatory response. **Neutrophils** — which you studied as the first responders in acute inflammation — flood into the alveolar space and release proteases, reactive oxygen species, and inflammatory cytokines. This cytokine storm (including IL-1β, TNF-α, and IL-8) amplifies the response and recruits more neutrophils. The critical consequence is that the inflammatory mediators dissolve the tight junctions holding the alveolar-capillary barrier together. Protein-rich fluid from the capillaries — exudate — pours into alveoli that normally contain only air.

Now think through the respiratory consequences. Fluid-filled alveoli cannot participate in gas exchange, but blood continues to flow past them — a ventilation-perfusion mismatch your respiratory physiology background prepared you for. The result is a **shunt**: blood passes through the lung and returns to circulation without picking up oxygen. This is why ARDS produces hypoxemia that does not respond to supplemental oxygen the way ordinary hypoxia does — adding more oxygen to ventilated alveoli helps very little if the blood is mostly flowing past collapsed, fluid-filled ones. The hallmark PaO2/FiO2 ratio below 300 captures this: even with 100% inspired oxygen (FiO2 = 1.0), the partial pressure of oxygen in arterial blood remains severely depressed.

ARDS has two pathological phases. The **exudative phase** (days 1–7) involves the barrier breakdown and flooding just described, along with hyaline membrane formation from precipitated proteins. The **fibroproliferative phase** (days 7–21) involves type II pneumocyte proliferation, fibroblast activation, and collagen deposition — the lung's attempt at repair. In severe cases this fibroproliferative response is excessive, leaving behind stiff, scarred lung tissue that impairs mechanics long after the acute crisis resolves. Treatment strategy reflects this pathophysiology: mechanical ventilation with **low tidal volumes** (6 mL/kg) prevents the volutrauma and barotrauma that would worsen the already-fragile lung, even though smaller breaths mean accepting higher CO2 levels — a deliberate tradeoff called permissive hypercapnia.
