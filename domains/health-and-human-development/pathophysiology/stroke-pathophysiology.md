---
id: stroke-pathophysiology
title: Ischemic and Hemorrhagic Stroke
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: cerebral-circulation-and-autoregulation
  type: hard
- id: thrombosis-pathophysiology
  type: hard
- id: necrosis-vs-apoptosis
  type: soft
builds-toward:
- stroke-recovery-and-neuroplasticity
- post-stroke-complications
tags:
- stroke
- cerebral-ischemia
- hemorrhage
stage: advanced
status: validated
---

# Ischemic and Hemorrhagic Stroke

## Core Idea
Ischemic stroke results from arterial occlusion causing focal cerebral ischemia with a penumbra of hypoxic but viable tissue (therapeutic window for thrombolysis). Hemorrhagic stroke causes mass effect, increased ICP, and secondary ischemia. Both trigger inflammatory cascades, excitotoxicity, and neuronal death.

## How It's Best Learned
Understand the ischemic cascade: loss of ATP → loss of ion homeostasis → calcium influx → protease activation and ROS. Study acute imaging (CT for hemorrhage, MRI DWI for ischemia) and time-based intervention thresholds.

## Common Misconceptions
MRI DWI hyperintensity appears within minutes of ischemia, not hours—timing is crucial for intervention eligibility. Hemorrhagic transformation can occur after thrombolysis in large infarcts; this is a known risk, not a contraindication.

## Questions

```yaml
- question: "A 68-year-old with atrial fibrillation presents with sudden right-sided weakness and aphasia. CT scan shows no hemorrhage. Which intervention is most appropriate within 4.5 hours of symptom onset?"
  type: multiple-choice
  options:
    - "Administer IV tPA to dissolve the likely cardioembolic thrombus"
    - "Administer IV heparin to prevent further clot extension"
    - "Withhold treatment until MRI DWI confirms ischemia — CT alone is insufficient for diagnosis"
    - "Administer reversal agents for anticoagulation to prevent hemorrhagic transformation"
  answer: 0
  explanation: "This presentation is classic cardioembolic ischemic stroke (atrial fibrillation is the most common cardiac source). CT serves its purpose by excluding hemorrhage — tPA can then be administered. Waiting for MRI is not indicated in the acute window; CT negative for hemorrhage is sufficient to proceed. Heparin is not the acute thrombolytic agent. Reversal agents are for hemorrhagic stroke, which the CT has ruled out."

- question: "Why does 'time is brain' have a precise biological basis in ischemic stroke?"
  type: multiple-choice
  options:
    - "Brain cells die instantly at occlusion, so every second of delay adds irreversible infarct"
    - "The penumbra — hypoperfused but still viable tissue surrounding the ischemic core — converts to irreversible infarct at approximately 1.9 million neurons per minute without restored perfusion"
    - "Edema forms progressively and compresses healthy tissue, causing secondary death within the first hour"
    - "Thrombus extension occurs rapidly, enlarging the occluded territory within minutes of onset"
  answer: 1
  explanation: "The penumbra is the key concept. The ischemic core (directly deprived of perfusion) dies quickly, but surrounding tissue with some collateral flow — the penumbra — remains viable for a time-limited window. It is not dead yet but is dying. The penumbra converts to core at ~1.9 million neurons per minute if perfusion is not restored. Thrombolysis and thrombectomy are attempts to rescue this tissue before that window closes."

- question: "The distinction between hemorrhagic and ischemic stroke cannot be reliably made on clinical presentation alone — brain imaging is mandatory before any treatment decision."
  type: true-false
  answer: true
  explanation: "Both stroke types can present with sudden focal neurological deficits and are clinically indistinguishable in many cases. Hemorrhagic stroke must be excluded by CT before administering tPA, because tPA given to a hemorrhagic stroke could be catastrophic. The treatments are mechanistically opposite: restore perfusion for ischemic stroke, control the bleed and manage ICP for hemorrhagic stroke."

- question: "In hemorrhagic stroke, neuronal injury is confined to the immediate vicinity of the bleed, with no ischemia occurring in distant brain regions."
  type: true-false
  answer: false
  explanation: "Hemorrhagic stroke causes mass effect: the hematoma raises intracranial pressure, which reduces cerebral perfusion pressure globally and can shift brain structures (herniation). This creates secondary ischemia in tissue distant from the hematoma. Additionally, blood products trigger inflammatory cascades that compound injury over days, extending the zone of damage well beyond the bleed itself."

- question: "Explain the therapeutic significance of the ischemic penumbra — what it is, why it exists, and why its existence justifies the urgency of stroke treatment."
  type: short-answer
  answer: "The penumbra is tissue surrounding the ischemic core that receives reduced but not zero perfusion — metabolically stressed but still viable. It exists because arterial occlusion creates a perfusion gradient: the core supplied only by the blocked vessel dies quickly, while surrounding tissue supplied by collateral vessels retains some flow. This viable tissue is the therapeutic target: restoring perfusion through tPA or mechanical thrombectomy can rescue it. Without treatment, the penumbra converts to infarct at ~1.9 million neurons per minute — the biological basis for the narrow treatment window and the maxim 'time is brain.'"
  explanation: "The penumbra concept transforms stroke from a single catastrophic event into a race against time. Treatment isn't simply useful — it has a mechanistic basis for why earlier intervention saves more neurons. The shrinking penumbra also explains why thrombectomy eligibility (up to 24h) requires imaging confirmation of salvageable tissue: if the penumbra has already converted to core, intervention no longer helps."
```

