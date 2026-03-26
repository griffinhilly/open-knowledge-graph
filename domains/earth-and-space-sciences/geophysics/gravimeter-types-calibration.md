---
id: gravimeter-types-calibration
title: Gravimeter Types, Calibration, and Field Operations
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: gravity-surveys-and-data-inversion
  type: hard
builds-toward:
- gravity-data-reduction
tags:
- gravimeter
- calibration
- survey
- instruments
stage: advanced
status: validated
---

# Gravimeter Types, Calibration, and Field Operations

## Core Idea
Relative gravimeters (spring-based) measure gravity differences with high precision; absolute gravimeters determine actual g. Drift, temperature sensitivity, and site calibration affect data quality. Base-station networks and careful instrument handling are essential.

## Questions

```yaml
- question: "A gravity survey uses a relative gravimeter and returns to a base station four times throughout the day in addition to visiting field stations. What is the primary purpose of these repeated base-station occupations?"
  type: multiple-choice
  options:
    - "To improve GPS positioning accuracy by averaging multiple readings at a well-surveyed location"
    - "To characterize and remove the instrument's drift — the slow creep of the spring that causes readings at a fixed location to change over time even when gravity does not"
    - "To verify that the base station has the highest gravity value in the survey area, ensuring it is a valid reference point"
    - "To average out random measurement noise by accumulating multiple readings at the highest-precision site"
  answer: 1
  explanation: "Spring-based relative gravimeters drift: the spring slowly relaxes (viscous creep), causing the instrument to read different values at the same station across hours even when gravity hasn't changed. Returning to the base station provides known time-stamped readings; the difference between successive base-station readings divided by the elapsed time gives the drift rate. This drift is then interpolated across the intervening time and subtracted from field readings. Without base-station reoccupations, drift would be indistinguishable from real geological gravity signals. Option D is a misconception: averaging multiple readings at one site reduces random noise, but that is not the purpose of cycling back to the base station throughout the day."

- question: "For which application would you prefer an absolute gravimeter over a relative gravimeter, despite the absolute instrument being heavier, slower, and more expensive?"
  type: multiple-choice
  options:
    - "A rapid regional survey requiring 200 stations covered in a week"
    - "Monitoring gravity changes at a volcano over many years to detect subsurface magma movement"
    - "Establishing a benchmark station with a well-known absolute gravity value to anchor a regional relative survey network"
    - "A marine gravity survey conducted from a moving ship"
  answer: 2
  explanation: "Absolute gravimeters determine the actual value of g from first principles (free-fall timing), need no external reference, and do not drift. This makes them ideal for establishing benchmark stations that anchor entire survey networks — all relative measurements in the region can be tied to the absolute value at the benchmark. For rapid dense surveys (option A), the slow measurement rate of absolute instruments (minutes per reading) makes them impractical; relative gravimeters cover many more stations per day. For volcanic monitoring over years (option B), both types are used, but if the monitoring network needs to be self-consistent across decades without drift accumulation, absolute gravimeters have advantages for periodic reoccupation."

- question: "A relative gravimeter can determine the absolute value of gravitational acceleration at a field station with the same precision it uses to measure gravity differences."
  type: true-false
  answer: false
  explanation: "A relative gravimeter measures gravity *differences* between stations — its output is a reading on a scale, not an absolute acceleration in m/s². To convert these differences to absolute values, the instrument must be tied to at least one station where absolute g is already known (a benchmark established by an absolute gravimeter). The precision of the difference measurement (microgals) is maintained in the final absolute values, but the absolute value itself cannot be determined without the external reference. A relative gravimeter operating entirely alone can only give you a self-consistent map of differences, not absolute gravity."

- question: "A sudden unexplained step offset ('tare') in repeated base-station readings from a relative gravimeter permanently corrupts most data collected after the tare occurs."
  type: true-false
  answer: false
  explanation: "A tare appears as a discrete step change in base-station readings at a specific time. If the survey returns to the base station frequently enough, the tare can be detected as an abrupt jump (rather than the smooth linear drift expected). Once detected, the data can be split into segments before and after the tare, and separate drift corrections can be applied to each segment. The tare's magnitude is estimated from the step size and subtracted from subsequent readings. Frequent base-station returns are precisely what makes tares detectable and correctable rather than permanently corrupting the data."

- question: "Explain why spring-based relative gravimeters drift, and how gravity survey design accounts for it."
  type: short-answer
  answer: "Spring-based gravimeters measure gravity differences by monitoring how much a test mass deforms a spring. The spring is subject to viscous creep — slow, time-dependent deformation — so the spring constant gradually changes, causing the instrument to read slightly different values at the same location over hours even when gravity is constant. This drift is typically close to linear over the timescale of a field day. Surveys account for it by returning the gravimeter to a base station at regular intervals throughout the day. The difference between successive base-station readings reveals how much the instrument drifted over that time interval. Assuming linear drift between reoccupations, the drift can be interpolated and subtracted from all field readings collected between those times. The result isolates real spatial variations in gravity from the instrument's temporal drift."
  explanation: "Drift correction is one of the most important processing steps in gravity surveying because the geological signals of interest are often only a few milligals — comparable in magnitude to instrument drift over a field day. The survey design (how often to return to base) is directly driven by the instrument's known drift rate."
```

## Explainer

From your background in gravity surveys and data inversion, you know that gravity anomalies — tiny variations in gravitational acceleration from place to place — encode information about subsurface density structure. But measuring those anomalies requires instruments sensitive enough to detect changes on the order of microgals (1 μGal = 10⁻⁸ m/s²), which is roughly one billionth of Earth's surface gravity. The instruments that achieve this precision fall into two categories with fundamentally different operating principles.

A **relative gravimeter** measures the *difference* in gravity between two stations rather than the absolute value of g. The most common type is the LaCoste-Romberg spring gravimeter, which uses a zero-length spring — a spring engineered so that its restoring force is proportional to its total length, not just its extension. A test mass hangs on this spring, and when gravity changes, the mass shifts. The operator adjusts a micrometer screw to return the beam to its null position, and the screw reading gives the gravity difference. Modern electronic versions (like the Scintrex CG-series) use electrostatic feedback to keep the mass stationary and record the required restoring force digitally, achieving precisions of a few microgals. The key limitation is **drift**: the spring slowly creeps over time, so readings at the same station will change over hours. Surveys therefore return to a **base station** repeatedly throughout the day, and the drift is removed by assuming it varies linearly (or polynomially) between base-station reoccupations.

An **absolute gravimeter** measures the actual value of g directly, typically by dropping a test mass in a vacuum and tracking its free-fall trajectory with a laser interferometer. The distance-time data are fit to the kinematic equation of free fall, yielding g to precisions better than 1 μGal. Because the measurement is self-contained — based on the definitions of length and time — it does not drift and needs no base-station corrections. However, absolute gravimeters are expensive, heavy, and slow (each measurement takes minutes of stacking drops), so they are used to establish benchmark stations that anchor relative survey networks rather than for dense field surveys.

Field operations for a gravity survey require meticulous attention to calibration and logistics. The gravimeter must be **calibrated** on a known gravity range — a set of stations with established absolute gravity values spanning the expected range of the survey — to convert instrument readings to milligals. Temperature control matters because spring stiffness is temperature-dependent; most modern instruments have internal thermostats, but rapid temperature swings can still introduce noise. Transport shocks can cause "tares" — sudden offsets in the spring's zero position — which show up as unexplained jumps in repeated base-station readings. A well-designed survey loops through base stations frequently enough that both drift and tares can be identified and corrected, ensuring that the subtle density signals you are after are not buried in instrumental artifacts.
