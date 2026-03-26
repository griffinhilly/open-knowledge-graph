---
id: attention-capacity-and-bottlenecks
title: Attention Capacity and Bottlenecks
domain: psychology
course: cognitive-psychology
prerequisites:
- id: attention-divided
  type: hard
- id: working-memory-model
  type: soft
- id: working-memory-capacity-chunking
  type: soft
builds-toward:
- task-switching-executive-control-costs
tags:
- attention
- capacity
- limitations
- performance
stage: formal-systems
status: validated
---
# Attention Capacity and Bottlenecks

## Core Idea
Attention has limited capacity: we cannot process multiple streams of information equally well simultaneously. The bottleneck occurs at different processing stages depending on task demands and practice level. Understanding capacity limitations explains why multitasking degrades performance and why automaticity develops for well-practiced tasks.

## Questions

```yaml
- question: "Two students try to read text for comprehension while listening to music with lyrics; a third listens to instrumental music. Based on attentional resource theory, which prediction is most accurate?"
  type: multiple-choice
  options:
    - "All three perform equally — music does not affect visual reading"
    - "The lyric-music students show more reading impairment because lyrics and reading compete for the same verbal/linguistic resource pool"
    - "Lyric music helps reading by maintaining arousal"
    - "All students perform identically after sufficient practice"
  answer: 1
  explanation: "Kahneman's resource model and Wickens' multiple resource theory both predict that tasks sharing a resource pool interfere more than tasks drawing from different pools. Lyrics engage verbal/linguistic processing — the same resource reading demands. Instrumental music uses primarily spatial/auditory resources and competes less. Option D is partially true long-term (automaticity) but does not describe the initial dual-task situation."

- question: "A novice driver cannot maintain a conversation while navigating an unfamiliar route. An experienced driver chats easily on the same route. The best explanation is:"
  type: multiple-choice
  options:
    - "The experienced driver has greater total brain capacity"
    - "Practice has shifted driving toward automatic processing, reducing its demands on the central capacity-limited bottleneck"
    - "The novice driver is less intelligent"
    - "Experience physically enlarges the attentional bottleneck"
  answer: 1
  explanation: "Automaticity — not expanded capacity — is the mechanism. Well-practiced tasks migrate away from controlled, resource-demanding processing toward automatic processing that runs in parallel and requires little central bottleneck involvement. The capacity of the bottleneck itself does not grow; the demand placed on it by familiar tasks shrinks. This is why the dual-task ceiling is partly a function of skill level, not just fixed cognitive architecture."

- question: "The attentional bottleneck is a fixed, early-stage filter that prevents most but one stream of sensory information from receiving any further processing."
  type: true-false
  answer: false
  explanation: "Broadbent's early-filter model proposed this, but evidence undermined it — the cocktail party effect (hearing your name across a noisy room) shows unattended information can receive at least partial semantic processing. Modern consensus places the bottleneck primarily at central response selection and decision stages, not at early sensory filtering. The bottleneck location is also not fixed: it varies with task demands, consistent with late-selection and capacity models."

- question: "Automaticity trades processing efficiency for reduced flexibility — well-practiced tasks become harder to modify deliberately, even when you know they need to change."
  type: true-false
  answer: true
  explanation: "This tradeoff is genuine and well-documented. The Stroop effect illustrates it: skilled readers cannot suppress the automatic process of reading a word even when instructed to name the ink color instead. The same applies to any deeply practiced skill — the efficiency gain that made the task easy to dual-task comes at the cost of reconfigurability. This is why correcting deeply ingrained habits requires substantial effort even with full awareness of the problem."

- question: "Explain why extensive practice on a single task can improve performance on a simultaneously performed second task, even without any practice on the two-task combination itself."
  type: short-answer
  answer: "Practice shifts the practiced task toward automatic processing, reducing its demands on the central capacity-limited bottleneck. With less competition for the bottleneck, the second task experiences less interference and performs better — even though neither task was practiced together."
  explanation: "This result distinguishes capacity-based explanations from pure coordination-based explanations of dual-task improvement. If dual-task practice were the only mechanism, you would not expect single-task practice to help. The fact that it does supports the idea that the bottleneck load is the key variable — and that automaticity genuinely reduces that load, freeing resources for concurrent tasks."
```

## Explainer

From your study of divided attention, you know that performance degrades when people try to do two things at once — but the interesting question is why, and why it degrades more for some task combinations than others. The concept of an **attentional bottleneck** provides the answer: at some stage of information processing, the system has limited capacity, and two tasks that compete for that stage interfere with each other in proportion to their shared demands.

Early cognitive theorists proposed the bottleneck as a **filter** that operates at the perceptual stage — only one stream of sensory information can be processed for meaning at a time (Broadbent's early selection model). Later evidence showed this was too early; Treisman's attenuation model and Deutsch & Deutsch's late selection model pushed the bottleneck further along, suggesting that more processing occurs in parallel than early models assumed. The consensus view that emerged — and that fits most of the empirical data — is that the bottleneck location is not fixed. For early sensory discrimination tasks, parallel processing is possible and interference is minimal. For tasks requiring conscious response selection, memory encoding, or executive decision-making, competition for the same processing resource creates a genuine queue — one task must wait while the other is processed. This is the **psychological refractory period**: when two tasks overlap in time and both require central processing, the second task's response is delayed as if waiting for a single-lane bridge to clear.

**Capacity models** — particularly Kahneman's resource model — offer a complementary framework. Rather than a single-channel bottleneck, these models posit a pool of general-purpose attentional resources that tasks draw from. Tasks that compete for the same resource pool interfere with each other; tasks that draw from different resources may coexist without interference. For example, a verbal task and a spatial task can often be performed together more successfully than two verbal tasks, suggesting partially separate resource pools. The dual-task cost — performance degradation relative to single-task baseline — measures how much resource overlap exists between two tasks.

**Automaticity** is what changes with practice. Well-practiced tasks make fewer demands on the central capacity-limited stages, potentially shifting from controlled processing (which requires attentional resources and is slow, serial, and effortful) to automatic processing (which runs in parallel, requires few resources, and is fast but inflexible). The classic demonstration is Spelke, Hirst, and Neisser's study of subjects trained for months to read while taking dictation — initially impossible, eventually nearly seamless. The implication is that the fixed "multitasking ceiling" is not entirely fixed: it is partly a function of skill level. But automaticity has a tradeoff: automatic processes are less amenable to modification, which is why it is so hard to change deeply ingrained habits even when you know they are wrong.
