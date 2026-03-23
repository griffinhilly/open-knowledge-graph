---
id: sensors-basics
title: Sensors Basics
domain: engineering
course: design-and-build
prerequisites:
- id: switches-and-control
  type: hard
- id: building-a-simple-circuit
  type: hard
builds-toward:
- technology-in-everyday-life
- adc-dac-fundamentals
tags:
- sensors
- circuits
- input
- engineering
- technology
stage: concrete-operations
status: draft
---
# Sensors Basics

## Core Idea
A sensor is a device that detects something in the environment — light, temperature, sound, motion, pressure, or proximity — and converts it into an electrical signal that a circuit can use. Sensors are like a circuit's eyes, ears, and fingertips: they let electronic devices respond to the world around them. A night light uses a light sensor to detect darkness. A thermostat uses a temperature sensor to detect cold. A motion-sensor light uses a motion detector to detect movement. Engineers use sensors to make devices "smart" — able to react automatically to changing conditions instead of requiring a human to flip a switch.

## How It's Best Learned
Build circuits that respond to the environment. Start with a light-dependent resistor (LDR): wire it into a circuit with an LED, and the LED brightness changes when you cover the LDR with your hand (blocking light). Then try a tilt switch — a small tube with a metal ball that completes a circuit when tilted one way and breaks it when tilted the other. Have students brainstorm everyday devices that use sensors (automatic doors, phone screens that dim, car backup sensors) and identify what each sensor detects and how the device responds.

## Common Misconceptions
- Sensors are complicated computer parts. (Many sensors are simple components — a light sensor is just a resistor that changes with light. A tilt switch is a ball in a tube. Sensors can be very simple and still very useful.)
- Sensors make decisions. (Sensors only detect and report. The circuit or computer connected to the sensor makes the decision about what to do with the information.)
- Every sensor needs a computer to work. (Simple sensor circuits work without computers. A night light with a light sensor and a relay can turn on automatically with no computer involved.)

## Questions

```yaml
- question: "What does a sensor do in a circuit?"
  type: multiple-choice
  options: ["It stores energy like a battery", "It detects something in the environment and converts it into an electrical signal", "It makes the circuit faster", "It controls the voltage of the battery"]
  answer: 1
  explanation: "A sensor is an input device. It detects a physical quantity — light, heat, motion, sound, pressure — and converts that detection into an electrical change (more or less current, higher or lower voltage) that the rest of the circuit can respond to."

- question: "A sensor detects something in the environment AND decides what to do about it."
  type: true-false
  answer: false
  explanation: "A sensor only detects — it is an input device. It reports what it senses as an electrical signal. The decision about what to do with that information is made by the rest of the circuit (or a computer). A temperature sensor reports that it is cold; the thermostat circuit decides to turn on the heater."

- question: "Name an everyday device that uses a sensor, and explain what the sensor detects."
  type: short-answer
  answer: "An automatic door at a store uses a motion sensor that detects when a person approaches. When it senses motion, the circuit activates the motor that opens the door."
  explanation: "Other examples: a phone screen that dims in bright light (light sensor), a thermostat that turns on heat when it is cold (temperature sensor), a car backup alarm that beeps when close to an object (distance sensor), a smoke detector (particle sensor). In each case, the sensor detects a change, and the circuit responds."
```

## Explainer
You have built circuits with switches — devices that let **you** control whether current flows. But what if the circuit could control itself? What if it could detect light, or temperature, or motion, and respond automatically? That is what **sensors** do.

A sensor is a component that detects something in the physical world and converts it into an **electrical signal**. Think of it as a translator: the sensor experiences light, heat, sound, or pressure and translates that experience into a change in current or voltage that the circuit can understand and act on.

One of the simplest sensors is a **light-dependent resistor (LDR)**. In the dark, the LDR has high resistance and barely lets current through. In bright light, its resistance drops and current flows freely. Wire an LDR into a circuit with an LED, and you have a device that automatically adjusts brightness based on ambient light — dim in daylight, bright in darkness. This is the same principle behind the night lights that turn on automatically when a room gets dark.

A **tilt switch** is even simpler — a small tube with a metal ball inside. When the tube is upright, the ball rests on two contacts at the bottom, completing the circuit. When the tube is tilted, the ball rolls away from the contacts, breaking the circuit. This simple sensor can detect orientation and is used in devices like game controllers and construction levels.

Here is the important distinction: **sensors do not make decisions**. A temperature sensor reports "it is 60 degrees" as an electrical signal, but it does not decide to turn on the heater — the thermostat circuit makes that decision. A motion sensor reports "something moved," but the automatic door circuit decides to open the motor. The sensor is the **input** (what does the world look like?), and the circuit is the **processor** (what should we do about it?). This separation of detection and decision is a fundamental engineering concept that scales all the way up to complex systems like self-driving cars, which have dozens of sensors all feeding information to a central computer that makes driving decisions.

Once you understand sensors, you start seeing them everywhere. Your phone has a light sensor (auto-brightness), an accelerometer (detects tilting for screen rotation), a proximity sensor (turns off the screen when you hold the phone to your ear), a microphone (sound sensor), and a camera (light sensor array). Each sensor gives the phone's computer information about the world, and the computer decides what to do with it. Every "smart" device is really just a combination of sensors, circuits, and decision logic — and understanding that combination starts right here.
