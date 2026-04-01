---
id: information-flow-security
title: Information Flow Security
domain: computer-science
course: formal-methods
prerequisites:
- id: type-systems-overview
  type: hard
- id: operational-semantics
  type: soft
- id: predicate-logic-introduction
  type: soft
builds-toward: []
tags:
- information-flow
- noninterference
- data-flow-analysis
- taint-analysis
- multi-level-security
- covert-channels
stage: expert
status: validated
---

# Information Flow Security

## Core Idea

Information flow security analyzes how data flows through a program to prevent unauthorized information leakage. The central property is **noninterference**: if two executions differ only in a secret input, their observable outputs should be identical (secrets don't interfere with public behavior). Approaches include: **static analysis** (tracking data dependencies to detect where secrets flow), **type-based enforcement** (assigning security labels to data, with type rules preventing secret data from leaking to public channels), and **dynamic monitoring** (tainting data as it flows and preventing tainted data from reaching public outputs). Information flow analysis detects subtle security vulnerabilities like timing attacks (program execution time depends on secrets) and side-channel attacks (memory access patterns leak information). The framework is foundational to computer security, applying to both software security (protecting passwords, encryption keys) and privacy (preventing unauthorized access to personal data).

## Questions

```yaml
- question: "Noninterference is a fundamental security property defined as: if two executions differ only in a secret input S, their observable outputs should be identical. Why is this a strong security guarantee?"
  type: short-answer
  answer: "Noninterference ensures that secrets have no causal effect on observables. If an attacker can observe outputs, the outputs tell the attacker nothing about the secret (since changing the secret doesn't change observables). This rules out all information leakage through normal channels: the attacker cannot infer secrets from program behavior, output timing, memory consumption, or any observable effect. Noninterference is the gold standard of information flow security because it's composable (if A doesn't interfere with B and B doesn't interfere with C, then A doesn't interfere with C) and proof of noninterference guarantees secrecy."
  explanation: "Noninterference is stronger than typical security definitions because it considers the absence of information as a positive property. Many programs don't leak secrets through their outputs but leak through side channels (timing, power consumption). Noninterference captures all these by saying: any difference in observables that could allow an attacker to infer information about secrets is forbidden. Proving noninterference rigorously is hard, which is why static and dynamic analysis tools approximate it."

- question: "Taint analysis tracks the flow of sensitive data (taints) through a program. If a password string P is tainted, and the program computes H = hash(P), is H tainted?"
  type: multiple-choice
  options:
    - "Yes, H is tainted because it depends on P"
    - "No, H is untainted because hash is a one-way function"
    - "It depends on the analysis. Conservative taint analysis marks H as tainted (information from P flows to H). However, if the analysis understands that hash is cryptographically secure, it might mark H as untainted because the hash doesn't leak information about P"
    - "Taint analysis cannot handle hash functions"
  answer: 2
  explanation: "Taint analysis is a conservative approximation to noninterference: track data dependencies. If H depends on P (even transitively through hash), H is tainted. This is conservative (may mark data as tainted even if it's cryptographically safe) but effective at catching obvious leaks. Sophisticated analyses (like those in Android security or JavaScript sandboxing) understand cryptographic functions and skip tainting their outputs. The question highlights that taint analysis is a practical approximation to the theoretical ideal (noninterference) but with engineering pragmatism."

- question: "Type-based information flow security assigns security labels to data (e.g., Secret, Public) and enforces that Secret data never reaches Public outputs. A program reads a password P (Secret) and checks if P == 'admin'. This produces a boolean result. Should the result be labeled Secret or Public?"
  type: short-answer
  answer: "The result should be labeled Secret because it depends on the secret password. Even though the result is a boolean (not the password itself), it reveals information: if the result is true, the attacker learns the password is 'admin'. Type-based enforcement would raise an error if this boolean is used to determine a public output (e.g., 'access granted' message). The program would need to ensure the comparison result stays secret throughout its execution. This is a subtle but critical aspect of information flow typing: the type system prevents derived information from leaking, not just the original secret."
  explanation: "This is where information flow security gets subtle. A comparison result is 'derived secret' — it doesn't contain the original secret but reveals something about it. Type-based enforcement must propagate this: if a value depends on secrets, it is tainted/labeled secret, and cannot reach public outputs. The type system enforces this globally, preventing the most insidious bugs where secrets leak through derived values."

- question: "Timing attacks exploit information leaks through execution time. A password checker loop terminates early if the password is wrong but runs longer for correct passwords (checking all characters). How can information flow analysis detect this vulnerability?"
  type: short-answer
  answer: "The program's execution time depends on the secret password. Information flow analysis detects this by tracking data dependencies: the loop termination condition depends on the password (secret). If the execution time is observable (it is — an attacker can measure it), then the execution time correlates with the secret, violating noninterference. Information flow analysis would flag this as an error: the program's control flow (whether the loop continues) depends on secrets, and control flow determines timing, which is observable. To fix this, the program should always check all characters (constant-time comparison) so timing is independent of the password."
  explanation: "Timing attacks are a classic example of side-channel information leakage. The secret (password) is never explicitly leaked, but its effect on timing allows attackers to infer it. Information flow analysis catches this by recognizing that control flow depending on secrets leads to timing-dependent behavior. This is particularly important for cryptographic code, where constant-time operations are mandatory. Some languages (like Rust) provide constant-time cryptographic libraries; information flow analysis can verify that programs use them correctly."
```

## Explainer

Most security focuses on preventing direct access to secrets: lock passwords in files, encrypt data in transit. But secrets can leak through information flow — the paths data takes through computation. A program might never explicitly output a password but might leak it through timing, memory access patterns, or inferred values. **Information flow security** detects and prevents these leaks.

**Noninterference: The Ideal**

The gold standard of information flow security is **noninterference**: an attacker observing the program's outputs learns nothing about secrets. Formally, if two executions differ only in secret inputs, their observable outputs are identical. Noninterference is powerful: it rules out all possible information leakage through observable channels (outputs, timing, resources). But proving noninterference is hard, requiring global analysis of the entire program. Practical techniques approximate noninterference using static and dynamic analysis.

**Static Analysis: Data Dependency Tracking**

One approach is **taint analysis**: mark sensitive data as "tainted," track how it flows through the program, and flag any flow to public outputs. If a password P is tainted and a comparison `if (P == "admin")` produces a boolean B, then B is tainted (it depends on the secret). If B is used to print "access granted," the analysis flags an error: tainted data reaches public output.

Taint analysis is conservative — it marks data as tainted if it depends on secrets, even if the dependence is cryptographically secure (e.g., hash functions). But this conservatism is practical: it catches obvious leaks. Sophisticated analyses refine this by understanding special operations (cryptographic functions, error correction codes) that break the taint propagation.

**Type-Based Enforcement**

A more principled approach is **type-based information flow**: assign **security labels** to all data (Secret, Public, or a lattice of levels like {Public < Confidential < Secret}). Type rules enforce that operations on labeled data preserve security properties. A function accepting both Public and Secret inputs requires its output type to be Secret (information from Secret inputs contaminates the output). A function that only reads Public inputs can safely output Public.

The type checker verifies globally that Secret data never flows to Public outputs. This provides compile-time guarantees of noninterference without runtime monitoring. Languages like Jif (Java Information Flow) and LIO (Liquid Information Flow) implement this, allowing programmers to write secure code with precise security guarantees.

**Dynamic Monitoring**

Type-based enforcement is static and conservative. **Dynamic information flow** monitors data at runtime, tainting data that flows from secrets and preventing tainted data from leaving the system. Android's information flow framework uses dynamic taint analysis to track sensitive data (phone numbers, contacts) and prevent unauthorized sharing. The advantage of dynamic analysis is accuracy: you know exactly what data actually flowed, not a conservative over-approximation. The disadvantage is runtime overhead and the inability to catch errors before deployment.

**Covert Channels and Timing Attacks**

Explicit data flow (variable assignments) is only one path for information leakage. **Covert channels** leak information through indirect means:

1. **Timing channels**: Program execution time depends on secrets (e.g., password checker exits early on mismatch). An attacker measures timing and infers secrets.
2. **Power channels**: Power consumption during execution depends on data; monitoring power reveals information.
3. **Cache channels**: Memory access patterns affect CPU caches; cache timing attacks infer accessed data.

Information flow analysis can detect timing channels by checking whether control flow depends on secrets. If a secret value determines which branch executes, execution time will differ, creating a timing channel. To prevent this, the program must use **constant-time operations** — operations whose execution time is independent of secret inputs.

**Practical Applications**

- **Cryptographic libraries**: Ensuring constant-time implementations to prevent timing attacks. Formal verification can prove a cryptographic function's execution time is independent of its secret key.
- **Android security**: Tracking sensitive data (contacts, location, microphone) through the system and preventing unauthorized leakage.
- **JavaScript sandbox**: Preventing scripts in one origin from accessing data from another origin through information channels.
- **Database security**: Enforcing that queries don't leak information about secret data (e.g., timing-based inference attacks on encrypted databases).

**Research Frontiers**

Current challenges include: (1) handling implicit flows (control flow depending on secrets), (2) reasoning about probabilistic information leakage (leaking partial information is sometimes acceptable), (3) scaling to complex systems with many interacting components, (4) handling cryptographic functions and their non-leakage properties. The field is maturing from academic theory to practical tools (Rust cryptographic libraries with constant-time guarantees, JavaScript isolation guarantees), and information flow analysis is becoming standard in security-critical software development.
