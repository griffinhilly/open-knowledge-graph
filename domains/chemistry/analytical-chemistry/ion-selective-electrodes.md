---
id: ion-selective-electrodes
title: Ion-Selective Electrodes
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: potentiometry
  type: hard
tags:
- ISE
- glass electrode
- membrane potential
- Nernst equation
- selectivity coefficient
- pH electrode
- fluoride electrode
stage: formal-systems
status: draft
---

# Ion-Selective Electrodes

## Core Idea
An ion-selective electrode (ISE) develops a potential across a membrane that responds preferentially to one target ion, allowing its activity (and, with appropriate calibration, concentration) to be measured potentiometrically. The glass pH electrode is the most familiar example: a thin glass membrane generates a potential proportional to the logarithm of H⁺ activity according to the Nernst equation. Other ISEs use crystalline membranes (fluoride electrode with LaF₃), liquid membranes (calcium electrode with organophosphate ionophore), or polymer membranes doped with selective ionophores. The selectivity coefficient quantifies how much an interfering ion contributes to the measured potential; a smaller coefficient means better selectivity for the target ion.

## How It's Best Learned
Calibrate a fluoride ISE with a series of standards in TISAB (total ionic strength adjustment buffer), construct a Nernst plot of potential vs. log[F⁻], and then measure fluoride in a tap water sample. Observing the near-ideal 59.2/n mV slope and seeing how ionic-strength adjustment matters builds intuition for the technique's strengths and practical requirements.

## Common Misconceptions
- ISEs measure ion activity, not concentration; converting to concentration requires controlling or knowing the ionic strength, which is why total ionic strength adjustment buffers are essential for accurate work.
- No ISE is perfectly selective — the selectivity coefficient is never zero, so high concentrations of interfering ions can bias results even with a supposedly 'selective' electrode.

## Explainer

From your study of potentiometry, you know that electrochemical cells can generate voltages that depend on the concentration (more precisely, the activity) of ions in solution. An **ion-selective electrode** exploits this principle by incorporating a membrane that responds preferentially to one specific ion. When target ions interact with the membrane — either by exchanging into it, binding to sites within it, or migrating through its crystal lattice — a potential difference develops across the membrane that is proportional to the logarithm of the ion's activity. This logarithmic relationship is described by the Nernst equation, which predicts a slope of 59.16/n mV per decade of activity change at 25°C, where n is the ion's charge.

The most familiar ISE is the **glass pH electrode**, which has been used for over a century. Its thin glass membrane contains metal oxide sites that selectively exchange hydrogen ions. When immersed in solution, H⁺ ions interact with the hydrated gel layer on the glass surface, and the resulting charge separation generates a potential that changes by approximately 59.2 mV for each unit change in pH. But the same principle applies to many other ions. A **fluoride electrode** uses a crystal of lanthanum fluoride (LaF₃) doped with europium — fluoride ions migrate through vacancies in the crystal lattice, and the resulting potential responds selectively to fluoride with a near-Nernstian slope of −59.2 mV per decade. Calcium and potassium electrodes use liquid or polymer membranes containing organic molecules called **ionophores** — molecules designed to wrap around a specific ion and carry it selectively across the membrane.

In practice, using an ISE requires careful attention to several factors. First, because ISEs measure **activity** rather than concentration, you must control the ionic strength of your standards and samples. This is typically accomplished by adding a **total ionic strength adjustment buffer (TISAB)** — a high-concentration inert salt that swamps the variable ionic strength of different samples, making the activity coefficient effectively constant. Second, calibration requires at least two standards spanning the expected concentration range, and the measured potential-versus-log-activity plot should yield a slope close to the theoretical Nernstian value. A slope significantly below theoretical indicates a tired or damaged membrane.

The key limitation is **selectivity**. The Nikolsky-Eisenman equation extends the Nernst equation to include the contribution of interfering ions, weighted by a **selectivity coefficient** (K). A selectivity coefficient of 10⁻³ for an interferent means that the interferent must be present at 1000 times the target ion's concentration to produce an equivalent potential change. This sounds impressive, but in real samples — seawater, blood, or industrial wastewater — interfering ions can easily reach concentrations that matter. Understanding the selectivity coefficients for your electrode and your sample matrix is essential for knowing when ISE results are trustworthy and when you need to choose a different technique.
