---
id: galaxy-rotation-curves-dark-matter
title: Galaxy Rotation Curves and Dark Matter
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: galaxy-morphology-and-classification
  type: hard
- id: kepler-laws-planetary-orbits
  type: soft
builds-toward:
- cosmological-redshift-and-hubble-law
tags:
- dark-matter
- galaxy-dynamics
- mass-distribution
stage: formal-systems
status: validated
---

# Galaxy Rotation Curves and Dark Matter

## Core Idea
Galaxy rotation curves measure orbital velocities of gas and stars at different distances from the galactic center using Doppler shifts. Observations show rotation curves remaining roughly flat at large radii, contrary to the prediction from visible matter alone. This discrepancy reveals non-luminous dark matter dominating the gravitational potential beyond the luminous disk, comprising ~85% of galactic mass. Dark matter's nature—whether WIMPs, axions, or other particles—remains a fundamental open question.

## How It's Best Learned
Study actual rotation curve data from nearby galaxies like Andromeda and the Milky Way. Understand how orbital mechanics predicts velocity curves and why flat curves require dark matter. Consider alternative explanations and the evidence favoring dark matter.

## Questions

```yaml
- question: "If most of a spiral galaxy's visible mass is concentrated in its central bulge (as it appears to be), what does orbital mechanics predict the rotation curve should look like at large radii?"
  type: multiple-choice
  options:
    - "Flat — velocity stays roughly constant because the disk provides a uniform mass sheet"
    - "Rising — stars at larger radii move faster because they are farther from the gravitational center"
    - "Declining — velocity should fall off at large radii, roughly as v ∝ 1/√r, like planets in the solar system"
    - "Oscillating — velocities alternate high and low depending on the density of spiral arms"
  answer: 2
  explanation: "From Kepler's laws: for a roughly point-mass or centrally concentrated mass M, orbital velocity v = √(GM/r), which decreases with radius as v ∝ 1/√r. This is exactly what we see in the solar system — Mercury orbits much faster than Neptune. If galaxies had most of their mass in the visible bulge, the same Keplerian decline would apply at large radii beyond the visible disk. The observed FLAT curve is therefore shocking and cannot be explained by the visible mass distribution."

- question: "Galaxy rotation curves are observed to be flat at large radii — orbital velocity stays roughly constant far beyond the visible disk. What does this directly imply about the distribution of mass in the galaxy?"
  type: multiple-choice
  options:
    - "The galaxy has no mass beyond the visible disk, but the rotation is maintained by electromagnetic forces"
    - "The total enclosed mass must increase proportionally with radius, even where no visible matter is present"
    - "Gravity works differently at galactic scales, so the normal mass-velocity relationship does not apply"
    - "The flat curve reflects the average of many stars at different distances, masking the true Keplerian decline"
  answer: 1
  explanation: "For circular orbital velocity to be constant (v = constant), we need GM(r)/r = v² = constant, which means M(r) ∝ r — the enclosed mass grows linearly with radius. But at large radii, the visible stars and gas have already thinned out, so visible mass M(r) is roughly constant — not growing. Something invisible must be contributing mass that keeps increasing with radius. This is the dark matter halo: a roughly spherical distribution of non-luminous mass extending 5–10 times beyond the visible disk."

- question: "The observation that galaxy rotation curves remain flat at large radii is consistent with the distribution of visible stars and gas in the galactic disk."
  type: true-false
  answer: false
  explanation: "This is the core observational puzzle. The visible light in spiral galaxies is concentrated in the bright central bulge and thins out rapidly at large radii — the luminous disk essentially ends. If rotation curves were determined by visible mass alone, they should show a Keplerian decline (v ∝ 1/√r) at large radii. The observed flat curves require mass to keep increasing with radius even in regions where there is no visible matter, implying a dominant dark matter halo that the light distribution cannot account for."

- question: "If orbital velocity v is constant at large galactic radii, the enclosed mass M(r) within radius r must increase proportionally with r."
  type: true-false
  answer: true
  explanation: "This follows directly from the orbital mechanics: for a circular orbit, gravitational force equals centripetal force, giving v² = GM(r)/r. If v is constant, then GM(r)/r = constant, so M(r) = v²r/G ∝ r. The enclosed mass must grow linearly with radius. Since visible mass stops increasing beyond the luminous disk, the additional mass must be invisible — the dark matter halo. This is why flat rotation curves are the primary kinematic evidence for dark matter."

- question: "Why do flat rotation curves require a dark matter halo rather than simply a redistribution of the galaxy's existing visible mass to larger radii?"
  type: short-answer
  answer: "Because we can directly observe where the visible matter is — stars and gas traced by light emission and absorption — and it really does thin out at large radii. The 21-cm hydrogen line maps gas well beyond the stellar disk and also shows no sufficient mass increase. The required M(r) ∝ r growth at large radii exceeds what any redistribution of observed matter could provide. The dark matter halo must contain roughly 85% of the total galactic mass with no corresponding luminous component."
  explanation: "The key point is that astronomers have independent observational tracers of visible mass (optical starlight, hydrogen 21-cm, CO emission), and all of them confirm that luminous matter does not extend to large radii in sufficient density. The flat curves are measured at radii where the luminous mass is already roughly constant, yet velocity stays constant — requiring non-luminous mass that simply isn't there in visible form. Multiple independent lines of evidence (gravitational lensing, cluster dynamics, CMB) confirm this conclusion."
```

