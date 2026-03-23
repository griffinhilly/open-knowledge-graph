---
id: power-supply-rectification
title: Power Supply Rectification
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: diode-circuit-applications
  type: hard
- id: capacitor-inductor-energy-storage
  type: hard
tags:
- half-wave-rectifier
- full-wave-rectifier
- bridge-rectifier
- ripple-voltage
- filter-capacitor
- voltage-regulation
- power-supply
- peak-inverse-voltage
stage: formal-systems
status: draft
---

# Power Supply Rectification

## Core Idea
Power supply rectification converts AC mains voltage to DC for powering electronic circuits, proceeding through three stages: transformation (stepping voltage down via a transformer), rectification (converting AC to pulsating DC using diodes), and filtering (smoothing to near-constant DC using capacitors). A half-wave rectifier uses one diode to pass only positive half-cycles, wasting half the input power and producing large ripple at the line frequency. A full-wave bridge rectifier uses four diodes to redirect both half-cycles to the load with the same polarity, doubling the ripple frequency and halving the ripple for a given filter capacitor. The ripple voltage is approximated by V_ripple = I_load / (f_ripple * C), where f_ripple is the line frequency for half-wave and twice the line frequency for full-wave. Each diode must withstand the peak inverse voltage (PIV): V_peak for a bridge rectifier, 2*V_peak for a center-tapped full-wave rectifier. A voltage regulator (Zener diode or IC regulator like the 7805) follows the filter to provide a constant output voltage independent of load current and input voltage variations, reducing ripple by the regulator's line regulation and ripple rejection specifications.

## How It's Best Learned
Trace current paths through the bridge rectifier during each half-cycle, marking which diodes are forward-biased and which are reverse-biased. Calculate the required filter capacitor for a target ripple voltage and load current. Then design a complete supply: transformer ratio for the desired voltage, bridge rectifier with PIV-rated diodes, filter capacitor sized for acceptable ripple, and a voltage regulator to produce a clean output. Measure the waveform at each stage with an oscilloscope to see transformation, rectification, filtering, and regulation in action.

## Common Misconceptions
- Ignoring the diode voltage drops — each forward-biased diode drops approximately 0.7 V, and a bridge rectifier has two diodes in the current path, so the output peak is V_peak - 1.4 V, which matters significantly for low-voltage supplies.
- Assuming a larger filter capacitor is always better — while it reduces ripple, it also increases the peak diode current (since the capacitor charges only near the voltage peak in a narrow pulse), potentially exceeding the diode's surge current rating.
- Confusing PIV ratings between topologies — the PIV for a bridge rectifier diode is V_peak, but for a center-tapped full-wave rectifier it is 2*V_peak, a common source of design errors.

## Questions

```yaml
- question: "You replace a half-wave rectifier with a full-wave bridge rectifier, keeping the same filter capacitor, load resistance, and input voltage. What happens to the ripple voltage?"
  type: multiple-choice
  options:
    - "It doubles, because four diodes introduce more losses"
    - "It halves, because the ripple frequency doubles and the capacitor discharges for half as long between pulses"
    - "It stays the same, because the capacitor size and load are unchanged"
    - "It increases by a factor of four, because the bridge rectifier introduces two diode drops instead of one"
  answer: 1
  explanation: "The ripple formula V_ripple ≈ I_load / (f_ripple × C) shows that ripple is inversely proportional to ripple frequency. A half-wave rectifier produces pulses at the line frequency (60 Hz); a full-wave bridge uses both half-cycles, doubling the ripple frequency (120 Hz). With twice the frequency, the capacitor discharges for only half as long between charge pulses, cutting ripple in half. The number of diodes affects only the output peak voltage (−1.4 V for the bridge), not the ripple frequency."

- question: "In a full-wave bridge rectifier, the input peak voltage is 20 V. What is the minimum peak inverse voltage (PIV) rating required for each diode?"
  type: multiple-choice
  options:
    - "10 V — the two conducting diodes each share the peak voltage"
    - "20 V — each reverse-biased diode must withstand the full input peak"
    - "40 V — the bridge doubles the PIV compared to a half-wave rectifier"
    - "18.6 V — the PIV equals V_peak minus the two conducting diode drops"
  answer: 1
  explanation: "In a bridge rectifier, when two diodes are conducting, the two reverse-biased diodes each see approximately V_peak across them (with a small correction for conducting diode drops). So the PIV rating must be at least V_peak = 20 V. This is often confused with the center-tapped full-wave rectifier topology, where each diode must withstand 2×V_peak = 40 V — a common design error when mixing topologies. The bridge rectifier's V_peak PIV requirement is actually one of its advantages over the center-tapped design."

- question: "Using a larger filter capacitor always reduces ripple voltage with no engineering drawbacks."
  type: true-false
  answer: false
  explanation: "A larger capacitor does reduce ripple (V_ripple ≈ I_load / f × C), but it creates a significant drawback: the capacitor charges only during the brief interval when the rectified voltage exceeds the capacitor voltage (near the peak). A larger capacitor requires a larger charge per cycle delivered in a narrower pulse, producing higher peak diode currents. If the peak current exceeds the diode's surge current rating, the diode can fail. Large capacitors also cause higher inrush current at turn-on. Diode selection and capacitor sizing must be designed together."

- question: "In a full-wave bridge rectifier, the maximum output voltage (before filtering) equals the transformer secondary peak voltage minus approximately 1.4 V due to two forward-biased diode drops in the current path."
  type: true-false
  answer: true
  explanation: "In a bridge rectifier, current always flows through exactly two diodes simultaneously: one on the positive rail and one on the negative rail (or their counterparts during the other half-cycle). Each silicon diode drops approximately 0.7 V when forward-biased, so the combined drop is 2 × 0.7 V = 1.4 V. For a 20 V peak secondary, the output peak is approximately 18.6 V. This 1.4 V loss is negligible for a 100 V supply but significant for a 5 V or 3.3 V supply — a key design consideration for low-voltage applications."

- question: "Explain why the ripple voltage formula V_ripple ≈ I_load / (f_ripple × C) predicts that a full-wave rectifier produces half the ripple of a half-wave rectifier when the capacitor and load are identical."
  type: short-answer
  answer: "The formula shows ripple is inversely proportional to ripple frequency. A half-wave rectifier passes only the positive half-cycles, producing one pulse per AC cycle (f_ripple = line frequency, e.g., 60 Hz). The capacitor must sustain the load for a full cycle between pulses. A full-wave bridge rectifier redirects both half-cycles, producing two pulses per AC cycle (f_ripple = 2 × line frequency = 120 Hz). The capacitor only discharges for half a cycle between pulses, so it sags half as much. Doubling frequency halves ripple with no change to C or I_load."
  explanation: "Physically: the capacitor discharges through the load between rectifier pulses. The longer the gap between pulses, the more it discharges. Full-wave halves this gap, halving the discharge and thus halving the ripple. This is why full-wave rectification is strongly preferred in practice — you get half the ripple for the same cost in capacitance, or equivalently, the same ripple with half the capacitor."
```

