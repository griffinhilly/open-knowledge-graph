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

## Questions

```yaml
- question: "A global seismic tomography image shows a strong fast-velocity anomaly in the upper mantle extending from beneath a known subduction zone to depths of 700 km. What is the most likely geophysical interpretation?"
  type: multiple-choice
  options:
    - "A large magma chamber fed by decompression melting at the subduction zone"
    - "A region of anomalously high water content, which accelerates seismic wave velocities"
    - "A cold, dense subducting oceanic slab that is seismically faster than the surrounding mantle"
    - "A continental root that has been advected laterally by mantle convection"
  answer: 2
  explanation: "In seismic tomography, fast velocity anomalies indicate cold, dense, or compositionally distinct rock. Subducting slabs are cold oceanic lithosphere descending into the hot mantle — they are the prototypical fast anomaly. Magma chambers are slow (hot, partially molten = low velocity). Water-rich rock typically reduces seismic velocity, not increases it. This interpretive logic — fast = cold/dense, slow = hot/molten — is the key to reading tomographic images."

- question: "Why is regularization (damping and smoothing) required when inverting travel-time data for seismic velocity structure?"
  type: multiple-choice
  options:
    - "To ensure that the resulting velocity model matches previously known geological boundaries exactly"
    - "Because the system is underdetermined in regions with poor ray coverage, so infinitely many velocity models fit the data equally well without constraints"
    - "To prevent the inversion algorithm from recovering velocity anomalies smaller than one kilometer"
    - "Because P-wave and S-wave data must be averaged before inversion to avoid contradiction"
  answer: 1
  explanation: "In regions where earthquakes and seismometers are sparse, few rays pass through those volume elements, leaving the velocity poorly constrained. Without regularization, the inversion can fit the data by placing arbitrary, physically unreasonable velocity anomalies in these unconstrained regions. Damping penalizes large perturbations from the reference model; smoothing penalizes rapid spatial variations. These constraints make the solution physically reasonable at the cost of potentially smoothing over real structure."

- question: "Each individual travel-time measurement in seismic tomography provides a direct measurement of seismic velocity at the specific point in the Earth where the wave spent the most time."
  type: true-false
  answer: false
  explanation: "A travel-time measurement is an integral of slowness (inverse velocity) along the entire ray path — it reflects the cumulative effect of velocities along a potentially thousands-of-kilometer path. There is no single 'most time' point; the measurement is fundamentally non-local. This is exactly what makes tomography an inverse problem: the data (path integrals) are not direct measurements of the quantity we want (local velocities), and recovering local velocities requires solving a system of equations with many overlapping ray paths."

- question: "In seismic tomography, slow velocity anomalies in the mantle typically indicate regions that are hotter, less dense, or partially molten compared to the surrounding mantle."
  type: true-false
  answer: true
  explanation: "Seismic wave velocity increases with density and elastic moduli, which decrease with temperature and melt fraction. Hot regions — mid-ocean ridges, mantle plumes, regions of active volcanism — show up as slow anomalies because elevated temperature reduces elastic stiffness and partial melting creates compliant fluid-solid mixtures that dramatically slow seismic waves. This relationship is the physical basis for using seismology to image temperature and compositional structure that cannot be sampled directly."

- question: "Why is seismic tomography described as an 'inverse problem,' and what fundamental challenge does this pose for interpreting the resulting velocity models?"
  type: short-answer
  answer: "Seismic tomography is an inverse problem because we observe effects (travel-time anomalies at the surface) and must infer causes (velocity anomalies in the interior) — the opposite of the forward problem, which predicts travel times given a known velocity model. The fundamental challenge is non-uniqueness: many different velocity models can fit the same set of travel-time observations equally well, especially in regions with poor ray coverage. Regularization constraints are needed to select a physically reasonable solution, but the choice of constraints shapes the result. Interpreters must always consider resolution — whether a velocity anomaly is real or an artifact of the inversion — and test whether model features are robust to changes in regularization parameters."
  explanation: "This inverse problem structure means that seismic tomography models are never uniquely determined. Resolution tests (like synthetic checkerboard tests) assess which features in the model can actually be recovered given the available ray geometry. A feature visible in the tomography may be real, smeared from nearby structures, or entirely an artifact of data coverage — distinguishing these requires careful uncertainty analysis."
```

## Questions

