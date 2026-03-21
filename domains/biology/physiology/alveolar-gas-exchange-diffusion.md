---
id: alveolar-gas-exchange-diffusion
title: Alveolar Gas Exchange and Diffusion
domain: biology
course: physiology
prerequisites:
- id: gas-exchange-and-diffusion
  type: hard
- id: oxygen-diffusion-capacity-lungs
  type: soft
builds-toward:
- oxygen-transport-hemoglobin-dynamics
- respiratory-acid-base-regulation
tags:
- alveolar
- gas exchange
- diffusion
- oxygen
- carbon dioxide
stage: advanced
status: draft
---

# Alveolar Gas Exchange and Diffusion

## Core Idea
Oxygen and carbon dioxide diffuse passively across the alveolar-capillary membrane along concentration gradients. The large surface area, thin barrier, and extended capillary transit time enable efficient gas exchange. Ventilation-perfusion matching—the ratio of air reaching alveoli to blood reaching capillaries—is critical; mismatch in disease impairs oxygenation despite adequate overall ventilation.

## Questions

```yaml
- question: "A patient with severe pneumonia breathes rapidly with a high total ventilation rate, yet remains profoundly hypoxemic. The most likely explanation is:"
  type: multiple-choice
  options:
    - "Their hemoglobin cannot carry oxygen due to the infection depleting iron stores"
    - "Faster breathing decreases alveolar PO₂ by washing out CO₂ too quickly"
    - "Fluid-filled alveoli create shunt regions where blood passes through the lungs without equilibrating with fresh air, and increased total ventilation cannot oxygenate blood in non-ventilated regions"
    - "Carbon dioxide accumulates faster than oxygen can be absorbed during pneumonia"
  answer: 2
  explanation: "Fluid-filled alveoli in pneumonia are perfused (blood flows through their capillaries) but not ventilated (no fresh air reaches them). This creates a shunt: blood passes through the lungs without picking up oxygen. The hypoxemia from shunt cannot be corrected by breathing faster because the extra air goes into already well-ventilated alveoli, which can only oxygenate the blood that flows through them — and hemoglobin in those regions is already near-saturated. The fundamental problem is that the mismatch between where ventilation goes and where blood flows undermines gas exchange efficiency regardless of total ventilation."

- question: "A pulmonary embolism completely blocks blood flow to the right lower lobe. The affected alveoli remain ventilated normally. This situation creates:"
  type: multiple-choice
  options:
    - "A shunt — blood passes through the affected region without picking up oxygen"
    - "Dead space — air is delivered to alveoli that have no blood flow to exchange gas with"
    - "Hypoxic pulmonary vasoconstriction in the affected region, redirecting blood to improve V/Q"
    - "Normal gas exchange in the affected region due to compensatory oxygen diffusion from adjacent alveoli"
  answer: 1
  explanation: "Dead space is defined as ventilated but unperfused lung — ventilation is wasted because there is no blood to exchange gas with. A pulmonary embolism stops blood flow to a region, making those alveoli dead space. This is the opposite of shunt (perfused but unventilated). Hypoxic pulmonary vasoconstriction (option C) occurs in response to low alveolar PO₂ — but in dead space, PO₂ is normal because ventilation continues; it is perfusion that is absent. Dead space increases the work of breathing without improving oxygenation."

- question: "In the lung, local hypoxia causes pulmonary arterioles to constrict (hypoxic pulmonary vasoconstriction), redirecting blood toward better-ventilated regions — the opposite of the vasodilation response to hypoxia in systemic circulation."
  type: true-false
  answer: true
  explanation: "This counterintuitive reversal is a key feature of pulmonary physiology. Systemic arterioles dilate in response to hypoxia to deliver more oxygenated blood to hypoxic tissues. Pulmonary arterioles constrict in response to hypoxia as a homeostatic mechanism to maintain V/Q matching: if an alveolus is poorly ventilated (low PO₂), constricting its arterioles diverts blood away from that region toward better-ventilated alveoli where it can be oxygenated. This is an active regulatory mechanism that limits the V/Q mismatch caused by regional hypoventilation."

- question: "As long as a patient's total minute ventilation is adequate — they are moving a normal volume of air per minute — their gas exchange will be sufficient, regardless of how that ventilation is distributed among alveoli."
  type: true-false
  answer: false
  explanation: "Total ventilation does not guarantee adequate gas exchange — V/Q matching at the regional level is what matters. A patient could have perfectly normal total ventilation and total cardiac output while still being profoundly hypoxemic if the ventilation and perfusion are mismatched at the alveolar level (ventilated alveoli not perfused, or perfused alveoli not ventilated). This is exactly the situation in pneumonia (shunt) and pulmonary embolism (dead space). Effective gas exchange requires the right amount of air and blood in the same alveolus at the same time."

- question: "Explain why a patient with severe V/Q mismatch can be profoundly hypoxemic despite breathing rapidly. What specifically goes wrong in a shunt situation?"
  type: short-answer
  answer: "Gas exchange requires that ventilation and perfusion meet in the same alveolus. In a shunt (e.g., fluid-filled alveoli in pneumonia), blood flows through capillaries of unventilated alveoli and reaches the pulmonary veins without picking up oxygen — it is essentially bypassing the lung's gas-exchange function. This deoxygenated blood mixes with oxygenated blood from normal regions, dragging down arterial PO₂. Breathing faster increases ventilation to the normal alveoli, but those alveoli can only maximally saturate hemoglobin in the blood flowing through them — they cannot compensate for the shunted blood from non-ventilated regions. Hemoglobin is already near-saturation in well-ventilated regions, so more ventilation there adds little additional O₂ to the total. The shunted blood remains poorly oxygenated regardless of how fast the patient breathes."
```

