---
id: corrosion-and-environmental-attack
title: Corrosion and Environmental Degradation
domain: engineering
course: materials-science
prerequisites:
- id: atomic-bonding-engineering-materials
  type: hard
tags:
- corrosion
- oxidation
- galvanic
- passivation
- electrochemistry
stage: advanced
status: draft
---

# Corrosion and Environmental Degradation

## Core Idea
Corrosion is degradation of materials through chemical or electrochemical reaction with the environment. Oxidation forms oxide layers (beneficial if protective, like Al₂O₃ on aluminum; detrimental if porous, like Fe₂O₃ on iron). Galvanic corrosion occurs when dissimilar metals are in contact; the more active metal corrodes preferentially. Passivation (formation of protective oxide film) protects many metals (stainless steels, aluminum) and is maintained by maintaining oxidizing conditions.

## Explainer

From your study of atomic bonding, you know that metals bond metallically — valence electrons are delocalized, shared across the whole structure. This electron mobility also means metals can give electrons up relatively easily in chemical reactions. Corrosion is exactly this process: a metal returns to a lower-energy oxidized state, releasing electrons to the environment. Thermodynamically, most structural metals prefer to be oxides, hydroxides, or salts rather than pure metal. Engineering is largely the art of slowing down this inevitable tendency.

The difference between iron and aluminum in everyday experience illustrates how the oxide product governs everything. Both metals oxidize readily — iron to Fe₂O₃ (rust), aluminum to Al₂O₃. But Al₂O₃ is dense, adherent, and tightly bonded to the aluminum surface, forming a continuous barrier only nanometers thick that blocks further oxygen access. The Pilling-Bedworth ratio (volume of oxide divided by volume of metal consumed) is about 1.28 for aluminum — slightly greater than one, meaning the oxide is mildly compressed and seals completely. For iron, the ratio exceeds 2, so the oxide is under tension, cracks, and flakes off, continuously exposing fresh metal. This is why unpainted steel rusts through while aluminum forms a thin, self-limiting oxide layer.

**Galvanic corrosion** arises when two dissimilar metals are electrically connected in an electrolyte (seawater, moisture, soil). The metals have different standard electrode potentials — one is more anodic (active), the other more cathodic (noble). The anodic metal oxidizes (loses electrons = corrodes) while the cathodic metal is protected. The galvanic series ranks metals from most active (magnesium, zinc) to most noble (platinum, gold). This principle is exploited deliberately in cathodic protection: attach a **sacrificial anode** of zinc or magnesium to a steel structure, and the anode corrodes while the steel is protected. Ship hulls, buried pipelines, and concrete reinforcement use this technique. The converse — attaching copper fittings to iron pipes — accelerates iron corrosion catastrophically.

**Passivation** is the formation of a stable, adherent oxide film that kinetically inhibits further corrosion even though thermodynamics still favors it. Stainless steel owes its corrosion resistance entirely to a chromium oxide passive film, not to thermodynamic stability — stainless steel would corrode rapidly if this film were removed and not allowed to re-form. The passive film requires oxidizing conditions: in strongly reducing environments or in the presence of chloride ions (which competitively adsorb on the oxide), the film breaks down locally. This causes **pitting corrosion** — small but deep pits that penetrate rapidly into the metal while the surrounding surface appears intact. Pitting is more dangerous than uniform corrosion because it is hard to detect and concentrates stress.

The engineering response to corrosion operates at several levels: **material selection** (choose noble metals or passivating alloys for aggressive environments; avoid galvanic couples), **protective coatings** (paint, plating, anodizing, galvanizing), **cathodic protection** (sacrificial anodes or impressed current), and **corrosion inhibitors** in process fluids. In design, the critical rule is: whenever two dissimilar metals must contact, place an insulating barrier between them, or choose metals close together on the galvanic series. Understanding corrosion is ultimately understanding the electrochemical thermodynamics and kinetics of metal oxidation — the same atomic bonding framework that explains why metals conduct electricity also explains why they corrode.
