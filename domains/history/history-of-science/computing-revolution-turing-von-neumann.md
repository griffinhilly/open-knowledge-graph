---
id: computing-revolution-turing-von-neumann
title: "The Computing Revolution: From Turing to Stored-Program Computers"
domain: history
course: history-of-science
prerequisites:
- id: enlightenment-science
  type: soft

builds-toward:
- internet-origins-arpanet
- digital-economy-history
tags:
- history
- History Of Science
stage: advanced
status: validated
---

# The Computing Revolution: From Turing to Stored-Program Computers

## Core Idea
Alan Turing's 1936 paper on computable numbers defined a theoretical model of computation (the Turing machine) that established the limits of what could be computed. During WWII, Turing worked on code-breaking at Bletchley Park, and the challenge of breaking the Enigma cipher drove early developments in mechanical computation. After the war, von Neumann, Turing, and others developed the concept of the stored-program computer — a machine that could be reprogrammed by modifying its internal memory rather than its hardware. Early computers (ENIAC, EDVAC) were massive, power-hungry machines. Yet the stored-program architecture established the fundamental principle of modern computing: code and data are both information, stored and manipulated the same way. The history of computing illustrates how abstract mathematical theory (Turing's formalism), military necessity, and engineering ingenuity converged to create a transformative technology.

## Questions

```yaml

- question: "What was the key innovation of the 'stored-program' computer architecture, and who is associated with formalizing it?"
  type: short-answer
  answer: "In earlier machines, programs were represented in hardware — rewiring the machine to change its function. The stored-program architecture, formalized by John von Neumann in his 1945 First Draft of a Report on EDVAC, proposed that instructions (programs) should be stored in the same memory as data, allowing the machine to modify and execute programs dynamically without hardware changes. This made computers general-purpose machines. Von Neumann drew on ideas from Turing, Mauchly, Eckert, and others, and the resulting architecture — CPU, memory, I/O — is still the basis of nearly all modern computers."
  explanation: "The stored-program concept is perhaps the single most important architectural decision in computing history. The question of who deserves credit (Turing, von Neumann, Mauchly and Eckert) is historically contested."

- question: "Alan Turing's 1936 paper introduced the concept of a Turing machine. What was Turing trying to answer with this mathematical construction?"
  type: multiple-choice
  options:
    - "How fast a mechanical calculator could multiply numbers"
    - "Whether it was possible to build a practical electronic computer"
    - "Whether every mathematical problem has a definite procedure for solving it"
    - "How to crack encrypted German military communications"
  answer: 2
  explanation: "Turing's 1936 paper 'On Computable Numbers, with an Application to the Entscheidungsproblem' was responding to David Hilbert's challenge: is there a definite procedure (algorithm) that can decide, for any mathematical statement, whether it is provable? Turing showed the answer was no by defining computation abstractly and proving some problems were undecidable. The Turing machine was a mathematical thought experiment, not a design for a real machine — but it established the theoretical foundations of computer science."

- question: "What was Colossus, and why was its existence kept secret for decades?"
  type: short-answer
  answer: "Colossus was an electronic programmable computer built at Bletchley Park in 1943-1944 to help crack German Lorenz cipher messages. It used vacuum tubes to process encrypted teleprinter traffic at electronic speeds. Colossus is arguably the world's first operational electronic computer. Its existence was kept secret under the British Official Secrets Act until the 1970s because the cryptographic techniques it embodied — and the fact that Britain could read German high-command communications — remained strategically sensitive. This secrecy meant that its inventors (Tommy Flowers and colleagues) received no recognition during the postwar computing boom."
  explanation: "The secrecy around Colossus meant that US computers like ENIAC (1945) and EDVAC were long credited as the first electronic computers, when Colossus arguably preceded them by years."

- question: "ENIAC, completed in 1945, was the world's first electronic general-purpose computer."
  type: true-false
  answer: false
  explanation: "ENIAC was not fully general-purpose in the modern sense — its programs were initially set by rewiring, not stored-program. Colossus preceded it by two years. And whether any particular machine deserves the title 'first computer' depends on how 'computer' is defined. What ENIAC did represent was massive scale: 18,000 vacuum tubes, 30 tons, filling a large room. The stored-program architecture came later with EDVAC and the Manchester Baby (1948)."

- question: "How did Alan Turing's wartime work at Bletchley Park connect to the development of modern computing?"
  type: short-answer
  answer: "At Bletchley Park, Turing helped design the 'Bombe' — an electromechanical machine that exploited cribs (known plaintext) to narrow the search space for Enigma settings. This work was not fully electronic and is distinct from later stored-program computers, but it demonstrated the practical power of Turing's abstract computational thinking: logical analysis of cipher structure could be mechanized. The experience also convinced Turing and colleagues that electronic computation was feasible and valuable. After the war, Turing worked on the ACE (Automatic Computing Engine) at the National Physical Laboratory and contributed to the Manchester computing project."
  explanation: "Turing's career is a remarkable thread connecting pure mathematical logic (1936), wartime code-breaking (1939-1945), and postwar computer design (1945-1954). His prosecution and death from cyanide poisoning in 1954 — the result of chemical castration ordered by British courts after a conviction for homosexuality — came before he received any public recognition for his wartime work."

```

## Explainer

The computing revolution traces two converging paths: one through abstract mathematical logic, the other through wartime engineering necessity.

Alan Turing's 1936 paper 'On Computable Numbers' was not about engineering at all. It was a contribution to the mathematical foundations controversy — specifically, an attempt to answer David Hilbert's question whether there exists a definite procedure for deciding the truth of any mathematical statement. Turing answered no, by defining a mathematical abstraction — the Turing machine — and proving that some problems could not be solved by any such machine. The Turing machine was a thought experiment: an infinitely long tape, a read/write head, and a finite set of states. Its importance was theoretical: it defined, for the first time, what computation was. Any computation that can be performed at all can be described as a Turing machine computation.

The engineering path converged with the mathematical one during WWII. German forces used Enigma cipher machines whose settings were reset daily; German high command used a more complex system called Lorenz. At Bletchley Park, Turing helped design the 'Bombe,' an electromechanical machine that systematically tested Enigma configurations. Tommy Flowers and colleagues built Colossus (1943-1944), an electronic programmable machine that attacked Lorenz cipher traffic. Colossus used vacuum tubes — much faster than electromechanical components — and was arguably the first electronic programmable computer. Its existence was kept secret under the Official Secrets Act until the 1970s.

In the United States, ENIAC (Electronic Numerical Integrator and Computer), completed in 1945 by Mauchly and Eckert at the University of Pennsylvania, was 18,000 vacuum tubes and 30 tons. But its programs were set by rewiring. The crucial conceptual step came in John von Neumann's 1945 report on EDVAC: the stored-program architecture, in which instructions and data both lived in the same memory, allowing the machine to be reprogrammed without hardware changes. This was the fundamental insight of modern computing — programs are data, and a computer that can process data can process and execute programs. The Manchester Mark 1 (1949) was among the first operational stored-program computers.

The history illustrates how abstract theory, military urgency, and engineering ingenuity converged. No single person invented the computer; the invention was distributed, contested, and shaped by war. Turing himself received no public recognition during his lifetime — prosecuted for homosexuality in 1952, subjected to chemical castration, dead by 1954. The computing revolution's origins are inseparable from both intellectual brilliance and historical injustice.
