---
id: precipitation-hardening
title: Precipitation Hardening
domain: engineering
course: materials-science
prerequisites:
- id: strengthening-mechanisms
  type: hard
- id: phase-diagrams-binary
  type: hard
builds-toward:
- materials-selection-design
tags:
- age-hardening
- nucleation-and-growth
- coherent-precipitates
- overaging
- guinier-preston-zones
stage: formal-systems
status: validated
---

# Precipitation Hardening

## Core Idea
Precipitation hardening (age hardening) strengthens an alloy by dispersing fine second-phase particles throughout the matrix, forcing dislocations to either cut through or bow around them. The process requires three steps: solution treatment (dissolving the solute into a single-phase solid solution at high temperature), quenching (rapidly cooling to trap the solute in a supersaturated state), and aging (holding at an intermediate temperature to allow controlled precipitation). During aging, precipitates evolve through a sequence — from coherent Guinier-Preston (GP) zones that share the matrix lattice, to semi-coherent intermediate precipitates, to incoherent equilibrium precipitates. Peak hardness occurs at an optimal aging time when precipitates are large enough to strongly impede dislocations but still coherent or semi-coherent with the matrix. Beyond this point, overaging occurs: precipitates coarsen (Ostwald ripening), lose coherency, and the spacing between them increases, reducing their effectiveness as barriers. The Al-Cu system is the classic example, but precipitation hardening is used extensively in nickel superalloys, maraging steels, and titanium alloys.

## How It's Best Learned
Plot hardness versus aging time at a fixed temperature to see the characteristic rise-to-peak-then-decline curve. Use a phase diagram with a solvus line to identify the temperature windows for solution treatment and aging. Examine TEM micrographs showing GP zones, intermediate precipitates, and coarsened equilibrium particles to connect microstructure to mechanical response at each aging stage.

## Common Misconceptions
- Precipitation hardening is not instantaneous after quenching — the supersaturated solution must be aged at a controlled temperature for the precipitates to form and reach optimal size.
- Overaging does not mean the material is ruined; it simply means the precipitates have grown past the peak-hardness configuration. The material can often be re-solution-treated and re-aged.
- Larger precipitates are not stronger obstacles — peak strength corresponds to fine, closely spaced precipitates that force dislocations to interact with many particles simultaneously.

## Questions

```yaml
- question: "An aluminum alloy is aged at 150°C. After 4 hours it reaches peak hardness. An engineer continues aging it for 24 hours to 'fully develop' the precipitates. What happens to the hardness?"
  type: multiple-choice
  options:
    - "Hardness continues to increase as more precipitates nucleate and grow"
    - "Hardness remains constant — once peak hardness is reached, further aging has no effect"
    - "Hardness decreases — precipitates coarsen through Ostwald ripening, lose coherency, and become less effective dislocation barriers"
    - "Hardness oscillates — precipitates grow and dissolve repeatedly during extended aging"
  answer: 2
  explanation: "Extended aging beyond the peak causes overaging. Ostwald ripening drives large precipitates to grow at the expense of small ones — total particle count decreases, average spacing increases. The equilibrium precipitates that form lack coherency strain fields, and dislocations can bypass them via the Orowan mechanism at lower stress. The result is a declining hardness curve. Option A is the classic misconception: 'more aging = more hardening.' Peak hardness occurs at the semi-coherent intermediate precipitate stage, not at maximum precipitate size."

- question: "During early aging (GP zone formation), what is the primary mechanism by which fine precipitates impede dislocation motion?"
  type: multiple-choice
  options:
    - "The GP zones are hard, incoherent obstacles that physically block dislocations from advancing"
    - "Coherency strain fields around the zones distort the surrounding lattice, increasing the stress required for dislocations to cut through the mismatched region"
    - "The zones attract vacancies, which cluster around dislocations and pin them in place"
    - "The high density of zone-matrix interfaces scatters dislocations in random directions"
  answer: 1
  explanation: "GP zones are coherent with the matrix — their lattice planes are continuous with the surrounding aluminum. This coherency creates elastic strain fields in the surrounding lattice due to misfit. Dislocations must cut through these strained regions, which requires additional energy (higher applied stress). It is the strain field, not the particle itself, that does the strengthening. As precipitates coarsen and become incoherent (overaging), they lose these strain fields and become weaker obstacles — dislocations bypass them by Orowan looping rather than cutting."

- question: "An alloy that has been overaged can be restored to near-peak hardness by re-solution treating above the solvus temperature followed by re-quenching and re-aging."
  type: true-false
  answer: true
  explanation: "Overaging changes the precipitate microstructure but does not permanently alter the alloy chemistry. Re-solution treatment above the solvus dissolves the coarsened equilibrium precipitates back into a homogeneous solid solution, and the three-step process (solution treat → quench → age) can be repeated to regenerate the fine precipitate structure associated with peak hardness. This is why overaging is not catastrophic — it is recoverable, unlike true microstructural damage such as cracking."

- question: "Larger precipitate particles are stronger barriers to dislocation motion than smaller ones at the same volume fraction."
  type: true-false
  answer: false
  explanation: "At the same volume fraction, larger particles mean fewer particles and greater inter-particle spacing. Dislocations encounter obstacles less frequently and can bow more easily around widely spaced particles (Orowan mechanism), requiring less stress. Fine, closely spaced precipitates force dislocations to interact with many obstacles simultaneously, maximizing strengthening. This is why peak hardness corresponds to the fine semi-coherent precipitate stage, not the fully grown equilibrium stage — larger is weaker, not stronger, for the same volume fraction."

- question: "Why does hardness first increase then decrease during aging at a fixed temperature, even though precipitates continue to grow throughout the entire aging period?"
  type: short-answer
  answer: "During early aging, fine coherent and semi-coherent precipitates form with strong coherency strain fields and close spacing — dislocations must cut through many strained regions, requiring high stress. Hardness rises. At peak hardness, the semi-coherent precipitates are optimally sized: large enough to create strong strain fields but still closely enough spaced that dislocations cannot easily bypass them. During overaging, Ostwald ripening coarsens the precipitates: fewer, larger, more widely spaced incoherent particles. Incoherent particles lack coherency strain fields, and widely spaced particles allow dislocations to bypass via Orowan looping at lower stress. Hardness falls even though total precipitate volume is roughly constant — it is size and coherency, not quantity, that determines strengthening."
  explanation: "This rise-then-fall hardness curve is the hallmark signature of precipitation hardening. The engineering lesson is that aging time and temperature are design variables: the goal is the 'peak aged' condition, not simply 'as much aging as possible.' Over-specification of aging time is a common manufacturing error."
```

