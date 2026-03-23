---
id: lung-compliance-and-elastic-recoil
title: Lung Compliance and Elastic Recoil
domain: biology
course: physiology
prerequisites:
- id: respiratory-system-overview
  type: hard
builds-toward:
- airway-resistance-breathing
- ventilation-perfusion-matching
tags:
- compliance
- elasticity
- surfactant
stage: formal-systems
status: draft
---

# Lung Compliance and Elastic Recoil

## Core Idea
Lung compliance—the change in lung volume per unit change in pressure—depends on elastic recoil properties conferred by collagen and elastin, and surface tension at the air-liquid interface reduced by pulmonary surfactant. Reduced compliance increases work of breathing and contributes to restrictive lung diseases.

## How It's Best Learned
Compare pressure-volume curves for normal lungs vs. lungs with reduced compliance. Discuss why surfactant reduces surface tension and why its absence (in respiratory distress syndrome) causes compliance to fall.

## Questions

```yaml
- question: "A patient with emphysema has extensive destruction of pulmonary elastic fibers. A medical student predicts this patient will have very low lung compliance and struggle to inhale. Is the student correct?"
  type: multiple-choice
  options:
    - "Yes — elastic fiber destruction makes the lungs rigid and very difficult to inflate"
    - "No — elastic fiber destruction actually increases compliance (easier to inflate) but eliminates elastic recoil, making expiration inefficient and trapping air"
    - "Yes — but only during expiration, because elastic fibers are only engaged when the lung deflates"
    - "No — elastic fibers have no role in compliance; only surfactant determines lung stiffness"
  answer: 1
  explanation: "This is the key clinical inversion: compliance and elastic recoil are opposite sides of the same mechanism. In emphysema, destruction of elastin fibers removes the elastic recoil that normally drives expiration. The lungs become highly compliant — paradoxically easy to inflate — but they cannot deflate efficiently on their own, trapping air and leading to hyperinflation. Reduced compliance (stiff lungs) is characteristic of restrictive diseases like pulmonary fibrosis, not emphysema. The student confused the two."

- question: "Pulmonary surfactant is most critical for preventing alveolar collapse at which point in the breathing cycle?"
  type: multiple-choice
  options:
    - "During peak inspiration, when alveoli are at maximum volume and surface tension is highest"
    - "During expiration, when alveoli shrink, surfactant molecules compress together and reduce surface tension most — counteracting the Laplace pressure that would otherwise collapse the alveolus"
    - "At high altitude, where reduced atmospheric pressure destabilizes small alveoli"
    - "During strenuous exercise, when increased respiratory rate produces more turbulent airflow"
  answer: 1
  explanation: "Surfactant works by a concentration-dependent mechanism. As alveoli shrink during expiration, surfactant molecules are crowded together at the air-liquid interface, lowering surface tension to near zero — dramatically reducing the collapsing pressure (P = 2T/r). This prevents the catastrophic collapse that would otherwise occur in small alveoli. During inspiration, as alveoli expand, surfactant molecules spread apart and surface tension rises slightly, resisting overexpansion. This dynamic behavior is the key — surfactant stabilizes alveoli at both ends of the volume range."

- question: "According to the Law of Laplace (P = 2T/r), a smaller alveolus generates higher collapsing pressure than a larger alveolus at the same surface tension."
  type: true-false
  answer: true
  explanation: "The Law of Laplace states that the collapsing pressure of a spherical surface is P = 2T/r. With a smaller radius r, the same surface tension T generates a higher inward pressure P. Without surfactant, smaller alveoli would tend to collapse into larger ones because they experience greater collapsing pressure — an unstable situation. Surfactant counters this by reducing surface tension more in smaller (more compressed) alveoli, equalizing pressures across alveoli of different sizes."

- question: "High lung compliance is always beneficial because it means less work is required to expand the lungs during each breath."
  type: true-false
  answer: false
  explanation: "High compliance is beneficial when it reflects normal elastic properties — easy inflation with intact elastic recoil to drive expiration. But pathologically high compliance, as in emphysema, is not beneficial: the loss of elastic fibers means the lungs cannot recoil to force air out, trapping stale air and reducing ventilation efficiency. Meanwhile, pathologically low compliance (stiff lungs, as in respiratory distress syndrome or pulmonary fibrosis) forces the respiratory muscles to work much harder for each breath. Optimal compliance is neither too high nor too low, balancing ease of inflation with adequate elastic recoil."

- question: "Why does the absence of pulmonary surfactant — as in neonatal respiratory distress syndrome — make breathing so difficult?"
  type: short-answer
  answer: "Without surfactant, the air-liquid interface of each alveolus is dominated by the full surface tension of water. By the Law of Laplace (P = 2T/r), this generates large collapsing pressures, especially in small alveoli. The total surface tension across 300 million alveoli makes the lungs extremely stiff (low compliance), requiring enormous inspiratory muscle effort to expand them. Worse, without surfactant's concentration-dependent tension reduction during expiration, alveoli collapse completely between breaths (atelectasis), so each breath must reinflate collapsed alveoli from scratch. Premature infants exhaust themselves within hours trying to breathe against this resistance."
  explanation: "The two-part answer covers both why each breath is hard (low compliance) and why the problem resets with every breath (atelectasis between breaths). Surfactant treatment (exogenous surfactant replacement) is the definitive therapy — within hours of administration, compliance improves dramatically and infants can breathe with normal effort."
```

