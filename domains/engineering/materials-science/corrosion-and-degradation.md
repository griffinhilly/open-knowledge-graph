---
id: corrosion-and-degradation
title: Corrosion and Material Degradation
domain: engineering
course: materials-science
prerequisites:
- id: electrochemistry-basics
  type: hard
- id: electrochemical-cells
  type: hard
- id: crystal-defects
  type: soft
tags:
- corrosion
- galvanic
- passivation
- oxidation
- degradation
stage: formal-systems
status: validated
---

# Corrosion and Material Degradation

## Core Idea
Corrosion is the electrochemical degradation of metals in reactive environments. In galvanic corrosion, two dissimilar metals in electrical contact and a common electrolyte form an electrochemical cell — the more active (anodic) metal corrodes preferentially. The galvanic series ranks metals and alloys by their tendency to corrode in seawater. Passivation (the formation of a stable, adherent oxide layer, as in stainless steel and aluminum) can dramatically slow corrosion. Prevention strategies include cathodic protection (sacrificial anodes or impressed current), coatings, alloy selection, and geometric design to avoid crevices and bimetallic contacts.

## How It's Best Learned
Use the Nernst equation to calculate the driving voltage for a galvanic pair and predict which metal acts as anode. Analyze real corrosion case studies (Titanic hull, buried pipelines) to connect electrochemical theory to engineering practice.

## Common Misconceptions
- Stainless steel does not corrode because it is passive, not because steel is inherently corrosion-resistant. Scratching through the passive layer in a chloride environment can cause pitting.
- Galvanic corrosion risk depends on area ratio — a small anode connected to a large cathode corrodes very rapidly.

## Explainer

From your electrochemistry prerequisites, you know that oxidation–reduction reactions involve electron transfer. Corrosion is exactly this process occurring at a metal surface in contact with an electrolyte (water, soil, humid air). The metal surface sets up tiny electrochemical cells: at the **anode**, metal atoms oxidize and dissolve into solution (M → Mⁿ⁺ + ne⁻); at the **cathode**, electrons are consumed by a reduction reaction — typically oxygen reduction in neutral environments (O₂ + 2H₂O + 4e⁻ → 4OH⁻) or hydrogen evolution in acidic ones. The flow of electrons through the metal from anode to cathode is the corrosion current; the larger this current, the faster the metal dissolves.

**Galvanic corrosion** occurs when two dissimilar metals are in electrical contact and share an electrolyte. The **galvanic series** ranks metals by their electrochemical potential in a given environment (typically seawater): active metals (magnesium, zinc, aluminum) sit at the anodic end and corrode preferentially; noble metals (platinum, gold, titanium, stainless steel in passive state) sit at the cathodic end and are protected. The larger the potential difference between two coupled metals, the stronger the driving force for corrosion. The area ratio matters enormously: a large cathode coupled to a small anode concentrates all the corrosion current on the small anode, causing it to dissolve rapidly. Stainless steel fasteners in an aluminum panel — a large cathodic area, small anodic area — can rapidly pit the aluminum near each fastener.

**Passivation** is the mechanism that makes many engineering alloys so corrosion-resistant. Aluminum and stainless steel both form dense, adherent oxide layers (Al₂O₃ and Cr₂O₃, respectively) that are nearly impermeable to oxygen and ionic transport, effectively stopping further corrosion. The passive layer is self-healing in most environments: if scratched, it re-forms spontaneously. However, in chloride-rich environments (seawater, road salt), chloride ions can penetrate the passive film at local defects, triggering **pitting corrosion** — highly localized, deep cavities that grow autocatalytically once started. This is why the "stainless steel doesn't corrode" simplification is dangerous in marine applications.

Prevention strategies all derive from the electrochemical model. **Cathodic protection** works by making the structure the cathode — either by connecting it to a more active **sacrificial anode** (zinc blocks on a ship hull, magnesium anodes on buried pipelines) that corrodes preferentially, or by an **impressed current** system that forces electrons into the structure from an external power supply. Protective **coatings** break the electrical circuit by isolating metal from electrolyte; the danger is that a coating defect creates a small anode exposed to the entire large cathodic area of the coated surface, potentially causing accelerated attack at the defect. **Alloy selection** exploits passivation and the galvanic series: specifying compatible metals for joints and choosing corrosion-resistant alloys for the environment are the first lines of defense.
