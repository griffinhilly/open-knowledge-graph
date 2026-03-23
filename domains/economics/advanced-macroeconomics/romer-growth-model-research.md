---
id: romer-growth-model-research
title: Romer Growth Model and R&D-Based Endogenous Growth
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: endogenous-growth-theory
  type: hard
tags:
- romer-model
- research-development
- technological-progress
stage: expert
status: draft
---

# Romer Growth Model and R&D-Based Endogenous Growth

## Core Idea
The Romer model endogenizes technological progress through R&D spending. The economy has a manufacturing sector producing output and an R&D sector producing designs. Sustained growth occurs because knowledge accumulation increases productivity of all future capital, creating a positive externality that drives perpetual growth.

## Questions

```yaml
- question: "A pharmaceutical firm argues it cannot share its drug formula because sharing would eliminate all incentives to invest in research. Which fundamental tension in the Romer model does this argument reflect?"
  type: multiple-choice
  options:
    - "The tradeoff between physical capital investment and consumption in the Solow model"
    - "The tension between dynamic innovation incentives (requiring monopoly pricing) and the static efficiency loss from underuse of nonrival ideas"
    - "The problem of diminishing returns to physical capital that makes long-run growth impossible"
    - "The distinction between exogenous and endogenous technological progress in neoclassical models"
  answer: 1
  explanation: "Ideas are nonrival — once created, they can be used by many firms simultaneously at zero marginal cost. Competitive pricing would drive the price of an idea to zero, eliminating incentives to invest in costly R&D. Patents grant monopoly rights to allow innovators to recoup their investment, but monopoly power restricts access below the socially optimal level. This is the dynamic-incentive vs. static-efficiency tradeoff at the heart of Romer's model and the broader economics of innovation policy."

- question: "Why does the decentralized market outcome in the Romer model result in too little R&D investment relative to the social optimum?"
  type: multiple-choice
  options:
    - "Firms prefer physical capital investment because it offers higher private returns than research"
    - "Patents reduce the profitability of R&D by limiting the time period over which innovators can earn returns"
    - "The private innovator captures only part of the social return from a new idea because each discovery raises the productivity of all future researchers"
    - "Researchers have diminishing marginal utility for discovery, leading them to stop short of the social optimum"
  answer: 2
  explanation: "Each new idea creates a positive externality: it expands the stock of knowledge, making all future R&D more productive ('standing on the shoulders of giants'). The private innovator is compensated only for the value they can capture through patents — the direct private return. The spillover benefit to future researchers is not internalized. Because the social return exceeds the private return, the market supplies less R&D than is socially optimal. This market failure justifies R&D subsidies, public research funding, and other policy interventions."

- question: "In the Romer model, a permanent increase in the fraction of workers employed in R&D leads to a permanently higher long-run economic growth rate."
  type: true-false
  answer: true
  explanation: "This is one of the Romer model's most important departures from the Solow model. In Solow, the long-run growth rate equals the exogenous rate of technological progress (n + g) regardless of policy. In Romer, the growth rate depends on the size of the research workforce and the productivity of the R&D sector — parameters that policy can influence. Shifting more workers into R&D permanently increases the rate at which new ideas are produced, permanently raising the economy's growth rate. Policy has long-run growth effects."

- question: "In the Solow model, a higher savings rate permanently raises the long-run economic growth rate."
  type: true-false
  answer: false
  explanation: "This is a common misconception. In the Solow model, a higher savings rate raises the level of output per capita (by increasing the steady-state capital stock) but not the long-run growth rate. In steady state, the economy grows at the exogenous rate n + g regardless of the savings rate. The Romer model was motivated precisely by this limitation: to explain why some policies genuinely affect growth rates rather than just levels, you need endogenous technological progress."

- question: "Explain why the nonrivalry of ideas — unlike physical capital — enables sustained long-run growth without diminishing returns."
  type: short-answer
  answer: "Physical capital faces diminishing returns: adding one more machine to an already capital-intensive economy adds less output than the previous machine did. Ideas are nonrival — one firm's use of an idea does not prevent another firm from using it simultaneously. When a researcher develops a new idea, it raises the productivity of every other researcher who can build on it, so the R&D sector does not face the same diminishing-returns constraint. Each new idea expands the base from which future ideas are generated, enabling the economy to sustain positive growth indefinitely without an external technology shock."
  explanation: "The nonrivalry of ideas is the structural foundation of endogenous growth theory. Rival goods (machines, labor, land) are depleted or congested by use, creating diminishing returns that pull growth toward zero in the long run. Nonrival goods are not depleted, and — through knowledge spillovers — each unit raises the productivity of all future units. This property alone is what separates Romer-style growth from Solow-style level effects."
```

## Explainer

From your study of endogenous growth theory, you know the core dissatisfaction with the Solow model: long-run growth depends on an exogenous technology parameter that the model itself cannot explain. The Romer model attacks this gap directly by asking where new technology actually comes from. The answer is **purposeful R&D investment** — firms devote real resources (researchers, labs, funding) to producing new ideas, and those ideas become the engine of growth.

The model splits the economy into three sectors. The **final goods sector** uses labor and intermediate capital goods to produce output, much like a standard production function. The **intermediate goods sector** produces differentiated capital inputs — each one protected by a patent purchased from innovators. The **R&D sector** employs researchers who produce new designs (blueprints for novel intermediate goods). When a researcher invents a new design, it enters the stock of knowledge, expanding the variety of intermediate goods available. The critical insight is that this stock of knowledge is **nonrival**: one firm's use of an idea does not diminish another firm's ability to use it. This nonrivalry is what makes sustained growth possible.

The positive externality works through knowledge spillovers. Each new design not only earns its inventor a patent (the private return) but also raises the **productivity of all future researchers** (the social return). The existing stock of ideas A makes the next idea easier to discover — standing on the shoulders of giants. Because of this externality, the decentralized market outcome underinvests in R&D relative to the social optimum. The private innovator captures only a fraction of the total benefit their discovery creates, so too few resources flow into research.

In equilibrium, the growth rate of the economy depends on parameters the model pins down: the size of the research workforce, the productivity of the R&D process, and the degree of knowledge spillovers. Unlike the Solow model, **policy matters for long-run growth** — R&D subsidies, patent protection, and education investments that increase the number of researchers can permanently raise the economy's growth rate. This is the model's most important policy implication: growth is not manna from heaven but the result of incentives, institutions, and deliberate resource allocation toward the production of ideas.

The Romer framework also highlights a deep tension. Nonrival ideas require some form of monopoly power (patents) to incentivize their production, since competitive pricing would drive the price of an idea to its zero marginal cost. But monopoly power creates static inefficiency — the intermediate goods are underproduced relative to the social optimum. This tradeoff between **dynamic incentives for innovation** and **static efficiency in the use of ideas** is fundamental to the economics of growth and intellectual property, and it recurs throughout the innovation policy literature that builds on Romer's foundation.
