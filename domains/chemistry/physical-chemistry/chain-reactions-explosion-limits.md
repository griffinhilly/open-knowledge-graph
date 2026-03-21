---
id: chain-reactions-explosion-limits
title: Chain Reactions and Explosion Limits
domain: chemistry
course: physical-chemistry
prerequisites:
- id: reaction-mechanisms-elementary-steps
  type: hard
- id: arrhenius-rate-constants-temperature
  type: soft
tags:
- chain-reaction
- branching
- explosion
- kinetics
stage: advanced
status: draft
---

# Chain Reactions and Explosion Limits

## Core Idea
Chain reactions proceed via initiation (rare event creating radical), propagation (radical generates another radical), and termination (radicals are removed). When propagation exceeds termination, a chain branching explosion occurs—reaction rate increases explosively. Explosion limits define regions in the temperature-pressure diagram where explosions occur. Understanding chain reactions is crucial for combustion control, industrial safety, and atmospheric chemistry.

## Questions

```yaml
- question: "A H₂/O₂ mixture at fixed temperature is stable below 0.01 atm, explosive between 0.01 and 0.1 atm, stable again between 0.1 and 3 atm, then explosive above 3 atm. What explains the non-monotonic behavior between the first and second limits?"
  type: multiple-choice
  options:
    - "Higher pressure always increases reaction rate, so the first explosive region is just a pressure effect on Arrhenius kinetics"
    - "At the second limit, three-body gas-phase collisions become frequent enough to deactivate chain-carrying radicals, quenching the branching explosion"
    - "Above 0.1 atm, the reaction switches from branching to linear chain propagation, eliminating the exponential radical buildup"
    - "Higher pressure reduces the diffusion rate of reactants, starving the reaction of fuel"
  answer: 1
  explanation: "Between the first and second explosion limits, the counterintuitive result is that increasing pressure can suppress an explosion. At the second limit, increased pressure makes three-body collisions (H· + O₂ + M → HO₂· + M) frequent enough to convert the reactive H· into the much less reactive HO₂·, effectively quenching chain branching. This is why the same mixture can be stable → explosive → stable as pressure rises — the dominant termination mechanism changes with pressure."

- question: "What is the key mechanistic difference between a chain branching explosion and a thermal explosion?"
  type: multiple-choice
  options:
    - "A chain branching explosion involves fuel being consumed faster; a thermal explosion involves heat being produced faster"
    - "In chain branching, the radical population grows exponentially because each branching step produces more radicals than it consumes; in a thermal explosion, heat builds up faster than it dissipates, accelerating the reaction rate through temperature"
    - "Chain branching explosions only occur in gas phase; thermal explosions only occur in condensed phase"
    - "Thermal explosions are controlled by initiation; chain branching explosions are controlled by propagation"
  answer: 1
  explanation: "Chain branching and thermal explosions are fundamentally different mechanisms. In chain branching, each branching step (e.g., H· + O₂ → OH· + O·) produces two radicals from one, so the chain carrier population grows exponentially — a purely kinetic runaway. In a thermal explosion, heat from the exothermic reaction accumulates faster than it can escape, raising temperature, which accelerates the rate (Arrhenius), which produces more heat — a thermal feedback loop. Both can occur in the same system (the third explosion limit in H₂/O₂ is thermal)."

- question: "In a linear chain reaction (no branching), the radical population remains approximately constant during propagation because each propagation step consumes one radical and produces exactly one new radical."
  type: true-false
  answer: true
  explanation: "True. In a linear chain, propagation steps have the stoichiometry: radical + stable molecule → product + radical. The chain carrier count is preserved, so the reaction proceeds at a roughly steady rate determined by the balance of initiation and termination. This is distinct from chain branching, where one radical in can yield two or more radicals out, causing exponential growth in radical concentration."

- question: "In a chain branching explosion, the radical concentration remains constant because each branching step simply replaces radicals rather than creating new ones."
  type: true-false
  answer: false
  explanation: "False. This describes linear chain propagation, not chain branching. In chain branching, a single propagation step produces *more* radicals than it consumes — for example, H· + O₂ → OH· + O· converts one radical into two. If this branching rate exceeds termination, the radical population grows exponentially with each cycle, causing an accelerating (explosive) reaction rate. The distinction between linear propagation (constant radicals) and branching (growing radicals) is the mechanistic origin of explosive behavior."

- question: "Why is initiation necessary to start a chain reaction even when the overall combustion is thermodynamically highly favorable (large negative ΔG)?"
  type: short-answer
  answer: "Initiation is kinetically, not thermodynamically, necessary. The first step — bond homolysis to create radicals — has a very high activation energy, meaning it is extremely slow at room temperature despite being thermodynamically driven. Thermodynamic favorability tells you the final state is lower in energy, not how fast the reaction proceeds. Without initiation (heat, light, or a spark to provide activation energy), the kinetic barrier prevents the reaction from starting. Once the first radicals are created, the low-barrier propagation cycle takes over."
  explanation: "This question gets at the distinction between thermodynamic spontaneity and kinetic accessibility. The H₂ + ½O₂ → H₂O reaction is extremely exergonic, yet a mixture of H₂ and O₂ can sit stable in a container for years without a spark. The initial bond homolysis requires overcoming a large energy barrier — this is why a match is needed. The thermodynamic driving force explains *why* combustion releases so much energy; the activation energy of initiation explains *why* you need a spark to start it."
```

