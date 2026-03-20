---
id: metapopulation-dynamics-connectivity
title: Metapopulation Dynamics and Habitat Connectivity
domain: biology
course: ecology-and-evolution
prerequisites:
- id: population-ecology-intro
  type: hard
- id: gene-flow
  type: soft
- id: island-biogeography
  type: soft
- id: systems-of-first-order-linear-odes
  type: soft
builds-toward:
- conservation-genetics-effective-size
- extinction-vortex-populations
tags:
- metapopulation
- habitat-patches
- dispersal
- connectivity
stage: advanced
status: draft
---

# Metapopulation Dynamics and Habitat Connectivity

## Core Idea
A metapopulation is a population of populations connected by dispersal across fragmented habitat patches. Local extinctions and recolonization drive metapopulation dynamics. Connectivity determines whether patches function as a connected network or as isolated islands; high connectivity promotes persistence, while fragmentation increases extinction risk.

## Explainer

Island biogeography taught you that isolated habitat patches experience immigration and extinction in balance. Metapopulation theory extends this logic by asking: what happens when we track a *single species* across a network of such patches, and the "mainland" source is just another patch that can itself go extinct? Instead of a permanent species pool sending colonists to islands, you now have a constellation of local populations — some thriving, some declining, some empty — connected by individuals dispersing between them. The fate of the whole system depends not on any single patch, but on whether recolonization of empty patches happens fast enough to offset local extinctions elsewhere.

The simplest model, Levins' **metapopulation model**, captures this with two rates: the colonization rate (how quickly empty patches get reoccupied) and the extinction rate (how quickly occupied patches lose their population). If you think of each patch as a light bulb that flickers on and off, the metapopulation persists as long as enough bulbs are lighting up to replace the ones going dark. The fraction of occupied patches reaches an equilibrium analogous to species richness equilibrium in island biogeography, but now the currency is patch occupancy rather than species count. Critically, a metapopulation can persist regionally even when every local population is doomed to eventual extinction — persistence is an emergent property of the network, not of any single population.

**Connectivity** is the central variable that distinguishes a functioning metapopulation from a set of doomed isolates. Connectivity depends on the distance between patches, the quality of the intervening landscape (the **matrix**), and the dispersal ability of the organism. A frog metapopulation in a landscape of ponds separated by forest has high connectivity; the same ponds separated by highways have low connectivity. Gene flow — which you've already encountered — is the genetic consequence of this connectivity: when individuals successfully disperse and breed, they carry alleles between patches, counteracting genetic drift and inbreeding within small local populations.

Real metapopulations rarely match the Levins model perfectly. Some patches are large and rarely go extinct — these act as **sources** that sustain smaller, extinction-prone **sink** patches. The source-sink distinction matters enormously for conservation: protecting a single large source patch may matter more than protecting many small sinks. Corridor design, stepping-stone habitat, and matrix management all aim to maintain connectivity above the threshold where recolonization can keep pace with extinction. When connectivity drops below this threshold, the metapopulation enters an **extinction debt** — patches still occupied by aging populations that will not be rescued when they decline. The landscape looks occupied, but collapse is already inevitable without intervention.
