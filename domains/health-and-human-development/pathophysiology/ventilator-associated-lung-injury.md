---
id: ventilator-associated-lung-injury
title: Ventilator-Associated Lung Injury
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: ards-pathophysiology
  type: soft
tags:
- ventilator
- barotrauma
- volutrauma
- biotrauma
- lung-injury
stage: expert
status: validated
---

# Ventilator-Associated Lung Injury

## Core Idea
Mechanical ventilation, while life-saving, can paradoxically injure the lungs through barotrauma (high pressures rupturing alveoli), volutrauma (overdistension from large tidal volumes), atelectotrauma (repetitive opening/closing of alveoli), and biotrauma (mechanical stress triggering inflammatory mediator release). Ventilator-associated lung injury is a spectrum from subclinical inflammation to overt pulmonary edema and gas trapping. Lung-protective ventilation strategies (low tidal volume 6-8 mL/kg, PEEP to prevent collapse, plateau pressure <30 cmH2O) reduce VALI incidence.

## How It's Best Learned
Study the mechanisms of each type of VALI. Understand why PEEP is both preventive (reopens collapsed alveoli) and harmful (overdistension if excessive). Compare lung-protective ventilation strategies and their physiologic basis.

## Common Misconceptions
PEEP is not always harmful; appropriate PEEP prevents atelectotrauma by maintaining alveolar recruitment. Ventilator-induced lung injury can occur even with controlled, 'protected' ventilation if underlying disease is severe. The balance between ventilation and avoiding injury is dynamic and requires frequent reassessment.

## Questions

```yaml
- question: "The ARDSNet trial compared tidal volumes of 6 mL/kg versus 12 mL/kg in ARDS patients. The low-volume group developed higher CO₂ levels (permissive hypercapnia). Why was this accepted rather than corrected by using larger breaths?"
  type: multiple-choice
  options:
    - "Elevated CO₂ is beneficial in ARDS because it suppresses the inflammatory response"
    - "The volutrauma caused by larger tidal volumes to normalize CO₂ costs more in lung injury than the elevated CO₂ is worth"
    - "The ventilators used in the trial could not regulate CO₂ levels precisely enough"
    - "Elevated CO₂ improves oxygen delivery by shifting the hemoglobin dissociation curve rightward"
  answer: 1
  explanation: "The ARDSNet insight was that the mortality cost of volutrauma from larger tidal volumes (22% higher mortality in the 12 mL/kg group) outweighs the cost of mild hypercapnia. 'Permissive hypercapnia' is a deliberate trade-off: accept elevated CO₂ to protect the lung from stretch injury. Option D describes the Bohr effect, which is real but is not why hypercapnia was permitted; option A is incorrect — elevated CO₂ does not play a beneficial anti-inflammatory role in this context."

- question: "A mechanically ventilated ARDS patient has a plateau pressure of 27 cmH₂O — apparently safely below the 30 cmH₂O threshold. Why might significant volutrauma still be occurring?"
  type: multiple-choice
  options:
    - "Plateau pressure is unreliable in ARDS because airways are collapsed and do not transmit pressure accurately"
    - "The ARDS lung is heterogeneous — tidal volume distributes almost entirely into the small fraction of open alveoli, which suffer enormous stretch even at acceptable global airway pressures"
    - "Volutrauma requires pressures above 30 cmH₂O; below that threshold it cannot occur regardless of volume"
    - "Biotrauma elevates pressure readings, making them appear lower than the actual injurious pressure"
  answer: 1
  explanation: "This is the 'baby lung' concept: consolidated and atelectatic regions are functionally unavailable, so a tidal volume calculated for a normal-sized lung channels almost entirely into a much smaller volume of recruitable alveoli. Each of those alveoli is stretched far beyond safe limits even though global airway pressure appears controlled. This is why driving pressure (plateau pressure minus PEEP) is a better surrogate for alveolar strain than plateau pressure alone — it normalizes to the actual compliant lung volume."

- question: "Positive end-expiratory pressure (PEEP) can be both protective against ventilator-associated lung injury and a cause of it, depending on how much is applied."
  type: true-false
  answer: true
  explanation: "PEEP prevents atelectotrauma by maintaining recruited alveoli open at end-expiration, eliminating the repetitive collapse-re-expansion cycle and its shear forces. But excessive PEEP overdistends already-open alveoli in adjacent regions, causing volutrauma — and can increase right ventricular afterload enough to compromise cardiac output. Optimal PEEP is patient-specific, requiring titration that balances recruitment against overdistension in each patient's unique lung architecture."

- question: "Barotrauma — injury from high airway pressure — is the primary mechanism of ventilator-associated lung injury, making pressure monitoring more important than volume monitoring."
  type: true-false
  answer: false
  explanation: "Volutrauma — injury from alveolar wall stretch due to excessive volume change — is now understood to be more important than barotrauma alone. Classic experiments showed that lung injury correlates better with tidal volume than with peak pressure: high-pressure, low-volume ventilation causes less injury than low-pressure, high-volume ventilation. Plateau pressure is useful as a surrogate because it approximates distending pressure, but the actual injurious force is alveolar stretch, not pressure per se. This is why volume limits (6 mL/kg ideal body weight) are the foundation of lung-protective ventilation."

- question: "Why does the heterogeneous nature of ARDS — with mixed areas of consolidated, atelectatic, and still-normal lung — make weight-based tidal volume calculations potentially misleading?"
  type: short-answer
  answer: "A tidal volume calculated for the patient's full body weight actually distributes only into the small, open fraction of recruitable lung. This concentrated volume causes massive overdistension in the remaining open alveoli, even when global airway pressures look acceptable. The 'baby lung' concept captures this: the functional lung receiving ventilation may be only 20–30% of normal size, so a volume that seems modest by weight creates enormous regional strain in the open alveoli."
  explanation: "This is why driving pressure (ΔP = plateau pressure − PEEP) is a better correlate of alveolar strain and mortality than tidal volume per kilogram alone — it normalizes volume to the actual compliant lung volume. Emerging tools like electrical impedance tomography can directly visualize regional ventilation distribution, enabling truly individualized lung protection."
```

