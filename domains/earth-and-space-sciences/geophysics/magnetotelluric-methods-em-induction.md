---
id: magnetotelluric-methods-em-induction
title: Magnetotelluric Methods and Electromagnetic Induction
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: earths-magnetic-dipole-field-basics
  type: hard
tags:
- electromagnetic
- magnetotelluric
- induction
- conductivity
stage: advanced
status: draft
---

# Magnetotelluric Methods and Electromagnetic Induction

## Core Idea
Magnetotelluric (MT) methods measure natural time-varying electric and magnetic fields (sourced by solar wind–magnetosphere coupling and thunderstorms) to probe electrical conductivity structure to mantle depths. At each frequency, the impedance tensor Z relates orthogonal E and B field components; its phase and magnitude yield apparent resistivity and impedance tensor orientation. 3D MT inversions reveal high-conductivity zones (fluid-rich, partial melt, hydrated minerals), making MT particularly sensitive to volatile distribution in subduction zones and beneath volcanoes.

## Explainer

From your study of Earth's magnetic field, you know that the planet sits within a dynamic electromagnetic environment — the geomagnetic field fluctuates on timescales from seconds to years due to solar wind interactions and ionospheric currents. The magnetotelluric method exploits these natural fluctuations as a free source of electromagnetic energy. Instead of generating an artificial signal (as active-source methods do), MT simply listens to the natural electric and magnetic fields at Earth's surface and uses them to image conductivity structure at depth. This makes MT uniquely capable of probing to depths of hundreds of kilometers without any heavy equipment — just sensitive electric and magnetic field sensors deployed at the surface.

The physics relies on **electromagnetic induction**. Time-varying magnetic fields from external sources induce electric currents in the conductive Earth (the same principle behind a transformer). These induced currents generate their own secondary magnetic fields. The key insight is that the **penetration depth** of electromagnetic energy depends on frequency: high-frequency signals are attenuated quickly and probe only shallow structure, while low-frequency signals penetrate deeper. This relationship is captured by the **skin depth** — the depth at which the signal amplitude decays to about 37% of its surface value. Skin depth increases with both lower frequency and higher resistivity, so by measuring the response across a range of frequencies, you effectively scan from the surface down through the crust and into the mantle.

At each measurement site, you record two horizontal components of the electric field (Ex, Ey) and two of the magnetic field (Bx, By). The relationship between them is encoded in the **impedance tensor** Z, a 2×2 complex matrix: E = Z × B. The elements of Z contain all the information about subsurface conductivity structure. From Z, you calculate **apparent resistivity** (how resistive the ground appears at each frequency) and **phase** (the time lag between E and B variations). Plotting these quantities against frequency produces sounding curves — the MT equivalent of a depth profile. A conductive layer at depth shows up as a drop in apparent resistivity at the frequency corresponding to that layer's depth.

The real power of MT emerges in multi-dimensional imaging. A single site gives a 1D sounding, but deploying arrays of stations across a region enables **2D and 3D inversions** — computational algorithms that find the conductivity model best fitting all the data simultaneously. These inversions routinely resolve features like magma chambers beneath volcanoes (appearing as high-conductivity anomalies), zones of aqueous fluid release above subducting slabs, and graphite-bearing shear zones in ancient continental crust. Because fluids and melts are far more conductive than dry rock, MT is especially sensitive to the volatile pathways that control volcanism, earthquake generation, and ore deposit formation — making it a complement to seismic methods, which image structure through elastic properties rather than electrical ones.
