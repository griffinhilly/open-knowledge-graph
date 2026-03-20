---
id: passive-active-surveillance-systems
title: Passive vs. Active Disease Surveillance
domain: health-and-human-development
course: public-health
prerequisites:
- id: disease-surveillance-systems
  type: hard
builds-toward:
- outbreak-investigation
- infectious-disease-surveillance
tags:
- surveillance
- disease-monitoring
- systems
stage: advanced
status: draft
---

# Passive vs. Active Disease Surveillance

## Core Idea
Passive surveillance relies on healthcare providers voluntarily reporting cases to public health authorities; active surveillance has public health officials proactively contacting providers to collect data. Passive systems are less resource-intensive but miss many cases and detect outbreaks late. Active systems detect outbreaks earlier but require dedicated resources. Most effective surveillance combines both approaches, with active surveillance focused on serious, unusual, or outbreak-related diseases.

## How It's Best Learned
Review surveillance data for a notifiable disease and compare case counts between passive and active surveillance periods.

## Common Misconceptions
Thinking passive surveillance provides complete case counts—it consistently misses cases. Not recognizing that active surveillance is cost-prohibitive for all diseases.

## Explainer

Your foundation in disease surveillance systems established why systematic case detection matters: without knowing where disease is occurring, public health cannot respond efficiently. The passive versus active distinction is essentially about who does the work of finding cases — and that structural difference has large consequences for data quality, timeliness, and cost.

**Passive surveillance** describes the default infrastructure most countries use for routine notifiable disease reporting. A physician diagnoses measles, fills out a report form, and sends it to the local health department. The information flows upward spontaneously, but only when clinicians remember to report, have time to do so, and correctly diagnose the condition. Each of those three conditions fails routinely. Studies comparing passive surveillance counts to active case-finding surveys consistently find that passive systems capture only a fraction of true cases — often 10–50% — a gap called **under-ascertainment**. For diseases with mild or non-specific presentations (early HIV, many foodborne illnesses), the fraction is even lower because many cases never reach a healthcare provider at all, much less trigger a report.

**Active surveillance** reverses the information flow. Instead of waiting for reports to arrive, public health officials proactively contact providers, laboratories, hospitals, or community members to ask about cases. During an outbreak investigation of Salmonella, for example, an active surveillance team might call every lab in the region weekly, request line lists of all Salmonella-positive stool cultures, and cross-reference them with restaurant exposure data. This approach dramatically increases case ascertainment and shortens the time between case occurrence and detection. The tradeoff is cost: active surveillance requires dedicated staff making outgoing contacts, which is not sustainable at scale for hundreds of diseases simultaneously.

The practical architecture of disease surveillance programs reflects this tradeoff. Most countries maintain **passive surveillance for all notifiable diseases** (a large list of conditions that providers are legally required to report) while deploying **active surveillance selectively** for high-priority scenarios: emerging or novel diseases (early COVID-19), outbreak investigations, diseases targeted for elimination (polio, measles), or sentinel surveillance at specially designated sites that provide early warning signals. **Sentinel surveillance systems** — networks of a few hundred hospitals or clinics that actively report specific syndromes — provide a middle path: deeper data quality than pure passive reporting without the cost of universal active surveillance. Understanding which system generated a particular dataset is essential for interpreting its completeness and deciding what inferences it can support.
