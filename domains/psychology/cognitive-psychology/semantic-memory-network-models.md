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
status: validated
---

# Semantic Memory and Network Models

## Core Idea
Semantic memory stores factual knowledge and concepts in organized network structures. Network models represent concepts as nodes connected by associative links of varying strength. Spreading activation through these networks explains semantic priming effects and how activation of one concept influences processing of related concepts.

## How It's Best Learned
Use semantic priming paradigms where prior exposure to related words speeds target recognition, demonstrating the network connectivity underlying semantic memory.

## Questions

```yaml
- question: "In a lexical decision task, participants see a prime word and then must decide if a target is a real word. 'Doctor' primes 'nurse' — responses to 'nurse' are faster after seeing 'doctor' than after seeing 'lamp.' Spreading activation theory predicts that 'hospital' would prime 'nurse'..."
  type: multiple-choice
  options:
    - "More than 'doctor,' since hospitals are more directly associated with nurses in a professional sense"
    - "Equally to 'doctor,' since both are semantically medical and priming is categorical"
    - "Somewhat, but likely less than 'doctor' if the 'hospital'–'nurse' associative link is weaker than the 'doctor'–'nurse' link"
    - "Not at all, because spreading activation only travels one link at a time and 'hospital' is not directly linked to 'nurse'"
  answer: 2
  explanation: "Spreading activation predicts priming proportional to associative link strength, not just category membership. If 'doctor'–'nurse' is a stronger or more direct link than 'hospital'–'nurse,' then 'doctor' will prime 'nurse' more. Both primes should produce some facilitation since both are semantically related to 'nurse,' but the degree of priming varies with link strength. This is precisely why reaction time experiments can map the fine-grained structure of semantic memory."

- question: "Collins and Quillian's (1969) hierarchical network model predicted equal verification times for 'A robin is a bird' and 'A penguin is a bird,' since both require one taxonomic step. The observed typicality effect — robins are verified faster — is best explained by which account?"
  type: multiple-choice
  options:
    - "Penguins are less common words, so lexical access is slower regardless of the semantic relationship"
    - "The hierarchical model is correct; the typicality effect is an artifact of participants being more familiar with robins"
    - "Typical members like robins have stronger or more numerous associative links to 'bird,' receiving more spreading activation than atypical members like penguins"
    - "People store typical and atypical category members in separate memory systems with different access speeds"
  answer: 2
  explanation: "Spreading activation networks explain typicality effects naturally: a typical bird like a robin has many strong connections to bird features (flies, has wings, sings, builds nests) and to the 'bird' node itself, so it receives activation from many directions simultaneously. An atypical member like a penguin has fewer or weaker links — it shares fewer features with the bird prototype. The hierarchical model's assumption of equal one-step distances for all category members is the flaw that typicality effects expose."

- question: "In spreading activation theory, semantic priming occurs because seeing a prime word causes activation to spread through the network before the target appears, so related concepts are already partially active when the target word must be processed."
  type: true-false
  answer: true
  explanation: "This is the core mechanistic account of priming in spreading activation models. The prime activates its node, activation spreads along associative links to neighboring nodes with strength proportional to link weight, and nodes that are pre-activated require less additional activation to reach threshold for recognition. The result is faster reaction times for targets semantically related to the prime. This mechanism makes the model empirically testable: stronger associative links should produce larger priming effects."

- question: "Patients with semantic dementia lose knowledge of typical category members (like 'dog') before atypical ones (like 'hyena'), because typical items are encountered more frequently in daily life and are therefore more vulnerable to degradation."
  type: true-false
  answer: false
  explanation: "The opposite is true: atypical members are lost before typical ones. The explanation is not frequency of encounter but network structure. Typical members like 'dog' have many strong connections to the 'animal' node, to shared features, and to other typical members — they receive activation from many directions and are robust to partial damage. Atypical members like 'hyena' have fewer, weaker links and depend on a smaller number of connections that degrade early. This gradient of loss from periphery to center is precisely what spreading activation networks predict."

- question: "Why does the spreading activation network model predict that semantic dementia patients will lose knowledge of atypical category members before typical ones? What does this pattern reveal about how knowledge is organized in semantic memory?"
  type: short-answer
  answer: "Typical category members (like 'robin' for birds) are densely connected — they share many features with the category prototype, have strong links to the category node, and receive spreading activation from many directions. Even as some connections degrade, activation still reaches them along multiple pathways. Atypical members (like 'penguin') have fewer strong connections and depend on a small number of links that are more vulnerable to damage. When anterior temporal lobe atrophy reduces network connectivity, peripheral nodes lose their activation supply first while densely connected typical members remain accessible longer. This reveals that semantic memory is not a flat list but a weighted network where knowledge is represented through the density and strength of relational connections."
```

## Explainer

From your work on memory encoding, you know that deeper, meaning-based processing produces stronger memory traces than shallow surface processing. **Semantic memory** is the system that stores this meaning-based knowledge: facts about the world, word meanings, categorical relationships, and conceptual knowledge. Unlike episodic memory (memories of specific personal events tied to time and place), semantic memory is largely context-free — you know that Paris is the capital of France without remembering when or how you learned it. Network models attempt to formalize how this knowledge is organized and how activating one piece of knowledge influences access to related pieces.

The core architecture of network models is simple: **concepts are represented as nodes** in a network, connected by labeled links of varying strength. In Collins and Quillian's (1969) **hierarchical network model**, concepts are organized taxonomically — "canary" links to "bird" links to "animal," with properties stored at the highest applicable level. "Has wings" is stored at "bird," not duplicated for every bird species. This storage economy predicts that verifying "A canary can fly" should take longer than "A canary is yellow," because flight requires traversing up one level. Early experiments confirmed this prediction, suggesting a neat hierarchical structure. But the model failed when typicality was varied: people verify "A robin is a bird" faster than "A penguin is a bird," even though both are exactly one link from "bird." Typicality — how much a concept resembles the prototype — affects retrieval speed, and a pure hierarchy cannot explain this.

Collins and Loftus (1975) replaced the hierarchy with **spreading activation networks**, where link strength reflects degree of semantic relatedness rather than taxonomic level. When you activate the concept "fire," activation spreads outward through the network — strongly to closely associated concepts (fire engine, red, ambulance) and weakly to distant ones (sky, water). This spreading activation provides the mechanism for **semantic priming**: seeing the word "doctor" reduces your reaction time to recognize "nurse" because activation from "doctor" has already spread to the "nurse" node before the target appears. The amount of priming predicts the network distance between concepts — strongly associated pairs prime more, distant pairs prime less or not at all. Reaction time experiments can thus map the structure of semantic memory by measuring pairwise priming across large sets of word pairs.

The network framework also illuminates how semantic memory breaks down in neurological conditions. In **semantic dementia** (caused by anterior temporal lobe atrophy), patients lose semantic knowledge gradually — but not randomly. They lose atypical category members before typical ones (knowing "dog" but losing "hyena"), fine-grained distinctions before broad categories ("animal" preserved after "dog" is lost), and peripheral properties before defining ones. This pattern is exactly what spreading activation networks predict: typical members and central properties are more densely connected and receive activation from more directions, making them more robust to partial damage. Atypical members with fewer strong connections are lost first because their representation depends on links that degrade early. The network is not just a metaphor — it is a mechanistic account of semantic organization that predicts both the normal structure of knowledge retrieval and the specific pattern in which that structure fails.
