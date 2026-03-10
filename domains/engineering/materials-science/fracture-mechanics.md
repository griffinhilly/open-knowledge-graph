---
id: fracture-mechanics
title: 'Fracture Mechanics: Brittle and Ductile Failure'
domain: engineering
course: materials-science
prerequisites:
- id: stress-strain-behavior
  type: hard
- id: mechanical-testing-methods
  type: soft
builds-toward:
- fatigue-in-materials
- fracture-toughness-and-design
tags:
- fracture
- stress-concentration
- KIC
- griffith
- brittle
- ductile
stage: formal-systems
status: draft
---

# Fracture Mechanics: Brittle and Ductile Failure

## Core Idea
Fracture is the separation of a material under stress. Brittle fracture occurs with little plastic deformation, often by rapid crack propagation along cleavage planes; ductile fracture is preceded by significant plastic deformation and void coalescence. Griffith's theory explains why cracks propagate: a crack spreads when the energy released by crack extension exceeds the energy required to create new surfaces. The fracture toughness KIc quantifies a material's resistance to crack propagation in plane-strain conditions and is the critical design parameter for components containing flaws.

## How It's Best Learned
Apply the fracture mechanics equation K = Yσ√(πa) to calculate critical crack size for a given applied stress, or critical stress for a given crack size. Compare KIc values for glass, steel, and aluminum to understand the range of fracture toughness in engineering materials.

## Common Misconceptions
- A stronger material is not necessarily tougher; high-strength steels often have lower fracture toughness than lower-strength variants.
- Stress concentrations at notches and holes do not cause higher average stress — they cause local stress amplification that can exceed the fracture stress.
