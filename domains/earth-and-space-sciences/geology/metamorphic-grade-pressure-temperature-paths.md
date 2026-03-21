---
id: metamorphic-grade-pressure-temperature-paths
title: Metamorphic Grade and Pressure-Temperature Paths
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: metamorphic-rocks
  type: soft
- id: crustal-heat-flow-and-geotherms
  type: soft
builds-toward:
- metamorphic-facies-rock-associations
- subduction-zone-structure-metamorphism
tags:
- metamorphism
- PT-diagrams
- grade
stage: advanced
status: draft
---

# Metamorphic Grade and Pressure-Temperature Paths

## Core Idea
Metamorphic grade reflects temperature and pressure conditions; mineral assemblages record equilibrium PT conditions at specific times. PT paths (P-T-t trajectories) show burial, heating, and exhumation history of rocks. Comparison of observed mineral assemblages to experimental phase diagrams reveals the geothermal history of orogenic belts.

## Questions

```yaml
- question: "Blueschist-facies rocks containing glaucophane and lawsonite are found exhumed at the surface. Which tectonic environment most likely produced them, and what does their P-T path look like?"
  type: multiple-choice
  options:
    - "Continental collision zone; a clockwise P-T path with initial burial followed by heating at depth"
    - "Subduction zone; a high-pressure, low-temperature path where the rock was buried faster than it could heat up"
    - "Mid-ocean ridge; a high-temperature, low-pressure path from proximity to an underlying magma source"
    - "Continental rift; a low-pressure, high-temperature path reflecting crustal thinning and asthenosphere upwelling"
  answer: 1
  explanation: "Glaucophane and lawsonite are stable only at high pressure and low temperature — conditions that arise when rock is subducted rapidly into the mantle before the surrounding hot mantle can heat it. The subducting slab carries cold oceanic crust to great depth quickly, producing the characteristic high-P, low-T path of blueschist facies. In a collision zone, the slower thickening process allows more thermal equilibration, producing a clockwise path with higher temperatures at similar pressures and generating different mineral assemblages (garnet, kyanite, staurolite)."

- question: "A geologist finds garnet porphyroblasts in a schist, with inclusions of chlorite and albite trapped inside the garnet cores. What can be inferred from this?"
  type: multiple-choice
  options:
    - "The rock simultaneously equilibrated at conditions where both chlorite-albite and garnet are stable"
    - "The inclusions record earlier, lower-grade conditions; the garnet grew later as the rock reached higher grade, preserving the earlier assemblage inside it"
    - "The chlorite and albite inclusions indicate the garnet is unstable and currently breaking down"
    - "Nothing useful — inclusions within minerals are always contamination artifacts"
  answer: 1
  explanation: "When a porphyroblast like garnet grows during prograde metamorphism, it can trap mineral grains present at the time of nucleation as inclusions. These inclusions are then shielded from further reaction by the surrounding garnet and preserve a 'snapshot' of the earlier, lower-grade assemblage. The core inclusions (chlorite + albite, low grade) record conditions before garnet stability; the garnet rim may include higher-grade phases grown later. This sequential record allows geologists to reconstruct stages of the P-T path rather than just peak conditions."

- question: "The metamorphic grade of a rock tells you both the peak conditions it reached and the full P-T path it traveled to get there."
  type: true-false
  answer: false
  explanation: "Metamorphic grade primarily records peak (or near-peak) conditions — the most intense conditions the rock experienced, which set the dominant stable mineral assemblage. The grade does not, by itself, reveal the path: two rocks reaching identical peak conditions (same grade) could have traveled very different P-T paths to get there. Reconstructing the path requires identifying sequential assemblages — such as inclusions within porphyroblasts preserving earlier stages, or retrograde overprinting of peak minerals — rather than just identifying the dominant mineral assemblage."

- question: "Mineral assemblages in a metamorphic rock can record conditions from multiple stages of the rock's pressure-temperature history, not just the peak metamorphic conditions."
  type: true-false
  answer: true
  explanation: "True. Inclusions trapped within porphyroblasts during their growth can preserve earlier, lower-grade assemblages. Retrograde minerals overprinting peak-grade minerals record the cooling and decompression during exhumation. A single rock may thus contain textural evidence of prograde, peak, and retrograde stages. This multilayer record is how geologists reconstruct P-T paths rather than just identifying a single set of peak conditions."

- question: "Why do rocks in subduction zones follow different P-T paths than rocks in continent-continent collision zones, and what mineral evidence distinguishes the two settings?"
  type: short-answer
  answer: "In subduction zones, cold oceanic lithosphere descends rapidly into the hot mantle. The fast burial rate means the rock reaches great depth (high pressure) before the surrounding mantle has time to heat it — producing a high-pressure, low-temperature path. Diagnostic minerals include glaucophane and lawsonite (blueschist facies). In continent-continent collision zones, crustal thickening buries rocks more slowly, allowing more thermal equilibration. The P-T path is clockwise: burial increases pressure first, then prolonged residence at depth allows heating at roughly constant pressure, followed by exhumation. Diagnostic minerals include garnet, staurolite, and kyanite (greenschist to amphibolite facies). The two paths occupy different regions of the P-T diagram and stabilize fundamentally different mineral assemblages."
  explanation: "The rate of burial relative to the rate of thermal equilibration is the controlling factor. Fast subduction keeps the slab cold at depth; slow collision allows heating. These different thermal histories trace distinct trajectories on the P-T diagram, which experimental petrology has mapped to distinct mineral stability fields. Reading the minerals is reading the tectonic history."
```

