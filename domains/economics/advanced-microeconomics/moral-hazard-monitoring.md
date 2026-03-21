---
id: moral-hazard-monitoring
title: Moral Hazard and Incentive Contracting
domain: economics
course: advanced-microeconomics
prerequisites:
- id: nash-equilibrium-microeconomics
  type: hard
- id: profit-maximization-microeconomics
  type: hard
builds-toward:
- principal-agent-contracting
tags:
- contract-theory
- information-asymmetry
- incentives
stage: advanced
status: draft
---

# Moral Hazard and Incentive Contracting

## Core Idea
Moral hazard arises when one party (agent) can take unobserved actions affecting payoffs to another party (principal). The agent has incentive to shirk if effort is unobserved; the principal must design incentives (performance pay, profit-sharing, equity) to motivate effort. Optimal contracts balance incentive provision against risk-sharing given the agent's risk aversion.

## Questions

```yaml
- question: "A risk-neutral agent is offered a contract where she pays the firm a fixed fee upfront and then keeps all the revenue she generates. Why does this 'franchise' contract solve the moral hazard problem?"
  type: multiple-choice
  options:
    - "The fixed fee eliminates earnings risk for the firm, removing the principal's concern about agent behavior."
    - "Bearing all the downside risk makes the agent more cautious and therefore more careful about effort decisions."
    - "The agent keeps all output, so she fully internalizes the return to effort — her incentives align perfectly with the firm's, achieving first-best effort."
    - "Commission contracts make effort directly observable by tying pay to measured output."
  answer: 2
  explanation: "The franchise contract gives the agent the full marginal return on effort: she gets 100% of any additional revenue from working harder. This means her private return to effort equals the social return — she has exactly the same incentive to work hard as if she owned the firm outright. This is the 'selling the firm' solution that achieves first-best. It works only when the agent is risk-neutral, because a risk-neutral agent doesn't demand compensation for bearing income variance. Bearing all the output risk is not a problem for a risk-neutral agent — she values the expected value regardless of its variance."

- question: "A principal discovers she can install monitoring technology that makes agent effort partially observable. How does monitoring affect the optimal contract?"
  type: multiple-choice
  options:
    - "Monitoring has no effect because workers already respond optimally to output-based incentives."
    - "Monitoring allows the principal to offer weaker output-based incentives (more salary, less commission) while maintaining the same effort level, reducing the efficiency cost of moral hazard."
    - "Monitoring eliminates moral hazard entirely, allowing the principal to pay a flat salary with no performance component."
    - "Monitoring reduces agent effort because workers respond negatively to being observed."
  answer: 1
  explanation: "The core tradeoff in moral hazard contracting is incentive provision vs. risk-sharing. Output-based pay incentivizes effort but exposes the risk-averse agent to revenue variance from luck. Monitoring partially substitutes for output-based incentives by making effort itself observable, allowing the principal to reward effort directly rather than just outcomes. This tightens the link between effort and reward without adding output risk, so the optimal contract can reduce the commission rate (less risk for the agent) while keeping incentive compatibility satisfied. Unless monitoring is perfect (effort fully observable), some output-based pay remains optimal — so option C overstates the effect."

- question: "When a principal offers a risk-averse agent a flat salary contract, the moral hazard problem is eliminated because the agent is fully insured against earnings risk."
  type: true-false
  answer: false
  explanation: "A flat salary does eliminate earnings risk — the agent receives the same pay regardless of output. But it also eliminates the incentive to exert costly effort: since pay does not change with performance, the agent's optimal response is to exert the minimum effort. This is precisely the moral hazard problem — the agent's privately optimal behavior diverges from the principal's preferred behavior. Full insurance requires zero incentive power, and zero incentive power guarantees shirking. The flat salary 'solves' the risk problem by creating the effort problem in its most extreme form."

- question: "Relative performance evaluation — comparing an agent's output to that of peers in similar environments — can reduce the cost of incentive provision by filtering out common noise unrelated to any individual's effort."
  type: true-false
  answer: true
  explanation: "If all agents face the same exogenous shocks (market conditions, weather, economic cycle), then comparing Agent A's output to peer outputs subtracts the common noise and isolates the effort signal. The principal can now provide strong incentives tied to relative performance without exposing the agent to variance from factors outside her control. This reduces the risk premium the agent requires, shrinking the efficiency loss from moral hazard. The mechanism only works if agents face correlated noise; if each agent's environment is independent, peer performance conveys no information about another's effort."

- question: "Explain the fundamental tradeoff that prevents first-best outcomes when an agent is risk-averse. Why can't the principal simply offer strong performance pay to eliminate moral hazard?"
  type: short-answer
  answer: "First-best requires aligning the agent's incentives with the firm's — achieved by making pay perfectly tied to output (full commission). But for a risk-averse agent, full commission means bearing all revenue variance, including the portion driven by luck rather than effort. Risk-averse agents demand a risk premium to accept this variance, making the contract costly. The principal's optimal response is to trade off incentive strength for insurance: include a salary component (reducing risk exposure) at the cost of accepting some shirking in equilibrium. The stronger the performance pay, the better the incentives but the higher the risk premium — so the optimal contract balances these two costs. The residual shirking in this second-best contract is the unavoidable cost of moral hazard under risk aversion."
  explanation: "The first-best would require that effort be observable (so the principal pays for effort directly, not outcomes) or that the agent be risk-neutral (so full commission imposes no welfare loss). Neither holds in the canonical moral hazard model. The tension is irreducible: you cannot simultaneously provide full insurance and full incentives for a risk-averse agent. The optimal contract is second-best, and the gap from first-best is the cost of unobservable effort."
```

