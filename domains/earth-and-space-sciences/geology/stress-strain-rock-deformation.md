---
id: stress-strain-rock-deformation
title: 'Stress and Strain: Rock Deformation Fundamentals'
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: plate-tectonics-driving-forces
  type: hard
builds-toward:
- brittle-ductile-transition
- fault-mechanics-rupture
tags:
- stress
- strain
- deformation
- mechanics
stage: advanced
status: validated
---

# Stress and Strain: Rock Deformation Fundamentals

## Core Idea
Stress (force per unit area) applied to rock causes strain (deformation). Stress is a 3D tensor with principal stresses oriented in three directions; strain relates to changes in shape and volume. The stress field orientation determines which existing faults will slip and in what direction.

## How It's Best Learned
Draw Mohr circles to analyze stress states. Use focal mechanisms from earthquakes to infer crustal stress orientations.

## Common Misconceptions
- Stress and pressure are identical.
- Rocks deform uniformly in all directions under stress.
- Strain is always permanent.

## Questions

```yaml
- question: "Two crustal regions have identical lithostatic pressure (weight of overlying rock), but one lies near a converging plate boundary with added horizontal compression. A fault develops only in the second region. The best explanation is:"
  type: multiple-choice
  options:
    - "The converging boundary region has higher total pressure, and pressure alone drives fracture when it exceeds rock strength"
    - "The converging boundary adds horizontal stress, creating a non-uniform stress field that generates shear stress on favorably oriented planes, enabling fracture"
    - "The converging boundary region is warmer, reducing rock strength and allowing fracture under the same pressure conditions"
    - "Stress and pressure are equivalent, so both regions should behave identically — another explanation must account for the difference"
  answer: 1
  explanation: "This targets the key misconception: pressure and stress are not the same. Pressure is isotropic — it pushes equally in all directions and produces no net shear on any plane. Tectonic stress is directional; different principal stress magnitudes in different directions create shear stress on planes oblique to the principal axes. Shear stress is what drives slip on faults. The converging boundary adds compressive stress in one direction (not all directions), creating the anisotropic stress field that generates shear on the fault plane. Uniform pressure — even very high pressure — does not produce shear."

- question: "According to Anderson's theory of faulting, what primarily determines which type of fault (normal, reverse, or strike-slip) forms in a given region?"
  type: multiple-choice
  options:
    - "The total magnitude of differential stress — higher stress produces reverse faults; lower stress produces normal faults"
    - "The orientation of the maximum principal stress (σ₁) relative to the Earth's surface"
    - "The temperature and depth at which deformation occurs — deeper rocks form reverse faults; shallow rocks form normal faults"
    - "The composition of the rock — mafic rocks form strike-slip faults; felsic rocks form normal faults"
  answer: 1
  explanation: "Anderson's theory identifies the Earth's surface as a free boundary (no shear stress), which constrains one principal stress to be vertical (the others are horizontal). The fault type then depends on which principal stress is vertical: σ₁ vertical → normal fault (extensional regime — the crust is being pulled apart); σ₃ vertical (σ₁ horizontal) → reverse fault (compressional regime); σ₂ vertical (σ₁ and σ₃ both horizontal) → strike-slip fault. This elegant framework connects observed fault geometry directly to the regional stress field orientation."

- question: "Elastic strain in rocks is permanent — once rock deforms elastically under tectonic stress, it does not return to its original shape when that stress is removed."
  type: true-false
  answer: false
  explanation: "Elastic strain is by definition reversible. Like a spring or rubber band, rock deforming elastically stores strain energy and returns to its original shape when stress is removed. Permanent deformation requires either plastic (ductile) flow or brittle fracture. In the context of the earthquake cycle, rocks in the upper crust accumulate elastic strain energy as tectonic stress builds; when fracture occurs on a fault, that stored elastic energy is suddenly released as seismic waves. The elastic rebound theory of earthquakes depends on this reversibility."

- question: "Increasing pore fluid pressure in a fault zone can promote fault slip even if the applied tectonic stress remains unchanged."
  type: true-false
  answer: true
  explanation: "Pore fluid pressure acts against normal stress on the fault plane, reducing the *effective* normal stress (σ_effective = σ_applied − Pf). On a Mohr diagram, this shifts the circle leftward toward the failure envelope without changing its size. If the circle was previously just below the failure envelope, an increase in fluid pressure can push it to failure. This is why elevated pore pressures in fault zones (from fluid injection, metamorphic dehydration reactions, or seasonal groundwater changes) can trigger earthquakes without any change in tectonic loading."

- question: "Why do earthquakes occur primarily in the upper 15–20 km of the crust, even though tectonic stresses are present throughout the lithosphere?"
  type: short-answer
  answer: "Earthquakes require brittle fracture — sudden displacement along a fault. Brittle behavior requires that rocks be cold and under relatively low confining pressure, conditions found only in the shallow upper crust. Below about 15–20 km, increasing temperature and confining pressure promote plastic (ductile) deformation: rocks flow and bend rather than fracturing. This ductile flow dissipates stress gradually and continuously rather than storing and releasing it suddenly. The brittle-ductile transition depth marks the base of the seismogenic zone. Below it, stress is still present and deformation still occurs, but the mechanism is continuous creep rather than stick-slip faulting."
  explanation: "The depth of the brittle-ductile transition varies with geothermal gradient, rock composition, and strain rate — it is shallower in warm continental crust and deeper in cold oceanic subduction zones, which is why subduction zone earthquakes can occur much deeper than typical continental earthquakes."
```

