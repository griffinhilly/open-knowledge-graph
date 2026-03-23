---
id: asset-valuation-and-returns
title: Asset Valuation and Present Value in Microeconomics
domain: economics
course: microeconomics
prerequisites:
- id: present-value-and-discounting
  type: hard
tags:
- asset pricing
- capital
- investment
stage: formal-systems
status: validated
---

# Asset Valuation and Present Value in Microeconomics

## Core Idea
An asset's value equals the discounted present value of expected future cash flows: V = Σ [CF_t / (1+r)^t]. The discount rate r reflects time preference and risk. Assets yielding higher returns than safer alternatives must offer a risk premium. Portfolio equilibrium requires equal expected returns adjusted for risk across assets. Capital investment (firms choosing projects) uses NPV rule: invest if net present value > 0. Risk diversification reduces portfolio variance without reducing expected return.

## Questions

```yaml
- question: "Two firms have identical expected future cash flows. Firm A's returns are highly correlated with the overall stock market; Firm B's returns are driven almost entirely by company-specific events uncorrelated with the market. Which firm should have a higher market valuation, and why?"
  type: multiple-choice
  options:
    - "Firm A, because market-correlated returns are more predictable and therefore safer"
    - "Firm B, because its idiosyncratic risk means it pays higher dividends to attract investors"
    - "Firm B, because its risk is idiosyncratic and can be diversified away, so investors require no risk premium for it — a lower discount rate implies higher value"
    - "Both firms have identical valuations since their expected cash flows are the same"
  answer: 2
  explanation: "This question tests the key insight about diversifiable versus non-diversifiable risk. Firm B's risk is idiosyncratic — investors who hold a diversified portfolio bear none of it, because bad outcomes at Firm B are offset by other holdings. Rational investors therefore require no risk premium for idiosyncratic risk, resulting in a lower discount rate and higher valuation. Firm A's risk is systematic (correlated with the market) and cannot be diversified away, so investors demand a risk premium — a higher discount rate and thus lower valuation — despite identical expected cash flows."

- question: "A project requires a $1,000 upfront investment and is expected to return $1,050 in one year. The appropriate discount rate for comparable-risk investments is 8%. Should the firm invest?"
  type: multiple-choice
  options:
    - "Yes, because the project earns a positive return of 5%"
    - "No, because the NPV is negative — the present value of $1,050 at 8% is about $972, less than the $1,000 cost"
    - "Yes, because any positive cash flow exceeds the cost of the project"
    - "No, because returning more than invested in one year implies excessive risk"
  answer: 1
  explanation: "NPV = PV(cash flows) − cost = $1,050/1.08 − $1,000 ≈ $972 − $1,000 = −$28. A negative NPV means this project earns less than the 8% available on comparable-risk alternatives — it destroys value relative to the next-best use of the $1,000. The 5% return sounds positive in isolation, but the correct benchmark is the opportunity cost of capital (8%), not zero. The NPV rule embeds this comparison automatically: NPV > 0 means the project beats the market; NPV < 0 means it does not."

- question: "Diversification reduces both the expected return and the variance of a portfolio."
  type: true-false
  answer: false
  explanation: "Diversification reduces portfolio variance without reducing expected return — this is what makes it a 'free lunch' in finance. Expected portfolio return is simply the weighted average of individual asset expected returns, and combining assets doesn't change this. But when assets are imperfectly correlated, their risks partially cancel: bad outcomes on some assets coincide with good outcomes on others. Portfolio variance falls below the weighted average of individual variances. The insight is that risk reduction through diversification costs nothing in expected return, which is why any rational investor holds a diversified portfolio."

- question: "An asset that generates higher expected returns than a risk-free government bond must be offering investors compensation for bearing systematic risk that cannot be diversified away."
  type: true-false
  answer: true
  explanation: "In equilibrium, the extra expected return above the risk-free rate — the risk premium — compensates investors for bearing risk they cannot eliminate. Idiosyncratic risk can be diversified away by combining it with other uncorrelated assets, so rational investors who hold diversified portfolios bear none of it and will not pay a premium for bearing it. Only systematic risk (correlated with the broad market) survives diversification and therefore commands a risk premium. This is the core implication of the Capital Asset Pricing Model and of modern portfolio theory."

- question: "Why does diversification reduce portfolio risk without reducing expected portfolio return? What is the mathematical and intuitive reason?"
  type: short-answer
  answer: "Expected portfolio return is the weighted average of individual expected returns — combining assets doesn't change this. Portfolio variance, however, depends not just on individual variances but on covariances between assets. When assets are imperfectly correlated (covariance < product of standard deviations), the variance of their combination is less than the weighted average of their individual variances. Intuitively: when one asset has a bad year, another may have a good year, and these offsetting movements reduce the portfolio's overall swings without affecting the average outcome."
  explanation: "The formula var(aX + bY) = a²var(X) + b²var(Y) + 2ab·cov(X,Y) shows that if cov(X,Y) is negative or even less than var(X)·var(Y), the portfolio variance is below the weighted average variance. Perfect correlation (cov = σₓσᵧ) would mean no benefit from diversification; negative correlation provides the maximum benefit. This is why mixing a domestic stock fund with an international or bond fund reduces volatility — not because expected returns change, but because correlations are less than 1."
```

