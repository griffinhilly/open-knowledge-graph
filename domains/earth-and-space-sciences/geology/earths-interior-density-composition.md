---
id: earths-interior-density-composition
title: 'Earth''s Interior: Density and Composition'
domain: earth-and-space-sciences
course: geology
prerequisites: []
builds-toward:
- lithosphere-asthenosphere-layers
- isostasy-density-equilibrium
tags:
- structure
- density
- composition
- crust-mantle
stage: abstract-reasoning
status: validated
---

# Earth's Interior: Density and Composition

## Core Idea
Earth's interior increases in density and temperature with depth due to increasing pressure and changing mineral composition. The crust (~10-70 km) is compositionally distinct from the denser mantle below, creating a fundamental density boundary. Iron-rich material in the core distinguishes it from silicate layers above.

## How It's Best Learned
Use density profiles and velocity-depth curves from seismic data to infer composition. Compare crustal samples from drilling with computed properties.

## Common Misconceptions
- Earth's layers are defined only by temperature, not composition.
- Density increases uniformly with depth.

## Questions

```yaml
- question: "At approximately 660 km depth, seismic wave velocities change abruptly. What best explains this discontinuity?"
  type: multiple-choice
  options:
    - "The chemical composition changes from silicate rock to iron-rich material"
    - "Minerals undergo a phase transition to denser crystal structures without changing chemical composition"
    - "Temperature drops sharply, causing rock to become more rigid"
    - "This is the core-mantle boundary where rock transitions to liquid iron"
  answer: 1
  explanation: "The 660 km discontinuity is a phase transition: olivine-family minerals transform into denser bridgmanite under pressure. The chemical composition remains silicate throughout — only the crystal structure changes. The iron-rich core boundary is much deeper (~2,900 km). Temperature generally increases, not decreases, with depth. Distinguishing phase-change layering from compositional layering is a key insight in this topic."

- question: "What is the primary seismological evidence that Earth's outer core is liquid?"
  type: multiple-choice
  options:
    - "Drilling samples from the outer core contain liquid iron"
    - "S-waves do not pass through the outer core, while P-waves do"
    - "Temperature measurements show material exceeds the melting point throughout the outer core"
    - "The density of the outer core exceeds that of any known solid material"
  answer: 1
  explanation: "S-waves (shear waves) cannot propagate through liquids because liquids do not resist shear stress. When S-waves disappear at the core-mantle boundary (~2,900 km) but P-waves continue, geophysicists conclude the outer core is liquid. Direct sampling is impossible — the deepest drilling projects have only reached ~12 km. Temperature measurements at those depths are extrapolated, not directly observed."

- question: "Oceanic crust is denser than continental crust because it contains more iron- and magnesium-rich basaltic rock."
  type: true-false
  answer: true
  explanation: "Oceanic crust (~3.0 g/cm³) is basaltic — relatively rich in iron and magnesium. Continental crust (~2.7 g/cm³) is more granitic, dominated by lighter silicon- and aluminum-rich minerals. This density difference is tectonically important: when oceanic and continental plates collide, the denser oceanic plate subducts. The compositional difference, not just density, drives this behavior."

- question: "Density increases smoothly and continuously from Earth's surface to its center."
  type: true-false
  answer: false
  explanation: "Density increases in steps, not smoothly. Compositional boundaries — the Moho (crust-mantle) at ~35 km average depth and the core-mantle boundary at ~2,900 km — produce abrupt density jumps. Phase transitions within the mantle at ~410 km and ~660 km add additional steps. Within each layer, density does increase gradually with pressure, but the overall depth profile is a staircase, not a ramp."

- question: "How do seismic waves allow geophysicists to determine the composition and physical state of Earth's interior layers without directly sampling them?"
  type: short-answer
  answer: "Seismic waves change speed when they cross boundaries between materials with different density, rigidity, or physical state. P-waves (compressional) travel through both solids and liquids; S-waves (shear) travel only through solids. Abrupt velocity changes reveal compositional or phase boundaries — for instance, the Moho marks the sharp transition from lighter crustal rock to denser mantle rock. The disappearance of S-waves at ~2,900 km reveals the outer core is liquid. Speed profiles within layers, compared against laboratory experiments on minerals at high pressure and temperature, allow identification of specific mineral compositions at each depth."
  explanation: "This indirect method is analogous to medical imaging — you send waves through an opaque body and infer internal structure from how the waves are altered. The combination of P-wave and S-wave behavior is especially powerful: P-waves alone can't distinguish solid from liquid, but the S-wave shadow zone directly reveals where liquid exists."
```

## Explainer

Earth is not uniform inside — it is layered, and the layering is defined by two distinct properties: **composition** (what material is present) and **mechanical behavior** (how that material responds to stress). The compositional layers are the most fundamental. The outermost layer, the **crust**, is thin (5–10 km under oceans, 30–70 km under continents) and composed of relatively light silicate rocks. Oceanic crust is basaltic (density ~3.0 g/cm³), while continental crust is more granitic (density ~2.7 g/cm³). Below the crust lies the **mantle**, a thick shell of denser silicate rock (density ~3.3–5.5 g/cm³) dominated by minerals like olivine and pyroxene. At the center sits the **core**, composed primarily of iron and nickel, with density reaching ~13 g/cm³ at Earth's center.

How do we know what is inside a planet we cannot directly access below the first few kilometers? The answer is **seismic waves**. When earthquakes generate waves that travel through Earth's interior, their speed changes at boundaries between materials of different density and rigidity. P-waves (compressional) travel through both solids and liquids; S-waves (shear) travel only through solids. The sharp velocity change at the **Mohorovičić discontinuity** (Moho) at the base of the crust marks the compositional transition from crustal rock to denser mantle rock. Deeper, S-waves disappear entirely at the outer core boundary — revealing that the outer core is liquid iron. These velocity-depth profiles, combined with laboratory experiments on minerals at high pressures, allow geophysicists to reconstruct the density and composition of each layer.

The density increase with depth is not smooth — it occurs in steps that correspond to compositional boundaries and phase transitions. Within the mantle, increasing pressure forces minerals into denser crystal structures even though composition changes relatively little. At about 410 km depth, olivine transforms to a higher-density structure (wadsleyite), and at 660 km, another transition produces even denser minerals (bridgmanite). These **phase transitions** cause abrupt jumps in seismic velocity without requiring a change in chemical composition. Understanding this distinction — between compositional layering and phase-change layering — is essential for interpreting Earth's interior structure correctly and forms the foundation for understanding why tectonic plates move, why some regions of the mantle convect differently from others, and how Earth has differentiated over geologic time.
