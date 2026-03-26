---
id: mineral-physics-high-pressure
title: Mineral Physics and High-Pressure Phase Transitions
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: minerals-and-crystal-structure
  type: hard
- id: planetary-differentiation
  type: soft
builds-toward:
- planetary-interior-dynamics
tags:
- minerals
- phase-transitions
- interior-structure
stage: expert
status: validated
---

# Mineral Physics and High-Pressure Phase Transitions

## Core Idea
Mineral compositions and crystal structures transform dramatically under the extreme pressures and temperatures of planetary interiors. These phase transitions alter density, elastic properties, and seismic velocities, allowing inference of interior composition and structure from geophysical data. Laboratory high-pressure experiments on candidate mantle materials constrain planetary interiors.

## Questions

```yaml
- question: "A seismologist observes a sharp discontinuity in seismic wave velocity at 410 km depth within Earth's mantle. What does mineral physics predict is the most likely cause?"
  type: multiple-choice
  options:
    - "A change in chemical composition from iron-rich to magnesium-rich material at that depth"
    - "A phase transition from olivine to wadsleyite — the same chemistry rearranged into a denser crystal structure"
    - "The boundary between the crust and the mantle (the Mohorovičić discontinuity)"
    - "A thermal boundary layer where temperature increases rapidly over a short depth interval"
  answer: 1
  explanation: "The 410 km discontinuity corresponds precisely to the olivine-to-wadsleyite phase transition observed in laboratory experiments at ~13 GPa. The chemical composition does not change — only the crystal structure reorganizes into a denser packing. This is the core inferential tool of mineral physics: matching lab-measured phase transitions to seismic observations to infer interior composition. Option A is the common misconception — a compositional boundary would produce a gradual velocity change, not the sharp discontinuity associated with a phase transition."

- question: "Scientists compare two rocky exoplanets with identical bulk compositions — one is Earth-sized, one is twice Earth's mass. What does mineral physics predict about their interiors?"
  type: multiple-choice
  options:
    - "They will have essentially the same layered structure, just scaled proportionally in size"
    - "The larger planet will have phase transitions at shallower relative depths, with higher-pressure mineral phases (like post-perovskite) dominating its lower mantle"
    - "The smaller planet will have more phase transitions because its interior experiences greater pressure variation per unit depth"
    - "Both planets will have phase transitions at the same absolute depths, since the chemical compositions are identical"
  answer: 1
  explanation: "A more massive planet has a steeper pressure gradient — pressure increases faster with depth. Phase transitions are governed by pressure-temperature conditions, not by depth per se. So on a larger planet, the olivine-wadsleyite transition occurs at a shallower absolute depth, and the lower mantle is dominated by even higher-pressure phases like post-perovskite that may not appear on Earth at all. Interior structure changes qualitatively, not just in scale, with planetary size."

- question: "Seismic discontinuities within a planet's mantle usually indicate boundaries between regions of different chemical composition."
  type: true-false
  answer: false
  explanation: "Phase transitions produce sharp changes in seismic velocity even when chemistry is constant. Earth's 410 km and 660 km discontinuities arise from olivine transforming to wadsleyite and ringwoodite breaking down into bridgmanite + ferropericlase — the same chemical elements, just reorganized into denser crystal structures. Inferring composition purely from discontinuities without knowing the pressure-temperature phase diagram would conflate compositional boundaries with phase transition boundaries."

- question: "A diamond anvil cell experiment squeezes olivine to 13 GPa and finds that the atoms rearrange into a new crystal structure with higher density. The new phase is expected to therefore have a different chemical formula than the original olivine."
  type: true-false
  answer: false
  explanation: "Phase transitions change crystal structure, not chemical composition. Wadsleyite and ringwoodite have the same chemical formula as olivine (Mg,Fe)₂SiO₄ — the same atoms are present, just packed into a denser lattice arrangement that minimizes energy under high pressure. The higher density and different seismic velocity arise from the structural reorganization, not from a change in what elements are present."

- question: "Why do mineral physics laboratory experiments on tiny crystal samples provide reliable information about planetary interiors that we can never directly sample?"
  type: short-answer
  answer: "Phase transitions are governed by pressure-temperature conditions alone, not by sample size. A diamond anvil cell recreates the same pressure-temperature environment that exists at a given depth inside a planet, producing the same stable mineral phase. By measuring seismic velocities of each phase in the lab and matching against observed seismic discontinuities, we can identify what material is present at any depth. The physics of crystal packing is scale-invariant."
  explanation: "This is the fundamental logic of mineral physics as a field: controlled laboratory experiments on milligram samples constrain the composition of worlds we cannot sample directly. The key is that phase stability depends on intensive variables (pressure and temperature per unit volume) rather than extensive ones (total mass), making lab experiments directly applicable to planetary interiors."
```

## Explainer

You already know that minerals have ordered crystal structures — atoms arranged in repeating lattice patterns that determine a mineral's physical properties. At Earth's surface, olivine is a common mantle mineral with a particular arrangement of silicon, oxygen, magnesium, and iron atoms. But push that same olivine down to 410 km depth, where pressures exceed 13 gigapascals, and the atoms rearrange into a denser crystal structure called **wadsleyite**. Push further to 520 km and it transforms again into **ringwoodite**. At 660 km depth, roughly 24 GPa, ringwoodite breaks down entirely into **bridgmanite** (a magnesium silicate perovskite) and **ferropericlase**. The chemistry is the same — the atoms just pack more tightly to minimize energy under crushing pressure.

These **phase transitions** matter because each new crystal structure has different density, compressibility, and ability to transmit seismic waves. When a seismologist observes a sharp change in wave velocity at a particular depth, that discontinuity maps directly to a phase transition predicted by mineral physics. The 410 km and 660 km seismic discontinuities in Earth's mantle correspond precisely to the olivine-to-wadsleyite and ringwoodite-to-bridgmanite transitions observed in laboratory experiments. This is the core inferential tool: we squeeze minerals in **diamond anvil cells** or **multi-anvil presses** at millions of atmospheres, measure the resulting phase changes, and match them against seismic observations to determine what the deep interior is made of.

The implications extend far beyond Earth. For any rocky planet or large moon, the interior pressure profile determines which mineral phases are stable at each depth. A planet twice Earth's mass has a steeper pressure gradient, so phase transitions occur at shallower depths and the lower mantle is dominated by even higher-pressure phases like **post-perovskite**. This means interior structure is not simply a scaled-up version of Earth — the mineral physics changes qualitatively with planetary size, affecting everything from density profiles to convection patterns to the likelihood of plate tectonics.

Understanding these transitions also connects back to planetary differentiation. During a planet's early molten history, the sequence in which minerals crystallize from a cooling magma ocean depends on pressure-dependent phase diagrams. Which minerals sink, which float, and where chemical boundaries form are all governed by the same high-pressure physics. Mineral physics thus provides the bridge between a planet's bulk composition and its observable geophysical signature — turning laboratory measurements of tiny crystal samples into constraints on worlds we can never directly sample.
