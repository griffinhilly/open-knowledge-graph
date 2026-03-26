---
id: respiratory-mechanics-and-gas-exchange
title: Respiratory Mechanics and Gas Exchange
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: respiratory-system-anatomy-and-ventilation
  type: hard
- id: pulmonary-ventilation-mechanics-compliance
  type: hard
- id: gas-exchange-and-diffusion
  type: hard
- id: hemoglobin-cooperativity-oxygen-binding
  type: hard
- id: gas-exchange-alveoli-and-diffusion
  type: soft
builds-toward:
- oxygen-transport-and-hemoglobin
- acid-base-homeostasis-physiology
tags:
- ventilation
- compliance
- airway-resistance
- gas-exchange
stage: formal-systems
status: validated
---
# Respiratory Mechanics and Gas Exchange

## Core Idea
Breathing depends on pressure gradients created by diaphragm contraction and elastic recoil of lung tissue. Lung compliance—the change in volume per unit pressure change—reflects the elastic properties of lung parenchyma and chest wall. Airway resistance is proportional to airway radius to the 4th power, making small airways disproportionately important. Gas exchange occurs across the alveolar-capillary membrane by simple diffusion driven by partial pressure gradients.

## How It's Best Learned
Measure your own lung volumes and capacities using spirometry. Trace air pathways through progressively smaller generations of airways to understand how resistance increases nonlinearly.

## Common Misconceptions
- Thinking the diaphragm pulls air into the lungs; actually it creates a negative pressure gradient that air flows down.
- Assuming equal ventilation to all lung regions; gravity and pleural pressure gradients create regional differences.

## Questions

```yaml
- question: "A patient has emphysema, where the elastic tissue of the lung parenchyma is destroyed. What is the primary consequence for breathing mechanics?"
  type: multiple-choice
  options:
    - "Inspiration becomes extremely difficult because the lungs are too stiff to expand"
    - "Expiration becomes difficult because passive elastic recoil is lost, requiring active muscular effort to exhale"
    - "Airway resistance increases dramatically because the destroyed tissue narrows the bronchioles"
    - "Gas exchange improves because the thinner alveolar walls reduce diffusion distance"
  answer: 1
  explanation: "Elastic recoil drives passive expiration. In emphysema, destruction of elastic tissue means the lungs no longer recoil inward after inspiration, so the patient must actively use expiratory muscles to exhale — this is why emphysema patients often purse their lips and lean forward. Option A describes pulmonary fibrosis (stiff lungs), not emphysema. Emphysema actually makes inflation easy; it's expiration that suffers."

- question: "Bronchospasm reduces an airway's radius by half. By approximately what factor does resistance in that airway increase?"
  type: multiple-choice
  options:
    - "2-fold — resistance increases proportionally to the reduction in radius"
    - "4-fold — resistance scales with the square of the radius"
    - "8-fold — resistance scales with the cube of the radius"
    - "16-fold — resistance is inversely proportional to the fourth power of the radius"
  answer: 3
  explanation: "Poiseuille's Law states resistance ∝ 1/r⁴. Halving the radius means the new resistance = 1/(0.5)⁴ = 1/0.0625 = 16 times the original. This fourth-power relationship explains why even modest bronchospasm during an asthma attack dramatically increases the work of breathing — a 30% reduction in radius more than quadruples resistance. The linear, squared, and cubed options represent common misconceptions about the r⁴ relationship."

- question: "During quiet breathing at rest, expiration is an active process that requires contraction of the abdominal and internal intercostal muscles."
  type: true-false
  answer: false
  explanation: "Quiet expiration is entirely passive. At rest, the diaphragm simply relaxes, and the elastic recoil of the lungs and chest wall compresses alveolar volume, raising alveolar pressure above atmospheric. Air flows out down the resulting pressure gradient with no muscular effort. Active expiration only occurs during exercise or forced breathing when faster or more complete exhalation is required."

- question: "In pulmonary fibrosis, lung compliance is reduced, which means more muscular work is required for each breath."
  type: true-false
  answer: true
  explanation: "Compliance is the volume change per unit pressure change (ΔV/ΔP). Reduced compliance means the lungs are stiffer — a larger pressure change is needed to achieve the same volume change. This requires greater diaphragm and accessory muscle effort on each inspiration. Patients with pulmonary fibrosis typically breathe with a pattern of rapid, shallow breaths, as each deep breath is prohibitively effortful."

- question: "Why does halving an airway's diameter increase its resistance by 16-fold rather than 2-fold, and what does this mean clinically for conditions like asthma?"
  type: short-answer
  answer: "Airway resistance follows Poiseuille's Law: resistance is inversely proportional to the fourth power of the radius (R ∝ 1/r⁴). Halving the radius means resistance increases by (1/0.5)⁴ = 16-fold. Clinically, this means that even modest bronchospasm in asthma — perhaps reducing airway diameter by 20–30% — produces a disproportionately large increase in resistance and breathing work, explaining why asthma attacks can become life-threatening rapidly and why bronchodilators that restore even partial airway diameter have dramatic therapeutic effects."
  explanation: "The key insight is the nonlinearity. A linear relationship would mean diameter halved = resistance doubled. The r⁴ relationship amplifies small anatomical changes into enormous physiological consequences. This also explains why total airway resistance is actually highest in large central airways (absolute resistance) rather than the terminal bronchioles — even though individual small airways have high resistance, they exist in large numbers and act in parallel, reducing their collective contribution."
```

