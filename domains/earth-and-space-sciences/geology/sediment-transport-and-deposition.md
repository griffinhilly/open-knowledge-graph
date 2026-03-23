---
id: sediment-transport-and-deposition
title: Sediment Transport and Deposition
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: weathering-and-erosion
  type: hard
builds-toward:
- sedimentary-rocks
- geomorphology
- hydrogeology-groundwater
tags:
- sediment
- transport
- deposition
- sorting
- alluvial
- fluvial
stage: formal-systems
status: validated
---

# Sediment Transport and Deposition

## Core Idea
After weathering liberates particles from bedrock, they are transported by flowing water, wind, glaciers, or gravity until energy decreases enough for deposition. Hjulström's diagram describes the critical velocity needed to erode, transport, or deposit particles of a given size: coarse gravel requires the fastest flows, while very fine clay also resists entrainment due to cohesion. During transport, sediments are sorted by size and density and rounded through abrasion, so grain size, sorting, and roundness record the transport history of a deposit. Depositional environments—river channels, deltas, beaches, deep-sea fans—each produce characteristic sediment assemblages that can be read from ancient rocks.

## How It's Best Learned
Flume experiments or stream table simulations where flow velocity is varied to show bedload vs. suspended load vs. solution load make the physics of transport intuitive. Interpreting the grain size distribution of a sand sample from a known environment reinforces how transport energy is encoded in sediment properties.

## Common Misconceptions
- Large boulders are not always deposited close to their source; glaciers can transport car-sized erratics hundreds of kilometers.
- 'Well-sorted' means particles are similar in size, not that they have been carefully arranged; it reflects uniform transport energy.
- Deposition is not always gradual; turbidity currents can deposit graded beds (coarse-to-fine upward) catastrophically in hours.

## Questions

```yaml
- question: "A geologist observing a riverbed notices that sand grains (0.5 mm) are actively moving downstream, but fine clay particles on the same streambed are not being eroded. Why might clay resist erosion at the same flow velocity that moves sand?"
  type: multiple-choice
  options:
    - "Clay particles are denser than sand, requiring more force to move them"
    - "Cohesive forces between clay minerals bind particles together, requiring higher erosion velocities than size alone would predict — clay's resistance to erosion is not simply a function of grain size"
    - "Clay cannot be transported by water at all; it only moves with glaciers"
    - "The small surface area of clay particles means drag forces cannot act on them effectively"
  answer: 1
  explanation: "This is the key counterintuitive result from Hjulström's diagram. For sand-sized particles, intuition holds: finer grains erode at lower velocities. But very fine particles (clay, silt) have strong cohesive electrostatic bonds between mineral surfaces, and it takes more energy to rip a clay particle off a muddy streambed than to pick up a loose sand grain. This creates the characteristic 'U-shape' minimum in the Hjulström curve around the sand fraction. However, once clay is entrained into suspension, it stays suspended at much lower velocities than were needed to erode it — this is why rivers remain turbid for days after a flood."

- question: "A geologist finds a deposit of well-rounded, well-sorted quartz sandstone. What does this indicate about the sediment's transport history?"
  type: multiple-choice
  options:
    - "The deposit formed near its source from a brief, intense flood that winnowed fine grains"
    - "The grains traveled a long distance under sustained, relatively uniform current conditions — rounding by abrasion and sorting by size both require prolonged, consistent transport"
    - "Well-sorted means the grains were deliberately arranged by grain size at the time of deposition"
    - "The well-rounded appearance resulted from chemical weathering, not physical transport"
  answer: 1
  explanation: "Rounding requires abrasion over time and distance — angular fragments lose their corners through repeated collisions during transport. Sorting reflects selective deposition: at any location, the flow velocity selects for a characteristic grain size (faster flows carry larger grains farther). A well-rounded, well-sorted deposit is the signature of sustained, relatively uniform transport — beach sand and aeolian (wind-blown) dune sand are classic examples. Contrast this with glacial till, which is unsorted (everything from clay to boulders deposited together) and angular (glacial transport doesn't produce rounding by abrasion)."

- question: "A 'well-sorted' sediment deposit means the particles are similar in size, reflecting that they were deposited under relatively uniform transport energy conditions."
  type: true-false
  answer: true
  explanation: "Sorting in geology refers to the uniformity of grain sizes in a deposit — well-sorted means most grains are roughly the same size; poorly sorted means a wide range of sizes mixed together. It has nothing to do with arrangement or organization by human hands. Sorting is a direct record of transport energy: steady, uniform flows (beaches, dunes) sort grains effectively because only particles of a specific size range can be transported at that energy level. Variable or catastrophic flows (floods, glaciers) deposit unsorted material because the energy conditions change too rapidly for selective deposition to occur."

- question: "Deposition of sediment is always a slow, gradual process that occurs over years to centuries — catastrophic rapid deposition does not produce recognizable sedimentary structures."
  type: true-false
  answer: false
  explanation: "Turbidity currents are underwater avalanches of sediment-laden water that flow down continental slopes at speeds up to 100 km/h, depositing entire graded beds (coarse-to-fine upward) in a matter of hours. Each bed records a single catastrophic event. The 1929 Grand Banks earthquake triggered a turbidity current that deposited graded beds over a vast area of the Atlantic seafloor in hours, snapping submarine telegraph cables in sequence. Recognizing the difference between gradual and catastrophic deposition is essential for interpreting the geological record correctly."

- question: "Why does Hjulström's diagram show that very fine clay particles require higher erosion velocities than medium sand grains, even though the clay particles are far smaller and lighter?"
  type: short-answer
  answer: "Clay minerals have strong cohesive electrostatic bonds between their flat, sheet-like surfaces. On a muddy streambed, clay particles are bound to each other and to the substrate by these forces, and the flow must overcome them before particles can be detached. Sand grains, by contrast, are loose — only their weight resists entrainment. Because sand is heavy enough that a moderate flow velocity provides sufficient drag and lift, and light enough that cohesion is irrelevant, it erodes at lower velocities than either gravel (too heavy) or clay (too cohesive). This creates the Hjulström diagram's minimum erosion velocity around medium sand."
  explanation: "This question tests whether students understand that 'harder to erode' is not simply a function of grain size or weight — cohesion introduces a completely different resistance mechanism. The practical implication is important: rivers running across soft clay floodplains don't erode them as easily as one might expect, but once the clay is disturbed and entrained, it stays in suspension far longer than the flow conditions that initiated transport would predict. Understanding this asymmetry between erosion and deposition thresholds for fine particles explains why fine-grained rivers take so long to 'run clear' after a disturbance."
```

