---
id: respiratory-anatomy-and-mechanics
title: Respiratory System Anatomy and Ventilation Mechanics
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: body-organization-and-terminology
  type: hard
- id: respiratory-system-overview
  type: hard
- id: gas-exchange-and-diffusion
  type: hard
builds-toward:
- ventilation-and-gas-transport
tags:
- lungs
- alveoli
- diaphragm
- compliance
- tidal-volume
- spirometry
stage: formal-systems
status: validated
---

# Respiratory System Anatomy and Ventilation Mechanics

## Core Idea
The respiratory system consists of conducting airways (nasal cavity → pharynx → larynx → trachea → bronchi → bronchioles) and the respiratory zone (respiratory bronchioles → alveolar ducts → alveoli). The ~300 million alveoli provide ~70 m² of surface area for gas exchange. Ventilation is driven by pressure gradients created by volume changes: the diaphragm and external intercostals contract during inhalation, expanding thoracic volume and lowering intrapulmonary pressure below atmospheric. Lung compliance (stretchability) and surfactant (which reduces surface tension and prevents alveolar collapse) are key determinants of respiratory work.

## How It's Best Learned
Use a bell-jar lung model to visualize the pressure-volume relationship during breathing. Practice interpreting spirometry traces to identify tidal volume, vital capacity, residual volume, and FEV1.

## Common Misconceptions
- We do not breathe by 'sucking air in'; the diaphragm creates negative pressure and air flows in passively along the pressure gradient.
- Surfactant is not just a lubricant — it is a phospholipid complex that reduces surface tension and is critical for premature infants.

## Questions

```yaml
- question: "A patient with asthma has airway narrowing (bronchoconstriction) that slows airflow out of the lungs. Which spirometry pattern would you expect?"
  type: multiple-choice
  options:
    - "Reduced total lung capacity and vital capacity with a normal FEV₁/FVC ratio"
    - "Low FEV₁/FVC ratio with near-normal total lung volumes, because narrowed airways slow forced expiration disproportionately"
    - "Normal spirometry, since asthma affects gas exchange but not mechanical airflow"
    - "Increased FEV₁/FVC ratio, because bronchospasm forces air out more rapidly"
  answer: 1
  explanation: "Asthma is an obstructive disease: airway narrowing increases resistance, particularly during forced expiration (which tends to collapse already-narrowed airways further). FEV₁ falls because air cannot move out rapidly in 1 second, while FVC may be more preserved. The FEV₁/FVC ratio below ~0.70 indicates obstruction. In contrast, restrictive diseases like pulmonary fibrosis shrink total lung volumes but leave the FEV₁/FVC ratio normal — both numerator and denominator shrink proportionally when the lung is simply stiff and small, not obstructed."

- question: "During normal quiet inhalation, which statement most accurately describes how air enters the lungs?"
  type: multiple-choice
  options:
    - "The lungs actively expand by contracting smooth muscle in the alveolar walls, creating suction pressure"
    - "The diaphragm and external intercostals contract, increasing thoracic volume; intrapulmonary pressure falls below atmospheric pressure, and air flows in along the pressure gradient"
    - "The trachea dilates, reducing airway resistance enough to allow passive airflow driven by body heat"
    - "Surfactant secretion at the alveoli creates a chemical gradient that pulls air molecules inward"
  answer: 1
  explanation: "Breathing is an application of Boyle's law: at constant temperature, pressure and volume are inversely related. When the diaphragm flattens and the rib cage lifts (via the external intercostals), thoracic volume increases. Air already in the lungs now occupies a larger space, so its pressure drops below atmospheric (~760 mmHg). This gradient — high pressure outside, lower inside — drives air in. The lungs do not 'suck' air; they create a low-pressure zone that the atmosphere fills. Exhalation at rest is the reverse: muscle relaxation allows elastic recoil to decrease volume and raise pressure above atmospheric."

- question: "Normal quiet exhalation requires no muscular effort because relaxation of the inspiratory muscles allows the thorax and lungs to recoil passively, raising intrapulmonary pressure above atmospheric."
  type: true-false
  answer: true
  explanation: "The lungs and chest wall have elastic properties: stretched during inhalation, they naturally recoil toward their resting position when the diaphragm and external intercostals relax. This recoil decreases lung volume, raises intrapulmonary pressure above atmospheric, and drives air out — all without active muscular contraction. Forced exhalation (as in blowing hard or during exercise) does recruit internal intercostals and abdominal muscles, but quiet tidal breathing relies entirely on passive elastic recoil."

- question: "Surfactant prevents alveolar collapse primarily by lubricating adjacent alveolar surfaces so they can slide freely past each other during breathing."
  type: true-false
  answer: false
  explanation: "Surfactant works by reducing surface tension at the air-liquid interface of alveoli, not by lubrication. By Laplace's law (P = 2T/r), surface tension at a curved surface creates a collapsing pressure — and for tiny alveoli, this would be enormous without intervention. Surfactant — a phospholipid mixture secreted by type II pneumocytes — inserts into the air-liquid interface and dramatically lowers surface tension, reducing the collapsing pressure. Without surfactant, alveoli collapse (atelectasis) at the end of each breath. This is why premature infants lacking mature type II cells develop respiratory distress syndrome, treated by administering synthetic surfactant."

- question: "Explain, using Boyle's law, why contracting the diaphragm causes air to flow into the lungs."
  type: short-answer
  answer: "Boyle's law states that at constant temperature, pressure and volume are inversely related (PV = constant). When the diaphragm contracts and flattens, it increases the volume of the thoracic cavity. The air inside the lungs now occupies a larger volume, so its pressure drops below atmospheric. This creates a pressure gradient — atmospheric pressure (~760 mmHg) outside is greater than intrapulmonary pressure (now ~758 mmHg) — and air flows from high to low pressure, from the atmosphere into the lungs, until the pressures equalize. The diaphragm does not suck air in; it creates the low-pressure zone that the atmosphere fills."
  explanation: "The key insight is that breathing is passive air movement driven by pressure gradients, not active suction. The respiratory muscles change volume; Boyle's law translates that volume change into a pressure change; and the pressure difference drives bulk airflow. This is also why a penetrating chest wound (pneumothorax) can be immediately life-threatening: air enters the pleural space instead of the lungs, collapsing the pressure gradient that drives inhalation."
```

