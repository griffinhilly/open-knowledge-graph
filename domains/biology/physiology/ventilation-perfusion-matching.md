---
id: ventilation-perfusion-matching
title: Ventilation-Perfusion Matching and Gas Exchange Efficiency
domain: biology
course: physiology
prerequisites:
- id: respiratory-system-overview
  type: hard
- id: gas-exchange-and-diffusion
  type: hard
builds-toward:
- oxygen-diffusion-capacity-lungs
tags:
- v-q-ratio
- hypoxemia
- lung-disease
stage: formal-systems
status: validated
---

# Ventilation-Perfusion Matching and Gas Exchange Efficiency

## Core Idea
Effective gas exchange requires that ventilation (air reaching alveoli) matches perfusion (blood flow through pulmonary capillaries) in the same lung regions; a V/Q ratio near 1 is optimal. Ventilation-perfusion mismatch occurs in pulmonary and cardiac diseases, causing hypoxemia and CO2 retention despite normal alveolar ventilation.

## Questions

```yaml
- question: "A patient with severe pneumonia has fluid-filled alveoli in the right lower lobe with intact blood flow — blood traverses the lobe without any gas exchange. You increase their inspired oxygen to 100% FiO₂. What is the expected effect on arterial oxygenation?"
  type: multiple-choice
  options:
    - "Complete correction of hypoxemia, because 100% oxygen fully saturates all available hemoglobin"
    - "Moderate improvement, because the higher FiO₂ boosts diffusion across the fluid-filled alveoli"
    - "Minimal improvement, because the shunted blood never contacts the extra oxygen regardless of FiO₂"
    - "Paradoxical worsening, because high FiO₂ inhibits hypoxic pulmonary vasoconstriction throughout the lung"
  answer: 2
  explanation: "This is a true shunt (V/Q = 0): blood passes through completely unventilated alveoli and returns to the left heart deoxygenated. Since this blood never contacts alveolar gas, raising FiO₂ cannot correct the problem — the extra oxygen is simply not available to the shunted fraction. Hemoglobin in the ventilated regions is already near 100% saturated, so supplemental oxygen adds little additional oxygen content to compensate for the fixed shunt fraction."

- question: "A pulmonary embolism completely obstructs blood flow to the right upper lobe while ventilation continues normally. What is the V/Q ratio of the affected lobe, and what clinical term describes this?"
  type: multiple-choice
  options:
    - "V/Q = 0, called a shunt — no ventilation reaching the perfused alveoli"
    - "V/Q approaches infinity, called dead space — ventilation with no perfusion"
    - "V/Q = 1.0, called optimal matching — embolism has no effect on V/Q ratio"
    - "V/Q < 0.6, called a low V/Q zone — blood flow exceeds ventilation"
  answer: 1
  explanation: "Dead space is ventilation without perfusion — air arrives at the alveoli but no blood is present to pick up oxygen. A pulmonary embolism eliminates perfusion while ventilation continues, making V/Q → ∞ in that region. A shunt is the opposite: perfusion without ventilation (V/Q = 0). This distinction matters clinically: dead space responds to supplemental oxygen, while true shunt does not."

- question: "Hypoxic pulmonary vasoconstriction (HPV) is a local response that diverts blood away from poorly ventilated alveoli — the opposite of how systemic blood vessels respond to low oxygen in peripheral tissues."
  type: true-false
  answer: true
  explanation: "In systemic tissues, hypoxia signals that local metabolic demand exceeds oxygen delivery, so arterioles dilate to increase blood flow. In the lung, the logic is reversed: a hypoxic alveolus has poor ventilation, so directing blood there would waste perfusion on a non-functional gas exchange unit. Pulmonary arterioles therefore constrict in response to low alveolar PO₂, redirecting blood to better-ventilated regions. This local optimization improves overall V/Q matching."

- question: "Supplemental oxygen can correct hypoxemia from any form of V/Q mismatch, including true shunt, if the FiO₂ is increased high enough."
  type: true-false
  answer: false
  explanation: "True shunt (V/Q = 0) does not respond to supplemental oxygen regardless of FiO₂, because shunted blood bypasses ventilated alveoli entirely and never encounters the extra oxygen. In contrast, hypoxemia from dead space or low V/Q mismatch does respond to supplemental oxygen, because increasing alveolar PO₂ in functional regions can compensate for the impaired ones. The response to 100% O₂ is therefore a key clinical test for distinguishing shunt from other causes of hypoxemia."

- question: "Why does true shunt (V/Q = 0) not respond to supplemental oxygen, even at 100% FiO₂? Explain the mechanism."
  type: short-answer
  answer: "In true shunt, a fixed fraction of blood flows through completely unventilated lung units — it never contacts alveolar gas, regardless of how high the inspired oxygen concentration is raised. The oxygenated blood exiting normal lung units is already near 100% hemoglobin saturation, so increasing FiO₂ adds only a trivial amount of dissolved oxygen (not enough to compensate for the deoxygenated shunt fraction being added to the output). The resulting mixture remains hypoxemic because the shunted fraction is a fixed oxygen debt that supplemental therapy cannot reach."
  explanation: "This contrasts with V/Q mismatch from dead space, where functional lung units can be 'rescued' by raising alveolar PO₂. The shunt fraction is immune to FiO₂ manipulation because the blood physically bypasses the gas exchange surface."
```

