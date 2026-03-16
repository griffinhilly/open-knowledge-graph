---
id: transcranial-magnetic-stimulation
title: Transcranial Magnetic Stimulation and Brain Mapping
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: biological-psychology-overview
  type: hard
- id: motor-cortex
  type: soft
builds-toward:
- causal-inference-neuroscience
tags:
- neuroimaging
- methods
- stimulation
stage: advanced
status: draft
---

# Transcranial Magnetic Stimulation and Brain Mapping

## Core Idea
Transcranial magnetic stimulation (TMS) uses magnetic coils to induce electrical currents in specific cortical regions, temporarily disrupting or facilitating neural activity. Unlike passive imaging, TMS establishes causal relationships: if disrupting region X impairs behavior Y, X is necessary for Y. This allows functional mapping of brain regions and testing predictions from brain imaging studies about which regions are critical for cognition.

## Explainer

In biological psychology you learned that the brain mediates behavior through the coordinated activity of neural circuits, and that the motor cortex is the principal output station for voluntary movement. TMS enters this picture as a tool that lets researchers ask a precise question that passive observation cannot answer: not "is region X active when behavior Y occurs?" but "is region X *necessary* for behavior Y?" This is the logic of causal inference in neuroscience, and it is the fundamental innovation TMS provides.

The physical mechanism is Faraday's law of electromagnetic induction. A brief, strong pulse of current through a coil placed on the scalp generates a rapidly changing magnetic field that passes through the skull (magnetic fields are not blocked by biological tissue the way electrical currents are). This changing magnetic field induces an electrical current in the cortical neurons beneath the coil, which can depolarize those neurons and disrupt their normal activity — or, at subthreshold intensities, can facilitate processing. A single TMS pulse delivered during a cognitive task can act as a **virtual lesion**: temporarily disrupting processing in the targeted region for roughly 100 milliseconds while leaving the rest of the brain intact. If performance on the task degrades with TMS over region X but not over a control site, you have causal evidence that region X contributes to that task.

The **motor cortex** plays a special role in TMS methodology. Because M1 stimulation produces measurable **motor evoked potentials (MEPs)** — detectable twitches in the contralateral hand muscles that can be recorded with surface electrodes — it serves as the calibration target for establishing individual TMS parameters. The stimulation intensity needed to produce a reliable hand twitch in 50% of trials defines the **motor threshold** and is used as a standardized reference for dosing TMS across other brain regions. This is why almost every TMS study begins with a motor cortex localization procedure.

**Repetitive TMS (rTMS)** extends the approach beyond single-pulse disruption. High-frequency rTMS (>5 Hz) tends to facilitate cortical excitability; low-frequency rTMS (≤1 Hz) tends to suppress it — and these effects can outlast the stimulation period by minutes to an hour. This lasting effect is the basis for rTMS as a **clinical treatment**: the FDA has approved rTMS of the left dorsolateral prefrontal cortex for major depression, where the protocol aims to increase activity in a region implicated in mood regulation and cognitive control. The therapeutic mechanism is not fully understood, but the approach leverages TMS's ability to induce durable changes in cortical excitability. TMS thus bridges basic neuroscience (causal brain mapping) and clinical application (non-invasive neuromodulation), making it one of the most versatile tools in cognitive neuroscience.
