---
id: fatigue-stress-cycles
title: Fatigue Behavior Under Cyclic Loading
domain: engineering
course: materials-science
prerequisites:
- id: yield-strength-tensile-properties
  type: hard
- id: fatigue-in-materials
  type: soft
tags:
- fatigue
- stress-cycles
- s-n-curves
- endurance-limit
stage: formal-systems
status: validated
---

# Fatigue Behavior Under Cyclic Loading

## Core Idea
Fatigue is progressive damage accumulation and crack growth under cyclic loading, causing failure at stresses far below static yield strength. The S-N curve (stress vs. number of cycles) characterizes fatigue behavior, with many materials exhibiting an endurance limit below which they theoretically survive infinite cycles. Fatigue failure initiates at stress concentrations (notches, defects) and propagates through dislocation motion and microcrack coalescence.

## Questions

```yaml
- question: "A steel shaft is designed to carry a cyclic load producing 150 MPa of nominal stress. The steel's yield strength is 500 MPa and its endurance limit is 200 MPa. After 10 million cycles of operation at this stress, what do we predict?"
  type: multiple-choice
  options:
    - "The shaft will have failed — repeated loading always causes eventual fatigue failure regardless of stress level"
    - "The shaft should survive indefinitely — the applied stress (150 MPa) is below the endurance limit (200 MPa)"
    - "The shaft will fail — any stress above 30% of yield strength causes fatigue failure in steel"
    - "The shaft will fail — failure occurs whenever stress exceeds half the tensile strength"
  answer: 1
  explanation: "For ferrous metals like steel, the endurance limit represents a stress amplitude below which the S-N curve is horizontal — the material theoretically survives an unlimited number of cycles. At 150 MPa, which is below the 200 MPa endurance limit, the shaft should not accumulate fatigue damage. This is a key distinction between steel and nonferrous metals (like aluminum), which have no true endurance limit. Note that this assumes no stress concentrations or surface defects — the 150 MPa is the *local* stress, not just the nominal stress."

- question: "Two identical aluminum alloy specimens are fatigue-tested. Specimen A has a polished surface; Specimen B has a notch with stress concentration factor K_t = 2. Both are loaded at 80 MPa nominal stress. Why does Specimen B fail first?"
  type: multiple-choice
  options:
    - "The notch increases average stress across the entire cross-section, so Specimen B experiences higher overall loading"
    - "The notch locally amplifies stress to 160 MPa at the notch root, where crack initiation begins — even though the bulk of the specimen remains at 80 MPa"
    - "Aluminum has no endurance limit, so any surface imperfection causes immediate failure"
    - "Surface finish only affects corrosion resistance, not fatigue initiation"
  answer: 1
  explanation: "Stress concentration factors multiply the nominal stress locally. At the notch root, the local stress is K_t × σ_nom = 2 × 80 = 160 MPa. Fatigue damage initiates where local stress is highest, not where nominal stress is highest. The bulk of the component may remain well below the fatigue strength, but the notch root exceeds it — and crack initiation begins there. This is why surface condition, notch geometry, and fillet radii are design priorities in fatigue-critical components. Specimen A, with no stress raisers, experiences uniform 80 MPa throughout and lasts much longer."

- question: "Fatigue failure can occur at applied stresses far below the static yield strength of the material."
  type: true-false
  answer: true
  explanation: "This is the defining and counterintuitive characteristic of fatigue. A material that easily survives a single load of 200 MPa may fracture after 10⁶ cycles at only 80 MPa — well below its yield strength. Cyclic loading accumulates invisible damage (dislocations, microcracks at stress concentrations) that a single static load would not produce. This is why fatigue is responsible for the majority of mechanical failures in engineering practice and why fatigue design requires a different analytical framework from static stress analysis."

- question: "All engineering materials have an endurance limit — a stress amplitude below which they can withstand an unlimited number of load cycles without failure."
  type: true-false
  answer: false
  explanation: "Only ferrous metals (steels, cast irons) exhibit a true endurance limit where the S-N curve becomes horizontal. Nonferrous metals — including aluminum alloys, titanium alloys, and copper alloys — show no horizontal asymptote. Their S-N curves continue declining even at very high cycle counts. This has major engineering consequences: aluminum aircraft components must be designed for a *finite* fatigue life (e.g., 10⁷ cycles), and every flight cycle counts toward that limit. There is no stress amplitude low enough to guarantee infinite life in aluminum, which drives retirement schedules for aircraft structures."

- question: "Explain why fatigue cracks typically initiate at the surface or at geometric discontinuities rather than in the interior of a component, and what this implies for engineering design and manufacturing practice."
  type: short-answer
  answer: "Fatigue initiates where local stress is highest. Geometric features — notches, holes, fillet radii, keyways, thread roots — act as stress concentrators, amplifying local stress by a factor K_t above the nominal value. Surface machining marks, corrosion pits, and weld toes create additional stress concentration sites. The surface also carries the highest bending and torsional stresses in most loading configurations. Because fatigue responds to *local* peak stress rather than bulk average stress, even a small geometric discontinuity can raise local stress above the endurance limit while the surrounding material remains safely below it. Design implication: avoid sharp corners (use generous fillet radii), improve surface finish (polishing raises the effective endurance limit), use shot peening to introduce compressive surface residual stresses, and locate stress concentrations away from high-nominal-stress regions."
  explanation: "The core principle is that fatigue is a local phenomenon. A component fails not when the 'average' stress exceeds some threshold, but when the *local* stress at a vulnerable point accumulates enough cyclic damage. This is why two components with identical bulk geometry but different surface conditions or notch geometries can differ by a factor of 2–4 in fatigue life. Manufacturing choices — grinding vs. turning, shot peening, heat treatment — are not cosmetic; they directly set the effective fatigue resistance of the finished part."
```