## Explainer

From your study of cerebral circulation, you know that the brain is metabolically exceptional: it constitutes 2% of body weight but consumes 20% of cardiac output and has essentially no energy reserves. Cerebral autoregulation normally maintains constant blood flow across a wide range of perfusion pressures. Stroke is what happens when that flow is interrupted — either because a vessel is blocked (**ischemic stroke**, ~87% of cases) or because one ruptures (**hemorrhagic stroke**, ~13%). The mechanisms, imaging findings, and treatment windows differ sharply between them.

In **ischemic stroke**, a thrombus (arising from atherosclerotic plaque) or embolus (typically from cardiac sources like atrial fibrillation, the mechanism you know from thrombosis pathophysiology) occludes a cerebral artery. Downstream tissue is deprived of both oxygen and glucose. The ischemic injury is not homogeneous: the core — directly supplied by the occluded vessel — loses perfusion almost immediately and undergoes rapid irreversible necrosis. Surrounding it is the **penumbra**: tissue with reduced but not zero perfusion, metabolically stressed but still viable for a window of time. The penumbra is the therapeutic target. ATP depletion causes failure of the Na⁺/K⁺-ATPase, ions flow down their gradients, intracellular sodium and calcium accumulate, and neurons depolarize abnormally. **Excitotoxicity** follows: excessive glutamate release activates NMDA receptors, allowing massive calcium influx that activates proteases, lipases, and endonucleases — the same cascade you studied in necrosis pathways. The penumbra converts to core at a rate of roughly 1.9 million neurons per minute if perfusion is not restored. This is the biological basis for the maxim "time is brain."

The therapeutic implication is a race against the penumbra's shrinkage. Intravenous **thrombolysis** (tPA) within 4.5 hours can dissolve the clot and restore flow to viable penumbral tissue. **Mechanical thrombectomy** (physically retrieving the clot) extends the window to 24 hours in selected patients with imaging-confirmed salvageable penumbra. CT is done first because it rapidly excludes hemorrhage — tPA given to a hemorrhagic stroke would be catastrophic. MRI diffusion-weighted imaging (DWI) shows ischemic core within minutes because restricted water diffusion in cytotoxically swollen cells appears bright before structural necrosis is visible on conventional imaging.

**Hemorrhagic stroke** operates by an entirely different mechanism. Rupture of a vessel — from hypertensive arteriolar damage, an aneurysm, or an arteriovenous malformation — floods the parenchyma or subarachnoid space with blood. The hematoma exerts **mass effect**: it compresses surrounding tissue, raises intracranial pressure, and can shift the brain across the midline (herniation). Elevated ICP also secondarily reduces cerebral perfusion pressure, creating ischemia around the bleed — hence "secondary ischemia" in hemorrhagic stroke. The inflammatory response to blood products then compounds injury over the following days. Treatment is the reverse of ischemic stroke: instead of restoring flow, the goal is hematoma control, ICP management, and reversal of any anticoagulation that may have precipitated the bleed. The distinction between hemorrhagic and ischemic stroke cannot be made clinically — imaging is mandatory before any treatment decision, because a drug that saves an ischemic stroke patient can kill a hemorrhagic one.
