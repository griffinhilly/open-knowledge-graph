---
id: combining-simple-machines
title: Combining Simple Machines
domain: engineering
course: design-and-build
prerequisites:
- id: levers-in-action
  type: hard
- id: pulleys-in-action
  type: soft
- id: gears-and-wheels
  type: soft
- id: inclined-planes-in-building
  type: soft
- id: testing-and-improving
  type: soft
builds-toward:
- mechanical-advantage-in-real-life
- frames-machines-analysis
tags:
- simple-machines
- compound-machines
- engineering
- design
stage: concrete-operations
status: draft
---
# Combining Simple Machines

## Core Idea
Most real machines are not single simple machines — they are combinations of two or more simple machines working together, called compound machines. A bicycle combines wheels, axles, gears, and levers. Scissors combine two levers with wedge-shaped blades. A wheelbarrow combines a lever, a wheel, and an axle. Engineers design compound machines by figuring out what each stage of a task needs (lifting, cutting, turning, moving) and choosing the right simple machine for each stage, then connecting them so the output of one feeds into the input of the next.

## How It's Best Learned
Give students a real compound machine (a can opener, a hand-crank pencil sharpener, a pair of scissors) and challenge them to identify every simple machine inside it. Then reverse the process: present a task (move a heavy ball up a hill and into a bucket) and have students design a compound machine that combines at least two simple machines to accomplish it. Building Rube Goldberg machines (intentionally overcomplicated devices) is an engaging way to practice connecting one machine's output to another's input.

## Common Misconceptions
- A compound machine is always complicated. (Many compound machines are simple and everyday — scissors, a shovel, a bicycle. Compound just means "more than one simple machine combined.")
- Each simple machine in a compound machine works independently. (The simple machines are connected so that the output of one becomes the input of another. In a bicycle, your legs push pedals that turn a gear that pulls a chain that turns a wheel.)
- Compound machines eliminate the force-distance trade-off. (Each simple machine still obeys the trade-off. Combining machines chains the trade-offs together — they do not cancel out.)

## Questions

```yaml
- question: "Which simple machines are combined in a pair of scissors?"
  type: multiple-choice
  options: ["A pulley and a wheel", "Two levers and two wedges", "A gear and an inclined plane", "A screw and a pulley"]
  answer: 1
  explanation: "Scissors are two first-class levers joined at a fulcrum (the central screw or pin), and the blades are wedge-shaped — they taper to a thin cutting edge. When you squeeze the handles (lever action), the wedge-shaped blades concentrate force along a thin line to cut material."

- question: "In a compound machine, combining simple machines eliminates the trade-off between force and distance."
  type: true-false
  answer: false
  explanation: "Each simple machine in a compound machine still obeys the force-distance trade-off. Combining machines chains these trade-offs together. A bicycle, for example, uses gears to trade pedaling speed for wheel speed, and uses the wheel and axle to convert rotation into forward motion — but you still cannot get both more force and more speed for free."

- question: "Choose an everyday compound machine and identify at least two simple machines inside it."
  type: short-answer
  answer: "A wheelbarrow contains a lever (the handles and tray pivot around the wheel) and a wheel and axle (the wheel at the front). The lever lets you lift a heavy load with less force by placing it close to the wheel, and the wheel reduces friction so you can roll the load instead of dragging it."
  explanation: "Many everyday objects are compound machines. Other examples: a can opener (lever + gear + wedge), a bicycle (wheel and axle + gears + lever), a hand drill (wheel and axle + screw + gear). Identifying the simple machines inside compound machines develops the analytical skill engineers use when designing new machines."
```

## Explainer
You have learned about levers, pulleys, gears, wheels, inclined planes, and wedges individually. Now here is the engineering insight that makes these simple machines truly powerful: **you can combine them**.

A **compound machine** is two or more simple machines connected so that they work together. Most of the machines you use every day are compound machines. Take a **bicycle**: your foot pushes a pedal (a lever), which turns a chainring (a gear), which pulls a chain that turns a smaller gear on the rear wheel (another gear), which spins the rear wheel and axle (a wheel and axle). Four simple machines, chained together, convert your leg motion into fast rolling travel.

The key engineering principle is that the **output of one simple machine becomes the input of the next**. In the bicycle, the lever's output (rotation of the chainring) becomes the gear system's input. The gear system's output (rotation of the rear sprocket) becomes the wheel's input. Each stage transforms force, speed, or direction to get closer to the final goal. An engineer designing a compound machine thinks step by step: "What does the first stage need to do? What comes out of it? What does the next stage need?"

Consider a **can opener**. You squeeze the handles — that is a lever, multiplying your hand force. The lever turns a cutting wheel — that is a gear, changing the direction from squeezing to rotating. The cutting wheel has a sharp edge — that is a wedge, concentrating the force into a thin line that cuts through metal. Three simple machines, each doing one part of the job, connected in sequence.

Here is something important: combining simple machines does **not** magically overcome the force-distance trade-off. Each machine still trades force for distance (or speed for power). What combining does is let you chain multiple trade-offs together to transform your input into exactly the output you need. Your leg pushes a bicycle pedal slowly with a lot of force, and through three stages of simple machines, that becomes a wheel spinning fast with less force. The total work is the same — but the form of the work is completely different, and that is what makes compound machines useful.

Building a Rube Goldberg machine — an intentionally overcomplicated device where a ball rolls down a ramp (inclined plane) that tips a lever that releases a weight on a pulley that pulls a string that turns a gear — is a fun way to practice connecting simple machines. The machine is absurdly complex for what it does, but building one teaches you to think about inputs and outputs, connections and sequences, which is exactly what real engineering requires.
