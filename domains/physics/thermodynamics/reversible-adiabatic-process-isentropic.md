---
id: reversible-adiabatic-process-isentropic
title: Reversible Adiabatic (Isentropic) Processes
domain: physics
course: thermodynamics
prerequisites:
- id: adiabatic-processes
  type: hard
- id: boundary-work-pv-diagram
  type: hard
tags:
- adiabatic
- reversible-processes
- isentropic
stage: formal-systems
status: draft
---

# Reversible Adiabatic (Isentropic) Processes

## Core Idea
In a reversible adiabatic (isentropic) expansion, no heat is transferred (Q = 0), so W = −ΔU. For an ideal gas, this follows PV^γ = constant and TV^(γ−1) = constant, where γ = Cp/Cv. The process is both reversible (quasi-static) and adiabatic (no heat transfer), making entropy change zero.

## Explainer

From your study of adiabatic processes, you know that Q = 0 implies ΔU = −W, and for an ideal gas undergoing a quasi-static adiabatic process, the constraint PV^γ = constant holds. From your work with PV diagrams and boundary work, you know that the work done by a gas is the area under the PV curve: W = ∫P dV. The **reversible adiabatic** process — also called **isentropic** — combines both conditions: no heat transfer and no irreversibility. The result is a process in which entropy is perfectly conserved.

The entropy connection is the key. Recall that the differential entropy change is dS = dQ_rev / T. For any adiabatic process, dQ = 0, so dS = 0 only if the process is also reversible. An irreversible adiabatic process (like a free expansion) also has Q = 0, but entropy *increases* because irreversibility generates entropy internally. The isentropic label signals that we have the special case where these two entropy-changing tendencies exactly cancel — zero heat flow and zero irreversible entropy generation — leaving total entropy unchanged. On a T-S diagram, an isentropic process is simply a vertical line.

The useful relations follow directly from PV^γ = constant and the ideal gas law. Combining them gives two equivalent forms: TV^(γ−1) = constant (pressure eliminated) and T^γ P^(1−γ) = constant (volume eliminated). The TV relation is often more useful in practice: if a gas expands from volume V₁ to V₂, the final temperature is T₂ = T₁ (V₁/V₂)^(γ−1). Since γ > 1, expansion (V₂ > V₁) means T₂ < T₁ — the gas cools. Compression heats it. The boundary work done by the gas is W = (P₁V₁ − P₂V₂) / (γ − 1) = nCᵥ(T₁ − T₂), which is simply the decrease in internal energy (confirming ΔU = −W).

Isentropic processes are the idealized working strokes in many engineering devices. The adiabatic legs of the Carnot cycle are isentropic. In turbines, nozzles, and compressors, the working fluid undergoes rapid pressure changes that are well approximated as isentropic — the process is too fast for significant heat transfer, and well-designed devices minimize friction and other irreversibilities. Real devices are characterized by an **isentropic efficiency** (the ratio of actual work to ideal isentropic work) that quantifies how closely they approach the reversible limit. A turbine with 90% isentropic efficiency extracts 90% of the work that a perfect isentropic expansion would deliver — the remaining 10% is lost to irreversibilities that generate entropy and deposit waste heat.
