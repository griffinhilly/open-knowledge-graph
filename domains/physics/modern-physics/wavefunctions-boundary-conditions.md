---
id: wavefunctions-boundary-conditions
title: Wavefunctions and Boundary Conditions
domain: physics
course: modern-physics
prerequisites:
- id: schrodinger-equation-time-dependent
  type: hard
builds-toward:
- probability-amplitude-interpretation
- particle-in-box-1d
tags:
- quantum-mechanics
- boundary-conditions
stage: advanced
status: draft
---

# Wavefunctions and Boundary Conditions

## Core Idea
Wavefunctions must be continuous, single-valued, and normalizable; at potential barriers they must vanish (or approach zero). These boundary conditions arise from the physical requirement that the wavefunction represents probability and from continuity of the probability current. Boundary conditions quantize energy levels: only certain discrete energies satisfy both the Schrödinger equation and the boundary conditions.

## How It's Best Learned
Solve the particle-in-a-box problem explicitly, deriving the quantization condition from boundary conditions. Visualize low-energy wavefunctions to see how nodes emerge.

## Explainer

The time-dependent Schrödinger equation is a differential equation, and like all differential equations it requires boundary conditions to select a unique solution from the infinitely many functions that satisfy the equation in its interior. The physical interpretation of the wavefunction — that |ψ(x)|² is a probability density — immediately constrains what ψ can do. A probability density must be non-negative and integrable over all space (so the total probability is 1), which means ψ must be **normalizable**: it cannot blow up at infinity or diverge anywhere. At hard walls (infinite potential), there is zero probability of finding the particle inside the wall, so ψ must vanish at the boundary.

Two further conditions complete the set. First, ψ must be **continuous** everywhere: a jump discontinuity in ψ would require an infinite probability current at that point, which is unphysical (it would imply particles teleporting). Second, the derivative dψ/dx must also be continuous wherever the potential is finite — a discontinuous slope would require an infinite kinetic energy (since the kinetic energy operator involves the second derivative). The exception is an *infinite* potential step, where dψ/dx can be discontinuous because the infinite potential can supply an infinite force. These three rules — normalizability, continuity of ψ, and continuity of dψ/dx at finite potentials — are the complete set of wavefunction boundary conditions.

The particle-in-a-box illustrates how these conditions produce **energy quantization**. Inside the box (0 < x < L), the Schrödinger equation gives sinusoidal solutions ψ(x) = A sin(kx) + B cos(kx). The boundary condition ψ(0) = 0 forces B = 0, leaving ψ(x) = A sin(kx). The boundary condition ψ(L) = 0 then requires sin(kL) = 0, which means kL = nπ for positive integers n = 1, 2, 3, ... Each allowed value of k corresponds to one allowed energy E = ℏ²k²/(2m) = n²π²ℏ²/(2mL²). The quantization did not come from assuming energy is discrete — it came from enforcing the boundary conditions. Continuous energies would correspond to wavefunctions that do not vanish at the walls: they are solutions to the differential equation but not physically acceptable ones.

The number of **nodes** (zero crossings inside the box) equals n−1 for the nth energy level. This is a general pattern in quantum mechanics: the ground state has no nodes, the first excited state has one, and higher states have more. Nodes accumulate kinetic energy because more oscillations mean a larger second derivative of ψ — physically, more curvature in the wavefunction means the particle has more kinetic energy on average. This node-counting rule, forced by boundary conditions, is why energy levels are ordered the way they are and why no two bound eigenstates have the same energy in a one-dimensional confining potential.
