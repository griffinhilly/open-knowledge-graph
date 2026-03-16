---
id: fmri-blood-oxygen-signaling
title: Functional MRI and BOLD Imaging
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: biological-psychology-overview
  type: hard
- id: brain-lobes-and-functions
  type: soft
- id: fourier-series-definition
  type: soft
builds-toward:
- neuroimaging-cognitive-mapping
- statistical-inference-neuroimaging
tags:
- neuroimaging
- methods
- bold
stage: advanced
status: draft
---

# Functional MRI and BOLD Imaging

## Core Idea
fMRI detects brain activity by measuring blood oxygen-level-dependent (BOLD) signals—blood oxygenation increases when neurons consume oxygen during task performance. This allows millisimeter-scale spatial mapping of which brain regions activate during perception, cognition, and action. While fMRI has excellent spatial resolution, its temporal resolution is limited to seconds, making it better suited for identifying where cognitive functions occur than when they occur.

## Explainer

You know from biological psychology that neurons are metabolically expensive: sustained firing consumes oxygen and glucose, and active brain regions require increased blood supply. **fMRI** exploits a peculiar fact about this blood flow: when a brain region becomes active, local blood flow increases *more* than the neurons actually consume — an oversupply that shifts the ratio of oxygenated to deoxygenated hemoglobin in local capillaries. **Oxyhemoglobin** (carrying oxygen) is diamagnetic — it barely perturbs a magnetic field. **Deoxyhemoglobin** is paramagnetic — it distorts the local magnetic field around blood vessels. An MRI scanner tuned to these field distortions can detect the shift in oxy-to-deoxy ratio. When neural activity increases, the flush of oxygenated blood pushes out deoxyhemoglobin, reducing field distortion and increasing the **BOLD signal** (blood oxygen-level-dependent). fMRI measures this proxy for neural activity, not neural activity directly.

The signal you are measuring is a vascular response, not a neural one — and vascular responses are slow. The **hemodynamic response function (HRF)** rises over 4–5 seconds after a neural event, peaks around 5–6 seconds, and returns to baseline over the following 10–15 seconds. If you have studied Fourier analysis, you can think of the HRF as a low-pass filter applied to the underlying neural signal: rapid, high-frequency neural events get smeared and blurred in time. A 50-millisecond neural response looks like a 15-second BOLD ripple. This is why fMRI's **temporal resolution** is measured in seconds — far slower than EEG (milliseconds) or single-unit recording — even though its **spatial resolution** (1–3 mm) is excellent for a non-invasive technique.

To isolate the BOLD signal for a specific cognitive process, you need a **contrast** between two conditions that differ only in the process of interest. In a **block design**, the brain alternates between 20-second blocks of task and rest, producing large, reliable BOLD differences but poor trial-level resolution. In an **event-related design**, brief individual trials are modeled separately, allowing comparison of different trial types but with lower statistical power per comparison. The BOLD signal is small (1–5% above baseline) and rides on top of noise from scanner drift, head motion, heartbeat, and respiration. Careful preprocessing — motion correction, spatial smoothing, temporal filtering — is essential. The multiple-comparisons problem across hundreds of thousands of voxels makes statistical thresholding critical; insufficient correction produces dramatic-looking but spurious activation maps, illustrated vividly by the "dead salmon study" in which uncorrected analysis appeared to show BOLD responses in a deceased fish.

fMRI tells you *where* — which brain regions are reliably more active during a condition — with spatial precision that no other non-invasive method matches. It is poorly suited to *when*, given the hemodynamic lag. More fundamentally, fMRI is **correlational**: a region that activates during a task is associated with it, but activation does not establish that the region is *necessary* for task performance. A region might activate as a downstream consequence of cognitive processing, or as part of a control network engaged by task difficulty, without contributing directly to the core computation. This is where TMS (which you will study next) complements fMRI: fMRI identifies candidate regions; TMS tests whether disrupting those regions impairs behavior — the causal test that correlation alone cannot provide.
