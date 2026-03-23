---
id: attentional-blink-temporal-refractory
title: Attentional Blink and Temporal Attention Limits
domain: psychology
course: cognitive-psychology
prerequisites:
- id: attention-selective
  type: hard
- id: working-memory-model
  type: soft
builds-toward:
- attention-networks-brain
tags:
- attention
- temporal-dynamics
- perception
stage: formal-systems
status: validated
---

# Attentional Blink and Temporal Attention Limits

## Core Idea
When two targets appear in rapid succession (within 200-500ms), people often fail to detect the second target despite directing attention to it. This temporal refractory period reflects a fundamental limit in attentional capacity—the attentional system requires time to disengage from one target and engage with the next. The attentional blink demonstrates that attention operates under strict temporal constraints and cannot flexibly shift between rapid events.

## How It's Best Learned
Demonstrate with dual-target RSVP (rapid serial visual presentation) experiments where participants try to identify two targets in a stream of letters at different temporal lags. Computing the blink curve (% correct detection as a function of lag between targets) makes the effect concrete.

## Common Misconceptions
- Assuming that if you're 'paying attention,' you'll always notice everything; the blink shows attention itself creates blindness.
- Confusing attentional blink with simple decay—the effect is specific to close temporal proximity, not general memory loss.

## Questions

```yaml
- question: "In an RSVP experiment, T2 appears immediately after T1 in the very next position (lag-1). What typically happens to T2 detection?"
  type: multiple-choice
  options:
    - "T2 is strongly missed — the attentional system is fully occupied processing T1"
    - "T2 is often successfully detected despite the minimal interval between targets"
    - "T2 is detected only if the participant was pre-warned to expect two consecutive targets"
    - "T2 reaches the visual system but cannot be consciously reported"
  answer: 1
  explanation: "Lag-1 sparing is the key counterintuitive finding: T2 appearing immediately after T1 is usually NOT missed. The attentional blink is worst at lags 2–4 (roughly 200–400ms), producing a U-shaped curve. This pattern proves the effect is not simply about the stream being too fast — if it were general overload, lag-1 would be the hardest case, not a spared one. Instead, something about T1 consolidation specifically catches closely-following stimuli within a defined temporal window."

- question: "Which explanation best accounts for why the attentional blink occurs at lags 2–4 rather than uniformly across all temporal positions?"
  type: multiple-choice
  options:
    - "Visual masking from subsequent RSVP items is strongest at those specific positions"
    - "Short-term memory decay is fastest within the first 200–500ms of encoding"
    - "The attentional system enters a processing bottleneck during T1 consolidation into working memory, temporarily preventing T2 from gaining conscious access"
    - "The attentional spotlight physically relocates away from the RSVP stream after detecting T1"
  answer: 2
  explanation: "The dominant account connects the blink to conscious consolidation: successfully identifying T1 requires transferring it into working memory, a limited-capacity process that occupies the attentional resources needed to gate T2 into conscious representation. T2 arrives during this occupied window and cannot gain access. The boost-and-bounce model adds that T1's processing boost triggers an inhibitory rebound that actively suppresses nearby stimuli. The effect is not passive decay or masking — it is a specific refractory period in the machinery of conscious access."

- question: "The attentional blink shows that attention itself, when successfully deployed to process one target, can impair perception of a closely following second target."
  type: true-false
  answer: true
  explanation: "This is the core paradox of the attentional blink: the very act of attending successfully to T1 produces the conditions for missing T2. The blink occurs specifically because T1 was detected and processed — not because attention failed. This overturns the intuition that 'paying attention' reliably improves perception. Under the right temporal conditions, successful attention to one thing creates a window of blindness for the next thing."

- question: "The attentional blink is caused by the RSVP stream being presented too rapidly for the visual system to perceive items, so slowing the stream would eliminate the effect."
  type: true-false
  answer: false
  explanation: "The blink is not about the absolute speed of presentation — it is about the temporal interval between T1 and T2. If T2 still falls within the 200–500ms post-T1 window, the blink occurs regardless of the stream's overall rate. The U-shaped detection curve (with lag-1 sparing and recovery by lag 7–8) cannot be explained by general perceptual overload. The effect reflects a specific refractory period in conscious consolidation, not a perceptual speed limit."

- question: "Why does the attentional blink occur within a specific 200–500ms window rather than extending indefinitely after T1?"
  type: short-answer
  answer: "The blink reflects the finite time required for T1 to be consolidated into working memory — a process that occupies the attentional gating mechanism needed to admit T2 into conscious representation. Once T1 consolidation is complete (roughly 500ms post-T1), the system becomes available again and T2 detection recovers to baseline. The window is bounded because the bottleneck has a characteristic timecourse: it opens when T1 processing begins and closes when that processing completes."
  explanation: "The bounded timecourse is the diagnostic signature that separates the blink from general fatigue or masking. The recovery by lag 7–8 shows the system is not permanently degraded — it is temporarily occupied with a specific task (T1 consolidation) and becomes available again when that task is done. This timecourse matches predictions from working memory models and global workspace theory, both of which treat conscious access as a limited-capacity process with a finite completion time."
```

