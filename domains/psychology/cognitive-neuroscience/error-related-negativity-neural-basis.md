---
id: error-related-negativity-neural-basis
title: Error-Related Negativity and Error Processing
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: anterior-cingulate-cortex-conflict-monitoring
  type: hard
- id: erp-components-attention
  type: hard
builds-toward:
- error-awareness-consciousness
- error-driven-learning-plasticity
tags:
- ERN
- error-negativity
- error-monitoring
- ACC
- ERP
stage: advanced
status: draft
---

# Error-Related Negativity and Error Processing

## Core Idea
The error-related negativity (ERN), an ERP component peaking 50-100ms after error commission, reflects anterior cingulate activity signaling response conflict and error detection. The ERN predicts behavioral adjustment following errors and correlates with individual differences in error sensitivity and learning rate. Larger ERN amplitude is associated with better error-driven learning and self-monitoring capacity.

## Questions

```yaml
- question: "A researcher finds that the ERN peaks about 80ms after the participant's button press on error trials. A colleague proposes that the ERN simply reflects conscious error awareness. Which finding would most directly contradict that interpretation?"
  type: multiple-choice
  options:
    - "The ERN is larger in participants with higher IQ scores"
    - "The ERN appears even on trials where participants later report no awareness of making an error"
    - "The ERN amplitude correlates with post-error slowing on the next trial"
    - "The ERN is absent on correct trials"
  answer: 1
  explanation: "The ERN peaks 50-100ms after the response — often before conscious awareness can register. If it reflected conscious awareness, it could not appear on trials where awareness is absent. Finding ERN on unreported-error trials demonstrates the signal is generated preconsciously, consistent with ACC conflict monitoring rather than a conscious recognition process. Options C and D are consistent with both accounts; option A is a demographic correlation, not a test of the awareness hypothesis."

- question: "Participants with OCD show large ERN amplitudes even after correct responses. What does this suggest about ERN function?"
  type: multiple-choice
  options:
    - "Their motor systems are slower, so the ACC receives delayed feedback"
    - "OCD causes actual errors that go consciously unregistered"
    - "The monitoring system generating the ERN is over-triggered, flagging non-errors as errors"
    - "Larger ERN amplitude always reflects better learning and self-monitoring"
  answer: 2
  explanation: "The ERN reflects ACC conflict monitoring — a system that compares executed responses to intended ones and generates an error signal when they diverge. In OCD, this system appears hyperactive: it fires even when no error was made. This is directly diagnostic because it separates the neural monitoring process from actual error commission. Option D is wrong because in OCD the large ERN after correct responses reflects pathological over-monitoring, not superior learning — the system is misfiring, not performing better."

- question: "The ERN is stimulus-locked, meaning it is triggered by the sensory event that precedes the error."
  type: true-false
  answer: false
  explanation: "The ERN is response-locked, not stimulus-locked. It is time-locked to the moment the participant makes their response (the button press), peaking roughly 50-100ms afterward. This is what makes the ERN remarkable: unlike most ERP components that respond to external events, the ERN reflects the brain's internal evaluation of its own output. The response-locking is also why it can precede conscious error awareness — the ACC evaluates the motor output as it happens, not after perceiving a stimulus."

- question: "A larger ERN amplitude is associated with greater behavioral adjustment on the trial immediately following an error."
  type: true-false
  answer: true
  explanation: "This is a key finding establishing that the ERN is not merely a passive index but has functional significance. Larger ERN predicts more post-error slowing and sometimes greater post-error accuracy on the next trial. This link between neural signal strength and behavioral adjustment is what makes the ERN a window into error-driven learning — it shows the error detection signal directly influences subsequent control, rather than being an epiphenomenal byproduct."

- question: "Why is the ERN described as analogous to a negative prediction error, and what prerequisite concept does this connect to?"
  type: short-answer
  answer: "A negative prediction error occurs when actual outcome falls short of expected outcome — the brain registers a mismatch between what was predicted and what happened. The ERN reflects the ACC comparing the executed response to the internally computed correct response; when they diverge (an error was made), the ACC generates a signal analogous to 'this fell short of expectation.' This connects to reinforcement learning frameworks: just as dopamine systems compute reward prediction errors to update future behavior, the ERN computes performance prediction errors to trigger post-error adjustments. The ACC serves as the conflict monitor detecting this divergence."
  explanation: "The prediction error framing is theoretically important because it connects cognitive control to learning mechanisms. It implies the ERN is not just flagging a bad outcome but generating a teaching signal that can update future responses. This is why ERN amplitude predicts behavioral adjustment — the magnitude of the error signal determines the strength of the corrective impulse. The connection to ACC conflict monitoring (from prerequisites) explains the neural source: the ACC detects competing response activations and generates the error signal when the wrong one was executed."
```

## Explainer

From your study of ERP components, you know that event-related potentials are small voltage changes extracted from the EEG by averaging many trials time-locked to an event. Most ERP components you have studied (P300, N2) are locked to stimulus events — something in the environment triggers a brain response. The **error-related negativity (ERN)** is distinctive: it is locked to the participant's own response, not to a stimulus. Specifically, it is a negative deflection peaking roughly 50–100 milliseconds after the moment an error is committed — in many cases before the person is even consciously aware they made an error. This is remarkable: the brain signals a mistake faster than consciousness can register it.

The source of the ERN connects to your knowledge of the **anterior cingulate cortex (ACC)** as a conflict monitor. The ACC sits at the interface between cognitive control and motor systems, and it is particularly sensitive to situations where competing response tendencies are simultaneously active — for instance, when you are making a fast choice and partially activate an incorrect response before suppressing it. The ERN appears to reflect a comparison function: when the executed response and the internally computed "correct" response diverge, the ACC generates an error signal. This fits the reinforcement learning interpretation: the ERN resembles a **negative prediction error** — the brain's recognition that actual outcome fell short of intended outcome — analogous to what dopamine systems compute for rewards.

What makes the ERN scientifically valuable is its relationship to post-error behavior. After an error, people typically slow down on the next trial (**post-error slowing**) and sometimes improve accuracy (**post-error accuracy increase**). The amplitude of the ERN predicts the magnitude of this behavioral adjustment — larger ERN, more slowing, more correction. This is a direct link between a neural signature and adaptive behavior change. The ERN is also sensitive to individual differences: people high in trait anxiety and error concern show larger ERNs. People with OCD show abnormally large ERNs even after correct responses, consistent with the hypothesis that their monitoring system is over-triggered. People with low ERN amplitude following substance use or sleep deprivation show impaired error correction.

The ERN is thus a window into a specific neural computation: the brain's real-time assessment of its own performance. Unlike behavioral measures (response time, accuracy), which only tell you what happened, the ERN tells you how the brain responded to what happened — whether it flagged the error, how strongly, and whether that flag translated into adaptive adjustment. Understanding the ERN requires holding together three things from your prerequisites: the biophysics of EEG and how averaging isolates neural components, the conflict-monitoring function of the ACC, and the temporal precision that makes ERPs useful for studying processes that unfold in milliseconds.
