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
stage: concrete-operations
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

## Explainer

You already know how to find a percent of a number: to find 4% of $500, you convert the percent to a decimal (4% → 0.04) and multiply: 500 × 0.04 = $20. **Simple interest** takes that idea and adds time. When you borrow or lend money, interest is the cost of using that money over a period of time. Simple interest asks: how much does the interest grow each year?

The formula I = Prt connects three quantities. **P** (principal) is the amount you start with — the original loan or deposit. **r** is the annual interest rate written as a decimal. **t** is the number of years. Multiply them together and you get the total interest earned or owed. If you deposit $500 at 4% annual interest for 3 years: I = 500 × 0.04 × 3 = $60. The total amount in the account is A = P + I = $500 + $60 = $560.

The word "simple" in simple interest means something precise: interest is calculated only on the original principal, every year. In year 1 you earn $20, in year 2 another $20, in year 3 another $20. The interest never builds on itself — it stays flat. This makes growth **linear**: a graph of total value over time is a straight line. Double the time, double the interest. Triple the time, triple the interest. That predictable linearity is what distinguishes simple interest from compound interest, where interest earned in one period starts earning interest of its own in the next.

A quick way to catch errors is to check units. P is in dollars, r is in "per year," and t is in years — so r × t produces a dimensionless number (years cancel years), and P × r × t gives dollars of interest. If you forget the percent-to-decimal conversion and write r = 4 instead of r = 0.04, you get an answer exactly 100 times too large. That unit check is also a reminder that if the time isn't given in years, you must convert: 6 months is t = 0.5, not t = 6.
