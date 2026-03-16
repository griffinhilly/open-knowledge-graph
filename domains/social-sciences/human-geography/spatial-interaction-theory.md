---
id: spatial-interaction-theory
title: Spatial Interaction and the Gravity Model
domain: social-sciences
course: human-geography
prerequisites:
- id: place-and-space-concepts
  type: hard
- id: population-distribution-density
  type: soft
- id: economic-geography-fundamentals
  type: soft
- id: proportional-relationships
  type: soft
- id: ratios
  type: soft
- id: direct-and-inverse-variation
  type: soft
- id: geographic-information-systems-intro
  type: soft
- id: urban-geography-fundamentals
  type: soft
- id: distance-formula
  type: hard
- id: functions-domain-codomain-range
  type: soft
- id: distance-and-distance-formula-3d
  type: soft
- id: optimization-multivariable-basics
  type: soft
builds-toward:
- world-cities-global-hierarchy
tags:
- spatial interaction
- gravity model
- distance decay
- complementarity
- transferability
- connectivity
stage: formal-systems
status: validated
---
# Spatial Interaction and the Gravity Model

## Core Idea
Spatial interaction theory explains flows of people, goods, information, and capital between places as a function of the size of those places and the distance between them. The gravity model predicts that interaction is proportional to the product of the 'masses' of two places (typically measured by population or economic output) and inversely proportional to the distance between them — analogous in form to Newton's gravitational law. Distance decay describes the empirical regularity that interaction diminishes with increasing separation. Three conditions are necessary for spatial interaction to occur: complementarity (one place has what another needs), the absence of a sufficient intervening opportunity, and transferability (movement costs are not prohibitive). Modern telecommunications reduce but do not eliminate the friction of distance.

## How It's Best Learned
Apply the gravity model to predict trade flows or commuting patterns between cities and compare predictions to observed data. Map airline networks to see how hub-and-spoke systems reflect distance decay modified by hub connectivity advantages. Examine how telecommunications has changed (but not eliminated) distance effects on business location and social interaction.

## Common Misconceptions
- The gravity model is an empirical regularity, not a physical law; it describes patterns without fully explaining the social and economic mechanisms producing them.
- Distance is not only physical; cultural, political, and economic barriers (tariffs, language differences, visa requirements) create 'friction' equivalent to additional physical distance.
- The 'death of distance' predicted by early internet theorists has not materialized; geographic proximity continues to strongly influence interaction in most economic, social, and cultural domains.

## Questions

```yaml
- question: "According to the gravity model, if the distance between two cities doubles while their populations remain constant, how does predicted interaction between them change?"
  type: multiple-choice
  options: ["It halves", "It falls to one-quarter of the original value", "It doubles", "It remains the same because populations are unchanged"]
  answer: 1
  explanation: "The gravity model predicts interaction ∝ (M₁ × M₂) / d². If d doubles, d² quadruples, so the interaction is divided by 4 — falling to one-quarter of the original. Distance is squared in the denominator, which is why increasing separation has a compounding dampening effect on spatial interaction."

- question: "Modern telecommunications and the internet have effectively eliminated the effect of geographic distance on most economic and social interactions."
  type: true-false
  answer: false
  explanation: "Despite predictions of the 'death of distance,' geographic proximity continues to strongly influence interaction in most economic, social, and cultural domains. Agglomeration in cities, face-to-face business clustering, regional trade intensity, and local social ties all show persistent distance effects. Telecommunications reduces some friction of distance but does not eliminate it."

- question: "What are Ullman's three conditions necessary for significant spatial interaction to occur between two places, and why is each condition necessary?"
  type: short-answer
  answer: "Complementarity: one place must supply what the other demands, otherwise there is no motivation to interact. Absence of an intervening opportunity: no closer alternative must be available to satisfy the same need, or it will redirect the interaction. Transferability: movement must be physically and economically feasible — if transport costs are prohibitive, interaction cannot occur regardless of complementarity."
  explanation: "The gravity model captures mass and distance but not the content of why places interact. Complementarity explains the motivation; intervening opportunity explains why two complementary places may still have low interaction (a nearer substitute intercepts it); transferability sets a hard practical limit. All three must hold for meaningful spatial interaction to develop."
```

## Explainer

Why do more people travel between two nearby cities than between two distant ones of equal size? Why do countries trade more with neighbors than with equally wealthy partners across the ocean? Spatial interaction theory provides a systematic framework for answering these questions — one that turns out to generalize remarkably well across migration, trade, telecommunications, and commuting.

The foundation is the gravity model, borrowed by analogy from Newtonian physics. Predicted interaction between two places (I₁₂) is proportional to the product of their "masses" — typically population or GDP — divided by the square of the distance between them: I₁₂ ∝ (M₁ × M₂) / d². The intuition is straightforward: larger places generate and attract more movement; greater distance suppresses it. The d² term is the crucial detail. Distance is not just a drag — it is a squared drag. Doubling the distance between two cities reduces predicted interaction to one-quarter of its original level. This steep, nonlinear drop-off is called distance decay, and it appears consistently across empirical data on migration flows, airline passenger volumes, phone call frequencies, and retail spending patterns.

But mass and distance alone do not fully explain when interaction actually develops. Ullman's three conditions add the necessary substantive layer. Complementarity requires that one place actually supply what the other demands — two cities both producing the same goods have limited trade motivation. Absence of intervening opportunity recognizes that even two complementary places may barely interact if a closer alternative satisfies the need first; a suburb does not commute to a distant employment center when a nearer one offers equivalent jobs. Transferability sets the hard floor: movement must be physically and economically feasible given infrastructure, cost, and political conditions. High tariffs, visa requirements, and poor roads all create "friction" equivalent to additional distance.

An important methodological note: the gravity model is an empirical regularity, not a physical law. The exponent on distance is not fixed at 2 — it is estimated from data and varies by context (airline travel shows different exponents than grocery shopping). The definition of "mass" also varies by application. When the model's predictions diverge significantly from observed flows, that divergence is itself informative: it points to barriers, special relationships, or structural features the simple model does not capture.

Finally, distance is not only physical. Cultural distance (language differences), political distance (visa requirements, trade barriers), and economic distance (transaction costs, incompatible standards) all act as friction equivalents that reduce interaction below what geography alone predicts. This helps explain why countries with shared language or colonial history trade more than their distance would suggest, and why political borders depress cross-border interaction even when physical distance is minimal. Modern telecommunications has genuinely reduced some of these frictions — it is faster and cheaper to coordinate across distance than ever before — but it has not substituted for proximity advantages in activities requiring trust, tacit knowledge, and face-to-face collaboration.
