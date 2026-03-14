---
id: network-epidemiology
title: Network Epidemiology and Contact Structures
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: infectious-disease-surveillance
  type: hard
- id: sir-compartmental-model
  type: hard
tags:
- disease-transmission
- contact-networks
- outbreak-prediction
stage: advanced
status: draft
---

# Network Epidemiology and Contact Structures

## Core Idea
Disease spread depends fundamentally on the network structure of contacts—how individuals connect and interact—rather than population averages alone. Network epidemic models use graph theory to model how pathogens spread through populations, accounting for heterogeneous contact patterns, degree distribution, clustering, and community structure. Key metrics like network basic reproduction number and percolation thresholds predict outbreak potential. Network interventions (vaccination of high-degree nodes, community leaders) are often more efficient than random population strategies.

## How It's Best Learned
Simulate disease spread on real (social network, transportation) and synthetic networks with varying degree distributions; compare outbreak thresholds.

## Common Misconceptions
All network structures have similar outbreak thresholds (highly dependent on degree distribution and clustering). Mean-field models adequately account for network topology.
