---
id: oxygen-diffusion-capacity-lungs
title: Oxygen Diffusion Capacity and Alveolar-Capillary Transfer
domain: biology
course: physiology
prerequisites:
- id: ventilation-perfusion-matching
  type: hard
- id: gas-exchange-and-diffusion
  type: hard
tags:
- dlco
- diffusion-coefficient
- membrane-thickness
stage: advanced
status: draft
---

# Oxygen Diffusion Capacity and Alveolar-Capillary Transfer

## Core Idea
Oxygen diffusion across the alveolar-capillary membrane depends on diffusing capacity (DLCO), which incorporates the alveolar surface area, membrane thickness, and diffusion coefficient of oxygen. Diseases causing alveolar thickening (fibrosis) or surface area loss (emphysema) impair diffusion and cause hypoxemia, particularly during exercise.

## Questions

```yaml
- question: "A patient with pulmonary fibrosis has normal oxygen saturation at rest but drops to 88% during moderate exercise. What best explains this pattern?"
  type: multiple-choice
  options:
    - "Exercise increases oxygen consumption so dramatically that no lung can keep pace"
    - "Fibrosis thickens the alveolar membrane; the diffusion reserve compensates at rest, but exercise shortens capillary transit time and eliminates the buffer"
    - "Exercise-induced hyperventilation reduces alveolar PO₂ by washing out CO₂ too rapidly"
    - "Fibrosis reduces hemoglobin concentration, limiting oxygen-carrying capacity during exertion"
  answer: 1
  explanation: "At rest, blood has ~0.75 seconds of capillary transit time but only needs ~0.25 seconds to equilibrate — a 3x diffusion reserve. Fibrosis slows equilibration, but the reserve compensates. During exercise, cardiac output rises and blood moves faster, shortening transit time. When transit time falls below the equilibration time required by the thickened membrane, oxygen cannot fully transfer before blood exits the capillary, causing arterial O₂ saturation to drop."

- question: "DLCO (diffusing capacity for carbon monoxide) is a clinically useful pulmonary function test primarily because it:"
  type: multiple-choice
  options:
    - "Measures tidal volume and respiratory rate under resting and exercise conditions"
    - "Directly quantifies the partial pressure gradient across the alveolar membrane"
    - "Captures the combined effect of alveolar surface area, membrane thickness, and capillary blood volume on gas transfer efficiency"
    - "Detects airway obstruction characteristic of asthma and COPD"
  answer: 2
  explanation: "DLCO quantifies how efficiently gas crosses the alveolar-capillary membrane, incorporating all three physical determinants: surface area (reduced in emphysema), membrane thickness (increased in fibrosis), and the volume of hemoglobin-containing blood available in pulmonary capillaries. Airway obstruction affects ventilation, not diffusion — DLCO is specific to the diffusion step and can detect early interstitial lung disease before symptoms appear."

- question: "In a healthy adult at rest, blood passing through the pulmonary capillaries reaches full oxygen equilibrium with alveolar air before completing its transit through the capillary bed."
  type: true-false
  answer: true
  explanation: "Equilibration takes approximately 0.25 seconds, while average pulmonary capillary transit time at rest is approximately 0.75 seconds. Blood fully equilibrates at roughly the one-third mark of the capillary, providing a substantial diffusion reserve. This reserve is why patients with early interstitial lung disease remain asymptomatic at rest even as their diffusing capacity is being reduced."

- question: "Emphysema impairs oxygen diffusion primarily by thickening the alveolar-capillary membrane."
  type: true-false
  answer: false
  explanation: "Emphysema impairs diffusion by destroying alveolar walls, dramatically reducing total surface area for gas exchange — the opposite of thickening. This is the key distinction from pulmonary fibrosis, which impairs diffusion by depositing scar tissue that thickens the membrane. Both diseases reduce DLCO but through different mechanisms: surface area loss (emphysema) vs. membrane thickening (fibrosis). Confusing them reverses the underlying pathophysiology."

- question: "Explain why exercise-induced hypoxemia is often the earliest clinical sign of diffusion impairment, appearing before resting hypoxemia does."
  type: short-answer
  answer: "At rest, the lung's diffusion reserve (the blood has ~3x more transit time than it needs for equilibration) compensates for modest reductions in diffusing capacity caused by early disease. Blood still has enough time to equilibrate despite a thickened membrane or reduced surface area. During exercise, cardiac output increases and blood moves through the pulmonary capillaries faster, shortening transit time. When transit time falls below what the impaired membrane requires for full equilibration, blood exits the capillary under-oxygenated and arterial saturation drops. Exercise acts as a physiological stress test that exposes the reduced diffusion reserve before disease is severe enough to compromise resting oxygenation."
  explanation: "This is why DLCO is measured at rest but predicts exercise performance: it quantifies the diffusion reserve. A patient with a DLCO of 60% predicted may be asymptomatic at rest but will desaturate with exertion because the reserve has been substantially consumed."
```

## Explainer

From your study of gas exchange and diffusion, you know that gases move across membranes according to Fick's law: the rate of diffusion is proportional to the surface area and the partial pressure gradient, and inversely proportional to membrane thickness. The lung is engineered to maximize every term in this equation. The alveolar surface area is enormous — roughly 70 square meters in a healthy adult, about the size of a tennis court — spread across approximately 300 million alveoli. The **alveolar-capillary membrane** is extraordinarily thin, typically only 0.2 to 0.5 micrometers, consisting of the alveolar epithelium, a fused basement membrane, and the capillary endothelium. And the partial pressure gradient for oxygen is maintained by continuous ventilation (refreshing alveolar air) and perfusion (cycling deoxygenated blood past the membrane).

The lung's **diffusing capacity** (commonly measured as **DLCO** using carbon monoxide as a test gas) quantifies how efficiently gas crosses this membrane. DLCO captures both the membrane component (surface area and thickness) and the blood component (the volume of hemoglobin available to bind the gas in pulmonary capillaries). In a healthy resting adult, DLCO is more than sufficient: blood passing through the pulmonary capillaries reaches oxygen equilibrium with alveolar air in about 0.25 seconds, yet the transit time through the capillary bed is roughly 0.75 seconds. This means there is a substantial **diffusion reserve** — the blood has three times longer than it needs to fully oxygenate.

This reserve becomes critical during exercise. When cardiac output increases, blood moves through the pulmonary capillaries faster, reducing transit time. In a healthy person, even with transit times shortened to 0.25 seconds during heavy exercise, complete equilibration still occurs because the membrane's diffusing capacity is so large. But in disease states, this margin disappears. **Pulmonary fibrosis** thickens the alveolar-capillary membrane with scar tissue, slowing diffusion so that equilibration requires more time than is available — especially during exercise when transit times are short. **Emphysema** destroys alveolar walls, dramatically reducing surface area. In either case, the diffusion reserve is consumed, and oxygen levels in arterial blood begin to fall.

This is why exercise-induced hypoxemia is often the earliest clinical sign of diffusion impairment. At rest, even a damaged membrane may allow enough time for adequate oxygenation. But the physiological stress test of exercise exposes the reduced reserve: blood rushes through damaged capillaries too quickly to equilibrate, and arterial oxygen saturation drops. The DLCO measurement captures this vulnerability quantitatively, making it one of the most clinically useful pulmonary function tests for detecting early interstitial lung disease or assessing the severity of emphysema.
