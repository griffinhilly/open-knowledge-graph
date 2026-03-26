---
id: harmonic-functions-complex-analysis
title: Harmonic Functions
domain: mathematics
course: complex-analysis
prerequisites:
- id: cauchy-riemann-equations
  type: hard
builds-toward:
- harmonic-conjugates
tags:
- harmonic-functions
- laplace-equation
- pde
stage: advanced
status: validated
---

# Harmonic Functions

## Core Idea
A real-valued function u(x,y) is harmonic if ∇²u = ∂²u/∂x² + ∂²u/∂y² = 0. The real and imaginary parts of any holomorphic function are harmonic. Conversely, on simply connected domains, any harmonic function is the real part of some holomorphic function. Harmonic functions model steady-state heat and electrostatic potential.

## Questions

```yaml
- question: "The real and imaginary parts of a holomorphic function f(z) = u + iv are both harmonic. What is the deepest reason this must be true?"
  type: multiple-choice
  options:
    - "It is a definition — harmonic and holomorphic mean the same thing"
    - "It follows from differentiating the Cauchy-Riemann equations and using the equality of mixed partial derivatives"
    - "It is true only for analytic functions, not all holomorphic functions"
    - "It holds because holomorphic functions satisfy the wave equation"
  answer: 1
  explanation: "Differentiating u_x = v_y with respect to x gives u_xx = v_yx, and differentiating u_y = −v_x with respect to y gives u_yy = −v_xy. Since mixed partials are equal (v_xy = v_yx), adding these yields u_xx + u_yy = 0 — the Laplace equation. Holomorphic and harmonic are not synonyms: holomorphic means complex-differentiable everywhere in a domain (a condition on f as a complex function), while harmonic means satisfying ∇²u = 0 (a condition on u as a real function). They are related but distinct concepts."

- question: "A student claims: 'The function u(x,y) = x² − y² has a local maximum at the origin inside the disk x² + y² < 1, so it cannot be harmonic.' Is this claim correct?"
  type: multiple-choice
  options:
    - "Correct — harmonic functions cannot have interior extrema, so if u has a maximum inside the disk it is not harmonic"
    - "Incorrect — u(x,y) = x² − y² is actually harmonic, so the student must be wrong about the maximum"
    - "Correct — the maximum principle applies to all smooth functions on bounded domains"
    - "Incorrect — the maximum principle only applies to harmonic functions on unbounded domains"
  answer: 1
  explanation: "u(x,y) = x² − y² is harmonic: u_xx = 2 and u_yy = −2, so u_xx + u_yy = 0. The maximum principle says harmonic functions cannot have interior maxima or minima — their extreme values occur only on the boundary. At the origin, u = 0, but moving along the x-axis gives u = x² > 0, so the origin is a saddle point, not a maximum. The student's premise is wrong: u does not have an interior maximum. The function 'balances' via the mean value property, preventing any interior extremum."

- question: "A harmonic function u defined on the annulus {1 < |z| < 2} is not necessarily the real part of a globally defined holomorphic function on that domain."
  type: true-false
  answer: true
  explanation: "The converse of the holomorphic-implies-harmonic result requires the domain to be simply connected (no holes). An annulus has a hole, so it is not simply connected. On such domains, a harmonic function may fail to have a single-valued harmonic conjugate v globally — the line integral used to recover v may change value depending on the path taken around the hole. The classic example is u = ln|z|, which is harmonic on the annulus but whose harmonic conjugate arg(z) is multivalued."

- question: "Nearly every harmonic function on the entire complex plane is expected to achieve its maximum value somewhere in the interior."
  type: true-false
  answer: false
  explanation: "This reverses the maximum principle. The maximum principle states that a harmonic function on a bounded domain achieves its maximum on the boundary, not the interior. On an unbounded domain like the whole plane, a nonconstant harmonic function need not achieve a maximum at all — consider u(x,y) = x, which grows without bound. The principle forbids interior maxima; it does not guarantee any maximum exists."

- question: "What is the mean value property of harmonic functions, and why does it rule out interior local extrema?"
  type: short-answer
  answer: "The mean value property states that the value of a harmonic function at any point equals the average of its values over any circle centered at that point. An interior local maximum would require the function to be strictly larger at the center than on nearby circles, but then the average over a surrounding circle would be strictly less than the center value — contradicting the mean value property. By the same logic, interior minima are also impossible."
  explanation: "This is the geometric heart of harmonicity. ∇²u = 0 expresses that u has no net curvature — no tendency to spike or dip — which manifests as the mean value property. The maximum principle follows directly: if u achieved a strict interior maximum, the mean value property would be violated. This is why harmonic functions model equilibrium phenomena (steady-state temperature, electrostatic potential) — in equilibrium, there is no accumulation at any interior point."
```

## Explainer

Your prerequisite — the **Cauchy-Riemann equations** — says that a holomorphic function f(z) = u(x,y) + iv(x,y) must satisfy u_x = v_y and u_y = −v_x. This pair of constraints, combined with the assumption that the second partial derivatives are continuous, forces something remarkable about u and v individually. Differentiate the first equation with respect to x: u_xx = v_yx. Differentiate the second with respect to y: u_yy = −v_xy. Since mixed partials are equal (v_xy = v_yx), adding gives u_xx + u_yy = 0. The real part u automatically satisfies the **Laplace equation** ∇²u = 0. The same argument applied to v shows v is harmonic too.

A **harmonic function** is a real-valued function u(x,y) satisfying ∇²u = ∂²u/∂x² + ∂²u/∂y² = 0. The Laplace equation is the condition that a function has no local extrema in its interior — its value at any point equals the average of its values on any circle centered at that point. This **mean value property** is the geometric heart of harmonicity: harmonic functions are "balanced," never spiking or dipping in the interior of their domain. As a consequence, harmonic functions cannot have local maxima or minima in the interior — they achieve their extreme values only on the boundary (the **maximum principle**).

The connection runs both ways. Any holomorphic function yields a pair of harmonic functions (u and v). But on a **simply connected** domain (one with no holes), the converse holds: any harmonic function u is the real part of some holomorphic function f = u + iv, where v is called the **harmonic conjugate** of u. The harmonic conjugate is found by integrating the Cauchy-Riemann equations: v_x = −u_y and v_y = u_x. The simple connectedness is essential — on a domain with holes (like an annulus), harmonic functions may fail to have a single-valued conjugate globally.

The physical meaning anchors the abstraction. Harmonic functions describe **steady-state phenomena**: temperature distribution in a conducting plate after it has equilibrated, electrostatic potential in a region with no free charges, or fluid velocity potential in irrotational flow. In each case, "steady state" means no net flux accumulating at any interior point — exactly what ∇²u = 0 says analytically. This is why complex analysis, despite being pure mathematics, is an extraordinarily powerful tool for solving two-dimensional physics problems: every holomorphic function simultaneously solves two physical steady-state problems via its real and imaginary parts.