## Explainer

From your respiratory system overview, you know that breathing requires the respiratory muscles to generate pressure changes that move air in and out of the lungs. But how much pressure is needed to inflate the lungs by a given volume? That question is answered by **lung compliance** — defined as the change in lung volume per unit change in transmural pressure (ΔV/ΔP). High compliance means the lung inflates easily with little pressure; low compliance means the lung is stiff and resists expansion.

Two forces determine compliance. The first is the **elastic tissue** of the lung — networks of collagen and elastin fibers woven through the alveolar walls and around airways. Elastin stretches easily and snaps back, like a rubber band; collagen is stiffer and limits overexpansion, like a safety strap. Together they create **elastic recoil**, the tendency of the lung to collapse inward after being stretched. This is why the lungs don't simply stay inflated when you stop breathing in — the elastic fibers pull them back toward their resting volume. In diseases like emphysema, destruction of elastic fibers reduces recoil, making the lung very compliant (easy to inflate) but unable to deflate efficiently, trapping air inside.

The second — and often more important — force is **surface tension** at the air-liquid interface lining each alveolus. Every alveolus is coated with a thin film of water, and the cohesive forces between water molecules at this film's surface create an inward-directed tension that tends to collapse the alveolus, much like a soap bubble trying to shrink. According to the **Law of Laplace**, the collapsing pressure generated by surface tension is higher in smaller alveoli (P = 2T/r). Without compensation, small alveoli would collapse into larger ones, and the enormous total surface tension across 300 million alveoli would make the lungs extremely stiff — requiring dangerously high pressures to inflate.

The solution is **pulmonary surfactant**, a mixture of phospholipids (mainly dipalmitoylphosphatidylcholine) and proteins secreted by type II alveolar cells. Surfactant molecules sit at the air-liquid interface with their hydrophobic tails pointing toward the air and their hydrophilic heads in the water, disrupting the cohesive forces between water molecules and dramatically reducing surface tension. Crucially, surfactant's effect is concentration-dependent: as an alveolus shrinks during expiration, surfactant molecules are compressed together, reducing surface tension more — which prevents collapse. As it expands during inspiration, surfactant molecules spread apart, allowing surface tension to rise slightly — which prevents overexpansion. This dynamic behavior stabilizes alveoli of different sizes and reduces the overall work of breathing by roughly two-thirds. Premature infants who lack sufficient surfactant develop **neonatal respiratory distress syndrome**: their lungs are so non-compliant that each breath requires enormous effort, and alveoli collapse between breaths (atelectasis).