## Explainer

From your study of elementary reaction steps, you know that complex reactions can be decomposed into sequences of simple steps. A **chain reaction** is a specific type of multi-step mechanism where a reactive intermediate — typically a free radical — is consumed in one step and regenerated in the next, creating a self-sustaining cycle. The classic example is the hydrogen-oxygen reaction: a single H· radical can trigger thousands of successive reactions before it is finally destroyed. The three phases — initiation, propagation, and termination — determine whether the reaction proceeds steadily, dies out, or explodes.

**Initiation** creates the first radicals, usually through bond homolysis caused by heat, light, or a spark. This step is slow and has a high activation energy, which is why a match is needed to ignite a gas mixture even though combustion is thermodynamically favorable. Once radicals exist, **propagation** takes over: each radical reacts with a stable molecule to form product and a new radical. In a simple (linear) chain, each propagation step produces exactly one new radical, so the radical population stays roughly constant. The reaction proceeds at a steady rate until reactants are consumed or radicals are removed by **termination** — when two radicals collide and combine, or a radical hits a wall and is deactivated.

The situation changes dramatically with **chain branching**, where a single propagation step produces two or more new radicals instead of one. In the H₂/O₂ system, the reaction H· + O₂ → OH· + O· is a branching step — one radical in, two radicals out. If branching outpaces termination, the radical population grows exponentially with each cycle, and the reaction rate accelerates without limit until it becomes an **explosion**. Whether this happens depends on the balance between branching rate (which increases with temperature and reactant concentration) and termination rate (which depends on pressure and vessel geometry).

This balance produces the famous **explosion limits** on a pressure–temperature diagram. At very low pressures (below the first limit), radicals diffuse to the vessel walls and are destroyed faster than branching can replace them — no explosion. As pressure increases past the first limit, gas-phase branching overwhelms wall termination and an explosion occurs. But at still higher pressures (the second limit), three-body collisions become frequent enough to deactivate radicals in the gas phase, quenching the explosion. Above the third limit, the sheer amount of heat generated by the exothermic reaction cannot be dissipated fast enough, causing a thermal explosion. These limits explain why the same H₂/O₂ mixture can be stable, explosive, stable again, and then explosive once more as pressure rises — a counterintuitive result that only makes sense when you think about the competing rates of branching and termination at each pressure regime.
