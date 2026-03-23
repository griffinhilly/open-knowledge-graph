---
id: apr-apy-and-interest-rate-calculation
title: APR vs. APY and Interest Rate Calculation
domain: practical-life-skills
course: financial-literacy
prerequisites:
- id: money-fundamentals-definition-and-characteristics
  type: hard
- id: percent-of-a-number
  type: soft
- id: exponential-functions-and-graphs
  type: soft
- id: compound-interest
  type: hard
- id: percent-concept
  type: soft
- id: exponents-intro
  type: soft
builds-toward:
- bonds-and-fixed-income-securities
- economic-indicators-and-personal-finance-impact
- compound-interest
tags:
- interest-rates
- apr
- apy
- borrowing-costs
- savings-returns
stage: formal-systems
status: validated
---

# APR vs. APY and Interest Rate Calculation

## Core Idea
APR (Annual Percentage Rate) and APY (Annual Percentage Yield) both express interest rates but differ in how they account for compounding. APR is the simple annual rate without compounding; APY includes the effect of compounding and represents the true annual return. This distinction significantly affects borrowing costs and savings returns over time.

## How It's Best Learned
Calculate APR and APY for a sample loan and savings account. Use online calculators to compare the same nominal rate under APR vs. APY to see the compounding effect.

## Common Misconceptions
APR and APY are interchangeable (they account for compounding differently). Higher APR always means higher actual cost (APY reveals the true cost).

## Questions

```yaml
- question: "Bank A offers a savings account with 6% APR compounded monthly. Bank B offers 5.9% APY. Which provides a better annual return?"
  type: multiple-choice
  options:
    - "Bank A, because 6% is greater than 5.9%"
    - "Bank B, because APY already includes compounding and is the correct basis for comparison"
    - "Bank A, because monthly compounding produces more interest than annual compounding"
    - "They are equivalent — APR and APY represent the same rate expressed differently"
  answer: 1
  explanation: "Bank A's 6% APR compounded monthly converts to APY = (1 + 0.06/12)^12 − 1 ≈ 6.17%. Since Bank B's APY of 5.9% is lower than 6.17%, Bank A is actually better. The trap in option A is comparing the stated rates directly (6% vs. 5.9%) without converting to the same basis. APY is the correct comparison because it captures the full effect of compounding — always compare APYs when evaluating savings accounts."

- question: "A credit card advertises a 20% APR. Why might advertising APR rather than APY be considered favorable to the lender?"
  type: multiple-choice
  options:
    - "APR and APY are equal for credit cards, so the choice doesn't affect the apparent rate"
    - "When interest compounds more than once per year, APY > APR, so advertising APR makes the rate appear lower than the true annual cost"
    - "APY is more complex to compute and would confuse consumers"
    - "APR is a universal international standard while APY varies by country"
  answer: 1
  explanation: "When interest compounds more frequently than once per year (daily on most credit cards), APY > APR. A 20% APR compounded daily converts to APY ≈ 22.1%. Advertising the lower APR number makes the product appear cheaper than it truly is. This asymmetry is why savvy borrowers convert APR to APY — the advertised rate systematically understates the true annual cost when compounding is frequent."

- question: "For a savings account with a fixed nominal rate, more frequent compounding always results in a higher APY."
  type: true-false
  answer: true
  explanation: "APY = (1 + APR/n)^n − 1, where n is the number of compounding periods per year. As n increases, this expression increases monotonically (approaching e^(APR) at continuous compounding), which is always greater than the simple APR. Daily compounding always yields a higher APY than monthly compounding at the same APR, which yields higher than annual compounding. The effect shrinks as n grows large, but APY is always at least as large as APR."

- question: "Two savings accounts with the same APY but different compounding frequencies will produce different year-end balances."
  type: true-false
  answer: false
  explanation: "APY already accounts for compounding frequency — that's its purpose. If two accounts have the same APY, they produce the same annual return by definition, regardless of how often they compound. APY is the effective annual rate after compounding is factored in. This is exactly why APY is the right number to compare: it strips away compounding frequency differences so accounts can be evaluated on equal footing."

- question: "Why is APY the better number to use when comparing savings accounts, even though APR is what lenders typically advertise?"
  type: short-answer
  answer: "APY includes the full effect of compounding over a year, showing what you actually earn. APR simply multiplies the periodic rate by the number of periods without accounting for compounding — it ignores the fact that interest compounds on itself. Two accounts with the same APR but different compounding frequencies will have different APYs and produce different balances. Comparing APYs gives a consistent, apples-to-apples view of actual annual returns regardless of compounding schedule."
  explanation: "The formula APY = (1 + APR/n)^n − 1 converts any APR and compounding frequency into a single comparable number. An account with 5% APR compounded monthly has APY ≈ 5.12%, while one compounded daily has APY ≈ 5.13%. These are small at low rates but grow at higher rates. The same logic applies to borrowing: always convert loan APRs to APY to see the true annual cost — the advertised APR is almost always lower than what you actually pay."
```

## Explainer

You already understand compound interest: when interest is added to a balance and then earns interest itself, the growth accelerates over time. **APR** (Annual Percentage Rate) and **APY** (Annual Percentage Yield) are two ways of expressing how much interest applies to a financial product annually — but they treat compounding very differently. APR ignores compounding and simply states the periodic rate multiplied by the number of periods. APY captures the full effect of compounding and tells you what you actually earn or pay over a year.

Here's a concrete example. Suppose a savings account advertises a 6% APR, compounded monthly. The monthly rate is 6% ÷ 12 = 0.5%. After 12 months of compounding, $1,000 grows to $1,000 × (1.005)^12 ≈ $1,061.68. The APY is therefore about 6.17% — not 6%. The gap seems small, but it widens significantly at higher rates or when compounding happens more frequently (daily vs. monthly). This is why APY is the honest number: it tells you what you'll actually end up with. When comparing savings accounts or certificates of deposit, always compare APYs, not APRs.

The same arithmetic applies in reverse for borrowing, but now you're the one paying the interest. A credit card with a 24% APR compounded daily has an APY of about 27.1%. The advertised APR looks lower than the true annual cost. Lenders are legally required to disclose APR under the Truth in Lending Act in the U.S., which means the advertised number is often the one that makes the product look more attractive. Savvy borrowers convert APR to APY to understand the real cost: APY = (1 + APR/n)^n − 1, where n is the number of compounding periods per year.

The strategic implication is straightforward: when you're **saving**, look for the highest APY. When you're **borrowing**, look for the lowest APY (even if the lender advertises APR). The same 5% stated rate can translate to very different real costs depending on how often the interest compounds. For mortgages and auto loans with monthly payments, the math is more complex because principal reduces over time — but understanding APR vs. APY is the foundation that makes those more advanced calculations interpretable.
