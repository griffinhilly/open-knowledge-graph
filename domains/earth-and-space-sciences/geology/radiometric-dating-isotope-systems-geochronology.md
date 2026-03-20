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
stage: advanced
status: draft
---

# Radiometric Dating Methods and Absolute Geochronology

## Core Idea
Radiometric dating uses the predictable decay of radioactive isotopes (K-Ar, Rb-Sr, U-Pb, Sm-Nd) to determine absolute ages of rocks and minerals. Each isotope system has a different closure temperature; U-Pb dates zircon crystallization while K-Ar dates cooling through ~300°C. Combining multiple systems constrains burial and cooling histories.

## Explainer

From your study of radioactive decay and alpha emission, you know that unstable isotopes transform into daughter products at rates governed by their half-lives, and from exponential functions, you know how to describe this mathematically: the number of parent atoms decreases as N(t) = N₀ · e^(−λt), where λ is the decay constant. **Radiometric dating** applies this principle to geology: if you can measure the ratio of parent to daughter isotopes in a mineral, and you know the decay constant, you can solve for *t* — the time since the mineral's isotopic clock started ticking.

The key concept that makes different isotope systems useful for different purposes is the **closure temperature**. A mineral's isotopic clock does not start at formation — it starts when the mineral cools below a temperature at which the daughter isotope can no longer escape from the crystal lattice by diffusion. Above the closure temperature, daughter atoms migrate freely and the system remains "open"; below it, the system "closes" and daughter atoms accumulate in place. The **U-Pb system in zircon** has an extremely high closure temperature (~900°C), meaning zircon locks in its lead almost immediately upon crystallizing from a magma. This makes U-Pb zircon dating ideal for determining the crystallization age of igneous rocks. The **K-Ar system in muscovite** closes at around 350°C, and in biotite at around 300°C — so these minerals record the time when a rock cooled through those temperatures, not necessarily when it first formed.

This is what makes multi-system dating so powerful. Imagine a granite that crystallized at 800°C deep in a mountain belt, then slowly cooled as the mountains eroded and the rock approached the surface. U-Pb in zircon gives you the crystallization age — say 400 million years ago. Rb-Sr in muscovite (closure ~500°C) might give 380 Ma. K-Ar in biotite (closure ~300°C) gives 360 Ma. K-Ar in feldspar (closure ~150°C) gives 340 Ma. Together, these ages trace out a **cooling path**: you know the rock took 60 million years to cool from 900°C to 150°C, and you can calculate cooling rates and infer how fast the overlying rock was being eroded away. This technique — **thermochronology** — reconstructs the exhumation history of mountain belts and is indispensable in tectonics.

Each system also has practical limitations that determine when it is appropriate to use. K-Ar dating is straightforward but can be reset by later heating events (since argon diffuses easily), so a K-Ar age on a metamorphic rock might date the last metamorphic episode rather than original formation. The **Rb-Sr isochron method** avoids the problem of not knowing initial daughter isotope ratios by analyzing multiple minerals from the same rock and plotting them on an isochron diagram — the slope of the line gives the age. U-Pb dating benefits from having two independent decay chains (²³⁸U→²⁰⁶Pb and ²³⁵U→²⁰⁷Pb), providing a built-in cross-check: if a sample plots on the **concordia curve**, both systems agree and the age is robust; deviations indicate lead loss or other disturbance. For very old rocks (billions of years), the Sm-Nd system is preferred because samarium and neodymium are resistant to weathering and metamorphic resetting. Choosing the right isotope system for a geological question is as important as the measurement itself.
