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
stage: advanced
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

## Questions

```yaml
- question: "An engineer bolts a small stainless steel fastener into a large aluminum structural panel for use in a marine environment. The galvanic series shows aluminum is more active (anodic) than stainless steel. What does the electrochemical circuit model predict?"
  type: multiple-choice
  options:
    - "The stainless steel bolt corrodes rapidly because it is the smaller component and more exposed"
    - "Both metals corrode at equal rates because they share the same electrolyte (seawater)"
    - "The aluminum near the bolt corrodes rapidly — it is the small anodic area coupled to a large cathodic area, concentrating all corrosion current at the contact zone"
    - "No significant corrosion occurs because aluminum's passive oxide layer protects it in marine environments"
  answer: 2
  explanation: "This is a dangerous area ratio configuration: the small aluminum anode (the contact area around each bolt) is coupled to a large stainless steel cathode. All the corrosion current concentrates on the small anodic area, causing rapid localized pitting of the aluminum. Option D is the common misconception — aluminum's passive layer is disrupted by chloride ions in seawater, which is why 'aluminum is protected by passivation' is insufficient reasoning in marine environments."

- question: "Why does cathodic protection prevent corrosion of a buried steel pipeline?"
  type: multiple-choice
  options:
    - "It coats the pipeline with a passive chromium oxide layer similar to stainless steel"
    - "It eliminates the electrolyte (moist soil) surrounding the pipeline, breaking the electrochemical circuit"
    - "It makes the pipeline the cathode — by connecting it to a sacrificial anode or impressing current — so metal dissolution at the surface cannot occur"
    - "It increases the pipeline's electrical resistance, reducing the corrosion current to negligible levels"
  answer: 2
  explanation: "Corrosion requires anodic dissolution (metal → metal ions + electrons) at the corroding surface. Cathodic protection forces the pipeline to act as the cathode, where reduction reactions (not oxidation) occur. At a cathode, metal does not dissolve. Either a sacrificial anode (e.g., magnesium, which is more active and corrodes preferentially) or an impressed current (external power supply forcing electrons into the pipeline) achieves this. The electrochemical driving force for dissolution is removed because the pipeline is no longer the anode."

- question: "Stainless steel is corrosion-resistant because the iron and chromium in the alloy are inherently noble metals that do not react with water or oxygen under normal conditions."
  type: true-false
  answer: false
  explanation: "Stainless steel's corrosion resistance comes entirely from its passive layer — a thin, adherent Cr₂O₃ film that forms spontaneously and blocks further oxidation. Iron and steel are not inherently noble; plain steel corrodes readily. In chloride-rich environments (seawater, road salt), chloride ions can penetrate the passive film at local defects, initiating pitting corrosion that grows autocatalytically. The common belief that 'stainless steel doesn't corrode' is a dangerous oversimplification that has caused failures in marine and chemical processing applications."

- question: "In galvanic corrosion, the rate at which the anodic metal dissolves depends not only on the electrochemical potential difference between the two metals, but also critically on the relative surface areas of the anode and cathode."
  type: true-false
  answer: true
  explanation: "Area ratio is a key engineering variable in galvanic corrosion. A small anode coupled to a large cathode concentrates all the corrosion current on the small anode — intense localized attack. A large anode coupled to a small cathode spreads the same current over a large area — slow, diffuse attack. This is why the joint design matters as much as alloy selection: stainless steel fasteners in an aluminum panel create a large-cathode/small-anode configuration that accelerates aluminum failure at each contact point."

- question: "A protective coating on a steel pipeline develops a small pinhole defect. Explain, using the electrochemical circuit model, why this defect can cause more severe corrosion at that spot than if the entire pipeline were left uncoated."
  type: short-answer
  answer: "The coating isolates the vast majority of the steel surface from the electrolyte, making it effectively cathodic (no anodic reactions possible). The tiny exposed steel at the pinhole becomes the only anode — a small anodic area coupled to a very large effective cathodic area (the entire coated surface that can still participate in the cathodic reduction circuit). All corrosion current concentrates at the defect, producing rapid deep pitting rather than the gradual uniform attack that would occur on a fully uncoated surface."
  explanation: "This 'holiday problem' is a well-known failure mode in coated pipeline systems. The coating paradoxically worsens attack at any breach because it creates an extreme area ratio: one tiny anode, enormous cathode. This is why coating integrity monitoring is critical for cathodically protected pipelines, and why cathodic protection is typically used alongside coatings rather than as an alternative — the two strategies address each other's failure modes."
```

## Explainer

From your electrochemistry prerequisites, you know that oxidation–reduction reactions involve electron transfer. Corrosion is exactly this process occurring at a metal surface in contact with an electrolyte (water, soil, humid air). The metal surface sets up tiny electrochemical cells: at the **anode**, metal atoms oxidize and dissolve into solution (M → Mⁿ⁺ + ne⁻); at the **cathode**, electrons are consumed by a reduction reaction — typically oxygen reduction in neutral environments (O₂ + 2H₂O + 4e⁻ → 4OH⁻) or hydrogen evolution in acidic ones. The flow of electrons through the metal from anode to cathode is the corrosion current; the larger this current, the faster the metal dissolves.

**Galvanic corrosion** occurs when two dissimilar metals are in electrical contact and share an electrolyte. The **galvanic series** ranks metals by their electrochemical potential in a given environment (typically seawater): active metals (magnesium, zinc, aluminum) sit at the anodic end and corrode preferentially; noble metals (platinum, gold, titanium, stainless steel in passive state) sit at the cathodic end and are protected. The larger the potential difference between two coupled metals, the stronger the driving force for corrosion. The area ratio matters enormously: a large cathode coupled to a small anode concentrates all the corrosion current on the small anode, causing it to dissolve rapidly. Stainless steel fasteners in an aluminum panel — a large cathodic area, small anodic area — can rapidly pit the aluminum near each fastener.

**Passivation** is the mechanism that makes many engineering alloys so corrosion-resistant. Aluminum and stainless steel both form dense, adherent oxide layers (Al₂O₃ and Cr₂O₃, respectively) that are nearly impermeable to oxygen and ionic transport, effectively stopping further corrosion. The passive layer is self-healing in most environments: if scratched, it re-forms spontaneously. However, in chloride-rich environments (seawater, road salt), chloride ions can penetrate the passive film at local defects, triggering **pitting corrosion** — highly localized, deep cavities that grow autocatalytically once started. This is why the "stainless steel doesn't corrode" simplification is dangerous in marine applications.

Prevention strategies all derive from the electrochemical model. **Cathodic protection** works by making the structure the cathode — either by connecting it to a more active **sacrificial anode** (zinc blocks on a ship hull, magnesium anodes on buried pipelines) that corrodes preferentially, or by an **impressed current** system that forces electrons into the structure from an external power supply. Protective **coatings** break the electrical circuit by isolating metal from electrolyte; the danger is that a coating defect creates a small anode exposed to the entire large cathodic area of the coated surface, potentially causing accelerated attack at the defect. **Alloy selection** exploits passivation and the galvanic series: specifying compatible metals for joints and choosing corrosion-resistant alloys for the environment are the first lines of defense.