## Explainer

From strengthening mechanisms, you know that strength in metals comes from making dislocation motion difficult. The more barriers a dislocation encounters — grain boundaries, solute atoms, other dislocations, or second-phase particles — the higher the stress required to push it through the lattice. **Precipitation hardening** exploits phase diagrams to generate a dense, tunable dispersion of very fine particles inside the crystal, creating the most potent obstacle array achievable in metallic systems.

The starting point is a phase diagram with a **solvus** line — a curved boundary that separates a single-phase solid solution (at high temperature) from a two-phase field (at lower temperature). In the Al-Cu system, above the solvus a copper-rich solid solution in aluminum is stable; below it, a second phase (the θ phase, CuAl₂) is thermodynamically favored. The three-step process uses this geometry directly. First, **solution treatment**: heat well above the solvus to dissolve all copper into a homogeneous FCC aluminum matrix. Second, **quench**: cool rapidly enough that copper atoms are frozen in place — they cannot diffuse to form the equilibrium θ phase, so the alloy is now a **supersaturated solid solution** out of equilibrium but temporarily stable. Third, **aging**: hold at an intermediate temperature. Here, with moderate thermal energy, copper atoms begin to cluster and precipitate. But the sequence of precipitates they form is not the equilibrium θ phase — not at first.

The early precipitates are **Guinier-Preston (GP) zones**: thin, plate-like clusters of copper atoms, just a few atomic layers thick, that remain coherent with the aluminum matrix (their lattice planes are continuous with the surrounding matrix). This coherency creates local strain fields around each zone, and it is these strain fields — not the zones themselves — that impede dislocations by forcing them to cut through mismatched lattice regions. As aging continues, GP zones grow into larger, semi-coherent intermediate precipitates (θ'' and θ'), which are even more effective obstacles. Peak hardness typically occurs at this semi-coherent stage: precipitates are large enough to create strong strain fields but still closely enough spaced that dislocations encounter many of them before traveling far.

Beyond peak hardness, **overaging** occurs. The intermediate precipitates grow into the incoherent equilibrium θ phase via Ostwald ripening — larger particles grow at the expense of smaller ones, because the smaller particles have higher surface energy. The equilibrium precipitates have no coherency strain field, so they are weaker obstacles. Worse, as the total number of particles decreases and average spacing increases, the **Orowan mechanism** becomes relevant: instead of cutting through particles, dislocations bow around them and bypass, leaving dislocation loops. The critical stress for Orowan bowing decreases as particle spacing increases. The result is a declining hardness curve with continued aging time. The engineering lesson is that aging time and temperature are variables to be optimized, not just minimized — there is a specific "peak aged" condition that maximizes strength.
