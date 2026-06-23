---
id: compound-interest
title: Compound Interest
domain: practical-life-skills
course: financial-literacy
prerequisites:
- id: time-value-of-money-personal
  type: hard
- id: exponential-growth-and-decay
  type: soft
- id: percent-concept
  type: soft
- id: exponents-intro
  type: soft
- id: exponential-functions-and-graphs
  type: soft
- id: percent-of-a-number
  type: soft
- id: financial-numeracy-and-quantitative-literacy
  type: soft
builds-toward:
- inflation-and-purchasing-power
- debt-management-strategies
- investment-risk-and-return
- mortgage-and-home-buying
tags:
- compound-interest
- exponential-growth
- savings
- debt
stage: formal-systems
status: validated
---

# Compound Interest

## Core Idea
Compound interest means earning interest on previously earned interest, not just on the principal. The formula A = P(1 + r/n)^(nt) shows how principal P grows at annual rate r compounded n times per year for t years. Compounding frequency matters: more frequent compounding yields more growth. Compound interest works powerfully in your favor when saving and investing, but against you when carrying debt.

## How It's Best Learned
Use the Rule of 72: divide 72 by the annual interest rate to estimate how many years it takes to double money. Compare a savings account at 5% versus credit card debt at 22% to viscerally see both sides of compounding.

## Common Misconceptions
- Many people believe interest is always simple (applied only to principal); most real-world financial products use compound interest.
- Starting early matters more than contributing more — a 10-year head start can outweigh twice the contributions started later.

## Questions

```yaml
- question: "You invest $1,000 at 6% annual interest compounded annually. After 2 years, how much interest have you earned (rounded to the nearest cent)?"
  type: multiple-choice
  options: ["$120.00", "$123.60", "$60.00", "$126.00"]
  answer: 1
  explanation: "Year 1: $1,000 x 0.06 = $60 interest, balance = $1,060. Year 2: $1,060 x 0.06 = $63.60 interest, balance = $1,123.60. Total interest = $123.60. The key difference from simple interest ($120.00) is the $3.60 earned on Year 1's interest — that is the compounding effect. Option A ($120) is the simple interest answer, which is the most common error."

- question: "Compound interest mainly benefits savers. Borrowers are not affected by compounding."
  type: true-false
  answer: false
  explanation: "Compounding works identically for debt. Credit card balances, mortgages, and student loans all compound — meaning you pay interest on previously accumulated interest. A $5,000 credit card balance at 22% APR grows alarmingly fast if only minimum payments are made. Compound interest is a neutral mathematical force that amplifies both savings and debt."

- question: "Explain why someone who starts saving $200/month at age 25 can end up with more money at 65 than someone who saves $400/month starting at age 35, assuming the same interest rate."
  type: short-answer
  answer: "The person starting at 25 has 10 extra years of compounding. Those early contributions earn interest for 40 years instead of 30, and the interest itself earns interest for longer. Exponential growth means time matters more than contribution size."
  explanation: "With 7% annual returns: $200/month for 40 years grows to roughly $528,000. $400/month for 30 years grows to roughly $489,000. The early starter contributes $96,000 in principal while the late starter contributes $144,000 — yet the early starter ends up with more. This is the most powerful practical lesson of compound interest: time is the dominant variable."
```

## Explainer

You already understand that money has a time value — a dollar today is worth more than a dollar tomorrow. Compound interest is the specific mechanism that makes this true in practice. It is the engine behind both wealth building and debt accumulation, and understanding it deeply will influence every major financial decision you make.

Start with the simplest case. You deposit $1,000 in an account earning 5% per year. After one year, you earn $50 in interest and your balance is $1,050. Here is where compounding enters: in year two, you earn 5% on $1,050 — not just on the original $1,000. That gives you $52.50 in interest, bringing your balance to $1,102.50. The extra $2.50 seems trivial, but it is interest earned on interest, and this effect accelerates over time. By year 30, that original $1,000 has grown to $4,321.94 — more than four times the original amount — without you adding another cent.

The formula A = P(1 + r/n)^(nt) captures this precisely. P is your principal (starting amount), r is the annual interest rate, n is how many times per year interest compounds, and t is the number of years. The exponent nt is what makes this exponential growth rather than linear. When you double the time, you do not double the result — you get dramatically more because each period builds on every previous period's accumulated growth. The Rule of 72 gives you a quick mental estimate: divide 72 by the interest rate to approximate the doubling time. At 6%, money doubles roughly every 12 years; at 12%, every 6 years.

Compounding frequency matters, but less than most people think. An account compounding monthly at 6% yields slightly more than one compounding annually at 6% (6.17% effective vs. 6.00%). The difference between daily and monthly compounding is even smaller. What matters far more than compounding frequency is the interest rate and, above all, time. This is why financial advisors emphasize starting early: the first ten years of contributions have the longest runway for compounding and often produce more final wealth than contributions made later, even if the later amounts are larger.

The uncomfortable flip side is that compound interest works exactly the same way on debt. A credit card charging 22% APR compounds your unpaid balance relentlessly. If you carry a $5,000 balance and make only minimum payments, you may pay more in total interest than the original purchase price. The same mathematical force that can turn modest savings into substantial wealth can turn modest debts into crushing obligations. Recognizing this symmetry — that compounding is neutral, amplifying whatever direction money flows — is the most important practical insight in personal finance.
