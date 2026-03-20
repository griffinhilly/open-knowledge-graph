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
stage: advanced
status: draft
---

# Fatigue Behavior Under Cyclic Loading

## Core Idea
Fatigue is progressive damage accumulation and crack growth under cyclic loading, causing failure at stresses far below static yield strength. The S-N curve (stress vs. number of cycles) characterizes fatigue behavior, with many materials exhibiting an endurance limit below which they theoretically survive infinite cycles. Fatigue failure initiates at stress concentrations (notches, defects) and propagates through dislocation motion and microcrack coalescence.

## Explainer

Static tensile testing, which you know from yield strength and tensile properties, measures a material's resistance to a single monotonically increasing load. Fatigue asks a fundamentally different question: what happens when a smaller stress is applied and removed thousands — or millions — of times? The answer is counterintuitive: materials fail at stresses well below the yield strength, through progressive, often invisible damage that accumulates until sudden fracture. A shaft that easily withstands a static load of 200 MPa may fracture after 10⁶ cycles at only 80 MPa.

The **S-N curve** (Wöhler curve) is the primary characterization tool. On a semi-log or log-log plot of applied stress amplitude S versus cycles to failure N_f, the curve slopes downward: higher stress amplitude produces fewer cycles to failure. For ferrous metals — steel and cast iron — the S-N curve typically flattens at high cycle counts, becoming horizontal at the **endurance limit** S_e (roughly 0.4–0.5 × tensile strength for steels). Below this stress, the material is assumed to survive indefinitely. Nonferrous metals (aluminum, titanium, copper alloys) show no true horizontal asymptote; their S-N curves continue declining, so fatigue design uses a **fatigue strength at a specified life**, typically 10⁷ or 10⁸ cycles. The engineering implication: for aluminum aircraft components, every cycle counts, and there is no stress low enough to guarantee infinite life.

Fatigue damage initiates at **stress concentrations** — locations where the local stress significantly exceeds the nominal (average section) stress. Notches, holes, fillet radii, weld toes, machining marks, and internal voids all act as stress raisers. The stress concentration factor K_t quantifies the amplification: if K_t = 2 and the nominal stress is 100 MPa, the local stress is 200 MPa. Fatigue responds to local stress, not nominal stress, so even a small K_t at a sharp notch can elevate local stress above the endurance limit while the bulk of the component remains elastic. This is why fatigue design focuses on surface finish, avoiding sharp corners, and minimizing geometric discontinuities — a smooth, polished specimen may have an endurance limit twice that of the same material with a notch.

Once a crack initiates (Stage I), it propagates under the tensile portion of each stress cycle (Stage II). Each cycle advances the crack tip by a small increment, leaving a characteristic **beach mark** or **fatigue striation** on the fracture surface — each striation corresponds to one cycle of crack advance, making striations visible evidence of cyclic loading history. Crack propagation continues until the remaining net section can no longer support the peak load in the cycle, at which point sudden final fracture (Stage III) occurs. The final fracture zone is rough and granular (typical of fast fracture), clearly distinguishable from the smooth, striated crack propagation zone. This fracture surface morphology is the forensic signature of fatigue failure and is the starting point of any failure analysis investigation involving cyclic loading.
