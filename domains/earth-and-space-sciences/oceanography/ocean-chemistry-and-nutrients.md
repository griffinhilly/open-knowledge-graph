---
id: ocean-chemistry-and-nutrients
title: 'Ocean Chemistry: Nutrients, Dissolved Gases, and Buffering'
domain: earth-and-space-sciences
course: oceanography
prerequisites:
- id: seawater-properties
  type: hard
- id: acid-base-chemistry
  type: hard
- id: chemical-equilibrium
  type: soft
- id: solution-concentration
  type: soft
builds-toward:
- ocean-acidification
- marine-primary-productivity
tags:
- nutrients
- dissolved oxygen
- nitrogen cycle
- phosphorus
- marine chemistry
stage: formal-systems
status: validated
---

# Ocean Chemistry: Nutrients, Dissolved Gases, and Buffering

## Core Idea
The ocean is a complex chemical system containing dissolved gases (O₂, CO₂, N₂), major ions (Na⁺, Cl⁻, SO₄²⁻, Mg²⁺), and trace nutrients essential for life (nitrate, phosphate, silicate, iron). Nutrient concentrations are depleted in sunlit surface waters due to biological uptake and replenished in the deep ocean by decomposition of sinking organic matter — a process called the biological pump. The ocean also acts as a CO₂ buffer through the carbonate system (CO₂ ↔ H₂CO₃ ↔ HCO₃⁻ ↔ CO₃²⁻), which stabilizes ocean pH and plays a central role in the global carbon cycle.

## How It's Best Learned
Trace the path of a nitrogen atom from atmospheric N₂ through marine fixation, phytoplankton uptake, grazing, sinking, decomposition, and upwelling. Work through carbonate equilibrium calculations to understand how CO₂ addition shifts the system.

## Common Misconceptions
- Nutrient-rich waters are not necessarily more productive — light availability, iron, and mixing all interact to limit production.
- Ocean pH is not neutral — it is naturally slightly alkaline (~8.1), and 'ocean acidification' means it is becoming less alkaline, not actually acidic.

## Questions

```yaml
- question: "The ocean's natural pH is approximately 8.1. 'Ocean acidification' means the ocean's pH is doing which of the following?"
  type: multiple-choice
  options: ["Dropping toward 7.0 (neutral)", "Dropping below 7.0 into truly acidic conditions", "Becoming less basic while remaining above pH 7", "Rising toward 9 due to increased carbonate"]
  answer: 2
  explanation: "Ocean acidification describes a decrease in pH from ~8.1 toward lower values — the ocean is becoming less alkaline, not actually acidic. The term is misleading; the ocean is still basic. The drop from 8.2 to 8.1 since the industrial era represents a ~26% increase in hydrogen ion concentration, which has real biological consequences even without crossing pH 7."

- question: "Waters with the highest dissolved nutrient concentrations will always support the greatest marine biological production."
  type: true-false
  answer: false
  explanation: "Biological production depends on multiple co-limiting factors. Light availability, iron, and mixing depth interact with nutrient concentrations. Polar waters can be nutrient-rich but light-limited in winter. Parts of the Southern Ocean and equatorial Pacific are nutrient-rich but iron-limited (high-nutrient, low-chlorophyll zones). Nutrients are necessary but not sufficient for high productivity."

- question: "Why are dissolved nutrients (nitrate, phosphate) nearly depleted in surface ocean waters but elevated at depth?"
  type: short-answer
  answer: "Phytoplankton in the sunlit surface zone take up nutrients for growth. When organisms die or are grazed, their organic remains sink as particles. Bacteria decompose this material at depth, releasing nutrients back into solution. This biological pump continuously exports nutrients downward, creating a vertical gradient — depleted at the surface, enriched at depth."
  explanation: "The biological pump is the mechanism: photosynthesis consumes nutrients in the photic zone, while bacterial remineralization returns them to dissolved form in deeper, darker water. Upwelling zones (like off Peru or Antarctica) are highly productive precisely because circulation returns this nutrient-rich deep water to the surface."
```

## Explainer

You already know from acid-base chemistry that adding acid to a buffered solution shifts equilibrium rather than producing a sharp pH change. The ocean's carbonate system works on exactly this principle, but at planetary scale.

When CO₂ dissolves in seawater, it reacts with water to form carbonic acid (H₂CO₃), which dissociates into bicarbonate (HCO₃⁻) and carbonate (CO₃²⁻) ions. This linked equilibrium (CO₂ ↔ H₂CO₃ ↔ HCO₃⁻ ↔ CO₃²⁻) acts as a buffer: added CO₂ is partly consumed by converting CO₃²⁻ to HCO₃⁻, so pH changes more slowly than it would in pure water. The ocean has absorbed roughly 25–30% of human CO₂ emissions this way. But the buffering capacity is finite, and ocean pH has already dropped from about 8.2 to 8.1 since the industrial era — a small-sounding number that represents a ~26% increase in hydrogen ion concentration with real consequences for organisms that build calcium carbonate shells.

Nutrients follow a different logic. Phytoplankton at the sunlit surface take up dissolved nitrate, phosphate, and silicate to build biomass. When those organisms die or are grazed, their remains sink as organic particles and aggregates — this is the biological pump. As particles sink through the water column, bacteria break them down, releasing nutrients back into solution at depth. The result is a characteristic vertical profile: nutrient concentrations near zero at the surface and rising sharply through the thermocline to maximum values in the deep ocean. Upwelling zones like the Peruvian coast and the Southern Ocean are globally important for fisheries precisely because circulation delivers nutrient-rich deep water to the surface.

Dissolved oxygen mirrors this pattern in reverse. The surface ocean equilibrates with the atmosphere and gains oxygen from photosynthesis, keeping concentrations high. At intermediate depths, bacterial decomposition of sinking organic matter consumes oxygen, creating an oxygen minimum zone (OMZ). Below this, cold deep waters that formed at high latitudes carry high oxygen concentrations from their last contact with the atmosphere. Iron illustrates an additional complication: present at trace concentrations, it limits production across much of the open Pacific and Southern Ocean — a reminder that nutrient dynamics are not just about nitrate and phosphate.

These chemical systems set the stage for two of the most consequential topics in Earth system science: ocean acidification (the pH response to rising atmospheric CO₂) and marine primary productivity (how nutrient availability shapes biological carbon uptake). Both feed back on the global carbon cycle and therefore on climate.
