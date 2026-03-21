---
id: simple-interest
title: Simple Interest
domain: mathematics
course: prealgebra
prerequisites:
- id: percent-of-a-number
  type: hard
- id: percent-increase-decrease
  type: soft
builds-toward: []
tags:
- interest
- percent
- finance
- applications
stage: abstract-reasoning
status: validated
---
# Simple Interest

## Core Idea
Simple interest is calculated using the formula I = Prt, where P is the principal (initial amount), r is the annual interest rate (as a decimal), and t is time in years. The total amount owed or earned is A = P + I. For example, $500 at 4% annual interest for 3 years yields I = 500 × 0.04 × 3 = $60, so the total is $560. Unlike compound interest, simple interest is computed only on the original principal, making the growth linear rather than exponential. Simple interest appears in short-term loans, some savings accounts, and as the foundation for understanding more complex financial concepts.

## How It's Best Learned
Start with concrete scenarios: saving birthday money in a bank, or borrowing money for a purchase. Have students identify P, r, and t from word problems before plugging into the formula. Practice converting interest rates from percents to decimals. Compare simple interest across different rates and time periods to build intuition about how each variable affects the total.

## Common Misconceptions
- Forgetting to convert the interest rate from a percent to a decimal before multiplying (using 4 instead of 0.04).
- Confusing simple interest with compound interest — simple interest does not "earn interest on interest."

## Questions

```yaml
- question: "You deposit $1,000 at 5% simple annual interest for 3 years. How much interest have you earned?"
  type: multiple-choice
  options:
    - "$157.63 — interest compounds each year on the growing balance"
    - "$150 — interest is calculated only on the original $1,000 each year"
    - "$50 — you earn 5% total over the 3 years, not per year"
    - "$15 — 5 and 3 multiply to 15, applied directly as dollars"
  answer: 1
  explanation: "Using I = Prt: I = 1000 × 0.05 × 3 = $150. Simple interest is calculated on the original principal every year — $50 per year for 3 years = $150 total. Option A shows compound interest, where interest earns additional interest each year. Option C misapplies the rate as a total rather than an annual rate. Option D confuses the rate value with a dollar amount and forgets the decimal conversion."

- question: "A student calculates simple interest on a $200 loan at 3% for 2 years by computing 200 × 3 × 2 = 1,200. What error did the student make?"
  type: multiple-choice
  options:
    - "Used the wrong formula — should have added the values instead of multiplied"
    - "Did not convert the interest rate from percent to decimal (should use 0.03, not 3)"
    - "Used the wrong time period — 2 years should be converted to 24 months first"
    - "Forgot to add the principal to the interest at the end to get the total amount"
  answer: 1
  explanation: "The student used r = 3 instead of r = 0.03, making the answer 100 times too large. The formula requires the rate as a decimal: 3% = 0.03. Correct calculation: I = 200 × 0.03 × 2 = $12. The percent-to-decimal conversion is the most common computational error in simple interest problems — using the raw percent number instead of its decimal equivalent inflates the result by a factor of 100."

- question: "If you borrow money at simple interest, doubling the loan period doubles the total interest owed."
  type: true-false
  answer: true
  explanation: "Simple interest grows linearly with time because interest is always calculated on the same original principal. If I = Prt, and you double t, you get I = Pr(2t) = 2(Prt) — exactly double the interest. This linear relationship is the defining characteristic of simple interest. It contrasts directly with compound interest, where doubling the time more than doubles the interest because of exponential growth."

- question: "With simple interest, more interest is earned in year 3 than in year 1, because the account has grown larger over time."
  type: true-false
  answer: false
  explanation: "This describes compound interest, not simple interest. In simple interest, the same dollar amount of interest is earned every year because interest is always calculated on the original principal — never on previously accumulated interest. In year 1, year 2, and year 3, you earn exactly P × r. The account grows linearly — the graph of total value over time is a straight line, not a curve upward."

- question: "What does 'simple' mean in 'simple interest,' and how does this make its growth pattern different from compound interest?"
  type: short-answer
  answer: "'Simple' means interest is calculated only on the original principal each period — it never earns interest on itself. This makes growth linear: the same fixed dollar amount accumulates each year. Compound interest, by contrast, applies the rate to the growing balance (principal plus previously earned interest), so each year's interest is larger than the last, producing exponential growth."
  explanation: "The practical effect is small over short periods but dramatic over long ones. A $1,000 deposit at 5% simple interest earns $50 every year forever. At 5% compound interest, year 1 earns $50, year 10 earns about $77, and year 30 earns about $208. The word 'simple' is the signal that no compounding occurs — the interest calculation resets to the same base every period."
```

## Explainer

You already know how to find a percent of a number: to find 4% of $500, you convert the percent to a decimal (4% → 0.04) and multiply: 500 × 0.04 = $20. **Simple interest** takes that idea and adds time. When you borrow or lend money, interest is the cost of using that money over a period of time. Simple interest asks: how much does the interest grow each year?

The formula I = Prt connects three quantities. **P** (principal) is the amount you start with — the original loan or deposit. **r** is the annual interest rate written as a decimal. **t** is the number of years. Multiply them together and you get the total interest earned or owed. If you deposit $500 at 4% annual interest for 3 years: I = 500 × 0.04 × 3 = $60. The total amount in the account is A = P + I = $500 + $60 = $560.

The word "simple" in simple interest means something precise: interest is calculated only on the original principal, every year. In year 1 you earn $20, in year 2 another $20, in year 3 another $20. The interest never builds on itself — it stays flat. This makes growth **linear**: a graph of total value over time is a straight line. Double the time, double the interest. Triple the time, triple the interest. That predictable linearity is what distinguishes simple interest from compound interest, where interest earned in one period starts earning interest of its own in the next.

A quick way to catch errors is to check units. P is in dollars, r is in "per year," and t is in years — so r × t produces a dimensionless number (years cancel years), and P × r × t gives dollars of interest. If you forget the percent-to-decimal conversion and write r = 4 instead of r = 0.04, you get an answer exactly 100 times too large. That unit check is also a reminder that if the time isn't given in years, you must convert: 6 months is t = 0.5, not t = 6.