## Explainer

Every asset — a share of stock, a rental property, a bond, a machine in a factory — is ultimately a claim on future cash flows. Your prerequisite on present value established that a dollar received in the future is worth less than a dollar today, discounted at rate r per period. Asset valuation applies this logic directly: to find what an asset is worth *now*, list all the cash flows it will generate in the future, discount each one back to the present, and sum them. The result, V = Σ [CF_t / (1+r)^t], is the **fundamental valuation equation**. If the market price of an asset is below this value, the asset is underpriced relative to its cash-generating potential; if above, overpriced. In liquid markets, competition among buyers and sellers drives prices toward fundamental value.

The discount rate r is doing two jobs simultaneously. First, it captures **time preference** — the pure preference for having resources now rather than later, independent of risk. Second, it captures **risk**. If two assets have identical expected cash flows but one is riskier, rational investors will pay less for the risky one, equivalently requiring a higher expected return to hold it. This extra required return is called the **risk premium**. A safe government bond might be discounted at 4%; a volatile equity stake at 12%. The difference (8%) is the risk premium investors demand for bearing that additional uncertainty. This explains why risky assets must offer higher *expected* returns — not as a reward for past performance, but as the price of attracting investors who could otherwise hold safer assets.

The **NPV rule** translates this valuation logic into a decision rule for firms investing in projects. A project is worth undertaking if the present value of its expected future cash flows exceeds the upfront cost — that is, if its **net present value** is positive. A positive NPV means the project earns more than the opportunity cost of capital (the rate r): it creates value. A negative NPV destroys value relative to the next-best use of funds. Firms maximizing value should accept all positive-NPV projects and reject negative-NPV ones — this is the microeconomic foundation of capital budgeting. Note that r here represents the return available on comparable-risk alternatives, so NPV automatically benchmarks against the market.

**Diversification** adds an important wrinkle to risk. When you hold a single risky asset, you bear all its variability. But when you combine assets whose returns do not move together perfectly — **uncorrelated** or **negatively correlated** assets — bad outcomes on one are partially offset by good outcomes on another. The mathematical result is that portfolio variance falls below the average variance of its components, even though expected portfolio return is just the weighted average of individual expected returns. This means investors can reduce risk without sacrificing expected return, purely by mixing assets wisely. The implication for pricing: only **systematic risk** (risk correlated with the overall market, which cannot be diversified away) commands a risk premium. **Idiosyncratic risk** (firm-specific risk) does not, because any rational investor holding a diversified portfolio bears none of it. This is why two firms with similar expected profits can have very different valuations: the one whose fortunes are tightly linked to the broad economy is riskier to hold and therefore cheaper relative to its cash flows.
