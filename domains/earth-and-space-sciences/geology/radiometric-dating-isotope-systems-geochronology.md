---
id: radiometric-dating-isotope-systems-geochronology
title: Radiometric Dating Methods and Absolute Geochronology
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: geological-time-scale
  type: soft
- id: radioactive-decay
  type: hard
- id: alpha-decay-emission
  type: hard
- id: exponential-functions-and-graphs
  type: hard
tags:
- geochronology
- dating
- isotopes
stage: formal-systems
status: validated
---

# Radiometric Dating Methods and Absolute Geochronology

## Core Idea
Radiometric dating uses the predictable decay of radioactive isotopes (K-Ar, Rb-Sr, U-Pb, Sm-Nd) to determine absolute ages of rocks and minerals. Each isotope system has a different closure temperature; U-Pb dates zircon crystallization while K-Ar dates cooling through ~300°C. Combining multiple systems constrains burial and cooling histories.

## Questions

```yaml
- question: "A geologist uses K-Ar dating on biotite from a granite and obtains an age of 280 Ma. A colleague reports U-Pb zircon ages from the same granite of 320 Ma. Which interpretation is most likely correct?"
  type: multiple-choice
  options:
    - "The K-Ar date is more reliable because biotite is more resistant to lead loss than zircon"
    - "The dates contradict each other, so one system must have been contaminated and the results are unreliable"
    - "The granite crystallized around 320 Ma, and the K-Ar date records when the rock cooled through biotite's closure temperature (~300°C) at 280 Ma"
    - "The granite formed at 280 Ma and was later reheated to temperatures that reset the U-Pb zircon clock to 320 Ma"
  answer: 2
  explanation: "Different isotope systems have different closure temperatures, so they record different thermal events — not contradictory versions of the same event. Zircon's closure temperature is ~900°C, so U-Pb records crystallization from magma. Biotite's K-Ar closure temperature is ~300°C, so it records cooling through that temperature threshold. The 40 Ma gap between them tells us how long the granite took to cool from crystallization temperature to ~300°C — a record of uplift and erosion rate, not an inconsistency. Option D is reversed: U-Pb in zircon is extremely resistant to resetting, whereas K-Ar is the system more easily disturbed."

- question: "Zircons from an ancient metamorphic terrane plot below the concordia curve (they are 'discordant'). What is the most straightforward geological interpretation?"
  type: multiple-choice
  options:
    - "The zircons crystallized from two distinct magmatic events and their ages are mixed"
    - "The uranium decay constants used in the calculation are slightly wrong"
    - "Some radiogenic lead was lost from the crystal lattice after crystallization, causing both the ²⁰⁶Pb/²³⁸U and ²⁰⁷Pb/²³⁵U ratios to shift away from concordia"
    - "The zircons formed below their closure temperature, so the clock never started properly"
  answer: 2
  explanation: "Concordia is the curve on a Wetherill diagram where both U-Pb decay systems agree perfectly. Points plotting below concordia indicate 'lead loss' — some radiogenic lead has escaped the crystal after it formed, decreasing both Pb/U ratios. Lead loss commonly happens during metamorphic events when the crystal lattice is partially disturbed. The power of the U-Pb system is that discordance itself carries information: a straight line (discordia) drawn through multiple discordant analyses intersects concordia at the original crystallization age (upper intercept) and the age of lead loss (lower intercept). This is why U-Pb is considered the gold standard for geochronology."

- question: "The closure temperature of a mineral determines when its radiometric clock starts — not necessarily when the rock formed, but when it cooled enough to stop losing daughter isotopes by diffusion."
  type: true-false
  answer: true
  explanation: "True. Above the closure temperature, daughter isotopes (like ⁴⁰Ar in K-Ar or ⁸⁷Sr in Rb-Sr) can diffuse through the crystal lattice and escape. The isotopic ratio is constantly being reset by this loss. Once the mineral cools below its closure temperature, daughter atoms are trapped and begin accumulating. The 'clock' starts at closure, not at formation. This is the fundamental concept that allows different minerals to record different stages of a rock's thermal history rather than all recording the same 'formation age.'"

- question: "A mineral with a higher closure temperature records a more recent thermal event than a mineral with a lower closure temperature from the same cooling rock."
  type: true-false
  answer: false
  explanation: "False — it records an earlier (older) event, not a more recent one. During cooling, a rock passes through higher temperatures first, then lower temperatures. A mineral with a high closure temperature (like zircon at ~900°C) closes its isotopic system early in the cooling history, when the rock was still very hot; this records the oldest age. A mineral with a lower closure temperature (like K-feldspar at ~150°C) closes much later in the cooling history; this records the most recent age. High closure = closes early = older recorded age. This is the exact opposite of the common intuition."

- question: "A geologist collects a single granite sample and obtains radiometric ages from four different minerals: U-Pb in zircon (900°C closure), Rb-Sr in muscovite (500°C closure), K-Ar in hornblende (500°C closure), and K-Ar in K-feldspar (150°C closure). Explain what these four ages collectively reveal that no single age could reveal alone."
  type: short-answer
  answer: "Each mineral records the time the rock cooled through its specific closure temperature. Together the four ages define a cooling path through time: the zircon age gives crystallization, and the progressively younger ages of muscovite, hornblende, and K-feldspar record the temperature-time path as the rock moved toward the surface. From the ages and closure temperatures, geologists can calculate cooling rates (°C per million years) at different stages of the rock's history, and from cooling rates infer exhumation rates — how fast overlying material was eroded away. This technique (thermochronology) reconstructs the erosion and tectonic history of mountain belts from a single rock sample."
  explanation: "No single radiometric age tells you whether a rock cooled slowly or quickly, or whether it was reburied and reheated. Multiple systems with known closure temperatures turn the question into a cooling-path problem: plot temperature versus time, connect the data points, and read off the history. Rapidly cooled rocks (e.g., a lava flow) give clustered ages from all systems; slowly cooled rocks (e.g., a deeply buried batholith) show a spread of ages spanning tens or hundreds of millions of years."
```

