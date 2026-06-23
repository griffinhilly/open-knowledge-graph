---
id: gas-exchange-alveoli-and-diffusion
title: 'Gas Exchange: Alveoli and Diffusion Across the Respiratory Membrane'
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: respiratory-system-anatomy-and-ventilation
  type: hard
- id: gas-exchange-and-diffusion
  type: soft
- id: diffusion-and-ficks-laws
  type: soft
- id: blood-vessel-structure-and-types
  type: soft
tags:
- gas-exchange
- diffusion
- oxygen
- carbon-dioxide
stage: formal-systems
status: validated
---

# Gas Exchange: Alveoli and Diffusion Across the Respiratory Membrane

## Core Idea
Alveoli are tiny air sacs where oxygen diffuses from air into pulmonary capillary blood and carbon dioxide diffuses from blood into the alveolar space. The respiratory membrane consists of alveolar epithelium, basement membranes, and capillary endothelium—a thin barrier optimized for rapid gas exchange.

## Questions

```yaml
- question: "A patient with pulmonary fibrosis (thickened respiratory membrane) develops hypoxemia (low blood O₂) but maintains normal blood CO₂ levels. The best explanation is:"
  type: multiple-choice
  options:
    - "CO₂ is a smaller molecule than O₂ and therefore crosses the thickened membrane more easily"
    - "CO₂'s approximately 20-fold greater solubility in tissue fluid allows it to maintain adequate diffusion across a thickened membrane even as O₂ diffusion becomes significantly impaired"
    - "The patient hyperventilates in response to hypoxemia, which removes CO₂ faster and compensates for the thickened membrane"
    - "CO₂ is produced at a much lower rate than O₂ is consumed, reducing its diffusion burden"
  answer: 1
  explanation: "The key is solubility. CO₂ is approximately 20 times more soluble in tissue fluid than O₂, making it far more diffusible per unit of partial pressure gradient. When membrane thickness increases, the diffusion rate of both gases falls (by Fick's law), but CO₂'s solubility advantage compensates — it continues to clear adequately. O₂, lacking this advantage, becomes diffusion-limited much sooner, causing hypoxemia. Hyperventilation (option C) can partially compensate for hypoxemia but is a consequence, not the primary explanation for why CO₂ is maintained."

- question: "A pulmonary embolism blocks blood flow to a region of the lung that continues to receive ventilation. This creates:"
  type: multiple-choice
  options:
    - "A shunt — blood that bypasses the gas exchange surface entirely"
    - "Dead space — ventilated alveoli with no perfusion, so the fresh air cannot contribute to gas exchange"
    - "Increased diffusion distance due to clot material lining the alveolar walls"
    - "Pulmonary hypertension from redistribution of flow to the remaining lung"
  answer: 1
  explanation: "Dead space is ventilation without perfusion: air reaches the alveoli but no blood is present to pick up the oxygen, so that ventilatory effort is wasted. A shunt is the opposite — perfusion without ventilation (e.g., a blocked airway), where blood flows past an alveolus without gas exchange. A pulmonary embolism blocks the arterial supply to a lung region, leaving ventilation intact but eliminating perfusion — this is dead space. Both V/Q mismatches impair overall gas exchange efficiency even when the membrane itself is normal."

- question: "Carbon dioxide has a larger partial pressure gradient across the respiratory membrane than oxygen, which is why it diffuses more rapidly despite being a larger molecule."
  type: true-false
  answer: false
  explanation: "The partial pressure gradient for CO₂ is actually smaller: about 5 mmHg (45 mmHg in venous blood vs 40 mmHg in alveolar air), compared to about 60 mmHg for O₂ (40 mmHg in blood vs 100 mmHg in alveoli). CO₂ diffuses more rapidly not because of a larger gradient but because it is approximately 20 times more soluble in tissue fluid than O₂. Solubility — not gradient size — is the dominant factor explaining CO₂'s superior diffusibility across the respiratory membrane."

- question: "According to Fick's law, reducing the surface area of the respiratory membrane (as occurs in emphysema) decreases the rate of gas diffusion."
  type: true-false
  answer: true
  explanation: "Fick's law states that diffusion rate is proportional to surface area × concentration gradient / membrane thickness. Emphysema destroys alveolar walls, collapsing multiple small alveoli into larger but fewer air spaces, reducing the total surface area (normally ~70 m²) substantially. With less surface area available, the total diffusion capacity falls — less O₂ can cross per breath even if the remaining membrane is of normal thickness. This is distinct from fibrosis, which thickens the membrane; emphysema reduces surface area while leaving membrane thickness relatively normal."

- question: "Explain why a patient with pulmonary fibrosis typically develops hypoxemia before hypercapnia, despite the fact that CO₂ has a smaller partial pressure gradient across the respiratory membrane than O₂."
  type: short-answer
  answer: "CO₂ is approximately 20 times more soluble in tissue fluid than O₂, which means its effective diffusivity is far greater even across a thickened membrane. When fibrosis increases membrane thickness (reducing diffusion rate by Fick's law for both gases), CO₂'s superior solubility compensates — it continues to diffuse adequately despite the thicker barrier and the smaller partial pressure gradient. O₂ has no such solubility advantage: its diffusion rate is limited by the thickened membrane without compensation, causing blood O₂ to fall. The result is that hypoxemia (low O₂) appears well before hypercapnia (elevated CO₂) in restrictive lung disease. Only when fibrosis or respiratory muscle failure severely limits ventilation does CO₂ accumulate."
  explanation: "This distinction is clinically important for diagnosis. Isolated hypoxemia with normal CO₂ in a patient with breathing difficulty suggests a diffusion or V/Q mismatch problem, not ventilatory failure. Combined hypoxemia and hypercapnia suggests ventilatory failure or very severe disease."
```

