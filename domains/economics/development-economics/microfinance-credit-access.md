---
id: microfinance-credit-access
title: Microfinance and Access to Credit
domain: economics
course: development-economics
prerequisites:
- id: asymmetric-information-markets
  type: soft
- id: credit-constraints-poverty
  type: soft
builds-toward:
- agricultural-credit-markets
tags:
- microfinance
- credit
stage: advanced
status: draft
---

# Microfinance and Access to Credit

## Core Idea
Microfinance institutions provide loans to poor households and microenterprises excluded from formal banking by lack of collateral and high transaction costs. Grameen Bank pioneered group lending to overcome information problems. Recent randomized evidence reveals microfinance increases business activity but often fails to reliably increase earnings or reduce poverty, suggesting credit requires complementary inputs for escape from poverty.

## Questions

```yaml
- question: "A microfinance program in rural India achieves 96% loan repayment rates, but a rigorous randomized controlled trial finds no statistically significant effect on household income after two years. What best explains this gap between repayment success and income impact?"
  type: multiple-choice
  options:
    - "High repayment proves borrowers found the loans profitable, so the RCT must have measurement error"
    - "Borrowers deliberately hid income gains from researchers to avoid losing loan eligibility"
    - "Credit alone cannot overcome all binding constraints — borrowers face saturated markets, poor roads, health shocks, or skill gaps that prevent translating loans into income gains"
    - "Two years is too short for microenterprise returns to materialize; a longer study would show large effects"
  answer: 2
  explanation: "This is precisely the pattern found in six-country RCT studies around 2010. High repayment and zero income effect are compatible: borrowers may use loans for consumption smoothing (bridging lean seasons or covering emergencies) rather than productive investment, or they may invest productively but face binding constraints beyond credit — market access, business skills, health, or infrastructure — that prevent turning investment into income. Credit addresses one constraint in a multi-constraint problem. Option D contradicts the RCT evidence; longer follow-ups have not systematically reversed the findings."

- question: "Group lending at Grameen Bank achieves high repayment rates among borrowers who lack traditional collateral. What is the primary mechanism enabling this?"
  type: multiple-choice
  options:
    - "The government guarantees loan repayment, eliminating default risk for the bank"
    - "Interest rates are set high enough that only low-risk borrowers apply"
    - "Peer screening and mutual monitoring among group members substitute for collateral, aligning incentives for repayment"
    - "Loans are small enough that the cost of default exceeds any possible benefit to the borrower"
  answer: 2
  explanation: "Group lending solves two information problems. First, adverse selection: group members know each other and screen out unreliable borrowers when forming groups — they won't form a group with someone likely to default, since they share liability. Second, moral hazard: group members monitor each other's use of funds and apply social pressure for repayment, because one member's default raises costs for all. This social collateral substitute is what enables 95%+ repayment rates without physical collateral — option A is false (no government guarantee), and option B would price out the poor entirely."

- question: "Randomized controlled trial evidence from multiple countries shows that microfinance reliably lifts households out of poverty by enabling productive investment in microenterprises."
  type: true-false
  answer: false
  explanation: "The wave of RCTs conducted around 2010 across six countries (India, Ethiopia, Bosnia, Morocco, Mexico, Mongolia) found remarkably consistent results: microcredit modestly increased business investment and self-employment activity, but did not produce statistically significant increases in household income, consumption, or standard poverty measures. The initial enthusiasm — that microcredit was a 'silver bullet' for poverty — was not supported by rigorous evidence. This does not mean microfinance is useless (it provides valuable financial services), but it revealed that credit alone is insufficient for poverty escape."

- question: "The Grameen Bank's group lending model effectively solves the adverse selection and moral hazard problems that prevent conventional banks from serving poor borrowers without collateral."
  type: true-false
  answer: true
  explanation: "Adverse selection (lenders can't tell good borrowers from bad) is addressed because group members screen each other — they know who in their village is reliable and won't form a group with someone likely to default. Moral hazard (borrowers may misuse funds or shirk repayment) is addressed because group members monitor each other and apply social pressure, since one default raises costs for all. Both problems are solved using local information and social ties that conventional banks lack, which explains why Grameen achieved repayment rates of 95%+ — far above what conventional banks achieved with poor borrowers."

- question: "Why does randomized evidence show that microfinance increases business activity but often fails to reduce poverty, and what does this imply about the nature of poverty?"
  type: short-answer
  answer: "Poverty is a multi-constraint problem. Microfinance provides access to a lump sum of capital — one scarce input — but a borrower who invests in a market stall may still face saturated local demand, poor roads, lack of business skills, health shocks that divert funds, or legal barriers. Removing one constraint (credit) when multiple binding constraints remain may allow some adjustment but cannot generate sustained income growth. This implies that poverty is not simply caused by credit shortage; it is maintained by several interlocking constraints simultaneously. Effective interventions — like graduation programs — must address multiple constraints together: asset transfer, skills training, savings support, health care, and coaching bundled in sequence."
  explanation: "The implication is important for policy: if credit were the sole binding constraint on poor households, providing it would produce large income gains. The RCT evidence that it doesn't reveals a multi-constraint poverty trap. Graduation programs that bundle assets, training, savings facilitation, health support, and coaching have shown sustained income gains in randomized trials where microcredit alone did not — supporting the multi-constraint interpretation."
```

