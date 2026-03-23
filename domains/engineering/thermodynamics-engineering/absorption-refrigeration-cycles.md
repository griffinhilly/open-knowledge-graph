---
id: absorption-refrigeration-cycles
title: Absorption and Adsorption Refrigeration Cycles
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: vapor-compression-refrigeration-cycle
  type: hard
- id: psychrometrics-humid-air-properties
  type: soft
tags:
- absorption
- adsorption
- refrigeration
- cop
- heat-pump
stage: formal-systems
status: draft
---

# Absorption and Adsorption Refrigeration Cycles

## Core Idea
Absorption cycles replace mechanical compression with heat-driven chemical separation (e.g., ammonia-water, lithium-bromide-water). A weak solution is heated in the generator to release refrigerant vapor; vapor cools in the condenser and expands to the evaporator, where it absorbs heat; concentrated solution returns to the generator via solution pump. Lower COP (0.5-0.8) than vapor-compression but enables waste heat recovery and reduced electric consumption.

## Questions

```yaml
- question: "An industrial plant has abundant waste heat from its manufacturing process. An engineer proposes an absorption chiller (COP = 0.7) instead of a vapor-compression chiller (COP = 4.0). A colleague objects: 'The absorption system's COP is nearly 6× worse — it's clearly the wrong choice.' Who is right?"
  type: multiple-choice
  options:
    - "The colleague — COP directly measures efficiency, so a COP of 4.0 is always superior to a COP of 0.7"
    - "The engineer — when the driving heat is waste heat with near-zero marginal cost, a lower COP on free heat can deliver cheaper cooling than a higher COP requiring expensive electricity"
    - "The colleague — absorption systems only make sense when electricity costs exceed $0.50/kWh"
    - "Neither — both systems should be run in parallel to maximize cooling capacity"
  answer: 1
  explanation: "COP comparison is only meaningful when the inputs have the same cost. Vapor-compression COP is refrigeration per unit of shaft work (electricity); absorption COP is refrigeration per unit of heat input. If waste heat is free — exhaust from generators, process heat from manufacturing — then a COP of 0.7 on zero-cost heat delivers cooling at essentially zero energy cost, far cheaper than a COP of 4.0 requiring paid electricity. The absorption cycle is specifically designed for contexts where heat is cheap and electricity is expensive or scarce."

- question: "What is the fundamental thermodynamic reason that the solution pump in an absorption cycle requires far less work than a vapor compressor doing the same pressure lift?"
  type: multiple-choice
  options:
    - "The solution pump operates at lower temperatures, reducing the work required"
    - "Liquids are nearly incompressible, so pumping a liquid to high pressure requires roughly 1/1000 the work of compressing a vapor through the same pressure ratio"
    - "The solution pump uses a different thermodynamic cycle that avoids entropy generation"
    - "The refrigerant in solution has lower molecular weight, reducing compression energy"
  answer: 1
  explanation: "This is the core mechanical substitution that makes absorption cycles work. Work input for pumping is proportional to the specific volume of the fluid — and liquids have dramatically smaller specific volumes than vapors. Pumping a liquid requires roughly v·ΔP work per unit mass, while compressing a vapor requires integrating v·dP over a much larger volume range. The result is that the solution pump's work input is negligible compared to a vapor compressor's, making heat (for the generator) the dominant energy input rather than shaft work."

- question: "In an absorption refrigeration cycle, the generator is the component that absorbs heat from the space being cooled."
  type: true-false
  answer: false
  explanation: "The evaporator absorbs heat from the cooled space — this is true in both vapor-compression and absorption cycles. The generator's function is entirely different: it receives external heat (from waste heat, a gas flame, or solar energy) to drive refrigerant vapor out of the strong solution, effectively replacing the compressor's thermodynamic function of raising the refrigerant to high pressure and temperature. Confusing the generator with the evaporator is a common error; the generator is on the high-pressure, heat-input side of the cycle, not the low-pressure, cooling side."

- question: "An absorption refrigeration system driven entirely by waste heat from an industrial process effectively achieves a useful COP much higher than its rated thermal COP of 0.7, when evaluated in terms of electricity cost."
  type: true-false
  answer: true
  explanation: "If the waste heat has zero marginal cost (it would otherwise be rejected to the environment), then the effective cost of the cooling delivered is nearly zero regardless of the thermal COP. In economic terms, the system's 'effective COP' relative to paid energy input is essentially infinite — you're getting refrigeration for free from heat that was being wasted. This is precisely why absorption systems are attractive in industrial waste-heat recovery: the thermodynamic COP comparison with vapor-compression is misleading when the energy inputs have very different costs."

- question: "Explain the role of the absorber-pump-generator combination in the absorption cycle and what thermodynamic function this trio replaces from the vapor-compression cycle."
  type: short-answer
  answer: "The absorber-pump-generator trio replaces the mechanical compressor. In the absorber, low-pressure refrigerant vapor from the evaporator dissolves into a weak solution, releasing heat. The resulting strong solution (rich in refrigerant) is pumped by the solution pump — requiring minimal work because liquids are nearly incompressible — to high pressure. In the generator, external heat drives the refrigerant back out of the strong solution as high-pressure vapor. The net result is refrigerant vapor elevated from low to high pressure, exactly what the compressor does in vapor-compression, but using heat as the primary energy input instead of shaft work."
  explanation: "Understanding this substitution is the key insight of absorption cycles. The compressor lifts refrigerant from low to high pressure by mechanical work. The absorption trio accomplishes the same pressure lift through a thermochemical detour: dissolve at low pressure (absorber), pump as a liquid (negligible work), release at high pressure using heat (generator). The remaining cycle components — condenser, expansion valve, evaporator — are identical to vapor-compression. The entire innovation is in what replaces the compressor."
```