## Explainer

You already know the anatomy of the respiratory tract and that ventilation moves air in and out. This topic explains the *mechanics* — the physical forces that make breathing work — and the *chemistry* of how gases actually cross from air into blood. Both depend on gradients: pressure gradients for bulk airflow, and partial pressure gradients for diffusion.

**Inspiration** begins with diaphragm contraction. When the diaphragm flattens, it increases thoracic volume. Because the pleural space is sealed and the lungs are attached to the chest wall by surface tension across the thin pleural fluid layer, lung volume increases too. By Boyle's Law, increasing volume decreases pressure — alveolar pressure drops below atmospheric, and air flows down the pressure gradient into the lungs. **Expiration** at rest is passive: the diaphragm relaxes, elastic recoil of the lung tissue compresses alveolar volume, pressure rises above atmospheric, and air flows out. **Lung compliance** — the volume increase per unit pressure increase — reflects how easily the lungs stretch. Reduced compliance (stiff lungs, as in pulmonary fibrosis) means more muscular effort is needed for each breath. Increased compliance (as in emphysema, where elastic tissue is destroyed) makes inflation easy but expiration hard because passive recoil is lost.

**Airway resistance** is governed by Poiseuille's Law: resistance is inversely proportional to the *fourth power* of airway radius. Halving an airway's diameter multiplies its resistance 16-fold. This is why bronchospasm — even modest airway narrowing — produces dramatic increases in breathing work. Paradoxically, total cross-sectional area increases enormously as airways branch toward the alveoli, so resistance is actually highest in the large, central airways, not the terminal bronchioles.

**Gas exchange** occurs across the **alveolar-capillary membrane**, a barrier less than 0.5 μm thick. Oxygen diffuses from alveolar air (partial pressure ~100 mmHg) into pulmonary capillary blood (arriving at ~40 mmHg), while CO₂ diffuses in the opposite direction (from ~46 mmHg in blood to ~40 mmHg in alveoli). This diffusion is passive — no active transport — and depends on membrane area, membrane thickness, and the partial pressure gradient. Your prerequisite knowledge of hemoglobin's cooperative oxygen binding explains how blood loads oxygen so efficiently even though the driving gradient is modest: the sigmoidal O₂-hemoglobin dissociation curve means small drops in pO₂ trigger large unloading of oxygen at the tissues, while small rises in pO₂ drive nearly complete loading at the alveoli.
