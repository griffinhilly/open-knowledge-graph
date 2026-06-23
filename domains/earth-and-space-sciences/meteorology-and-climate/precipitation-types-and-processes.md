---
id: precipitation-types-and-processes
title: Precipitation Types and Formation Processes
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: cloud-formation-and-types
  type: hard
- id: air-masses-and-fronts
  type: soft
- id: phase-transitions
  type: soft
- id: clouds-and-rain
  type: soft
- id: humidity-and-precipitation
  type: soft
builds-toward:
- thunderstorms-and-lightning
- severe-weather-systems
tags:
- rain
- snow
- sleet
- hail
- Bergeron-process
- coalescence
stage: formal-systems
status: validated
---

# Precipitation Types and Formation Processes

## Core Idea
Precipitation forms through two main processes: the Bergeron-Findeisen process in cold clouds where ice crystals grow at the expense of supercooled water droplets, and collision-coalescence in warm clouds where droplets collide and merge until heavy enough to fall. Precipitation type at the surface depends on the temperature profile of the air column below the cloud: rain falls through entirely above-freezing air; snow when the column is below freezing throughout; sleet forms when snow melts then refreezes in a cold layer near the surface; freezing rain occurs when snow melts but the surface layer is too thin to refreeze the drops in the air. Hail forms in strong updrafts in thunderstorms where ice embryos cycle repeatedly through the cumulonimbus.

## How It's Best Learned
Draw temperature profiles for each precipitation type and trace the water phase through each layer. Compare warm-process versus cold-process clouds using real tropical versus mid-latitude examples.

## Common Misconceptions
- Sleet and freezing rain are opposite situations, not synonyms — sleet refreezes in the air, freezing rain refreezes on contact with the surface.
- Large raindrops do not look like teardrops; they are spherical or flattened oblate spheroids.
- Snow does not require temperatures below 0°C at the surface to reach the ground — falling snow can survive briefly in slightly above-freezing air.

## Questions

```yaml
- question: "Snow falls from a cloud, passes through a warm layer (above 0°C) aloft where it melts, then descends through a deep cold layer (below 0°C) near the surface. What precipitation type reaches the ground?"
  type: multiple-choice
  options:
    - "Sleet — the melted drops refreeze into ice pellets while still in the air above the surface"
    - "Freezing rain — the drops arrive as liquid and refreeze on contact with cold surfaces"
    - "Snow — the cold near-surface layer causes the drops to re-solidify back into snowflakes"
    - "Rain — once snow melts into liquid water, it cannot refreeze before reaching the ground"
  answer: 0
  explanation: "This temperature profile — warm layer aloft, deep cold layer below — produces sleet. The snow melts in the warm layer, then has sufficient time falling through the thick cold layer to refreeze into ice pellets before landing. Freezing rain (option B) requires a thin near-surface cold layer — too shallow for in-air refreezing, so drops arrive liquid and freeze on contact. The depth of the near-surface cold layer is the key variable distinguishing sleet from freezing rain."

- question: "In a mixed-phase cloud containing both ice crystals and supercooled liquid droplets at the same subfreezing temperature, why do ice crystals grow at the expense of the liquid droplets?"
  type: multiple-choice
  options:
    - "The saturation vapor pressure over ice is lower than over liquid water, so the air is simultaneously supersaturated with respect to ice and undersaturated with respect to liquid, causing ice to grow and droplets to evaporate"
    - "Ice crystals fall faster than droplets and sweep them up by collision and coalescence"
    - "Liquid droplets transfer latent heat to ice crystals on contact, freezing the droplets"
    - "Ice crystals have greater surface area per unit mass than droplets, allowing faster vapor absorption"
  answer: 0
  explanation: "The Bergeron-Findeisen process exploits a physical asymmetry: at any given subfreezing temperature, equilibrium vapor pressure over liquid water is higher than over ice. When both phases coexist, air reaches a vapor pressure between the two equilibrium values — supersaturated with respect to ice (ice grows by deposition) but simultaneously undersaturated with respect to liquid water (droplets evaporate). Mass is transferred from liquid droplets to ice crystals through the vapor phase. Option B describes collision-coalescence, which is a separate mechanism operating in warm clouds."

- question: "Sleet and freezing rain are essentially the same phenomenon — both occur when precipitation refreezes near the surface."
  type: true-false
  answer: false
  explanation: "Sleet and freezing rain differ in where refreezing occurs. Sleet (ice pellets) forms when melted precipitation refreezes in the air before reaching the ground — the near-surface cold layer is deep enough to accomplish this. Freezing rain forms when that cold layer is too thin for in-air refreezing; drops arrive as liquid and freeze on contact with cold surfaces. This distinction matters practically: freezing rain creates invisible glaze ice on roads and power lines, making it far more dangerous than the visible pellets of sleet."

- question: "Large raindrops falling from mature storm clouds are typically teardrop-shaped — pointed at the top and rounded at the bottom due to air resistance."
  type: true-false
  answer: false
  explanation: "Despite being the intuitive image, large raindrops are not teardrop-shaped. Small drops are nearly spherical; larger drops are flattened into oblate spheroids (like a hamburger bun) due to air pressure on the falling drop's underside. True teardrop shapes do not occur — drops that grow too large break apart into smaller spherical drops rather than maintaining a teardrop form. The teardrop misconception is perpetuated by diagrams and logos, not by physics."

- question: "Why is freezing rain generally more hazardous than sleet, even though both involve precipitation associated with subfreezing temperatures near the surface?"
  type: short-answer
  answer: "Freezing rain arrives as liquid water and freezes on contact with objects, forming a continuous, transparent glaze of ice that coats roads, sidewalks, power lines, and tree branches. This glaze is difficult to see (especially 'black ice' on pavement) and extremely slippery. Sleet arrives as already-frozen ice pellets that bounce and pile up — still slippery, but more visible and less prone to uniformly coating surfaces. Freezing rain also accumulates weight on power lines and branches, causing widespread infrastructure damage from line breaks and falling trees."
  explanation: "The physical difference — liquid that freezes on contact versus solid pellets — produces entirely different hazard profiles. Freezing rain creates a uniform ice surface across all exposed infrastructure simultaneously, while sleet creates discrete accumulations. Major ice storms, like the 1998 North American Ice Storm that devastated the Canadian power grid, are caused by extended freezing rain, not sleet — illustrating how thin, invisible ice layers can cause catastrophic damage well beyond their apparent severity."
```

