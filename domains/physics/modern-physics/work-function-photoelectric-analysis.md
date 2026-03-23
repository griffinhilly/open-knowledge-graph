---
id: work-function-photoelectric-analysis
title: Work Function and Photoelectric Energy Analysis
domain: physics
course: modern-physics
prerequisites:
- id: photoelectric-effect
  type: hard
- id: photon-model
  type: hard
builds-toward:
- stopping-potential-kinetic-energy
tags:
- quantum-mechanics
- photons
- photoelectric-effect
stage: advanced
status: validated
---

# Work Function and Photoelectric Energy Analysis

## Core Idea
The work function W is the minimum energy needed to remove an electron from a metal surface. When a photon of energy hf hits the surface, the maximum kinetic energy of the emitted electron is KE_max = hf − W. This relationship (Einstein's photoelectric equation) was central to proving the photon hypothesis; no amount of low-frequency light will cause emission, no matter how intense.

## How It's Best Learned
Plot stopping potential (and thus maximum kinetic energy) versus frequency; the slope gives h and the intercept gives W/e. Measure work functions for different metals and relate to periodic table properties.

## Common Misconceptions
Photon intensity affects the number of electrons emitted, not their maximum kinetic energy (energy comes from the photon, not the intensity). Electrons are emitted instantaneously (within femtoseconds), not built up over time.

## Questions

```yaml
- question: "A physicist shines light of frequency f = 0.8f₀ on a metal, where f₀ is the threshold frequency. The light intensity is extremely high — 1000 times the intensity used in previous experiments. What happens?"
  type: multiple-choice
  options:
    - "Electrons are emitted with low kinetic energy, since some intensity can compensate for insufficient frequency"
    - "No electrons are emitted, regardless of intensity, because each photon carries insufficient energy to overcome the work function"
    - "Electrons are emitted after a brief time delay while energy builds up from many photons"
    - "Electrons are emitted with kinetic energy proportional to the intensity"
  answer: 1
  explanation: "Each photon interacts with a single electron in an all-or-nothing transaction. A photon of frequency f carries energy hf; if hf < W (the work function), no individual photon can free an electron regardless of how many photons arrive. Intensity determines how many photons per second hit the surface — it increases the number of available transactions, but each transaction still involves only one photon of the same energy. There is no mechanism by which multiple low-energy photons pool their energy to free one electron (at least not at these intensities). This is precisely the result that refuted the classical wave theory."

- question: "A researcher doubles the intensity of light shining on a metal above its threshold frequency. What changes?"
  type: multiple-choice
  options:
    - "The maximum kinetic energy of emitted electrons doubles"
    - "The threshold frequency decreases"
    - "The photocurrent (number of electrons emitted per second) roughly doubles, but the maximum kinetic energy is unchanged"
    - "Both the photocurrent and the maximum kinetic energy increase proportionally"
  answer: 2
  explanation: "Intensity determines how many photons per second arrive at the surface, which determines how many electrons are freed per second — the photocurrent. But the energy each electron receives comes from a single photon (energy = hf), and the maximum kinetic energy is KE_max = hf − W. Doubling the intensity doubles the number of photons (and thus electrons) but does not change the energy per photon. Therefore KE_max is unchanged. Only changing the frequency of the light changes KE_max. This separation — intensity controls count, frequency controls energy — is the signature of light quantization."

- question: "The maximum kinetic energy of photoelectrons depends on the frequency of the incident light but not on its intensity."
  type: true-false
  answer: true
  explanation: "KE_max = hf − W. The work function W is a fixed property of the metal; the photon energy hf depends only on frequency f. Intensity tells you how many photons per second arrive, which sets the photocurrent, but each electron's maximum kinetic energy is set by a single photon interaction. No matter how many photons arrive, each electron can receive at most one photon's worth of energy (hf), so the maximum is determined solely by frequency. This is one of the clearest experimental signatures distinguishing the photon picture from the classical wave picture."

- question: "The classical wave theory of light predicts that increasing light intensity should eventually cause photoelectron emission even below the threshold frequency, given enough time for energy to accumulate."
  type: true-false
  answer: true
  explanation: "This is correct — and it is precisely what the classical wave theory predicted that turned out to be wrong. Classical wave theory treated light as a continuous wave delivering energy uniformly across the metal surface. Given enough time (or enough intensity), any surface electron should accumulate enough energy to escape, regardless of frequency. Experiments found the opposite: below the threshold frequency, no electrons are ever emitted no matter how long you wait or how bright the light is. This is the result that proved the classical picture was wrong and required Einstein's photon hypothesis."

- question: "Explain why Einstein's photoelectric equation KE_max = hf − W requires the photon hypothesis, and what observation it accounts for that the classical wave theory cannot explain."
  type: short-answer
  answer: "The equation assumes light comes in discrete packets (photons) each carrying energy hf, and that one photon interacts with one electron. The work function W is the minimum escape energy; whatever energy remains after paying this cost becomes kinetic energy, giving KE_max = hf − W. The classical wave theory cannot explain why there is a sharp threshold frequency below which no emission ever occurs regardless of intensity, nor why KE_max depends on frequency rather than intensity. Both observations follow naturally if light is quantized: a photon below threshold simply lacks the energy to free an electron, no matter how many arrive."
  explanation: "The stopping potential experiment (measuring V₀ vs. f) provides a direct, quantitative test: the linear relationship V₀ = (h/e)f − W/e gives Planck's constant as the slope. Millikan's precise measurements confirmed Einstein's equation and reluctantly validated the photon hypothesis. The conceptual point — that 'how many photons' and 'how much energy per photon' are independent quantities controlled by intensity and frequency respectively — remains one of the cleanest illustrations of quantization in introductory physics."
```

## Explainer

From your study of the photoelectric effect and the photon model, you know that light arrives in discrete packets — **photons** — each carrying energy E = hf, where h is Planck's constant and f is the frequency. When a photon strikes a metal surface, it interacts with a single electron in an all-or-nothing transaction: either the photon's energy is absorbed entirely or it isn't. This one-photon, one-electron picture is the starting point for understanding how much energy the emitted electron carries away.

Electrons inside a metal are bound — they require a minimum energy to escape the surface entirely. This minimum is the **work function** W, which is a property of the specific metal (typically 2–5 eV, varying by surface composition and crystal structure). Think of W as the depth of the energy well that the electron must climb out of. The metal's outermost electrons sit closest to the top of this well; inner electrons need more energy to escape. When a photon of energy hf arrives, it first pays the escape cost W. Whatever energy remains after that becomes the kinetic energy of the freed electron.

This gives Einstein's **photoelectric equation**: KE₍ₘₐₓ₎ = hf − W. The subscript "max" is important: most electrons don't escape from the outermost layer — they originate deeper in the metal and lose additional energy in collisions before reaching the surface. The maximum kinetic energy corresponds to electrons at the surface that escape with the minimum energy penalty. If hf < W, no electrons are emitted regardless of how intense the light is — you simply haven't provided enough energy per photon to overcome the barrier.

To measure KE₍ₘₐₓ₎ experimentally, physicists use a **stopping potential** V₀: an opposing voltage applied to decelerate the photoelectrons. The electrons just barely stopped by the voltage have converted all their kinetic energy to electric potential energy, so eV₀ = KE₍ₘₐₓ₎ = hf − W. If you plot V₀ against f for a series of different light frequencies, you get a straight line. The slope is h/e — this gives you Planck's constant — and the x-intercept is the threshold frequency f₀ = W/h below which no emission occurs. Millikan performed this experiment precisely, measuring h and confirming Einstein's equation to high accuracy.

The intensity distinction is the conceptual payoff. Intensity tells you how many photons per second arrive, not how much energy each carries. Doubling the intensity doubles the number of emitted electrons (the photocurrent), but each individual electron still gets exactly one photon's worth of energy, so KE₍ₘₐₓ₎ is unchanged. This is completely unlike the classical wave picture, where more intense waves would gradually build up energy in the surface electron until it could escape — the wave picture predicted a time delay and an intensity-dependent KE, neither of which is observed. The clean separation of "how many electrons" (intensity) from "how much energy each carries" (frequency) is one of the clearest signatures that light is quantized.


