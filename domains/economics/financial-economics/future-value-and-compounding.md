---
id: future-value-and-compounding
title: Future Value and Compounding
domain: economics
course: financial-economics
prerequisites:
- id: time-value-of-money
  type: hard
- id: exponential-growth-and-decay
  type: soft
- id: geometric-sequences-and-series
  type: soft
builds-toward:
- annuities-and-perpetuities
tags:
- future-value
- compounding
- interest
- growth
stage: formal-systems
status: validated
---

# Future Value and Compounding

## Core Idea
Future value (FV) measures how much a present sum will be worth after earning returns over time: FV = PV × (1+r)^t. Compounding means earning returns on previously earned returns, causing wealth to grow exponentially rather than linearly. More frequent compounding periods (monthly vs. annual) raise the effective annual yield; in the continuous limit, FV = PV × e^(rt). The power of compounding over long horizons is often dramatically underestimated by intuition calibrated to linear thinking.

## How It's Best Learned
Compare simple interest vs. compound interest over 30-year horizons to see the difference compounding makes. The Rule of 72 — divide 72 by the interest rate to approximate the doubling time — is a powerful shortcut for building intuition. Simulate different compounding frequencies in a spreadsheet.

## Common Misconceptions
- Daily vs. monthly compounding makes little practical difference compared to the effect of the interest rate itself — students overweight compounding frequency.
- Forgetting taxes and fees when projecting future wealth leads to significant over-optimism in retirement planning.

## Explainer

The time value of money — your prerequisite — establishes that a dollar today is worth more than a dollar tomorrow because today's dollar can be invested to earn a return. Future value makes this concrete: it answers the question "if I invest PV dollars today at annual rate r, what will it be worth in t years?" The answer, FV = PV × (1+r)ᵗ, follows directly from the structure of compounding. After year 1, you have PV(1+r). After year 2, you earn r on the entire PV(1+r), giving PV(1+r)². The (1+r)ᵗ factor accumulates these multiplications, and its exponential shape — familiar from your work on geometric sequences — is what makes long time horizons so consequential.

The word **compounding** captures the key mechanism: you earn returns not only on your original principal but on the accumulated returns from prior periods. Compare simple interest (interest only on principal) to compound interest: $1,000 at 8% simple interest grows by $80/year, reaching $3,400 in 30 years. At 8% compound interest, it grows to $1,000 × (1.08)^30 ≈ $10,063 — nearly ten times the original. The gap between $3,400 and $10,063 is entirely due to reinvesting the interest. This is why the **Rule of 72** is so striking: divide 72 by the interest rate to estimate the doubling time. At 8%, money doubles roughly every 9 years; at 6%, every 12 years. Applied repeatedly, an investment at 8% roughly multiplies by 16 in 36 years.

**Compounding frequency** extends the logic: what if interest is credited monthly rather than annually? An annual rate r compounded m times per year yields FV = PV × (1 + r/m)^(mt). At the limit as m → ∞, this converges to **continuous compounding**: FV = PV × e^(rt), connecting directly to your knowledge of exponential functions. Continuous compounding is the mathematical idealization used frequently in finance and derivative pricing because it simplifies algebra considerably. The practical difference between daily and monthly compounding on a given annual rate is small, but understanding the formula matters for comparing instruments quoted with different compounding conventions — APR versus APY, for instance.

Two common traps distort intuition about compounding. First, people underestimate the impact of long time horizons because the relationship is exponential, not linear — the final years of accumulation contribute more absolute dollars than the early years, even at the same rate. Second, fees and taxes compound just as surely as returns, but subtractively. A 1% annual management fee on a growing fund doesn't just cost 1% of the final amount — it costs 1% per year, compounded against the fund's full value, quietly eroding wealth over decades. These insights from future value become essential prerequisites when you move to annuities, bond pricing, and net present value calculations, where streams of future cash flows must each be discounted back using (1+r)^t.
