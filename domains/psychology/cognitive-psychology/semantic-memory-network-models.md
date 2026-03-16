---
id: semantic-memory-network-models
title: Semantic Memory and Network Models
domain: psychology
course: cognitive-psychology
prerequisites:
- id: memory-encoding-depth
  type: hard
- id: semantic-processing-temporal-cortex
  type: soft
builds-toward:
- mental-model-construction
tags:
- semantic-memory
- networks
- knowledge
- representation
stage: formal-systems
status: draft
---

# Semantic Memory and Network Models

## Core Idea
Semantic memory stores factual knowledge and concepts in organized network structures. Network models represent concepts as nodes connected by associative links of varying strength. Spreading activation through these networks explains semantic priming effects and how activation of one concept influences processing of related concepts.

## How It's Best Learned
Use semantic priming paradigms where prior exposure to related words speeds target recognition, demonstrating the network connectivity underlying semantic memory.

## Explainer

From your work on memory encoding, you know that deeper, meaning-based processing produces stronger memory traces than shallow surface processing. **Semantic memory** is the system that stores this meaning-based knowledge: facts about the world, word meanings, categorical relationships, and conceptual knowledge. Unlike episodic memory (memories of specific personal events tied to time and place), semantic memory is largely context-free — you know that Paris is the capital of France without remembering when or how you learned it. Network models attempt to formalize how this knowledge is organized and how activating one piece of knowledge influences access to related pieces.

The core architecture of network models is simple: **concepts are represented as nodes** in a network, connected by labeled links of varying strength. In Collins and Quillian's (1969) **hierarchical network model**, concepts are organized taxonomically — "canary" links to "bird" links to "animal," with properties stored at the highest applicable level. "Has wings" is stored at "bird," not duplicated for every bird species. This storage economy predicts that verifying "A canary can fly" should take longer than "A canary is yellow," because flight requires traversing up one level. Early experiments confirmed this prediction, suggesting a neat hierarchical structure. But the model failed when typicality was varied: people verify "A robin is a bird" faster than "A penguin is a bird," even though both are exactly one link from "bird." Typicality — how much a concept resembles the prototype — affects retrieval speed, and a pure hierarchy cannot explain this.

Collins and Loftus (1975) replaced the hierarchy with **spreading activation networks**, where link strength reflects degree of semantic relatedness rather than taxonomic level. When you activate the concept "fire," activation spreads outward through the network — strongly to closely associated concepts (fire engine, red, ambulance) and weakly to distant ones (sky, water). This spreading activation provides the mechanism for **semantic priming**: seeing the word "doctor" reduces your reaction time to recognize "nurse" because activation from "doctor" has already spread to the "nurse" node before the target appears. The amount of priming predicts the network distance between concepts — strongly associated pairs prime more, distant pairs prime less or not at all. Reaction time experiments can thus map the structure of semantic memory by measuring pairwise priming across large sets of word pairs.

The network framework also illuminates how semantic memory breaks down in neurological conditions. In **semantic dementia** (caused by anterior temporal lobe atrophy), patients lose semantic knowledge gradually — but not randomly. They lose atypical category members before typical ones (knowing "dog" but losing "hyena"), fine-grained distinctions before broad categories ("animal" preserved after "dog" is lost), and peripheral properties before defining ones. This pattern is exactly what spreading activation networks predict: typical members and central properties are more densely connected and receive activation from more directions, making them more robust to partial damage. Atypical members with fewer strong connections are lost first because their representation depends on links that degrade early. The network is not just a metaphor — it is a mechanistic account of semantic organization that predicts both the normal structure of knowledge retrieval and the specific pattern in which that structure fails.