## Explainer

From your study of diode circuit applications, you know the diode's essential property: it allows current to flow in one direction (forward-biased, approximately 0.7 V drop) and blocks it in the other direction (reverse-biased). From capacitor and inductor energy storage, you know that a capacitor stores charge and resists rapid voltage changes — it acts as a reservoir. Power supply rectification combines these two concepts to solve a fundamental problem: AC power from the wall is a sinusoid that swings positive and negative at 50 or 60 Hz, but nearly all electronic circuits require a stable, positive DC voltage. The conversion proceeds through three stages: transformation, rectification, and filtering.

The **transformation** stage uses a transformer to step the mains voltage (120 V or 240 V AC) down to a lower AC voltage appropriate for the target DC output. The **rectification** stage is pure diode work. A **half-wave rectifier** uses a single diode: during positive half-cycles, the diode conducts and current reaches the load; during negative half-cycles, the diode blocks and no current flows. The output is a series of positive pulses at the line frequency, with half the input waveform discarded. A **full-wave bridge rectifier** uses four diodes arranged so that during both half-cycles, current reaches the load with the same polarity — the negative half-cycle is "flipped" rather than blocked. Both half-cycles are used, the ripple frequency doubles to 2× line frequency, and energy efficiency improves significantly. The cost: two diodes are always in the current path, so the output peak voltage is V_peak − 1.4 V (two 0.7 V drops), which matters at low supply voltages.

After rectification, the output is still pulsating — it surges and sags at the ripple frequency. The **filtering** stage places a large capacitor in parallel with the load. When the rectified voltage rises above the capacitor's current charge, the diodes conduct and the capacitor charges toward the peak. When the rectified voltage falls below the capacitor voltage between pulses, the diodes are reverse-biased and the capacitor discharges slowly through the load, sustaining the output. The resulting **ripple voltage** — the peak-to-peak swing between charge and discharge — is approximated by V_ripple ≈ I_load / (f_ripple × C). To halve the ripple, double the capacitor or double the ripple frequency; this is why full-wave rectification (which doubles f_ripple compared to half-wave) is strongly preferred for a given filter capacitor size.

A critical constraint in diode selection is the **peak inverse voltage** (PIV): the reverse voltage each diode must withstand when it is blocking. In a bridge rectifier, the two reverse-biased diodes see approximately V_peak across them, setting the minimum PIV rating. In a center-tapped full-wave rectifier topology, the PIV is 2 × V_peak — a frequently overlooked difference that has caused circuit failures when diodes specified for one topology were substituted for another. Diode selection also requires checking the surge current rating, since the filter capacitor charges in narrow pulses near the voltage peak, producing high peak currents even when the average current is modest.

Even with a filter capacitor, the output voltage drifts with load current and input voltage variations — unacceptable for precision circuits. A **voltage regulator** provides the final stage. A Zener diode regulator exploits the Zener's reverse breakdown characteristic to clamp the output at a fixed voltage, absorbing variation in supply current. IC regulators like the 7805 use internal feedback to maintain a precise output (5 V in this case) over a wide range of input voltages and load currents, with very high **ripple rejection** (often 70 dB or more — a factor of 3,000 in voltage). Together, the four-stage chain — transform, rectify, filter, regulate — converts rough sinusoidal mains power into the stable, quiet DC that digital logic and analog circuits require to function reliably.
