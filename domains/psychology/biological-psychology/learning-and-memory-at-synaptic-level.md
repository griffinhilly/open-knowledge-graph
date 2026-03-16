---
id: learning-and-memory-at-synaptic-level
title: Learning and Memory at the Synaptic Level
domain: psychology
course: biological-psychology
prerequisites:
- id: synaptic-plasticity-mechanisms
  type: hard
- id: spike-timing-dependent-plasticity
  type: soft
tags:
- Hebbian
- learning
- consolidation
- protein-synthesis
stage: formal-systems
status: draft
---

# Learning and Memory at the Synaptic Level

## Core Idea
Hebbian learning (neurons that fire together wire together) and its molecular implementations via synaptic plasticity provide cellular foundations for conditioning, habit formation, and memory trace formation. Multiple molecular pathways (calcium/calmodulin-dependent kinases, transcription factors like CREB, immediate early genes) translate repeated synaptic activity into stable structural changes: increased spine size, growth of new spines, changes in receptor expression. These changes are consolidated and maintained by new protein synthesis.

## How It's Best Learned
Compare behavioral learning curves with synaptic plasticity timecourse. Study protein synthesis inhibitor effects on memory. Examine spine density changes with experience using dendritic imaging. Trace gene expression changes following learning. Link molecular changes to behavioral memory retention.

## Common Misconceptions
Learning only happens in prefrontal cortex / synaptic plasticity is the complete story of learning / all learning requires NMDA receptors / memory consolidation is fast.

## Explainer

The phrase "neurons that fire together wire together" — **Hebbian learning** — captures the core logic of how experience changes the brain. From your study of synaptic plasticity, you know that long-term potentiation (LTP) strengthens synapses when pre- and postsynaptic neurons activate coincidentally. What this topic adds is the molecular story of *how* that strengthening becomes permanent and *what biological machinery* encodes it as a lasting memory trace.

The key insight is that memory formation happens in stages, and each stage has a distinct molecular signature. In the first seconds to minutes after a strong experience, **calcium influx** through NMDA receptors triggers **CaMKII** (calcium/calmodulin-dependent protein kinase II) to phosphorylate existing proteins, rapidly inserting AMPA receptors into the synapse and inflating synaptic strength. This is fast but fragile — it can be reversed by protein phosphatases if not followed up. The next stage involves **CREB** (cAMP response element-binding protein), a transcription factor that, when activated, switches on **immediate early genes** like *c-fos* and *Arc*. These gene products change the synapse structurally: dendritic spines grow larger, new spines sprout, and the postsynaptic density thickens. This structural remodeling is what makes memory stable over days and years.

Why does memory consolidation require **new protein synthesis**? Because structural changes — growing a spine, building new receptor scaffolds — require proteins that must be manufactured fresh. Blocking protein synthesis with drugs like anisomycin in the hours after learning prevents long-term memory while leaving short-term memory intact, a dissociation that reveals the two-phase architecture. This explains a clinical puzzle: patients with amnesia who can recall events from years ago but lose the ability to form new long-term memories (as in hippocampal damage) are failing at the consolidation-to-structural-change pipeline, not at initial synaptic strengthening.

Not all learning uses the same molecular path. Fear conditioning in the amygdala, spatial learning in the hippocampus, and motor habit learning in the striatum each use variations of the core Hebbian machinery but with different modulatory influences (dopamine for reward-based learning, norepinephrine for emotionally salient events). The **NMDA receptor as coincidence detector** is central to most, but some forms of plasticity bypass it entirely. This is why the misconception that all learning requires NMDA receptors is misleading: the basic logic of activity-dependent strengthening is universal, but evolution has implemented it with considerable local variation across circuits.

The big picture is that learning is literally a physical remodeling of the brain's wiring diagram. Every memory you have is encoded in a specific pattern of synaptic weights across a distributed network, stabilized by proteins that were synthesized in the hours after the learning event. This means memory is not a recording — it is a reconstruction at retrieval, shaped by whatever synaptic configuration exists at that moment. The same molecular plasticity that makes learning possible also makes memories malleable, which is both the hope behind reconsolidation-based therapies and the challenge of traumatic memory that persists despite its distortions.
