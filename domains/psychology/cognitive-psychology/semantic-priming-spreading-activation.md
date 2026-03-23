---
id: semantic-priming-spreading-activation
title: Semantic Priming and Spreading Activation
domain: psychology
course: cognitive-psychology
prerequisites:
- id: language-comprehension
  type: soft
builds-toward:
- false-memory-source-misattribution
tags:
- semantics
- priming
- activation
- networks
stage: formal-systems
status: draft
---

# Semantic Priming and Spreading Activation

## Core Idea
Semantic priming—faster response to target words following related primes—reveals that activation spreads automatically through semantic networks. Priming effects depend on association strength and decay over time. This indicates semantic memory is organized as interconnected networks where activating one concept increases activation of related concepts.

## Questions

```yaml
- question: "A participant is told to ignore the prime word and focus only on judging whether each target is a real word. Despite these instructions, they still respond faster to 'BUTTER' when preceded by 'BREAD' than when preceded by 'TRUCK.' What does this result best demonstrate?"
  type: multiple-choice
  options:
    - "Participants cannot reliably follow instructions, so the priming effect is a task-compliance artifact"
    - "The priming effect is strategic — participants predict the target based on the prime despite instructions"
    - "Spreading activation is automatic and does not require conscious attention or intention"
    - "The lexical decision task is too simple to reveal true priming under attentional suppression"
  answer: 2
  explanation: "Automaticity is the defining feature of spreading activation priming. Because activation spreads passively through the network regardless of conscious intention, the priming effect persists even when participants are instructed to ignore the prime. This distinguishes semantic priming from strategic expectancy, which does respond to instructions and requires time to develop. A strategically generated effect would diminish when participants are told not to predict; the early, short-interval priming effect does not."

- question: "A patient with semantic dementia (anterior temporal lobe damage) shows uniformly reduced priming across all semantic categories. A second patient with visual cortex damage shows reduced priming only for visual-property words like 'bright' while priming for other semantic relationships is normal. What is the best interpretation?"
  type: multiple-choice
  options:
    - "Both patients demonstrate that semantic memory is stored entirely in a single central hub"
    - "The first patient supports a hub model; the second supports a distributed model where concept meaning partly depends on sensory-motor cortex"
    - "Both patients demonstrate that priming is primarily a strategic expectancy effect rather than automatic activation"
    - "The second patient's pattern shows that the visual cortex controls all lexical decisions regardless of word meaning"
  answer: 1
  explanation: "Hub damage (semantic dementia) flattens the semantic network uniformly — all categories degrade together, consistent with a central convergence zone where semantic representations are integrated. Sensory-motor area damage produces category-specific deficits: words whose meaning involves visual properties depend partly on visual cortex, words with strong motor associations depend partly on motor cortex. This double dissociation supports a distributed model where meaning is grounded in the sensory-motor systems that represent the relevant properties."

- question: "Priming effects are larger when the associative relationship between prime and target is stronger."
  type: true-false
  answer: true
  explanation: "In the spreading activation model, activation spreads along edges in proportion to association strength. A strongly associated prime-target pair (BREAD → BUTTER) sends more activation to the target node before the lexical decision than a weakly associated pair (BREAD → CARBOHYDRATE). More pre-activation means the target reaches threshold faster, producing a larger response time advantage — a larger priming effect."

- question: "Strategic expectancy and spreading activation produce identical priming effects at all prime-target time intervals."
  type: true-false
  answer: false
  explanation: "They have distinct temporal signatures. Spreading activation is fast and produces priming effects even at very short prime-target intervals (as little as 50–250ms). Strategic expectancy requires time to generate a prediction and is visible primarily at longer intervals. Critically, strategic effects disappear when participants are told not to predict; automatic spreading activation does not. If the effects were identical across all intervals and conditions, we could not distinguish the mechanisms — but they are not, which is why short-interval priming is used as a 'pure' measure of automatic activation."

- question: "Why does the semantic priming effect provide evidence about the *organization* of semantic memory rather than just its *contents*?"
  type: short-answer
  answer: "The priming effect reveals that semantic memory is not just a list of concepts but a network where concepts are linked by associative edges with varying strengths. Activating one node automatically spreads pre-activation to neighboring nodes in proportion to connection strength before the target even appears. This shows the architecture — an interconnected structure where relationships between concepts are explicitly encoded — not merely the fact that those concepts exist in memory."
  explanation: "If semantic memory were an unstructured store, there would be no reason to expect that seeing one word speeds processing of a related word. The priming effect requires a mechanism by which the prime's activation propagates to related representations. That mechanism — weighted associative links between concept nodes — is what the spreading activation model proposes, and the graded nature of the priming effect (stronger for stronger associations) directly reflects the structure of those links."
```

## Explainer

The **priming paradigm** is deceptively simple: show a participant a word (the prime), then show them a target word and measure how quickly they can make a lexical decision (is this a real word?). When prime and target are semantically related — BREAD → BUTTER — responses are faster than when they are unrelated — NURSE → BUTTER. This **semantic priming effect** is typically 20–50ms, small but reliable, and it reveals something important about how knowledge is stored and accessed.

**Spreading activation** (Collins & Loftus, 1975) is the dominant explanation. In this model, semantic memory is organized as a **network of nodes** (concepts) connected by edges (associations). When you encounter BREAD, the BREAD node activates. That activation then **spreads** along edges to neighboring nodes — BUTTER, TOAST, CARBOHYDRATE, WHEAT — in proportion to the strength of the association. By the time you see BUTTER, its node is already partially activated, so the lexical decision process reaches threshold faster. Stronger associations produce larger priming effects; weaker or more indirect associations produce smaller effects that decay more quickly.

A critical feature of spreading activation is that it is **automatic and passive** — it does not require conscious attention or intention. Even if participants are told the prime is irrelevant to their task, priming effects still occur. This automaticity distinguishes semantic priming from strategic expectancy: if you see the prime DOCTOR and consciously predict that NURSE is coming next, you will show a priming effect even for non-associates — but this strategic effect takes longer to develop, is visible only at long prime-target intervals, and disappears when participants are told not to predict. The early, short-interval priming effect is purely the result of spreading activation through the semantic network.

The architecture of the network carries theoretical implications. **Hub models** (where abstract semantic concepts are stored in a central hub, such as anterior temporal lobe) and **distributed models** (where meaning emerges from patterns of activity across sensory-motor cortex) make different predictions about the structure of priming. Hub damage (semantic dementia) flattens the semantic network — priming effects degrade uniformly across all semantic categories. Sensory-motor area damage produces category-specific deficits: patients with motor cortex damage show reduced priming for action words; patients with visual cortex damage show reduced priming for visual-property words like "bright." **Semantic priming thus provides a behavioral window into the organization of conceptual knowledge** — not just whether two things are related, but how the mind represents the nature of that relationship.
