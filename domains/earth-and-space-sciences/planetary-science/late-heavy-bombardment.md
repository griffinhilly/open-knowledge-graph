---
id: late-heavy-bombardment
title: Late Heavy Bombardment and Planetary Migration
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: planetary-formation
  type: hard
- id: planetary-migration-mechanisms
  type: hard
builds-toward:
- planetary-system-stability
tags:
- early-solar-system
- migration
- bombardment
- asteroids
stage: expert
status: validated
---

# Late Heavy Bombardment and Planetary Migration

## Core Idea
The Late Heavy Bombardment (LHB) is the hypothesis that impacts on the inner solar system spiked sharply about 3.8–4.1 billion years ago, long after the planets formed. The original Nice model explained such a spike as the result of a delayed instability among the giant planets, which scattered the outer planetesimal disk. The spike is now contested: re-dated lunar samples, sampling bias and newer dynamical models fit a declining or "sawtooth" impact rate as well or better. Either way, impacts in this era added some water and organic compounds to the terrestrial worlds.

## How It's Best Learned
Sketch impact rate against time in two versions: a smooth decline from 4.5 billion years ago, and a decline with a spike near 3.9 billion years ago. Ask which features of the lunar sample ages would favor each curve. Then check the resonance with Kepler's third law. Today Saturn's period is about 29.5 years and Jupiter's is about 11.9, a ratio near 2.5, so the pair now sits beyond the 2:1 ratio the model says they crossed.

