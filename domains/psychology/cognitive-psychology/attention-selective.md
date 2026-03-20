---
id: attention-selective
title: Selective Attention
domain: psychology
course: cognitive-psychology
prerequisites:
- id: cognitive-psychology-overview
  type: hard
- id: sensory-pathways-overview
  type: soft
builds-toward:
- attention-divided
- cognitive-load-theory
- cognitive-biases-overview
tags:
- attention
- perception
- filter-theory
stage: advanced
status: validated
---

# Selective Attention

## Core Idea
Selective attention is the cognitive process by which the mind focuses on a subset of available sensory information while suppressing the rest. Early filter models (Broadbent) proposed selection occurs before perceptual analysis; late-selection models proposed it occurs after meaning is extracted. Research using dichotic listening, visual search tasks, and the attentional blink has revealed that selection is flexible and depends on task demands, prior knowledge, and stimulus salience.

## How It's Best Learned
Experience the Stroop task and cocktail party effect firsthand, then map these phenomena onto filter model predictions. Contrasting early versus late selection models sharpens understanding of where in processing the bottleneck occurs.

## Common Misconceptions
- Paying attention is not a single unitary resource — different attentional systems handle spatial, feature-based, and object-based selection.
- Unattended stimuli are not completely blocked; some semantic processing occurs even for ignored channels.

## Questions

```yaml
- question: "According to Broadbent's early selection (filter) model, what happens to unattended sensory information?"
  type: multiple-choice
  options: ["It is fully processed for meaning before being filtered out", "It is filtered out before perceptual analysis, based on physical characteristics like pitch or location", "It competes with attended information at the level of conscious awareness", "It is stored in long-term memory for possible later retrieval"]
  answer: 1
  explanation: "Broadbent proposed a bottleneck that operates on physical features (e.g., ear of entry, pitch) before the signal is analyzed for meaning. This contrasts with late-selection models, which allow semantic processing of all stimuli before selection."

- question: "Unattended stimuli in the ignored channel of a dichotic listening task receive no semantic processing whatsoever."
  type: true-false
  answer: false
  explanation: "Research by Moray (1959) showed that personally relevant words like one's own name can break through from an unattended channel, indicating some degree of semantic analysis occurs even for ignored information. This finding challenged strict early-selection accounts."

- question: "What does the 'cocktail party effect' reveal about selective attention that early filter models struggle to explain?"
  type: short-answer
  answer: "Meaningful stimuli — especially one's own name — can capture attention from an unattended channel, implying that unattended information receives at least some semantic processing before being filtered. Early selection models predict that unattended channels are blocked before meaning is extracted, so they cannot easily account for this name-detection effect."
  explanation: "The cocktail party effect demonstrates that selection is not purely based on low-level physical features. The significance of a stimulus (like your own name) must be recognized before attention can be redirected to it — which requires some semantic processing of nominally unattended input."
```

## Explainer

Imagine you are in a noisy room with many conversations happening at once. You focus on the person in front of you, yet somehow you still hear your name spoken across the room. This everyday experience — the cocktail party effect — sits at the heart of selective attention research, and explaining it has driven decades of theoretical debate.

The central problem is that the brain receives far more sensory information than it can fully process at any moment. Selective attention is the mechanism by which cognition prioritizes some signals and suppresses others. But *where* in the processing chain does this selection happen? Broadbent's early filter model (1958) proposed a bottleneck just after sensory registration: unattended stimuli are blocked based on simple physical properties (which ear the message arrived in, the pitch of the voice) before any analysis of meaning occurs. This is computationally efficient — you do not waste processing resources on irrelevant signals.

The problem is the cocktail party effect. If unattended channels are blocked before meaning is extracted, how does your name — a *semantic* property — ever reach consciousness? Treisman (1960) proposed a modified model: rather than a complete filter, unattended channels are *attenuated* (turned down, not off), and stimuli with high personal relevance have lower thresholds for breaking through. Deutsch and Deutsch pushed further, arguing that selection happens late, after meaning is fully extracted from all inputs, with the conscious bottleneck occurring at the stage of response selection rather than perception.

The resolution is that attention is not a single, fixed-location switch. Different attentional systems — spatial attention, feature-based attention, object-based attention — operate with some independence, and the "location" of the bottleneck shifts depending on task demands. High perceptual load in the attended task leaves little capacity for unattended processing; low perceptual load allows more seepage from unattended channels. This load theory (Lavie) reconciles early and late selection views by treating them as endpoints on a continuum.

What you should carry forward: unattended information is not simply deleted. It is processed — at least partially — and can influence behavior and awareness, particularly when it is personally relevant or unusually salient. Attention is less a gate than a spotlight that can be redirected, and understanding what controls that redirection is essential to understanding cognition more broadly.