## Explainer

From your study of gas exchange and diffusion, you know that gases move down concentration gradients across thin membranes. The respiratory system's job is to continuously replenish the air on one side of that membrane — the alveolar side — so the gradient never collapses. To do that, the lungs must move air in and out through a branching network of passages, each level serving a different function. The **conducting zone** (nose to terminal bronchioles) warms, humidifies, and filters incoming air but performs no gas exchange — it is the delivery system. The **respiratory zone** begins where the bronchioles become alveolated, and here the actual diffusion you studied occurs across a membrane thinner than a cell.

Breathing is a pressure game. Boyle's law — which you encountered in your study of body organization and gas behavior — states that at constant temperature, pressure and volume are inversely related. The respiratory system exploits this: when the **diaphragm** contracts and flattens, the thoracic cavity expands; when the external intercostals contract, the rib cage lifts outward. Both movements increase lung volume. Because air in the lungs is now spread over a larger space, its pressure falls below atmospheric (~760 mmHg). Air flows in along this pressure gradient — the lung does not suck; it creates a low-pressure zone that the atmosphere fills. Exhalation is normally passive: the diaphragm relaxes, the chest recoils, volume decreases, pressure rises above atmospheric, and air flows out.

**Lung compliance** is the stretchability of the lung tissue — how much volume change you get per unit of pressure change. Stiff lungs (low compliance, as in pulmonary fibrosis) require more muscular effort to inflate. But compliance alone would make breathing impossible without one critical ingredient: **surfactant**. The alveoli are tiny air sacs, and surface tension at the air-liquid interface (La Place's law: pressure = 2T/r) would collapse small alveoli into large ones and require enormous pressure to re-inflate them. Surfactant — a mixture of phospholipids secreted by type II pneumocytes — coats the alveolar surface and reduces surface tension dramatically. Without it, alveoli collapse at the end of each breath (atelectasis). In premature infants whose type II cells are not yet mature, this is life-threatening — the basis for administering synthetic surfactant at birth.

**Lung volumes** measured by spirometry reflect the functional capacity of the respiratory system. **Tidal volume** (~500 mL) is the volume of a normal quiet breath. **Vital capacity** is the maximum volume exhaled after a maximum inhalation. **Residual volume** (~1.2 L) is the air that stays in the lungs after maximal exhalation — this cannot be measured by spirometry because you cannot exhale it. **FEV₁** (forced expiratory volume in 1 second) measures how quickly air moves out and is the key diagnostic for obstructive diseases like asthma (low FEV₁/FVC ratio, because narrowed airways slow expiration) versus restrictive diseases like fibrosis (normal FEV₁/FVC ratio, but small total volumes because stiff lungs cannot expand fully). These traces are your primary clinical window into respiratory mechanics.