## Explainer

From your study of gas exchange and diffusion, you know that gases move passively from regions of high partial pressure to low partial pressure. Alveolar gas exchange applies this principle at an astonishing scale. The lungs contain roughly 300 million **alveoli** — tiny, thin-walled air sacs that collectively provide about 70 square meters of surface area for gas exchange, roughly the size of a tennis court folded into your chest. Each alveolus is wrapped in a dense mesh of capillaries, and the barrier separating air from blood is only about 0.5 micrometers thick — thin enough that oxygen and carbon dioxide can diffuse across it in a fraction of a second.

The driving force for gas exchange is the **partial pressure gradient**. Inspired air arriving in the alveoli has a PO₂ of about 104 mmHg, while deoxygenated blood entering the pulmonary capillaries has a PO₂ of roughly 40 mmHg. This 64 mmHg gradient drives oxygen from alveolar air into the blood. For carbon dioxide, the gradient is reversed but smaller: venous blood PCO₂ is about 45 mmHg while alveolar PCO₂ is about 40 mmHg. Despite this smaller gradient, CO₂ diffuses about 20 times more readily than O₂ because of its much higher solubility in the aqueous layer lining the alveoli. Blood spends approximately 0.75 seconds transiting a pulmonary capillary, but equilibration for both gases is essentially complete within the first third of that transit — providing a substantial safety margin during exercise when transit time shortens.

The efficiency of gas exchange depends critically on **ventilation-perfusion (V/Q) matching** — the ratio of air delivered to an alveolus to the blood flow through its capillaries. The ideal V/Q ratio is about 1.0, meaning ventilation and perfusion are perfectly matched. In reality, gravity creates regional differences: in an upright person, the lung bases receive more blood flow (perfusion) than the apices, while ventilation is more evenly distributed. The body compensates through **hypoxic pulmonary vasoconstriction** — when an alveolus is poorly ventilated and its local PO₂ drops, the surrounding arterioles constrict, diverting blood away from that region toward better-ventilated areas. This is the opposite of what happens in systemic circulation, where hypoxia causes vasodilation.

When V/Q matching breaks down — as in pneumonia (where fluid fills alveoli, reducing ventilation) or pulmonary embolism (where a clot blocks perfusion) — gas exchange deteriorates even if total ventilation and total cardiac output are normal. A region with ventilation but no perfusion is **dead space** (wasted ventilation), while a region with perfusion but no ventilation is a **shunt** (blood passes through the lungs without picking up oxygen). Understanding V/Q mismatch explains why patients with lung disease can be profoundly hypoxemic despite breathing rapidly: the problem is not how much air moves in and out, but whether that air reaches regions where blood is flowing.
