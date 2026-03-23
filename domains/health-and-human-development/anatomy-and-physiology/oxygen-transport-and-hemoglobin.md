---
id: oxygen-transport-and-hemoglobin
title: Oxygen Transport and Hemoglobin
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: respiratory-mechanics-and-gas-exchange
  type: hard
- id: oxygen-hemoglobin-binding-cooperativity
  type: hard
- id: blood-composition-and-function
  type: hard
- id: hemoglobin-cooperativity-oxygen-binding
  type: hard
- id: protein-quaternary-structure
  type: soft
builds-toward:
- acid-base-homeostasis-physiology
tags:
- hemoglobin
- oxygen-binding
- cooperativity
- oxygen-content
stage: formal-systems
status: validated
---

# Oxygen Transport and Hemoglobin

## Core Idea
Hemoglobin's oxygen-carrying capacity depends on cooperative binding: oxygen binding to one subunit increases affinity of others, creating a sigmoidal binding curve. This cooperativity allows high oxygen loading in lungs and substantial oxygen unloading in tissues. The oxygen content of blood includes both dissolved oxygen and hemoglobin-bound oxygen; dissolved oxygen contributes minimally but becomes significant at high altitude or hyperbaric conditions.

## Questions

```yaml
- question: "A patient with severe anemia (hemoglobin 5 g/dL) has a pulse oximetry reading of 99%. Which statement best describes their oxygen delivery?"
  type: multiple-choice
  options:
    - "Oxygen delivery is normal — saturation of 99% indicates the blood is carrying maximal oxygen"
    - "Oxygen delivery is critically reduced — hemoglobin concentration dominates total oxygen content"
    - "Oxygen delivery is slightly reduced — dissolved oxygen partially compensates"
    - "Oxygen delivery cannot be assessed without knowing arterial PO₂"
  answer: 1
  explanation: "Oxygen content is CaO₂ = (1.34 × Hgb × SaO₂) + (0.003 × PaO₂). At Hgb = 5 g/dL and SaO₂ = 99%, the hemoglobin-bound component is only 1.34 × 5 × 0.99 ≈ 6.6 mL/100 mL — roughly one-third of normal. Pulse oximetry measures saturation, not content. The common error is equating 'fully saturated' with 'adequate oxygen delivery'; the hemoglobin concentration term dominates, so severe anemia is life-threatening even with normal SaO₂."

- question: "The sigmoidal shape of the oxyhemoglobin dissociation curve, as opposed to a simple hyperbolic shape, provides which physiological advantage?"
  type: multiple-choice
  options:
    - "It allows hemoglobin to bind the maximum number of oxygen molecules at any PO₂ above zero"
    - "It keeps hemoglobin highly saturated across a wide range of alveolar PO₂ while still allowing substantial unloading in tissues"
    - "It increases the total oxygen-carrying capacity per gram of hemoglobin"
    - "It prevents any oxygen from being released until the tissues are severely hypoxic"
  answer: 1
  explanation: "The flat upper portion of the sigmoid (PO₂ 70–100 mmHg) means hemoglobin stays highly saturated even at altitude or with mild hypoventilation — a useful safety margin. The steep middle portion (PO₂ 20–60 mmHg) is where most unloading occurs in tissues. A hyperbolic curve (like myoglobin's) would stay saturated in tissues and unload poorly. Cooperativity produces this S-shape, which is not merely aesthetic — it is functionally essential."

- question: "A rightward shift of the oxyhemoglobin dissociation curve, caused by tissue acidosis (Bohr effect), increases oxygen loading in the lungs."
  type: true-false
  answer: false
  explanation: "A rightward shift reduces hemoglobin's affinity for oxygen — it promotes unloading in tissues, not loading. In the lungs (where pH is higher and CO₂ lower), the curve is shifted leftward, favoring loading. The Bohr effect is a fine-tuning mechanism that matches unloading to metabolic demand: acidic, CO₂-rich, active tissues extract more oxygen from each passing hemoglobin molecule."

- question: "The majority of oxygen carried in arterial blood is dissolved directly in plasma rather than bound to hemoglobin."
  type: true-false
  answer: false
  explanation: "At normal arterial PO₂ of 100 mmHg, dissolved oxygen contributes only ~0.3 mL/100 mL of blood. Hemoglobin-bound oxygen at normal hemoglobin levels contributes ~19–20 mL/100 mL — roughly 66 times more. Dissolved oxygen matters clinically only in extremes: hyperbaric oxygen therapy raises dissolved O₂ enough to sustain metabolism without functional hemoglobin, which is why it treats carbon monoxide poisoning."

- question: "Why can a patient with severe anemia have critically low oxygen delivery despite a normal or near-normal pulse oximetry reading? Explain using the oxygen content equation."
  type: short-answer
  answer: "Pulse oximetry measures SaO₂ (the fraction of hemoglobin that is saturated), not total oxygen content. Oxygen content is CaO₂ = (1.34 × Hgb × SaO₂) + (0.003 × PaO₂). The hemoglobin concentration term dominates: with severe anemia (low Hgb), even fully saturated hemoglobin carries far less oxygen per deciliter of blood than normal. Dissolved oxygen (the second term) is trivially small at normal PO₂. So oxygen delivery — the product of cardiac output and content — is critically reduced despite a reassuring saturation reading."
  explanation: "This is one of the most clinically important distinctions in respiratory physiology. Saturation tells you what fraction of available hemoglobin is loaded; content tells you the actual amount of oxygen per unit volume. Both the 'how full' (saturation) and the 'how many' (hemoglobin concentration) terms matter. Treating only the saturation is like knowing a fuel tank is 99% full while ignoring that the tank is 1/3 its normal size."
```

