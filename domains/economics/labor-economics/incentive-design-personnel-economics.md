---
id: incentive-design-personnel-economics
title: Incentive Design and Personnel Economics
domain: economics
course: labor-economics
prerequisites:
- id: wage-determination
  type: hard
- id: labor-demand-theory
  type: hard
- id: principal-agent-contracting
  type: soft
- id: moral-hazard
  type: soft
tags:
- personnel-economics
- Lazear
- piece-rates
- performance-pay
- tournaments
- efficiency-wages
- deferred-compensation
stage: advanced
status: validated
---

# Incentive Design and Personnel Economics

## Core Idea
Personnel economics applies principal-agent theory to the employment relationship, analyzing how firms design compensation structures to elicit effort from workers whose actions they cannot perfectly observe. The core problem is moral hazard: workers bear the cost of effort but firms capture most of the output, creating a misalignment of incentives. Key compensation mechanisms include piece rates (pay per unit of output, which provide strong incentives but expose workers to risk and distort effort toward measurable dimensions), tournaments (rank-order compensation as in Lazear and Rosen, 1981, where workers compete for promotion and the prize spread motivates effort), deferred compensation (Lazear, 1979, where workers are underpaid early and overpaid late in their careers, creating self-enforcing incentives because workers lose deferred pay if fired for shirking), and efficiency wages (paying above market-clearing wages so that job loss is costly, motivating effort without direct monitoring). Each mechanism involves a different tradeoff between incentive power, risk allocation, and measurement costs.

## Questions

```yaml
- question: "Lazear's deferred compensation model predicts that workers are underpaid relative to their marginal product early in their careers and overpaid later. The incentive mechanism works because..."
  type: multiple-choice
  options:
    - "Workers become more productive over time due to human capital accumulation"
    - "Workers who shirk risk being fired and losing the above-marginal-product wages they would have received later — the future overpayment serves as a bond against shirking"
    - "Firms use seniority-based pay because it is administratively simpler"
    - "Workers prefer increasing wage profiles due to hyperbolic discounting"
  answer: 1
  explanation: "The key insight is that the upward-sloping age-earnings profile is not simply a return to experience — it is an incentive device. By backloading compensation, the firm creates a situation where workers have something to lose (the future premium over marginal product) if they are caught shirking. The worker effectively posts a bond through years of below-marginal-product wages early in the career. This explains mandatory retirement (otherwise, firms would want to terminate overpaid senior workers) and why long-tenure workers earn more than equally productive new hires — the tenure premium is a return on the implicit bond, not a return on skills."

- question: "In a tournament model of promotion (Lazear and Rosen, 1981), worker effort depends primarily on their absolute output level."
  type: true-false
  answer: false
  explanation: "In tournaments, what matters is relative rank, not absolute output. Workers compete against each other, and the one with the highest output (or performance evaluation) wins the promotion and the associated pay increase. Effort incentives depend on the prize spread (the difference between winner and loser pay) and the number of competitors, not on absolute performance thresholds. This has several implications: common shocks (a bad economy, a difficult assignment) do not change incentives because they affect all competitors equally; the optimal prize spread increases with the difficulty of monitoring individual effort; and tournaments can generate sabotage or excessive risk-taking if the prize spread is very large relative to base pay."

- question: "Why might a firm choose to pay efficiency wages (above market-clearing wages) rather than use piece rates or monitoring to motivate workers?"
  type: short-answer
  answer: "Efficiency wages are optimal when individual output is difficult or costly to measure (making piece rates infeasible), when monitoring is expensive or imperfect, and when the cost of worker malfeasance is high. By paying above the market wage, the firm makes job loss costly to workers — the gap between the current wage and the worker's next-best option (the 'employment rent') motivates effort because shirking risks detection and termination. The premium replaces direct monitoring: workers self-discipline because the consequences of being caught are severe. Efficiency wages also reduce turnover (saving recruitment and training costs) and may attract higher-quality applicants through adverse selection effects."
  explanation: "Shapiro and Stiglitz (1984) formalized this as a no-shirking condition: the wage must be high enough that the expected cost of shirking (probability of detection times the employment rent lost) exceeds the benefit of reduced effort. In equilibrium, all firms pay above the market-clearing wage, creating involuntary unemployment — which is itself part of the incentive mechanism, because unemployment makes job loss even more costly. This provides a microfoundation for involuntary unemployment based on incentive considerations rather than wage rigidity."
```