```yaml
- question: "Seismic waves from a deep earthquake arrive at a recording station 2 seconds earlier than predicted by the reference Earth model. What does this travel-time anomaly most likely indicate about the mantle along that ray path?"
  type: multiple-choice
  options:
    - "The mantle is hotter than average, causing molecules to vibrate faster and waves to travel more quickly"
    - "The mantle is colder, denser, or compositionally distinct (e.g., a subducting slab), producing higher seismic velocity"
    - "The recording station's clock is slightly fast, introducing a systematic error"
    - "The earthquake was shallower than estimated, shortening the ray path"
  answer: 1
  explanation: "Seismic velocity increases with rock stiffness (elastic moduli) and decreases with temperature and partial melt. Cold subducting slabs are stiffer than the surrounding mantle and appear as fast (negative residual) anomalies in tomographic images. Hot material — mantle plumes, mid-ocean ridges — is slower and appears as positive (late-arriving) anomalies. The common misconception is answer A: higher temperature means faster molecular motion thermally, but in solids, higher temperature *reduces* seismic velocity by softening the rock. Seismic velocity is governed by elastic moduli and density, not molecular thermal speed."

- question: "Why must seismic tomography use regularized inversion rather than directly solving the system of linear equations for the velocity model?"
  type: multiple-choice
  options:
    - "Because ray paths are curved, making the relationship between travel time and velocity inherently nonlinear"
    - "Because the system is simultaneously overdetermined (thousands of redundant measurements) and underdetermined (poor ray coverage in some regions), requiring damping and smoothing constraints to produce a stable, geologically reasonable solution"
    - "Because travel-time measurements have random errors that make linear algebra inapplicable"
    - "Because the forward problem (predicting travel times from a velocity model) cannot be expressed as a matrix equation"
  answer: 1
  explanation: "The mathematical challenge is uneven coverage. In well-sampled regions (e.g., under seismically active subduction zones), the system is overdetermined — many crossing rays constrain the velocity well. In poorly sampled regions (e.g., deep mantle under remote ocean areas with few stations), the system is underdetermined — a near-infinite family of velocity models could fit the data equally well. Without regularization (damping toward a smooth or reference model), the inversion amplifies noise in under-sampled cells. Regularization finds the solution that fits the data while remaining physically plausible — the 'minimum structure' model."

- question: "Seismic tomography and medical computed tomography (CT) scanning share the same fundamental mathematical principle: both recover a 3D spatial property by inverting integral measurements along paths through the medium."
  type: true-false
  answer: true
  explanation: "Both techniques solve essentially the same inverse problem. In medical CT, X-rays travel through the body and attenuation is integrated along each ray; the inverse problem recovers tissue density. In seismic tomography, seismic waves travel through the Earth and travel time is integrated along each ray; the inverse problem recovers seismic velocity. The analogy is why the term 'tomography' (from the Greek for 'slice') was borrowed from medical imaging. The key mathematical structure — Radon transform / back-projection / regularized inversion — is the same in both fields."

- question: "The spatial resolution of a seismic tomographic image is uniform throughout the model, because the same number of earthquakes and stations contribute equally to all regions."
  type: true-false
  answer: false
  explanation: "Resolution is entirely dependent on ray coverage — the density and angular diversity of ray paths crossing each region. Well-instrumented continental areas with many nearby earthquakes produce high-resolution images (kilometer scale for crustal studies). Remote oceanic regions with few seismographs and few local earthquakes are poorly sampled; the tomographic image there is highly smoothed and uncertain. Resolution tests (like 'checkerboard tests,' where a synthetic velocity model is recovered to see how well small-scale anomalies are retrieved) are a standard way to map where a tomographic model can be trusted."

- question: "What are travel-time residuals in seismic tomography, and what information do they encode about Earth structure?"
  type: short-answer
  answer: "A travel-time residual is the difference between the observed arrival time of a seismic wave at a station and the predicted arrival time from a reference (1D) Earth model. A negative residual (early arrival) means the wave traveled faster than average — it passed through colder, denser, or compositionally distinct material with higher seismic velocity (e.g., a subducting slab). A positive residual (late arrival) means the wave was slowed — it traversed hotter, partially molten, or fluid-saturated material (e.g., a mantle plume or magma chamber). Each residual represents an integral of the velocity anomaly along the entire ray path, not a point measurement. By assembling thousands of residuals from crossing paths, seismologists set up a linear system whose solution is the 3D velocity model that best explains all the observed residuals simultaneously."
  explanation: "The key insight is that residuals are path integrals — they contain information about every point the ray passed through, not just one location. This is why you need many crossing rays to separate the contributions of different Earth regions, and why sparse coverage leads to ambiguous models. A student who says 'residuals tell you where it's fast or slow' without explaining the path-integral nature misses the core reason tomography is an inverse problem rather than a direct measurement."
```

## Explainer

From your understanding of elastic wave propagation and seismic body waves, you know that P-waves and S-waves travel through rock at speeds determined by the material's elastic properties and density. **Seismic tomography** exploits this relationship in reverse: by measuring how long waves take to travel through the Earth, it reconstructs the velocity structure of the interior — much like a medical CT scan builds an image of the body from X-ray travel times.

The basic data are **arrival times** — the precise moments when seismic waves from an earthquake (or a controlled explosion) reach recording stations around the world or across a survey area. If the Earth had perfectly uniform velocity, these travel times would be predictable from distance alone. In reality, waves that pass through hotter, slower regions arrive late, while waves traversing cold, fast regions arrive early. These **travel-time residuals** — the differences between observed and predicted arrival times — encode information about the velocity anomalies along each ray path.

The mathematical challenge is that each travel-time measurement represents an integral of slowness (inverse velocity) along the entire ray path, not a point measurement. To recover the three-dimensional velocity structure, seismologists divide the Earth (or the region of interest) into a grid of cells and set up a system of linear equations: each equation relates one observed travel-time residual to the sum of slowness perturbations in every cell the ray passes through. With thousands of earthquakes recorded at hundreds of stations, the system is massively overdetermined but also underdetermined in regions with poor ray coverage. **Regularized least-squares inversion** — often using damping and smoothing constraints — finds the velocity model that best fits the data while remaining physically reasonable.

The resolution of the resulting image depends on ray coverage. At the global scale, dense networks of seismographic stations and decades of recorded earthquakes produce images of mantle convection: subducting slabs appear as fast (cold) anomalies plunging through the upper and lower mantle, while mantle plumes and mid-ocean ridges show as slow (hot) anomalies. At regional and crustal scales, controlled-source experiments with dense receiver arrays can achieve resolution of a few kilometers, imaging fault zones, magma chambers, and sedimentary basins. In every case, the interpretive logic is the same: fast velocity anomalies indicate cold, dense, or compositionally distinct rock, while slow anomalies indicate hot, partially molten, or fluid-saturated material. Seismic tomography thus provides the closest thing geophysics has to a direct photograph of Earth's interior.
