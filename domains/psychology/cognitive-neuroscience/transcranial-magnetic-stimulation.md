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
- id: fmri-principles-and-interpretation
  type: soft
builds-toward:
- causal-inference-neuroscience
tags:
- neuroimaging
- methods
- stimulation
stage: expert
status: validated
---
# Transcranial Magnetic Stimulation and Brain Mapping

## Core Idea
Transcranial magnetic stimulation (TMS) uses magnetic coils to induce electrical currents in specific cortical regions, temporarily disrupting or facilitating neural activity. Unlike passive imaging, TMS establishes causal relationships: if disrupting region X impairs behavior Y, X is necessary for Y. This allows functional mapping of brain regions and testing predictions from brain imaging studies about which regions are critical for cognition.

## Questions

```yaml
- question: "A researcher uses fMRI and finds the left angular gyrus consistently activates during mental arithmetic. A second researcher applies TMS to disrupt the left angular gyrus during arithmetic and observes significant performance impairment. Which finding supports a stronger claim about this brain region?"
  type: multiple-choice
  options:
    - "The fMRI finding, because correlational data across many trials is statistically more reliable than a single disruption study"
    - "The TMS finding, because disrupting the region impairs the behavior, establishing causal necessity rather than mere association"
    - "Both are equally strong — fMRI shows normal function, TMS shows what happens under damage"
    - "Neither — only studies of patients with permanent lesions can establish causal brain-behavior relationships"
  answer: 1
  explanation: "fMRI reveals correlation: the region activates during arithmetic, but that could reflect contribution, monitoring, or even suppression of the computation. TMS creates a virtual lesion — temporarily disabling region X impairs behavior Y — which establishes that X is causally necessary for Y. This is TMS's fundamental advantage over passive imaging. Patient lesion studies (option D) also establish causality, but lesions are rarely precise; TMS allows targeted disruption of specific regions in healthy participants."

- question: "Why is the motor cortex used as the calibration site for establishing individual TMS stimulation parameters?"
  type: multiple-choice
  options:
    - "The motor cortex is the largest cortical region and therefore the easiest coil target to localize"
    - "Motor cortex stimulation produces objectively measurable motor evoked potentials that define each individual's motor threshold"
    - "The motor cortex is less sensitive than other regions, providing a safe lower bound for stimulation intensity"
    - "Motor cortex stimulation has no cognitive effects, making it an ideal control condition for cognitive TMS studies"
  answer: 1
  explanation: "Stimulating M1 produces hand twitches detectable with surface electrodes as motor evoked potentials (MEPs). The motor threshold is the intensity that produces a reliable MEP in 50% of trials. This objective, individually measured readout provides a standardized reference for dosing TMS across participants and sessions before targeting cognitive regions. Without this calibration, stimulation intensity would be arbitrary."

- question: "TMS and fMRI both measure neural activity during cognitive tasks and differ primarily in temporal resolution."
  type: true-false
  answer: false
  explanation: "This is the core misconception. fMRI passively measures hemodynamic correlates of neural activity — telling you which regions activate while a task is performed, but not whether they are necessary. TMS actively disrupts neural processing, acting as a virtual lesion. The two methods answer fundamentally different questions: fMRI asks 'where is activity correlated with this task?'; TMS asks 'is this region causally necessary for this task?' They differ in inferential logic, not just temporal resolution."

- question: "High-frequency repetitive TMS (above 5 Hz) suppresses cortical excitability for a period that outlasts the stimulation itself."
  type: true-false
  answer: false
  explanation: "The relationship is reversed: high-frequency rTMS (>5 Hz) tends to *facilitate* (increase) cortical excitability, while low-frequency rTMS (≤1 Hz) suppresses it. Both effects can outlast stimulation by minutes to an hour. This asymmetry matters clinically — the FDA-approved depression protocol applies high-frequency rTMS to the left DLPFC to facilitate activity in an underactive mood-regulation region."

- question: "What does it mean for TMS to function as a 'virtual lesion,' and why is this a stronger inferential tool than correlational neuroimaging?"
  type: short-answer
  answer: "A virtual lesion refers to the temporary disruption of a specific brain region's normal processing during a task. If that disruption degrades task performance, it establishes that the region is causally necessary — not just associated with — that behavior. Correlational imaging can only show that a region is active during a task, which is consistent with many causal roles (or no causal role at all). The virtual lesion follows experimental logic: remove X, observe change in Y, conclude X causes Y. TMS achieves this in healthy participants with millisecond precision and without permanent damage."
  explanation: "The distinction is the difference between observation and intervention. Seeing a fire truck near a fire doesn't mean fire trucks cause fires — correlation doesn't imply causation. TMS removes the truck and asks whether the fire changes, enabling causal inference."
```

## Explainer

In biological psychology you learned that the brain mediates behavior through the coordinated activity of neural circuits, and that the motor cortex is the principal output station for voluntary movement. TMS enters this picture as a tool that lets researchers ask a precise question that passive observation cannot answer: not "is region X active when behavior Y occurs?" but "is region X *necessary* for behavior Y?" This is the logic of causal inference in neuroscience, and it is the fundamental innovation TMS provides.

The physical mechanism is Faraday's law of electromagnetic induction. A brief, strong pulse of current through a coil placed on the scalp generates a rapidly changing magnetic field that passes through the skull (magnetic fields are not blocked by biological tissue the way electrical currents are). This changing magnetic field induces an electrical current in the cortical neurons beneath the coil, which can depolarize those neurons and disrupt their normal activity — or, at subthreshold intensities, can facilitate processing. A single TMS pulse delivered during a cognitive task can act as a **virtual lesion**: temporarily disrupting processing in the targeted region for roughly 100 milliseconds while leaving the rest of the brain intact. If performance on the task degrades with TMS over region X but not over a control site, you have causal evidence that region X contributes to that task.

The **motor cortex** plays a special role in TMS methodology. Because M1 stimulation produces measurable **motor evoked potentials (MEPs)** — detectable twitches in the contralateral hand muscles that can be recorded with surface electrodes — it serves as the calibration target for establishing individual TMS parameters. The stimulation intensity needed to produce a reliable hand twitch in 50% of trials defines the **motor threshold** and is used as a standardized reference for dosing TMS across other brain regions. This is why almost every TMS study begins with a motor cortex localization procedure.

**Repetitive TMS (rTMS)** extends the approach beyond single-pulse disruption. High-frequency rTMS (>5 Hz) tends to facilitate cortical excitability; low-frequency rTMS (≤1 Hz) tends to suppress it — and these effects can outlast the stimulation period by minutes to an hour. This lasting effect is the basis for rTMS as a **clinical treatment**: the FDA has approved rTMS of the left dorsolateral prefrontal cortex for major depression, where the protocol aims to increase activity in a region implicated in mood regulation and cognitive control. The therapeutic mechanism is not fully understood, but the approach leverages TMS's ability to induce durable changes in cortical excitability. TMS thus bridges basic neuroscience (causal brain mapping) and clinical application (non-invasive neuromodulation), making it one of the most versatile tools in cognitive neuroscience.
