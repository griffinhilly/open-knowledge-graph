---
id: thevenin-norton-equivalents
title: Thevenin and Norton Equivalent Circuits
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: node-voltage-method
  type: hard
- id: superposition-theorem-circuits
  type: soft
- id: mesh-current-method
  type: soft
builds-toward:
- first-order-transient-circuits
- ac-circuit-analysis-methods
- bjt-amplifier-configurations
tags:
- thevenin
- norton
- source-transformation
- maximum-power-transfer
- equivalent-circuits
stage: formal-systems
status: validated
---

# Thevenin and Norton Equivalent Circuits

## Core Idea
Any linear two-terminal network can be replaced by a Thevenin equivalent — a single voltage source V_th in series with a resistance R_th — or a Norton equivalent — a current source I_N in parallel with R_th, where I_N = V_th / R_th. The Thevenin voltage equals the open-circuit terminal voltage and the Norton current equals the short-circuit terminal current. For circuits with only independent sources, R_th is found by deactivating all sources and computing the equivalent resistance; circuits with dependent sources require applying a test source. Maximum power is transferred to a load when R_load = R_th.

## How It's Best Learned
Practice finding Thevenin equivalents using all three methods: (1) open-circuit voltage and short-circuit current, (2) source deactivation for R_th, and (3) test-source injection. Use the test-source method whenever dependent sources are present. Verify by connecting a load and computing the load voltage two ways.

## Common Misconceptions
- Deactivating dependent sources when finding R_th — this gives incorrect results; use the test-source method.
- Confusing which terminal pair the equivalent is referenced to.
- Assuming the Thevenin equivalent preserves internal branch voltages and currents — only the external terminal behavior is preserved.

## Questions

```yaml
- question: "An engineer finds the Thevenin equivalent of a complex amplifier circuit (V_th = 6V, R_th = 100Ω) and uses it to correctly predict the load voltage. She then uses the same Thevenin model to find the voltage drop across a specific internal resistor deep inside the original amplifier. What is wrong with this approach?"
  type: multiple-choice
  options:
    - "Nothing — the Thevenin equivalent is an exact model that preserves all internal voltages and currents"
    - "The Thevenin equivalent only applies when the load resistance equals R_th"
    - "The Thevenin equivalent preserves only the external terminal behavior — internal branch voltages and currents cannot be recovered from the two-element model"
    - "The Thevenin voltage must be recalculated for each internal node before it can be used"
  answer: 2
  explanation: "The Thevenin theorem guarantees equivalence at the terminals: any load you connect will see the same voltage and current as if the full network were present. But the two-element model (V_th in series with R_th) has no internal branches — the complex internal structure is compressed into a single resistance. You cannot use the Thevenin model to find what is happening inside the original network. If you need internal branch quantities, you must return to the full circuit analysis. The Thevenin equivalent is a terminal model, not a full internal model."

- question: "A circuit contains a voltage-controlled current source (a dependent source) plus some independent resistors and an independent voltage source. To find R_th, a student deactivates the independent voltage source (replaces it with a short) and the dependent source (replaces it with an open), then measures resistance at the terminals. Why is this incorrect?"
  type: multiple-choice
  options:
    - "Independent voltage sources should be replaced with opens, not shorts"
    - "Dependent sources cannot be deactivated — they respond to circuit variables and their effect on terminal impedance must be captured by applying a test source with all independent sources deactivated"
    - "You must leave the independent source active when finding R_th for circuits with dependent sources"
    - "R_th does not exist for circuits that contain dependent sources"
  answer: 1
  explanation: "Dependent sources are not independent inputs — they are internal feedback mechanisms whose value depends on some other circuit variable (a voltage or current elsewhere in the network). Setting them to zero removes the feedback and fundamentally changes the effective impedance of the circuit. The correct method is the test-source approach: deactivate all *independent* sources only, then apply a test voltage V_test at the terminals and find the resulting current I_test (or vice versa). The dependent source responds to V_test through the circuit, and R_th = V_test/I_test automatically captures its contribution."

- question: "When a load resistance equals the Thevenin resistance (R_load = R_th), maximum power is delivered to the load — and at this optimal point, 100% of the Thevenin source's available power reaches the load."
  type: true-false
  answer: false
  explanation: "At the maximum power transfer condition (R_load = R_th), exactly half the total power is dissipated in the load and half in R_th. The load power is V_th²/(4R_th) and the total power drawn from the source is V_th²/(2R_th), so efficiency is exactly 50%. This surprises students who expect 'maximum power transfer' to mean maximum efficiency. The condition maximizes the power delivered to the load, not the fraction of total power that reaches it. Maximum efficiency (approaching 100%) occurs when R_load >> R_th, but then very little current flows and very little power is transferred at all."

- question: "A Thevenin equivalent and its Norton equivalent representation contain the same R_th, and the two are related by V_th = I_N × R_th."
  type: true-false
  answer: true
  explanation: "This relationship — V_th = I_N × R_th — is called source transformation, and it allows free conversion between the two forms. Both equivalents represent the same network behavior at the terminals. R_th appears in both because it captures the same internal impedance regardless of whether you express the source as a voltage (Thevenin) or a current (Norton). In practice, you find whichever is easier to calculate — often V_th = open-circuit voltage and I_N = short-circuit current — and then use the relationship to find the third quantity without additional computation."

- question: "Why does deactivating a dependent source when finding R_th give an incorrect result, and what does the test-source method do differently that makes it correct?"
  type: short-answer
  answer: "A dependent source produces a voltage or current that is a function of some other variable in the circuit. Deactivating it sets it to zero permanently, which removes internal feedback and changes the effective impedance the terminals 'see.' The test-source method keeps dependent sources active: you apply a known test signal at the terminals, let the dependent source respond as it normally would, and measure the result. R_th = V_test/I_test then captures the actual impedance including all feedback effects."
  explanation: "Concretely: suppose a circuit has a dependent current source equal to 3 times the current in a certain branch. When you apply a test voltage, current flows in that branch, and the dependent source adds 3 times that current elsewhere in the network — changing how much total current the test voltage drives. This changes the effective resistance. If you had set the dependent source to zero, you would have computed the resistance of the network without its feedback, which is a different (and wrong) number. The test-source method is the only approach that correctly handles all linear networks, with or without dependent sources."
```

