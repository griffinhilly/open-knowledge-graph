---
id: second-law-thermodynamics-entropy
title: Second Law of Thermodynamics and Entropy
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: second-law-of-thermodynamics
  type: hard
builds-toward:
- entropy-calculation-properties
- exergy-concept-availability
- refrigeration-thermodynamic-analysis
tags:
- second-law
- entropy
- irreversibility
stage: advanced
status: draft
---

# Second Law of Thermodynamics and Entropy

## Core Idea
Entropy S is a state property measuring disorder or irreversibility; the second law states entropy of an isolated system never decreases. For reversible (ideal) processes, entropy is constant; for irreversible processes, entropy generation S_gen > 0. Engineering irreversibilities include friction, turbulence, throttling, and non-ideal heat transfer; quantifying entropy generation reveals where inefficiencies occur.

## How It's Best Learned
Calculate entropy generation for simple processes (throttling, mixing, friction) to build intuition about which real phenomena create irreversibility. Use the T ds Gibbs equations to relate entropy changes to measurable properties (T, P, v). Understand that entropy is a state function, so entropy change depends only on initial and final states, not the path.

## Common Misconceptions
- Entropy always increases in any process; it increases for isolated systems but can decrease for open systems that reject heat.
- Entropy generation S_gen is always positive; reversible processes have S_gen = 0 as a theoretical ideal.
- Entropy is only relevant to spontaneity; entropy generation quantifies lost work opportunity and is central to efficiency analysis.