## Explainer

From your understanding of plate tectonics and the forces driving plate motion, you know that enormous forces act on Earth's lithosphere — ridge push, slab pull, mantle drag. These forces create **stress** within the rock, and the rock's response to that stress — its **strain** — produces the faults, folds, and fractures that geologists map in the field. Understanding the relationship between stress and strain is the gateway to structural geology and earthquake mechanics.

**Stress** is force per unit area, but unlike simple pressure (which pushes equally in all directions), tectonic stress is directional. It is described mathematically as a **tensor** — a quantity that captures force intensity in every direction simultaneously. At any point in the crust, the stress state can be resolved into three mutually perpendicular **principal stresses**: σ₁ (the maximum), σ₂ (the intermediate), and σ₃ (the minimum). No shear stress acts along these principal directions — they represent the orientations where stress is purely compressional or tensional. The relative magnitudes and orientations of these three principal stresses determine what kind of deformation occurs. When σ₁ is vertical (lithostatic load dominates), normal faults form. When σ₁ is horizontal, you get reverse faults (if σ₃ is vertical) or strike-slip faults (if σ₂ is vertical). This framework — formalized as **Anderson's theory of faulting** — connects the stress field directly to fault type.

**Strain** is the deformation that results from applied stress. It can be **elastic** (reversible, like stretching a rubber band — remove the stress and the rock returns to its original shape), **plastic** (permanent deformation without fracture, like bending a metal bar), or **brittle** (fracture and discrete displacement along faults). Whether a rock deforms elastically, plastically, or brittly depends on the rock type, temperature, pressure, strain rate, and presence of fluids. At shallow depths in the upper crust, rocks are cold and under low confining pressure, so they behave brittly — they fracture. At greater depths, higher temperature and pressure promote plastic flow. This is why earthquakes are concentrated in the upper 15–20 km of the crust: below that, rocks deform by flowing rather than breaking.

The tool that ties stress and strain together visually is the **Mohr circle** — a graphical representation of the stress state on planes of all possible orientations within a rock. On a Mohr diagram, you plot normal stress on the horizontal axis and shear stress on the vertical axis. The circle defined by σ₁ and σ₃ shows the stress resolved on every plane. When the circle touches the **failure envelope** (defined by the rock's cohesion and internal friction angle), fracture occurs on the plane corresponding to that point. This predicts both the stress conditions required for failure and the orientation of the resulting fracture. Mohr circles make abstract tensor mathematics tangible: you can see how increasing pore fluid pressure (which shifts the circle leftward toward the failure envelope) promotes faulting, or how increasing confining pressure (expanding the circle rightward) suppresses it.
