---
id: acid-base-homeostasis-physiology
title: Acid-Base Homeostasis Physiology
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: acid-base-chemistry
  type: hard
- id: fluid-balance-and-electrolytes
  type: hard
- id: oxygen-transport-and-hemoglobin
  type: hard
- id: buffer-chemistry-le-chatelier-application
  type: soft
- id: buffer-solutions
  type: hard
builds-toward:
- renal-regulation-acid-base
- respiratory-compensation-and-control
tags:
- pH
- buffer
- bicarbonate
- respiratory-compensation
stage: formal-systems
status: validated
---

# Acid-Base Homeostasis Physiology

## Core Idea
Blood pH is maintained near 7.4 through three mechanisms: the bicarbonate buffer system (H⁺ + HCO₃⁻ ↔ H₂CO₃ ↔ CO₂ + H₂O), respiratory compensation (CO₂ elimination), and renal compensation (bicarbonate reabsorption and acid secretion). Respiratory compensation occurs within minutes; renal compensation takes hours to days. Metabolic acidosis triggers hyperventilation to eliminate CO₂; metabolic alkalosis triggers hypoventilation to retain CO₂.

## Questions

```yaml
- question: "A patient with severe diabetic ketoacidosis has pH 7.2 and elevated plasma H⁺. Which compensatory change would you expect in their arterial blood gas?"
  type: multiple-choice
  options:
    - "Elevated pCO₂ — the lungs retain CO₂ to buffer excess acid"
    - "Reduced pCO₂ — hyperventilation blows off CO₂ to consume protons"
    - "Elevated HCO₃⁻ — the kidneys rapidly generate more bicarbonate within minutes"
    - "No change in pCO₂ — respiratory compensation only occurs in respiratory disorders"
  answer: 1
  explanation: "Metabolic acidosis triggers brainstem-mediated hyperventilation, which blows off CO₂. Because CO₂ + H₂O ↔ H₂CO₃ ↔ H⁺ + HCO₃⁻, removing CO₂ pulls the equilibrium left, consuming protons and raising pH. This respiratory compensation begins within minutes. Option A is wrong — retaining CO₂ would worsen acidosis. Option C is wrong because renal compensation takes hours to days, not minutes. Option D is wrong because respiratory compensation is the primary acute response to metabolic acid-base disorders."

- question: "What makes the bicarbonate buffer system more effective than a typical closed chemical buffer in blood?"
  type: multiple-choice
  options:
    - "Bicarbonate has a higher pKa, making it more effective near physiological pH"
    - "The body can independently manipulate both ends of the equilibrium — CO₂ via breathing and HCO₃⁻ via the kidneys"
    - "Bicarbonate is present in higher concentrations than any other buffer in plasma"
    - "It is the only buffer system that directly neutralizes strong acids without producing any byproducts"
  answer: 1
  explanation: "The key advantage is that the bicarbonate system is open: CO₂ is a volatile gas regulated by ventilation rate, and HCO₃⁻ is regulated by renal reabsorption and secretion. Controlling both sides independently gives the body far greater buffering range than a closed system. Options A and C are factually incorrect (bicarbonate's pKa of 6.1 is actually suboptimal for 7.4, yet the system is powerful precisely because it is open). Option D is wrong — the neutralization products include CO₂ and water."

- question: "Respiratory compensation for metabolic acidosis acts faster than renal compensation."
  type: true-false
  answer: true
  explanation: "Respiratory compensation via altered ventilation rate begins within minutes of a pH change, as the brainstem's chemoreceptors rapidly detect rising CO₂ and falling pH. Renal compensation — increasing H⁺ secretion and bicarbonate reabsorption — requires hours to days to achieve maximal effect. This difference in timescale is clinically important: in acute metabolic acidosis, the respiratory system acts first as a bridge while the slower but more complete renal correction catches up."

- question: "In metabolic acidosis, if respiratory compensation is working effectively, the patient's blood pH will return substantially to 7.4."
  type: true-false
  answer: false
  explanation: "Respiratory compensation can only partially offset a metabolic acid-base disorder — it never fully corrects it and never overshoots. If the pH were fully corrected to 7.4, the brainstem stimulus for hyperventilation would disappear and breathing would normalize, allowing pH to fall again. The compensation stabilizes at a new lower pCO₂ and a pH between 7.4 and the nadir of the disorder, buying time for the kidneys to achieve more complete correction. Full normalization requires renal compensation."

- question: "Why is it clinically significant that acid-base compensation never overshoots — i.e., why can't respiratory compensation cause alkalosis in a patient with metabolic acidosis?"
  type: short-answer
  answer: "Compensation is driven by the deviation from normal pH. As hyperventilation reduces CO₂ and pH rises toward 7.4, the brainstem stimulus diminishes, slowing ventilation. The system reaches a new equilibrium short of full correction. If compensation fully corrected pH to 7.4, the stimulus would vanish and the system would revert. This self-limiting negative feedback prevents compensation from becoming an independent primary disorder."
  explanation: "This is critical for clinical interpretation of arterial blood gases. If you see a patient with metabolic acidosis and an alkaline pH, that cannot be explained by compensation — it indicates a second, independent primary disorder (respiratory alkalosis) occurring simultaneously. Recognizing this prevents misattributing two simultaneous primary disorders to compensation, which would lead to treating only one cause."
```

