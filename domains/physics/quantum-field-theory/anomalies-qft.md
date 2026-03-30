---
id: anomalies-qft
title: Anomalies in Quantum Field Theory
domain: physics
course: quantum-field-theory
prerequisites:
- id: renormalization-of-qed
  type: hard
- id: noethers-theorem-fields
  type: hard
- id: non-abelian-gauge-theories
  type: soft
tags:
- anomalies
- chiral-anomaly
- gauge-anomaly
stage: expert
status: validated
---

# Anomalies in Quantum Field Theory

## Core Idea
An anomaly occurs when a symmetry of the classical Lagrangian is broken by quantum effects (loop corrections). The chiral anomaly breaks the classical conservation of the axial current and explains neutral pion decay. Gauge anomalies would destroy the consistency of a gauge theory; their cancellation constrains the particle content of the Standard Model.

## Questions

```yaml
- question: "The classical QED Lagrangian with massless fermions has two conserved currents: the vector current j^mu = psi-bar gamma^mu psi and the axial current j^mu_5 = psi-bar gamma^mu gamma_5 psi. What happens to the axial current at the quantum level?"
  type: multiple-choice
  options:
    - "Both currents remain conserved"
    - "The axial current acquires a non-zero divergence proportional to F_{mu nu} F-tilde^{mu nu} — the chiral anomaly — due to the triangle diagram where two photons couple to the axial current through a fermion loop"
    - "The vector current becomes anomalous instead"
    - "Both currents are broken by quantum effects"
  answer: 1
  explanation: "The Adler-Bell-Jackiw (ABJ) anomaly states that partial_mu j^mu_5 = (e^2)/(16 pi^2) F_{mu nu} F-tilde^{mu nu}, where F-tilde is the dual field strength. This is computed from the triangle diagram with one axial vertex and two vector vertices. The anomaly is exact — it receives no higher-order corrections (Adler-Bardeen theorem). The vector current remains conserved (no anomaly), which is essential for electric charge conservation. The anomaly has real physical consequences: it explains the decay rate of pi^0 -> gamma gamma, which would be zero without the anomaly."

- question: "If the gauge symmetry of a theory is anomalous (i.e., the gauge current has an anomaly), the theory is inconsistent and must be discarded. Why is a gauge anomaly more dangerous than a global anomaly?"
  type: multiple-choice
  options:
    - "Because gauge anomalies violate Lorentz invariance"
    - "Because a gauge anomaly breaks the Ward identities that ensure unitarity and renormalizability — without gauge invariance at the quantum level, negative-norm states (ghosts) do not decouple, probability is not conserved, and the theory makes no sense"
    - "Because gauge anomalies produce infinite cross sections"
    - "Because gauge anomalies violate energy conservation"
  answer: 1
  explanation: "Gauge invariance is not merely a convenient symmetry — it is essential for the consistency of the theory. It ensures that unphysical polarization states of gauge bosons decouple (unitarity), that divergences can be systematically removed (renormalizability), and that the number of physical degrees of freedom is correct. If quantum corrections break gauge invariance (a gauge anomaly), all of this fails. This is why anomaly cancellation is a non-negotiable consistency condition on the particle content of any gauge theory. A global anomaly (breaking a global symmetry) is physically interesting but not fatal."

- question: "In the Standard Model, the anomalies from quarks and leptons within each generation cancel exactly. This cancellation is a coincidence with no deeper explanation."
  type: true-false
  answer: false
  explanation: "Anomaly cancellation in the Standard Model requires specific relationships among the hypercharges and representations of quarks and leptons. Within each generation, the sum of certain products of charges (the anomaly coefficients for SU(3)^2 U(1), SU(2)^2 U(1), U(1)^3, and gravitational anomalies) vanishes. This cancellation appears highly non-trivial when the particle content is taken as given, but it follows automatically if the Standard Model is embedded in a grand unified theory (like SU(5) or SO(10)), where quarks and leptons live in unified representations. Anomaly cancellation is therefore evidence for a deeper structure."

- question: "Explain how the chiral anomaly resolves the puzzle of neutral pion decay (pi^0 -> gamma gamma) and why this decay would be forbidden without it."
  type: short-answer
  answer: "The pion is a pseudo-Goldstone boson of the spontaneously broken chiral symmetry of QCD. Its coupling to photons occurs through the axial current: the matrix element involves <0|j^mu_5|pi^0> coupled to two photons. If the axial current were exactly conserved (no anomaly), partial_mu j^mu_5 = 0, the coupling to the two-photon state would vanish (by taking the divergence of the amplitude and using current conservation), and the pi^0 would not decay to two photons. The chiral anomaly gives partial_mu j^mu_5 = (e^2 N_c)/(16 pi^2) F_{mu nu} F-tilde^{mu nu}, which provides the coupling. The predicted decay rate, proportional to N_c^2 alpha^2 m_pi^3/(f_pi^2), agrees with experiment when N_c = 3 colors. This was one of the first confirmations that quarks come in three colors."
  explanation: "This is a remarkable story: a formal mathematical anomaly in the quantum theory resolves a physical puzzle and simultaneously provides evidence for the color degree of freedom. It shows that anomalies are not defects but essential features of the quantum theory with observable consequences."
```

## Explainer

An **anomaly** in quantum field theory occurs when a symmetry of the classical Lagrangian fails to survive quantization. The classical theory has a conserved current (by Noether's theorem), but quantum corrections (specifically, loop diagrams) generate a nonzero divergence of that current. The most important example is the **chiral anomaly** (or ABJ anomaly), discovered independently by Adler and by Bell and Jackiw in 1969.

Consider massless QED. The classical Lagrangian is invariant under both vector transformations (psi -> e^{i alpha} psi, conserving the vector current) and axial transformations (psi -> e^{i alpha gamma_5} psi, conserving the axial current). But the triangle diagram -- a fermion loop with one axial-current vertex and two vector-current vertices -- is ambiguous: you cannot regularize it in a way that preserves both symmetries simultaneously. The standard choice preserves the vector symmetry (essential for electric charge conservation) at the expense of the axial symmetry, giving the anomaly equation partial_mu j^mu_5 = (e^2)/(16 pi^2) F_{mu nu} F-tilde^{mu nu}. This is an exact result, receiving no corrections beyond one loop.

Anomalies are classified into two types with very different implications. **Global anomalies** (anomalies in global symmetries) are physically real and have observable consequences. The chiral anomaly explains the decay pi^0 -> gamma gamma: without it, this decay would be forbidden, and the predicted rate (proportional to the number of quark colors squared) agrees with experiment for N_c = 3. **Gauge anomalies** (anomalies in local gauge symmetries) would be fatal: they would destroy unitarity and renormalizability, making the theory mathematically inconsistent. Gauge anomaly cancellation is therefore a constraint on the allowed particle content.

In the Standard Model, gauge anomaly cancellation places tight constraints on the charges and representations of the particles. The anomaly coefficients for SU(3)^2 U(1)_Y, SU(2)^2 U(1)_Y, U(1)_Y^3, and the mixed gravitational-U(1)_Y anomaly must all vanish. Remarkably, they do -- but only when the quarks and leptons are included with their observed quantum numbers, and within each complete generation. This cancellation is one of the most compelling pieces of evidence that the Standard Model has a deeper structure, likely a grand unified theory in which quarks and leptons are unified into larger representations where anomaly cancellation is automatic.
