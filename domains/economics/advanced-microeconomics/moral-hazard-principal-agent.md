---
id: moral-hazard-principal-agent
title: Moral Hazard and the Principal-Agent Problem
domain: economics
course: advanced-microeconomics
prerequisites:
- id: incentive-compatibility-constraints
  type: hard
- id: constrained-optimization-lagrange
  type: soft
- id: probability-theory
  type: hard
- id: game-theory-basics-microeconomics
  type: hard
tags:
- contract-theory
- information-asymmetry
stage: advanced
status: draft
---

# Moral Hazard and the Principal-Agent Problem

## Core Idea
Moral hazard arises when the principal cannot observe the agent's effort. The agent, knowing effort is unobserved, may shirk. The principal must tie compensation to observable outcomes to induce effort. This creates a fundamental tradeoff: incentivizing effort requires exposing the risk-averse agent to outcome risk, reducing their welfare and imposing a cost of imperfect information.

## Explainer

Consider hiring a contractor to renovate your kitchen. You care about the quality of the result, but you cannot watch them work every hour of every day. The contractor can exert high effort (careful craftsmanship, quality materials) or low effort (cutting corners, rushing). High effort is costly and unpleasant for the contractor but produces better outcomes for you. The outcome you observe — the finished kitchen — depends on both effort *and* luck (supply delays, hidden structural problems). This is the **moral hazard** problem: the agent's effort is hidden, and the principal can only observe a noisy signal of it.

If you could observe effort directly, the solution would be simple: pay the contractor a fixed wage conditional on high effort, and both parties share no risk. This is the **first-best** outcome. But with hidden effort, a fixed wage gives the contractor no reason to work hard — they get paid regardless. You must instead link compensation to the observable outcome, which does correlate with effort even if imperfectly. The challenge is that the contractor is **risk-averse** (from your prerequisites on probability and expected utility), so tying pay to uncertain outcomes imposes a cost on them. They would demand a higher average payment to accept a risky contract than a safe one. This is the **risk premium** — the extra cost the principal bears for using outcome-based incentives.

The optimal contract balances two forces. Stronger incentives (steeper pay-for-performance) better motivate effort but impose more risk on the agent, requiring a larger risk premium. Weaker incentives reduce risk costs but allow more shirking. The **second-best** contract — the best achievable under moral hazard — solves this tradeoff using the tools of constrained optimization you know from Lagrangian methods. The principal maximizes expected profit subject to two constraints: the **participation constraint** (the agent must prefer this contract to their outside option) and the **incentive compatibility constraint** (the agent must prefer high effort to low effort given the contract's payment structure).

The key result is that the second-best outcome is strictly worse for the principal than the first-best. Information friction has a real cost. The **informativeness principle** sharpens this: the optimal contract should use any observable signal that is informative about effort, even if it is not directly related to output. If a supervisor's report or a co-worker's performance provides additional information about whether the agent worked hard, incorporating it into the contract reduces the noise in the incentive scheme and lowers the risk premium. This principle explains real-world practices like relative performance evaluation, team-based bonuses, and the use of multiple metrics in executive compensation — each additional informative signal allows the principal to better separate effort from luck, narrowing the gap between the first-best and second-best outcomes.
