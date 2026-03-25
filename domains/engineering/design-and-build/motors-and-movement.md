---
id: motors-and-movement
title: Motors and Movement
domain: engineering
course: design-and-build
prerequisites:
- id: building-a-simple-circuit
  type: hard
- id: gears-and-wheels
  type: soft
- id: led-circuits
  type: soft
builds-toward:
- sensors-basics
- technology-in-everyday-life
- charge-and-current-flow
tags:
- motors
- circuits
- movement
- engineering
stage: concrete-operations
status: validated
---
# Motors and Movement

## Core Idea
An electric motor converts electrical energy into motion — it spins when current flows through it. Motors are inside fans, washing machines, electric toothbrushes, toy cars, and drones. In an engineering project, a motor turns a circuit from something that just lights up into something that moves. Engineers connect motors to wheels, gears, propellers, and other mechanisms to create useful motion. The direction a motor spins can be reversed by flipping the battery connections, and the speed can be changed by adjusting the voltage or adding gears.

## How It's Best Learned
Give students a small DC motor, a battery pack, and wires. First, connect the motor and let it spin freely — feel the vibration, see the shaft rotate. Then attach a small propeller or a piece of tape to the shaft so the spin is visible. Reverse the battery connections and observe the motor spin the opposite direction. Then challenge students to build something that moves: a simple car using the motor, a battery, and recycled materials. Connect to the gears topic: add a gear to the motor shaft and show how different gear ratios change the speed and force of the output.

## Common Misconceptions
- Motors only spin — they cannot create other types of motion. (Motors provide rotation, but engineers convert that rotation into other motions using gears, cranks, cams, and linkages. A windshield wiper's back-and-forth motion starts as motor rotation.)
- All motors are the same. (Motors vary enormously in size, power, speed, and type. A watch motor is tiny and precise. A car engine motor is powerful and heavy. Choosing the right motor is an engineering decision.)
- Motors spin at one fixed speed. (Motor speed depends on the voltage supplied and the load on the motor. Engineers use gears, controllers, and variable power supplies to adjust speed for different applications.)

## Questions

```yaml
- question: "What does an electric motor do?"
  type: multiple-choice
  options: ["It stores electricity for later use", "It converts electrical energy into rotational motion", "It converts motion into electricity", "It makes electricity flow faster"]
  answer: 1
  explanation: "A motor converts electrical energy into mechanical motion — specifically, rotation (spinning). This spinning motion can then be transferred to wheels, gears, propellers, or other mechanisms to create useful movement. The device that does the opposite — converting motion into electricity — is called a generator."

- question: "You can reverse the direction a motor spins by switching the positive and negative battery connections."
  type: true-false
  answer: true
  explanation: "Reversing the polarity (swapping which wire connects to positive and which connects to negative) reverses the direction of the magnetic field inside the motor, which reverses the spin direction. This is how many toys and devices control forward and backward motion."

- question: "A motor spins very fast but does not have much pushing force. How could an engineer make it push harder while accepting slower speed?"
  type: short-answer
  answer: "Attach a small gear to the motor shaft and have it drive a larger gear. The larger gear will turn slower but with more force (torque). This is the same gear ratio trade-off used in bicycles — trading speed for power."
  explanation: "This connects motors to the gears topic. A motor's raw output is usually high-speed, low-force. For tasks like turning wheels on a toy car or lifting something, engineers use gear reduction to convert that high speed into the slower, more powerful rotation they need. Almost every motor in a real product has a gearbox attached to it."
```

## Explainer
So far, your circuits have been static — they light up, but they do not move. A **motor** changes everything. Connect a small DC motor to a battery, and the shaft spins. That spinning shaft is the starting point for every electric-powered moving device: fans, cars, drones, washing machines, robots, and electric toothbrushes.

A motor converts **electrical energy into rotational motion**. Inside the motor, electric current creates a magnetic field that pushes against permanent magnets, causing the central shaft to spin. The details of how this works involve electromagnets and magnetic forces, which you may study later. For now, the engineering takeaway is simple: **current in, spinning out**.

The first thing to try with a motor is **reversing the battery connections**. Swap the wires connected to the positive and negative terminals. The motor spins in the opposite direction. This is how many devices control forward and backward motion — a toy car reverses by reversing the current to its motor. This simple trick gives you control over direction.

The second important concept is that a motor's raw spin is usually **fast but weak**. A small hobby motor might spin at thousands of revolutions per minute, but it cannot push very hard. For most engineering tasks, you need slower rotation with more force. This is where **gears** come in. Attach a small gear to the motor shaft and connect it to a larger gear. The large gear turns slower but pushes harder — the same speed-for-force trade-off you learned about with gears. Almost every real motor in a product — from power drills to electric cars — has a **gearbox** that adjusts the motor's speed and force to match the task.

Now the engineering challenge becomes interesting: **build something that moves**. A simple car needs a motor connected to wheels (through gears or directly), a battery for power, a switch for control, and a frame to hold everything together. A fan needs a motor with a propeller attached to the shaft. A vibrating phone alert is just a motor with an unbalanced weight on the shaft. Each application uses the same basic motor but connects it to different mechanisms to produce different kinds of useful motion. The engineering skill is in the connection — figuring out how to transfer the motor's rotation into the specific movement your design needs.
