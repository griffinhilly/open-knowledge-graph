---
id: tms-principles-and-causal-inference
title: 'Transcranial Magnetic Stimulation: Principles and Causal Methods'
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: neuroimaging-methods
  type: hard
- id: causal-inference-neuroscience
  type: hard
builds-toward:
- tms-motor-system-testing
- tms-speech-language-circuits
tags:
- TMS
- causal
- cortical-excitability
- virtual-lesion
- neuroplasticity
stage: advanced
status: draft
---

# Transcranial Magnetic Stimulation: Principles and Causal Methods

## Core Idea
Transcranial magnetic stimulation uses rapidly changing magnetic fields to induce electrical currents in brain tissue, temporarily disrupting local neural activity. Single-pulse TMS measures cortical excitability and can produce behavioral effects; repetitive TMS can induce lasting plasticity changes. Unlike correlational neuroimaging, TMS enables causal claims about brain-behavior relationships by directly manipulating neural activity.

## Explainer

You have studied neuroimaging methods — tools that reveal which brain regions are active during cognitive tasks. You have also studied causal inference in neuroscience, which means you understand the problem: correlation between brain activity and behavior does not establish that the region is *necessary* for that behavior. A region might activate as a downstream consequence, as part of a general engagement network, or simply because it receives input from the task-relevant circuit. Neuroimaging can tell you "this region lights up with that task." It cannot tell you "without this region, the task fails." **Transcranial Magnetic Stimulation (TMS)** addresses this gap by intervening directly on the brain rather than merely observing it.

A TMS device discharges a brief, intense electrical pulse through a coil of wire held against the scalp. By Faraday's law of electromagnetic induction, this rapidly changing current generates a **magnetic field** that penetrates the skull without attenuation — unlike electrical current, which is blocked by bone. In the cortical tissue directly beneath the coil (roughly 1–2 cm depth and lateral extent), this time-varying magnetic field induces secondary electrical currents sufficient to depolarize neurons. The effect is focal and transient. Delivered to motor cortex, a single TMS pulse produces a **motor-evoked potential (MEP)** — a visible muscle twitch detectable by surface EMG. The amplitude of the MEP is a direct readout of **cortical excitability** at that moment, enabling precise measurements of how excitability changes with tasks, drugs, learning, or disease state.

The critical experimental application is the **virtual lesion**: TMS pulses delivered to a brain region *during* a cognitive task transiently disrupt local processing. If the task becomes harder — reaction times lengthen, errors increase, a behavior fails to occur — you have demonstrated that the targeted region is *causally necessary* for that task at that moment. This is the TMS-to-fMRI pipeline: neuroimaging identifies candidate regions associated with a cognitive process → TMS disrupts each candidate → only the necessary regions produce behavioral deficits. Unlike lesion studies in patients, TMS lesions are reversible (lasting tens to hundreds of milliseconds with single pulses), precisely timed relative to the stimulus or response, and can be applied within-subject across conditions. This eliminates the confounds of patient lesion studies — variable lesion extent, chronic compensation, group differences between patients and controls.

**Repetitive TMS (rTMS)** extends the effect beyond the stimulation period itself by applying sustained pulse trains that modify cortical excitability for minutes to hours. High-frequency rTMS (typically >5 Hz) generally increases excitability; low-frequency (≤1 Hz) generally decreases it — effects analogous to LTP and LTD at the circuit level, though the synaptic mechanisms are not identical. **Theta-burst stimulation (TBS)** delivers bursts of high-frequency pulses in a theta-frequency envelope, producing reliable excitability changes in as little as 40 seconds of stimulation. rTMS over left dorsolateral prefrontal cortex is FDA-approved for treatment-resistant depression — a clinical application where the causal logic holds: increasing prefrontal excitability in a region hypoactive in depression produces sustained mood effects. Every TMS application, from basic research to clinical treatment, depends on the same insight: manipulating neural activity produces behavioral consequences, and that consequence is evidence for a causal relationship that passive observation can never establish.
