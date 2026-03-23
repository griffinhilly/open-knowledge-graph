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
stage: expert
status: validated
---

# ERP Components and Cognitive Processes

## Core Idea
ERP components provide markers of cognitive processes: P1 reflects sensory gain, N1 indexes attention filtering, N2 indicates conflict detection, P3 marks stimulus evaluation and updating, and N400 indexes semantic surprise. Different components have distinct scalp distributions and are independent variables—attention can enhance P1 without changing N1. Understanding ERP components reveals the timing and neural mechanisms of perception, attention, and decision-making at millisecond resolution, complementing fMRI's spatial specificity.

## Questions

```yaml
- question: "A drug selectively reduces P3 amplitude in a cognitive task while leaving N400 amplitude unchanged. What can you infer?"
  type: multiple-choice
  options:
    - "The drug impairs overall cognitive processing, since P3 and N400 reflect the same general attention resource"
    - "The drug specifically impairs context updating (P3 function) while leaving semantic integration (N400 function) intact"
    - "The drug affects early sensory processing, because both P3 and N400 reflect perceptual gating"
    - "No inference is possible because ERP components are too variable to support single-component interpretations"
  answer: 1
  explanation: "This is dissociation logic in action. The P3 reflects context updating — revising an internal model of the task situation when a significant event occurs. The N400 reflects semantic integration — how easily a word fits its context. Because the two components are independently modulated, a manipulation that selectively reduces P3 without touching N400 specifically impairs the context-updating stage while leaving semantic processing intact. This precision of inference is exactly what makes ERPs valuable beyond behavioral measures."

- question: "In a spatial attention experiment, attended stimuli show enhanced P1 amplitude (80–130 ms) compared to unattended stimuli. What does this demonstrate about attention?"
  type: multiple-choice
  options:
    - "Attention operates after the stimulus has been fully identified, selecting relevant items from a complete perceptual representation"
    - "Attention modulates sensory gain in early visual cortex before detailed stimulus analysis — amplifying the signal at attended locations from the very start of processing"
    - "The P1 enhancement reflects conscious awareness of the stimulus, not attention per se"
    - "Attention can only modulate processing after 200 ms, so P1 enhancement must reflect baseline differences between conditions"
  answer: 1
  explanation: "The P1 peaks at 80–130 ms over occipital scalp — too early for detailed object identification. Its enhancement by spatial attention demonstrates that the brain amplifies sensory signals at attended locations before it 'knows' what the stimulus is. This is sensory gain modulation: attention acts like a spotlight that brightens input from attended regions in early visual cortex. Option A describes a 'late selection' theory that the P1 evidence contradicts. Option C is wrong because subjects can show P1 enhancement without conscious awareness of stimuli."

- question: "Attention can independently modulate P1 amplitude without changing N1 amplitude, demonstrating that early sensory gain and attentional filtering are separable processing stages."
  type: true-false
  answer: true
  explanation: "This is one of the key empirical demonstrations of dissociation in ERP research. P1 (80–130 ms) reflects sensory gain modulation at attended locations; N1 (150–200 ms) reflects discrimination and filtering of stimuli at those locations. Experimental manipulations can selectively enhance P1 without changing N1 (or vice versa), which proves these are not a single 'attention effect' but genuinely distinct stages. If they were the same process, you could not modulate one without the other."

- question: "The N400 component is larger (more negative) for words that are semantically congruent with their preceding context than for incongruent words."
  type: true-false
  answer: false
  explanation: "This is backwards — and it is a very common confusion. The N400 is LARGER (more negative amplitude) for semantically INCONGRUENT or unexpected words (e.g., 'I take my coffee with cream and dog'). The N400 indexes the difficulty of integrating each word into the ongoing meaning representation: congruent words are easy to integrate (small N400), while incongruent words are costly to integrate (large N400). Larger N400 = harder semantic integration = more surprising word."

- question: "Why do cognitive neuroscientists often use ERP recordings alongside fMRI rather than relying on either method alone?"
  type: short-answer
  answer: "ERPs provide millisecond temporal resolution that reveals the timing and sequence of processing stages (e.g., P1 at 80 ms vs. N1 at 150 ms), but offer limited spatial resolution. fMRI provides precise localization of active brain regions but lacks the temporal resolution to separate processes occurring hundreds of milliseconds apart. Together, they provide complementary information: ERPs reveal *when* each processing stage occurs and whether stages can be dissociated; fMRI reveals *where* the activity is generated. Neither method alone tells the full story of neural computation."
  explanation: "The complementarity of ERPs and fMRI is a practical expression of a deeper principle: understanding cognition requires knowing both the spatial organization of processing (which brain regions are involved) and the temporal dynamics (in what order, and with what timing). ERP dissociations like P3-vs-N400 tell you that two processes can be selectively impaired; fMRI tells you where each process lives. When both methods converge on an answer, the evidence is much stronger than either alone."
```

## Explainer

From your study of EEG and ERP temporal dynamics, you know that an ERP is the average of many EEG epochs time-locked to the same event, and that the resulting waveform reflects the summed electrical activity of neuron populations as they process that event. The individual peaks and troughs in this waveform — the **components** — are the vocabulary of cognitive neuroscience. Each component is characterized by its polarity (positive or negative), its latency (when it peaks relative to the stimulus), and its scalp distribution (where the signal is largest, reflecting which cortical region is generating it). The key insight is that different components can be selectively modulated by different experimental manipulations, making them independent functional markers of distinct processing stages.

The earliest attention-sensitive component is the **P1**, a positive deflection peaking around 80–130 ms over occipital scalp regions. The P1 is enhanced when attention is directed to the spatial location of a stimulus compared to an unattended location — even before the subject has consciously processed what the stimulus was. This reflects **sensory gain modulation**: attended locations have their sensory signals amplified in early visual cortex, as if a spotlight is brightening the input before detailed analysis begins. The **N1**, peaking around 150–200 ms, indexes a different process — the discrimination and filtering of stimuli at attended locations. Attention can independently modulate P1 (early gain) without changing N1, or vice versa, demonstrating that these are genuinely separable processing stages rather than one global attention effect.

Moving later in the waveform, the **N2** (around 200–300 ms) reflects conflict detection and response inhibition, particularly over frontocentral sites. The N2 is larger when a stimulus requires suppression of a prepotent response (as in a go/no-go task) or when two potential responses compete. The **P3** (or P300), peaking 300–600 ms over centroparietal scalp, is one of the most studied ERP components: it is sensitive to the probability and task relevance of a stimulus. Rare, task-relevant targets elicit large P3 components; common or irrelevant stimuli do not. The P3 is interpreted as reflecting **context updating** — the revision of an internal representation of the current task situation when an unexpected or significant event occurs. Finally, the **N400** (around 400 ms) is uniquely sensitive to semantic processing: it is larger for words or images that are semantically incongruent with their context (e.g., "I take my coffee with cream and dog"), providing a real-time index of how easily each word is integrated into the ongoing meaning representation.

The power of ERP methodology lies in **dissociation logic** combined with millisecond temporal resolution. Because ERP and fMRI measure different aspects of neural activity, they are most informative together: fMRI shows you that the intraparietal sulcus is more active during attention tasks, while ERP shows you that this effect begins at 80 ms post-stimulus in the P1 and is separable from later attentional selection at 150 ms. Neither method alone tells the full story. When a drug, lesion, or developmental factor selectively reduces the P3 while leaving N400 intact, you can infer that the context-updating stage is impaired while semantic processing is preserved — a precision of interpretation that behavior alone cannot provide.

