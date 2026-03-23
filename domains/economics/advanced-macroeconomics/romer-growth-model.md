---
id: romer-growth-model
title: Romer's Endogenous Technological Progress Model
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: endogenous-growth-theory
  type: hard
- id: differential-equations-intro
  type: soft
tags:
- innovation
- r&d
- monopolistic-competition
- scale-effects
stage: expert
status: validated
---

# Romer's Endogenous Technological Progress Model

## Core Idea
Romer's model features R&D firms that create new products or improve existing ones, generating increasing returns to scale and sustaining long-run growth. Monopolistic competition in the intermediate goods sector provides profit incentives for innovation while creating efficiency losses from market power and duplication. The model shows how market size, R&D intensity, innovation rates, and human capital jointly determine long-run growth and explains cross-country income differences through R&D investments.

## Questions

```yaml
- question: "In Romer's model, which property of ideas is ESSENTIAL for generating economy-wide increasing returns to scale, even when individual firms face constant returns?"
  type: multiple-choice
  options:
    - "Excludability — patents allow inventors to prevent rivals from using their ideas"
    - "Nonrivalry — an idea can be used simultaneously by any number of firms without being depleted"
    - "Scarcity — the limited supply of good ideas drives up their price and returns"
    - "Embodiment — ideas only generate returns once they are embedded in physical capital"
  answer: 1
  explanation: "Nonrivalry is the key. A blueprint for a better engine can be used by any number of factories at once — using it in one place does not prevent its use elsewhere. This means doubling all rival inputs (labor, capital) while holding the stock of knowledge constant more than doubles output, because knowledge scales with all uses simultaneously. Excludability matters for private incentives (without some ability to profit, no one invests in R&D), but it is nonrivalry that generates the increasing returns. Excludability without nonrivalry — like a physical machine — would not produce economy-wide scale effects."

- question: "In Romer's model, the decentralized economy underinvests in R&D relative to the social optimum. What is the PRIMARY reason?"
  type: multiple-choice
  options:
    - "Researchers lack sufficient human capital and training to perform cutting-edge R&D"
    - "Monopolistic competition in the intermediate sector makes innovation too risky"
    - "Inventors cannot capture the full spillover benefits their ideas generate for future researchers who build on existing knowledge"
    - "Patents expire too quickly, reducing the present value of future profits below the cost of research"
  answer: 2
  explanation: "The market failure is a knowledge spillover. When a researcher invents a new intermediate good, other researchers can build on that idea — learning from it, improving it, combining it with other ideas. The private inventor captures profits only from their own patent, not from the value they add to the entire knowledge stock. Because the social return to R&D exceeds the private return, less R&D is done than would be socially optimal. This externality provides the core theoretical rationale for public subsidies to research."

- question: "In Romer's model, monopolistic competition in the intermediate goods sector is necessary for sustained innovation, because it allows inventors to earn positive profits on their patents."
  type: true-false
  answer: true
  explanation: "This is correct, and it represents a key tension in the model. Monopoly power creates efficiency losses (intermediate goods are priced above marginal cost, so the final goods sector uses fewer inputs than it would under perfect competition). But without monopoly profits, inventors have no private incentive to pay the upfront cost of R&D. Romer's model accepts this inefficiency as the price of sustained innovation — perfect competition would drive profits to zero and eliminate R&D investment."

- question: "In Romer's model, long-run economic growth is ultimately determined by the rate of physical capital accumulation, just as in the Solow model."
  type: true-false
  answer: false
  explanation: "This is the central point of departure from the Solow model. In Solow, long-run growth depends entirely on exogenous technological progress. In Romer, long-run growth is driven by the rate of idea creation — determined by how much human capital the economy allocates to R&D, the productivity of the research sector, and the size of the market. Physical capital accumulation still matters for the level of output, but it is the endogenous innovation rate that determines the long-run growth rate."

- question: "Why are ideas fundamentally different from physical goods like machines or raw materials, and how does this difference generate increasing returns to scale in Romer's model?"
  type: short-answer
  answer: "Physical goods are rival: a machine used in one factory cannot simultaneously operate in another. Ideas are nonrival: a blueprint, formula, or algorithm can be used by any number of producers simultaneously without being depleted. This means that when an economy doubles its physical inputs (labor, capital), output more than doubles if the stock of knowledge also grows — because knowledge scales with every use at once. In Romer's model, knowledge accumulates as R&D produces new blueprints for intermediate goods. More variety of inputs raises total factor productivity, so growth can continue indefinitely without running into diminishing returns, unlike in models with only rival inputs."
  explanation: "The nonrivalry of ideas is the engine of the Romer model. It is what makes the aggregate production function exhibit increasing returns, what makes sustained growth possible without exogenous technological manna, and what creates the market failure (spillovers) that justifies R&D subsidies. The model's central message is that growth is not an accident of nature but a consequence of purposeful human investment in knowledge — and that competitive markets left to themselves will systematically underinvest in it."
```

## Explainer

From endogenous growth theory, you know that long-run growth can arise from decisions within the economy rather than from exogenous technological improvement falling from the sky. Romer's 1990 model makes this concrete by asking: why would anyone invest resources in creating new ideas? The answer hinges on a crucial property of ideas — they are **nonrival**. A blueprint for a better engine can be used by any number of factories simultaneously without being depleted. This nonrivalry means that ideas generate **increasing returns to scale** at the economy-wide level, even if individual firms face constant or diminishing returns. But nonrivalry alone is not enough to motivate private investment. Ideas must also be at least partially **excludable** — inventors need some ability to profit from their creations, or no one would bother doing R&D.

Romer resolves this tension by splitting the economy into three sectors. A **final goods sector** uses labor and a variety of intermediate inputs to produce output under perfect competition. An **intermediate goods sector** consists of firms that each hold a patent on a unique input variety and sell it at a markup — this is where **monopolistic competition** enters. Each intermediate firm faces a downward-sloping demand curve because its product is differentiated, giving it pricing power and positive profits. Those profits are what attract resources into the third sector: the **R&D sector**, which uses human capital to produce new blueprints. When a researcher invents a new variety of intermediate good, they receive a patent and become a monopolist for that variety. The expected present value of future monopoly profits is what compensates them for the cost of research.

The growth mechanism works as follows. More researchers produce more blueprints, which means a greater variety of intermediate inputs available to the final goods sector. Greater variety raises total factor productivity — the economy produces more output from the same labor and capital. This is the "expanding variety" interpretation of technological progress. The steady-state growth rate of the economy depends on how much human capital the economy allocates to R&D versus production, which in turn depends on the size of the market (larger markets mean more profits from each invention), the productivity of the research sector, and the interest rate (which determines how heavily future profits are discounted).

A striking implication is the **scale effect**: larger economies grow faster because a larger market increases the return to inventing. This prediction has generated significant empirical debate, since countries like Luxembourg do not obviously grow slower than the United States. Later models by Jones and others modified Romer's framework to eliminate strong scale effects while preserving endogenous innovation. Nevertheless, Romer's core insight endures — growth is not manna from heaven but the result of purposeful, profit-motivated investment in ideas. The model also reveals a fundamental market failure: because inventors cannot capture all the spillover benefits their ideas create (other researchers build on existing knowledge), the decentralized equilibrium underinvests in R&D relative to the social optimum, providing a rationale for public subsidies to research.