## Explainer

Mechanical ventilation saves lives by taking over the work of breathing when a patient cannot maintain adequate gas exchange. But the mechanics of artificial ventilation differ fundamentally from physiologic breathing, and those differences carry real risks. Normally, inhalation is driven by diaphragmatic contraction creating negative intrathoracic pressure — the lung is pulled open from outside. Positive-pressure mechanical ventilation pushes air in from above, stressing the lung from inside. You know from your study of ARDS pathophysiology that the diseased lung is not uniformly stiff but a heterogeneous patchwork of consolidated, atelectatic, and still-normal regions. A tidal volume that seems reasonable by weight-based calculation gets channeled almost entirely into the small fraction of open lung, producing enormous regional overdistension in those units even while global airway pressures look acceptable.

The four mechanisms of VALI each represent a different way that ventilatory physics can damage cells. **Barotrauma** is the most visible: high peak airway pressures rupture alveoli, forcing air into the pleural space (pneumothorax), mediastinum (pneumomediastinum), or subcutaneous tissue. **Volutrauma** is subtler and arguably more dangerous: it is the *volume change* — the stretch of alveolar walls — not peak pressure per se, that tears epithelial and endothelial cells. A highly non-compliant ARDS lung may transmit high pressures to a tiny volume of recruitable alveoli, each suffering enormous stretch while plateau pressures measured at the airway opening appear controlled. **Atelectotrauma** is produced by repetitive collapse and re-expansion of unstable alveoli: each breath cycle requires breaking the surface tension of a collapsed alveolus, generating shear forces at the liquid-air interface that mechanically injure surfactant-depleted epithelium. This is why **PEEP** (positive end-expiratory pressure) is protective — by maintaining a baseline airway pressure that keeps recruited alveoli open at end-expiration, PEEP prevents the repetitive collapse-re-expansion cycle. **Biotrauma** is the systemic consequence: stretch-activated epithelial and endothelial cells release pro-inflammatory cytokines (IL-1β, IL-6, TNF-α) that enter the bloodstream and contribute to multi-organ dysfunction syndrome — connecting ventilator settings directly to distant organ failure.

Lung-protective ventilation emerged from the landmark ARDSNet trial published in 2000, which showed that tidal volumes of 6 mL/kg ideal body weight reduced ARDS mortality by 22% compared to 12 mL/kg — despite the low-tidal-volume group having higher CO₂ levels (permissive hypercapnia). The key insight was that maintaining "normal" CO₂ by using larger breaths costs more in volutrauma than the benefit is worth. The lung-protective bundle — low tidal volume, plateau pressure <30 cmH₂O, sufficient PEEP to prevent atelectotrauma — has become standard of care.

The therapeutic tension within this framework is that **optimal PEEP** is not a fixed number. Too little PEEP allows atelectotrauma by permitting repeated alveolar collapse. Too much PEEP overdistends already-open alveoli in adjacent regions, causing its own volutrauma and compromising cardiac output by increasing right ventricular afterload. Finding the optimal PEEP requires titrating to the individual patient's lung mechanics — using the pressure-volume curve inflection point, driving pressure (plateau pressure minus PEEP as a surrogate for strain), or emerging tools like electrical impedance tomography that can visualize regional ventilation distribution in real time. This is the frontier of individualized lung-protective care: moving from population-level protocols to patient-specific ventilator settings that balance recruitment against overdistension in each patient's unique lung architecture.