## Explainer

You know from cloud formation that water vapor condenses onto nuclei to form cloud droplets, but those tiny droplets — typically 10–20 micrometers across — are far too small to fall as rain. Something must make them grow by a factor of a million in volume before they become precipitation. The atmosphere uses two fundamentally different growth mechanisms depending on cloud temperature, and understanding both is the key to predicting what falls from the sky.

In warm clouds (entirely above 0°C, common in the tropics), the **collision-coalescence process** does the work. Larger droplets fall faster than smaller ones, sweeping them up in a chain reaction. A droplet that starts slightly larger — perhaps because it formed on a giant sea-salt nucleus — collects smaller droplets as it descends through the cloud, growing rapidly until it is heavy enough to fall as rain. This process is efficient in deep, warm, maritime clouds where droplets are large and varied in size, but it struggles in thin or continental clouds where droplets are numerous but uniformly small.

In cold clouds (with temperatures below 0°C, which includes most mid-latitude precipitation-producing clouds), the **Bergeron-Findeisen process** dominates. This mechanism exploits a remarkable physical asymmetry: the saturation vapor pressure over ice is lower than over liquid water at the same subfreezing temperature. When ice crystals and supercooled water droplets coexist in a cloud, the air can be supersaturated with respect to ice while undersaturated with respect to liquid water. The ice crystals grow by vapor deposition while the liquid droplets evaporate, effectively transferring mass from droplets to ice crystals. The crystals grow into snowflakes, which may aggregate into larger flakes or acquire a coating of supercooled water (riming) as they fall.

What reaches the ground depends entirely on the **temperature profile** of the air below the cloud. If temperatures stay below freezing from cloud to surface, snow reaches you. If the entire column below the cloud is above freezing, snow melts into rain. The interesting cases involve layered temperature profiles. If snow falls through a warm layer aloft (above 0°C) that melts it into rain, and then enters a deep cold layer near the surface (below 0°C), the rain refreezes into ice pellets — **sleet**. But if that near-surface cold layer is too shallow for the drops to refreeze in mid-air, they arrive at the surface as liquid and freeze on contact with cold objects — **freezing rain**, one of the most hazardous precipitation types. **Hail** follows a different path entirely: strong thunderstorm updrafts loft ice embryos repeatedly through the cloud, where each pass adds a new layer of ice until the stone is too heavy for the updraft to support and it falls to the ground.