## Explainer

In the vapor-compression cycle you already know, a mechanical compressor does the essential thermodynamic work: it raises the refrigerant vapor from low pressure (evaporator) to high pressure (condenser). That compression requires shaft work — electricity or a mechanical drive. The absorption cycle asks a different question: can we replace that electrical energy with *heat* instead? The answer is yes, because of a chemical trick: certain refrigerants (typically ammonia, NH₃) dissolve readily into absorbent solutions (typically water) at low temperature and low pressure, and are then driven back out of solution by heating.

Here is the substitution. In vapor-compression, the compressor receives low-pressure vapor and delivers high-pressure vapor. In absorption, this function is replaced by three components working together: an **absorber**, a **solution pump**, and a **generator**. In the absorber, refrigerant vapor from the evaporator is absorbed into the weak solution, releasing heat. The resulting strong solution (rich in refrigerant) is then pumped to high pressure — and pumping a *liquid* requires only about 1/1000 the work of compressing a *vapor* at the same pressure ratio, because liquids are nearly incompressible. In the generator, heat from an external source (waste heat, a gas flame, solar energy) drives the refrigerant back out of the strong solution as high-pressure vapor. The depleted solution returns to the absorber via an expansion valve, completing the solution circuit. Meanwhile, the high-pressure refrigerant vapor proceeds through a condenser and evaporator exactly as in the vapor-compression cycle.

The thermodynamic accounting changes because you are now supplying heat (Q_gen) rather than work (W_comp) as the primary input. The **COP** is defined as Q_evap / Q_gen — refrigeration delivered per unit of heat consumed — and typically falls between 0.5 and 0.8 for single-effect absorption systems, compared to 3–5 for vapor-compression. On the surface this looks worse, but the comparison is misleading when the heat input is essentially free: waste heat from an industrial process, exhaust from a generator, or solar thermal panels all have near-zero marginal cost. In those contexts, a COP of 0.7 with free heat beats a COP of 4 requiring expensive electricity.

The most common working pairs are **ammonia-water** (NH₃/H₂O), used where sub-zero evaporator temperatures are needed, and **lithium bromide-water** (LiBr/H₂O), used in large commercial chillers where evaporator temperatures stay above 0°C (since the refrigerant is water itself). The choice of pair determines the operating pressures, temperatures, the complexity of rectification needed to purify the refrigerant vapor, and the practical COP. Absorption refrigeration is widely used in industrial waste-heat recovery, natural-gas-fired cooling in remote locations, and wherever the economics favor heat over electricity as the driving energy.

