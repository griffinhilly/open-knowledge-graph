---
id: seismic-wave-velocity-attenuation
title: Seismic Wave Velocity, Attenuation, and Crustal Structure
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: seismic-waves
  type: soft
tags:
- seismology
- waves
- velocity
stage: advanced
status: draft
---

# Seismic Wave Velocity, Attenuation, and Crustal Structure

## Core Idea
Seismic wave velocities vary systematically with rock type, mineralogy, temperature, pressure, porosity, and pore fluid saturation. Velocity and attenuation anomalies are used in seismic tomography to image crustal and mantle structure, revealing subduction zones, mantle plumes, and other large-scale features.

## Questions

```yaml
- question: "A seismic tomography study images a region beneath a volcanic arc and finds anomalously slow P-wave velocities and very low Q (high attenuation). What is the most geologically plausible interpretation?"
  type: multiple-choice
  options:
    - "The region contains cold, rigid lithosphere that has subducted to depth and is cooling the surrounding mantle"
    - "The region is a zone of hot, partially molten rock — low velocity because high temperature reduces elastic moduli, low Q because molten material dissipates wave energy"
    - "The slow velocity indicates lower-density felsic rock that has been tectonically emplaced into the mantle"
    - "The anomaly reflects a data artifact because P-waves attenuate more in volcanic arcs due to interference from volcanic tremors"
  answer: 1
  explanation: "Slow velocity + low Q (high attenuation) is the diagnostic signature of hot, partially molten rock. Temperature reduces elastic moduli, slowing seismic waves. Partial melt and hot grain boundaries dissipate wave energy efficiently, producing very low Q. A subducting cold slab would appear as fast velocity and high Q (low attenuation) — the opposite signature. This combination of velocity and attenuation anomalies is exactly what seismologists look for to locate magmatic systems and estimate melt fraction beneath volcanic arcs."

- question: "Why do cold, dense subducting slabs appear as fast-velocity anomalies in seismic tomography images?"
  type: multiple-choice
  options:
    - "Subducting slabs contain more iron-rich minerals that transmit seismic waves faster than surrounding mantle"
    - "Cold temperatures stiffen the rock (higher elastic moduli) while density changes are smaller, so the stiffness-to-density ratio increases, raising wave velocity"
    - "Subducting slabs are composed of oceanic crust, which is faster than continental crust at all depths"
    - "Faster velocity in slabs is an artifact of the tomographic inversion caused by the dense network of seismometers near subduction zones"
  answer: 1
  explanation: "Seismic velocity depends on the ratio of elastic moduli to density (V = √(K/ρ)). Cold subducting slabs are stiffer than the surrounding warmer mantle — low temperature means high elastic moduli, meaning the rock resists deformation more strongly. The density difference is proportionally smaller, so the stiffness-to-density ratio is higher, producing faster wave velocities. This is purely a temperature effect: cold = stiff = fast. The same principle explains why wave velocity decreases in the low-velocity zone where temperature is highest relative to pressure."

- question: "Seismic wave velocity always increases with depth throughout Earth's interior because pressure increases monotonically with depth, compressing rock and raising its elastic moduli."
  type: true-false
  answer: false
  explanation: "False. While pressure generally increases velocity, temperature counteracts this effect by softening rock. In the low-velocity zone (LVZ) at roughly 100–200 km depth, temperature rises sharply, partially melting the asthenosphere and reducing elastic moduli enough to overcome the pressure effect — velocity actually decreases with depth in this zone. The competition between pressure (raises velocity) and temperature (lowers velocity) produces Earth's complex layered velocity structure, including this notable exception to the general depth-velocity trend."

- question: "Seismic attenuation (measured by quality factor Q) is a more sensitive indicator of temperature and partial melt than wave velocity alone, because hot and partially molten rock has very low Q."
  type: true-false
  answer: true
  explanation: "True. While both velocity and Q decrease with temperature and melt fraction, attenuation is more sensitive to small amounts of partial melt. Even a fraction of a percent of melt can dramatically lower Q by providing grain boundaries and melt pockets where wave energy is converted to heat. Velocity changes require larger melt fractions to produce detectable anomalies. This is why joint interpretation of velocity and attenuation tomography provides better constraints on melt fraction and temperature than either measurement alone."

- question: "How does seismic tomography use wave velocity anomalies to image Earth's interior, and what do fast versus slow anomalies indicate physically?"
  type: short-answer
  answer: "Seismic tomography records how much earlier or later waves arrive at seismometer stations compared to predictions from a reference Earth model. Earlier arrivals (positive residuals) indicate faster-than-average velocity; later arrivals indicate slower velocity. By inverting thousands of such travel-time residuals from many earthquakes and stations, seismologists build 3D maps of velocity anomalies. Fast anomalies (earlier arrivals) indicate cold, stiff material — typically subducting slabs or cold lithosphere. Slow anomalies (later arrivals) indicate hot, soft material — mantle plumes, partially molten rock under ridges and arcs, or the asthenosphere."
  explanation: "The analogy to medical CT scanning is precise: both techniques reconstruct 3D structure from multiple 1D measurements taken at different angles. In CT scanning, X-ray density variations reveal tissue type; in seismic tomography, velocity variations reveal temperature, composition, and melt fraction. The physical interpretation of fast vs. slow relies on knowing how temperature, pressure, and composition affect elastic moduli and density — exactly the relationships covered in this topic. Attenuation tomography adds a second imaging channel that is particularly sensitive to the presence of partial melt."
```

