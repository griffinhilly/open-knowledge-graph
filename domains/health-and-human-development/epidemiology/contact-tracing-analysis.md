---
id: contact-tracing-analysis
title: Contact Tracing and Chain of Transmission
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: outbreak-investigation
  type: hard
- id: network-epidemiology
  type: soft
tags:
- contact-tracing
- transmission-chains
- outbreak-response
stage: advanced
status: draft
---

# Contact Tracing and Chain of Transmission

## Core Idea
Contact tracing identifies individuals exposed to confirmed cases and monitors them for infection. Epidemiologic analysis reconstructs transmission chains, estimates secondary attack rates, and identifies super-spreaders. Contact tracing data informs network structure and transmission patterns guiding targeted interventions.

## Explainer

From outbreak investigation, you know how to identify a case definition, build an epidemic curve, and form hypotheses about the source of an outbreak. Contact tracing is the operational follow-through: once cases are found, you work both backward (who exposed this case?) and forward (who did this case expose?) to map the transmission network. The analytical goal is not just to interrupt current spread, but to learn the shape of transmission — who spreads to whom, how efficiently, and through what settings.

The core unit of analysis in contact tracing is the **transmission pair**: a source case and a secondary case linked by documented exposure. From a set of transmission pairs, you can estimate the **secondary attack rate (SAR)** — the proportion of exposed contacts who develop confirmed infection. SAR varies by contact type: household contacts typically have higher SAR than casual workplace contacts, because the dose and duration of exposure are greater. Comparing SAR across contact categories tells you where transmission is most efficient and where interventions (quarantine, ventilation, masking) would have the most impact.

Aggregating transmission pairs produces **transmission chains** — directed graphs where each node is a case and each edge points from source to secondary case. Most chains are short: one person infects one or two others and the chain dies out. But occasionally a single case generates a disproportionately large number of secondary cases — a **super-spreader event**. Super-spreading is partly biological (some individuals shed more pathogen) but mostly contextual: crowded, poorly ventilated, high-contact settings dramatically amplify transmission regardless of who the index case is. The statistical signature of super-spreading is an overdispersed offspring distribution — most cases have a reproduction number near zero, but a fat tail of cases with very high numbers. This has direct implications for control: interrupting super-spreading events (by regulating venue capacity, improving ventilation, or rapidly isolating high-risk gatherings) may be more efficient than trying to uniformly reduce transmission everywhere.

If you have studied network epidemiology, you can connect these transmission chains to network structure. Each case is a node; each transmission is a directed edge. Super-spreaders are high-degree hubs. The density and clustering of the contact network determines how quickly a pathogen can reach the whole population from a single introduction. Contact tracing data provides empirical estimates of this network's local structure that purely mathematical models cannot — it reveals which edges actually transmit infection, not just which contacts exist.

The practical limits of contact tracing are important to understand analytically. Tracing success depends on case ascertainment (finding cases quickly), recall accuracy (contacts correctly identifying their exposures), and quarantine compliance (traced contacts actually isolating). When any of these fail, chains go unmapped, and the data underestimates true transmission. In fast-moving outbreaks, contact tracing may become infeasible — the case burden exceeds tracing capacity — and population-level interventions must substitute. Understanding when tracing is informative and when it is overwhelmed is itself an analytical judgment central to outbreak response.
