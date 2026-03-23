---
id: focal-mechanisms-and-stress-tensors
title: Focal Mechanisms and Stress Tensors
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-body-waves-p-and-s
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- moment-tensor-inversion
- seismic-moment-and-magnitude
- subduction-zone-structure-and-dynamics
tags:
- seismology
- focal-mechanism
- stress-tensor
- earthquake-source
stage: expert
status: validated
---

# Focal Mechanisms and Stress Tensors

## Core Idea
The focal mechanism describes the orientation of faulting and stress at an earthquake source using the radiation pattern of seismic waves. A beach ball diagram visualizes P-wave first motions (compressions and dilatations) and defines nodal planes that represent the fault plane and auxiliary plane. The stress tensor encodes the state of stress; its eigenvalues and eigenvectors reveal principal stress directions, which align with plate motions and regional tectonics.

## Questions

```yaml
- question: "A focal mechanism beach ball diagram has two nodal planes. What do these two planes represent?"
  type: multiple-choice
  options: ["The fault plane and the Earth's surface", "The fault plane and the mathematically equivalent auxiliary plane — seismic data alone cannot distinguish which is which", "The two conjugate fault planes that both ruptured during the earthquake", "The horizontal and vertical projections of the fault"]
  answer: 1
  explanation: "The P-wave radiation pattern from a double-couple source is symmetric: two orthogonal nodal planes produce identical first-motion patterns. One is the actual fault plane; the other is the auxiliary (conjugate) plane that is a mathematical artifact of the double-couple model. Seismic waveforms alone cannot distinguish between them — additional geological or geodetic information (e.g., the orientation of a known fault, surface rupture, or aftershock distribution) is needed to identify the true fault plane."

- question: "On a beach ball diagram, the black (compressional) quadrants directly indicate the regions of Earth's surface where the fault ruptured."
  type: true-false
  answer: false
  explanation: "The black and white quadrants indicate the P-wave first-motion pattern at seismometers around the globe, not the geographic location of fault rupture. Black (compressional) quadrants show the directions from which seismometers recorded an initial upward ground motion (compression); white (dilatational) quadrants show initial downward motion. The pattern encodes the geometry of faulting (strike, dip, rake), not fault location."

- question: "The stress tensor at a point in the crust has three principal stress axes (σ₁ ≥ σ₂ ≥ σ₃). In a normal faulting regime, how are these axes typically oriented, and which one drives the fault slip?"
  type: short-answer
  answer: "In a normal faulting regime, σ₁ (maximum compressive stress) is vertical, σ₂ is horizontal intermediate, and σ₃ (minimum, or least compressive) is horizontal. Gravity drives the overburden down, making the vertical stress maximum. The crust extends horizontally, and faults dip steeply, allowing the hanging wall to slide down under gravity. σ₁ being vertical is the defining characteristic of an extensional (normal faulting) stress regime."
  explanation: "Anderson's theory of faulting relates the three fault types to the orientation of principal stresses relative to Earth's surface. Normal faulting: σ₁ vertical. Reverse/thrust faulting: σ₃ vertical (horizontal compression dominates). Strike-slip faulting: σ₂ vertical. Eigenvalues of the stress tensor give the magnitudes of the three principal stresses; eigenvectors give their orientations — which is why eigenvalue decomposition is the core mathematical tool."
```

## Explainer

You know from studying P and S waves that seismic energy radiates outward from an earthquake source in a characteristic pattern depending on the fault geometry. A focal mechanism takes that radiation pattern and works backward: by measuring whether the first ground motion at seismometers in different directions was compressional (upward push) or dilatational (downward pull), seismologists reconstruct the orientation of the faulting that produced it.

The result is displayed as a "beach ball" — a lower-hemisphere stereographic projection of the focal sphere. The sphere is divided into compressional (black) and dilatational (white) quadrants by two perpendicular great circles called nodal planes. These planes mark the directions of zero P-wave radiation. One nodal plane is the actual fault plane; the other is the mathematically equivalent auxiliary plane. The beach ball pattern encodes three angles — strike, dip, and rake — that fully describe the fault geometry. A beach ball that is mostly black at the poles and white at the equator indicates thrust faulting; one with black lobes at the sides indicates normal faulting; a "yin-yang" pattern indicates strike-slip.

The stress tensor is the mathematical framework underlying all of this. At any point in the crust, stress is not a single number but a 3×3 symmetric matrix relating the stress vector on any oriented surface to its components. The eigenvectors of this tensor are the principal stress axes (σ₁ ≥ σ₂ ≥ σ₃) — the three mutually perpendicular directions on which shear stress vanishes and only normal stress acts. Their eigenvalues are the magnitudes of those principal stresses. Faults tend to form and slip in orientations that maximize shear stress relative to normal stress, which depends directly on the principal stress orientations.

Anderson's faulting theory connects stress to fault type with elegant simplicity. Earth's surface is a free surface, so one principal stress axis is always approximately vertical. If σ₁ is vertical (gravity dominates, crust extends horizontally), normal faults develop. If σ₃ is vertical (horizontal compression dominates), reverse or thrust faults form. If σ₂ is vertical (one horizontal direction compresses, the other extends), strike-slip faults result. Reading a beach ball diagram and immediately inferring the tectonic regime — compression, extension, or shear — is a core skill in seismology and tectonics.

Beyond individual earthquakes, catalogues of focal mechanisms across a region reveal the regional stress field. Inverting many focal mechanisms simultaneously (stress tensor inversion) yields the orientation of σ₁, σ₂, and σ₃ for that crust volume. This is how geophysicists map stress patterns along subduction zones, mid-ocean ridges, and transform faults — directly testing plate tectonic models with seismic data.
