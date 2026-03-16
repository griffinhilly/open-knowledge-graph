---
id: erp-components-attention
title: ERP Components and Cognitive Processes
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: eeg-erp-temporal-dynamics
  type: hard
- id: visual-attention-mechanisms
  type: soft
tags:
- erp
- components
- cognition
stage: advanced
status: draft
---

# ERP Components and Cognitive Processes

## Core Idea
ERP components provide markers of cognitive processes: P1 reflects sensory gain, N1 indexes attention filtering, N2 indicates conflict detection, P3 marks stimulus evaluation and updating, and N400 indexes semantic surprise. Different components have distinct scalp distributions and are independent variables—attention can enhance P1 without changing N1. Understanding ERP components reveals the timing and neural mechanisms of perception, attention, and decision-making at millisecond resolution, complementing fMRI's spatial specificity.

## Explainer

From your study of EEG and ERP temporal dynamics, you know that an ERP is the average of many EEG epochs time-locked to the same event, and that the resulting waveform reflects the summed electrical activity of neuron populations as they process that event. The individual peaks and troughs in this waveform — the **components** — are the vocabulary of cognitive neuroscience. Each component is characterized by its polarity (positive or negative), its latency (when it peaks relative to the stimulus), and its scalp distribution (where the signal is largest, reflecting which cortical region is generating it). The key insight is that different components can be selectively modulated by different experimental manipulations, making them independent functional markers of distinct processing stages.

The earliest attention-sensitive component is the **P1**, a positive deflection peaking around 80–130 ms over occipital scalp regions. The P1 is enhanced when attention is directed to the spatial location of a stimulus compared to an unattended location — even before the subject has consciously processed what the stimulus was. This reflects **sensory gain modulation**: attended locations have their sensory signals amplified in early visual cortex, as if a spotlight is brightening the input before detailed analysis begins. The **N1**, peaking around 150–200 ms, indexes a different process — the discrimination and filtering of stimuli at attended locations. Attention can independently modulate P1 (early gain) without changing N1, or vice versa, demonstrating that these are genuinely separable processing stages rather than one global attention effect.

Moving later in the waveform, the **N2** (around 200–300 ms) reflects conflict detection and response inhibition, particularly over frontocentral sites. The N2 is larger when a stimulus requires suppression of a prepotent response (as in a go/no-go task) or when two potential responses compete. The **P3** (or P300), peaking 300–600 ms over centroparietal scalp, is one of the most studied ERP components: it is sensitive to the probability and task relevance of a stimulus. Rare, task-relevant targets elicit large P3 components; common or irrelevant stimuli do not. The P3 is interpreted as reflecting **context updating** — the revision of an internal representation of the current task situation when an unexpected or significant event occurs. Finally, the **N400** (around 400 ms) is uniquely sensitive to semantic processing: it is larger for words or images that are semantically incongruent with their context (e.g., "I take my coffee with cream and dog"), providing a real-time index of how easily each word is integrated into the ongoing meaning representation.

The power of ERP methodology lies in **dissociation logic** combined with millisecond temporal resolution. Because ERP and fMRI measure different aspects of neural activity, they are most informative together: fMRI shows you that the intraparietal sulcus is more active during attention tasks, while ERP shows you that this effect begins at 80 ms post-stimulus in the P1 and is separable from later attentional selection at 150 ms. Neither method alone tells the full story. When a drug, lesion, or developmental factor selectively reduces the P3 while leaving N400 intact, you can infer that the context-updating stage is impaired while semantic processing is preserved — a precision of interpretation that behavior alone cannot provide.