## Explainer

Static tensile testing, which you know from yield strength and tensile properties, measures a material's resistance to a single monotonically increasing load. Fatigue asks a fundamentally different question: what happens when a smaller stress is applied and removed thousands — or millions — of times? The answer is counterintuitive: materials fail at stresses well below the yield strength, through progressive, often invisible damage that accumulates until sudden fracture. A shaft that easily withstands a static load of 200 MPa may fracture after 10⁶ cycles at only 80 MPa.

The **S-N curve** (Wöhler curve) is the primary characterization tool. On a semi-log or log-log plot of applied stress amplitude S versus cycles to failure N_f, the curve slopes downward: higher stress amplitude produces fewer cycles to failure. For ferrous metals — steel and cast iron — the S-N curve typically flattens at high cycle counts, becoming horizontal at the **endurance limit** S_e (roughly 0.4–0.5 × tensile strength for steels). Below this stress, the material is assumed to survive indefinitely. Nonferrous metals (aluminum, titanium, copper alloys) show no true horizontal asymptote; their S-N curves continue declining, so fatigue design uses a **fatigue strength at a specified life**, typically 10⁷ or 10⁸ cycles. The engineering implication: for aluminum aircraft components, every cycle counts, and there is no stress low enough to guarantee infinite life.

Fatigue damage initiates at **stress concentrations** — locations where the local stress significantly exceeds the nominal (average section) stress. Notches, holes, fillet radii, weld toes, machining marks, and internal voids all act as stress raisers. The stress concentration factor K_t quantifies the amplification: if K_t = 2 and the nominal stress is 100 MPa, the local stress is 200 MPa. Fatigue responds to local stress, not nominal stress, so even a small K_t at a sharp notch can elevate local stress above the endurance limit while the bulk of the component remains elastic. This is why fatigue design focuses on surface finish, avoiding sharp corners, and minimizing geometric discontinuities — a smooth, polished specimen may have an endurance limit twice that of the same material with a notch.

Once a crack initiates (Stage I), it propagates under the tensile portion of each stress cycle (Stage II). Each cycle advances the crack tip by a small increment, leaving a characteristic **beach mark** or **fatigue striation** on the fracture surface — each striation corresponds to one cycle of crack advance, making striations visible evidence of cyclic loading history. Crack propagation continues until the remaining net section can no longer support the peak load in the cycle, at which point sudden final fracture (Stage III) occurs. The final fracture zone is rough and granular (typical of fast fracture), clearly distinguishable from the smooth, striated crack propagation zone. This fracture surface morphology is the forensic signature of fatigue failure and is the starting point of any failure analysis investigation involving cyclic loading.