## Common Misconceptions
- In the 2:1 resonance, Jupiter's orbital period was twice Saturn's. (Saturn is farther out and slower. Its period was twice Jupiter's.)
- Earth escaped the bombardment, since it shows few craters from that time. (Earth's larger gravitational cross-section means it was hit even harder than the Moon. Plate tectonics and erosion have erased most of the evidence.)
- The Nice model's account of the bombardment is confirmed. (It remains a model. Both the timing of the giant-planet instability and whether a sharp spike in impacts happened at all are still debated.)

## Questions

```yaml
- question: "The Nice model explains the Late Heavy Bombardment as the gradual clearing of leftover debris from the initial planetary formation phase. Which of the following best describes what the model actually proposes?"
  type: multiple-choice
  options:
    - "The LHB was indeed gradual debris clearing — the Nice model refines the timing but not the mechanism"
    - "The LHB was triggered by Jupiter and Saturn crossing an orbital resonance, destabilizing the outer solar system and flinging planetesimals inward"
    - "The LHB was caused by a rogue star passing through the solar system and gravitationally perturbing asteroid orbits"
    - "The LHB was triggered by Mars forming late and disturbing the asteroid belt through repeated close passes"
  answer: 1
  explanation: "The original Nice model proposes that the LHB was NOT gradual debris clearing but a dynamically triggered event. When Jupiter and Saturn crossed the 2:1 mean-motion resonance, it destabilized the entire outer solar system, flinging Uranus and Neptune into the planetesimal disk and scattering vast numbers of impactors inward. In this account, a delayed instability produces a distinct second pulse of impacts some 400 million years after the planets formed. Whether that pulse actually happened is a separate question, and it is now debated."

- question: "Beyond the obvious destructive impact record, the Late Heavy Bombardment may have contributed constructively to Earth's habitability. Which of the following best describes this constructive role?"
  type: multiple-choice
  options:
    - "The impacts melted and homogenized Earth's mantle, allowing plate tectonics to begin"
    - "The bombardment sterilized the early Earth, giving simple chemistry time to produce the first life"
    - "Cometary and asteroidal impactors delivered volatile compounds including water and organic molecules to the inner planets"
    - "The heat from impacts drove volcanic activity that built up the early atmosphere"
  answer: 2
  explanation: "Impactors in this era — rocky asteroids and, in some models, icy comets from the outer disk — delivered volatile compounds: water, CO₂, nitrogen, and organic molecules. This holds whether the impacts came as a spike or as the tail of a declining flux. Most of Earth's water probably arrived earlier, during planet formation itself, so late impacts likely added a modest share. Large impacts were destructive to early life (option B gets the effect backwards — repeated sterilization works against life rather than giving it time), and the other options describe internal or volcanic processes, not delivery."

- question: "Apollo impact-melt rocks cluster in age near 3.9 Gya. Critics of the bombardment spike argue that this cluster could appear even if the impact rate was declining steadily, because many Apollo samples may come from a single basin-forming impact."
  type: true-false
  answer: true
  explanation: "This is a real argument in the debate. The Apollo 15, 16 and 17 sites lie near the Imbrium, Serenitatis and Nectaris basins, and Imbrium ejecta spread across much of the near side. If many dated samples are Imbrium debris, one event can look like many. Re-analysis of argon-argon ages adds a second concern: later impacts can partly reset older rocks, piling ages up near the end of heavy cratering. Supporters of the spike counter with lunar meteorites and asteroid meteorites that also show ages near 3.9–4.1 Gya. The statement describes the critics' case correctly; it does not settle which side is right."

- question: "The Nice model's giant-planet instability only works if it happened about 3.9 billion years ago, so evidence for an earlier instability would rule out the model."
  type: true-false
  answer: false
  explanation: "The instability mechanism does not fix its own timing. The original 2005 version tuned the delay to match a 3.9 Gya spike, but later versions let the instability happen much earlier. The survival of the fragile Patroclus–Menoetius binary among Jupiter's Trojan asteroids suggests the instability came within about 100 million years of planet formation. If so, the giant planets still reshaped the solar system, but they did not cause the youngest lunar basins. Those impacts would then come from leftover planet-building debris, as in declining-flux or sawtooth models."

- question: "Why does the Nice model predict that the giant planets would trigger a bombardment hundreds of millions of years after planetary formation, rather than immediately?"
  type: short-answer
  answer: "The Nice model proposes that the giant planets began in a compact configuration and slowly evolved toward a resonance crossing through gradual gravitational interactions with the outer planetesimal disk. The slow drift of orbital periods eventually brought Jupiter and Saturn to the 2:1 mean-motion resonance — a process taking hundreds of millions of years. Only at that resonance crossing did the instability become dramatic enough to scatter Uranus and Neptune outward into the disk, which then flung vast numbers of icy bodies inward. The delay is the time it took orbital drift to reach the critical resonance threshold."
  explanation: "The key is that the resonance crossing requires orbits to evolve slowly first. Gravitational interactions with the planetesimal disk gradually shift orbital periods. Only when the ratio of orbital periods reached the critical value (2:1 for Jupiter-Saturn) did the resulting resonant perturbations become large enough to trigger the cascade. This is why the model predicts a spike rather than a continuous decline — it marks the moment the system crossed a dynamical threshold. The length of the delay depends on how far the disk sat from the planets, and later versions of the model allow a much shorter one."
```

## Explainer

After the initial burst of planetary formation wound down roughly 4.5 billion years ago, the solar system did not settle into a calm state immediately. In the 1970s, radiometric ages of impact-melt rocks returned by the Apollo missions were found to cluster between about 3.8 and 4.1 billion years ago. Researchers read this as a sharp spike in impacts, several hundred million years after the planets had assembled, and named it the lunar cataclysm or **Late Heavy Bombardment** (LHB). The puzzle it posed was clear: if leftover debris from planet formation should have been swept up early, what caused a second wave of impacts so late? Today the question comes first: did the spike happen at all?

The best-known explanation for a spike comes from the **Nice model**, named after the French city where it was developed. Building on the planetary migration mechanisms you already know, the Nice model proposes that the four giant planets initially orbited in a much more compact configuration than they do today. For hundreds of millions of years, gravitational interactions with a dense outer disk of planetesimals gradually nudged the giant planets' orbits. Eventually, Jupiter and Saturn crossed a critical **orbital resonance** — likely the 2:1 mean-motion resonance, where Saturn's orbital period was exactly twice Jupiter's. In the model, this resonance crossing destabilized the entire outer solar system in a geologically brief episode. Uranus and Neptune were flung outward into the planetesimal disk, scattering vast numbers of icy bodies inward, while the shifting resonances stirred rocky asteroids out of the main belt.

The case for a spike has weakened since then. Much of the Apollo material may be ejecta from a single basin, Imbrium, so one impact could look like many. Re-analysis of argon-argon ages suggests that later impacts partly reset older rocks, which can pile ages up near 3.9 billion years even under a steady decline. Some lunar meteorites, which sample random spots on the Moon, show a broader spread of melt ages. Dynamical work has also moved: the survival of a fragile binary asteroid among Jupiter's Trojans points to a giant-planet instability within the first 100 million years, too early to make the youngest lunar basins. Many researchers now favor a declining flux from leftover planet-building debris, or a "sawtooth" with a modest uptick near 4.1 billion years ago. Supporters of the spike point to meteorite ages and lunar chemistry that still fit a late surge. Basins such as Imbrium and Orientale are about 3.8–3.9 billion years old either way; the dispute is over how many basins formed shortly before them.

Whatever its shape, impacts in this era may have played a constructive role. Asteroids and comets delivered **volatile compounds** — water, carbon dioxide, nitrogen, and organic molecules — to the inner planets. Most of Earth's water probably arrived earlier, during planet formation, so late impacts likely added a modest share. Earth, with its larger gravitational cross-section, was hit harder than the Moon, though plate tectonics and erosion have erased most of the record. Large impacts would have sterilized surface environments at times, so early life may have faced bottlenecks. How severe those were depends on whether the impacts came as a late burst or a slow decline, which is one reason the debate matters for the origin of life.
