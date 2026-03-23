---
id: thermoregulation
title: Thermoregulation
domain: biology
course: physiology
prerequisites:
- id: homeostasis-and-feedback
  type: hard
- id: negative-feedback-mechanisms
  type: hard
- id: nervous-system-overview
  type: soft
tags:
- thermoregulation
- body temperature
- hypothalamus
- fever
- shivering
- sweating
stage: formal-systems
status: validated
---

# Thermoregulation

## Core Idea
Thermoregulation maintains core body temperature at approximately 37°C via a negative feedback system centered on the hypothalamus, which integrates input from central thermoreceptors (in the hypothalamus itself) and peripheral thermoreceptors (in skin and viscera). When temperature rises above the set point, the anterior hypothalamus triggers heat dissipation: cutaneous vasodilation diverts warm blood to the skin, and evaporative sweat cooling reduces heat load. When temperature falls, the posterior hypothalamus activates heat conservation (peripheral vasoconstriction) and heat generation (shivering generates heat as a byproduct of skeletal muscle ATP hydrolysis; non-shivering thermogenesis occurs in brown adipose tissue via uncoupling proteins). During infection, pyrogens (IL-1, IL-6, TNF-α, and especially prostaglandin E2) reset the hypothalamic set point upward, producing fever — a regulated elevation, not a loss of control.

## How It's Best Learned
Draw both the heating and cooling responses as complete feedback loops, naming sensor (thermoreceptors), control center (hypothalamus), and effectors (sweat glands, cutaneous blood vessels, skeletal muscle). Distinguish fever (set-point elevation) from hyperthermia (uncontrolled temperature rise): in fever, the body actively generates heat to reach the new set point; in heat stroke, the regulatory system is overwhelmed. Explain why antipyretics (aspirin, ibuprofen) reduce fever by inhibiting prostaglandin synthesis — they reset the set point downward.

## Common Misconceptions
- Shivering does not generate heat from nothing — it generates heat as a thermodynamic byproduct of ATP hydrolysis in rapidly cycling muscles.
- Fever is a regulated physiological response, not a regulatory failure — the body is actively trying to reach a higher set point set by pyrogens.
- Antipyretics do not cool the body directly; they block prostaglandin synthesis, resetting the hypothalamic set point toward normal, after which normal heat-dissipation mechanisms lower body temperature.

## Questions

```yaml
- question: "A patient with a bacterial infection develops a fever of 39°C and begins shivering intensely. Why is the patient shivering?"
  type: multiple-choice
  options:
    - "Shivering is a direct immune response to bacteria, agitating tissues to improve white blood cell delivery"
    - "Pyrogens have raised the hypothalamic set point to 39°C, so the body at 37°C 'perceives' itself as too cold and activates heat-generating mechanisms"
    - "The infection is lowering core body temperature below 37°C, triggering the normal cold response"
    - "The patient is shivering because core temperature is too high and shivering helps dissipate heat"
  answer: 1
  explanation: "Fever is a regulated set-point elevation, not a loss of control. When pyrogens (via prostaglandin E2) raise the hypothalamic set point from 37°C to 39°C, the body at its current 37°C is below the new target — it 'feels cold.' The hypothalamus activates the same heat-generating responses (peripheral vasoconstriction, shivering) it would use on a cold day, until core temperature rises to meet the new set point."

- question: "How do NSAIDs like ibuprofen reduce fever?"
  type: multiple-choice
  options:
    - "They directly cool blood flowing through the hypothalamus, lowering its temperature"
    - "They bind to and neutralize pyrogens (IL-1, IL-6) in the bloodstream before they reach the brain"
    - "They inhibit COX enzymes, reducing prostaglandin E2 synthesis and lowering the hypothalamic set point back toward normal"
    - "They activate sweat glands and cutaneous vasodilation directly, forcing heat dissipation"
  answer: 2
  explanation: "NSAIDs block cyclooxygenase (COX) enzymes, preventing the conversion of arachidonic acid to prostaglandin E2 (PGE2). Without PGE2, the hypothalamic set point falls back toward 37°C. With a lower set point, the body 'perceives' itself as too warm at fever temperature and activates heat-dissipation (sweating, vasodilation) — the fever 'breaks.' NSAIDs do not directly cool the body or neutralize cytokines."

- question: "Fever and hyperthermia are both caused by the same mechanism — a thermoregulatory system overwhelmed by excess heat — and differ only in severity."
  type: true-false
  answer: false
  explanation: "They are mechanistically distinct. In fever, the hypothalamic set point is actively reset to a higher value by pyrogens — the body is working correctly to reach its new target. In hyperthermia (e.g., heat stroke), the set point remains normal but heat gain exceeds the system's ability to dissipate — a failure of capacity. This difference matters for treatment: antipyretics work for fever but not heat stroke."

- question: "When a fever 'breaks' after ibuprofen administration, the patient sweats and feels warm because the thermoregulatory set point has returned to normal while body temperature is still elevated above it."
  type: true-false
  answer: true
  explanation: "After NSAIDs lower the set point back to ~37°C, the body is now above its target. The hypothalamus activates heat-dissipation responses — cutaneous vasodilation and sweating — exactly as it would in normal overheating. The patient sweats and feels warm because the normal cooling response is now directed at eliminating the excess heat that was generated during the fever."

- question: "Explain why a patient with a rising fever feels cold and may shiver, even though a thermometer shows their temperature is above 37°C."
  type: short-answer
  answer: "Fever is a regulated set-point elevation. Pyrogens cause the hypothalamus to 'decide' that normal body temperature (37°C) is too low — the new target might be 39°C. From the hypothalamus's perspective, the current temperature is below the set point, so it activates the same responses used on a cold day: peripheral vasoconstriction (reducing heat loss) and shivering (generating heat through inefficient muscle ATP hydrolysis). The patient subjectively feels cold because the thermoregulatory system is treating the situation as cold — even though an external thermometer reads an elevated temperature. The system isn't malfunctioning; it's working correctly toward its new, higher target."
  explanation: "The key distinction: in fever the thermostat is reset, so behaviors appropriate to 'I am below set point' (shivering, vasoconstriction) occur even at temperatures that would be 'hot' by normal standards."
```