## Explainer

The fundamental problem of personnel economics is that the employment relationship involves delegation under imperfect information. A firm hires a worker to produce output, but the firm cannot perfectly observe the worker's effort — it can only observe output, which depends on effort, ability, and luck. If the firm pays a fixed wage regardless of output, rational workers have no incentive to exert costly effort beyond the minimum needed to avoid termination. This is the principal-agent problem applied to labor, and the various compensation structures studied in personnel economics are solutions to this problem, each with different strengths and weaknesses.

Piece rates — payment per unit of output — seem like the obvious solution: tie pay directly to output and the worker internalizes the marginal benefit of effort. Lazear's (1996) study of Safelite Glass found that switching from hourly wages to piece rates increased output per worker by 44%, with half coming from incentive effects (existing workers worked harder) and half from sorting effects (more productive workers were attracted to, and stayed at, the firm). But piece rates have well-documented problems: when output has multiple dimensions (quantity and quality, individual output and teamwork), workers distort effort toward the measured dimension and neglect unmeasured ones. Teachers paid by test scores teach to the test; salespeople paid by revenue neglect customer service. Holmstrom and Milgrom's (1991) multitask model formalizes this: when some tasks are easier to measure than others, strong incentives on measured tasks reduce effort on unmeasured tasks, and the optimal contract may deliberately weaken incentives to maintain balance.

Tournaments offer an alternative that does not require measuring absolute output — only relative rank. Lazear and Rosen (1981) showed that when workers of similar ability compete for promotion, the promotion wage premium functions as a tournament prize that motivates effort. The optimal prize spread depends on the number of competitors, the variance of the noise in performance evaluation, and the marginal cost of effort. Tournaments have practical advantages: they automatically filter out common shocks (a recession affects all competitors equally, so relative rank is informative about individual effort), they require only ordinal ranking (easier than cardinal measurement), and they are pervasive in corporate hierarchies where promotion decisions determine large pay jumps. The downsides include potential for sabotage (harming competitors' performance is as effective as improving one's own), collusion (competitors may tacitly agree to limit effort), and excessive risk-taking (if winning requires exceptional performance, players may gamble).

Deferred compensation addresses the incentive problem over the lifecycle of the employment relationship. Lazear (1979) proposed that the observed pattern of wages rising with tenure — faster than productivity gains can explain — is an incentive device, not just a return to experience. Workers are underpaid relative to their marginal product early in their careers and overpaid later. The worker effectively posts a bond: years of below-marginal-product wages that they will recoup only if they remain employed until the end of their career. A worker caught shirking is fired and loses the accumulated "bond." This explains several otherwise puzzling features of labor markets: mandatory retirement (firms need a termination date because they do not want to keep paying above marginal product indefinitely), seniority-based layoff rules (more senior workers have more deferred compensation at stake and thus need less monitoring), and the observation that wage-tenure profiles are steeper than productivity-tenure profiles.

Efficiency wages complete the incentive toolkit by using above-market wages as a substitute for monitoring. Rather than trying to observe effort directly, the firm pays a wage premium that makes the job valuable. Workers then self-monitor: the expected cost of being caught shirking (losing the employment rent) exceeds the benefit of reduced effort. Shapiro and Stiglitz (1984) showed that in equilibrium, all firms pay above the market-clearing wage, producing involuntary unemployment — which is itself a necessary part of the incentive mechanism, because full employment would eliminate the cost of job loss and destroy the incentive effect. This provides a microeconomic foundation for involuntary unemployment based on information asymmetries rather than sticky wages, and it connects personnel economics to macroeconomic questions about the natural rate of unemployment.
