---
id: outbreak-epidemic-curve-interpretation
title: Epidemic Curves and Outbreak Dynamics
domain: health-and-human-development
course: public-health
prerequisites:
- id: outbreak-investigation
  type: hard
- id: disease-frequency-measures
  type: hard
builds-toward:
- outbreak-transmission-models
- infectious-disease-surveillance
tags:
- outbreak
- epidemiology
- case-investigation
stage: advanced
status: draft
---

# Epidemic Curves and Outbreak Dynamics

## Core Idea
An epidemic curve displaying case count over time reveals critical information about an outbreak's source and progression. Point-source outbreaks (single exposure event) show a sudden rise and rapid decline as the susceptible population exhausts. Propagated outbreaks (person-to-person transmission) show prolonged elevation with multiple peaks as new generations of cases occur. The curve's shape indicates the incubation period length and the effectiveness of interventions.

## How It's Best Learned
Examine epidemic curves from three published outbreak investigations and determine point-source vs. propagated patterns. Calculate incubation periods from curve timing.

## Common Misconceptions
Assuming all outbreaks show exponential growth—point-source outbreaks peak quickly without intervention. Not recognizing that curve shape changes when control measures are implemented.

## Explainer

You've already studied the mechanics of outbreak investigation: defining a case, building a line list, calculating attack rates by exposure. The epidemic curve is the visual summary of that line list — case count plotted against time of symptom onset. It is one of the most information-dense displays in epidemiology, capable of revealing the type of exposure, the incubation period, and the effectiveness of control measures, all without a single statistical test.

The shape of the curve is the primary diagnostic. A **point-source** curve looks like a sharp spike: cases rise steeply, peak quickly, and fall off within a time window roughly equal to one incubation period. This pattern tells you that all cases shared a single, time-limited exposure — a contaminated food item at a catered event, a shared water supply, a single aerosol release. The rise and fall reflect the distribution of incubation periods among exposed individuals: not everyone develops symptoms at the same moment even if they were all exposed simultaneously. The rapid decline reflects exhaustion of exposed individuals: once those who were going to get sick have gotten sick, there are no new cases because the source event is over. Attack rate among those exposed, which you've already calculated using disease frequency measures, is the key statistic for diagnosing and investigating point-source outbreaks.

A **propagated** (person-to-person) curve looks different: the rise is gradual, cases persist over weeks or months, and successive waves may appear, each representing a new generation of transmission. Each infected person exposes others, who expose others — the slope reflects the reproductive number (how many people each case infects on average). The interval between peaks approximates the serial interval of the disease. Control measures show up in the curve as inflection points: if an intervention is implemented mid-outbreak, the curve bends downward from that date. This is epidemiological evidence in real time — not a controlled trial, but a visible change in trajectory that supports causation when it aligns with the intervention.

A subtlety worth mastering is the **mixed** pattern: point-source exposure followed by secondary person-to-person spread. A contaminated food item causes a spike, and then a handful of those cases infect household contacts, creating a secondary lower rise days later. Recognizing this composite pattern changes the response: you need to both remove the source and interrupt transmission simultaneously. The curve can also detect **case ascertainment artifacts**: a sudden apparent drop in cases may reflect an interruption in reporting or testing capacity rather than a true decline. Learning to read what the curve says about the process of data collection — not just the biology — is what separates experienced epidemiologists from those who read curves at face value.
