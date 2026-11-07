---
id: divergence-theorem
title: Divergence Theorem
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: flux-integrals
  type: hard
- id: triple-integrals
  type: hard
- id: divergence-theorem-applications
  type: soft
- id: curl-divergence
  type: hard
- id: greens-theorem
  type: soft
builds-toward:
- applications-multivariable
tags:
- divergence
- flux
stage: formal-systems
status: validated
---
# Divergence Theorem

## Core Idea
Divergence theorem: ∬_S F · dS = ∭_W (∇·F) dV, where S is the closed surface bounding W (outward normal). This relates flux through a closed surface to divergence integrated over the volume.

## How It's Best Learned
Slice the region into many small boxes. For each box, the outward flux is about (∇·F) times its volume. Where two boxes share a face, one box's outflow is the other's inflow, so those terms cancel. Only faces on the outer surface survive. Sketching this in 2D with a grid of squares makes the cancellation visible before the 3D statement.

## Common Misconceptions
- The surface integral and the volume integral use the same integrand. (The surface side integrates F · n, while the volume side integrates the scalar ∇·F, a derivative of F.)
- Divergence at a point tells you the flux through the whole surface. (Divergence is a local rate per unit volume; the theorem needs it integrated over every point of W.)
- The theorem gives the flux through each piece of the surface, such as one face of a cube. (It gives only the total flux through the whole closed surface; to get one piece, you must subtract the flux through the other pieces.)
- The theorem works for any field you can write down. (It requires F to have continuous first partial derivatives throughout W and S to be closed and piecewise smooth.)

## Questions

```yaml
- question: "If the divergence of F is the constant 3 everywhere, and the region W has volume 4, what is the total outward flux of F through the boundary surface S?"
  type: multiple-choice
  options: ["3", "4", "12", "Cannot be determined without knowing the surface"]
  answer: 2
  explanation: "By the divergence theorem, flux = ∭_W (∇·F) dV = ∭_W 3 dV = 3 × (volume of W) = 3 × 4 = 12. Because ∇·F is constant, it factors out of the integral, leaving just the volume. Notably, the shape of the surface is irrelevant — only the enclosed volume matters."

- question: "The divergence theorem applies to any open surface, not just closed surfaces."
  type: true-false
  answer: false
  explanation: "The divergence theorem requires S to be a closed surface — one that completely encloses a three-dimensional region W with no boundary. An open surface (like a hemisphere without a base) has a boundary curve, and the appropriate theorem for that case is Stokes' theorem, not the divergence theorem. The outward normal on a closed surface points away from the enclosed region at every point."

- question: "What does it mean physically when ∇·F = 0 everywhere inside a region W?"
  type: short-answer
  answer: "The net outward flux through any closed surface inside the region is zero — there are no sources or sinks of the field inside W. Whatever flows in must flow out."
  explanation: "Divergence measures source density: positive divergence indicates a source (field spreading outward), negative divergence a sink (field converging inward). When ∇·F = 0 throughout W, the divergence theorem gives ∬_S F·dS = ∭_W 0 dV = 0. In fluid flow, this is incompressibility: mass is neither created nor destroyed in the region. In electrostatics, ∇·E = 0 in a charge-free region (from Gauss's law)."
```

## Explainer

You have computed flux integrals — the integral of a vector field F dotted with the outward normal over a surface — and triple integrals over solid regions. The divergence theorem is the bridge between these two operations: it says that the total outward flux through a closed surface equals the integral of the divergence of F over the enclosed volume.

The physical intuition is about sources and sinks. Think of F as the velocity field of a fluid. Divergence at a point measures how much the fluid is "spreading out" (positive divergence = source, like water from a faucet) or "converging" (negative divergence = sink, like a drain). If you enclose a region in a surface, the total flow escaping through the surface must equal the total amount being generated inside — that is exactly what the divergence theorem says. If ∇·F = 0 everywhere, nothing is being created or destroyed, and the net outward flux is zero regardless of which closed surface you choose.

The divergence theorem is the three-dimensional analogue of the Fundamental Theorem of Calculus. Just as ∫_a^b f'(x) dx = f(b) - f(a) relates a derivative over an interval to values at the boundary, the divergence theorem relates the divergence (a kind of derivative) integrated over a volume to the flux through the boundary surface. This pattern — "integral of a derivative over a region equals an integral over the boundary" — runs through all the major theorems of vector calculus: the FTC, Green's theorem (2D), Stokes' theorem (surfaces), and the divergence theorem (volumes).

The main practical use of the divergence theorem is simplification: computing a surface integral directly can be painful (especially for awkward surfaces), but computing the divergence and integrating over the volume may be far easier. The reverse is also sometimes useful — if the triple integral is hard but the surface is simple, you can compute the surface integral instead. As with all the vector calculus theorems, the key condition is that F must have continuous first-order partial derivatives throughout the region, and S must be a closed, piecewise-smooth surface with outward-pointing normals.

Watch out for the closed-surface requirement. Open surfaces (like a paraboloid cap without a base) are handled by Stokes' theorem, not the divergence theorem. If a surface is not closed, you can sometimes *make* it closed by adding a convenient cap or base, apply the divergence theorem to the closed surface, then subtract the flux through the piece you added. This strategy is a common technique for difficult flux computations.

