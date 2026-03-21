---
id: bergeron-process-precipitation
title: 'Bergeron Process: Ice Crystal Growth and Precipitation'
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: ice-nucleation-freezing-processes
  type: hard
- id: saturation-vapor-pressure-clausius
  type: hard
builds-toward:
- precipitation-mechanisms-coalescence
tags:
- precipitation
- microphysics
- ice-crystal
- growth
stage: advanced
status: draft
---

# Bergeron Process: Ice Crystal Growth and Precipitation

## Core Idea
The Bergeron process (ice-crystal mechanism) produces precipitation when ice crystals and supercooled droplets coexist in clouds: ice crystals have lower saturation vapor pressure than droplets, so vapor preferentially deposits on ice while droplets evaporate. Ice crystals grow rapidly to precipitation size (~100 μm), while droplets never do in competition with ice. This process dominates precipitation formation in clouds colder than −5°C.

## Questions

```yaml
- question: "In a cloud at −15°C containing both ice crystals and supercooled water droplets, what happens to the water droplets over time?"
  type: multiple-choice
  options:
    - "They continue to grow at the same rate as the ice crystals, since all condensed water behaves similarly"
    - "They evaporate, because the surrounding air is subsaturated with respect to liquid water while simultaneously supersaturated with respect to ice"
    - "They freeze spontaneously, because the temperature is far below 0°C"
    - "They collide with ice crystals and melt, contributing to raindrop formation"
  answer: 1
  explanation: "At −15°C, the saturation vapor pressure over ice is lower than over liquid water. In a mixed-phase cloud, the vapor pressure in the air lies between these two values — below what is needed to maintain liquid droplets but above what ice surfaces require. Droplets therefore evaporate (they are in undersaturated conditions relative to liquid), while ice crystals grow by vapor deposition (they are in supersaturated conditions relative to ice). Mass transfers through the vapor phase from droplets to crystals — the Bergeron process."

- question: "A student claims: 'Ice forms in clouds simply because the temperature drops below 0°C, causing all cloud droplets to freeze.' What is wrong with this explanation?"
  type: multiple-choice
  options:
    - "Cloud droplets cannot form unless the temperature is below 0°C"
    - "Supercooled liquid droplets can persist well below 0°C; the Bergeron process is driven by the vapor pressure difference between ice and liquid, not by spontaneous bulk freezing of droplets"
    - "Freezing in clouds requires temperatures below −40°C before any droplets freeze"
    - "Cloud droplets do freeze below 0°C, and the Bergeron process is just how they melt again"
  answer: 1
  explanation: "Supercooled water is remarkably common in clouds — liquid droplets routinely persist to −20°C and sometimes colder because they are small and lack efficient ice nuclei. The Bergeron process operates in this mixed-phase regime where both liquid and ice coexist. The driving force is not bulk freezing but the vapor pressure differential: ice surfaces have lower saturation vapor pressure, so the mixed-cloud environment is supersaturated for ice and subsaturated for liquid. This drives vapor deposition onto ice at the expense of evaporating droplets."

- question: "At the same subfreezing temperature, saturation vapor pressure over ice is lower than over liquid water — and this difference is what drives ice crystal growth at the expense of liquid droplets in a mixed-phase cloud."
  type: true-false
  answer: true
  explanation: "This is the physical heart of the Bergeron process. Water molecules are more tightly bound in the ice lattice than at a liquid surface, so fewer escape into the vapor phase — meaning less vapor pressure is needed to maintain equilibrium with ice than with liquid at the same temperature. In a mixed-phase cloud, the vapor pressure of the air falls between these two saturation values: too low to sustain liquid droplets (they evaporate) but too high for ice equilibrium (ice crystals grow). The vapor pressure gap is largest around −10°C to −20°C, making this the most efficient temperature range for the process."

- question: "The Bergeron process transfers water mass from liquid droplets to ice crystals by direct contact — droplets collide with ice crystals and freeze onto their surfaces."
  type: true-false
  answer: false
  explanation: "The Bergeron process operates entirely through the vapor phase. Droplets evaporate, releasing water vapor into the surrounding air; that vapor then deposits directly onto nearby ice crystals. There is no direct collision required. Direct contact freezing (riming) is a separate process — it happens as ice crystals fall and collide with supercooled droplets they encounter, and it contributes to further crystal growth after the initial Bergeron-driven growth, but it is not the Bergeron process itself."

- question: "Explain why a cloud droplet at −15°C might evaporate even though the surrounding air already contains water vapor. What property of ice versus liquid water drives this?"
  type: short-answer
  answer: "At −15°C, the saturation vapor pressure over liquid water is higher than over ice. In a cloud containing both phases, the actual vapor pressure lies between the two saturation values — above the ice saturation threshold but below the liquid water saturation threshold. From the droplet's perspective, the surrounding air is undersaturated relative to its surface (the air has less vapor than equilibrium with liquid requires), so the droplet evaporates. From the ice crystal's perspective, the air is supersaturated (it has more vapor than equilibrium with ice requires), so vapor deposits onto the crystal. The driving property is the stronger molecular bonding in the ice lattice, which reduces the equilibrium vapor pressure over ice compared to liquid at the same temperature."
  explanation: "The Bergeron process is a thermodynamic engine driven by the free energy difference between the ice and liquid phases at the same temperature. Understanding it requires recognizing that 'the air is saturated' is not a single condition — it depends on whether you are asking about equilibrium with ice or with liquid. This dual-saturation concept is why mixed-phase clouds are so effective at producing precipitation despite containing droplets that individually are too small to fall."
```

## Explainer

Most precipitation that reaches the ground in the midlatitudes begins not as rain but as ice, even in summer. Understanding why requires combining two ideas from your prerequisites: the difference in saturation vapor pressure over ice versus liquid water, and the surprising persistence of supercooled liquid droplets in clouds well below 0°C.

From the Clausius-Clapeyron relation, you know that saturation vapor pressure increases exponentially with temperature. But there is a critical detail: at the same subfreezing temperature, the **saturation vapor pressure over ice is lower than over liquid water**. This difference arises because water molecules are more tightly bound in an ice lattice than at a liquid surface, so fewer molecules escape into the vapor phase. The gap is small in absolute terms but enormous in its consequences. In a cloud containing both ice crystals and supercooled water droplets at, say, −15°C, the air can be simultaneously subsaturated with respect to liquid water and supersaturated with respect to ice.

The **Bergeron process** exploits this vapor pressure gradient. Ice crystals, sitting in air that is supersaturated relative to their surface, gain water molecules by vapor deposition and grow. Supercooled droplets, now in air that is effectively subsaturated relative to their surface, lose molecules by evaporation and shrink. The net effect is a transfer of water mass from liquid droplets to ice crystals through the vapor phase — the droplets sacrifice themselves to feed ice crystal growth. This transfer is most efficient between about −10°C and −20°C, where the vapor pressure difference between ice and liquid is greatest.

The growth rates involved are remarkable. A cloud droplet is typically 10–20 micrometers in diameter — far too small to fall as precipitation. Through the Bergeron process, an ice crystal can grow to 100 micrometers or more within minutes, reaching a size where it begins to fall. As it falls through the cloud, it may collect additional supercooled droplets by **riming** (contact freezing) or aggregate with other ice crystals, growing further into snowflakes, graupel, or hail depending on conditions. If the air below the cloud is warm enough, the ice melts into rain before reaching the surface. This is why the Bergeron process dominates precipitation in midlatitude and high-latitude clouds: most of these clouds extend above the freezing level, providing the mixed-phase environment where ice and liquid coexist and the vapor pressure differential drives efficient crystal growth.
