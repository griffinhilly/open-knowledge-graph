---
id: voltage-clamp-recording
title: 'Voltage Clamp: Measuring Ionic Currents in Isolation'
domain: biology
course: neuroscience
prerequisites:
- id: action-potential-repolarization
  type: hard
- id: action-potential-initiation
  type: soft
builds-toward:
- absolute-refractory-period
- short-term-plasticity-presynaptic
tags:
- electrophysiology
- measurement-technique
- quantitative-methods
stage: advanced
status: draft
---

# Voltage Clamp: Measuring Ionic Currents in Isolation

## Core Idea
The voltage clamp uses feedback amplification to hold membrane potential constant at a chosen level while measuring the current required to maintain that potential. This isolates and reveals ionic currents (Na+, K+, Ca2+) that would normally sum together, allowing direct measurement of channel properties as functions of voltage and time.

## Explainer

From your study of action potentials, you know that depolarization opens voltage-gated sodium channels, which drives further depolarization in a positive feedback loop, followed by potassium channel opening during repolarization. The problem for anyone trying to study these channels individually is that under normal conditions, all of this happens simultaneously and explosively — the membrane potential changes so fast that sodium and potassium currents overlap in time. You cannot easily ask "how much sodium current flows at −20 mV?" because the membrane does not stay at −20 mV long enough to measure. The **voltage clamp** solves this problem by using an electronic feedback circuit to force the membrane to stay at whatever potential the experimenter chooses.

The basic setup works like this: two electrodes are inserted into the cell. One measures the actual membrane potential, and a **feedback amplifier** compares this measurement to the experimenter's chosen **command voltage**. If the membrane potential deviates from the command — say, because sodium channels have opened and positive ions are rushing in — the amplifier instantly injects an equal and opposite current to push the voltage back to the command level. The key insight is that this injected current must be exactly equal in magnitude (and opposite in sign) to the ionic current flowing through the channels. By measuring the current the amplifier must inject, you are directly measuring the ionic current at that specific voltage.

This technique is what allowed Hodgkin and Huxley to dissect the action potential into its component parts. By stepping the membrane to different command voltages and recording the resulting currents, they could map out how sodium and potassium conductances depend on voltage and time. At a command voltage of −20 mV, for instance, they observed a fast inward current (sodium) followed by a slower outward current (potassium). By adding pharmacological blockers — **tetrodotoxin** to block sodium channels or **tetraethylammonium** to block potassium channels — they could isolate each current in turn and characterize its voltage dependence and kinetics independently.

The voltage clamp also reveals properties that are invisible during a normal action potential. For example, **sodium channel inactivation** — the process by which channels close despite sustained depolarization — was discovered because the voltage clamp could hold the membrane depolarized long enough to watch the inward current decline to zero even though the driving force for sodium entry remained. Without clamping the voltage, repolarization would have occurred too quickly to observe this process. The technique thus transformed electrophysiology from a descriptive science into a quantitative one, enabling researchers to write mathematical equations describing how each channel type behaves as a function of voltage and time.
