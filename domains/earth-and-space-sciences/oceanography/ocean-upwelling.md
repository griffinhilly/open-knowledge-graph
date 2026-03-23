---
id: ocean-upwelling
title: 'Ocean Upwelling: Coastal and Equatorial'
domain: earth-and-space-sciences
course: oceanography
prerequisites:
- id: wind-driven-ocean-circulation
  type: hard
- id: ocean-layering-and-stratification
  type: hard
- id: ocean-gyres-and-boundary-currents
  type: soft
builds-toward:
- marine-primary-productivity
- el-nino-southern-oscillation
tags:
- upwelling
- coastal upwelling
- Ekman divergence
- equatorial upwelling
- cold tongue
stage: formal-systems
status: validated
---

# Ocean Upwelling: Coastal and Equatorial

## Core Idea
Upwelling occurs when surface water is pushed away from a region (by Ekman transport) and replaced by colder, nutrient-rich water from depth. Coastal upwelling occurs along eastern ocean boundaries when equatorward winds drive surface water offshore; this is responsible for the high biological productivity of systems like the California, Humboldt, and Benguela currents. Equatorial upwelling results from the divergence of Ekman transport on either side of the equator driven by trade winds. Upwelling regions sustain some of the world's most productive fisheries but are highly sensitive to wind changes.

## How It's Best Learned
Trace the Ekman transport vectors for a coast with equatorward winds (Northern Hemisphere) and confirm offshore direction, then identify the compensating upwelling. Connect upwelling suppression during El Niño to the collapse of equatorial cold tongue.

## Common Misconceptions
- Upwelling zones are not caused by deep currents pushing up — they are caused by surface divergence creating a void that deeper water fills.
- Cold surface temperatures in upwelling zones are counterintuitively associated with high marine productivity, not hostile conditions.

## Questions

```yaml
- question: "Coastal upwelling along the western coast of South America is primarily caused by which mechanism?"
  type: multiple-choice
  options:
    - "Deep ocean currents pushing cold water upward along the continental shelf"
    - "Equatorward trade winds driving surface water offshore via Ekman transport, creating a void that deeper water fills"
    - "Temperature differences between coastal and open ocean water creating density-driven upward flow"
    - "The continental shelf acting as a ramp that deflects deep currents toward the surface"
  answer: 1
  explanation: "Upwelling is driven from the top down, not the bottom up. Equatorward trade winds drive Ekman transport at 90° to the wind direction — in the Southern Hemisphere, to the left, which is offshore. As surface water is removed from the coast, it cannot be replaced from the land side, so colder, nutrient-rich water from 100–300 m depth rises to fill the deficit. The deep water is not being pushed; it is drawn upward to replace the diverging surface layer. This distinction — surface divergence pulling water up vs. deep currents pushing up — is the key conceptual point."

- question: "During a strong El Niño event, trade winds across the tropical Pacific weaken substantially. A biologist monitoring the eastern equatorial Pacific observes that primary productivity drops dramatically. What is the most direct physical explanation?"
  type: multiple-choice
  options:
    - "Warmer sea surface temperatures lower oxygen solubility, suffocating phytoplankton"
    - "Weakened trade winds reduce Ekman divergence at the equator, suppressing upwelling and cutting off the nutrient supply from depth"
    - "El Niño shifts rainfall patterns, diluting surface salinity and disrupting phytoplankton growth"
    - "Stronger stratification during El Niño prevents phytoplankton from reaching sunlit surface waters"
  answer: 1
  explanation: "Equatorial upwelling is driven by trade winds pushing surface water poleward away from the equator (Ekman divergence in opposite directions on either side). When the trade winds weaken during El Niño, this divergence diminishes, upwelling slows, and the nutrient supply from depth is cut off. Warm, nutrient-depleted water spreads across the tropical Pacific, phytoplankton productivity collapses, and the food web from zooplankton to fish to seabirds is affected. The El Niño of 1972 devastated Peru's anchovy industry through exactly this mechanism."

- question: "Coastal upwelling zones are among the ocean's most biologically productive regions, in part because the cold water they bring to the surface is rich in nutrients that have accumulated from decomposing organic matter at depth."
  type: true-false
  answer: true
  explanation: "Cold surface temperatures in upwelling zones are counterintuitive — students often associate warm tropical waters with productivity — but the relationship is inverted here. Deep water is cold because it has been isolated from solar heating. It is nutrient-rich because organic particles sinking from the surface have been decomposing at depth (remineralization), releasing nitrate, phosphate, and silicate back into solution. When upwelling brings this water to the sunlit euphotic zone, phytoplankton have both light and nutrients, driving the explosive blooms that make upwelling systems like the Humboldt Current among the world's most productive fisheries."

- question: "Ocean upwelling is driven by deep currents actively pushing cold water upward toward the surface."
  type: true-false
  answer: false
  explanation: "Upwelling is driven by surface divergence, not by deep currents pushing upward. When wind-driven Ekman transport removes surface water from a region — offshore along a coast or poleward on either side of the equator — it creates a deficit. Deeper water is drawn upward passively to fill the void, much as water rises in a straw when you remove your thumb. The energy source is atmospheric wind transmitted to the surface ocean; the deep water responds to the pressure gradient created by surface removal. This explains why upwelling stops when winds weaken — the driving force is atmospheric, not oceanic."

- question: "Explain why equatorial upwelling occurs in the open ocean far from any coastline, using the Coriolis effect and Ekman transport in your answer."
  type: short-answer
  answer: "The trade winds blow westward across the equatorial ocean. Because the Coriolis effect deflects moving water to the right in the Northern Hemisphere and to the left in the Southern, Ekman transport carries surface water northward just north of the equator and southward just south of it. This creates a divergence: surface water is being removed from the equatorial band in both directions simultaneously. With no coastline to prevent inflow, deeper nutrient-rich water rises to replace the departing surface layer, producing the 'cold tongue' of cool, productive water visible in sea-surface temperature maps of the equatorial Pacific."
  explanation: "The Coriolis effect reverses sign exactly at the equator, making the equatorial band a location where symmetric Ekman transport naturally creates divergence. This is why the equatorial cold tongue exists thousands of kilometers from any coast. The same physical principle operates at coastlines, but there the continent plays the role the Coriolis reversal plays at the equator — preventing lateral inflow and forcing compensation from depth."
```