## Explainer

From Nash equilibrium, you understand strategic interaction where each player optimizes given the other's strategy. From profit maximization, you understand how firms make optimal decisions. **Moral hazard** introduces a twist: what happens when one player's action is hidden from the other? The concept is straightforward — if your boss cannot see whether you are working hard or browsing the internet, you have a temptation to slack off. The deep question is how to design contracts that align incentives when effort is unobservable.

Consider a sales manager (principal) hiring a salesperson (agent). The salesperson can exert high effort (costly, leads to high sales with high probability) or low effort (easy, leads to low sales usually). The manager observes sales revenue but not effort directly. If the manager pays a flat salary, the salesperson has no reason to work hard — she receives the same pay regardless. If the manager pays purely on commission, effort is incentivized but the salesperson bears all the revenue risk, which is inefficient because some variation in sales comes from luck, not effort. The **optimal contract** lies somewhere between these extremes, trading off incentive power against risk exposure.

The formal model captures this tradeoff precisely. The agent chooses effort e to maximize expected utility of compensation minus the cost of effort. The **incentive compatibility constraint** requires that the compensation scheme makes high effort the agent's best response. The **participation constraint** requires that the agent prefers the contract to her outside option. The principal maximizes expected profit subject to both constraints. When the agent is risk-neutral, the solution is simple: sell the agent the firm (or equivalently, pay a franchise fee and let the agent keep all revenue). The agent then fully internalizes the consequences of effort, achieving the **first-best** outcome. But when the agent is risk-averse, full incentive provision requires exposing the agent to too much risk, so the optimal contract dampens incentives to provide insurance — a **second-best** outcome where some shirking occurs in equilibrium.

The gap between first-best and second-best is the **cost of moral hazard** — the efficiency loss from unobservable actions. This cost can be reduced through **monitoring** (making effort partially observable), **relative performance evaluation** (comparing the agent to peers to filter out common noise), or **repeated interactions** (using past performance to infer effort over time). Each of these mechanisms works by tightening the link between effort and measured performance, allowing the principal to provide stronger incentives without imposing as much risk. Understanding this tradeoff is foundational for analyzing employment contracts, insurance design, corporate governance, and any setting where one party's hidden actions affect another's welfare.
