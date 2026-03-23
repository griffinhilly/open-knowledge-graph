---
id: tension-and-compression-engineering
title: Tension and Compression in Structures
domain: engineering
course: engineering-principles
prerequisites:
- id: newtons-third-law-conceptual
  type: hard
- id: free-body-diagrams-intro
  type: hard
- id: formal-engineering-design-cycle
  type: soft
builds-toward:
- load-distribution-structures
- beam-strength-analysis
- truss-design-principles
- stress-and-strain-fundamentals
tags:
- tension
- compression
- structural-forces
- internal-forces
stage: abstract-reasoning
status: validated
---
# Tension and Compression in Structures

## Core Idea
Every structural member experiences internal forces that can be classified as tension (pulling apart) or compression (pushing together). A rope holding a hanging sign is in tension -- the sign's weight pulls the rope fibers apart. A column supporting a roof is in compression -- the roof's weight pushes the column's material together. Understanding which members are in tension and which are in compression is the first step in structural engineering, because different materials handle these forces differently: steel is excellent in both, concrete is strong in compression but weak in tension, and rope handles only tension.

## How It's Best Learned
Use physical models: stretch a rubber band (tension) and squeeze a sponge (compression). Build a simple truss from popsicle sticks and identify which members are being pulled and which are being pushed when a load is applied. Color-code members red for tension and blue for compression. Connect to Newton's Third Law by showing that if a rope pulls on a weight, the weight pulls equally on the rope.

## Common Misconceptions
- Tension and compression are types of materials. (They are types of forces or loading conditions, not material properties. The same steel beam can be in tension or compression depending on how it is loaded.)
- Compression always makes things shorter. (Compression is a force, not a result. A material in compression may deform only microscopically if it is stiff enough. The force exists even if deformation is invisible.)
- If a structure is standing, no internal forces exist. (A standing structure is in equilibrium, meaning all forces balance. But individual members still carry significant internal tension or compression forces.)
- All materials handle tension and compression equally well. (This is a critical misconception. Concrete cracks easily under tension. Rope cannot resist compression at all. Material selection depends heavily on the type of loading expected.)

## Questions

```yaml
- question: "A cable suspending a bridge deck from a tower is experiencing what type of internal force?"
  type: multiple-choice
  options: ["Compression", "Tension", "Both equally", "Neither -- it is in equilibrium"]
  answer: 1
  explanation: "The cable supports the bridge deck by being pulled taut. The deck's weight pulls down on the cable, which transmits the force to the tower. This pulling force is tension."

- question: "Concrete is equally strong in tension and compression."
  type: true-false
  answer: false
  explanation: "Concrete is very strong in compression (it can support enormous weight stacked on top of it) but weak in tension (it cracks easily when pulled apart). This is why reinforced concrete includes steel rebar -- the steel handles the tension forces that concrete cannot."

- question: "Identify one structural member in tension and one in compression in a simple arch bridge."
  type: short-answer
  answer: "The arch itself is primarily in compression -- the weight of the bridge and traffic pushes the arch's material together along its curve. If the arch has a tie beam connecting its two base points, that beam is in tension -- it resists the outward push of the arch ends."
  explanation: "Arches are efficient because they convert the downward load into compressive forces along the curve, which stone and concrete handle well. The horizontal thrust at the base must be resisted either by massive supports or by a tie beam in tension."
```

## Explainer
Pick up a rubber band and stretch it between your fingers. You can feel it trying to pull your fingers together -- that resistance to being stretched is **tension**. Now imagine squeezing a block of wood between your palms. The wood pushes back against your hands -- that resistance to being squashed is **compression**. These two types of internal force are the fundamental building blocks of structural engineering.

Every structure you see -- bridges, buildings, towers, cranes -- is a collection of members, each carrying internal forces. Some members are being pulled (tension), some are being pushed (compression), and some experience both depending on how the load is applied. A suspension bridge cable is purely in tension -- the weight of the road deck pulls it taut. A building column is purely in compression -- the floors above press down on it. A beam spanning an opening experiences both: the bottom surface stretches (tension) while the top surface squeezes together (compression).

Why does this matter? Because **different materials excel at different force types**. Steel is strong in both tension and compression, making it versatile. Concrete can withstand enormous compression -- you can stack cars on a concrete column -- but it cracks easily under tension. That is why engineers embed steel reinforcing bars (rebar) inside concrete: the concrete handles the compression, and the steel handles the tension. Rope and cables are pure tension members; they go slack the instant you try to push on them.

Identifying which members are in tension and which are in compression is a skill that uses free-body diagrams and Newton's Third Law. If you mentally "cut" a structural member and ask what forces the two halves exert on each other, you can determine the internal force. If the halves pull on each other, the member is in tension. If they push against each other, it is in compression. This analysis guides every decision about material selection, member sizing, and connection design.

Understanding tension and compression also explains why certain structural forms exist. Arches have been used for thousands of years because they convert downward loads into compression along the curve -- and ancient builders had stone, which is excellent in compression. Suspension bridges work because cables are incredibly efficient in tension, allowing them to span distances that would be impossible with beams alone. The choice between structural forms is fundamentally a choice about how to manage tension and compression.
