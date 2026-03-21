---
id: intergenerational-equity-fiscal-policy
title: Intergenerational Equity and Fiscal Policy
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: overlapping-generations-models
  type: hard
- id: fiscal-policy-macroeconomics
  type: hard
builds-toward:
- government-debt-fiscal-sustainability
tags:
- fiscal-policy
- intergenerational
- debt
stage: advanced
status: draft
---

# Intergenerational Equity and Fiscal Policy

## Core Idea
OLG models reveal that government policies distribute burdens and benefits across generations. Unfunded government spending or deficits shift the tax burden to future generations; intergenerational equity requires that the present value of government spending across all generations be matched by taxes. This framework shows why current deficits create intergenerational imbalances and why sustainable policy requires current generations to pay for their consumption.

## Questions

```yaml
- question: "A government cuts taxes for today's working adults and finances the shortfall by issuing bonds. A standard Ricardian equivalence argument says this is welfare-neutral. Why does the OLG framework predict otherwise?"
  type: multiple-choice
  options:
    - "OLG models assume higher interest rates than Ricardian models, so debt is always more costly"
    - "In OLG, today's adults may retire or die before the bonds mature, shifting the repayment burden to future generations who had no say in the decision and cannot offset it"
    - "The Ricardian result requires rational expectations, which OLG models assume are unavailable to future generations"
    - "Ricardian equivalence only applies to tax cuts; it never predicts neutrality for debt-financed spending"
  answer: 1
  explanation: "Ricardian equivalence holds in a representative-agent model because the same infinitely-lived agent pays the debt in the future as received the tax cut today — their lifetime budget constraint is unchanged, so they just save the windfall. In an OLG model, the people who receive the tax cut are different from those who will repay the debt. Future generations cannot compensate by reducing saving today (they aren't born yet), so the transfer is real and non-neutral."

- question: "What is the core contribution of generational accounting (developed by Kotlikoff) to fiscal policy analysis?"
  type: multiple-choice
  options:
    - "It provides a real-time measure of GDP growth by cohort, replacing traditional national income accounting"
    - "It measures the net lifetime tax burden per birth cohort — taxes paid minus transfers received — revealing implicit intergenerational transfers in current fiscal policy"
    - "It computes the optimal tax rate for each generation to balance intergenerational equity with economic efficiency"
    - "It tracks the flow of physical capital between generations to measure wealth inequality"
  answer: 1
  explanation: "Generational accounting asks: for each birth cohort, what is the present value of all taxes they will pay minus all government transfers they will receive over their lifetime? By computing this for every living and future cohort, it makes explicit the intergenerational transfers embedded in current fiscal policy — transfers that are invisible in standard deficit accounting. Studies consistently find that current fiscal paths in developed nations impose higher lifetime burdens on younger and future cohorts than on those currently alive."

- question: "In an OLG model with no operative bequest motive, a deficit-financed tax cut is equivalent in welfare terms to an immediate tax cut of the same present value."
  type: true-false
  answer: false
  explanation: "False. Without a bequest motive, the generations who receive the tax cut have no reason to save and pass wealth to their children to offset future tax increases. The deficit therefore transfers real consumption from future generations to the current one — it is welfare-increasing for today's adults and welfare-decreasing for future adults. Welfare equivalence (Ricardian neutrality) requires an operative bequest motive that links all generations' utility functions into one, which OLG models without bequests explicitly do not assume."

- question: "Pay-as-you-go social insurance systems like Social Security are financed by accumulated investment assets, which insulates future generations from demographic risk."
  type: true-false
  answer: false
  explanation: "False. A pay-as-you-go (PAYG) system is financed by taxes on current workers that are immediately transferred to current retirees — there are no accumulated assets. Its sustainability depends entirely on the ratio of workers to retirees and on productivity growth. If birth rates fall or the population ages, current workers must pay higher taxes or current retirees must accept lower benefits. A funded pension system accumulates real assets and reduces this intergenerational transfer, but PAYG systems are explicit transfers from the working to the retired generation."

- question: "Why are democratic political processes systematically biased toward fiscal policies that favor current generations over future ones, and what analytical tools does the OLG framework provide to quantify this bias?"
  type: short-answer
  answer: "Future generations cannot vote, lobby, or bargain in political processes, so their interests are systematically underweighted in democratic decisions about spending, taxation, and debt. Current adults can vote to receive benefits financed by debt that future generations must repay. The OLG framework quantifies this through the government's intertemporal budget constraint (showing that the present value of spending must equal the present value of taxes) and generational accounting (measuring the net lifetime fiscal burden per cohort), making the intergenerational transfers analytically precise rather than merely rhetorical."
  explanation: "The political economy implication is stark: since future people have no political voice, there is a structural incentive to front-load spending and back-load taxes through deficit financing. Fiscal rules (debt brakes, balanced-budget requirements, spending caps) are institutional responses to this incentive problem — they attempt to constrain the current generation's ability to shift burdens forward by removing the decision from ordinary democratic deliberation."
```

## Explainer

From overlapping generations models, you know that the economy is not populated by a single infinitely-lived representative agent but by a succession of generations that are born, live, and die. This demographic structure creates a fundamental problem that does not exist in standard representative-agent models: **the interests of people alive today can conflict with the interests of people not yet born**. Fiscal policy — how the government taxes, spends, and borrows — is the primary mechanism through which these interests interact, because government debt issued today must be serviced by taxpayers in the future.

Consider a concrete example. Suppose the current generation votes for a tax cut financed by government borrowing. Today's adults enjoy higher disposable income and consume more. The government issues bonds to cover the revenue shortfall. When those bonds mature, taxes must rise to repay them — but by then, today's adults may have retired or died, and the burden falls on their children and grandchildren who had no voice in the original decision. This is the core **intergenerational transfer** at the heart of deficit spending: it shifts real resources from future generations to the present one. In the OLG framework, this transfer is not neutral (unlike in the Ricardian equivalence result for infinitely-lived agents) because there is no operative bequest motive connecting the utility of all generations into a single objective.

The **government's intertemporal budget constraint** requires that the present value of all future taxes equals the present value of all future spending plus the current outstanding debt. This is an accounting identity, not a policy choice — it must hold regardless of the government's preferences. The equity question is how the tax burden is distributed across generations. A policy of persistent deficits satisfies the budget constraint only if some future generation faces a dramatic tax increase or spending cut. **Generational accounting** — developed by Laurence Kotlikoff and others — attempts to measure these implicit transfers by computing the net tax burden (taxes paid minus transfers received) for each birth cohort over their lifetime. Studies consistently find that current fiscal policies in most developed nations impose substantially higher net burdens on future generations than on those currently alive.

Several policy instruments can address intergenerational imbalance. **Pay-as-you-go social insurance** (like Social Security) is an explicit intergenerational transfer from working-age to retired generations; its sustainability depends on demographics and productivity growth. **Funded pension systems** accumulate real assets rather than claims on future taxpayers, reducing intergenerational transfers. **Fiscal rules** — balanced budget amendments, debt brakes, spending caps — attempt to constrain the current generation's ability to shift burdens forward. The deeper challenge is political: future generations cannot vote, lobby, or bargain, so democratic processes systematically underweight their interests. The OLG framework makes this bias analytically precise and provides the tools to evaluate whether any proposed fiscal path treats generations equitably.
