---
id: geomorphology
title: 'Geomorphology: Landforms and Surface Processes'
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: weathering-and-erosion
  type: hard
- id: sediment-transport-and-deposition
  type: hard
- id: geologic-structures-folds-faults
  type: soft
- id: soil-formation
  type: soft
tags:
- geomorphology
- landforms
- fluvial
- glacial
- coastal
- mass-wasting
- landscape-evolution
stage: formal-systems
status: validated
---

# Geomorphology: Landforms and Surface Processes

## Core Idea
Geomorphology studies the origin, form, and evolution of Earth's landforms through the interplay of tectonic uplift, rock properties, and surface processes driven by water, ice, wind, and gravity. Fluvial systems (rivers and streams) shape most mid-latitude landscapes through incision, lateral erosion, and deposition; the stream power law relates erosion rate to drainage area and channel gradient. Glacial processes—abrasion, quarrying, and meltwater action—sculpt distinctive U-shaped valleys, cirques, moraines, and drumlins. Mass wasting (landslides, debris flows, rockfalls) moves material downslope under gravity; its triggering depends on slope angle, pore water pressure, and material cohesion. Landscape evolution models (Davisian cycle, dynamic equilibrium) attempt to describe how landforms change over geological time in response to base level changes and tectonic forcing.

## How It's Best Learned
Analyzing digital elevation models or topographic maps to identify stream capture, glacial features, or fault scarps trains the observational skills central to geomorphology. Comparing drainage basin morphology (elongated vs. dendritic vs. trellis patterns) with underlying geology links landscape form to structural and lithological controls.

## Common Misconceptions
- Larger rivers always cut deeper valleys is false; base level (usually sea level or a local lake) sets the lower limit of incision regardless of river size.
- Glaciers move by sliding and internal deformation, not by melting and refreezing alone; the mechanism depends on whether the base is at the pressure-melting point.
- Landslides are not limited to steep mountain slopes; gentle clay-rich slopes can fail suddenly when pore water pressure rises during heavy rainfall, as seen in many fatal events in low-relief terrain.

## Questions

```yaml
- question: "Two rivers run parallel through the same landscape: River A drains a 10,000 km² watershed and River B drains only 500 km². A student predicts River A will always cut a deeper valley because it has far greater discharge. What critical concept does this reasoning overlook?"
  type: multiple-choice
  options:
    - "River A carries more suspended sediment, which armors the valley floor and limits incision"
    - "Base level sets an absolute lower limit for incision regardless of river size; both rivers can only cut down to their local base level, making discharge alone insufficient to predict valley depth"
    - "Smaller rivers have steeper gradients, so River B will incise more deeply per unit discharge"
    - "Valley depth is determined entirely by bedrock hardness, not discharge or drainage area"
  answer: 1
  explanation: "The stream power law predicts erosion rate from gradient and discharge, but base level — typically sea level, a lake, or a resistant rock step — sets the floor below which no river can incise, regardless of its power. A large river draining to sea level is limited to the same ultimate incision depth as a small river draining to the same point. Base level changes (e.g., sea level fall or dam removal) are what unlock deeper incision, not river size alone."

- question: "On a topographic map, which cross-sectional shape most reliably distinguishes a glacially carved valley from a fluvially carved valley?"
  type: multiple-choice
  options:
    - "Glacial valleys are always deeper; fluvial valleys are always wider"
    - "Glacial valleys have U-shaped cross-sections with steep walls and flat floors; fluvial valleys have V-shaped cross-sections narrowing to the channel"
    - "Glacial valleys show meandering planform patterns; fluvial valleys are straight"
    - "Glacial valleys lack tributary streams; fluvial valleys have dendritic drainage networks"
  answer: 1
  explanation: "Rivers erode primarily by abrasion and hydraulic action concentrated at the channel bottom, producing a V-shape that narrows downward. Glaciers erode by abrasion and quarrying across their entire base and lower walls simultaneously, widening the valley floor and producing a characteristic U-shape with steep headwalls. This cross-sectional difference is the most diagnostic field indicator of glacial vs. fluvial origin."

- question: "Larger rivers with high discharge always cut deeper valleys than smaller rivers, because greater water volume provides greater erosive power."
  type: true-false
  answer: false
  explanation: "While discharge does increase erosion rate through the stream power law, base level provides an absolute lower limit on incision that no amount of discharge can overcome. A large river cannot incise below sea level or below a resistant bedrock step that defines its local base level. Valley depth reflects both the erosive capacity of the river and the position of its base level — not discharge alone."

- question: "Landslides and debris flows can occur on relatively gentle, clay-rich slopes when pore water pressure rises sufficiently during prolonged heavy rainfall, even in the absence of steep terrain."
  type: true-false
  answer: true
  explanation: "Slope stability depends on the balance between driving forces (gravity, proportional to slope angle and material weight) and resisting forces (friction, cohesion, root strength). Elevated pore water pressure reduces effective normal stress between grains, dramatically lowering friction. When pore pressure rises enough, even gentle clay-rich slopes can fail suddenly. Many fatal historical landslides have occurred on slopes that appear safe under dry conditions."

- question: "Explain how base level controls the depth to which a river can incise its valley, and why this makes a river's discharge an insufficient predictor of valley depth."
  type: short-answer
  answer: "Base level is the lowest elevation to which a river can erode — typically sea level for rivers draining to the ocean, or a resistant rock layer, lake, or dam for interior rivers. No matter how much erosive power a river has, it cannot cut below this level because the energy gradient that drives incision disappears at base level. Valley depth therefore reflects both the river's capacity to erode and how far above base level the surrounding landscape sits. Two rivers with very different discharges draining to the same base level can ultimately incise to the same depth, while a small river far above base level may carve a deeper gorge than a large one near sea level."
  explanation: "The concept of base level is essential for interpreting ancient and modern landscapes. Knickpoints (abrupt steps in the river profile) mark where base level change has not yet propagated upstream — classic evidence of glacial lake drainage, tectonic uplift, or human-altered base levels. Understanding this prevents the common error of attributing all landscape differences to discharge rather than to the history of base level change and tectonic context."
```

