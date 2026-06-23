---
id: quenching-and-tempering
title: Quenching and Tempering
domain: engineering
course: materials-science
prerequisites:
- id: heat-treatment-of-steels
  type: hard
- id: iron-carbon-phase-diagram
  type: hard
- id: twinning-and-martensitic-transformation
  type: soft
builds-toward:
- case-hardening-surface-treatments
tags:
- martensite-formation
- quench-media
- tempering
- ttt-diagram
- cct-diagram
- hardenability
stage: formal-systems
status: validated
---

# Quenching and Tempering

## Core Idea
Quenching and tempering is the two-step heat treatment used to produce steels with high strength and adequate toughness. In quenching, steel is heated into the austenite region (above the A3 or Acm line) and then rapidly cooled — in water, oil, polymer solution, or forced air — fast enough to suppress the diffusion-controlled formation of pearlite or bainite, trapping carbon in the iron lattice to form martensite. Martensite is a body-centered tetragonal (BCT) structure supersaturated with carbon; it is extremely hard but brittle. Time-Temperature-Transformation (TTT) diagrams and Continuous-Cooling-Transformation (CCT) diagrams map the kinetics of these phase transformations, showing the cooling rates needed to avoid the "nose" of the pearlite/bainite C-curve and achieve full martensitic transformation. In the tempering step, the as-quenched martensite is reheated to a temperature between 150 and 650 degrees C, allowing carbon to diffuse out and form fine carbide precipitates. This reduces hardness but substantially improves toughness and ductility. The choice of tempering temperature controls the final balance: low-temperature tempering retains high hardness (for cutting tools), while high-temperature tempering maximizes toughness (for structural components). Hardenability — the depth to which martensite forms during quenching — depends on alloy composition, with elements like Mn, Cr, Mo, and Ni shifting the TTT nose to longer times and enabling through-hardening of thicker sections.

## How It's Best Learned
Overlay cooling curves for water, oil, and air quenches onto a TTT diagram for a specific steel (e.g., 1080 or 4340) to predict the resulting microstructure. Then examine a hardness-versus-tempering-temperature plot to see the hardness-toughness trade-off quantitatively. Compare Jominy end-quench test results for plain-carbon versus alloy steels to understand hardenability differences.

## Common Misconceptions
- The quench medium does not directly harden the steel — it controls the cooling rate, which determines whether the austenite transforms to martensite (fast) or pearlite (slow).
- Tempering does not weaken the steel in a detrimental sense; it deliberately trades some hardness for greatly improved toughness, producing a more useful engineering material.
- All steels are not equally hardenable — low-carbon steels cannot form much martensite regardless of quench rate because there is insufficient carbon to distort the lattice.

## Questions

```yaml
- question: "Two identical bars of 1080 steel are austenitized and then quenched: one in cold water, one in warm oil. The water-quenched bar is substantially harder. What is the correct metallurgical explanation?"
  type: multiple-choice
  options:
    - "Water is chemically reactive with steel, causing surface hardening reactions during the quench"
    - "Water quenching cools the steel faster, allowing the cooling curve to miss the pearlite nose on the TTT diagram and form more martensite"
    - "Oil introduces carbon into the steel surface during quenching, reducing the carbon available for hardening"
    - "Water quenching increases dislocation density directly, independent of the phase transformation"
  answer: 1
  explanation: "The quench medium does not directly harden the steel — it controls the cooling rate. A faster cooling rate (water) produces a steeper cooling curve on the TTT diagram that passes to the left of the pearlite C-curve nose, suppressing diffusion and trapping carbon in a BCT martensite structure. Oil cools more slowly; if the cooling curve clips the nose, some austenite transforms to softer pearlite or bainite instead. The hardness comes from martensite formation, not from the medium itself."

- question: "A machinist needs maximum hardness in a tool steel component. After achieving a fully martensitic microstructure by quenching, she considers tempering at 600°C. Her supervisor cautions against this for a cutting tool application. What is the correct reason?"
  type: multiple-choice
  options:
    - "Tempering above 500°C reverses the martensitic transformation, returning the steel to austenite"
    - "High-temperature tempering allows carbon to diffuse out of the BCT lattice and form coarse carbide precipitates, substantially reducing hardness while improving toughness"
    - "600°C tempering introduces residual tensile stresses at the surface, causing delayed cracking"
    - "Tempering at any temperature weakens the steel and should be avoided for all tool applications"
  answer: 1
  explanation: "Tempering allows the supersaturated carbon in as-quenched martensite to diffuse out and precipitate as fine (then coarser at higher temperatures) carbides. This reduces the lattice strain that gives martensite its hardness. High-temperature tempering (500–650°C) maximizes toughness but significantly reduces hardness — the right choice for structural parts, wrong for cutting tools. Low-temperature tempering (150–250°C) retains high hardness with modest toughness improvement, appropriate for cutting and wear applications."

- question: "A low-carbon steel (0.15 wt% C) cannot be significantly hardened by quenching, regardless of how rapid the cooling rate is."
  type: true-false
  answer: true
  explanation: "Martensite hardness depends critically on carbon content. Carbon dissolved in the iron lattice creates the BCT distortion that makes martensite hard and brittle. With only 0.15 wt% C, there is insufficient carbon to create significant lattice strain even if the cooling is fast enough to suppress pearlite formation. Plain low-carbon steels form soft martensite ('lath martensite') that is only marginally harder than ferrite. For effective hardening, steels typically require at least 0.3–0.4 wt% C."

- question: "Tempering is best understood as a corrective step — a way to partially undo an overly aggressive quench that left the steel too brittle."
  type: true-false
  answer: false
  explanation: "Tempering is not corrective; it is a deliberately planned second step that follows a successful quench. As-quenched martensite is intentionally formed to maximize hardness, then intentionally tempered to improve toughness. The two steps together — quenching to martensite, then tempering to calibrate the hardness-toughness balance — constitute the quench-and-temper process. The temper is engineered for the application's requirements, not applied to fix a mistake."

- question: "Explain why the nose of the pearlite C-curve on a TTT diagram occurs at an intermediate temperature rather than at the highest or lowest temperatures, referencing the two competing factors that produce it."
  type: short-answer
  answer: "The nose represents the temperature where pearlite forms fastest. Two factors compete: (1) thermodynamic driving force — the free energy difference between austenite and pearlite, which increases as temperature drops below the eutectoid temperature, providing more driving force at lower temperatures; (2) atomic diffusivity — carbon and iron atoms must diffuse to form the layered pearlite structure, and diffusion slows dramatically as temperature decreases. At high temperatures near the eutectoid, diffusion is fast but driving force is small; at very low temperatures, driving force is large but diffusion is nearly frozen. The nose occurs at the intermediate temperature that best balances both factors — maximizing the transformation rate. This matters for quench selection: any cooling curve that passes through the nose region will produce some pearlite, so the quench medium must be fast enough to miss it entirely."
  explanation: "This is the fundamental reason TTT diagrams have C-shaped curves rather than straight lines. The nose temperature (typically around 550°C for plain carbon steels) sets the critical cooling rate. Alloying elements like Mn, Cr, and Mo shift this nose to longer times by slowing diffusion and stabilizing austenite, reducing the required cooling rate and improving hardenability."
```

