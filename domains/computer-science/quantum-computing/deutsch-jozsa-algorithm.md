---
id: deutsch-jozsa-algorithm
title: Deutsch-Jozsa Algorithm
domain: computer-science
course: quantum-computing
prerequisites:
- id: quantum-circuits
  type: hard
- id: quantum-measurement-and-born-rule
  type: hard
tags:
- Deutsch-Jozsa
- oracle
- quantum-speedup
- quantum-parallelism
stage: advanced
status: validated
---
# Deutsch-Jozsa Algorithm

## Core Idea
The Deutsch-Jozsa algorithm determines whether a Boolean function f:{0,1}^n -> {0,1} is constant (same output for all inputs) or balanced (outputs 0 for exactly half the inputs and 1 for the other half), promised that one of these holds. A classical deterministic algorithm requires 2^(n-1) + 1 queries in the worst case, but the quantum algorithm uses exactly one query to the function oracle. It was the first algorithm to demonstrate a provable exponential separation between quantum and classical deterministic query complexity, establishing that quantum computers can solve certain problems fundamentally faster.

## Questions

```yaml
- question: "The Deutsch-Jozsa algorithm achieves an exponential speedup over classical algorithms for determining whether a function is constant or balanced. What type of speedup is this?"
  type: multiple-choice
  options: ["Exponential speedup over all classical algorithms including probabilistic ones", "Exponential speedup over deterministic classical algorithms only — a randomized algorithm can solve it with high probability in O(1) queries", "Polynomial speedup similar to Grover's algorithm", "No speedup — it is primarily of theoretical interest"]
  answer: 1
  explanation: "The Deutsch-Jozsa problem has an exponential quantum vs. deterministic-classical separation, but a randomized classical algorithm can solve it with high probability using only O(1) queries (sample a few random inputs; if you ever see both 0 and 1 outputs, it's balanced). The significance is theoretical: it was the first proof that quantum query complexity can be exponentially smaller than deterministic query complexity. The practical speedup over randomized algorithms is constant, not exponential."

- question: "In the Deutsch-Jozsa circuit, the ancilla qubit is initialized to |1> rather than |0> before the Hadamard is applied. This is an arbitrary convention with no effect on the algorithm."
  type: true-false
  answer: false
  explanation: "Initializing the ancilla to |1> and then applying H produces |->  = (|0> - |1>)/sqrt(2). When the oracle Uf acts on |x>|-> it produces (-1)^f(x)|x>|->. This phase kickback encodes f(x) into the phase of |x> rather than into the ancilla state. If the ancilla were initialized to |0>, the oracle would write f(x) into the ancilla, entangling it with the input register and preventing the interference that the algorithm relies on."

- question: "Explain the role of interference in the Deutsch-Jozsa algorithm — specifically, why does the final Hadamard transform on the input register produce |0...0> for constant functions but never |0...0> for balanced functions?"
  type: short-answer
  answer: "After the oracle, each computational basis state |x> has acquired a phase (-1)^f(x). The final Hadamard transform on n qubits maps each |x> to a superposition over all basis states. The amplitude of |0...0> in the output is the sum of (-1)^f(x) over all x, divided by 2^n. If f is constant, all phases are the same and the sum is +/-1, giving probability 1 for |0...0>. If f is balanced, half the phases are +1 and half are -1, so the sum is exactly zero, giving probability 0 for |0...0>."
  explanation: "This is a clean example of constructive and destructive interference. The Hadamard transform recombines all 2^n amplitude paths, and the phases imposed by the oracle determine whether they add up or cancel. A constant function produces coherent addition (constructive interference at |0...0>), while a balanced function produces perfect cancellation (destructive interference at |0...0>). This interference pattern lets a single measurement distinguish the two cases with certainty."
```

## Explainer

The Deutsch-Jozsa algorithm is historically important as the first quantum algorithm to demonstrate an exponential separation from classical computation, even though the problem it solves is artificial. You are given a black-box function f:{0,1}^n -> {0,1} with the promise that f is either **constant** (all outputs are the same) or **balanced** (exactly half the outputs are 0 and half are 1). Classically, in the worst case, you must evaluate f on 2^(n-1) + 1 inputs to be certain — you might get unlucky and see the same output for the first 2^(n-1) queries. The quantum algorithm uses one query.

The circuit works as follows. Prepare n input qubits in |0> and one ancilla qubit in |1>. Apply Hadamard to all n+1 qubits. The input register is now in a uniform superposition over all 2^n basis states, and the ancilla is in |-> = (|0> - |1>)/sqrt(2). Apply the oracle Uf, which maps |x>|y> to |x>|y xor f(x)>. Because the ancilla is in |-> , the effect of the oracle is **phase kickback**: the ancilla stays in |-> and each input state |x> acquires a phase (-1)^f(x). The state is now (1/sqrt(2^n)) * sum_x (-1)^f(x) |x> tensor |-> .

Now apply Hadamard to each input qubit. The Hadamard transform maps the state to a sum over all output basis states, where the amplitude of each output state |y> is a sum involving (-1)^f(x) * (-1)^(x dot y) over all x. The amplitude of |0...0> specifically is (1/2^n) * sum_x (-1)^f(x). If f is constant, this sum is +/- 1, so the probability of measuring |0...0> is 1. If f is balanced, exactly 2^(n-1) terms are +1 and 2^(n-1) are -1, so the sum is zero and the probability of measuring |0...0> is 0. A single measurement therefore determines the answer with certainty.

The key mechanism is **interference**. The oracle embeds the function's behavior into phases, and the final Hadamard transform recombines these phases. For a constant function, all paths interfere constructively at |0...0>. For a balanced function, they interfere destructively and the amplitude at |0...0> vanishes completely. This pattern — oracle encodes information into phases, followed by interference that concentrates the answer — recurs throughout quantum algorithms. The Deutsch-Jozsa algorithm is the simplest instance of this paradigm. It is worth noting that a probabilistic classical algorithm can solve this problem with O(1) random queries and high confidence, so the exponential advantage is specifically over deterministic classical algorithms. The deeper significance is conceptual: it proves that quantum query complexity can be strictly less than classical.
