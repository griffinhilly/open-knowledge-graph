---
id: neuroimaging-methods-principles-and-applications
title: 'Neuroimaging Methods: Principles and Psychological Applications'
domain: psychology
course: biological-psychology
prerequisites:
- id: biological-psychology-overview
  type: soft
- id: brain-structure-and-functional-localization
  type: soft
- id: linear-algebra
  type: soft
- id: statistics
  type: soft
builds-toward:
- fmri-principles-and-interpretation
- eeg-erp-temporal-dynamics
tags:
- neuroimaging
- fMRI
- PET
- EEG
- MEG
- methods
stage: advanced
status: draft
---

# Neuroimaging Methods: Principles and Psychological Applications

## Core Idea
Neuroimaging comprises diverse techniques capturing brain structure (MRI), blood flow and metabolism (fMRI, PET), electrical activity (EEG, MEG), or chemistry. Each has distinct temporal and spatial resolution trade-offs: fMRI offers high spatial resolution but seconds of temporal lag; EEG provides millisecond resolution but poor localization. Interpreting neuroimaging requires understanding that correlation with cognition does not prove functional necessity—lesion studies and causal manipulations (transcranial magnetic stimulation) provide stronger evidence.

## Questions

```yaml
- question: "A researcher wants to determine exactly *when* during a visual search task the brain distinguishes a target from a distractor — an event lasting roughly 50 milliseconds. Which method is most appropriate?"
  type: multiple-choice
  options:
    - "fMRI, because it provides millimeter-level spatial resolution identifying the exact region"
    - "PET, because it can track metabolic changes associated with selective attention"
    - "EEG or MEG, because they provide millisecond temporal resolution sufficient to capture the rapid neural event"
    - "Structural MRI, to identify which regions are anatomically connected to visual cortex"
  answer: 2
  explanation: "The BOLD signal in fMRI peaks 5–6 seconds after neural activity — far too slow to resolve a 50-millisecond event. PET is even slower (minutes per scan). EEG and MEG record electrical and magnetic signals from neurons in real time, with millisecond resolution, making them the only viable choices for capturing fast cognitive events. The tradeoff is poor spatial localization for EEG (signals smear through the skull). MEG improves somewhat on localization. Choosing a method always requires matching the method's resolution profile to the research question."

- question: "An fMRI study shows the amygdala is consistently more active during fear conditioning trials than during neutral trials. A student concludes the amygdala is necessary for fear conditioning. What is the strongest objection?"
  type: multiple-choice
  options:
    - "fMRI measures blood flow, which is not related to neural activity and cannot support conclusions about cognition"
    - "The amygdala is too deep in the brain for reliable fMRI signal detection"
    - "fMRI establishes correlation between amygdala activity and the task — only lesion studies or TMS can establish that the amygdala is necessary for the function"
    - "Fear conditioning doesn't produce BOLD signals because it does not require conscious attention"
  answer: 2
  explanation: "fMRI measures the BOLD signal — a real proxy for neural activity via hemodynamics — so option A is wrong. The amygdala is detectable with fMRI. The correct objection is that correlation is not causation: the amygdala may be active because it is genuinely necessary, or it may be a downstream effect, or it may co-occur while an adjacent region does the causal work. Establishing necessity requires either observing that patients with amygdala damage lose fear conditioning (lesion study) or disrupting the amygdala with TMS in healthy subjects and observing impairment."

- question: "The BOLD signal in fMRI measures neural electrical activity directly, with a temporal resolution matching the millisecond timescale of neural firing."
  type: true-false
  answer: false
  explanation: "fMRI measures the hemodynamic response — changes in the ratio of oxygenated to deoxygenated hemoglobin in nearby blood vessels. Neurons that fire increase local blood flow over the following seconds, and this vascular response is what fMRI detects. The BOLD signal peaks roughly 5–6 seconds after neural activity, creating a fundamental temporal lag. It does not measure electrical activity at all — EEG and MEG measure electrical and magnetic signals respectively, which do track neural firing on the millisecond timescale."

- question: "To establish that a brain region is causally necessary for a cognitive function (not just correlated with it), researchers can use TMS to temporarily disrupt the region in healthy subjects and observe whether performance is impaired."
  type: true-false
  answer: true
  explanation: "TMS (Transcranial Magnetic Stimulation) delivers a focused magnetic pulse that temporarily disrupts neural activity in a targeted cortical region. If disrupting the region impairs task performance in healthy subjects, this establishes causal necessity — the region must be doing something essential to the task. This is fundamentally stronger than fMRI correlation, which only shows the region is active during the task. TMS complements lesion studies (which also establish necessity but involve patients with brain damage and lack experimental control)."

- question: "Why can't neuroimaging alone establish that a brain region is causally necessary for a cognitive function, even when activation is highly consistent across participants and studies?"
  type: short-answer
  answer: "Neuroimaging measures co-occurrence: a region active during a task might be genuinely causal, might be a downstream effect of causal regions, or might co-activate due to network connectivity without contributing causally. Consistent activation across studies still only shows the region is reliably involved, not that it is necessary. Necessity requires showing that removing or disrupting the region impairs function. Lesion patients with damage to the region who lack the function provide natural experiments; TMS, which temporarily disrupts a region in healthy participants, provides controlled causal tests. Without some form of manipulation or damage, correlation between activation and task performance cannot distinguish cause from accompaniment."
  explanation: "This is the foundational interpretive caution for all neuroimaging research. The field spent decades building activation maps, only to realize that activation is easy to find but necessity is hard to prove. The most rigorous conclusions combine converging evidence: fMRI for localization, TMS for causal disruption, lesion studies for double-dissociation, and ideally single-unit recording for mechanism. Any single method leaves interpretive gaps."
```

