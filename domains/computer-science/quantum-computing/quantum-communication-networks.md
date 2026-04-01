---
id: quantum-communication-networks
title: Quantum Communication Networks
domain: computer-science
course: quantum-computing
prerequisites:
- id: quantum-key-distribution
  type: hard
- id: quantum-entanglement-as-resource
  type: hard
- id: quantum-teleportation
  type: soft
tags:
- quantum-communication
- quantum-networks
- quantum-repeaters
- quantum-internet
stage: expert
status: validated
---

# Quantum Communication Networks

## Core Idea
Quantum communication networks extend quantum key distribution and quantum teleportation to build a distributed quantum internet where quantum information can be transmitted and processed across multiple nodes. Key components include quantum repeaters (extending communication distance beyond direct fiber), quantum memory (storing quantum states), and quantum-secured networks (distributed quantum computing, blind quantum computing). The vision is a "quantum internet" that complements classical networks, enabling unhackable communication, distributed quantum computing, and sensing applications. Practical challenges include maintaining quantum coherence over distance, constructing reliable quantum repeaters, and integrating with classical infrastructure.

## Questions

```yaml
- question: "Why can't quantum key distribution be extended to arbitrary distances using simple relay nodes, like classical networks?"
  type: short-answer
  answer: "Quantum communication is fundamentally limited by the no-cloning theorem: you cannot perfectly copy an unknown quantum state. Classical repeaters amplify and resend signals; quantum repeaters cannot simply amplify quantum states without destroying them. To extend quantum communication, you need quantum repeaters that use entanglement swapping: establish shared entanglement between adjacent segments, then perform Bell measurements to 'teleport' entanglement across segments. However, this requires quantum memory (storing quantum states) and suffers from decoherence loss over long distances. This is the core challenge of quantum repeaters: achieving sufficient fidelity and rate to be practical."
  explanation: "The no-cloning theorem is fundamental: quantum communication requires new techniques (entanglement swapping, quantum memory) not available classically. This explains why quantum networks are more challenging to build than classical networks."

- question: "A quantum repeater extends communication distance via entanglement swapping. What is entanglement swapping, and why does it preserve quantum properties over long distances?"
  type: multiple-choice
  options:
    - "Entanglement swapping is physically moving one qubit from node A to node B, which is impossible"
    - "Entanglement swapping connects two separate entangled pairs into a single longer-distance entangled pair via Bell measurements, extending the range of entanglement-dependent protocols like QKD and quantum teleportation"
    - "Entanglement swapping is creating new entanglement from scratch, not relying on prior entanglement"
    - "Entanglement swapping requires copying quantum states, violating the no-cloning theorem"
  answer: 1
  explanation: "Entanglement swapping is a Bell measurement technique. If you have two entangled pairs (A-B and B-C), a Bell measurement on B's qubits converts the state into a single entangled pair A-C, as if A and C were directly entangled. This enables establishing long-distance entanglement by chaining together shorter-distance segments. The measurement collapses information but correlates A and C in a maximally entangled state. This preserves the quantum properties of entanglement needed for QKD and teleportation, extending communication range."

- question: "Quantum repeaters require quantum memory to store quantum states between operations. Why is quantum memory so challenging?"
  type: true-false
  answer: true
  explanation: "Quantum states decohere rapidly: environmental interactions destroy superposition and entanglement. Quantum memory must maintain coherence for seconds or longer (in repeater networks), compared to microseconds in isolated quantum computers. Achieving long coherence times requires extreme conditions: ultra-low temperatures, electromagnetic shielding, and sophisticated error correction. Current quantum memories have coherence times of seconds (e.g., trapped atoms) or milliseconds (e.g., diamond NV centers), far from the extended times needed for continental-scale networks. Improving quantum memory is a critical bottleneck for practical quantum repeater networks."
```

## Explainer

Quantum communication networks extend distributed quantum computing across multiple locations via quantum channels. Unlike classical networks that transmit bits, quantum networks transmit quantum information (qubits, entangled pairs) over long distances, enabling quantum-secured communication, distributed quantum computing, and entanglement-based sensing.

**Quantum Repeaters**: The fundamental component of long-distance quantum networks. A quantum repeater connects shorter-range quantum links into a longer-range link via entanglement swapping. The process: (1) establish independent entangled pairs over short distances (a few kilometers of fiber or free space), (2) perform Bell measurements at intermediate nodes to "swap" entanglement, connecting the pairs, (3) repeat until spanning the desired distance. Each repeater must perform high-fidelity Bell measurements and store quantum states in quantum memory.

**Entanglement Swapping**: Suppose Alice-Bob share an entangled pair, Bob-Charlie share another. Bob performs a Bell measurement (projecting onto one of four Bell basis states), instantly correlating Alice and Charlie into an entangled state. If Bob's measurement is successful, Alice-Charlie are now entangled (with knowledge of which Bell state). If unsuccessful, entanglement swapping can be re-attempted with stored quantum states. This mechanism has no classical analog: you cannot establish long-distance communication without physically moving information, but entanglement swapping "teleports" correlations via measurement.

**Quantum Memory**: Critical for repeaters. Between receiving quantum states, storing them, and swapping entanglement, the states must survive decoherence. Quantum memory stores quantum states in atomic ensembles, trapped ions, diamond defects, or other systems. Current best coherence times are ~seconds (atomic ensembles), limiting repeater distance and rate. Improving memory coherence is a major research goal.

**Quantum Internet Alliance Vision**: A distributed quantum network enabling:
1. **Quantum-Key Distribution**: Unhackable encryption across the network.
2. **Blind Quantum Computing**: Clients delegate computation to a quantum server without revealing their computation (privacy-preserving distributed computing).
3. **Distributed Quantum Computing**: Multiple quantum computers connected to jointly solve large problems.
4. **Quantum Sensing**: Entanglement-enhanced sensing (e.g., distributed atomic clocks, gravitational wave detectors).

**Practical Challenges**:

1. **Distance and Rate**: Current quantum repeaters achieve short distances (~100 km) and low rates (few entangled pairs per second). Reaching continental scales requires improvements.

2. **Fidelity**: Each gate and measurement reduces fidelity. Maintaining high fidelity over many hops requires error correction, further multiplying qubit requirements.

3. **Integration**: Quantum networks must interoperate with classical infrastructure (timing, synchronization, control). Building hybrid quantum-classical networks is complex.

4. **Standardization**: Unlike classical networks (TCP/IP, Ethernet), no standard quantum network protocols exist. Research is developing quantum internet protocols.

**Current Implementations**:

- **Long-Distance QKD**: Over 400 km via satellites or fiber, with lower rates.
- **Chinese Quantum Satellite**: Demonstrates satellite-based long-distance QKD, proving feasibility of space-based quantum networks.
- **Academic Repeater Experiments**: Demonstrating Bell state entanglement swapping, quantum memory integration (e.g., Delft, Insbruck).

**Future Directions**:

- **Commercial Quantum Repeaters**: Moving from laboratory demonstrations to deployable hardware.
- **Quantum Network Operating System**: Developing protocols and software for quantum internet routing, error correction, and resource management.
- **Quantum-Classical Hybrid**: Integrating quantum communication with classical networks for practical applications.

Quantum communication networks represent the long-term vision of quantum technology: not isolated quantum computers, but a distributed quantum internet enabling cryptography, computing, and sensing applications at scale.
