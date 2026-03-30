---
id: quantum-circuits
title: Quantum Circuits
domain: computer-science
course: quantum-computing
prerequisites:
- id: quantum-gates
  type: hard
- id: qubits-and-quantum-states
  type: hard
tags:
- quantum-circuit
- circuit-model
- circuit-depth
- circuit-width
stage: advanced
status: validated
---
# Quantum Circuits

## Core Idea
A quantum circuit is a sequence of quantum gates applied to a register of qubits, read left-to-right in time. Each horizontal wire represents a qubit, gates are boxes or symbols on those wires, and measurement is typically performed at the end. Circuit depth (number of time steps) and width (number of qubits) are the primary complexity measures. The quantum circuit model is the standard computational model for quantum algorithms, analogous to Boolean circuits in classical computing, and is polynomially equivalent to quantum Turing machines.

## Questions

```yaml
- question: "In a quantum circuit diagram, what does a vertical line connecting two qubits with a dot on one and a circle-plus on the other represent?"
  type: multiple-choice
  options: ["A SWAP gate exchanging the two qubit states", "A CNOT gate with the dot as control and the circle-plus as target", "A measurement of both qubits in the Bell basis", "A classical conditional operation"]
  answer: 1
  explanation: "The standard circuit notation uses a filled dot for the control qubit and a circle-plus (oplus symbol) for the target qubit of a CNOT gate. The vertical line shows that the gate couples the two qubits. If the control qubit is |1>, the target qubit gets flipped. A SWAP gate is typically drawn with two X symbols connected by a line."

- question: "Quantum circuits must apply all gates sequentially — two gates on different qubits in the same time step would violate unitarity."
  type: true-false
  answer: false
  explanation: "Gates on disjoint sets of qubits can be applied simultaneously — they act on independent subsystems and their combined effect is the tensor product of the individual gates, which is still unitary. This parallelism is why circuit depth (time steps) is a separate measure from total gate count. Minimizing depth is important because qubits decohere over time, so shallower circuits are more practical."

- question: "Why is measurement typically placed at the end of a quantum circuit rather than interspersed throughout?"
  type: short-answer
  answer: "Measurement collapses the qubit to a definite classical state, destroying the superposition and any entanglement involving that qubit. Once measured, a qubit can no longer participate in quantum interference. Deferring measurement to the end preserves quantum coherence throughout the computation. By the principle of deferred measurement, any mid-circuit measurement followed by classical control can be replaced by a quantum-controlled operation with measurement deferred to the end."
  explanation: "The principle of deferred measurement shows that mid-circuit measurement is never necessary for the final outcome distribution — it can always be postponed. This simplifies circuit analysis because you can reason entirely in terms of unitary evolution until the final measurement. In practice, some error correction schemes do use mid-circuit measurement, but the computational power is the same."
```

## Explainer

A quantum circuit is the standard way to specify a quantum algorithm. The diagram looks like a musical score: each horizontal line is a qubit (a wire carrying quantum information through time), and gates are placed on these wires in the order they are applied, reading left to right. Single-qubit gates appear as boxes on one wire; two-qubit gates like CNOT span two wires with a vertical connector. The circuit begins with qubits initialized to |0> (by convention) and typically ends with measurement symbols on some or all wires.

The two key complexity measures for quantum circuits are **width** and **depth**. Width is the number of qubits — the spatial resource. Depth is the number of sequential time steps — the temporal resource. Gates on disjoint qubits can execute in the same time step (they commute because they act on independent subsystems), so depth counts the longest chain of dependent operations. Total gate count is also important but less fundamental: a circuit with many gates but low depth may be more practical than a shallow circuit with fewer gates, because real qubits decohere over time and depth directly corresponds to how long coherence must be maintained.

The quantum circuit model is **polynomially equivalent** to the quantum Turing machine, meaning either can simulate the other with at most polynomial overhead. This is the quantum analog of the equivalence between Boolean circuits and classical Turing machines. In practice, nearly all quantum algorithms are described as circuits rather than Turing machines because the circuit representation is more intuitive and directly maps to how quantum hardware operates. When we say an algorithm is "efficient," we mean it uses polynomial depth and polynomial width in the input size.

A crucial principle governing circuit design is **deferred measurement**: any circuit with mid-circuit measurements followed by classically controlled gates can be transformed into an equivalent circuit where all measurements occur at the end, with the classically controlled gates replaced by quantum-controlled gates. This means measurement never adds computational power — it only extracts classical information. The practical consequence is that you can analyze a quantum circuit as pure unitary evolution followed by a single round of measurement, even if the physical implementation performs measurements earlier. Understanding this principle clarifies why quantum circuits are reversible up to the final measurement step: the unitary part loses no information, and measurement is the irreversible extraction of a classical outcome from the quantum state.
