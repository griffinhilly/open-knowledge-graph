---
id: heat-flow-conduction-steady-state
title: Heat Conduction and Steady-State Heat Flow
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: geothermal-gradient-crustal-heat-flow
  type: hard
- id: thermal-conductivity-and-rocks
  type: hard
builds-toward:
- mantle-adiabat-temperature
- crustal-age-and-cooling-curves
tags:
- geothermics
- heat-flow
- conduction
stage: advanced
status: draft
---

# Heat Conduction and Steady-State Heat Flow

## Core Idea
Heat flow is governed by Fourier's law: q = −k(dT/dz), where k is thermal conductivity. In steady state, heat flow is constant with depth and depends on the geothermal gradient and rock conductivity. Continental heat flow (~60 mW/m²) exceeds oceanic heat flow (~82 mW/m² at young ridges, decreasing with age) due to differences in crustal thickness and radioactive heat production.

## Questions

```yaml
- question: "Two adjacent rock units share the same temperature gradient of 30°C/km. Unit A is granite with thermal conductivity k = 3.0 W/(m·K); Unit B is shale with k = 1.5 W/(m·K). What is the ratio of heat flow in granite to heat flow in shale?"
  type: multiple-choice
  options:
    - "1:1 — identical gradients produce identical heat flow regardless of rock type"
    - "1:2 — granite conducts heat faster, so it produces a smaller temperature gradient for the same flux"
    - "2:1 — granite has higher conductivity and therefore higher heat flow for the same gradient"
    - "4:1 — heat flow scales with the square of thermal conductivity"
  answer: 2
  explanation: "Fourier's law: q = −k(dT/dz). With the same temperature gradient, heat flow is directly proportional to thermal conductivity. Granite at k = 3.0 conducts twice as much heat as shale at k = 1.5. The common error (option A) treats gradient as if it determines flux alone, forgetting that conductivity is an equally essential factor. Analogously to Ohm's law: the same voltage (gradient) across a better conductor (higher k) drives more current (heat flow). The relationship is linear in k, not quadratic, so option D is also wrong."

- question: "A continental region is in thermal steady state and has no radioactive heat-producing elements. Heat flow measured at the surface is 52 mW/m². What does steady-state theory predict about heat flow at 20 km depth?"
  type: multiple-choice
  options:
    - "Greater than 52 mW/m², because pressure at depth compresses rock and drives more heat upward"
    - "Less than 52 mW/m², because some heat escapes laterally through horizontal conduction"
    - "52 mW/m² — in steady state without internal heat sources, heat flow is the same at every depth"
    - "Indeterminate — heat flow at depth depends on the rock types present, which are not given"
  answer: 2
  explanation: "Steady state means temperature is constant in time at every point. Energy conservation then requires that whatever heat enters the base of any layer equals what exits the top — otherwise that layer would be heating or cooling. Without internal sources generating additional heat, the flux q is constant with depth. This is the defining property of steady-state conduction and what makes surface measurements informative about the deep thermal state. When radioactive heat production is present, each layer adds to the upward flux, and heat flow increases toward the surface — but that source term is explicitly absent here."

- question: "Measuring surface heat flow in continental crust enriched in radioactive elements will overestimate the heat flux arriving from the mantle below."
  type: true-false
  answer: true
  explanation: "True. Surface heat flow is the cumulative sum of heat from all sources below: mantle heat plus heat generated within the crust by decay of uranium, thorium, and potassium. Granitic continental crust is enriched in these elements, and a substantial fraction of measured surface heat flow (~60 mW/m² continental average) was generated within the upper crust rather than arriving from the mantle. To estimate mantle heat flux beneath a continent, one must subtract the crustal heat production component. Ignoring this correction leads to overestimates of mantle temperature or heat flux."

- question: "Young oceanic lithosphere near mid-ocean ridges has lower heat flow than old oceanic lithosphere because the young lithosphere has not yet had time to warm up from the underlying mantle."
  type: true-false
  answer: false
  explanation: "False — it is exactly the opposite. Young oceanic lithosphere at mid-ocean ridges has among the highest heat flow on Earth (~200–300 mW/m² at the ridge axis) because the hot mantle is very close to the surface and only a thin, newly-formed lithosphere separates them. As lithosphere ages and moves away from the ridge, it cools and thickens; heat flow decreases approximately as the inverse square root of crustal age. Old oceanic crust has the lowest heat flow of any oceanic region. The ridge is the thermal source, not a place of low heat — it is where the hot mantle wells up."

- question: "The negative sign in Fourier's law (q = −k dT/dz) might seem counterintuitive for a formula describing upward heat flow in the Earth. Explain what it means physically and why it is mathematically necessary."
  type: short-answer
  answer: "In the Earth with z increasing downward, temperature increases with depth, so dT/dz is positive. Without the negative sign, q would also be positive (pointing downward), but heat actually flows upward — from hot to cold. The negative sign ensures that the heat flux vector points in the direction of decreasing temperature, i.e., upward toward the surface. Physically, the sign encodes the second law of thermodynamics: heat spontaneously flows from hot to cold. Mathematically, it makes q negative when dT/dz is positive, correctly indicating upward flux in a downward-positive coordinate system."
  explanation: "Students often drop the sign and treat q as a magnitude, which works only if you already know the direction. The sign convention becomes important in more complex analyses — for example, when a layer is generating internal heat, the gradient reverses within the layer, and the sign correctly tracks where heat flows toward versus away from the source. The negative sign is not an arbitrary convention but a direct mathematical statement that nature drives heat from high to low temperature."
```

