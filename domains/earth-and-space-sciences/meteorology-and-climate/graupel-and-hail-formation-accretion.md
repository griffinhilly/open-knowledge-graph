---
id: graupel-and-hail-formation-accretion
title: Graupel and Hail Formation Through Accretion
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: bergeron-process-ice-precipitation
  type: hard
- id: latent-heating-in-weather-systems
  type: hard
builds-toward:
- severe-weather-dynamics-supercells
- severe-weather-parameter-environment
tags:
- microphysics
- severe-weather
- ice-hydrometeors
stage: advanced
status: draft
---

# Graupel and Hail Formation Through Accretion

## Core Idea
Graupel forms when ice crystals or snow particles fall through supercooled liquid water regions and rapidly accumulate ice through accretion (riming). Hail results from graupel being lofted by strong updrafts into subfreezing regions, growing additional ice layers before eventually falling. Severe weather often correlates with high graupel production and large hail, which indicates vigorous mixed-phase microphysics.

## How It's Best Learned
Examine radar signatures showing the presence of graupel (high reflectivities); relate graupel production to updraft strength and moisture availability; study vertical profiles in severe thunderstorms.

## Common Misconceptions
- Confusing graupel with hail (graupel is soft and opaque; hail is hard with concentric layers and forms in strong updrafts).
- Thinking large hail requires cold upper atmosphere (it requires strong updrafts in warm, moist environments).

## Questions

```yaml
- question: "A forecaster says: 'We don't expect large hail today because temperatures at 500 hPa are only -12°C — not cold enough to support big hailstones.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — large hail requires temperatures below -20°C at the freezing level, so -12°C is indeed too warm"
    - "Hail size is primarily determined by updraft strength and supercooled liquid water availability, not by upper-level temperatures — warm, moist environments with strong updrafts produce the largest hail"
    - "The forecaster should use 300 hPa temperatures, not 500 hPa, to diagnose hail potential"
    - "Temperature only matters for graupel formation, not for hailstone growth cycles through updrafts"
  answer: 1
  explanation: "This is the core misconception about hail formation. Large hail does not require extremely cold temperatures — it requires strong, sustained updrafts in warm, moist environments that supply abundant supercooled liquid water. The largest hailstones form in warm, humid environments (like the Great Plains) where intense latent heat release fuels updrafts exceeding 30 m/s. Cold temperatures aloft are irrelevant without the updraft strength to keep growing hailstones aloft through multiple accretion cycles."

- question: "What causes the alternating clear and opaque rings visible when a hailstone is cut in half?"
  type: multiple-choice
  options:
    - "Each ring records a separate storm event — hailstones accumulate rings over multiple thunderstorm seasons like tree rings"
    - "Clear rings form when the stone passes through ice crystal regions; opaque rings form when it passes through liquid water regions"
    - "Each growth cycle through the updraft produces one ring — clear (dense) layers from wet growth when droplets freeze slowly, opaque (bubbly) layers from dry growth when droplets freeze instantly"
    - "The alternating rings reflect temperature oscillations within the storm as the hailstone spirals through regions of different temperatures"
  answer: 2
  explanation: "Each ring records one pass through the updraft cycle. When supercooled droplet concentration is high and droplets freeze slowly (wet growth), ice grows dense and clear. When the stone is in a colder zone with lower liquid water content and droplets freeze instantly on contact (dry growth), trapped air bubbles produce opaque, white ice. A hailstone with many alternating rings has cycled through the updraft multiple times, each time adding another layer — a physical record of the storm's internal structure."

- question: "Graupel forms through riming — direct collision and immediate freezing of supercooled liquid droplets onto an ice particle — which is fundamentally different from the vapor deposition growth that dominates in the Bergeron process."
  type: true-false
  answer: true
  explanation: "True. The Bergeron process grows ice crystals through vapor deposition: water vapor migrates from supercooled liquid droplets (higher vapor pressure) to ice crystals (lower vapor pressure), depositing layer by layer. Riming (accretion) is a direct collision process: supercooled liquid droplets physically collide with the ice particle and freeze instantly on contact, creating a rough, opaque coating. Graupel is the product of dominant riming — the Bergeron mechanism is essentially bypassed in favor of rapid, violent accretionary growth."

- question: "Large hailstones require very cold temperatures throughout the storm because ice can only grow in subfreezing air, and warmer environments cannot produce large hail."
  type: true-false
  answer: false
  explanation: "False. Large hail requires strong updrafts and abundant supercooled liquid water in the mixed-phase zone — conditions that occur in warm, moist environments with intense convection, not in cold environments. The supercooled water (liquid below 0°C) exists within the cloud regardless of surface temperatures. A warm, humid environment feeds more latent heat into the updraft as water vapor condenses and freezes, producing the strongest updrafts and the most supercooled liquid water for accretion. Cold environments typically produce weaker updrafts and less liquid water supply."

- question: "Explain why hail size is a proxy for updraft strength rather than atmospheric temperature, and how the formation mechanism supports this relationship."
  type: short-answer
  answer: "Hailstones grow by repeated accretion cycles: the stone is lofted by the updraft into the supercooled liquid water zone, accumulates ice, falls, and is lofted again. Each cycle adds mass. A stronger updraft can support a heavier stone and keep it in the accretion zone longer. A stone becomes too heavy to loft only when the updraft can no longer support its weight — so the final hailstone size is limited by the maximum updraft speed. Temperature primarily controls whether the water is supercooled (available for accretion), but updraft strength determines how many growth cycles occur and how large the stone can grow."
  explanation: "The key is understanding that hail growth is a balance between gravitational settling and updraft lofting. At terminal velocity for a given size, the hailstone neither rises nor falls. To keep growing, the updraft must exceed that terminal velocity so the stone stays in the supercooled liquid zone. As the stone grows, its terminal velocity increases, eventually exceeding even the strongest updraft — at that point it falls. Stronger updrafts therefore produce larger hailstones because they sustain more growth cycles before the stone becomes too heavy. This is why large hail is a direct indicator of updraft strength used in severe weather warning."
```

