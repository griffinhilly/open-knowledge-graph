---
id: government-debt-fiscal-sustainability
title: Government Debt and Fiscal Sustainability
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: ricardian-equivalence
  type: soft
- id: intergenerational-equity-fiscal-policy
  type: hard
tags:
- government-debt
- fiscal-sustainability
- long-run
stage: advanced
status: draft
---

# Government Debt and Fiscal Sustainability

## Core Idea
Fiscal sustainability requires that government debt does not grow faster than the economy indefinitely. The fundamental intertemporal budget constraint shows that if the real interest rate exceeds the growth rate, debt-to-GDP ratios will eventually explode unless primary deficits shrink. Sustainability analysis examines whether current tax and spending policies are viable long-term or require future adjustments. Countries with high debt levels face constraints on fiscal policy and higher refinancing costs, potentially triggering crises.

## Questions

```yaml
- question: "Country A has debt/GDP = 100%, real interest rate r = 5%, and growth rate g = 2%. Country B has the same debt ratio but r = 2% and g = 5%. Which country faces a more urgent fiscal challenge, and why?"
  type: multiple-choice
  options:
    - "Country A, because its interest-growth differential (r − g) is positive, so debt grows faster than the economy without primary surpluses"
    - "Country B, because higher growth creates more public spending pressure"
    - "Both face equal challenges since they have identical debt-to-GDP ratios"
    - "Country A, because higher interest rates attract foreign capital and worsen trade balances"
  answer: 0
  explanation: "The law of motion Δb ≈ (r − g)·b + d shows that what matters is the interest-growth differential, not the debt level alone. Country A has r − g = +3%, so each year the debt ratio automatically rises by 3 percentage points of GDP from interest compounding alone — requiring a large primary surplus just to stabilize. Country B has r − g = −3%, meaning the economy grows faster than its debt, and the ratio falls even with modest primary deficits. Same debt, opposite trajectories."

- question: "A government is running a primary surplus of 1% of GDP. Under what condition can the debt-to-GDP ratio still rise?"
  type: multiple-choice
  options:
    - "When the government has high total spending regardless of revenue"
    - "When the real interest rate exceeds the growth rate by enough that interest costs outpace the primary surplus"
    - "When the central bank raises interest rates, making new borrowing more expensive"
    - "When credit rating agencies downgrade the country's sovereign debt"
  answer: 1
  explanation: "The debt dynamics equation is Δb ≈ (r − g)·b + d. Even with a primary surplus (d < 0), the first term (r − g)·b can dominate if the interest-growth differential is large and the debt stock is high. For example, with b = 120%, r − g = 3%, the automatic debt increase is 3.6% of GDP per year; a 1% primary surplus leaves a net increase of 2.6% of GDP. Primary surpluses must exceed the interest-growth differential times the debt ratio to stabilize."

- question: "A country with g > r can run a sustained primary deficit and still see its debt-to-GDP ratio decline over time."
  type: true-false
  answer: true
  explanation: "When the growth rate exceeds the real interest rate, the economy outgrows its debt. The Δb equation shows that even with d > 0 (a primary deficit), if (r − g)·b is sufficiently negative, the debt ratio falls. This was approximately the situation in many advanced economies in the post-WWII decades, when strong growth and low interest rates allowed debt accumulated during the war to shrink relative to GDP without requiring fiscal austerity."

- question: "A country with a 150% debt-to-GDP ratio is necessarily on an unsustainable fiscal path."
  type: true-false
  answer: false
  explanation: "Sustainability depends on the interest-growth differential and primary balance trajectory, not the raw debt level. Japan has long maintained debt ratios well above 200% with low interest rates and domestic financing without a fiscal crisis. A high debt ratio combined with r < g and a commitment to even a small primary surplus can be entirely sustainable. Conversely, a 40% debt ratio with r >> g and persistent primary deficits is unsustainable. The debt level in isolation tells you little."

- question: "Why is the interest-growth differential (r − g) more important than the absolute size of the debt-to-GDP ratio in determining fiscal sustainability?"
  type: short-answer
  answer: "The differential determines whether existing debt compounds faster or slower than the economy grows. If r > g, each unit of debt generates interest costs that exceed the additional tax capacity created by growth, so the ratio spirals upward without ever-increasing primary surpluses. If g > r, GDP growth dilutes the debt burden automatically. The same debt level can be self-correcting or explosive depending entirely on this differential — which is why sustainability analysis centers on the trajectory implied by r, g, and the primary balance, not on the current stock of debt."
  explanation: "An analogy: a mortgage is manageable or crushing depending on whether your income grows faster or slower than your interest payments, not on the nominal dollar amount you borrowed. The intertemporal budget constraint formalizes this: the present value of future surpluses must cover current debt, and the discount rate for that calculation is (r − g). When r > g, the discount rate is positive, making future surpluses less valuable and required surpluses larger."
```

## Explainer

From your study of Ricardian equivalence and intergenerational fiscal policy, you know that government borrowing shifts tax burdens across time and across generations. Fiscal sustainability asks the most basic version of this question: can the government keep doing what it is currently doing, or must taxes eventually rise or spending fall to prevent debt from spiraling out of control?

The starting point is the **government budget constraint** expressed in terms of the debt-to-GDP ratio. Let *b* denote the debt-to-GDP ratio, *r* the real interest rate on government debt, *g* the real growth rate of GDP, and *d* the primary deficit (spending minus taxes, excluding interest payments) as a share of GDP. The law of motion is approximately: Δb ≈ (r − g)·b + d. This equation reveals the critical role of the **interest-growth differential** (r − g). When the interest rate exceeds the growth rate, each unit of existing debt grows faster than the economy, requiring ever-larger primary surpluses just to stabilize the debt ratio. When growth exceeds the interest rate, the economy "outgrows" its debt, and even modest primary deficits can be sustained indefinitely.

Consider two concrete scenarios. Country A has a debt-to-GDP ratio of 100%, r = 5%, and g = 3%. The interest-growth differential is +2%, meaning the debt ratio automatically rises by 2 percentage points of GDP per year from interest alone. To merely stabilize the ratio, Country A must run a primary surplus of 2% of GDP every year — a significant fiscal effort requiring either higher taxes or lower spending than current levels. Country B has the same debt ratio but r = 2% and g = 4%. The differential is −2%, meaning the economy grows faster than the debt, and Country B can actually run a primary deficit of 2% of GDP while still seeing its debt ratio fall. The same debt level is sustainable or unsustainable depending entirely on the interest-growth environment.

The **intertemporal budget constraint** formalizes this: the present value of all future primary surpluses must equal the current stock of outstanding debt. If projected surpluses fall short — because of aging populations increasing pension and healthcare costs, or because political constraints prevent tax increases — the debt path is unsustainable. Markets may tolerate unsustainable paths for years, but eventually rising debt raises borrowing costs (increasing *r*), which worsens the interest-growth differential, which accelerates debt accumulation — a vicious cycle that can culminate in a fiscal crisis, forced austerity, or default. This is why sustainability analysis focuses not on the current debt level in isolation but on the trajectory implied by existing policies, interest rates, and growth prospects.