## Explainer

From your study of asymmetric information and credit constraints, you know that credit markets break down when lenders cannot distinguish good borrowers from bad ones and when borrowers lack collateral to guarantee repayment. In developed countries, these problems are managed through credit histories, legal enforcement of contracts, and assets that serve as collateral. In developing countries, most poor households have none of these: no credit history, no formal property titles to pledge, and no access to courts that would enforce loan contracts. The result is that hundreds of millions of people who could productively use a small loan — to buy inventory for a market stall, purchase a dairy cow, or invest in better seeds — are entirely excluded from formal credit markets.

**Microfinance** emerged as an institutional innovation designed to solve this problem. The breakthrough insight, pioneered by Muhammad Yunus and the **Grameen Bank** in Bangladesh in the 1970s, was **group lending**: instead of requiring individual collateral, loans are made to small groups of borrowers (typically five women) who are jointly liable for each other's repayment. This mechanism works through several channels. First, group members screen each other — they know who in their village is reliable and will refuse to form a group with someone likely to default (solving **adverse selection**). Second, group members monitor each other's use of funds, since one member's default raises everyone's costs (solving **moral hazard**). Third, the social pressure of not wanting to let down neighbors and friends provides a powerful repayment incentive that substitutes for legal enforcement. Repayment rates at Grameen and similar institutions frequently exceeded 95%, far above what conventional banks achieved with poor borrowers.

The initial enthusiasm was enormous — microfinance was hailed as a silver bullet for poverty reduction, and Yunus received the Nobel Peace Prize in 2006. But beginning around 2010, a wave of **randomized controlled trials** across six countries produced more sobering results. The findings were remarkably consistent: access to microcredit modestly increased business investment and self-employment activity, but did not produce statistically significant increases in household income, consumption, or standard measures of well-being. Some borrowers expanded businesses successfully, but many others used loans for consumption smoothing (covering emergencies or bridging lean seasons) rather than productive investment. The average effect on poverty was essentially zero.

These results do not mean microfinance is useless — it clearly provides value as a financial service, giving poor households access to lump sums they could not otherwise obtain. But they reveal that **credit alone is insufficient** to escape poverty. A woman who borrows to stock her market stall may face saturated local demand, poor roads that prevent her from reaching larger markets, lack of business skills, or health shocks that force her to divert funds. Escaping poverty requires addressing multiple binding constraints simultaneously — credit, skills, health, infrastructure, and market access. This insight has shifted the frontier of development practice toward **graduation programs** that bundle asset transfers, training, savings facilitation, health support, and coaching together, which randomized trials have shown to produce sustained income gains where microcredit alone did not.
