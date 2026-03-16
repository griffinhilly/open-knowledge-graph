---
id: island-biogeography
title: Island Biogeography and the Species-Area Relationship
domain: biology
course: ecology-and-evolution
prerequisites:
- id: population-ecology-intro
  type: hard
- id: speciation
  type: soft
- id: species-interactions
  type: soft
- id: exponential-functions-and-graphs
  type: soft
builds-toward:
- biodiversity-and-conservation
tags:
- island-biogeography
- species-area
- colonization
- extinction
- fragmentation
stage: formal-systems
status: validated
---
# Island Biogeography and the Species-Area Relationship

## Core Idea
MacArthur and Wilson's theory of island biogeography proposes that species richness on islands is determined by the balance between immigration (colonization from the mainland) and local extinction rates. Larger islands support more species (lower extinction rates); islands closer to the mainland have higher immigration rates. The species-area relationship (S = cAᶻ) empirically describes how species number scales with area. This theory applies beyond literal islands — habitat patches, nature reserves, and forest fragments all follow similar dynamics, making it central to conservation biology.

## How It's Best Learned
Plot species richness vs. area on log-log axes for archipelago data and calculate the z-value (slope). Compare z-values for oceanic islands (higher, ~0.3) vs. habitat patches within continents (lower, ~0.15). Apply the theory to evaluate minimum reserve size and connectivity in conservation planning.

## Common Misconceptions
- The theory predicts an equilibrium number of species, not which specific species — turnover occurs even as richness is constant.
- Island biogeography does not account for habitat heterogeneity — larger islands may have more species partly because they have more habitat types, not just area.

## Explainer

You already know from population ecology that populations grow, shrink, and go extinct depending on birth, death, immigration, and emigration rates. Island biogeography takes this logic and applies it at the community level: instead of tracking one population's size, it tracks how many *species* persist on an island by modeling two opposing flows — the rate at which new species arrive (**immigration**) and the rate at which established species disappear (**local extinction**). Where these two rates balance, species richness reaches a dynamic equilibrium. The key insight is that this equilibrium is not static — species are constantly arriving and going extinct — but the total number stays roughly constant, like a hotel where guests check in and out but occupancy hovers around the same level.

Two geographic features drive the model's predictions. **Island area** affects extinction rate: larger islands support bigger populations with lower extinction risk, so large islands accumulate more species. **Distance from the mainland** (or source pool) affects immigration rate: nearby islands receive colonists more frequently, so they too accumulate more species. The interaction of these two factors generates a testable prediction matrix — a large, close island will be the richest; a small, remote island the poorest — and decades of empirical data from archipelagos worldwide confirm the pattern.

The **species-area relationship** (S = cA^z) quantifies one half of this framework. When you plot log(species) against log(area), you get a straight line whose slope z captures how steeply richness increases with area. For oceanic islands, z is typically around 0.25–0.35; for habitat patches embedded in a continent, z is lower (~0.15) because the surrounding matrix is not as hostile as open ocean — organisms can still disperse across it. This difference in z-values directly connects island biogeography to conservation biology: a forest fragment surrounded by farmland behaves like a continental "island" with moderate isolation, while a mountaintop sky island or a lake surrounded by desert behaves more like an oceanic island.

The theory's greatest practical impact is in **conservation planning**. Every habitat fragment — a national park, a wetland remnant, a patch of old-growth forest — is an ecological island. The theory predicts that reducing a reserve's area will increase local extinction rates, and that isolated reserves will receive fewer recolonists to rescue declining populations. This drives the design principles you encounter in conservation biology: larger reserves are better than smaller ones, connected reserves outperform isolated ones, and corridors between fragments can function like stepping-stone islands that boost effective immigration. The theory does have limits — it treats all species as equivalent and ignores habitat diversity — but its core logic of balancing immigration against extinction remains one of the most powerful frameworks in ecology.
