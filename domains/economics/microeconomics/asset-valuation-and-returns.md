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
status: draft
---

# Asset Valuation and Present Value in Microeconomics

## Core Idea
An asset's value equals the discounted present value of expected future cash flows: V = Σ [CF_t / (1+r)^t]. The discount rate r reflects time preference and risk. Assets yielding higher returns than safer alternatives must offer a risk premium. Portfolio equilibrium requires equal expected returns adjusted for risk across assets. Capital investment (firms choosing projects) uses NPV rule: invest if net present value > 0. Risk diversification reduces portfolio variance without reducing expected return.

## Explainer

Every asset — a share of stock, a rental property, a bond, a machine in a factory — is ultimately a claim on future cash flows. Your prerequisite on present value established that a dollar received in the future is worth less than a dollar today, discounted at rate r per period. Asset valuation applies this logic directly: to find what an asset is worth *now*, list all the cash flows it will generate in the future, discount each one back to the present, and sum them. The result, V = Σ [CF_t / (1+r)^t], is the **fundamental valuation equation**. If the market price of an asset is below this value, the asset is underpriced relative to its cash-generating potential; if above, overpriced. In liquid markets, competition among buyers and sellers drives prices toward fundamental value.

The discount rate r is doing two jobs simultaneously. First, it captures **time preference** — the pure preference for having resources now rather than later, independent of risk. Second, it captures **risk**. If two assets have identical expected cash flows but one is riskier, rational investors will pay less for the risky one, equivalently requiring a higher expected return to hold it. This extra required return is called the **risk premium**. A safe government bond might be discounted at 4%; a volatile equity stake at 12%. The difference (8%) is the risk premium investors demand for bearing that additional uncertainty. This explains why risky assets must offer higher *expected* returns — not as a reward for past performance, but as the price of attracting investors who could otherwise hold safer assets.

The **NPV rule** translates this valuation logic into a decision rule for firms investing in projects. A project is worth undertaking if the present value of its expected future cash flows exceeds the upfront cost — that is, if its **net present value** is positive. A positive NPV means the project earns more than the opportunity cost of capital (the rate r): it creates value. A negative NPV destroys value relative to the next-best use of funds. Firms maximizing value should accept all positive-NPV projects and reject negative-NPV ones — this is the microeconomic foundation of capital budgeting. Note that r here represents the return available on comparable-risk alternatives, so NPV automatically benchmarks against the market.

**Diversification** adds an important wrinkle to risk. When you hold a single risky asset, you bear all its variability. But when you combine assets whose returns do not move together perfectly — **uncorrelated** or **negatively correlated** assets — bad outcomes on one are partially offset by good outcomes on another. The mathematical result is that portfolio variance falls below the average variance of its components, even though expected portfolio return is just the weighted average of individual expected returns. This means investors can reduce risk without sacrificing expected return, purely by mixing assets wisely. The implication for pricing: only **systematic risk** (risk correlated with the overall market, which cannot be diversified away) commands a risk premium. **Idiosyncratic risk** (firm-specific risk) does not, because any rational investor holding a diversified portfolio bears none of it. This is why two firms with similar expected profits can have very different valuations: the one whose fortunes are tightly linked to the broad economy is riskier to hold and therefore cheaper relative to its cash flows.
