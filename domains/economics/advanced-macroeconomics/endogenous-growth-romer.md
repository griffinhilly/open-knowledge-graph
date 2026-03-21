---
id: endogenous-growth-romer
title: 'Endogenous Growth Theory: Romer Model'
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: steady-state-analysis-growth
  type: hard
- id: externalities-and-market-failure
  type: hard
- id: differential-equations-intro
  type: soft
builds-toward:
- endogenous-growth-lucas
- ak-model-endogenous-growth
tags:
- growth
- endogenous
- innovation
stage: advanced
status: draft
---

# Endogenous Growth Theory: Romer Model

## Core Idea
Romer's model breaks the exogeneity of technological progress by making the rate of innovation endogenous to economic incentives, particularly R&D investment. The model features a separate R&D sector where firms create new varieties of intermediate goods. Because ideas have public good properties and imperfect excludability, the economy can sustain positive long-run growth without population growth, with sustained increases in living standards driven by intentional innovation rather than exogenous technological manna.

## Questions

```yaml
- question: "In the Solow model, long-run growth in output per worker eventually halts unless an external factor is assumed. Romer's model avoids this fate primarily because:"
  type: multiple-choice
  options:
    - "Romer assumes a higher savings rate, which sustains capital accumulation indefinitely"
    - "Ideas are non-rival — using a design doesn't deplete it — so including knowledge in the production function creates increasing returns to scale that offset diminishing returns to capital"
    - "Romer assumes population growth, which keeps labor supply expanding and prevents stagnation"
    - "Romer eliminates the steady state by assuming constant marginal product of capital"
  answer: 1
  explanation: "The Solow model hits diminishing returns because doubling physical inputs (capital, labor) exactly doubles output — constant returns — and capital eventually accumulates to its steady-state level where investment just replaces depreciation. Romer's key insight is that ideas are non-rival: a design used in one factory can simultaneously be used in another. Including the stock of knowledge in the aggregate production function creates increasing returns to scale, which sustains long-run growth indefinitely as the knowledge stock expands."

- question: "In Romer's model, patents create temporary monopoly rights for innovators. A critic argues this is welfare-reducing because monopoly prices restrict output. Which response best captures the Romer-model counterargument?"
  type: multiple-choice
  options:
    - "Monopoly prices are actually efficient because they reflect the true social value of knowledge"
    - "Patents are unnecessary — innovators are motivated by fame and professional recognition, not profit"
    - "Without partial excludability through patents, no firm could earn a return on R&D investment and innovation would collapse; the static deadweight loss of monopoly is the price of sustaining dynamic innovation"
    - "Patents are bad policy in the model; the optimal solution is public ownership of all research"
  answer: 2
  explanation: "Romer's model acknowledges the tension: ideas are non-rival (should be freely shared) but require excludability (to give innovators an incentive to create them). Patents are a second-best solution — they create static monopoly distortions but solve the appropriability problem that would otherwise make private R&D investment zero. The model actually predicts *too little* innovation even with patents, because innovators cannot capture all the social spillovers their ideas create. The correct policy is not to eliminate patents but to supplement them with R&D subsidies."

- question: "In the Romer model, the economy exhibits increasing returns to scale at the aggregate level even though individual sectors have constant or diminishing returns."
  type: true-false
  answer: true
  explanation: "Each individual production function (final goods, intermediate goods) exhibits constant returns to scale in its physical inputs. But when knowledge is included alongside capital and labor in the aggregate picture, doubling all inputs — including the stock of ideas — more than doubles output. This is because ideas are non-rival: the same blueprint can be replicated across all producers simultaneously, unlike physical capital. The increasing returns at the aggregate level is precisely what sustains long-run growth in the Romer model."

- question: "The Romer model predicts that the market equilibrium produces the socially optimal level of innovation, since private R&D firms are rewarded through patent monopoly profits."
  type: true-false
  answer: false
  explanation: "Even with patents, the market produces *too little* innovation relative to the social optimum. This is because each new idea generates positive spillovers for future researchers — it expands the knowledge base from which new innovations are produced — but the innovating firm cannot capture this social value through its monopoly profits alone. The divergence between private return and social return to R&D is a market failure that Romer's model makes precise, providing a rigorous justification for R&D subsidies and public basic research funding."

- question: "Why does the non-rivalry of ideas imply that private markets will underinvest in R&D, even when innovators can patent their discoveries?"
  type: short-answer
  answer: "Non-rivalry means a new idea immediately becomes part of the public stock of knowledge that all future researchers build on — each idea raises the productivity of all subsequent R&D. The innovating firm captures only the private monopoly profit from its specific patent, not the value it creates for the entire future innovation stream. Since the social return to innovation exceeds the private return by the amount of these knowledge spillovers, private markets equate private marginal benefit to marginal cost and produce less R&D than would maximize social welfare."
  explanation: "This is the core market failure in Romer's model: R&D has positive externalities that are not internalized by the market. Patents improve appropriability but cannot capture the full social spillover value of new knowledge. The implication is that even perfectly competitive R&D markets with strong patent protection will systematically underinvest, justifying public subsidies to close the gap between private and social returns."
```

## Explainer

From your study of steady-state growth analysis and market failures, you know two things that set up Romer's contribution. First, in the Solow model, long-run growth in output per worker comes entirely from technological progress — but that progress is assumed to fall from the sky at a constant rate, with no explanation of where it comes from or why it varies across countries. Second, you know that externalities cause markets to deviate from social optimality. Romer's 1990 model connects these ideas: technological progress is the result of deliberate, profit-motivated investment in research, and because knowledge has externality-like properties, the market produces a suboptimal amount of it.

The model divides the economy into three sectors. The **final goods sector** uses labor and a variety of intermediate inputs to produce output, with a production function that exhibits diminishing returns to each individual input but constant returns overall. The **intermediate goods sector** consists of monopolistically competitive firms, each producing a unique variety of intermediate good using a patented design. The **R&D sector** employs researchers who combine existing knowledge with their own effort to produce new designs — blueprints for new intermediate good varieties. When a new design is invented, it is patented, and the inventor earns monopoly profits from licensing it to an intermediate goods producer. These expected profits are what motivate R&D investment in the first place.

The crucial economic property of ideas is **non-rivalry**: using a blueprint to produce one unit of an intermediate good does not prevent someone else from using the same blueprint simultaneously. This distinguishes ideas from physical capital — a machine can only be in one factory at a time, but a design can be replicated infinitely at near-zero marginal cost. Non-rivalry means that the production function for the economy as a whole exhibits **increasing returns to scale** when you include knowledge alongside labor and capital. This is what breaks the Solow model's prediction of convergence: countries that invest more in R&D generate more ideas, which raise productivity, which funds more R&D, sustaining growth indefinitely without the diminishing returns that eventually choke off capital accumulation.

However, non-rivalry creates a problem: if ideas were also non-excludable (freely available to everyone), no firm could earn a return on R&D investment, and no one would bother innovating. Romer resolves this with **partial excludability** through patents — innovators get temporary monopoly rights over their designs, earning enough profit to justify the R&D cost, even though the knowledge eventually diffuses. The policy implications are profound. Because private R&D decisions do not account for the positive spillovers that new knowledge creates for future researchers, the market equilibrium involves too little innovation relative to the social optimum. This provides a rigorous justification for R&D subsidies, patent protection, and public funding of basic research — not as ad hoc interventions but as corrections for a well-defined market failure at the heart of economic growth.
