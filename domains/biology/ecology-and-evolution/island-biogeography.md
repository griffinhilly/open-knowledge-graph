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

## Questions

```yaml
- question: "A conservation manager monitors a forest fragment and finds it has maintained the same number of bird species for 10 years. She concludes the community is stable and no species are at risk. What does island biogeography theory suggest she may be overlooking?"
  type: multiple-choice
  options:
    - "The species richness is artificially elevated by immigration from adjacent habitat, masking low reproductive success"
    - "Even with constant species richness, individual species are going extinct and being replaced by new colonists — turnover may be high and populations may be small and fragile"
    - "Stable species richness over 10 years proves the reserve has reached its maximum carrying capacity"
    - "The species-area relationship predicts richness should increase over time, so flat richness indicates habitat degradation"
  answer: 1
  explanation: "Island biogeography predicts a dynamic equilibrium: species richness stays approximately constant because extinction and immigration rates balance, not because the community is frozen. Individual species turn over — some go locally extinct, others colonize. The manager is observing constant richness but not individual species fates. Small populations in habitat fragments may be extinction-prone even as the total count holds steady, particularly if immigration rates are low and cannot rescue declining populations."

- question: "An oceanic island and a continental forest fragment of equal area are compared. The species-area z-value for the island is 0.30; for the fragment, it is 0.15. What best explains this difference?"
  type: multiple-choice
  options:
    - "Forest fragments support inherently fewer species per unit area than oceanic islands due to lower habitat quality"
    - "The surrounding matrix (farmland, roads) is less hostile than open ocean, allowing some dispersal across it — reducing effective isolation and lowering z"
    - "The island's higher z-value indicates greater biodiversity per unit area caused by evolutionary isolation"
    - "The species-area relationship has a different mathematical form for continental fragments and cannot be compared to oceanic islands"
  answer: 1
  explanation: "The z-value in S = cA^z captures how steeply species richness falls with decreasing area. Oceanic islands are surrounded by absolute barriers (open ocean), so small islands receive very few colonists and extinction is unrescued — species loss with decreasing area is steep (high z). Continental fragments are embedded in a traversable matrix; organisms can still disperse across farmland or roads, partially compensating for fragmentation. This reduces effective isolation, softens the extinction rate increase with decreasing area, and produces lower z-values (~0.15 vs. ~0.30)."

- question: "According to MacArthur and Wilson's island biogeography theory, a large island close to the mainland should support more species than a small island far from the mainland, because it has both lower extinction rates and higher immigration rates."
  type: true-false
  answer: true
  explanation: "Correct. Island area depresses extinction rates: larger islands support larger populations with lower extinction risk. Proximity to the mainland elevates immigration rates: colonists reach nearby islands more frequently. Both factors push species richness upward. The equilibrium species count is therefore highest for large, close islands and lowest for small, remote islands — a testable prediction confirmed by empirical data from many archipelagos."

- question: "Island biogeography theory predicts that once a habitat fragment reaches its equilibrium species richness, no individual species will go locally extinct as long as area and isolation remain constant."
  type: true-false
  answer: false
  explanation: "The equilibrium is dynamic, not static. At equilibrium, the immigration rate and extinction rate are equal, meaning species continue to go extinct and arrive at matching rates. The richness count is stable, but the identities of the species present change over time — this is species turnover. MacArthur and Wilson's own field experiments on Florida mangrove islands confirmed rapid turnover: they defaunated islands and watched species counts recover to predicted equilibria, but the specific species differed from the originals."

- question: "Explain the dynamic equilibrium at the heart of MacArthur and Wilson's island biogeography theory, and describe one implication this has for how we should interpret stable species richness in a nature reserve."
  type: short-answer
  answer: "MacArthur and Wilson proposed that species richness on islands is not a fixed property but a balance point between two opposing rates: immigration (new species arriving from a source pool) and local extinction (established species dying out). As richness increases, the immigration rate of new species falls (fewer unrepresented species left to arrive) while the extinction rate rises (more species competing for resources). Where these curves cross, richness reaches an equilibrium. Crucially, this equilibrium is dynamic — species continue to go extinct and be replaced by new colonists, so total count stays constant but individual species turn over. For conservation: stable species richness in a reserve does not mean the species are secure. If immigration from surrounding habitat is cut off, extinction events will not be rescued by recolonization, and richness will eventually decline even if no immediate change is visible."
  explanation: "The hotel analogy captures it well: constant occupancy doesn't mean the same guests — people check in and out continuously. For reserves, turnover matters because small populations going locally extinct may represent the loss of irreplaceable biodiversity even when the species count temporarily holds steady."
```

## Explainer

You already know from population ecology that populations grow, shrink, and go extinct depending on birth, death, immigration, and emigration rates. Island biogeography takes this logic and applies it at the community level: instead of tracking one population's size, it tracks how many *species* persist on an island by modeling two opposing flows — the rate at which new species arrive (**immigration**) and the rate at which established species disappear (**local extinction**). Where these two rates balance, species richness reaches a dynamic equilibrium. The key insight is that this equilibrium is not static — species are constantly arriving and going extinct — but the total number stays roughly constant, like a hotel where guests check in and out but occupancy hovers around the same level.

Two geographic features drive the model's predictions. **Island area** affects extinction rate: larger islands support bigger populations with lower extinction risk, so large islands accumulate more species. **Distance from the mainland** (or source pool) affects immigration rate: nearby islands receive colonists more frequently, so they too accumulate more species. The interaction of these two factors generates a testable prediction matrix — a large, close island will be the richest; a small, remote island the poorest — and decades of empirical data from archipelagos worldwide confirm the pattern.

The **species-area relationship** (S = cA^z) quantifies one half of this framework. When you plot log(species) against log(area), you get a straight line whose slope z captures how steeply richness increases with area. For oceanic islands, z is typically around 0.25–0.35; for habitat patches embedded in a continent, z is lower (~0.15) because the surrounding matrix is not as hostile as open ocean — organisms can still disperse across it. This difference in z-values directly connects island biogeography to conservation biology: a forest fragment surrounded by farmland behaves like a continental "island" with moderate isolation, while a mountaintop sky island or a lake surrounded by desert behaves more like an oceanic island.

The theory's greatest practical impact is in **conservation planning**. Every habitat fragment — a national park, a wetland remnant, a patch of old-growth forest — is an ecological island. The theory predicts that reducing a reserve's area will increase local extinction rates, and that isolated reserves will receive fewer recolonists to rescue declining populations. This drives the design principles you encounter in conservation biology: larger reserves are better than smaller ones, connected reserves outperform isolated ones, and corridors between fragments can function like stepping-stone islands that boost effective immigration. The theory does have limits — it treats all species as equivalent and ignores habitat diversity — but its core logic of balancing immigration against extinction remains one of the most powerful frameworks in ecology.