## Explainer

You know from studying weathering and erosion that physical and chemical processes break bedrock into particles of varying sizes — from clay-sized flakes to house-sized boulders. Sediment transport is what happens next: those particles are picked up, carried, and eventually dropped somewhere else, and the physics of how this works leaves a readable record in every sand grain, gravel bar, and mud flat on Earth.

The key concept is **transport energy** — the capacity of a moving fluid (water, wind, or ice) to carry particles. **Hjulström's diagram** captures the essential physics in a single graph: it plots flow velocity against grain size and shows three fields — erosion, transport, and deposition. For sand-sized particles (0.1–2 mm), the relationship is intuitive — faster water picks up bigger grains. But the diagram reveals two surprises. First, very coarse particles (gravel, cobbles) require enormous velocities to erode because they are simply heavy. Second, very fine particles (clay, silt) also resist erosion despite being tiny, because cohesive forces between clay minerals bind them together — it takes more energy to rip a clay particle off a muddy streambed than to pick up a loose sand grain. Once entrained, however, fine particles stay in suspension at much lower velocities than were needed to erode them, which is why rivers run muddy for days after a flood even as flow decreases.

Particles travel in three modes depending on their size and the flow conditions. **Bedload** consists of coarse grains that roll, slide, or bounce (saltate) along the bottom — gravel in a mountain stream is classic bedload. **Suspended load** consists of finer particles kept aloft by turbulent eddies in the flow — the brown color of a flooding river is suspended silt and clay. **Dissolved load** consists of ions in solution (calcium, sodium, silica) that are invisible and travel with the water itself until conditions change and minerals precipitate. During transport, particles undergo **sorting** (separation by size — faster flows carry bigger grains, so deposits at any location tend to have a characteristic size range) and **rounding** (abrasion knocks off corners, converting angular fragments into smooth, rounded grains). A well-rounded, well-sorted quartz sandstone has traveled a long way and been reworked by sustained, uniform currents; a poorly sorted, angular deposit like glacial till was dumped all at once without selective transport.

Deposition occurs wherever transport energy decreases — a river entering a lake, wind dying down behind a dune, a turbidity current losing speed on the ocean floor. Each **depositional environment** produces a characteristic assemblage of sediment properties. River channels deposit cross-bedded sands and gravels; floodplains accumulate fine silt and clay during overbank floods; deltas build outward with a predictable coarsening-upward sequence as the channel progrades over deeper-water muds; deep-sea fans receive graded beds from turbidity currents, with each bed recording a single catastrophic event. By examining grain size distribution, sorting, roundness, sedimentary structures, and fossil content, geologists can read ancient rocks and reconstruct the transport history and depositional environment — turning stone back into landscape.
