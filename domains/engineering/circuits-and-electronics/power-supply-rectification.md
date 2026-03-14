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