## Explainer

From your study of respiratory mechanics and gas exchange, you know that oxygen moves from alveoli into capillary blood down a partial pressure gradient. But simply dissolving in plasma would be hopelessly inadequate — at normal arterial PO₂ of 100 mmHg, only about 0.3 mL of O₂ dissolves per 100 mL of blood. Resting tissues need roughly 5 mL/100 mL. **Hemoglobin** solves this problem by binding oxygen reversibly and carrying it in a chemically bound form: a single gram of hemoglobin can carry 1.34 mL O₂ when fully saturated, so blood with 15 g/dL hemoglobin can carry nearly 20 mL O₂ per 100 mL — a 66-fold amplification over dissolved oxygen alone. The total **oxygen content** formula captures both contributions: CaO₂ = (1.34 × Hgb × SaO₂) + (0.003 × PaO₂).

The sigmoidal shape of the **oxyhemoglobin dissociation curve** is not an accident — it is a direct consequence of **cooperative binding**, which you studied in the prerequisite on hemoglobin cooperativity. Hemoglobin's four subunits communicate through conformational change: when the first O₂ binds, it shifts the protein toward a high-affinity "R state," making subsequent binding easier. This cooperativity produces the S-shaped curve. The steep middle portion (PO₂ 20–60 mmHg) is where most O₂ unloading to tissues occurs. The flat upper portion (PO₂ 70–100 mmHg) means hemoglobin stays highly saturated across a wide range of alveolar conditions — a safety margin that lets you breathe comfortably at altitude without dramatic drops in oxygen delivery.

Three physiological variables shift the curve and fine-tune O₂ delivery. **The Bohr effect**: rising CO₂ and falling pH in metabolically active tissues shift the curve rightward, reducing hemoglobin's affinity for O₂ and promoting unloading exactly where it is needed. **2,3-bisphosphoglycerate (2,3-BPG)**, a glycolytic intermediate that accumulates in red blood cells under hypoxia, binds the central cavity of deoxyhemoglobin and stabilizes the T (low-affinity) state — another rightward shift. **Temperature** also shifts the curve rightward in hot, active muscle. All three effects converge to ensure that working tissues, which are acidic, CO₂-rich, warm, and hypoxic, extract more oxygen from each hemoglobin molecule that passes through.

Understanding oxygen content (not just saturation) prevents a common clinical error. A patient with severe anemia may have normal SaO₂ of 99% yet critically low oxygen delivery — because the hemoglobin concentration term dominates the content equation. Conversely, hyperbaric oxygen therapy raises PaO₂ high enough that the dissolved oxygen term alone can sustain metabolism even without hemoglobin, which is why it can treat carbon monoxide poisoning where hemoglobin is blocked. The interplay between the two forms of oxygen transport — dissolved and hemoglobin-bound — defines the physiological and clinical picture across a wide range of conditions.
