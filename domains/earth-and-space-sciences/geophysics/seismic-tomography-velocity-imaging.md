---
id: seismic-tomography-velocity-imaging
title: Seismic Tomography and Velocity Imaging
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: elastic-wave-propagation-in-solids
  type: hard
- id: seismic-body-waves-p-and-s
  type: hard
tags:
- seismology
- tomography
- imaging
- velocity-model
- inverse-problems
stage: advanced
status: draft
---

# Seismic Tomography and Velocity Imaging

## Core Idea
Seismic tomography inverts arrival time data from earthquakes and controlled sources to recover 3D velocity structure of the Earth. Ray theory approximates high-frequency seismic wave propagation as straight rays; travel time anomalies are inverted using regularized least-squares methods to build velocity models. Applications include crustal imaging (high-resolution for exploration), lithospheric structure (10–100 km scale), and mantle structure (global scale), revealing the density, temperature, and composition anomalies that drive plate tectonics.

## Explainer

From your understanding of elastic wave propagation and seismic body waves, you know that P-waves and S-waves travel through rock at speeds determined by the material's elastic properties and density. **Seismic tomography** exploits this relationship in reverse: by measuring how long waves take to travel through the Earth, it reconstructs the velocity structure of the interior — much like a medical CT scan builds an image of the body from X-ray travel times.

The basic data are **arrival times** — the precise moments when seismic waves from an earthquake (or a controlled explosion) reach recording stations around the world or across a survey area. If the Earth had perfectly uniform velocity, these travel times would be predictable from distance alone. In reality, waves that pass through hotter, slower regions arrive late, while waves traversing cold, fast regions arrive early. These **travel-time residuals** — the differences between observed and predicted arrival times — encode information about the velocity anomalies along each ray path.

The mathematical challenge is that each travel-time measurement represents an integral of slowness (inverse velocity) along the entire ray path, not a point measurement. To recover the three-dimensional velocity structure, seismologists divide the Earth (or the region of interest) into a grid of cells and set up a system of linear equations: each equation relates one observed travel-time residual to the sum of slowness perturbations in every cell the ray passes through. With thousands of earthquakes recorded at hundreds of stations, the system is massively overdetermined but also underdetermined in regions with poor ray coverage. **Regularized least-squares inversion** — often using damping and smoothing constraints — finds the velocity model that best fits the data while remaining physically reasonable.

The resolution of the resulting image depends on ray coverage. At the global scale, dense networks of seismographic stations and decades of recorded earthquakes produce images of mantle convection: subducting slabs appear as fast (cold) anomalies plunging through the upper and lower mantle, while mantle plumes and mid-ocean ridges show as slow (hot) anomalies. At regional and crustal scales, controlled-source experiments with dense receiver arrays can achieve resolution of a few kilometers, imaging fault zones, magma chambers, and sedimentary basins. In every case, the interpretive logic is the same: fast velocity anomalies indicate cold, dense, or compositionally distinct rock, while slow anomalies indicate hot, partially molten, or fluid-saturated material. Seismic tomography thus provides the closest thing geophysics has to a direct photograph of Earth's interior.