## Explainer

Gas exchange is fundamentally a diffusion problem, and diffusion — as you studied via Fick's laws — is driven entirely by concentration gradients. In the lungs, concentration gradients are expressed as **partial pressures**: the pressure exerted by a single gas in a mixture. In freshly inhaled alveolar air, the partial pressure of oxygen (PO₂) is approximately 100 mmHg. In deoxygenated blood arriving at the pulmonary capillaries, PO₂ is about 40 mmHg. Oxygen moves down this 60 mmHg gradient, crossing the respiratory membrane from alveolus into blood. Carbon dioxide flows the other way: PCO₂ is about 45 mmHg in venous blood and only 40 mmHg in alveolar air, so CO₂ diffuses out of blood and into the alveolus to be exhaled.

The **respiratory membrane** is the physical barrier gases must cross, and its anatomy is designed to minimize resistance. It consists of the alveolar epithelial cell, the fused basement membranes of the epithelium and capillary endothelium, and the capillary endothelial cell — together only about 0.5 micrometers thick. Fick's law tells you that diffusion rate is proportional to surface area and inversely proportional to membrane thickness. The ~70 m² of alveolar surface area combined with this extraordinarily thin membrane makes the lungs enormously efficient. Conditions that thicken the membrane (pulmonary fibrosis) or reduce surface area (emphysema) directly impair gas exchange by these physical laws.

The efficiency of exchange also depends on **ventilation-perfusion matching** — how well airflow (ventilation) and blood flow (perfusion) are distributed to the same alveoli. From your study of respiratory anatomy, you know that the lungs have complex branching airways. Ideally, every alveolus that receives fresh air also receives blood flow to pick up that oxygen. When airways are blocked but blood still flows (low V/Q ratio), blood passes without picking up oxygen — a **shunt**. When alveoli receive air but no blood flow (high V/Q ratio), ventilation is wasted — **dead space**. Perfect matching produces maximal gas exchange; mismatching reduces the efficiency even if the membrane itself is intact.

Oxygen and carbon dioxide differ in their diffusion characteristics in an important way. CO₂ is about 20 times more soluble in tissue fluid than O₂, which means it diffuses much more readily across the membrane even though its partial pressure gradient is smaller. This is why hypercapnia (excess CO₂) is usually driven by ventilation problems rather than membrane problems — if someone can breathe adequately, CO₂ clears easily. Hypoxemia (low blood oxygen) is more sensitive to membrane thickening and surface area loss, because O₂ has less solubility to compensate. This distinction is clinically important: a patient with pulmonary fibrosis often develops hypoxemia long before hypercapnia appears.