## Explainer

You already know from the Bergeron process that ice crystals grow efficiently in mixed-phase clouds by consuming supercooled liquid water through a vapor pressure difference. You also know from latent heating that phase changes release energy that can strengthen updrafts. Graupel and hail formation takes these ideas a step further: instead of ice crystals growing delicately through vapor deposition, they grow violently through direct collision with supercooled droplets — a process called **accretion** or **riming**.

Picture a small ice crystal or snowflake falling through a cloud region thick with supercooled liquid droplets — water that remains liquid despite being well below 0°C. As the ice particle collides with these droplets, they freeze almost instantly on contact, coating the particle with a rough, opaque shell of ice. This is **graupel**: a rounded, soft pellet typically 2–5 mm across, looking somewhat like a small Styrofoam ball. Graupel forms rapidly because the collision-freezing mechanism is much faster than vapor deposition. If you've ever seen small white pellets bouncing off the ground during a spring thunderstorm, you've seen graupel.

**Hail** begins where graupel leaves off, but requires a crucial ingredient: a powerful updraft. In ordinary clouds, graupel simply falls to the ground once it grows heavy enough. In severe thunderstorms with updrafts exceeding 30 m/s (about 70 mph), graupel gets lofted back upward into the subfreezing zone. Each pass through the supercooled liquid water layer adds another coat of ice. If the liquid water concentration is high and the droplets freeze slowly, the ice grows clear and dense (wet growth). If the droplets freeze instantly, the layer is opaque and bubbly (dry growth). This is why cutting a hailstone in half often reveals alternating clear and opaque rings — each ring records one trip through the updraft cycle. The stone grows until it becomes too heavy for even the strongest updraft to support, then plummets to the surface.

The size of hail is therefore a direct indicator of updraft strength, not simply cold temperatures aloft. A supercell thunderstorm in the warm, humid Great Plains can produce baseball-sized hail because its updraft is sustained and intense, fed by enormous amounts of latent heat released as supercooled water freezes during accretion. This connection between microphysics and storm dynamics is why radar operators watch for high reflectivity cores aloft — they signal vigorous riming and potential hail, making graupel production a key diagnostic for severe weather warnings.