## Explainer

From your study of buffer chemistry, you know that a buffer resists pH change by absorbing or releasing protons. In blood, the **bicarbonate buffer system** is the dominant buffer, working through the equilibrium: CO₂ + H₂O ↔ H₂CO₃ ↔ H⁺ + HCO₃⁻. What makes this system especially powerful is that it is an *open* buffer — the CO₂ side is controlled by breathing and the HCO₃⁻ side is controlled by the kidneys. This means the body can manipulate both ends of the equilibrium independently, giving it far more buffering capacity than a closed chemical system would have.

Think of blood pH as a tug-of-war between two regulators working on different timescales. When acid accumulates — say, from lactic acid buildup during intense exercise or diabetic ketoacidosis — the rising H⁺ concentration drives the equilibrium toward CO₂ production. The brainstem detects the pH drop and signals the diaphragm to breathe faster and deeper (**hyperventilation**), blowing off CO₂ and pulling the equilibrium back left, consuming protons. This respiratory compensation kicks in within minutes. If you've ever noticed yourself breathing hard after a sprint and then gradually normalizing, you're watching this system at work. The **respiratory compensation** cannot fully correct a metabolic acid-base disorder on its own — it can only partially offset the pH change while buying time for the kidneys.

The **renal compensation** is slower but more complete. The kidneys regulate bicarbonate by reabsorbing or excreting it in the proximal tubule, and they directly secrete H⁺ into the urine via the collecting duct. In metabolic acidosis, the kidneys increase H⁺ secretion and reclaim HCO₃⁻, producing more acidic urine and raising plasma HCO₃⁻. This process takes hours to days but achieves near-complete correction. From your work on fluid balance and electrolytes, recall that this renal regulation is tightly linked to sodium and potassium handling — H⁺ secretion is coupled to Na⁺ reabsorption, and acidosis can shift K⁺ out of cells as H⁺ moves in, causing hyperkalemia as a common companion to acidosis.

The key clinical concept is **primary disorder vs. compensation**: a metabolic acidosis (low HCO₃⁻, low pH) will trigger a respiratory compensation (low pCO₂ via hyperventilation), but the compensation never overshoots — you won't see low pH from metabolic acidosis *and* alkaline pH from the respiratory response at the same time. If a patient appears to have both disorders present, that indicates two *separate* primary disorders occurring simultaneously, not compensation. Learning to read an arterial blood gas — pH, pCO₂, and HCO₃⁻ together — is essentially learning to decode this three-way balancing act in real time.
