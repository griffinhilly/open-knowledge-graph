---
id: maxwell-stress-tensor-forces
title: Maxwell Stress Tensor and Field Forces
domain: physics
course: electrodynamics
prerequisites:
- id: maxwell-stress-tensor
  type: hard
- id: em-field-momentum-density
  type: hard
tags:
- stress-tensor
- field-forces
- radiation-pressure
stage: advanced
status: draft
---

# Maxwell Stress Tensor and Field Forces

## Core Idea
The Maxwell stress tensor T_ij represents the flow of electromagnetic momentum. Its divergence gives the force density on matter, enabling calculation of electromagnetic pressure, tension, and forces between current-carrying conductors without explicit use of Lorentz force.

## Explainer

The Lorentz force law **f** = ρ**E** + **J** × **B** gives the force density on charges and currents directly. But integrating this over complex geometries is often difficult, especially when the charge/current distribution is itself a response to the field. The **Maxwell stress tensor** provides an equivalent but often more powerful method: instead of integrating over the sources, you integrate over a surface enclosing them. The force on everything inside the surface equals the flux of EM momentum through the surface — an approach analogous to using a Gaussian surface for flux instead of integrating over all charges.

The stress tensor T_ij has a concrete physical meaning: it is the flux of the i-th component of momentum in the j-th direction. The diagonal components represent **pressure** (force per unit area perpendicular to a surface), while the off-diagonal components represent **shear stress** (force per unit area parallel to a surface). Electric fields push along field lines (tension) and push outward perpendicular to them (pressure); magnetic fields similarly create tension along field lines and pressure perpendicular to them. The familiar result that field lines "want to be as short as possible" (tension) and "want to spread out sideways" (pressure) comes directly from the stress tensor's sign structure.

To find the force on an object, choose any closed surface S enclosing the object and evaluate **F** = ∮ T̄ · d**A** − ε₀μ₀ d/dt ∫**S** dV, where **S** = **E** × **H** is the Poynting vector. For static fields the time derivative vanishes and the force is purely the surface integral of the stress tensor. You can choose the surface however you like — close to the object's surface, or far away where the fields are simpler. This freedom to choose the Gaussian-like surface is what makes the method powerful.

**Radiation pressure** is a vivid application. A plane electromagnetic wave exerts pressure P = I/c on a perfectly absorbing surface (I = intensity). This follows directly from the Maxwell stress tensor: the wave carries momentum density **g** = **S**/c², and when absorbed the momentum is transferred to the surface. For a perfectly reflecting surface the pressure doubles to 2I/c because momentum reverses direction. This is not just a theoretical result — radiation pressure drives comet tails away from the sun, enables laser tweezers to trap cells, and is being exploited in proposed solar sail spacecraft. The Maxwell stress tensor is the machinery that makes these force calculations systematic.