## Explainer

The iron-carbon phase diagram you mastered as a prerequisite shows you what phases are thermodynamically stable — but thermodynamic stability is only half the story in heat treatment. The other half is **kinetics**: how fast do those stable phases actually form? When you heat steel into the austenite region and then rapidly cool it, you are racing against the clock. The austenite wants to decompose into ferrite and cementite (pearlite), but doing so requires carbon atoms to diffuse — and diffusion takes time. If you cool fast enough, you outrun the diffusion and the austenite has no choice but to transform to martensite, a metastable phase that captures all the carbon in a strained lattice.

The **TTT (Time-Temperature-Transformation) diagram** makes this concrete. It plots temperature on the y-axis and (logarithmic) time on the x-axis, and it shows C-shaped "nose" curves that mark when pearlite and bainite begin and finish forming at each temperature. The nose of the pearlite C-curve represents the temperature where transformation is fastest — typically around 550°C for plain carbon steels — because it balances two competing factors: the thermodynamic driving force (larger at lower temperature) and atomic diffusivity (faster at higher temperature). To form martensite, your cooling curve on this diagram must pass to the left of the pearlite nose without touching it. The **critical cooling rate** is the minimum rate that achieves this. Water quenching produces steep cooling curves that easily miss the nose; oil quenching is slower and may only just miss it; air cooling is usually too slow for plain carbon steels.

**CCT (Continuous-Cooling-Transformation) diagrams** are more directly applicable to real practice because they account for the changing transformation kinetics as temperature drops continuously, rather than isothermally. The CCT diagram shifts the C-curves to longer times and lower temperatures compared to the TTT diagram, and it shows what microstructure — martensite, bainite, pearlite, or mixtures — results from different cooling rates. Overlaying actual cooling curves (from thermocouple measurements at different depths in a quenched bar) onto the CCT diagram predicts the microstructure at each location. This is why large cross-sections are a problem: the surface cools faster than the center, potentially giving martensite at the surface and softer pearlite in the core.

**Hardenability** quantifies how deeply martensite forms during quenching, and it explains why alloy steels exist. Alloying elements like Mn, Cr, Mo, and Ni slow down pearlite and bainite formation — they shift the TTT nose to longer times — making it easier for slower cooling rates to achieve martensite. A 4340 alloy steel can be through-hardened in a 50 mm bar with an oil quench; a 1080 plain carbon steel of the same size might only harden a few millimeters from the surface. The **Jominy end-quench test** standardizes this measurement: a bar is water-quenched at one end only, and hardness is plotted as a function of distance from the quench end. The resulting **hardenability band** is tabulated for each steel grade. Selecting a steel for a structural component involves matching the hardenability to the required cross-section — too little hardenability leaves soft spots, too much is unnecessary cost. Tempering then calibrates the final property balance: low-temperature tempering (150–250°C) for tools requiring maximum hardness, high-temperature tempering (500–650°C) for structural parts requiring toughness.
