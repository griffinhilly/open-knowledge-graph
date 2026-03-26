---
id: sensors-and-feedback
title: Sensors and Feedback in Engineering Systems
domain: engineering
course: engineering-principles
prerequisites:
- id: circuit-design-basics
  type: hard
- id: digital-vs-analog-signals
  type: hard
- id: one-step-equations
  type: soft
builds-toward:
- control-systems-intro-engineering
- feedback-control-fundamentals
tags:
- sensors
- feedback
- measurement
- closed-loop
- transducers
stage: abstract-reasoning
status: validated
---
# Sensors and Feedback in Engineering Systems

## Core Idea
Sensors convert physical quantities (temperature, pressure, light, motion, force) into electrical signals that engineering systems can measure and respond to. Feedback is the process of using sensor measurements to adjust a system's behavior -- comparing the actual output to the desired output and making corrections. A thermostat is a classic feedback system: a temperature sensor measures the room temperature, compares it to the set point, and turns the heater on or off to reduce the difference. Without sensors and feedback, engineering systems operate "blindly," unable to adapt to changing conditions or correct errors.

## How It's Best Learned
Build a simple feedback system: a light sensor (photoresistor) connected to an LED brightness controller. As ambient light increases, the LED should get brighter to compensate (or dimmer to save energy, depending on the design goal). Students experience the feedback loop directly: sensor reads environment, controller compares to target, actuator adjusts output. Then disrupt the system (cover the sensor, change the target) and observe how it responds.

## Common Misconceptions
- Sensors measure things perfectly. (All sensors have limitations: accuracy (how close to the true value), precision (how repeatable), range (minimum and maximum values), response time (how quickly they react), and resolution (the smallest change they can detect). Engineers must understand these limitations when designing systems.)
- Feedback always makes systems better. (Poorly designed feedback can make systems worse -- it can cause oscillation (hunting back and forth), overshoot (overshooting the target before settling), or instability (the system spirals out of control). Feedback design requires careful tuning.)
- More sensors are always better. (Additional sensors add cost, complexity, and potential failure points. Engineers use the minimum number of sensors needed to achieve adequate feedback for the system's requirements.)
- Feedback happens only in electronic systems. (Mechanical governors on steam engines, float valves in toilets, and the human body's temperature regulation are all feedback systems. Feedback is a universal engineering and biological principle.)

## Questions

```yaml
- question: "A robot arm uses a position sensor to verify it reached the correct location after each move. What type of system is this?"
  type: multiple-choice
  options: ["Open-loop system", "Closed-loop (feedback) system", "Analog system", "Binary system"]
  answer: 1
  explanation: "The system measures its actual output (arm position) and compares it to the desired output (target position). If there is a difference, the controller adjusts. This measure-compare-adjust cycle is the definition of a closed-loop feedback system."

- question: "An open-loop system (no feedback) typically performs worse than a closed-loop system."
  type: true-false
  answer: false
  explanation: "Open-loop systems can be adequate when the process is highly predictable and disturbances are minimal. A toaster uses an open-loop timer -- it heats for a set duration regardless of the toast's actual color. For simple, predictable tasks, open-loop is cheaper and simpler. Feedback adds value when conditions vary or precision is critical."

- question: "A greenhouse heating system uses a temperature sensor but the heater runs at full power whenever the temperature is below the set point. What problem might this cause?"
  type: short-answer
  answer: "The system will overshoot the target temperature because the heater does not reduce its output as the temperature approaches the set point. The temperature will rise past the target, then the heater turns off, the temperature drops below the target, the heater turns on again, and the cycle repeats. This oscillation (called 'bang-bang' or on-off control) wastes energy and never achieves a stable temperature."
  explanation: "On-off control is the simplest form of feedback but causes cycling around the set point. More sophisticated control (like proportional control, which reduces heater power as the temperature approaches the target) can achieve smoother, more stable temperature regulation."
```

## Explainer
Imagine driving a car with your eyes closed. You set the steering wheel straight ahead and press the gas pedal, hoping you stay in your lane. Of course, this is absurd -- without visual feedback, you would crash almost immediately. Your eyes are **sensors** (measuring the car's position relative to the lane), and your hands on the steering wheel are the **actuator** (correcting deviations). The entire system works because of **feedback**: continuously measuring the actual state, comparing it to the desired state, and adjusting.

**Sensors** are the eyes and ears of engineering systems. A temperature sensor (thermistor, thermocouple, or RTD) converts heat into an electrical signal. A pressure sensor converts mechanical pressure into voltage. A light sensor (photodiode or photoresistor) converts brightness into a measurable signal. An accelerometer detects motion and vibration. Each sensor translates a physical phenomenon into an electrical signal that a controller can process.

Every sensor has limitations that engineers must understand. **Accuracy** is how close the reading is to the true value -- a cheap thermometer might be accurate to plus or minus 2 degrees. **Precision** is how repeatable readings are -- the same temperature measured ten times should give ten similar readings. **Range** defines the minimum and maximum the sensor can detect. **Response time** is how quickly the sensor reacts to changes. Choosing the right sensor means matching these characteristics to the application's requirements.

**Feedback** connects sensors to action. In a **closed-loop** system, the sensor measurement is continuously compared to a **set point** (the desired value), and the difference (called the **error**) drives a corrective action. If the room is too cold (error is negative), turn on the heater. If it is too warm (error is positive), turn off the heater. The heater's action changes the temperature, which the sensor detects, which changes the error, which changes the heater's action -- this circular flow of information is the **feedback loop**.

The alternative is an **open-loop** system, where the output is not measured or compared to anything. A microwave oven runs for a set time at a set power with no feedback about the food's actual temperature. This works adequately because the process is predictable and the consequences of imprecision are low (slightly overcooked leftovers). But for applications where precision matters -- industrial manufacturing, climate control, autonomous vehicles, medical devices -- feedback is essential. The ability to measure, compare, and correct is what transforms a blind process into an intelligent one.