## Explainer

From your study of seismic waves and elastic wave propagation, you know that P-waves and S-waves travel through solid rock at velocities determined by the material's elastic properties and density. The next step is understanding *why* those velocities vary from place to place — because those variations are the raw data that seismologists use to image the Earth's interior, much as X-ray density variations allow a CT scanner to image the human body.

**Seismic velocity** depends on the ratio of elastic moduli to density. Stiffer materials transmit waves faster; denser materials slow them down. In practice, several factors control this balance. Increasing **pressure** with depth compresses rock, closes pore spaces and microcracks, and increases stiffness — so velocity generally increases with depth. Increasing **temperature**, on the other hand, softens rock and can bring it closer to its melting point, reducing elastic moduli and decreasing velocity. The competition between these two effects produces Earth's layered velocity structure: velocity increases rapidly through the crust and upper mantle (pressure wins), drops in the **low-velocity zone** at 100-200 km depth (temperature wins, partially melting the asthenosphere), then resumes increasing through the deep mantle. **Composition** also matters: mafic rocks (basalt, gabbro) have higher velocities than felsic rocks (granite) at the same conditions, and the velocity jump at the Moho reflects the compositional change from crustal to mantle rocks.

**Attenuation** is the loss of wave energy as seismic waves propagate, beyond the geometric spreading that reduces amplitude with distance. Intrinsic attenuation occurs because real rocks are not perfectly elastic — some energy is converted to heat through internal friction at grain boundaries and along microcracks. Attenuation is quantified by the **quality factor Q**: high Q means low attenuation (the wave travels far with little energy loss), while low Q means rapid energy loss. Hot, partially molten rock has very low Q, while cold, rigid lithosphere has high Q. This makes attenuation a particularly sensitive indicator of temperature and melt fraction — often more sensitive than velocity alone.

**Seismic tomography** exploits velocity and attenuation variations to create three-dimensional images of Earth's interior. The principle is analogous to medical CT scanning: by recording seismic waves from earthquakes at stations around the globe and measuring whether they arrive earlier or later (faster or slower) than predicted by a reference Earth model, seismologists build maps of velocity anomalies. Cold, dense subducting slabs appear as fast (high-velocity) anomalies penetrating deep into the mantle. Hot mantle plumes appear as slow (low-velocity) anomalies rising from the core-mantle boundary. Regions of partial melt beneath mid-ocean ridges and volcanic arcs show up as both low-velocity and high-attenuation anomalies. These images have revolutionized our understanding of mantle convection, confirming that plate tectonics is the surface expression of a whole-mantle circulation system — and they depend entirely on understanding how rock properties control seismic wave velocity and attenuation.
