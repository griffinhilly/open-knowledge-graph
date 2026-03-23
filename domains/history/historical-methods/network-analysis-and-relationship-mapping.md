---
id: network-analysis-and-relationship-mapping
title: Network Analysis and Relationship Mapping
domain: history
course: historical-methods
prerequisites:
- id: prosopography-collective-biography
  type: hard
- id: quantitative-historical-analysis
  type: soft
tags:
- network-analysis
- relationships
- connections
- mapping
stage: formal-systems
status: draft
---

# Network Analysis and Relationship Mapping

## Core Idea
Network analysis visualizes connections—family ties, correspondence, patronage, trade—among historical actors, revealing power structures and information flow invisible in narrative. This approach reveals brokers, clusters, and patterns of influence that shape historical outcomes but may be obscured by narrative focus on individuals.

## Questions

```yaml
- question: "A historian maps the correspondence networks of sixteenth-century Italian merchants and identifies one merchant with few total letters but who appears as the sole connection between two otherwise separate trading clusters. What does this structural position most suggest?"
  type: multiple-choice
  options:
    - "This merchant was relatively unimportant, since they had fewer total connections than more central actors"
    - "This merchant occupied a structural hole and likely held disproportionate power to control information and opportunity between the clusters"
    - "This merchant was a marginal figure who failed to integrate into either cluster"
    - "This structural position indicates the merchant was a record-keeper rather than an active trader"
  answer: 1
  explanation: "Structural holes — gaps between otherwise disconnected clusters — are often where the most powerful brokers sit. The actor who connects two groups that would not otherwise interact controls what each group knows about the other, what opportunities are brokered, and at what terms. Volume of connections (degree centrality) can be misleading: a broker with few connections but positioned between dense clusters often has more influence than a well-connected actor within a single cluster. Network analysis makes this structural power visible."

- question: "Historical network analyses based on correspondence archives systematically underrepresent certain populations. What is the primary reason for this limitation?"
  type: multiple-choice
  options:
    - "Correspondence archives only survive for politically powerful actors whose documents were preserved by states"
    - "Non-literate populations, women, and the poor conducted their social relationships orally, leaving no written traces that can become edges in the network"
    - "Network analysis software cannot process handwritten documents, only digital records"
    - "Pre-modern people had fewer meaningful relationships, so their networks were too sparse to analyze"
  answer: 1
  explanation: "Network analysis can only map relationships that left systematic written records — correspondence, account books, parish registers, notarial documents. Non-literate populations had rich social networks conducted entirely orally, which left no archival trace. Women and the poor are similarly underrepresented because their relationships were less likely to generate the kinds of institutional records that survive. The historian must be explicit about whose networks they can and cannot reconstruct."

- question: "An actor who occupies a structural hole between two dense network clusters controls the flow of information and opportunity between those clusters."
  type: true-false
  answer: true
  explanation: "Structural holes are the gaps between clusters in a network. An actor positioned to bridge such a gap — present in both clusters or connecting them — controls what each side knows about the other, which people get introduced to which opportunities, and on what terms exchange happens. This positional power can be enormous relative to the broker's total number of connections. The Medici example illustrates this: their influence in Renaissance Florence came not from being the most connected, but from bridging networks that otherwise didn't interact."

- question: "A highly central actor in a historical correspondence network is necessarily the most powerful actor in the historical record."
  type: true-false
  answer: false
  explanation: "Network structure is a hypothesis-generator, not a direct measure of power. A highly central actor may have been powerful — or may have been a useful intermediary without autonomous influence, an administrative node, or an unusually prolific letter-writer whose correspondence doesn't translate into political or economic power. The historian's job is to note structural patterns and then return to primary sources to ask whether the structural position actually manifests as influence, access, or power. Network analysis and narrative history must be used together."

- question: "What is the key conceptual shift from prosopography to network analysis, and why does it change what historians can discover?"
  type: short-answer
  answer: "Prosopography studies individuals by collecting biographical data on groups and looking for patterns across their attributes and careers. Network analysis shifts the primary object of study from individuals to the relationships between them — edges, not nodes. This matters because power, influence, and historical outcomes often arise not from individual attributes but from structural positions: who is connected to whom, whether those connections span otherwise-separate groups, and where information or resources flow through the network. Narrative history focused on individuals can describe what Lorenzo de' Medici did; network analysis explains structurally why his position made it possible."
  explanation: "The conceptual shift is from attributes (who were these people?) to structure (how did these people connect, and what does that structure reveal?). This is not a rejection of individual biography but a supplement: it surfaces patterns of influence and exclusion that are invisible in any single life story, and makes claims about social structure that can be tested against quantitative data."
```

## Explainer

Prosopography — your prerequisite — gave you the practice of collecting biographical data on groups of individuals and looking for patterns. Network analysis extends this by making the **relationships between individuals** the primary object of study, not the individuals themselves. The shift is conceptual: instead of asking "who was this person and what did they do?", you ask "how did this person connect to others, and what does that position in the network reveal about their power, access, or influence?"

The core vocabulary comes from graph theory, applied to historical data. Each person (or institution, city, or state) becomes a **node**; each relationship — a letter exchanged, a business partnership, a marriage alliance, a trade route, a shared patron — becomes an **edge**. Once you map a network, structural features emerge that are invisible in narrative. **Centrality** measures how connected a node is: a highly central actor is one through whom many connections pass, making them an information broker or power node. **Clustering** reveals tight sub-groups — cliques within which information and trust circulate densely, but between which there may be sparse connections. The gaps between clusters, called **structural holes**, are often where the most powerful brokers sit: the person who connects otherwise-isolated groups controls the flow of information and opportunity between them.

Consider how this illuminates, say, Renaissance Florence. Narrative history might focus on Lorenzo de' Medici as a great patron of arts and letters. Network analysis asks: what was the Medici's position in Florence's financial, political, and kinship networks? It turns out the Medici occupied structural holes across multiple Florentine elite networks simultaneously — they were marriage partners, business creditors, and political clients to groups that didn't otherwise interact. This positional power explains their influence more precisely than invoking "greatness." The network map makes visible what narrative description can only gesture at.

The **data challenges** are real and worth understanding. Network analysis depends on systematic records — correspondence archives, account books, parish records, notarial registers. The richer the records, the more complete the network you can construct. But records systematically underrepresent women, the poor, and non-literate populations, whose relationships often left no written trace. A network of surviving correspondence reveals the networks of literate, institutionally-connected people — it does not reveal the social world of an illiterate artisan whose relationships were entirely oral and unrecorded. This isn't a reason to avoid network analysis, but it means you must be explicit about whose networks you can and cannot see.

Your prerequisite in quantitative analysis gives you a leg up here: network metrics are quantitative, and interpreting them requires the same care as any statistical claim. A network visualization can be visually compelling but analytically misleading if the underlying data is incomplete, or if edge definitions are inconsistent (treating a single letter exchange the same as a ten-year business partnership inflates apparent connections). The historian's job is to use network structure as a hypothesis-generator — noting a pattern, then returning to primary sources to ask whether the structural position actually manifests as influence, access, or power in the historical record.
