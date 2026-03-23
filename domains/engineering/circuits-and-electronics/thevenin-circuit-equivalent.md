---
id: thevenin-circuit-equivalent
title: Thévenin Equivalent Circuits
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-theorems-linearity
  type: hard
- id: ideal-voltage-and-current-sources
  type: hard
builds-toward:
- maximum-power-transfer
- sinusoidal-steady-state-analysis
tags:
- thevenin
- equivalent-circuit
- source-transformation
stage: formal-systems
status: validated
---

# Thévenin Equivalent Circuits

## Core Idea
Thévenin's theorem states any linear two-terminal circuit simplifies to a voltage source V_th in series with resistance R_th. V_th is the open-circuit voltage at the terminals, and R_th is found by zeroing independent sources and measuring resistance. This powerful simplification enables efficient load analysis and is widely used in circuit design.

## Questions

```yaml
- question: "You need to find the voltage delivered to load resistors of 10Ω, 47Ω, and 100Ω connected to a complex circuit. What is the advantage of finding the Thévenin equivalent first?"
  type: multiple-choice
  options:
    - "You still solve the circuit three times, but each solution is simpler because the Thévenin model has fewer nodes"
    - "You reduce the source network once to V_th and R_th, then use a simple voltage divider formula for each load — no re-solving required"
    - "You find V_th once, and R_th equals the smallest resistor in the source network"
    - "You cannot use Thévenin's theorem unless all three loads are connected simultaneously"
  answer: 1
  explanation: "The payoff of Thévenin equivalents is decoupling the source from the load. You solve the source network once to find V_th (open-circuit voltage) and R_th (Thévenin resistance). Then for any load R_L, V_load = V_th × R_L / (R_th + R_L) — a simple voltage divider. Changing the load never requires re-solving the source network. This is why Thévenin analysis is so widely used: it converts a complex multi-component problem into a trivial two-resistor calculation for every subsequent load variation."

- question: "To find R_th for a circuit containing only independent sources, you 'zero' the sources. What does zeroing a voltage source and zeroing a current source mean physically?"
  type: multiple-choice
  options:
    - "Both become open circuits, since a zero-value source contributes nothing to the circuit"
    - "Voltage sources become open circuits; current sources become short circuits"
    - "Voltage sources become short circuits (wires); current sources become open circuits (breaks)"
    - "Both sources are removed entirely and their terminals are left disconnected"
  answer: 2
  explanation: "Zeroing sets a source's value to zero. A voltage source with 0 V enforces zero potential difference across its terminals — exactly what a short circuit (wire) does. A current source with 0 A passes no current — exactly what an open circuit (break) does. Reversing these (option B) is a very common error that produces an incorrect R_th. The physical interpretation: a dead voltage source is a wire; a dead current source is a gap."

- question: "Thévenin's theorem works because a linear circuit produces a straight-line V-I relationship at any two terminals, and a voltage source in series with a resistor is precisely the minimal circuit with that characteristic."
  type: true-false
  answer: true
  explanation: "Linearity means the terminal voltage V is a linear function of the current I drawn: V = V_oc − I·R_th. This is a straight line in V-I space. The intercept at I = 0 is V_th (the open-circuit voltage), and the slope magnitude is R_th. A voltage source V_th in series with R_th produces exactly this same straight-line V-I characteristic. Thévenin's theorem is therefore a direct consequence of linearity: any circuit satisfying superposition has a Thévenin equivalent, because linearity guarantees the straight-line terminal behavior."

- question: "For a circuit that contains dependent sources, R_th can be found by zeroing the dependent sources and computing the resistance at the terminals."
  type: true-false
  answer: false
  explanation: "Dependent sources cannot be zeroed — they are controlled by circuit variables (other voltages or currents), and setting them to zero removes relationships that are essential to the circuit's behavior, producing an incorrect R_th. For circuits with dependent sources, the correct procedure is: (1) zero only the independent sources, (2) apply a test voltage V_test (or current I_test) at the terminals, and (3) compute R_th = V_test / I_test from the resulting current (or voltage). The test-source method correctly accounts for dependent source behavior."

- question: "Explain why Thévenin's theorem holds — why can any linear two-terminal circuit always be replaced by a voltage source and a single resistor?"
  type: short-answer
  answer: "Because linearity guarantees that the terminal voltage V is a linear function of the terminal current I: V = V_oc − I·R_th. Any straight-line V-I relationship can be reproduced by a voltage source V_th in series with a resistor R_th. No more complex internal structure is needed — from the terminals' perspective, only these two numbers (V_th and R_th) matter. V_th is the open-circuit voltage (I = 0), and R_th is the slope of the V-I line."
  explanation: "This is why Thévenin's theorem applies to any linear circuit regardless of how many resistors, capacitors, inductors, or sources it contains internally — the linearity property guarantees the terminal behavior collapses to a straight line. The theorem is essentially saying: all the internal complexity contributes only two numbers externally. This same reasoning underlies Norton's theorem (a current source in parallel with R_th), which represents the same straight line using the other intercept (at V = 0) and the same slope."
```

## Explainer

You've studied the linearity property of circuits: responses scale proportionally with sources, and superposition holds. Thévenin's theorem is one of the most powerful consequences of linearity. It says that no matter how tangled a network of resistors and sources looks internally, from the perspective of any two terminals it behaves exactly like a single voltage source in series with a single resistor. Everything inside the box collapses to just two numbers: **V_th** and **R_th**.

Why does this work? Because the circuit is linear, the voltage at the output terminals must be a linear function of the current drawn from those terminals: V = V_oc − I·R_th. This is the equation of a straight line in V-I space, and a straight-line I-V relationship is precisely what a voltage source in series with a resistor produces. The intercept on the voltage axis (where I = 0) is the **open-circuit voltage V_th** — the terminal voltage when nothing is connected. The slope of the line is the **Thévenin resistance R_th** — how much the terminal voltage drops per unit of current drawn. These two quantities completely characterize how the circuit interacts with any external load.

Finding **V_th** is usually straightforward: remove the load, leave the terminals open-circuited, and calculate the voltage across those open terminals using whatever circuit analysis techniques fit (node voltage, mesh current, superposition). Finding **R_th** requires more care. The standard method is to deactivate all independent sources — **zero them** by replacing voltage sources with short circuits (wires) and current sources with open circuits (breaks) — and then measure the resistance seen looking into the terminals. With ideal sources zeroed, you're left with a resistor network whose equivalent resistance is R_th. If the circuit contains only independent sources, this always works. (If it contains dependent sources, R_th must be found by applying a test source and computing the ratio V_test/I_test, because zeroing dependent sources is invalid.)

The practical power of Thévenin equivalents is that they decouple the source network from the load. Suppose you're designing a sensor interface and want to know how a variable load resistor will affect the sensor output. Without Thévenin, you'd solve the whole circuit for each load value. With Thévenin, you reduce the source network once to V_th and R_th, then treat all load variations as a simple voltage divider: V_load = V_th · R_L / (R_th + R_L). The theorem scales up beautifully — multi-battery power supplies, IC output stages, audio amplifier outputs, and transmission line models are all routinely reduced to Thévenin equivalents to analyze how they interact with their loads. The **maximum power transfer theorem** (a direct consequence) states that maximum power is delivered to a load when R_L = R_th — you can only derive this cleanly because the Thévenin framework makes R_th visible as a distinct quantity.