## Explainer

From your study of wind-driven ocean circulation, you know that wind stress on the ocean surface does not push water directly downwind — the Coriolis effect deflects it, producing **Ekman transport** at 90 degrees to the wind direction (to the right in the Northern Hemisphere, to the left in the Southern). Upwelling is what happens when this transport moves surface water away from a coast or away from the equator, and deeper water rises to fill the gap. The mechanism is elegantly simple, but its consequences for marine ecosystems and climate are enormous.

Consider the classic case of **coastal upwelling** along the west coast of South America. The prevailing trade winds blow toward the equator, parallel to the coastline. Ekman transport pushes the surface water offshore — to the left of the wind in the Southern Hemisphere. As surface water moves away from the coast, it creates a deficit that cannot be filled from the land side, so water from depths of 100–300 meters rises to replace it. This deep water is cold because it has been isolated from solar heating, and it is nutrient-rich because organic matter sinking from the surface has been decomposing at depth, releasing nitrate, phosphate, and silicate back into solution. When this water reaches the sunlit surface, phytoplankton explode in abundance, fueling food webs that support some of the world's most productive fisheries — the Humboldt Current off Peru being the most dramatic example.

**Equatorial upwelling** operates on a similar principle but with a different geometry. The trade winds blow westward across the tropical ocean. Because the Coriolis effect reverses direction across the equator, Ekman transport pushes surface water northward just north of the equator and southward just south of it — a divergence that pulls deep water upward right along the equatorial band. This is why satellite images of sea-surface temperature show a conspicuous **cold tongue** stretching westward along the equatorial Pacific. The nutrients brought up by equatorial upwelling sustain elevated primary productivity across a vast stretch of open ocean.

Upwelling regions are highly sensitive to changes in wind forcing. During **El Niño** events, the trade winds weaken or reverse across the tropical Pacific, suppressing equatorial upwelling and allowing warm, nutrient-poor surface water to spread eastward. The cold tongue disappears, primary productivity plummets, and fisheries collapse — the El Niño of 1972 devastated Peru's anchovy industry and reshaped global understanding of ocean-atmosphere coupling. Along coastlines, seasonal shifts in wind patterns turn upwelling on and off, creating pronounced seasonal cycles in productivity. Understanding upwelling is therefore not just an exercise in physical oceanography — it is essential for predicting fishery yields, carbon cycling, and the regional climate effects of cold surface waters interacting with overlying atmospheric circulation.