## Explainer

From your study of radioactive decay and alpha emission, you know that unstable isotopes transform into daughter products at rates governed by their half-lives, and from exponential functions, you know how to describe this mathematically: the number of parent atoms decreases as N(t) = N₀ · e^(−λt), where λ is the decay constant. **Radiometric dating** applies this principle to geology: if you can measure the ratio of parent to daughter isotopes in a mineral, and you know the decay constant, you can solve for *t* — the time since the mineral's isotopic clock started ticking.

The key concept that makes different isotope systems useful for different purposes is the **closure temperature**. A mineral's isotopic clock does not start at formation — it starts when the mineral cools below a temperature at which the daughter isotope can no longer escape from the crystal lattice by diffusion. Above the closure temperature, daughter atoms migrate freely and the system remains "open"; below it, the system "closes" and daughter atoms accumulate in place. The **U-Pb system in zircon** has an extremely high closure temperature (~900°C), meaning zircon locks in its lead almost immediately upon crystallizing from a magma. This makes U-Pb zircon dating ideal for determining the crystallization age of igneous rocks. The **K-Ar system in muscovite** closes at around 350°C, and in biotite at around 300°C — so these minerals record the time when a rock cooled through those temperatures, not necessarily when it first formed.

This is what makes multi-system dating so powerful. Imagine a granite that crystallized at 800°C deep in a mountain belt, then slowly cooled as the mountains eroded and the rock approached the surface. U-Pb in zircon gives you the crystallization age — say 400 million years ago. Rb-Sr in muscovite (closure ~500°C) might give 380 Ma. K-Ar in biotite (closure ~300°C) gives 360 Ma. K-Ar in feldspar (closure ~150°C) gives 340 Ma. Together, these ages trace out a **cooling path**: you know the rock took 60 million years to cool from 900°C to 150°C, and you can calculate cooling rates and infer how fast the overlying rock was being eroded away. This technique — **thermochronology** — reconstructs the exhumation history of mountain belts and is indispensable in tectonics.

Each system also has practical limitations that determine when it is appropriate to use. K-Ar dating is straightforward but can be reset by later heating events (since argon diffuses easily), so a K-Ar age on a metamorphic rock might date the last metamorphic episode rather than original formation. The **Rb-Sr isochron method** avoids the problem of not knowing initial daughter isotope ratios by analyzing multiple minerals from the same rock and plotting them on an isochron diagram — the slope of the line gives the age. U-Pb dating benefits from having two independent decay chains (²³⁸U→²⁰⁶Pb and ²³⁵U→²⁰⁷Pb), providing a built-in cross-check: if a sample plots on the **concordia curve**, both systems agree and the age is robust; deviations indicate lead loss or other disturbance. For very old rocks (billions of years), the Sm-Nd system is preferred because samarium and neodymium are resistant to weathering and metamorphic resetting. Choosing the right isotope system for a geological question is as important as the measurement itself.
