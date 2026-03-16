---
id: kolmogorov-complexity
title: Kolmogorov Complexity
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: hard
- id: re-and-co-re-languages
  type: soft
- id: cardinality-and-countability
  type: soft
- id: big-o-notation
  type: soft
- id: combinations
  type: soft
- id: algorithm-complexity
  type: soft
tags:
- algorithmic-information-theory
- randomness
- descriptional-complexity
stage: advanced
status: validated
---

# Kolmogorov Complexity

## Core Idea
The Kolmogorov complexity K(x) of a string x is the length of the shortest program that outputs x on a fixed universal Turing machine. It provides an objective measure of the information content or 'randomness' of a string — a string is random if its shortest description is roughly as long as itself. Kolmogorov complexity is uncomputable: no algorithm can compute K(x) for all x. It has deep connections to data compression, statistical inference, and the mathematical foundations of probability.

## How It's Best Learned
Start with concrete examples: a string of one million zeros has very low Kolmogorov complexity (a short program generates it), while a truly random string of the same length likely requires a program nearly as long as itself. Prove the incompressibility lemma to rigorously establish that most strings are almost incompressible.

## Common Misconceptions
- Kolmogorov complexity depends on the choice of universal Turing machine, but only up to an additive constant (the invariance theorem), making it machine-independent up to a fixed offset.
- Randomness in the Kolmogorov sense is a property of individual strings, not of a probability distribution — a specific string either is or is not complex, regardless of how it was generated.

## Explainer

You already understand Turing machines as universal computing devices. Kolmogorov complexity asks a different question about them: not "what can be computed?" but "how concisely can something be described?" The **Kolmogorov complexity** K(x) of a string x is the length (in bits) of the shortest program that, running on a fixed universal Turing machine, produces x and halts. It is the algorithmic analog of information content.

The intuition is immediate with examples. A string of one million zeros has K(x) around log₂(1,000,000) ≈ 20 bits — you only need to say "print zero a million times." But a string produced by fair coin flips has, with overwhelming probability, no description shorter than itself: the string *is* the most compact representation of itself. Such strings are called **incompressible** or, in Kolmogorov's sense, **random**. Note the paradox: most strings are random in this sense, yet you cannot name a specific one — the very act of specifying a string you claim is random gives it a short description (the specification itself).

The **invariance theorem** resolves the worry that K depends on which universal Turing machine you choose. If U and V are two universal machines, then |K_U(x) − K_V(x)| ≤ c_UV for a constant c_UV that depends only on the two machines, not on x. So the complexity of any string is machine-independent up to a fixed additive constant — a constant that becomes negligible for long strings. This makes K an objective property of the string itself, not of any particular computational formalism.

Kolmogorov complexity is **uncomputable**. The proof uses the incompressibility argument: if K were computable, you could enumerate all strings in order of increasing K value and thereby name a very complex string with a short description — a contradiction. This is closely related to the unsolvability of the halting problem you already know: computing K requires deciding whether short programs halt, which is in general undecidable. Kolmogorov complexity is therefore a theoretical tool rather than a practical compression algorithm; its power lies in the arguments it enables, not in computing it directly.

The incompressibility method is one of the most useful proof techniques that Kolmogorov complexity provides. To prove a combinatorial lower bound, you assume for contradiction that all objects of a certain type have a short description, then derive a string that is complex but which the assumption compresses — contradiction. Many lower bounds in combinatorics, data structures, and communication complexity have clean proofs via this method. Kolmogorov complexity also gives a rigorous foundation for randomness: a sequence of bits is random if and only if every prefix has Kolmogorov complexity close to its length, capturing the intuition that random sequences have no exploitable pattern.