## Explainer

Neuroimaging is essentially a set of different "windows" into the brain, each with different glass. From your prerequisite knowledge of brain structure and functional localization, you know that different regions handle different tasks — but how do researchers actually know which region is active during which task? That's what neuroimaging answers. The core insight is that no single method is perfect; each trades off **spatial resolution** (how precisely you can locate activity) against **temporal resolution** (how quickly you can detect changes).

**fMRI** (functional Magnetic Resonance Imaging) exploits the **BOLD signal** — Blood Oxygenation Level Dependent — detecting changes in oxygenated versus deoxygenated hemoglobin. When neurons fire, local blood flow increases over the next few seconds, causing a detectable shift in the MRI signal. The payoff is excellent spatial resolution (~1–3 mm), letting you pinpoint which cortical region is active. The cost is temporal: the hemodynamic response peaks 5–6 seconds after neural activity, so fMRI cannot resolve fast cognitive events. Think of it as a photograph with sharp detail but a slow shutter speed. **EEG** (Electroencephalography) records electrical potentials at the scalp generated by synchronized postsynaptic activity across thousands of neurons. Its strength is millisecond temporal resolution — you can see brain responses unfold in real time during a single cognitive event. Its weakness is poor spatial resolution: electrical signals smear across the scalp through the skull and skin, making source localization mathematically ill-posed. **MEG** (Magnetoencephalography) records magnetic fields instead, which are less distorted by the skull and offer somewhat better localization than EEG while maintaining millisecond resolution.

**PET** (Positron Emission Tomography) uses radioactive tracers to measure blood flow or metabolism. It was the forerunner of fMRI for localizing function but has even worse temporal resolution (minutes per scan) and involves radiation exposure, limiting repeat measures. PET remains valuable for specific questions — measuring receptor density or neurotransmitter synthesis — that fMRI cannot address. The choice of method is never arbitrary; it follows from the research question. If you want to know *where* an effect is, use fMRI. If you want to know *when* it unfolds, use EEG or MEG. If you want to know which receptor system is involved, use PET.

The most important interpretive caution — connecting to your statistics prerequisite — is that neuroimaging establishes **correlation**, not causation. A region that activates during a task might merely co-occur with the real cause. True causal evidence requires either lesion studies (patients with damaged tissue who lose the function) or **TMS** (Transcranial Magnetic Stimulation), which temporarily disrupts a region in healthy subjects, establishing that the region is *necessary* for the function, not merely coincidentally active. Knowing when to trust localization findings and when to demand causal evidence is what separates sophisticated consumers of neuroimaging research from naive ones.
