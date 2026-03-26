---
id: related-rates
title: Related Rates
domain: mathematics
course: calculus-1
prerequisites:
  - id: implicit-differentiation
    type: hard
  - id: chain-rule
    type: hard
builds-toward:
  - optimization-problems
tags: [derivatives, applications, related-rates]
stage: formal-systems
status: validated
---

# Related Rates

## Core Idea
Related rates problems involve two or more quantities that change with respect to time, connected by an equation. You differentiate the equation with respect to time (using implicit differentiation and the chain rule) to relate the rates of change. For example, if a balloon's volume V and radius r are related by V = (4/3)*pi*r^3, then dV/dt = 4*pi*r^2 * dr/dt. This is one of the most important applications of the derivative.

## How It's Best Learned
Follow a systematic process: draw a diagram, identify variables and rates, write the relating equation, differentiate with respect to time, substitute known values, and solve for the unknown rate. Work many examples: ladders, cones filling with water, shadows, expanding circles.

## Common Misconceptions
- Substituting known values before differentiating (this destroys the variable relationships).
- Forgetting that all variables are functions of time t.
- Not correctly identifying what rate is given vs. what rate is asked for.

## Questions

```yaml
- question: "A student solving a ladder problem notes that at the moment of interest x = 6 and y = 8, so she substitutes these into x² + y² = 100 first, obtaining 36 + 64 = 100. She then differentiates to find 0 = 0. What error did she make?"
  type: multiple-choice
  options:
    - "She used the Pythagorean theorem incorrectly for a moving triangle."
    - "She substituted instantaneous values before differentiating, collapsing the variable relationship into a constant."
    - "She should have differentiated each variable separately before writing the equation."
    - "The equation x² + y² = 100 does not hold when the ladder is sliding."
  answer: 1
  explanation: "Substituting before differentiating freezes the variables at a single instant, turning the equation into a numerical identity (36 + 64 = 100) whose derivative is zero. This destroys the rate information. The correct procedure: first differentiate x² + y² = 100 with respect to t (yielding 2x·dx/dt + 2y·dy/dt = 0), then substitute the known instantaneous values of x, y, and any given rates to solve for the unknown rate."

- question: "The radius of a spherical balloon is increasing at 3 cm/s. What is dV/dt when the radius is 5 cm? (V = 4/3 πr³)"
  type: multiple-choice
  options:
    - "12π cm³/s, because dV/dt = 4π(dr/dt)²"
    - "100π cm³/s, because dV/dt = (4/3)π(dr/dt)³"
    - "300π cm³/s, because dV/dt = 4πr² · dr/dt"
    - "60π cm³/s, because dV/dt = 4πr · dr/dt"
  answer: 2
  explanation: "Differentiating V = (4/3)πr³ with respect to t via the chain rule gives dV/dt = 4πr² · dr/dt. At r = 5 and dr/dt = 3: dV/dt = 4π(25)(3) = 300π cm³/s. Option A mistakes dr/dt for r; option D drops the square on r; option B substitutes dr/dt in place of r before differentiating — the classic error of confusing a variable's current value with its rate of change."

- question: "In a related-rates problem, all variables in the geometric equation are implicitly functions of time t, even when t does not appear explicitly in the equation."
  type: true-false
  answer: true
  explanation: "This is the foundational conceptual shift in related rates. A balloon's radius r and volume V are not static numbers — they change as time passes, making them functions r(t) and V(t). The equation V = (4/3)πr³ holds at every instant, so it is an identity between two time-varying functions. Differentiating both sides with respect to t (and applying the chain rule to r) is only valid because r = r(t). If r were a fixed constant, dr/dt would be zero and the equation would carry no dynamic information."

- question: "You can substitute the known instantaneous values of most position variables into the relating equation before differentiating, as long as you keep the rates (dx/dt, dy/dt) as unknowns."
  type: true-false
  answer: false
  explanation: "This is the most common error in related rates. Substituting position values before differentiating turns variables into constants, making the chain rule yield zero. The rates dx/dt and dy/dt cannot be extracted once x and y have been replaced by numbers. The correct order is always: (1) write the geometric equation in terms of variables, (2) differentiate both sides with respect to t applying the chain rule, (3) then substitute known instantaneous values and known rates to solve for the unknown rate."

- question: "Why must you differentiate the relating equation before substituting the known instantaneous values of the variables?"
  type: short-answer
  answer: "Because substituting turns variables into constants, and the derivative of a constant is zero — destroying all information about rates. The chain rule can only extract dr/dt, dx/dt, etc., while r and x are still present as variables. Once you substitute x = 6 into x², you get 36, a number with no derivative relationship to time. Differentiation with respect to t must act while all quantities are still expressed as changing functions of t."
  explanation: "The relating equation (like x² + y² = L²) is true at every instant — it is an identity between functions of t, not a fact about one particular moment. Differentiating with respect to t converts this identity into a relationship between rates. Only after that step can you substitute specific values to find a specific rate at a specific moment. This ordering is what makes related rates a differentiation problem, not just an algebra problem."
```

## Explainer

Related rates problems are an application of two tools you already own: the **chain rule** and **implicit differentiation**. The chain rule tells you how to differentiate a composition of functions; implicit differentiation lets you differentiate an equation involving multiple variables without solving for one variable first. Related rates put these together in a time-based setting: two quantities are changing simultaneously, they're linked by a geometric or physical equation, and you want to know one rate of change given the other.

The key mental shift is recognizing that every variable in a related-rates problem is secretly a function of time t, even if t doesn't appear explicitly in the equation. A sphere's volume V and radius r are related by V = (4/3)πr³. This equation is always true, so differentiating both sides with respect to t — treating r and V as functions of t and applying the chain rule — gives dV/dt = 4πr² · dr/dt. This says: the rate at which the volume grows equals 4πr² times the rate at which the radius grows. If you know how fast the radius is increasing (dr/dt) and the current radius, you can find dV/dt instantly.

The procedure for any related-rates problem follows a reliable sequence: (1) **Draw and label** a diagram with all variables marked. (2) **Write the relating equation** — the geometry or formula that connects the variables (Pythagorean theorem, similar triangles, volume formula, etc.). (3) **Differentiate both sides with respect to t**, applying the chain rule wherever a variable appears. (4) **Substitute the known values** (including the rates and the current values of variables) into the differentiated equation. (5) **Solve** for the unknown rate. The crucial rule: steps 3 and 4 must stay in this order. Substituting before differentiating freezes variables that must remain variable during differentiation, destroying the relationship.

A classic example: a 10-foot ladder leans against a wall. The base slides away from the wall at 2 ft/s. How fast is the top sliding down when the base is 6 feet from the wall? Label: x = horizontal distance, y = vertical height. The Pythagorean theorem gives x² + y² = 100. Differentiating: 2x(dx/dt) + 2y(dy/dt) = 0. At the moment x = 6: y = √(100 − 36) = 8. Substituting: 2(6)(2) + 2(8)(dy/dt) = 0, so dy/dt = −24/16 = −3/2 ft/s. The negative sign confirms the top is sliding *down*. Every related-rates problem is a variant of this template: a geometric constraint, implicit differentiation with respect to time, and careful substitution after differentiating.
