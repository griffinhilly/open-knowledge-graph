---
id: diel-vertical-migration-plankton
title: 'Diel Vertical Migration in Zooplankton: Behavior and Biogeochemistry'
domain: earth-and-space-sciences
course: oceanography
prerequisites:
- id: photic-zone-light-ocean-penetration
  type: hard
- id: zooplankton-food-web-structure
  type: hard
- id: ocean-temperature-structure-thermocline
  type: soft
builds-toward:
- mesopelagic-zone-ecology
- marine-biological-pump
tags:
- diel-migration
- zooplankton
- predation-avoidance
- active-transport
- visual-predation
stage: formal-systems
status: validated
---

# Diel Vertical Migration in Zooplankton: Behavior and Biogeochemistry

## Core Idea
Zooplankton ascend to surface waters at night to feed on abundant phytoplankton, then descend to depth during the day to avoid visual predators. This behavior creates the largest animal migration on Earth by biomass and drives significant vertical energy and nutrient transport (active transport), moving carbon and sustaining deep-sea communities independent of sinking particles.

## How It's Best Learned
Use acoustic data to track the deep scattering layer throughout diel cycles. Measure gut content and energy reserves in zooplankton collected at different times and depths. Model predation risk and feeding benefits to explain migration patterns and amplitude.

## Common Misconceptions
Diel migration is not a simple day-night toggle; it is more nuanced (twilight-triggered, ontogenetic shifts) and varies with moon phase and local predation pressure. Not all zooplankton migrate; large copepods and some euphausiids show smaller amplitudes. Migration is energetically costly; it represents a trade-off between feeding and predation avoidance.

## Questions

```yaml
- question: "What triggers zooplankton to begin ascending toward the surface at dusk?"
  type: multiple-choice
  options:
    - "An absolute light intensity threshold — when ambient light falls below a fixed lux level, ascent begins"
    - "Water temperature changes at the thermocline as the surface cools in the evening"
    - "The rate of change of light intensity at twilight, rather than an absolute light level"
    - "Chemical signals from phytoplankton that become detectable when light decreases"
  answer: 2
  explanation: "Diel vertical migration is triggered by the rate of change of light intensity at twilight, not by crossing an absolute light threshold. This distinction matters: it explains why migration timing shifts seasonally (twilight occurs at different absolute light intensities across seasons) and why the system is adaptive rather than merely reflexive. Responding to rate of change rather than absolute level allows zooplankton to consistently anticipate the transition from the risky daylit period to safer darkness, regardless of overall light conditions on a given day."

- question: "Larger zooplankton tend to migrate deeper during the day than smaller species. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "Larger organisms have more fat reserves and can sustain longer migrations without feeding"
    - "Larger organisms are more conspicuous to visual predators and therefore gain more survival benefit from seeking darker depths"
    - "Larger organisms produce more metabolic heat and must descend to cooler water to regulate temperature"
    - "Smaller organisms cannot survive the pressure at greater depths and are constrained to shallower water"
  answer: 1
  explanation: "Visual predators like fish and seabirds hunt by detecting zooplankton against background light. Larger, more visually conspicuous organisms are easier to detect and face higher predation risk in lit water. They gain more survival benefit from migrating to darker, deeper water during the day. Smaller species may be less detectable and tolerate shallower daytime depths or may not migrate at all. This size-gradient in migration depth is consistent with the predation-avoidance interpretation of DVM."

- question: "Diel vertical migration is triggered when ambient light intensity falls below a fixed absolute threshold that zooplankton can detect."
  type: true-false
  answer: false
  explanation: "The trigger is the rate of change of light intensity at twilight, not an absolute threshold. An absolute threshold would cause problems as seasons change, since twilight occurs at varying absolute light levels. A rate-of-change trigger ensures that migration consistently tracks the actual day-night transition regardless of season or cloud cover. It also explains behavioral nuances like migration suppression on bright full-moon nights, when the light change pattern at dusk is altered by moonrise."

- question: "Diel vertical migration actively transports carbon to depth, contributing to the ocean's biological pump beyond the passive sinking of dead organic particles."
  type: true-false
  answer: true
  explanation: "When zooplankton feed at the surface and descend to depth, they carry carbon with them in their bodies, guts, and as fecal pellets released below the photic zone. This active transport delivers organic carbon directly to the mesopelagic zone, bypassing the slow sinking process of the passive biological pump. Estimates suggest DVM-driven active transport accounts for 15–40% of total downward carbon flux in some ocean regions — a substantial contribution that would be missed if only passive particle sinking were considered."

- question: "Explain the core evolutionary trade-off that drives diel vertical migration, and why the energy cost of migrating hundreds of meters twice daily does not prevent this behavior."
  type: short-answer
  answer: "Zooplankton face a fundamental dilemma: food (phytoplankton) is in the sunlit surface water, but so are visual predators. DVM resolves this by separating feeding (surface, at night) from the high-predation-risk period (surface, during daylight). The energy cost of migration — estimated at 10–30% of daily energy budget — is outweighed by the survival benefit in environments where predation pressure is high. Natural selection favors migrators when the mortality cost of remaining near the surface during the day exceeds the metabolic cost of descending."
  explanation: "This is a classic life-history trade-off between energy acquisition and predation risk. The behavior is maintained when predation pressure is high enough that the survival benefit of the deep refuge outweighs the energetic cost of migration. Where predation pressure is low, migration frequency and amplitude are reduced — supporting the predation-avoidance interpretation. The behavioral flexibility seen across species, life stages, and moon phases shows that DVM is an adaptive optimum continuously tuned to local conditions, not a rigid fixed program."
```

