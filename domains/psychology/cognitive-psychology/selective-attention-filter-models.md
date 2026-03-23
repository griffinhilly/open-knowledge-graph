---
id: selective-attention-filter-models
title: Selective Attention and Filter Models
domain: psychology
course: cognitive-psychology
prerequisites:
- id: cognitive-psychology-overview
  type: hard
- id: attention-selective
  type: soft
builds-toward:
- perceptual-organization-gestalt-principles
tags:
- attention
- perception
- filtering
- cognitive
stage: formal-systems
status: validated
---

# Selective Attention and Filter Models

## Core Idea
Selective attention determines which information we consciously process from the environment. Broadbent's filter theory proposes that attention acts as a bottleneck early in processing, while later theories suggest the bottleneck can occur at semantic levels depending on task demands.

## Questions

```yaml
- question: "A participant shadows (repeats aloud) one ear's audio stream while ignoring the other. Later they report hearing their name in the 'ignored' channel. Which model best explains this finding and how?"
  type: multiple-choice
  options:
    - "Broadbent's filter theory — the filter allows personally relevant signals to pass before semantic processing"
    - "Treisman's attenuation theory — the unattended channel is weakened but not blocked; high-threshold words like one's name break through"
    - "Late selection theory — all channels are fully blocked after the filter, but name recognition is innate"
    - "Broadbent's filter theory — physical channel properties (pitch of one's own name) allow it to bypass the filter"
  answer: 1
  explanation: "The cocktail party effect — noticing your name in the unattended channel — directly challenged Broadbent's early filter, which predicted complete pre-semantic blocking of unattended channels. Treisman's attenuation model handles it by proposing the unattended channel is attenuated (weakened) rather than blocked, and that words with high personal relevance have low thresholds for conscious access, allowing them to break through even attenuated signals."

- question: "A researcher designs a demanding visual search task (high perceptual load) and a simple target detection task (low perceptual load). According to the perceptual load hypothesis, in which condition should irrelevant distractors produce more interference?"
  type: multiple-choice
  options:
    - "High perceptual load — the demanding task forces processing of all stimuli including distractors"
    - "Low perceptual load — spare processing capacity spills over to process distractors, producing interference"
    - "Both equally — distractor interference is independent of task demands"
    - "High perceptual load — more cognitive resources mean more distractor processing"
  answer: 1
  explanation: "The perceptual load hypothesis proposes that when the attended task consumes most available perceptual capacity (high load), little capacity remains for distractors — selection is early. When the task is easy (low load), spare capacity automatically processes distractors — selection is late, and distractors interfere. This explains why simple tasks produce more distractor interference despite seeming less demanding."

- question: "Broadbent's original filter theory proposed that the unattended channel is processed to a semantic level but blocked from reaching consciousness."
  type: true-false
  answer: false
  explanation: "Broadbent proposed a pre-semantic bottleneck: the filter operates on physical features (location, pitch) *before* any semantic content is extracted, and the unattended channel is blocked entirely. It was Treisman's attenuation theory and later late-selection theories that introduced semantic processing of unattended material. If Broadbent were right, you could never notice your name in the ignored channel."

- question: "Under high perceptual load, distractors are less likely to interfere with the attended task than under low perceptual load."
  type: true-false
  answer: true
  explanation: "This is the central prediction of Lavie's perceptual load hypothesis. High load consumes available perceptual capacity, preventing distractors from being processed — producing early selection and low distractor interference. The counterintuitive implication is that making a task harder can reduce distraction, because there is no spare capacity to 'waste' on irrelevant information."

- question: "Why is the debate between early and late selection theories ultimately a debate about the relationship between perception and consciousness?"
  type: short-answer
  answer: "Early selection theories hold that meaning is extracted only from attended stimuli — unattended information is blocked before semantic processing occurs, so consciousness is tightly coupled to the filter's gate. Late selection theories hold that all stimuli are fully processed semantically before selection occurs — the filter determines what we respond to, not what we perceive. The two positions disagree about where unconscious perceptual registration ends and conscious awareness begins."
  explanation: "The filter's location is not merely a technical question about processing stages — it defines what 'attention' means. Early selection makes attention a perceptual gate that controls what gets recognized. Late selection makes it a post-perceptual gate that controls what gets acted on or consciously reported. This maps onto broader debates about whether perception can occur without awareness and how much of the world we unconsciously process at any moment."
```

## Explainer

The central puzzle of selective attention is that the brain receives far more sensory information than it can fully process — you are surrounded by dozens of sound sources, visual objects, and bodily sensations at any moment, yet experience a coherent, focused perceptual world. **Selective attention** is the mechanism that resolves this: it selects a subset of incoming information for full conscious processing while filtering or attenuating the rest. **Filter models** attempt to specify *where* in the processing hierarchy this selection happens, with major theoretical disagreements about whether filtering is early (before meaning is extracted) or late (after meaning is processed).

**Broadbent's Filter Theory** (1958), the founding model, was motivated by the **dichotic listening task**: participants wear headphones with different auditory streams in each ear and are asked to "shadow" (repeat aloud) one ear while ignoring the other. Broadbent proposed that the filter operates on physical features — channel identity, pitch, location — *before* semantic content is processed. Only the attended channel passes through the filter; the other is blocked at a pre-semantic bottleneck and never reaches the level of meaning. This early selection view is computationally elegant: filtering early reduces the processing load most efficiently. But it was immediately challenged by the **cocktail party effect**: people reliably notice their own name spoken in the supposedly unattended channel — a finding that requires the unattended channel to have been processed to at least the level of semantic identity.

**Treisman's Attenuation Theory** (1964) modified the model to handle this finding: rather than blocking the unattended channel completely, the filter *attenuates* it — reduces its signal strength without eliminating it. Words with high personal relevance (your name, words like "fire" or "danger") have low thresholds for conscious access, so they break through even attenuated. This preserves the efficiency of early filtering while accounting for the cocktail party effect. **Late selection theories** (Deutsch & Deutsch, Norman) went further: all inputs are processed to the semantic level automatically, and selection happens only at the stage of action or conscious response. On this view, the bottleneck is not perceptual but post-perceptual — the question is not what gets recognized but what gets *responded to*. Evidence from the implicit processing of unattended information (semantic priming from ignored words) supports this position.

The contemporary resolution is that the locus of selection is **flexible** rather than fixed. The **perceptual load hypothesis** (Lavie) proposes that when the attended task has high perceptual load — consuming most available perceptual processing capacity — selection happens early and distractors are not processed. When perceptual load is low, spare capacity spills over to process distractors, producing late selection. This explains discrepant findings across paradigms: studies using simple, low-load tasks find late selection (distractor interference); studies using demanding high-load tasks find early selection. The filter is not a fixed gate at one location but a dynamic allocation of resources that adapts to task demands.

The broader significance of filter models is that they forced cognitive psychology to grapple with the distinction between **automatic and controlled processing**, between what the brain does *to you* (automatic perceptual registration) and what you do *with your brain* (effortful selective allocation). Every filter theory is implicitly a theory about the architecture of consciousness: it locates where the transformation from unconscious registration to conscious experience occurs, and what determines which representations make the crossing. The debate between early and late selection, still not fully resolved, is at its core a debate about the relationship between perception and awareness — one of the deepest questions in cognitive science.
