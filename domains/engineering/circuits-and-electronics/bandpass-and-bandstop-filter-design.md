---
id: bandpass-and-bandstop-filter-design
title: Bandpass and Bandstop Filter Design
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: first-order-passive-filters
  type: hard
- id: second-order-passive-filters
  type: hard
builds-toward:
- filter-selection-and-practical-applications
tags:
- bandpass
- bandstop
- notch
- cascade-filters
stage: formal-systems
status: draft
---

# Bandpass and Bandstop Filter Design

## Core Idea
Bandpass filters allow frequencies within a passband while rejecting others; the passband width and center frequency are set by component values. Bandstop (notch) filters do the opposite. Practical designs cascade first-order and second-order stages to achieve the desired attenuation slope and selectivity. The resonance characteristics of RLC circuits are exploited to create sharp transitions.

## Questions

```yaml
- question: "An engineer cascades a low-pass filter (10 kHz cutoff) in series with a high-pass filter (1 kHz cutoff). What is the resulting filter characteristic?"
  type: multiple-choice
  options:
    - "A bandstop response — frequencies between 1 and 10 kHz are blocked"
    - "A bandpass response — only frequencies between 1 and 10 kHz pass both stages"
    - "A low-pass response — the high-pass stage is dominated by the low-pass stage"
    - "No signal passes — the two filters cancel each other out"
  answer: 1
  explanation: "In series (cascade), a signal must pass both filters to reach the output. The low-pass stage passes everything below 10 kHz; the high-pass stage passes everything above 1 kHz. Only frequencies satisfying both conditions — between 1 kHz and 10 kHz — make it through both stages. This is a bandpass filter. For this to work, the low-pass cutoff must be above the high-pass cutoff; if they were reversed, no frequency would satisfy both conditions simultaneously."

- question: "An RLC bandpass filter is redesigned with resistance reduced by a factor of 10 while L and C remain unchanged. How does the filter's frequency response change?"
  type: multiple-choice
  options:
    - "The center frequency ω₀ decreases because lower resistance means lower energy dissipation"
    - "The bandwidth increases because lower resistance means less signal attenuation across the passband"
    - "The Q factor increases and the passband narrows, producing a more selective filter"
    - "The filter transitions from a bandpass to a bandstop response"
  answer: 2
  explanation: "The quality factor Q = ω₀L/R (for a series RLC). Reducing R by 10× increases Q by 10×. Since bandwidth BW = ω₀/Q, higher Q means narrower bandwidth — the filter becomes more selective, passing a tighter range of frequencies around the center frequency ω₀. Center frequency ω₀ = 1/√(LC) is unaffected by R. Option B has it backwards: lower resistance reduces losses but narrows, not widens, the passband — because the resonant peak becomes sharper."

- question: "To build a bandstop (notch) filter from separate low-pass and high-pass filter stages, the two stages are connected in series (one after the other)."
  type: true-false
  answer: false
  explanation: "For a bandstop filter, the low-pass and high-pass stages are connected in parallel: both receive the same input, and their outputs are summed. Signals low enough to pass the low-pass stage, or high enough to pass the high-pass stage, appear at the output. Signals in the notch band fail both tests and are rejected. Series connection produces the opposite behavior (bandpass), because a signal must satisfy both conditions simultaneously. Parallel lets either condition suffice."

- question: "Adding a second identical second-order stage in cascade with an existing second-order bandpass filter increases the roll-off rate from 40 dB/decade to 80 dB/decade beyond the cutoff."
  type: true-false
  answer: true
  explanation: "Each second-order filter section contributes 2 poles, adding 40 dB/decade of roll-off (20 dB/decade per pole). Cascading two second-order sections gives 4 poles and 80 dB/decade of attenuation slope. This is why higher-order filters (Butterworth, Chebyshev, elliptic) are built by cascading first- and second-order stages: each stage stacks attenuation, giving sharper transitions between passband and stopband."

- question: "When cascading a low-pass and a high-pass filter to form a bandpass filter, why must the low-pass cutoff frequency be set higher than the high-pass cutoff frequency?"
  type: short-answer
  answer: "In a series cascade, a signal must pass through both filters to reach the output. The bandpass region is the intersection of what each filter allows: frequencies below the low-pass cutoff AND above the high-pass cutoff. If the low-pass cutoff is lower than the high-pass cutoff, these two regions do not overlap — no frequency satisfies both conditions simultaneously, and no signal passes. The passband only exists when the low-pass cutoff exceeds the high-pass cutoff, creating an overlapping region between them."
  explanation: "This is the fundamental design constraint for cascaded bandpass filters. The bandwidth is (f_LP_cutoff − f_HP_cutoff), so the separation between the two cutoffs directly sets the passband width. Narrowing this gap narrows the passband; swapping the relationship (LP cutoff < HP cutoff) eliminates the passband entirely."
```

## Explainer

You already know that a **low-pass filter** passes low frequencies and blocks high ones, while a **high-pass filter** does the opposite. A **bandpass filter** targets a specific frequency range — passing everything in between and rejecting both low and high extremes. The most intuitive way to build one is to cascade a low-pass and a high-pass filter in series: the low-pass sets the upper edge of the passband, the high-pass sets the lower edge, and only frequencies satisfying both conditions get through. For this to work, the low-pass cutoff must be above the high-pass cutoff; otherwise the regions overlap and nothing passes.

The **center frequency** ω₀ and **bandwidth** BW are the key design parameters. For an RLC bandpass filter, ω₀ = 1/√(LC) — the resonant frequency at which the reactive components cancel, leaving only the resistive impedance. At resonance, the circuit passes signals with minimal attenuation. As you move away from ω₀ in either direction, the impedance imbalance grows and the output falls. The bandwidth is set by the resistance: lower R → higher Q → narrower bandwidth around ω₀. This is why you need your knowledge of second-order filter behavior: the sharpness of the bandpass response is entirely determined by the Q factor of the resonant circuit.

A **bandstop** (or **notch**) filter is the complement: it rejects a specific frequency range and passes everything else. The easiest conceptual construction is to place a low-pass and high-pass filter in *parallel* rather than series — signals that are low enough to pass the low-pass stage, or high enough to pass the high-pass stage, combine at the output, while the target band falls through the gap. RLC circuits can also be configured directly as notch filters, exploiting the same resonance that creates a bandpass peak but routing the resonant impedance to ground instead of the load.

In practice, real designs stack multiple first- and second-order stages to achieve steeper roll-off slopes. Each additional pole adds 20 dB/decade of attenuation beyond the cutoff. A **Butterworth** design maximizes flatness in the passband at the cost of gradual roll-off; a **Chebyshev** design allows ripple in the passband to achieve a sharper transition; an **elliptic** design permits ripple in both passband and stopband for the sharpest possible transition. Selecting among these is an engineering tradeoff: audio applications tolerate Butterworth's gradual roll-off, while interference rejection in communications often demands elliptic steepness.
