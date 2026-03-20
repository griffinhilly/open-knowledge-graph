---
id: heat-treatment-of-steels
title: Heat Treatment of Steels
domain: engineering
course: materials-science
prerequisites:
- id: iron-carbon-phase-diagram
  type: hard
- id: strengthening-mechanisms
  type: hard
- id: diffusion-in-solids
  type: soft
- id: thermal-properties-of-materials
  type: soft
tags:
- annealing
- quenching
- tempering
- martensite
- TTT-diagram
stage: advanced
status: validated
---
# Heat Treatment of Steels

## Core Idea
Heat treatment manipulates steel microstructure — and therefore properties — through controlled cycles of heating and cooling. Annealing (slow cooling) produces soft pearlite; quenching (rapid cooling) traps carbon in the BCC iron lattice, forming hard, brittle martensite. Tempering a quenched steel by reheating to an intermediate temperature allows carbon to partially diffuse out, increasing toughness at the cost of some hardness. Time-Temperature-Transformation (TTT) diagrams chart the kinetics of these transformations and guide the selection of cooling rates and alloy additions for desired microstructures.

## How It's Best Learned
Overlay cooling curves of different rates onto a TTT diagram to predict whether the product is martensite, bainite, pearlite, or a mixture. Then connect predicted microstructure to measured hardness values.

## Common Misconceptions
- Martensite is hard because of the tetragonal lattice distortion from supersaturated carbon, not simply because it is a different phase.
- Tempering always reduces hardness; the goal is to recover toughness, accepting that trade-off rather than eliminating it.

## Explainer

The iron-carbon phase diagram — your core prerequisite — tells you what phases are thermodynamically stable at a given temperature and composition. At high temperature, steel dissolves into **austenite** (FCC iron with carbon dissolved interstitially). Cool slowly through the eutectoid temperature and the carbon partitions out, forming alternating lamellae of ferrite and cementite known as **pearlite** — soft, tough, and machinable. Heat treatment exploits one key fact: what the phase diagram says is stable at a given temperature says nothing about how fast the transformation must occur. By manipulating cooling rate, you can trap the steel in non-equilibrium microstructures far from what the diagram predicts.

**Annealing** follows the phase diagram's prescription: heat to austenite, then cool slowly enough that the equilibrium transformation completes fully. The result is a soft pearlitic microstructure useful for machining or cold working. **Quenching** goes to the opposite extreme: cool so rapidly — by plunging the part into water or oil — that carbon atoms have no time to diffuse out of the FCC lattice. Instead, austenite transforms via a diffusionless shear mechanism into **martensite**: a body-centered tetragonal structure with carbon atoms trapped in interstitial sites, distorting the lattice and blocking dislocation motion. This lattice distortion, combined with the high internal stress from the rapid quench, makes martensite extremely hard (up to 65 HRC) but catastrophically brittle. The steel could shatter under impact.

**Tempering** rescues the brittleness. After quenching, the steel is reheated to an intermediate temperature (150–650°C, depending on the desired balance of properties). At these temperatures, carbon atoms have enough thermal energy to slowly diffuse and precipitate as fine carbide particles, relieving the lattice distortion and internal stresses. Toughness recovers substantially; hardness drops moderately. The engineer chooses the tempering temperature to target specific properties: low tempering temperatures preserve most hardness (tool steels, cutting edges), while higher tempering temperatures produce a tougher, more ductile steel (structural applications, springs). Quench-and-temper is the most widely used heat treatment cycle for medium- and high-carbon steels.

**Time-Temperature-Transformation (TTT) diagrams** make this practical. They show, for a specific steel composition, the time required to transform a given fraction of austenite as a function of temperature. The characteristic C-shape of the TTT diagram has a "nose" at intermediate temperatures where transformation is fastest (high driving force + adequate diffusion). A cooling curve that misses the nose entirely will produce 100% martensite; one that clips the nose produces a mixed microstructure; one that crosses the nose at high temperature before cooling rapidly may produce **bainite** — a fine-scale ferrite-carbide mixture with properties intermediate between pearlite and martensite, often desirable in its own right. Alloying elements (Mn, Cr, Ni, Mo) push the TTT nose to the right, buying more time for thicker sections to transform fully before the nose is reached — a property called **hardenability**.
