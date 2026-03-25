---
id: seismic-velocity-depth-models
title: Seismic Velocity and Depth Models
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: elastic-wave-propagation-in-solids
  type: hard
- id: seismic-waves
  type: hard
builds-toward:
- seismic-ray-tracing-methods
- seismic-tomography-velocity-imaging
tags:
- seismic
- velocity
- modeling
- earth-structure
stage: advanced
status: validated
---

# Seismic Velocity and Depth Models

## Core Idea
Seismic velocity varies with depth due to pressure, temperature, and composition changes in the Earth. Velocity-depth models describe how P-wave and S-wave velocities increase through the crust and mantle, creating the layered structure used in all seismic ray tracing and wave propagation studies. Understanding velocity structures is essential for converting seismic travel times to depth and for inferring Earth's internal composition.

## Questions

```yaml
- question: "Seismologists observe that S-waves from deep earthquakes never arrive at recording stations on the opposite side of the Earth. The most direct inference is:"
  type: multiple-choice
  options:
    - "S-waves are absorbed by the high-density iron of the lower mantle before reaching the core"
    - "S-wave velocities are too slow to traverse the full Earth within the observation window"
    - "The outer core is liquid, and shear waves cannot propagate through fluids"
    - "The inner core reflects all S-waves back toward the source hemisphere"
  answer: 2
  explanation: "S-waves (shear waves) require a solid medium for propagation — they deform material in a direction perpendicular to travel, which fluids cannot sustain. The absence of S-waves beyond ~103° from the epicenter (the S-wave shadow zone) is the definitive evidence that the outer core is liquid. P-waves, which compress material longitudinally, can travel through liquids — and they do arrive at the other side (though refracted), confirming the core is there. This is not an assumption; it is directly inferred from seismic wave behavior."

- question: "In a seismic velocity-depth profile, the low-velocity zone between approximately 80 and 200 km depth is caused by:"
  type: multiple-choice
  options:
    - "The compositional boundary where continental crust transitions to oceanic crust"
    - "The Mohorovičić discontinuity, where crustal granitic rock gives way to mantle peridotite"
    - "Partial melting and elevated temperatures in the asthenosphere reducing the shear modulus"
    - "Pressure-induced phase transitions in olivine crystal structure at those depths"
  answer: 2
  explanation: "Below the lithosphere, temperatures in the asthenosphere are high enough to partially melt mantle rock (~1–2% melt fraction). Even a small amount of melt dramatically reduces the shear modulus (G), which lowers both Vp and Vs despite the fact that pressure is increasing. This creates an anomalous velocity decrease — a 'low-velocity zone' — that is the seismological signature of the weak, partially molten asthenosphere. Option B (the Moho) occurs at ~35 km (continental) and ~7 km (oceanic) depth — far shallower. Option D (olivine phase transitions) occurs at 410 and 660 km — far deeper, and those transitions increase velocity."

- question: "Seismic tomography expresses its results as velocity perturbations — percentage deviations from a reference model — rather than absolute velocities."
  type: true-false
  answer: true
  explanation: "True. Reference models like PREM define a one-dimensional baseline velocity-depth profile representing the average Earth. Tomographic studies compare observed seismic travel times to those predicted by the reference model and invert for velocity anomalies — regions that are faster (typically colder, e.g., subducting slabs) or slower (typically hotter, e.g., mantle plumes) than average. Expressing results as perturbations rather than absolute velocities removes the baseline and highlights the three-dimensional heterogeneity that is the actual scientific target."

- question: "Seismic velocity generally decreases with depth throughout the Earth's mantle because increasing temperature progressively lowers the elastic moduli."
  type: true-false
  answer: false
  explanation: "False. The dominant trend in the mantle is a *velocity increase* with depth, not a decrease. Although temperature rises with depth and acts to lower elastic moduli, the effect of increasing pressure — which stiffens rock by compressing it — outpaces the temperature effect throughout most of the mantle. Velocity only decreases locally in the low-velocity zone (asthenosphere, ~80–200 km) where partial melting is sufficient to reduce the shear modulus. Below this zone, velocity resumes its upward trend through the transition zone and lower mantle."

- question: "Why is a velocity-depth model necessary before a seismologist can locate an earthquake, and what would happen to location estimates if the model were wrong?"
  type: short-answer
  answer: "Earthquake location works by measuring the difference in arrival times of seismic waves at multiple stations and inverting for the source position. This requires knowing how fast the waves travel along each path — which depends on the velocity structure of the Earth they pass through. If the velocity model is wrong, the predicted travel times will be wrong, and the best-fit source location will be systematically displaced from the true location. In regions where the velocity model is poorly known (e.g., subduction zones with anomalous structure), earthquake location errors of tens of kilometers are common, which matters enormously for understanding fault geometry and seismic hazard."
  explanation: "This question connects the abstract concept of velocity models to their practical function. Students often treat velocity models as background knowledge rather than active tools. The key insight is that every seismological result — earthquake locations, depth estimates, fault mechanisms — is model-dependent. Improving velocity models (via tomography) directly improves every downstream analysis."
```

## Explainer

From elastic wave propagation, you know that seismic velocities depend on the elastic moduli and density of the medium: Vp = √((K + 4G/3)/ρ) for P-waves and Vs = √(G/ρ) for S-waves. A velocity-depth model applies these relationships to the real Earth, specifying how Vp and Vs change from the surface to the core. These models are the foundation for everything in observational seismology — without them, you cannot convert a travel time into a depth or locate an earthquake.

The broad pattern is straightforward: **velocity generally increases with depth** because increasing pressure raises elastic moduli faster than it raises density. In the crust, P-wave velocities range from about 5.5–6.5 km/s in typical continental crust (granitic to granodioritic composition) to 6.5–7.0 km/s in oceanic crust (basaltic). At the **Mohorovičić discontinuity** (Moho), velocity jumps sharply to ~8.0 km/s as the composition changes from crustal rocks to olivine-rich mantle peridotite. Through the upper mantle, velocity continues to increase with depth except in the **low-velocity zone** (roughly 80–200 km depth), where partial melting and high temperatures reduce the shear modulus enough to decrease both Vp and Vs — this zone is the seismological signature of the asthenosphere.

Below the low-velocity zone, velocity increases steadily through the transition zone (410–660 km), where olivine undergoes pressure-induced phase transitions to denser crystal structures (wadsleyite, then ringwoodite), producing sharp velocity jumps at those depths. The lower mantle (660–2,890 km) shows a smooth velocity gradient until the **D″ layer** just above the core-mantle boundary, where heterogeneity and ultra-low-velocity zones signal the complex thermal and chemical boundary between silicate mantle and liquid iron core. At the core-mantle boundary itself, P-wave velocity drops dramatically (from ~13.7 to ~8.0 km/s) and **S-waves vanish entirely** — the definitive evidence that the outer core is liquid, since shear waves cannot propagate through fluids.

Reference models like **PREM** (Preliminary Reference Earth Model) and **IASP91** provide standardized one-dimensional velocity-depth profiles that serve as starting points for all seismological analysis. When a seismologist locates an earthquake, they trace rays through such a model using Snell's law to predict arrival times at each station, then adjust the source location until predicted and observed times match. When a tomographer images a mantle plume or subducting slab, they express their results as velocity *perturbations* relative to a reference model — percentage deviations that reflect temperature and composition anomalies. The reference model is thus the common language that connects raw seismograms to three-dimensional Earth structure.
