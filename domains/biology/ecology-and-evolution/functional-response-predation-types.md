---
id: functional-response-predation-types
title: 'Functional Response: Types and Predation Efficiency'
domain: biology
course: ecology-and-evolution
prerequisites:
- id: predator-prey-dynamics
  type: hard
- id: niche-concept-fundamental-realized
  type: soft
builds-toward:
- community-stability-resistance-resilience
tags:
- predation
- functional-response
- efficiency
- consumption-rate
stage: formal-systems
status: draft
---

# Functional Response: Types and Predation Efficiency

## Core Idea
Functional response describes how predation rate changes with prey density. Type I response (linear) reflects unlimited feeding; Type II response (saturating curve) shows prey handling time limits consumption; Type III response (sigmoidal) reflects predator learning or preference. Different functional responses produce different population dynamics and stability.

## Explainer

From predator-prey dynamics, you know that predator and prey populations are linked in feedback loops — more prey supports more predators, and more predators reduce prey. But those models often treat the predation rate as a simple constant. The **functional response** adds realism by asking: how does the rate at which an individual predator kills prey change as prey become more or less abundant? The answer turns out to depend on predator behavior, and it has major consequences for whether predator-prey systems are stable or prone to dramatic oscillations.

The **Type I functional response** is the simplest: the predator's kill rate increases linearly with prey density, with no upper limit. If prey doubles, kills double. This describes an idealized predator that can always find and process prey instantaneously — a useful mathematical baseline but rare in nature. Filter feeders like baleen whales or mussels come closest, passively straining food particles from water at a rate proportional to particle density, though even they eventually saturate. The key feature of Type I is the absence of any constraint on consumption rate.

The **Type II functional response** is far more common and biologically realistic. Here the kill rate rises with prey density but gradually levels off to a plateau — a **saturating curve** described mathematically by the **disc equation** (named by C.S. Holling after experiments with blindfolded volunteers picking sandpaper discs off a table). The saturation occurs because predators spend time not just searching for prey but also **handling** it — chasing, capturing, killing, eating, and digesting. As prey become abundant, search time shrinks toward zero but handling time remains constant, imposing a ceiling on how fast the predator can eat. The population-level consequence is important: at low prey density, Type II predators consume a *higher proportion* of the prey population (because each prey item encountered is still worth pursuing), which can destabilize prey populations and drive them to extinction at low numbers.

The **Type III functional response** is sigmoidal — an S-shaped curve where predation rate is low at low prey density, accelerates through an inflection point, and then saturates like Type II. The low predation at low prey density arises from **prey switching** (predators focus on alternative, more abundant prey) or **learning** (predators must develop a search image for rare prey before hunting them efficiently). This creates a **low-density refuge** for the prey: when prey are scarce, predators largely ignore them, allowing the population to recover. This density-dependent switching is stabilizing — it prevents predators from driving rare prey to extinction while still controlling abundant prey. Type III responses are common among generalist predators that can choose among multiple prey species, and they explain why prey diversity can be maintained even in the presence of efficient predators.