## Explainer

From your study of galaxy morphology, you can distinguish spirals from ellipticals and understand how stars and gas are distributed within galaxies. From Kepler's laws, you know that orbital velocity depends on the mass enclosed within the orbit — objects farther from a central mass should orbit more slowly, just as Neptune orbits the Sun more slowly than Earth. Combining these two ideas leads to one of the most important discoveries in modern astrophysics: the evidence that most of the matter in galaxies is invisible.

The technique is straightforward in principle. Astronomers measure the **rotation curve** of a spiral galaxy — the orbital velocity of stars and gas as a function of distance from the galactic center. For gas, this is done using the Doppler shift of the 21-cm hydrogen emission line, which can be observed far beyond the visible stellar disk. For a galaxy where most mass is concentrated in the bright central bulge (as the visible light suggests), Kepler's laws predict that orbital velocity should rise in the inner regions (as more mass is enclosed) and then fall off at larger radii, roughly as v ∝ 1/√r — the same way planetary velocities decrease with distance from the Sun.

What observers actually find is dramatically different. Beginning with Vera Rubin and Kent Ford's systematic measurements in the 1970s, rotation curves of spiral galaxies were shown to remain **flat** — orbital velocities stay roughly constant out to the farthest measurable radii, far beyond where the visible stars and gas thin out. For velocity to remain constant at large radius, the enclosed mass must continue increasing linearly with distance: M(r) ∝ r. But there is no corresponding increase in visible matter at those distances. The luminous disk has already faded away, yet something is still contributing gravitational mass. This unseen component is what astronomers call **dark matter**, and the flat rotation curves require it to be distributed in a roughly spherical **halo** extending well beyond the visible galaxy — typically 5 to 10 times the radius of the stellar disk.

The amount of dark matter required is enormous: roughly 85% of a typical galaxy's total mass is dark. This conclusion is not based on rotation curves alone — it is confirmed independently by gravitational lensing (the bending of background light by foreground mass), the dynamics of galaxy clusters, and the pattern of fluctuations in the cosmic microwave background. Alternative explanations have been proposed, most notably **Modified Newtonian Dynamics** (MOND), which adjusts the law of gravity at very low accelerations to reproduce flat rotation curves without dark matter. MOND successfully fits many individual galaxy rotation curves, but it struggles with galaxy cluster dynamics and the CMB, where dark matter provides a more complete and consistent explanation. The leading dark matter candidates — **WIMPs** (weakly interacting massive particles) and **axions** — have not yet been directly detected in laboratory experiments, making the identification of dark matter one of the most important open problems in physics.
