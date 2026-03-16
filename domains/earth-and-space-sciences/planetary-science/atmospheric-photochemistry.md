---
id: atmospheric-photochemistry
title: Atmospheric Photochemistry and UV-Driven Chemistry
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: atmospheric-chemistry-planets
  type: hard
- id: molecular-polarity
  type: soft
builds-toward:
- exoplanet-atmospheric-composition-spectroscopy
- biosignatures-exoplanet-atmospheres
tags:
- photochemistry
- atmospheres
- uv-radiation
- chemical-networks
- biosignatures
stage: advanced
status: draft
---

# Atmospheric Photochemistry and UV-Driven Chemistry

## Core Idea
Ultraviolet photons from the host star drive chemical reactions in planetary atmospheres, creating complex reaction networks of radicals and secondary species. These photochemical products determine atmospheric opacity, spectroscopic features, and the stability of potential biosignature molecules like O₂ and CH₄.

## Explainer

From your study of atmospheric chemistry on planets, you know that planetary atmospheres contain mixtures of gases whose composition is shaped by outgassing, escape, and chemical reactions. **Photochemistry** is the subset of those reactions driven by light — specifically ultraviolet (UV) photons with enough energy to break chemical bonds. When a UV photon strikes a molecule like water vapor (H₂O), carbon dioxide (CO₂), or methane (CH₄), it can split the molecule apart in a process called **photodissociation**, producing highly reactive fragments called **radicals**. These radicals — such as hydroxyl (OH), atomic oxygen (O), and atomic hydrogen (H) — are short-lived but chemically aggressive, and they drive cascading networks of secondary reactions that reshape the atmosphere's overall composition.

Consider Earth's ozone layer as a familiar example. Molecular oxygen (O₂) absorbs UV photons at wavelengths below about 240 nm and splits into two oxygen atoms. Each atom then combines with another O₂ molecule to form ozone (O₃). Ozone itself absorbs UV in the 200–320 nm range, splitting back into O₂ and O — a cycle that continually creates and destroys ozone while shielding the surface from harmful radiation. This **Chapman cycle** is pure photochemistry: no biology is needed to produce ozone, only UV light and O₂. But the steady-state ozone concentration also depends on catalytic destruction cycles involving nitrogen oxides (NOₓ), hydrogen oxides (HOₓ), and chlorine radicals — all of which are themselves photochemical products. The atmosphere's composition is therefore not a simple list of independently behaving gases; it is a coupled network where the abundance of each species depends on the UV-driven production and destruction of many others.

This network thinking becomes essential when evaluating **biosignatures** on exoplanets. Oxygen and methane coexisting in an atmosphere is often cited as a strong indicator of life, because these two gases react with each other (methane is oxidized by OH radicals derived from water photolysis), so their simultaneous presence implies continuous replenishment — plausibly by biological sources. But photochemistry complicates the story. On planets orbiting M-dwarf stars, which emit proportionally more UV at certain wavelengths and less at others compared to the Sun, the photochemical network operates differently. Lower near-UV flux can reduce OH production, allowing methane to accumulate abiotically. Conversely, high far-UV flux can photolyze CO₂ and H₂O efficiently enough to build up O₂ without any biology. Interpreting a detected atmospheric spectrum therefore requires running photochemical models that account for the host star's specific UV output, the planet's atmospheric composition and pressure, and the full web of radical reactions.

The practical toolkit of atmospheric photochemistry revolves around **photochemical models** — numerical simulations that divide the atmosphere into altitude layers and track the production, destruction, and transport of dozens to hundreds of chemical species simultaneously. Each reaction has a rate that depends on the local UV flux (which itself depends on altitude, because upper layers absorb photons before they reach lower layers) and the concentrations of reactants. The models solve for steady-state or time-dependent compositions, predicting what an atmosphere "should" look like given its inputs. When observations deviate from photochemical predictions — as when Cassini found unexpectedly complex hydrocarbons in Titan's upper atmosphere — it signals missing chemistry or unknown processes, driving new discoveries about planetary atmospheres both in our solar system and beyond.
