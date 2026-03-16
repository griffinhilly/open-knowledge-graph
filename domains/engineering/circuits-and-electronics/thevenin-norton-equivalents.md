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

## Explainer

You've already learned node-voltage and mesh-current methods — systematic techniques for solving circuits with many branches. Thevenin and Norton equivalents give you a complementary tool that addresses a different question: not "what is happening everywhere in this circuit?" but "what does this circuit look like to whatever is connected at these two terminals?" The power of the theorem is that any linear circuit, no matter how complicated — dozens of resistors, multiple sources — can be reduced to two elements as far as an external load is concerned.

The **Thevenin equivalent** replaces the circuit with a single voltage source V_th in series with a single resistance R_th. To find V_th, you disconnect the load and measure (or calculate) the **open-circuit voltage** at the terminals — the voltage that appears when nothing is connected and no current flows out. This is V_th. To find R_th for a circuit with only independent sources, you "deactivate" all sources (replace voltage sources with short circuits, current sources with open circuits) and compute the equivalent resistance looking into the terminals. The result is a two-element model that produces exactly the same terminal voltage and current for any load you connect, as if the whole network were still there.

The **Norton equivalent** is the current-source dual: a current source I_N in parallel with R_th, where I_N equals the **short-circuit current** — the current that flows when you connect a wire directly across the terminals. The same R_th appears in both equivalents. The relationship V_th = I_N × R_th is a **source transformation**, and it lets you convert freely between Thevenin and Norton forms. This duality is practically useful: depending on whether you're analyzing a series-type load or a parallel-type load, one form may be algebraically cleaner than the other.

The complication arises when the circuit contains **dependent sources** (controlled voltage or current sources whose value depends on some other circuit variable). You cannot deactivate these — they are not independent inputs but internal feedback mechanisms that change the effective resistance of the network. The fix is the **test-source method**: with all independent sources deactivated, apply a test voltage V_test (or test current I_test) at the terminals and compute the resulting current (or voltage). Then R_th = V_test / I_test. This works because the dependent sources respond to the test signal, and their contribution to the terminal impedance is automatically captured.

The most important application is **maximum power transfer**: for a fixed Thevenin source driving a variable load, maximum power is delivered to the load when R_load = R_th. At this point, the power delivered is V_th² / (4 R_th) — exactly half the available power, with the other half dissipated internally. This result is fundamental in communication systems (antenna impedance matching), audio amplifiers (speaker impedance matching), and any signal chain where you want maximum energy delivered to a downstream stage. Recognizing a circuit as a Thevenin source and identifying its R_th is often the first step in an impedance-matching design.