## Explainer

From your study of the respiratory system and gas exchange, you know that oxygen moves from alveolar air into pulmonary capillary blood by diffusion, driven by the partial pressure gradient between the two compartments. But efficient gas exchange requires more than open alveoli and flowing blood — it requires that air and blood arrive at the same place at the same time. **Ventilation-perfusion (V/Q) matching** is the principle that the lung must direct airflow and blood flow to the same regions for gas exchange to work efficiently.

In an ideal lung, every alveolus would receive exactly the right amount of air and blood to maintain a **V/Q ratio** near 1.0. In reality, gravity creates a natural gradient. In an upright person, blood flow (perfusion) is greatest at the lung bases because the hydrostatic pressure of the blood column increases pulmonary capillary pressure below the heart. Ventilation is also greater at the bases (because the lower alveoli are more compliant at the start of inspiration), but the perfusion gradient is steeper than the ventilation gradient. The result is that the V/Q ratio is highest at the lung apices (~3.0 — relatively over-ventilated) and lowest at the bases (~0.6 — relatively over-perfused). Despite this regional variation, the overall matching is good enough in healthy lungs that arterial blood leaves nearly fully oxygenated.

The lung has an elegant local mechanism to optimize V/Q matching: **hypoxic pulmonary vasoconstriction (HPV)**. When an alveolus is poorly ventilated — say, due to a mucus plug or atelectasis — the local oxygen tension drops. Unlike systemic vessels, which dilate in response to hypoxia, pulmonary arterioles *constrict* when surrounding alveolar PO2 falls. This diverts blood away from poorly ventilated regions toward better-ventilated alveoli, improving overall gas exchange efficiency. HPV is a purely local response mediated by oxygen-sensitive potassium channels in pulmonary smooth muscle cells — no neural input required. On the airway side, local CO2 levels influence bronchiolar tone: high alveolar CO2 (from good perfusion but poor ventilation) causes bronchodilation to increase airflow to that region.

**V/Q mismatch** is the most common cause of hypoxemia in clinical medicine. There are two extremes to understand. A region with ventilation but no perfusion (V/Q = infinity) is called **dead space** — the air reaches the alveolus but no blood is there to pick up oxygen. Pulmonary embolism is the classic cause. A region with perfusion but no ventilation (V/Q = 0) is called a **shunt** — blood passes through the lung without encountering fresh air, returning to the left heart still deoxygenated. Pneumonia, pulmonary edema, and atelectasis create shunt physiology. Most real disease produces a spectrum of V/Q ratios between these extremes rather than pure dead space or shunt. A key clinical distinction is that hypoxemia from V/Q mismatch (including dead space) generally responds to supplemental oxygen, because increasing alveolar PO2 in the functional regions compensates for the impaired ones. True shunt, however, does not respond to supplemental oxygen — the blood bypassing ventilated alveoli never encounters the extra oxygen, no matter how high you raise the FiO2.
