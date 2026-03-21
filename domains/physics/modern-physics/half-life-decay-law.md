---
id: half-life-decay-law
title: Half-Life and the Radioactive Decay Law
domain: physics
course: modern-physics
prerequisites:
- id: radioactive-decay
  type: hard
- id: exponential-functions-and-graphs
  type: hard
- id: exponential-growth-and-decay
  type: soft
- id: natural-logarithm-and-e
  type: soft
builds-toward:
- nuclear-fission-fusion
tags:
- nuclear
- half-life
- decay-constant
- exponential
- carbon-dating
stage: advanced
status: validated
---

# Half-Life and the Radioactive Decay Law

## Core Idea
The number of undecayed nuclei decreases exponentially: N(t) = N₀ e^(−λt), where λ is the decay constant (probability of decay per unit time per nucleus). The half-life T½ = ln2/λ is the time for half the nuclei to decay, independent of how many remain. The activity A = λN also decays exponentially. Because each nucleus decays independently with fixed probability, the decay law is exact on average for large N and follows from Poisson statistics. Applications include radiocarbon dating, medical isotopes, and nuclear waste management.

## How It's Best Learned
Derive N(t) by solving the first-order ODE dN/dt = −λN. Practice computing the amount remaining after multiple half-lives without a calculator. For carbon-14 dating, work backward from activity ratio to time.

## Common Misconceptions
- After two half-lives none of the material remains — after two half-lives one-quarter remains; the material never fully disappears in finite time.
- The decay law implies you can predict exactly when a nucleus will decay — the law predicts average rates; individual decays are random quantum events with no deterministic schedule.

## Questions

```yaml
- question: "A radioactive sample has undergone exactly 3 half-lives since it was created. What fraction of the original nuclei remains undecayed?"
  type: multiple-choice
  options:
    - "None — after 3 half-lives the material has fully decayed"
    - "1/3 — one-third remains after dividing by the number of half-lives elapsed"
    - "1/6 — each half-life removes another sixth of the original amount"
    - "1/8 — each half-life halves the remaining amount, so (1/2)³ = 1/8"
  answer: 3
  explanation: "After each half-life, exactly half of *what remains* decays — not half of the original. After 1 half-life: 1/2 remains. After 2: 1/4. After 3: 1/8. Option A is the most common misconception: radioactive material never fully disappears in finite time. Options B and C misapply arithmetic division rather than repeated halving. The key formula is (1/2)^n after n half-lives, which follows directly from N(t) = N₀ e^(−λt) evaluated at t = nT½."

- question: "What does the decay constant λ physically represent for a radioactive nucleus?"
  type: multiple-choice
  options:
    - "The time required for exactly one nucleus in the sample to decay"
    - "The probability per unit time that any given nucleus will decay, independent of how long it has already survived"
    - "The total number of decays that will occur before the sample is exhausted"
    - "The average time between successive decays in a large sample"
  answer: 1
  explanation: "λ is a probability rate — units of inverse time (e.g., per second). Each nucleus has a fixed probability λ·dt of decaying in any small time interval dt, regardless of its age. This memoryless property is what makes the decay law exponential: the fraction decaying per unit time is always the same constant λ, so the *number* decaying per unit time is proportional to N, giving dN/dt = −λN. Option A confuses λ with the mean lifetime τ = 1/λ. Options C and D describe the activity, not the decay constant itself."

- question: "After two half-lives have elapsed, none of the original radioactive material remains."
  type: true-false
  answer: false
  explanation: "After two half-lives, one-quarter (1/4) of the original nuclei remains undecayed. The material never fully disappears in finite time — exponential decay is asymptotic. Each half-life halves *whatever is currently present*, so you always have something left, even if the amount becomes negligibly small. After 10 half-lives, about 0.1% remains; after 100 half-lives, an extraordinarily tiny fraction persists. This is the most common misconception about half-lives."

- question: "Because radioactive decay is a quantum process with a fixed probability per unit time, a nucleus that has survived undecayed for a million years is no more likely to decay in the next second than a freshly created nucleus of the same species."
  type: true-false
  answer: true
  explanation: "This is the memoryless (Markov) property of radioactive decay. λ is constant in time — the nucleus does not 'age,' accumulate internal stress, or become more likely to decay the longer it survives. This is what makes the decay law exponential: the future decay probability depends only on the current state (undecayed), not on history. It is also why the half-life is constant regardless of how many nuclei remain — each surviving nucleus has the same λ as it always did."

- question: "Why is the half-life constant regardless of how many nuclei remain, and what does this reveal about radioactive decay at the level of individual nuclei?"
  type: short-answer
  answer: "The half-life is constant because each nucleus decays independently with a fixed probability per unit time (λ), regardless of how many other nuclei surround it or how long it has already survived. Whether 10²³ nuclei remain or just 10, each one has the same probability of decaying in the next second. This reveals that radioactive decay is a memoryless quantum process: a nucleus carries no internal clock and does not become 'due' to decay. The exponential law N(t) = N₀e^(−λt) describes the average behavior of large ensembles — it cannot predict when any individual nucleus will decay, which is fundamentally random."
  explanation: "The constant half-life is a direct signature of the memoryless property. If nuclei 'aged,' the decay rate would change over time and the law would not be exponential. Applications depend on this constancy: carbon-14 dating works because the ratio of decayed to undecayed carbon follows a predictable exponential curve that does not shift based on the size of the sample or its history, only on the elapsed time."
```

## Explainer

You already know from your study of radioactive decay that unstable nuclei spontaneously transform, emitting particles or radiation. The key insight of the decay law is that every nucleus decays independently and randomly, with a fixed probability λ per unit time — the **decay constant**. Because probability is constant in time, a nucleus that has been sitting undecayed for a million years is no more likely to decay in the next second than a freshly created nucleus. This memoryless property is what makes radioactive decay fundamentally different from, say, a person aging.

From your study of exponential functions, you know that the equation dN/dt = −λN describes a quantity whose rate of change is proportional to itself. Solving this gives N(t) = N₀ e^(−λt): the number of remaining nuclei decays exponentially. The constant λ sets the timescale. Define the **half-life** T½ as the time for N to fall to N₀/2. Setting e^(−λT½) = 1/2 and taking the natural logarithm gives T½ = ln(2)/λ ≈ 0.693/λ. Crucially, T½ depends only on the nuclear species — not on temperature, pressure, chemical form, or how many nuclei remain. After each additional half-life, exactly half the remaining nuclei decay, regardless of how much time has already passed.

The activity A = λN is the number of decays per second (measured in becquerels, Bq). Since N decays exponentially, so does A: A(t) = A₀ e^(−λt) = A₀ · 2^(−t/T½). When solving problems without a calculator, counting in half-lives is often easier: after n half-lives, the fraction remaining is (1/2)^n. After 10 half-lives, less than 0.1% remains; nothing is truly gone in finite time, but the levels become negligible.

**Radiocarbon dating** illustrates these ideas concretely. Living organisms continuously exchange carbon with the atmosphere, maintaining a fixed ratio of ¹⁴C (T½ = 5,730 years) to ¹²C. When an organism dies, exchange stops and ¹⁴C begins decaying. Measuring the ¹⁴C/¹²C ratio in a sample and comparing it to the atmospheric standard gives the elapsed time t = (T½/ln2) × ln(A₀/A). The method works reliably for materials up to about 50,000 years old — beyond that, too little ¹⁴C remains to measure accurately. Longer-lived isotopes like ²³⁸U (T½ = 4.5 billion years) are used for geological timescales by the same logic.