## Explainer

You've already learned node-voltage and mesh-current methods — systematic techniques for solving circuits with many branches. Thevenin and Norton equivalents give you a complementary tool that addresses a different question: not "what is happening everywhere in this circuit?" but "what does this circuit look like to whatever is connected at these two terminals?" The power of the theorem is that any linear circuit, no matter how complicated — dozens of resistors, multiple sources — can be reduced to two elements as far as an external load is concerned.

The **Thevenin equivalent** replaces the circuit with a single voltage source V_th in series with a single resistance R_th. To find V_th, you disconnect the load and measure (or calculate) the **open-circuit voltage** at the terminals — the voltage that appears when nothing is connected and no current flows out. This is V_th. To find R_th for a circuit with only independent sources, you "deactivate" all sources (replace voltage sources with short circuits, current sources with open circuits) and compute the equivalent resistance looking into the terminals. The result is a two-element model that produces exactly the same terminal voltage and current for any load you connect, as if the whole network were still there.

The **Norton equivalent** is the current-source dual: a current source I_N in parallel with R_th, where I_N equals the **short-circuit current** — the current that flows when you connect a wire directly across the terminals. The same R_th appears in both equivalents. The relationship V_th = I_N × R_th is a **source transformation**, and it lets you convert freely between Thevenin and Norton forms. This duality is practically useful: depending on whether you're analyzing a series-type load or a parallel-type load, one form may be algebraically cleaner than the other.

The complication arises when the circuit contains **dependent sources** (controlled voltage or current sources whose value depends on some other circuit variable). You cannot deactivate these — they are not independent inputs but internal feedback mechanisms that change the effective resistance of the network. The fix is the **test-source method**: with all independent sources deactivated, apply a test voltage V_test (or test current I_test) at the terminals and compute the resulting current (or voltage). Then R_th = V_test / I_test. This works because the dependent sources respond to the test signal, and their contribution to the terminal impedance is automatically captured.

The most important application is **maximum power transfer**: for a fixed Thevenin source driving a variable load, maximum power is delivered to the load when R_load = R_th. At this point, the power delivered is V_th² / (4 R_th) — exactly half the available power, with the other half dissipated internally. This result is fundamental in communication systems (antenna impedance matching), audio amplifiers (speaker impedance matching), and any signal chain where you want maximum energy delivered to a downstream stage. Recognizing a circuit as a Thevenin source and identifying its R_th is often the first step in an impedance-matching design.


