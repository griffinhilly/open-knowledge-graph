---
id: cash-transfers-and-incentives
title: 'Cash Transfers: Conditional and Unconditional'
domain: economics
course: development-economics
prerequisites:
- id: foreign-aid-effectiveness
  type: hard
- id: principal-agent-contracting
  type: soft
- id: group-lending-mechanisms
  type: soft
- id: conditional-cash-transfers-cct
  type: soft
builds-toward:
- school-attendance-and-incentives
tags:
- cash-transfers
- incentives
- development
stage: advanced
status: validated
---
# Cash Transfers: Conditional and Unconditional

## Core Idea
Conditional cash transfers (CCTs) tie payments to actions like school attendance or health checkups, incentivizing human capital investment. Evidence shows CCTs increase school enrollment and health visits; earnings gains are modest and take years. Unconditional cash transfers also improve welfare and school attendance (possibly through income effects) with lower administrative costs but face political resistance.

## Questions

```yaml
- question: "Evidence shows that recipients of unconditional cash transfers in Kenya did NOT significantly increase spending on alcohol or tobacco. Which assumption does this finding most directly refute?"
  type: multiple-choice
  options:
    - "That poor households face binding credit constraints preventing investment"
    - "That poor households make poor spending decisions when given unrestricted cash"
    - "That behavioral conditions are necessary to achieve human capital investments"
    - "That monitoring conditions is administratively costly"
  answer: 1
  explanation: "The common 'paternalistic' objection to unconditional transfers is that poor households will waste money on temptation goods. GiveDirectly's experimental evidence directly contradicts this: recipients invest in productive assets, food, education, and health. This supports the case for UCTs where income constraints — not behavioral failures — are the primary barrier to investment. The finding does not address whether conditions are behaviorally valuable (option C), only whether unguided cash is misspent."

- question: "In a setting where school fees are the main barrier to enrollment, a conditional cash transfer requiring school attendance will produce larger enrollment gains than an unconditional transfer of the same size."
  type: true-false
  answer: false
  explanation: "If the primary barrier is purely financial (fees, uniforms, transport costs), income alone — without a condition — is sufficient to overcome it. Parents who already want their children educated will spend the unconditional transfer on schooling once it is affordable. The condition adds value only when behavioral barriers (present bias, information gaps about returns, social norms) keep enrollment below what the income effect alone would predict. When the problem is purely financial, the condition is costly monitoring with little added enrollment effect."

- question: "A CCT program that successfully increases school enrollment is necessarily improving long-run welfare more than a UCT of equal size would."
  type: true-false
  answer: false
  explanation: "Even if a CCT increases enrollment more than a UCT, this doesn't establish higher welfare — the UCT recipient has flexibility to address other urgent needs (health, nutrition, shelter) that may have larger welfare effects than the marginal increase in schooling. CCTs also have higher administrative costs, so a nominally equal-size CCT delivers less net cash to households. Welfare comparisons require accounting for all effects across all dimensions, not just the targeted behavior."

- question: "A government is choosing between a CCT requiring clinic visits and a UCT for the same population where clinic attendance is low. Which factor most strongly favors the CCT?"
  type: multiple-choice
  options:
    - "High government administrative capacity to monitor compliance"
    - "Evidence that parents believe clinic visits are not worth the time and travel cost"
    - "High transportation costs making clinic access difficult"
    - "Credit constraints preventing households from affording food and basic necessities"
  answer: 1
  explanation: "CCTs add value over UCTs when the targeted behavior is underprovided relative to what income alone would predict — i.e., when a behavioral barrier, not a budget constraint, is binding. If parents believe clinics are not worthwhile (information gap or present bias), income alone won't change behavior — the financial nudge of the condition is needed. If transportation costs (C) or credit constraints (D) are the barriers, income unconditionally given solves the problem. High administrative capacity (A) makes CCTs feasible but doesn't indicate whether the condition adds behavioral value."

- question: "Under what conditions does the behavioral condition in a CCT add measurable value beyond what an income transfer alone would produce, and what is the policy implication?"
  type: short-answer
  answer: "The condition adds value when households underinvest in the target behavior relative to what their income level would predict — specifically when present bias, incomplete information about returns, or cultural norms are the binding constraint rather than pure budget limits. If parents know schooling pays off, can now afford it, and want it, income alone achieves the enrollment gain. If parents heavily discount future returns or underestimate them, the financial nudge of the condition changes the calculus beyond what income provides. The policy implication: CCTs are most valuable when behavioral barriers are measurable and monitoring is affordable; UCTs dominate when financial constraints are primary and monitoring costs are high."
  explanation: "The core insight is that 'not doing X' can have multiple causes: can't afford it, or won't do it even if they could. Conditional transfers address the latter; unconditional transfers address the former. Empirical research distinguishes these by comparing CCT and UCT effects in identical settings — when effects converge, the income effect was sufficient; when CCTs outperform, the condition added something beyond income."
```

## Explainer

From your study of foreign aid effectiveness, you know that the central challenge in development assistance is ensuring resources actually reach intended beneficiaries and change behavior in lasting ways. Cash transfers represent a sharp departure from traditional aid: instead of building infrastructure, shipping food, or funding government programs, you simply give money directly to poor households. The debate over whether to attach conditions to those payments is one of the most active empirical questions in development economics.

**Conditional cash transfers (CCTs)** require recipients to take specific actions — typically sending children to school, attending health clinics, or getting vaccinations — in exchange for regular payments. Mexico's Progresa/Oportunidades program (now Prospera) pioneered this approach in the late 1990s and has been widely replicated in Brazil (Bolsa Família), Colombia, and dozens of other countries. The logic draws on principal-agent reasoning you may recognize: households may underinvest in children's education due to credit constraints, present bias, or incomplete information about returns. The condition acts as a nudge backed by a financial incentive, aligning household behavior with long-run welfare. Rigorous evaluations show CCTs consistently increase school enrollment by 5–10 percentage points and improve health clinic visits, though effects on learning outcomes and adult earnings are more modest and take a generation to fully materialize.

**Unconditional cash transfers (UCTs)** give money with no strings attached, trusting recipients to allocate it where it matters most. The argument for UCTs is partly practical — monitoring conditions is expensive, bureaucratically complex, and can exclude the neediest households who cannot comply. It is also partly philosophical — poor households may know their own constraints better than program designers. GiveDirectly, operating in Kenya and Uganda, has produced some of the cleanest experimental evidence: unconditional transfers increase consumption, assets, and psychological well-being, with no evidence of increased spending on alcohol or tobacco (a common concern that the data consistently refutes).

The CCT-versus-UCT debate hinges on whether the conditions themselves cause the behavioral change, or whether the money alone is sufficient. In settings where barriers to school attendance are primarily financial (fees, uniforms, transport costs), unconditional transfers produce similar enrollment gains to conditional ones — the income effect does the work. But where cultural norms, information gaps, or present bias are the binding constraints, the condition adds value above the transfer itself. The policy implication is context-dependent: CCTs are more effective when the target behavior is underprovided relative to what income alone would predict, while UCTs dominate when administrative costs of monitoring are high and households face straightforward budget constraints.