## Explainer

You already understand negative feedback: a sensor detects a deviation from a set point, a control center processes the signal, and an effector drives the variable back toward the set point. **Thermoregulation** is one of the clearest physiological applications of this principle, with the hypothalamus serving as both sensor and control center, and a suite of effectors distributed across the skin, blood vessels, skeletal muscles, and adipose tissue.

When core body temperature rises — say, during exercise or in a hot environment — **thermoreceptors** in the anterior hypothalamus detect the increase (central thermoreceptors in the hypothalamus are especially sensitive to blood temperature, while peripheral thermoreceptors in the skin detect environmental temperature). The hypothalamus responds with two complementary heat-dissipation strategies. First, **cutaneous vasodilation**: sympathetic vasoconstrictor tone to skin arterioles decreases, allowing warm blood to flow from the core to the skin surface, where heat radiates and conducts to the environment. Second, **sweat production**: sympathetic cholinergic fibers activate eccrine sweat glands, and the evaporation of sweat from the skin surface removes approximately 2,400 kJ per liter of sweat evaporated — the single most effective cooling mechanism available to humans.

When core temperature falls, the posterior hypothalamus activates the opposite set of responses. **Cutaneous vasoconstriction** reduces blood flow to the skin, minimizing heat loss by keeping warm blood in the body's core — this is why your fingers and toes get cold first in winter. If vasoconstriction is insufficient, **shivering thermogenesis** begins: the hypothalamus activates rhythmic involuntary contractions of skeletal muscle. These contractions are metabolically inefficient by design — nearly all the ATP hydrolyzed is converted to heat rather than useful mechanical work. In infants and to a lesser extent in adults, **non-shivering thermogenesis** in brown adipose tissue provides an alternative heat source: uncoupling protein 1 (UCP1) in mitochondrial membranes short-circuits the proton gradient, allowing the energy of the gradient to dissipate as heat rather than driving ATP synthesis.

**Fever** is often confused with hyperthermia, but they are fundamentally different. Hyperthermia occurs when heat gain overwhelms the thermoregulatory system — the set point is normal, but the body cannot dissipate heat fast enough (as in heat stroke). Fever, by contrast, is a deliberate resetting of the hypothalamic set point to a higher value. During infection, immune cells release cytokines (IL-1, IL-6, TNF-alpha), which stimulate production of **prostaglandin E2 (PGE2)** in the hypothalamus. PGE2 raises the set point — say, from 37°C to 39°C. The body now "perceives" its current 37°C temperature as too cold, and activates the same heat-generating responses (vasoconstriction, shivering) that it would use on a cold day, until core temperature reaches the new set point. This is why patients with rising fevers feel cold and shiver. When antipyretics like ibuprofen block COX enzymes and reduce PGE2 synthesis, the set point drops back to normal, the body suddenly "perceives" itself as too warm, and heat-dissipation mechanisms (vasodilation, sweating) activate — the fever "breaks."
