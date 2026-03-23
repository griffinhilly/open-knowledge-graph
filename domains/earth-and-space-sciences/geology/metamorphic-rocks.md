---
id: metamorphic-rocks
title: Metamorphic Rocks
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: igneous-rocks
  type: hard
- id: sedimentary-rocks
  type: hard
- id: entropy-and-gibbs-free-energy
  type: soft
- id: gibbs-free-energy-spontaneity
  type: soft
builds-toward:
- rock-cycle
- geologic-structures-folds-faults
tags:
- metamorphism
- foliation
- pressure-temperature
- schist
- gneiss
- marble
stage: formal-systems
status: validated
---

# Metamorphic Rocks

## Core Idea
Metamorphic rocks form when pre-existing rocks (protoliths) are subjected to elevated temperature, pressure, or chemically active fluids that drive mineral recrystallization without melting. The grade of metamorphism reflects the peak pressure-temperature conditions reached; index minerals (chlorite → biotite → garnet → staurolite → kyanite → sillimanite) mark increasing grades in pelitic (clay-rich) protoliths. Foliation—the planar alignment of platy minerals like mica—develops under directed (non-hydrostatic) stress and distinguishes most metamorphic rocks from their protoliths. Contact metamorphism occurs locally around igneous intrusions; regional metamorphism affects large crustal volumes during mountain-building events.

## How It's Best Learned
Tracing the metamorphic progression from shale → slate → phyllite → schist → gneiss gives a concrete ladder of increasing grade. Comparing a hand sample of marble (recrystallized limestone) with the original limestone protolith makes the concept of recrystallization without melting tangible.

## Common Misconceptions
- Metamorphism requires solid-state recrystallization; if rock melts, the product is magma and eventually an igneous rock.
- High pressure alone does not produce high-grade metamorphism; temperature must also be elevated, which is why subducted cold slabs produce unusual blueschist facies rocks.
- Foliation angle does not directly record the direction of maximum compression; the geometry is more complex and involves both stress and strain history.

## Questions

```yaml
- question: "In a pelitic (clay-rich) protolith undergoing increasing metamorphism, which sequence of index minerals correctly represents increasing grade?"
  type: multiple-choice
  options: ["Chlorite → garnet → biotite → kyanite → sillimanite", "Chlorite → biotite → garnet → staurolite → kyanite → sillimanite", "Biotite → chlorite → staurolite → garnet → sillimanite", "Garnet → biotite → chlorite → kyanite → sillimanite"]
  answer: 1
  explanation: "The Barrovian sequence — chlorite, biotite, garnet, staurolite, kyanite, sillimanite — records progressively higher pressure-temperature conditions. Chlorite appears at low grade (greenschist facies); sillimanite is the highest-grade aluminosilicate polymorph. Confusing the order is a common error, especially with the biotite/garnet transition."

- question: "Foliation in a metamorphic rock directly records the orientation of maximum compressive stress at the time of formation."
  type: true-false
  answer: false
  explanation: "This is a classic misconception. Foliation reflects the orientation of platy minerals (like mica) that grew or rotated during deformation, but the relationship between foliation planes and the principal stress axes is geometrically complex. Foliation typically develops perpendicular to the maximum shortening direction, but strain history, mineral rotation, and subsequent deformation can all modify that relationship."

- question: "How does marble differ from limestone if both consist primarily of calcite, and what process accounts for that difference?"
  type: short-answer
  answer: "Marble forms when limestone undergoes solid-state recrystallization under heat and/or pressure. The calcite grains grow larger and interlock, obliterating original sedimentary structures like bedding and fossils. The key difference is texture — coarse interlocking crystals in marble versus finer, often layered grains in limestone — produced by metamorphic recrystallization without melting."
  explanation: "This tests understanding of the core concept: metamorphism transforms mineralogy and texture through recrystallization, not melting. Both rocks are calcite-dominant, so the distinction is entirely textural and structural, which reinforces what metamorphism actually does."
```

## Explainer

You already know that igneous rocks crystallize from magma and sedimentary rocks form from accumulated particles. Metamorphic rocks arise by a third route: an existing rock — the protolith — is subjected to elevated temperature, pressure, or reactive fluids, and its minerals recrystallize in the solid state. The word "solid-state" is critical. If the rock melts, the result is magma and eventually an igneous rock. Metamorphism stays below the melting point but still drives profound mineralogical and textural change.

The clearest way to grasp metamorphism is to follow one rock type through increasing grade. Start with shale — a clay-rich sedimentary rock with tiny, randomly oriented grains. Apply modest heat and directed pressure, and you get slate: fine-grained, splits cleanly along flat planes (cleavage). Push further and the grains grow visibly; mica crystals develop, producing phyllite with its silky sheen. Higher still and mica becomes obvious to the naked eye, foliation is pronounced — this is schist. At the highest grades, minerals segregate into alternating light and dark bands, creating gneiss. Each step reflects new mineral assemblages stable at the prevailing pressure-temperature conditions.

Foliation — the planar fabric of metamorphic rocks — develops because directed (non-hydrostatic) stress causes platy minerals like mica to grow perpendicular to the compression direction, or causes existing grains to rotate into alignment. This distinguishes most metamorphic rocks visually from igneous rocks, which typically lack this fabric. Granite and gneiss can have nearly the same mineral composition, yet look completely different because only the gneiss experienced directed stress during recrystallization.

Two settings produce most metamorphism. Contact metamorphism occurs locally around igneous intrusions, where heat bakes the surrounding rock (country rock) in a halo called an aureole. The changes are largely thermal — pressure effects are minor. Regional metamorphism affects enormous volumes of crust during mountain-building (orogenic) events, where both temperature and lithostatic plus directed pressure are elevated. This produces the foliated schists and gneisses found in the cores of ancient mountain ranges like the Appalachians and Himalayas.

Finally, the index minerals provide a geologic thermometer-barometer. When geologists map the distribution of chlorite, biotite, garnet, staurolite, kyanite, and sillimanite zones in the field, they are mapping the peak pressure-temperature conditions the rocks experienced — effectively reconstructing the ancient geothermal gradient and the depth of burial during metamorphism. This is why metamorphic petrology is central to reconstructing the thermal history of mountain belts.
