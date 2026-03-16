---
id: induced-polarization-methods
title: Induced Polarization and Frequency-Domain Response
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: electrical-conductivity-crustal
  type: hard
tags:
- induced-polarization
- ip
- frequency-domain
stage: advanced
status: draft
---

# Induced Polarization and Frequency-Domain Response

## Core Idea
Induced polarization (IP) measures the polarizability of subsurface materials through frequency-dependent impedance. IP anomalies from sulfide minerals, clay minerals, and permafrost aid in ore exploration and environmental mapping.

## Explainer

From your study of electrical conductivity in crustal materials, you know that different rocks and minerals conduct electric current in different ways — some through ionic flow in pore fluids, others through electronic conduction in metallic minerals. **Induced polarization** (IP) exploits a subtler phenomenon: when current is injected into the ground and then shut off, the voltage does not drop to zero instantly. Instead, it decays slowly over seconds, as though the ground were a leaky capacitor storing and releasing charge. This delayed voltage decay reveals the **polarizability** of subsurface materials — a property that standard resistivity measurements miss entirely.

The physical mechanism behind IP involves charge accumulation at interfaces within the rock. Two main processes produce this effect. **Electrode polarization** (also called metallic or overvoltage polarization) occurs when current flows through a rock containing disseminated metallic or sulfide mineral grains. Ions moving through pore fluid encounter a metallic grain surface, and the transition from ionic to electronic conduction creates a charge buildup at the grain boundary — like a bottleneck in traffic. When the current stops, this accumulated charge slowly dissipates, producing the characteristic IP decay. **Membrane polarization** occurs in rocks with clay minerals or narrow pore throats, where the electrical double layer at grain surfaces partially blocks ion flow, creating similar charge storage effects. Electrode polarization produces stronger signals and is the basis of sulfide mineral exploration; membrane polarization is weaker but important for clay detection.

IP can be measured in two ways. In **time-domain IP**, a current pulse is injected and then abruptly cut off; the decaying voltage is recorded over time, and the **chargeability** — a measure of how much charge was stored — is calculated from the area under the decay curve. In **frequency-domain IP**, current is injected at two or more frequencies, and the apparent resistivity is measured at each. Polarizable materials show lower resistivity at higher frequencies because the alternating current partially bypasses the charge-storage bottlenecks. The **percent frequency effect** (PFE) or **metal factor** quantifies this frequency dependence. Both approaches detect the same underlying property but suit different field conditions and survey designs.

The practical value of IP is enormous in mineral exploration. Disseminated sulfide deposits — the kind that host copper, gold, zinc, and nickel — are often too sparse to produce a strong resistivity anomaly on their own, but their electrode polarization response is unmistakable. An IP survey can detect a rock body containing just 1–2% sulfide minerals by volume, making it one of the most sensitive geophysical methods for ore discovery. Beyond mining, IP methods help map clay-rich zones in environmental and geotechnical investigations, detect permafrost boundaries, and characterize contamination plumes where metallic particles or organic compounds alter the polarization response of sediments.
