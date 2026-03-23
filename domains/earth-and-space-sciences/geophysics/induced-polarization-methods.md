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
stage: expert
status: validated
---

# Induced Polarization and Frequency-Domain Response

## Core Idea
Induced polarization (IP) measures the polarizability of subsurface materials through frequency-dependent impedance. IP anomalies from sulfide minerals, clay minerals, and permafrost aid in ore exploration and environmental mapping.

## Questions

```yaml
- question: "A geophysicist surveys a region looking for disseminated copper sulfide mineralization. Standard resistivity measurements show no anomaly, but an IP survey reveals a strong response. Why does IP succeed where resistivity fails?"
  type: multiple-choice
  options:
    - "IP uses higher voltages that penetrate deeper, reaching ore bodies that resistivity cannot detect"
    - "Disseminated sulfides have high polarizability from electrode polarization at grain boundaries, even though they are too sparse to significantly alter bulk resistivity"
    - "Sulfide minerals are always highly resistive, which IP measures more accurately than standard methods"
    - "IP averages readings over wider areas, smoothing out the small resistivity signature of disseminated ore"
  answer: 1
  explanation: "This is the key practical insight of IP: polarizability and resistivity are independent properties. A rock body containing 1-2% disseminated sulfide minerals by volume may barely change the bulk resistivity (there isn't enough metallic mineral to form continuous conductive pathways), but the electrode polarization at each grain boundary produces a strong, measurable chargeability signal. Resistivity measures how easily current flows through the rock; IP measures how much charge the rock can store and release — a different physical property entirely. This is why IP is uniquely effective for disseminated deposit types."

- question: "In time-domain IP, when is the chargeability signal measured?"
  type: multiple-choice
  options:
    - "While the current pulse is actively flowing — measuring the enhanced conductivity of polarizable minerals"
    - "Simultaneously at two frequencies — comparing resistivity at high and low frequency"
    - "After the current is abruptly cut off — measuring the slowly decaying residual voltage"
    - "Before the current pulse — establishing a baseline that is subtracted from the active measurement"
  answer: 2
  explanation: "Chargeability in time-domain IP is the integral of the decaying voltage measured after the current is switched off. When current flows, charge accumulates at interfaces (electrode polarization at sulfide grain surfaces, membrane polarization at clay surfaces). When current stops, that stored charge slowly dissipates, producing a measurable voltage that decays over seconds. This delayed decay is the IP signal. The area under the decay curve (normalized to the applied voltage) gives chargeability. This is directly analogous to discharging a capacitor — polarizable materials act as leaky capacitors embedded in the rock."

- question: "In time-domain IP, the chargeability signal is measured from the decaying voltage that persists after the injected current is shut off."
  type: true-false
  answer: true
  explanation: "This is the defining measurement in time-domain IP. The slow voltage decay after current shutoff directly reflects the charge storage and release at interfaces in the rock. Non-polarizable rocks drop their voltage to near-zero almost instantaneously when current is cut; polarizable rocks (those with sulfide minerals, clay, or other interface-rich materials) maintain a decaying voltage for seconds. The shape and magnitude of this decay curve encodes information about the type and abundance of polarizable material in the subsurface."

- question: "Electrode polarization in IP is caused by clay minerals partially blocking ion flow through narrow pore throats."
  type: true-false
  answer: false
  explanation: "That description is membrane polarization, not electrode polarization. Electrode polarization (also called metallic or overvoltage polarization) occurs when ions moving through pore fluid encounter a metallic or sulfide mineral grain surface. The transition from ionic to electronic conduction creates a bottleneck where charge accumulates at the grain boundary. Membrane polarization is distinct — it arises from clay minerals and narrow pore throats where electrical double layers partially block ion flow. Both mechanisms produce IP signals, but electrode polarization is stronger and is the basis of sulfide mineral exploration."

- question: "Explain why IP measurements reveal properties of subsurface materials that standard resistivity measurements cannot detect."
  type: short-answer
  answer: "Resistivity measures how efficiently current flows through rock, which depends mainly on pore fluid conductivity and porosity. IP measures polarizability — the ability of the rock to store and release charge at internal interfaces. These are independent properties. A rock can have normal resistivity but high polarizability (disseminated sulfides) or high resistivity with low polarizability (dry crystalline rock). IP is sensitive to the density of charge-storing interfaces (metal grain boundaries, clay surfaces, narrow pore throats) that leave no resistivity signature."
  explanation: "The physical basis of IP is charge storage, not charge transport. Resistivity methods measure the steady-state flow of current through a conductive medium; IP methods exploit the transient behavior when that flow is disrupted — specifically, the stored charge that dissipates after current is removed. Because charge storage depends on the density and geometry of interfaces within the rock, rather than bulk conductivity, IP detects features (disseminated sulfides, clay content, permafrost character) that appear invisible to resistivity. The two methods are complementary, and modern surveys often collect both simultaneously."
```

## Explainer

From your study of electrical conductivity in crustal materials, you know that different rocks and minerals conduct electric current in different ways — some through ionic flow in pore fluids, others through electronic conduction in metallic minerals. **Induced polarization** (IP) exploits a subtler phenomenon: when current is injected into the ground and then shut off, the voltage does not drop to zero instantly. Instead, it decays slowly over seconds, as though the ground were a leaky capacitor storing and releasing charge. This delayed voltage decay reveals the **polarizability** of subsurface materials — a property that standard resistivity measurements miss entirely.

The physical mechanism behind IP involves charge accumulation at interfaces within the rock. Two main processes produce this effect. **Electrode polarization** (also called metallic or overvoltage polarization) occurs when current flows through a rock containing disseminated metallic or sulfide mineral grains. Ions moving through pore fluid encounter a metallic grain surface, and the transition from ionic to electronic conduction creates a charge buildup at the grain boundary — like a bottleneck in traffic. When the current stops, this accumulated charge slowly dissipates, producing the characteristic IP decay. **Membrane polarization** occurs in rocks with clay minerals or narrow pore throats, where the electrical double layer at grain surfaces partially blocks ion flow, creating similar charge storage effects. Electrode polarization produces stronger signals and is the basis of sulfide mineral exploration; membrane polarization is weaker but important for clay detection.

IP can be measured in two ways. In **time-domain IP**, a current pulse is injected and then abruptly cut off; the decaying voltage is recorded over time, and the **chargeability** — a measure of how much charge was stored — is calculated from the area under the decay curve. In **frequency-domain IP**, current is injected at two or more frequencies, and the apparent resistivity is measured at each. Polarizable materials show lower resistivity at higher frequencies because the alternating current partially bypasses the charge-storage bottlenecks. The **percent frequency effect** (PFE) or **metal factor** quantifies this frequency dependence. Both approaches detect the same underlying property but suit different field conditions and survey designs.

The practical value of IP is enormous in mineral exploration. Disseminated sulfide deposits — the kind that host copper, gold, zinc, and nickel — are often too sparse to produce a strong resistivity anomaly on their own, but their electrode polarization response is unmistakable. An IP survey can detect a rock body containing just 1–2% sulfide minerals by volume, making it one of the most sensitive geophysical methods for ore discovery. Beyond mining, IP methods help map clay-rich zones in environmental and geotechnical investigations, detect permafrost boundaries, and characterize contamination plumes where metallic particles or organic compounds alter the polarization response of sediments.