## Explainer

You know from selective attention that the cognitive system handles limited information by selectively prioritizing certain inputs — the spotlight metaphor captures the spatial dimension of this selection. The **attentional blink** reveals a parallel constraint in the *temporal* dimension: even if you are attending to the right location, you can fail to perceive a target that appears too soon after you processed a previous one. The standard demonstration uses **rapid serial visual presentation (RSVP)**: a stream of letters or images flashed at rates of 8–12 items per second, with two designated targets embedded in the stream. When the second target (T2) appears within roughly 200–500 ms of the first (T1), it is missed at rates far above baseline — sometimes over 50% of the time — despite the fact that attention was fully directed to the stream.

The temporal specificity of the blink is diagnostic. It is not that the stream is simply too fast: if T2 appears immediately after T1 (lag-1 position), it is usually *not* missed — a phenomenon called **lag-1 sparing**. The blink is worst at lags 2–4 (roughly 200–400 ms) and resolves by lag 7–8. This U-shaped curve over time implies that the attentional system is not simply overloaded — it is undergoing a specific refractory process with a characteristic timecourse. Something about successfully processing T1 temporarily impairs the processing of T2 specifically within that 200–500 ms window.

The leading explanation connects directly to your working memory model. Processing T1 to the level required for identification and report requires conscious consolidation — transferring information into the limited-capacity workspace of working memory. During this consolidation, the system appears to enter a **processing bottleneck**: attentional resources needed to gate T2 into conscious representation are occupied, and T2 is suppressed or fails to be consolidated before it decays. This is not passive decay due to the passage of time; it is active suppression — a proposed **inhibitory rebound** in which the attentional system overshoots in its recovery from T1 processing and briefly suppresses information that would normally gain access to consciousness. The **boost-and-bounce** model formalizes this: T1 receives a boost that temporarily elevates processing, but this boost triggers a subsequent inhibitory bounce that catches any closely following stimulus.

Global workspace theory provides another lens: conscious perception requires a competitive process in which representations are amplified and broadcast across a distributed workspace. T1 "wins" this competition and monopolizes the broadcast, and T2 — which arrives while the workspace is still occupied with T1 — cannot gain entry. Strikingly, if T2 is emotionally significant (one's own name, a threatening word), it sometimes breaks through the blink anyway — suggesting that highly salient stimuli have privileged pathways to the workspace that bypass the ordinary bottleneck.

What the attentional blink reveals about cognition is fundamental: **consciousness is not a passive recorder of ongoing events but a limited-capacity process that must be allocated**. Successful attention to one thing actively impairs perception of the next thing, for a very specific window of time. This has practical implications — eyewitness accounts in rapidly unfolding events, air-traffic control under high load, multitasking during driving — all involve scenarios where the temporal dynamics of attention matter enormously. The blink also provides one of the cleaner experimental windows into the neural machinery of conscious access, making it a cornerstone of experimental research on the limits of perception.