## Explainer

You already understand that weathering breaks rock into transportable particles and that sediment transport moves those particles downhill and downstream. Geomorphology takes the next step: it asks how these processes, operating over thousands to millions of years, sculpt the landforms we see — valleys, ridges, floodplains, glacial cirques, coastal cliffs, and everything in between. The central insight is that landscape form reflects a competition between **tectonic uplift** (which raises rock above base level) and **surface processes** (which wear it down and carry it away).

**Fluvial geomorphology** — the study of river-shaped landscapes — dominates most of the Earth's surface outside polar regions. Rivers erode their beds and banks, transport sediment, and deposit it where energy decreases. The key quantitative relationship is the **stream power law**, which states that erosion rate scales with both drainage area (a proxy for water discharge) and channel gradient (the slope of the river bed). Steep, well-fed rivers cut deep valleys; gentle, sediment-laden rivers build broad floodplains. Drainage patterns themselves encode geological information: **dendritic** (branching) networks develop on uniform substrates, **trellis** patterns follow alternating resistant and weak rock layers, and **rectangular** patterns reflect joint or fault control. When a river cuts headward and captures the drainage of an adjacent basin — a process called **stream piracy** — the abrupt change in drainage area reshapes both landscapes rapidly.

**Glacial geomorphology** produces a distinctive suite of landforms because ice erodes differently from water. Glaciers erode by **abrasion** (rocks embedded in the ice base act like sandpaper on bedrock) and **quarrying** (meltwater freezes in cracks and plucks blocks loose). The result is U-shaped valleys with steep walls and flat floors, in contrast to the V-shaped valleys cut by rivers. At the head of a glacier, freeze-thaw weathering carves steep-walled **cirques**; where multiple cirques intersect, they leave sharp ridges called arêtes and pyramidal peaks called horns. Glacial deposits — **moraines** (ridges of unsorted debris), **drumlins** (streamlined hills of till), and **outwash plains** (sorted sand and gravel from meltwater) — record the extent and behavior of past ice sheets and are key evidence for reconstructing Pleistocene glaciation.

**Mass wasting** — the downslope movement of rock and soil under gravity — is the third major agent of landscape change. Unlike rivers and glaciers, gravity acts everywhere there is a slope, and mass wasting events range from slow soil creep (millimeters per year) to catastrophic rock avalanches (hundreds of kilometers per hour). The stability of a slope depends on the balance between the gravitational driving force (proportional to slope angle and material weight) and the resisting forces (friction, cohesion, and root strength). **Pore water pressure** is the most common trigger for failure: when heavy rain saturates a slope, water pressure in pore spaces reduces the effective friction, and the slope collapses. Understanding mass wasting connects directly to your knowledge of sediment transport — it is the first step in moving material from hillslopes into the channel network where fluvial processes take over.

Geomorphologists integrate these processes into models of **landscape evolution** that describe how entire regions change over geological time. The classical Davisian cycle envisioned landscapes progressing from youth (steep, V-shaped valleys) through maturity (broad valleys, lower relief) to old age (a flat peneplain), but modern approaches favor **dynamic equilibrium** — the idea that landscapes adjust continuously to changes in uplift rate, climate, and base level, and that steady-state forms reflect a balance between erosion and uplift rather than a one-way progression. Quantitative techniques like cosmogenic nuclide dating, digital elevation model analysis, and thermochronology now allow geomorphologists to measure erosion rates directly and test these models against real landscapes.
