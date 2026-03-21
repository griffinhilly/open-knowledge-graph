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
stage: advanced
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

## Questions

```yaml
- question: "You measure the same seawater sample with a sodium ISE twice: once after adding TISAB and once without. The reading without TISAB is higher. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "TISAB introduces a systematic negative error by binding sodium ions"
    - "Without TISAB, samples and standards have different ionic strengths, making activity coefficients unequal and causing concentration to be overestimated"
    - "The ISE membrane is damaged by high salt concentrations and must be equilibrated with TISAB first"
    - "Seawater's ionic strength is too low to activate the ISE membrane properly without TISAB"
  answer: 1
  explanation: "ISEs respond to ion activity, not concentration. Activity = activity coefficient × concentration. Without TISAB, the seawater sample has much higher ionic strength than the calibration standards (which are typically prepared in low-ionic-strength solutions), so the sample's activity coefficient is lower than the standards'. The electrode reads a similar potential to a lower-concentration standard, causing the calculated concentration to be wrong — not necessarily higher. The key principle: TISAB swamps variable ionic strength by adding a high concentration of an inert salt, making all samples and standards have the same ionic strength and therefore the same activity coefficient. Option A is wrong: TISAB contains complexing agents for interfering ions (like CDTA for fluoride) but not for the target ion."

- question: "A potassium ISE has a selectivity coefficient of K(K,Na) = 0.01 for sodium. A sample contains 1 mM K⁺ and 100 mM Na⁺. How significant is the sodium interference?"
  type: multiple-choice
  options:
    - "Negligible — sodium is a different element and ISEs are perfectly selective"
    - "Significant — the effective sodium contribution equals 100 mM × 0.01 = 1 mM, which equals the potassium concentration and introduces ~100% error"
    - "Moderate — sodium at 100 mM contributes 0.1 mM equivalent of potassium, or ~10% error"
    - "Significant — sodium at 100 mM overwhelms the ISE regardless of the selectivity coefficient"
  answer: 1
  explanation: "The Nikolsky-Eisenman equation tells us that an interfering ion j with selectivity coefficient K(i,j) contributes an apparent concentration of K(i,j) × [j] to the measured signal. Here: 0.01 × 100 mM = 1 mM apparent potassium from sodium alone. Since the actual potassium is only 1 mM, the interference doubles the measured signal — a 100% error. This example illustrates why knowing the selectivity coefficient and your sample matrix is essential: an apparently good selectivity coefficient (10⁻²) can still cause catastrophic error when interfering ions are present at 100-fold excess."

- question: "An ISE with a Nernstian slope measures the concentration of an ion directly."
  type: true-false
  answer: false
  explanation: "A Nernstian slope means the electrode responds ideally to changes in ion activity, not concentration. Activity = γ × c, where γ is the activity coefficient that depends on ionic strength. In dilute solutions or when ionic strength is carefully controlled (e.g., via TISAB), activity and concentration are numerically close. But in real complex samples, they can differ substantially. The Nernstian slope confirms the membrane is functioning correctly, but converting potential to concentration still requires either (1) matching ionic strength between standards and samples, or (2) knowing the activity coefficient. This is the most persistent misconception about ISEs."

- question: "A fluoride ISE with a measured slope of 45 mV/decade (instead of the theoretical 59.2 mV/decade) is likely to give accurate results if the samples are measured immediately."
  type: true-false
  answer: false
  explanation: "A sub-Nernstian slope indicates membrane degradation, contamination, or poor equilibration. The slope matters not just for one measurement but for the entire calibration: if you use the 45 mV/decade slope to convert potentials to concentrations, your results will be systematically wrong — the electrode compresses the dynamic range relative to ideal behavior. Accuracy requires a slope close to theoretical. In practice, a slope below about 54 mV/decade for a monovalent ion is considered unacceptable and the membrane should be reconditioned or replaced. Speed of measurement does not compensate for a bad slope."

- question: "Why do ISEs require total ionic strength adjustment buffer (TISAB), and what problem does it solve?"
  type: short-answer
  answer: "ISEs measure ion activity, not concentration, and activity depends on ionic strength via the activity coefficient (a = γ·c). Different samples have different ionic strengths, so their activity coefficients differ even at the same concentration. TISAB solves this by adding a high-concentration inert electrolyte that overwhelms the variable background ionic strength of all samples and standards, making the ionic strength (and therefore γ) effectively constant across all measurements. This converts the activity measurement into a reliable proxy for concentration."
  explanation: "Without TISAB, a sample with high ionic strength would show lower activity (lower γ) than a low-ionic-strength standard at the same concentration, leading to underestimation. TISAB eliminates this source of error. For fluoride ISEs specifically, TISAB also contains CDTA (a chelating agent) to complex iron and aluminum that would otherwise bind fluoride and reduce the free [F⁻] available to the electrode, plus acetic acid/acetate buffer to control pH (since OH⁻ can interfere with the fluoride electrode at high pH)."
```

## Explainer

From your study of potentiometry, you know that electrochemical cells can generate voltages that depend on the concentration (more precisely, the activity) of ions in solution. An **ion-selective electrode** exploits this principle by incorporating a membrane that responds preferentially to one specific ion. When target ions interact with the membrane — either by exchanging into it, binding to sites within it, or migrating through its crystal lattice — a potential difference develops across the membrane that is proportional to the logarithm of the ion's activity. This logarithmic relationship is described by the Nernst equation, which predicts a slope of 59.16/n mV per decade of activity change at 25°C, where n is the ion's charge.

The most familiar ISE is the **glass pH electrode**, which has been used for over a century. Its thin glass membrane contains metal oxide sites that selectively exchange hydrogen ions. When immersed in solution, H⁺ ions interact with the hydrated gel layer on the glass surface, and the resulting charge separation generates a potential that changes by approximately 59.2 mV for each unit change in pH. But the same principle applies to many other ions. A **fluoride electrode** uses a crystal of lanthanum fluoride (LaF₃) doped with europium — fluoride ions migrate through vacancies in the crystal lattice, and the resulting potential responds selectively to fluoride with a near-Nernstian slope of −59.2 mV per decade. Calcium and potassium electrodes use liquid or polymer membranes containing organic molecules called **ionophores** — molecules designed to wrap around a specific ion and carry it selectively across the membrane.

In practice, using an ISE requires careful attention to several factors. First, because ISEs measure **activity** rather than concentration, you must control the ionic strength of your standards and samples. This is typically accomplished by adding a **total ionic strength adjustment buffer (TISAB)** — a high-concentration inert salt that swamps the variable ionic strength of different samples, making the activity coefficient effectively constant. Second, calibration requires at least two standards spanning the expected concentration range, and the measured potential-versus-log-activity plot should yield a slope close to the theoretical Nernstian value. A slope significantly below theoretical indicates a tired or damaged membrane.

The key limitation is **selectivity**. The Nikolsky-Eisenman equation extends the Nernst equation to include the contribution of interfering ions, weighted by a **selectivity coefficient** (K). A selectivity coefficient of 10⁻³ for an interferent means that the interferent must be present at 1000 times the target ion's concentration to produce an equivalent potential change. This sounds impressive, but in real samples — seawater, blood, or industrial wastewater — interfering ions can easily reach concentrations that matter. Understanding the selectivity coefficients for your electrode and your sample matrix is essential for knowing when ISE results are trustworthy and when you need to choose a different technique.
