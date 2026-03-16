---
id: financial-system-interconnectedness
title: Financial System Interconnectedness and Systemic Risk
domain: economics
course: financial-economics
prerequisites:
- id: leverage-and-margin-trading
  type: soft
- id: credit-risk-and-default
  type: soft
tags:
- systemic-risk
- interconnectedness
- crises
stage: formal-systems
status: draft
---

# Financial System Interconnectedness and Systemic Risk

## Core Idea
Systemic risk arises from interconnectedness among financial institutions and markets. When one institution fails, contagion spreads through credit exposures, asset fire sales, and funding channels. Macroprudential policies and regulation aim to reduce systemic fragility, but interconnectedness-risk tradeoffs remain fundamentally unresolved.

## Explainer

From your prerequisites on leverage and credit risk, you know two key facts: leverage amplifies both gains and losses (a 10-to-1 leveraged firm is wiped out by a 10% fall in asset values), and credit risk means counterparties may not pay what they owe. Financial system interconnectedness is what happens when these individual-level risks become entangled across a web of institutions. A failure at one node can cascade to others in ways that individually prudent risk management cannot prevent, because each firm's safety depends partly on the health of its counterparties.

Think of the financial system as a network: nodes are banks, insurers, hedge funds, and money market funds; edges are bilateral obligations — loans, derivatives contracts, repo agreements, interbank deposits. In normal times, this interconnectedness is valuable. It distributes risk to those best able to bear it, provides liquidity, and enables efficient credit markets. But it creates **systemic fragility** that emerges from the aggregate rather than from any individual institution. A bank that appears solvent in isolation may become insolvent if several of its counterparties fail simultaneously. The riskiness of any one institution depends on the health of the entire network — a fact that individual balance sheet analysis cannot capture.

The **contagion channels** are distinct and can reinforce each other. **Direct exposure** is the most obvious: if Firm A holds Firm B's bonds and B defaults, A takes an immediate loss. **Fire sale contagion** is subtler: a distressed firm forced to liquidate assets quickly depresses prices, and other firms holding similar assets suffer mark-to-market losses, triggering their own margin calls, forcing further sales — a price spiral that spreads losses even to firms with no direct exposure to the failed institution. **Funding runs** occur when short-term lenders refuse to roll over overnight or weekly financing to any institution perceived as risky, forcing sudden deleveraging across the system. The 2008 crisis operated through all three simultaneously: Lehman's failure froze money markets (funding), bank assets fell (fire sales), and credit chains snapped (direct exposure).

**Macroprudential regulation** addresses systemic risk that individual institutions cannot internalize. Each bank, acting rationally in its own interest, may hold less capital than is socially optimal, because the cost of its failure is partly borne by the system — a classic negative externality. Regulatory responses include capital surcharges on systemically important financial institutions (SIFIs), stress tests that model correlated failures across institutions, and mandatory central clearing of derivatives contracts to reduce the opacity and complexity of the counterparty web. But the fundamental tension remains: the interconnectedness that creates systemic risk is also what enables efficient risk-sharing and credit allocation. Reducing it involves real costs.

The empirical measurement of interconnectedness uses network analysis: researchers map bilateral exposure matrices among large institutions and compute centrality measures (which nodes are most connected), clustering coefficients (are my counterparties also connected to each other?), and contagion simulations under various failure scenarios. A key insight is that "too big to fail" often understates the problem — it is more precisely "**too interconnected to fail**." A mid-size institution with tentacles into hundreds of counterparties via derivatives and repo can be more systemically dangerous than a larger institution with concentrated, transparent exposures. Size and interconnectedness are related but distinct dimensions of systemic importance.