## Explainer

You already understand two key ingredients: the **geothermal gradient** (temperature increases with depth, typically 25–30°C per kilometer in continental crust) and **thermal conductivity** (different rocks transmit heat at different rates, with crystalline rocks like granite conducting better than porous sediments). Steady-state heat conduction ties these together with a single equation that governs how thermal energy moves through the lithosphere.

**Fourier's law of heat conduction** states that heat flux q equals the negative product of thermal conductivity k and the temperature gradient dT/dz: q = −k(dT/dz). The negative sign simply means heat flows from hot to cold — downward-increasing temperature drives heat upward toward the surface. The units work out to watts per square meter (W/m²), and typical surface heat flow values are on the order of tens of milliwatts per square meter. Think of it like water flowing through a pipe: the temperature gradient is the pressure difference driving the flow, and thermal conductivity is how wide the pipe is. A steep gradient or a highly conductive rock produces more heat flow; a shallow gradient or an insulating rock produces less.

**Steady state** means that the temperature at every point is constant in time — heat entering the bottom of any layer equals heat leaving the top. This is a reasonable approximation for old, thermally equilibrated continental crust, but it breaks down where thermal transients matter (young oceanic lithosphere cooling from a hot ridge, or regions recently disturbed by magmatic intrusion). In steady state with no internal heat sources, heat flow is the same at every depth — measure it at the surface, and you know it throughout the column. When radioactive heat production is present (as in granitic continental crust, which is enriched in uranium, thorium, and potassium), the steady-state equation gains a source term: heat flow increases with depth because each layer of rock adds its own radiogenic contribution to the upward flux.

This framework explains a key observation in global geophysics. Continental crust has high radioactive heat production concentrated in the upper crust, so a significant fraction of continental surface heat flow (~60 mW/m²) is generated within the crust itself. Oceanic crust has very little radioactive heat production, so nearly all oceanic heat flow comes from the cooling mantle below. Young oceanic lithosphere near mid-ocean ridges has very high heat flow because the mantle is hot and close to the surface, but this decreases predictably with the square root of crustal age as the lithosphere thickens and cools — a transient process that steady-state analysis alone cannot capture, but which the steady-state framework helps benchmark. Measuring heat flow in boreholes (temperature gradient plus laboratory conductivity measurements on core samples) remains the primary method for constraining the thermal state of the lithosphere.
