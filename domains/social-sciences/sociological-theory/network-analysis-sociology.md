---
id: network-analysis-sociology
title: Network Analysis in Sociology
domain: social-sciences
course: sociological-theory
prerequisites:
- id: sociological-imagination
  type: hard
- id: graph-theory-intro
  type: hard
- id: degree-sequences
  type: soft
builds-toward:
- granovetter-weak-ties
tags:
- network
- social-networks
- graph-theory
- relations
stage: advanced
status: validated
---

# Network Analysis in Sociology

## Core Idea
Network analysis studies social structure as patterns of connections between actors (individuals, organizations, nations). Sociologists examine centrality, clustering, brokerage, and diffusion to understand how networks constrain opportunity, transmit information, and shape outcomes.

## Questions

```yaml
- question: "Two job seekers have equal qualifications. Alicia has 20 close friends who all work in her industry and know her well. Boris has 5 close friends but 200 acquaintances spanning many different industries. Based on network analysis, who has the structural advantage for finding a new job?"
  type: multiple-choice
  options:
    - "Alicia, because stronger ties provide more reliable referrals and her friends can vouch for her more credibly"
    - "Boris, because his weak ties bridge different clusters and give him access to novel job information his close friends don't have"
    - "Both equally, since total number of connections is what determines access to opportunity"
    - "Alicia, because her dense cluster provides stronger social support during a stressful job search"
  answer: 1
  explanation: "Alicia's close friends are all in her industry cluster—they know what she knows and have access to the same job listings. Boris's 200 weak ties reach into many different clusters, each carrying different information. Granovetter's weak-tie hypothesis follows directly from the logic of clustering: strong ties within a dense group produce redundant information, while weak ties bridge groups and carry novel information unavailable within the cluster."

- question: "A mid-level manager with modest credentials wields surprising influence in a large organization. She is not the most connected person, but she is the person most likely to appear on the shortest path between any two other employees. Network analysis would attribute her influence primarily to..."
  type: multiple-choice
  options:
    - "Her charisma and interpersonal skills, which allow her to overcome her credential gap"
    - "High betweenness centrality—she sits at critical information bridges between otherwise disconnected groups"
    - "High degree centrality—she must have more connections than her colleagues realize"
    - "Her membership in multiple dense clusters, which gives her simultaneous access to many information pools"
  answer: 1
  explanation: "Betweenness centrality measures how often a node lies on the shortest paths between other nodes. An actor with high betweenness is a broker who controls information flow between groups that would otherwise not communicate. This structural position translates into real influence regardless of formal credentials or raw number of connections—which is precisely the point: network position explains outcomes that individual attributes cannot."

- question: "Whether two people in a social network are connected to each other can affect both of their outcomes, even if neither person directly chose to create or avoid that connection."
  type: true-false
  answer: true
  explanation: "This is the core claim of the structural approach: people's outcomes are shaped by patterns of relationships they are embedded in, including indirect relationships they have no control over. If two of your contacts are connected to each other, they form a triangle with you—a dense cluster. If they are not connected, you occupy a brokerage position between them. This structural fact shapes the information you receive and the influence you can exert, independent of anyone's intentions."

- question: "In social network analysis, an individual's outcomes are best predicted by the attributes and credentials of their closest connections rather than by their structural position in the network."
  type: true-false
  answer: false
  explanation: "This is the misconception that network analysis most directly challenges. A person with modest credentials but high betweenness centrality can wield disproportionate influence. A highly talented person isolated within a dense cluster may accomplish less than a well-connected broker. Network analysis argues that structural position—where you sit in the relational topology—predicts outcomes independently of, and often more powerfully than, individual or neighbor attributes."

- question: "Why are weak ties (acquaintances) often more valuable than strong ties (close friends) for accessing novel information? Explain using the concept of clustering."
  type: short-answer
  answer: "Strong ties tend to connect people who are already embedded in the same dense cluster—they share the same social world, attend the same events, and have access to the same information. Because information circulates densely within a cluster, your close friends are likely to know what you already know. Weak ties, by contrast, bridge across clusters: your acquaintances typically belong to different social circles with different information environments. A weak tie is therefore a structural bridge to a non-redundant pool of information. For job searching, this means weak ties are more likely to know about opportunities in different industries or organizations than you and your close friends are already aware of."
  explanation: "Granovetter's insight reframes what we mean by 'useful' connection. It is not the tie strength (intimacy, frequency of contact) that determines informational value—it is the structural role of the tie. A weak tie that spans a structural hole between clusters carries more novel information than a strong tie within a cluster, precisely because the two sides of that bridge don't already share knowledge."
```

## Explainer

You bring two prerequisite frameworks to network analysis that are now in direct conversation. From the sociological imagination, you know that individual lives are shaped by social structures that individuals cannot fully see or control. From graph theory, you know how to represent relationships formally: nodes, edges, paths, components, and the mathematical properties that follow from those structures. Network analysis in sociology is what happens when you apply graph-theoretic tools to social structures — it gives the sociological imagination a formal vocabulary.

The foundational move is representing social actors as **nodes** and their relationships as **edges**. But which relationships? This choice is sociologically loaded. You can map friendship ties, advice-seeking, co-authorship, financial transactions, phone calls, or sexual contact — each captures a different social process and will produce a different structural picture. The network you analyze must be selected based on a theory of what kind of connection matters for the outcome you are trying to explain. Choosing the wrong relational substrate produces misleading structural conclusions.

Three concepts do most of the explanatory work. **Centrality** measures how well-positioned an actor is within the network. Degree centrality (raw number of connections) captures popularity; betweenness centrality measures how often an actor lies on the shortest path between other pairs — these are the **brokers** who sit at critical information bridges. Eigenvector centrality (the basis of PageRank) captures whether your connections are themselves well-connected. **Clustering** measures how often your connections are connected to each other — high clustering means you are embedded in a tight-knit community where information circulates densely but redundantly. **Path length** measures how many steps separate any two nodes — short average path lengths mean information diffuses quickly across the whole network.

These structural properties explain outcomes that individual-level attributes cannot. A person with modest credentials but high betweenness centrality can wield disproportionate influence by controlling information flow between otherwise disconnected groups. A highly talented person isolated within a dense cluster may accomplish less than a well-connected broker who can link knowledge across different communities. Granovetter's famous finding — that **weak ties** (acquaintances rather than close friends) are often more valuable for job searches than strong ties — follows directly from this logic: your close friends are in your cluster and know what you know, while weak ties reach into other clusters where novel information resides. Network analysis makes this structural insight precise, measurable, and portable across domains.