## Explainer

From your study of metamorphic rocks and crustal heat flow, you know that rocks change their mineralogy and texture when subjected to elevated temperature and pressure without fully melting. **Metamorphic grade** is the concept that organizes these changes along an intensity scale — from low-grade metamorphism (modest temperature and pressure, producing rocks like slate) to high-grade metamorphism (extreme conditions, producing rocks like migmatite that approach partial melting). The grade is not just a label; it corresponds to specific temperature and pressure ranges that determine which minerals are stable.

The key tool for understanding metamorphic grade is the **pressure-temperature (PT) diagram**. Imagine a graph with temperature on the horizontal axis and pressure (which increases with depth in the Earth) on the vertical axis. Experimental petrology has mapped out stability fields for mineral assemblages on this diagram — regions where specific combinations of minerals coexist in equilibrium. For example, the assemblage chlorite + albite + quartz is stable at low temperatures and pressures (low grade), while garnet + staurolite + kyanite indicates significantly higher temperatures and pressures (medium to high grade). When a geologist identifies the minerals present in a metamorphic rock, they can plot the corresponding stability field on the PT diagram and determine the approximate conditions the rock experienced. Each mineral assemblage acts like a thermometer and barometer frozen into the rock.

But rocks do not simply sit at one set of conditions — they move through PT space as they are buried, heated, and eventually brought back to the surface. The trajectory they follow is called a **PT path** (or more precisely, a P-T-t path when timing information is included). Consider a rock caught in a continental collision zone. As the collision thickens the crust, the rock is buried deeper, increasing both pressure and temperature. It then reaches peak metamorphic conditions — the highest grade it experiences. Eventually, erosion or tectonic processes bring the rock back toward the surface, decreasing pressure and temperature during **exhumation**. The PT path records this entire journey: burial on the way up the diagram, peak conditions at the turning point, and exhumation on the way back down.

Different tectonic settings produce characteristically different PT paths. Rocks in **subduction zones** follow a **high-pressure, low-temperature** path — they are carried to great depths rapidly by the descending slab before the surrounding mantle has time to heat them, producing minerals like blueschist-facies glaucophane and lawsonite. Rocks in the cores of **continent-continent collision zones** follow a **clockwise PT path** (on a standard PT diagram with T horizontal and P vertical): they are first buried (increasing P), then heated as the thickened crust equilibrates thermally (increasing T at roughly constant P), then exhumed (decreasing P and T). By identifying the sequence of mineral assemblages preserved in a single rock — sometimes as inclusions within later-grown minerals — geologists reconstruct these paths and read the tectonic history of mountain belts that may have formed hundreds of millions of years ago.
