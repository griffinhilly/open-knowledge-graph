---
id: electromagnetic-induction-methods
title: Electromagnetic Induction and Transient Methods
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: potential-field-methods-gravity-magnetics
  type: soft
- id: electromagnetic-waves
  type: soft
builds-toward:
- magnetotelluric-methods-em-induction
tags:
- electromagnetic
- induction
- tem
- methods
stage: advanced
status: draft
---

# Electromagnetic Induction and Transient Methods

## Core Idea
Time-domain (TEM) and frequency-domain electromagnetic methods measure electrical conductivity through induced currents and transient responses. Data are inverted for 1D/2D/3D conductivity-depth models.

## Questions

```yaml
- question: "In a TEM survey over a target zone containing a thick, highly conductive clay layer at depth, how would the transient decay curve differ from a survey over a resistive (low-conductivity) sand layer at the same depth?"
  type: multiple-choice
  options:
    - "The conductive clay produces a faster, sharper decay because induced currents dissipate quickly"
    - "The conductive clay produces a slower, more sustained decay at late times because induced currents persist longer in good conductors"
    - "The two curves would be identical because depth controls the late-time signal, not conductivity"
    - "The conductive clay produces a stronger early-time signal but is undetectable at late times"
  answer: 1
  explanation: "In good conductors, induced eddy currents are sustained longer before they decay (higher conductivity means lower resistivity, so currents meet less resistance). The result is a slow, persistent late-time decay. A resistive layer allows currents to dissipate quickly, producing a rapid, steep decay. The decay shape — not just the amplitude — encodes the conductivity-depth profile: a conductive target appears as a prolonged tail on the transient, which is precisely how ore bodies and saline aquifers are detected in TEM surveys."

- question: "A geophysicist wants to image a target at 200 m depth using frequency-domain EM. Compared to a 10 kHz source, a 100 Hz source would provide..."
  type: multiple-choice
  options:
    - "Shallower penetration, because lower-frequency signals carry less energy"
    - "Greater penetration depth, because skin depth increases as frequency decreases"
    - "The same penetration depth, because amplitude determines depth, not frequency"
    - "Greater penetration only if the subsurface is highly conductive"
  answer: 1
  explanation: "Skin depth δ ∝ 1/√(f × σ), where f is frequency and σ is conductivity. As frequency decreases, skin depth increases — the field attenuates more slowly with depth, reaching deeper targets. This inverse relationship between frequency and penetration depth is the core principle of frequency-domain EM depth sounding. The misconception that higher frequency means more energy and therefore deeper penetration confuses seismic (where wavelength governs) with EM induction (where diffusion governs). Lower frequency is the correct choice for deeper imaging."

- question: "In time-domain electromagnetic methods, late-time signals reflect deeper subsurface structure because the eddy currents induced at shut-off propagate downward into the earth over time."
  type: true-false
  answer: true
  explanation: "This is the smoke-ring diffusion principle. When the transmitter current is abruptly cut off, the induced eddy currents initially concentrate near the surface. Over time, these current loops diffuse downward into the earth at a rate that depends on conductivity. Early-time measurements (just after shut-off) therefore sample shallow structure, while late-time measurements sample deeper structure. The spatial evolution of the eddy current system with time is why the transient decay curve encodes the full conductivity-depth profile rather than just a single average value."

- question: "Higher frequency signals penetrate deeper in frequency-domain EM surveys because they carry more electromagnetic energy."
  type: true-false
  answer: false
  explanation: "The opposite is true. Skin depth δ = √(2/(ωμσ)), where ω = 2πf. Higher frequency means larger ω and smaller skin depth — the field decays more rapidly with depth. Deeper investigation requires lower frequencies. The confusion likely arises from other wave-based methods (e.g., seismic or radar) where energy or wavelength arguments work differently. In EM induction, penetration is controlled by diffusion physics, not wave energy, and the fundamental tradeoff is that shallow resolution and deep investigation pull in opposite directions via frequency."

- question: "In time-domain EM, explain why the shape of the transient decay curve — not just its peak amplitude — carries information about subsurface conductivity structure."
  type: short-answer
  answer: "The shape encodes how conductivity changes with depth. The early part of the decay reflects shallow structure (where the eddy currents initially concentrate), while the late-time tail reflects deeper structure (where the currents have diffused to). A highly conductive layer at depth produces a long-lived tail because currents persist longer in good conductors; a resistive basement produces rapid decay. The rate of decay at different times therefore acts as a depth-resolved conductivity profile. Amplitude alone tells you something exists, but the time evolution of the decay is what allows inversion for a layered conductivity model."
  explanation: "This is the key principle distinguishing EM induction from simpler geophysical measurements. Because eddy currents diffuse as a function of time, the time axis of the decay corresponds roughly to depth — the temporal structure maps onto spatial structure through the diffusion relationship depth ∝ √(time/conductivity). Multiple time windows can therefore sample multiple depth intervals with a single transmitted pulse, which is why TEM is both efficient and depth-sensitive."
```

## Explainer

From your background in electromagnetic waves, you know that a changing magnetic field induces an electric field, and that electric field can drive currents in any conductive material. Electromagnetic induction methods in geophysics exploit exactly this principle: they use a controlled or natural electromagnetic source to induce electrical currents in the subsurface, then measure the resulting secondary fields to map how **electrical conductivity** varies with depth. This gives access to a physical property — conductivity — that is exquisitely sensitive to fluid content, salinity, temperature, and mineralogy, making EM methods complementary to the density and magnetization contrasts you studied in potential field methods.

In **time-domain electromagnetic (TEM)** methods, a transmitter loop carries a steady current that is abruptly shut off. The sudden change in magnetic flux induces eddy currents in the ground that initially concentrate near the surface, then diffuse downward over time — a phenomenon called **smoke-ring diffusion**. The receiver measures how the secondary magnetic field decays after the transmitter switches off. Early-time signals reflect shallow conductivity structure; late-time signals, which arrive from deeper-propagating currents, reveal conductivity at greater depths. The decay curve's shape encodes the conductivity-depth profile: a highly conductive layer produces a slow, sustained decay because induced currents persist longer in good conductors.

**Frequency-domain methods** take a different approach. Instead of pulsing and watching the decay, they transmit a continuous sinusoidal signal and measure the amplitude and phase of the secondary field relative to the transmitted primary field. Low frequencies penetrate deeper because the **skin depth** — the distance over which the field amplitude decays to 1/e — increases as frequency decreases (skin depth ∝ 1/√(frequency × conductivity)). By sweeping through a range of frequencies, you effectively sample different depths. The ratio of secondary to primary field, expressed as apparent conductivity or mutual impedance, can be inverted for a layered conductivity model.

Both approaches ultimately produce a model of how conductivity varies with depth, but they have different practical strengths. TEM is excellent for detecting conductive targets (ore bodies, saline aquifers, clay layers) because the late-time response is dominated by the most conductive features. Frequency-domain systems are often more portable and provide continuous spatial coverage, making them ideal for mapping lateral variations in shallow conductivity — groundwater contamination plumes, for instance. In either case, the measured data are **inverted** using forward models that compute the expected response for a given conductivity structure, iteratively adjusting the model until it fits the observations. The non-uniqueness of this inverse problem — different conductivity distributions can produce similar responses — is managed through regularization, prior constraints, and, increasingly, joint inversion with other geophysical datasets.
