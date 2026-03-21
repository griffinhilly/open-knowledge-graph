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

## Questions

```yaml
- question: "A risk-averse employee is hired to manage a project whose outcome depends partly on effort and partly on random market conditions. Compared to a first-best contract (where effort is observable), the second-best contract (where effort is hidden) will:"
  type: multiple-choice
  options:
    - "Pay the employee a fixed wage, because outcome-based pay is too complex to implement"
    - "Pay more on average, because the employee must be compensated for bearing the outcome risk that incentivizes effort"
    - "Achieve the same expected surplus for the principal, since the employee will still exert high effort"
    - "Always result in low effort, because hidden effort can never be incentivized by contracts"
  answer: 1
  explanation: "To induce effort when it is unobservable, the principal must tie pay to outcomes, which are only an imperfect signal of effort. Exposing a risk-averse employee to outcome risk imposes a cost on them — they require a risk premium (higher average pay) to accept the uncertain contract over a safe one. This risk premium is an additional cost the principal must bear, making the second-best contract more expensive than the first-best. Hidden effort is incentivizable, but only at a real cost — the classic tradeoff."

- question: "According to the informativeness principle, when should a principal include an additional signal in a compensation contract?"
  type: multiple-choice
  options:
    - "Only when that signal directly and accurately measures the agent's final output"
    - "Whenever the signal is informative about the agent's effort, even if unrelated to output"
    - "Only when the agent agrees the signal is a fair measure of their performance"
    - "Only when measuring the signal is costless to the principal"
  answer: 1
  explanation: "The informativeness principle says that any observable signal providing statistical information about the agent's effort — even a tangential one — should be incorporated into the optimal contract. Adding an informative signal lets the principal better separate effort from luck, reducing the noise in the incentive scheme and allowing a lower risk premium. This explains real-world practices like relative performance evaluation (comparing an executive to industry peers) and multi-metric bonuses: each additional signal narrows the gap between second-best and first-best outcomes."

- question: "In a moral hazard model, using stronger pay-for-performance incentives to better motivate a risk-averse agent always reduces the total cost of the contract to the principal."
  type: true-false
  answer: false
  explanation: "This reverses the key tradeoff. Stronger incentives do motivate more effort, but they simultaneously expose the risk-averse agent to more outcome variance, requiring a higher risk premium. Beyond the optimal incentive intensity, the additional risk premium costs more than the value of the extra effort it extracts. The second-best contract balances these two forces; it does not maximize incentive strength."

- question: "Moral hazard imposes a real cost on the principal — the second-best outcome is strictly worse for the principal than the first-best, even when the optimal contract is used."
  type: true-false
  answer: true
  explanation: "This is the fundamental result of the principal-agent model with hidden action. Information asymmetry has a genuine economic cost: the principal cannot achieve the efficient outcome that would be possible if effort were observable. The gap between first-best and second-best reflects the cost of providing incentives to a risk-averse agent — it exists even with the most cleverly designed contract. This is why firms invest in monitoring, reporting systems, and performance metrics: each imperfect signal of effort partially closes the gap."

- question: "Why is it impossible to achieve the first-best outcome when the agent's effort is hidden, even if the principal offers the agent very generous compensation?"
  type: short-answer
  answer: "Under hidden effort, any contract must base pay on observable outcomes rather than effort directly. To induce the agent to choose high effort, the contract must make high-effort the individually optimal choice — but since outcomes are noisy signals of effort, achieving this requires exposing the risk-averse agent to outcome risk, which demands a risk premium. A fixed generous wage removes the risk but also removes the incentive to exert effort. You cannot simultaneously provide insurance (fixed pay) and incentives (variable pay tied to outcomes) — the two goals are in tension, and the information friction makes this tradeoff unavoidable."
  explanation: "The first-best requires both efficiency (right effort level) and optimal risk sharing (risk-averse agent bears no risk). With observable effort, a fixed wage achieves both. With hidden effort, any incentive-compatible contract that induces high effort must expose the agent to risk, violating optimal risk sharing and requiring a premium. The cost of this premium is the social cost of the information asymmetry — it is not merely distributional but represents destroyed value."
```

## Explainer

Consider hiring a contractor to renovate your kitchen. You care about the quality of the result, but you cannot watch them work every hour of every day. The contractor can exert high effort (careful craftsmanship, quality materials) or low effort (cutting corners, rushing). High effort is costly and unpleasant for the contractor but produces better outcomes for you. The outcome you observe — the finished kitchen — depends on both effort *and* luck (supply delays, hidden structural problems). This is the **moral hazard** problem: the agent's effort is hidden, and the principal can only observe a noisy signal of it.

If you could observe effort directly, the solution would be simple: pay the contractor a fixed wage conditional on high effort, and both parties share no risk. This is the **first-best** outcome. But with hidden effort, a fixed wage gives the contractor no reason to work hard — they get paid regardless. You must instead link compensation to the observable outcome, which does correlate with effort even if imperfectly. The challenge is that the contractor is **risk-averse** (from your prerequisites on probability and expected utility), so tying pay to uncertain outcomes imposes a cost on them. They would demand a higher average payment to accept a risky contract than a safe one. This is the **risk premium** — the extra cost the principal bears for using outcome-based incentives.

The optimal contract balances two forces. Stronger incentives (steeper pay-for-performance) better motivate effort but impose more risk on the agent, requiring a larger risk premium. Weaker incentives reduce risk costs but allow more shirking. The **second-best** contract — the best achievable under moral hazard — solves this tradeoff using the tools of constrained optimization you know from Lagrangian methods. The principal maximizes expected profit subject to two constraints: the **participation constraint** (the agent must prefer this contract to their outside option) and the **incentive compatibility constraint** (the agent must prefer high effort to low effort given the contract's payment structure).

The key result is that the second-best outcome is strictly worse for the principal than the first-best. Information friction has a real cost. The **informativeness principle** sharpens this: the optimal contract should use any observable signal that is informative about effort, even if it is not directly related to output. If a supervisor's report or a co-worker's performance provides additional information about whether the agent worked hard, incorporating it into the contract reduces the noise in the incentive scheme and lowers the risk premium. This principle explains real-world practices like relative performance evaluation, team-based bonuses, and the use of multiple metrics in executive compensation — each additional informative signal allows the principal to better separate effort from luck, narrowing the gap between the first-best and second-best outcomes.
