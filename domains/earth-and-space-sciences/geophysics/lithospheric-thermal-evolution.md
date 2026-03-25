---
id: lithospheric-thermal-evolution
title: Lithospheric Cooling and Thermal Evolution of Plates
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: conduction-models-crustal-heat
  type: hard
- id: plate-tectonics
  type: hard
- id: elastic-plate-flexure
  type: soft
- id: isostatic-flexure-lithosphere
  type: soft
tags:
- lithosphere
- cooling
- thermal-evolution
- plates
stage: expert
status: validated
---
# Lithospheric Cooling and Thermal Evolution of Plates

## Core Idea
Oceanic lithosphere cools as it ages, following half-space cooling or plate models. Temperature, density, and seismic velocity change predictably with age. Plate age variations explain bathymetry, heat flow, and isostatic structure across ocean basins and passive margins.

## Questions

```yaml
- question: "Two oceanic plates are sampled: one is 16 million years old, the other is 64 million years old. According to the half-space cooling model, how do their surface heat flows compare?"
  type: multiple-choice
  options:
    - "The 16 Ma plate has twice the heat flow of the 64 Ma plate"
    - "The 64 Ma plate has twice the heat flow of the 16 Ma plate"
    - "Their heat flows are equal because both are past the rapid cooling phase"
    - "The 16 Ma plate has four times the heat flow of the 64 Ma plate"
  answer: 0
  explanation: "In the half-space model, surface heat flow decreases as 1/√t. For the 16 Ma plate: 1/√16 = 1/4. For the 64 Ma plate: 1/√64 = 1/8. The ratio is (1/4)/(1/8) = 2, so the younger plate has twice the heat flow. The √t scaling governs both heat flow and lithospheric thickness, making age the primary control on thermal structure."

- question: "Why does the half-space cooling model overpredict both subsidence and heat flow decline for oceanic lithosphere older than about 80 Ma?"
  type: multiple-choice
  options:
    - "The half-space model ignores heat input from the asthenosphere, which prevents indefinite thickening of old plates"
    - "Old oceanic lithosphere undergoes radioactive heating that compensates for conductive cooling"
    - "The half-space model applies only to continental lithosphere; a different equation governs old oceanic plates"
    - "Sediment loading on old plates adds buoyancy that counteracts thermal subsidence"
  answer: 0
  explanation: "The half-space model assumes the lithosphere thickens without limit as cooling progresses. In reality, small-scale convection or heat flux from the underlying asthenosphere limits the thermal boundary layer thickness. The plate model corrects this by imposing a fixed temperature at the base of the lithosphere (~1300°C at ~100–125 km depth), causing heat flow and bathymetry to flatten rather than continue declining at old ages."

- question: "Mid-ocean ridges stand topographically higher than abyssal plains primarily because young, warm lithosphere is less dense than old, cold lithosphere."
  type: true-false
  answer: true
  explanation: "As oceanic lithosphere cools with age, it contracts and becomes denser. Isostasy requires that denser material sinks lower. Young lithosphere near the ridge is hot and buoyant, so it sits high; old lithosphere far from the ridge is cold and dense, so it subsides to abyssal depths. This is why ocean depth increases as √t with plate age — it's a direct consequence of thermal contraction and isostatic adjustment."

- question: "The plate model predicts that oceanic lithosphere continues to thicken indefinitely as it ages, but at a progressively slower rate."
  type: true-false
  answer: false
  explanation: "The plate model was specifically developed to correct this prediction of the half-space model. By imposing a fixed temperature boundary at the base of the lithosphere, the plate model predicts that the thermal boundary layer approaches a maximum thickness asymptotically — the lithosphere stops thickening once it reaches thermal equilibrium with the hot asthenosphere beneath. This explains why heat flow and bathymetry flatten for plates older than ~80 Ma."

- question: "Why does oceanic depth increase as oceanic lithosphere ages, and what is the physical mechanism connecting thermal state to ocean floor depth?"
  type: short-answer
  answer: "As oceanic lithosphere moves away from the mid-ocean ridge, it cools by conduction. Cooler rock is denser than warm rock (thermal contraction). Because the lithosphere floats on the asthenosphere (isostasy), denser lithosphere sinks lower. The half-space model predicts this depth increase follows √t: the thermal boundary layer thickens proportionally to √t, the plate becomes denser, and isostatic equilibrium requires it to sit deeper. This is why the ocean floor is shallow near ridges and deepens progressively toward subduction zones."
  explanation: "The chain is: age → cooling → thermal contraction → increased density → isostatic subsidence → greater ocean depth. The √t dependence emerges because heat diffuses into the plate following the diffusion equation, whose solution for a semi-infinite medium has a characteristic length scale proportional to √(κt), where κ is thermal diffusivity."
```

## Explainer

From your understanding of heat conduction models and plate tectonics, you know that temperature within the Earth is governed by the balance between heat sources (mantle convection, radioactive decay) and heat loss through conduction to the surface. Lithospheric thermal evolution applies these principles to track how an oceanic plate changes from the moment it forms at a mid-ocean ridge to its eventual subduction, often tens or hundreds of millions of years later.

At the ridge, hot asthenospheric material rises to near the surface, creating new lithosphere at temperatures close to 1,300°C. As this plate moves away from the ridge, it cools from the top down by conduction. The simplest model treating the plate as a **half-space cooling** from an initially uniform temperature predicts that the depth to any isotherm grows as the square root of age. This means the lithosphere thickens proportionally to √t — a 25-million-year-old plate has a thermal boundary layer roughly twice as thick as a 6-million-year-old one. The model successfully predicts two independently observable quantities: surface **heat flow** decreases as 1/√t (younger crust loses heat faster), and **ocean depth** increases as √t (cooler, denser lithosphere sinks isostatically).

The half-space model works well for young oceanic lithosphere (less than ~70 million years), but it overpredicts both subsidence and heat flow decline for older plates. Observations show that bathymetry and heat flow flatten out for ages beyond about 80 Ma, as if the plate reaches a maximum thickness and stops cooling further. The **plate model** resolves this by imposing a fixed temperature at the base of the lithosphere — effectively assuming that small-scale convection or heat input from the asthenosphere prevents the thermal boundary layer from growing indefinitely. The plate model treats the lithosphere as a slab of finite thickness (typically 100–125 km) with a hot base, and its predictions match the observed flattening of heat flow and bathymetry at old ages.

These thermal models have far-reaching consequences. Because density depends on temperature (cooler rock is denser), the thermal state of the lithosphere controls its buoyancy and therefore the depth of the ocean floor — this is why mid-ocean ridges stand high and abyssal plains are deep. The same cooling governs when oceanic lithosphere becomes dense enough to subduct. At passive margins, the thermal history of rifting and subsequent cooling controls the pattern of subsidence that creates accommodation space for sedimentary basins. Understanding lithospheric thermal evolution thus connects heat flow measurements at the surface to the large-scale dynamics of plate tectonics.