## Explainer

From your study of the photic zone, you know that sunlight penetrates only the upper 200 meters or so of the ocean, and that this well-lit layer is where nearly all photosynthesis — and therefore nearly all primary food production — occurs. From your study of zooplankton food web structure, you know that zooplankton are the crucial link between phytoplankton and higher trophic levels. The dilemma facing zooplankton is stark: the food is at the surface, but so are the predators. **Diel vertical migration** (DVM) is evolution's solution to this problem, and it constitutes the largest synchronized animal movement on Earth.

Every evening at twilight, vast populations of copepods, euphausiids (krill), and other zooplankton begin ascending from depths of 200–1,000 meters toward the surface. They feed on phytoplankton through the night, then descend back to depth before dawn. The trigger is light intensity — specifically the rate of change of light at twilight, not an absolute threshold. The logic is straightforward: **visual predators** like fish and seabirds hunt by sight. By occupying the dark mesopelagic zone during daylight hours, zooplankton become nearly invisible to these predators. The energy cost of swimming hundreds of meters twice daily is substantial — estimates suggest migration can consume 10–30% of a zooplankter's daily energy budget — but the survival benefit outweighs the cost in environments where predation pressure is high.

The migration is not uniform across species, sizes, or life stages. You might expect from the thermocline structure you studied that migrating through a sharp temperature gradient imposes metabolic costs — and it does. Larger, more conspicuous zooplankton tend to migrate deeper (they are more visible to predators), while smaller species may not migrate at all. Juvenile stages often migrate differently than adults, and migration amplitude varies with moon phase: on bright, full-moon nights, some species descend deeper or reduce migration because moonlight extends the visual hunting window for predators. This behavioral plasticity shows that DVM is not a rigid program but an adaptive response continually tuned to the local predation landscape.

The biogeochemical consequences of DVM are profound. When zooplankton feed at the surface and then descend to depth, they carry carbon with them — in their guts, in their bodies, and as fecal pellets released at depth. This **active transport** of carbon bypasses the slow sinking of dead organic particles (the passive biological pump) and delivers carbon directly to the mesopelagic and bathypelagic zones, where it can be sequestered for decades to centuries. Estimates suggest that DVM-driven active transport accounts for 15–40% of total downward carbon flux in some ocean regions. The migrators also excrete dissolved nutrients (ammonium, phosphate) at depth, fueling microbial communities far below the sunlit layer. Without this nightly conveyor belt, deep-ocean ecosystems would be significantly less productive, and the ocean's role in the global carbon cycle would be diminished.
