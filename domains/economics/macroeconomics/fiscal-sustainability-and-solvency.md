---
id: fiscal-sustainability-and-solvency
title: Fiscal Sustainability and Solvency
domain: economics
course: macroeconomics
prerequisites:
- id: government-deficit-and-debt-dynamics
  type: hard
- id: fiscal-policy-sustainability
  type: soft
- id: discretionary-fiscal-policy-decisions
  type: soft
- id: crowding-out-and-fiscal-effects
  type: soft
builds-toward:
- fiscal-dominance-vs-monetary-independence
tags:
- fiscal-policy
- sustainability
- solvency
stage: advanced
status: validated
---
# Fiscal Sustainability and Solvency

## Core Idea
A government is fiscally sustainable if the present value of its current and future revenues equals the present value of current and future spending plus existing debt. Unsustainable deficits eventually force painful adjustments: higher taxes, spending cuts, inflation (if the central bank accommodates), or default. Assessing sustainability requires long-term budget projections and assumptions about demographic trends, growth, and interest rates.

## Questions

```yaml
- question: "Country A has a debt-to-GDP ratio of 120%, an interest rate of 2%, and GDP growth of 3%. Country B has debt at 60% of GDP, an interest rate of 5%, and growth of 1%. Which country faces a more problematic fiscal trajectory?"
  type: multiple-choice
  options:
    - "Country A, because its absolute debt ratio is twice Country B's"
    - "Country B, because r > g means its debt-to-GDP ratio will rise without primary surpluses, creating explosive dynamics"
    - "Country A, because high debt always signals fiscal irresponsibility regardless of growth rates"
    - "Both equally — any country with debt above 60% of GDP is on an unsustainable path"
  answer: 1
  explanation: "The critical diagnostic is r − g. In Country A, r (2%) < g (3%), so the denominator of the debt ratio grows faster than interest compounds the numerator — debt dynamics are self-correcting even with a small primary deficit. In Country B, r (5%) > g (1%), so debt compounds faster than the economy grows, and the debt ratio explodes without sustained primary surpluses. Country A's higher absolute debt level is much less alarming than Country B's unfavorable r − g dynamics. Fiscal sustainability is about trajectories, not snapshots."

- question: "The intertemporal government budget constraint (IGBC) says a government is solvent if:"
  type: multiple-choice
  options:
    - "Its annual deficit stays below 3% of GDP in every year"
    - "Its debt-to-GDP ratio remains below 60% at all times"
    - "The present value of all future primary surpluses equals the current outstanding debt stock"
    - "It can roll over maturing debt in financial markets without triggering a liquidity crisis"
  answer: 2
  explanation: "The IGBC is a long-run solvency condition, not a short-run liquidity rule. It says: Debt today = PV(future revenues) − PV(future non-interest spending). A government that runs large deficits now can still be solvent if it credibly commits to sufficiently large future primary surpluses. Conversely, a government running small deficits in a high-debt, slow-growth environment may violate the IGBC. The 3% and 60% rules (EU Stability and Growth Pact) are arbitrary political thresholds, not theoretically derived solvency conditions."

- question: "A government can sustain a primary deficit indefinitely as long as the economy's growth rate exceeds the interest rate on its debt."
  type: true-false
  answer: true
  explanation: "When g > r, the debt-to-GDP ratio's denominator grows faster than its numerator compounds. This means the ratio can remain stable or even fall even while the government runs a primary deficit — the economy 'grows its way out' of the debt. This was broadly true in many advanced economies during the post-WWII boom and arguably in the 2010s with near-zero interest rates. The r − g comparison is the fundamental reason why some high-debt countries are sustainable and some low-debt countries are not."

- question: "A government running a large fiscal deficit is necessarily on an unsustainable debt path."
  type: true-false
  answer: false
  explanation: "Sustainability depends on r − g dynamics and the long-run trajectory projected by the intertemporal budget constraint — not on the current deficit level alone. A rapidly growing economy with g > r can sustain a primary deficit indefinitely. A government may also run a temporary large deficit during a recession or emergency (like a war or pandemic) and return to primary surplus afterward, satisfying the IGBC over the long run. The question is always whether current policy, projected forward with realistic assumptions, converges to a stable debt ratio — not whether today's deficit is large."

- question: "Why is the comparison of r and g (interest rate minus growth rate) the primary diagnostic for fiscal sustainability rather than the absolute level of debt or the size of the current deficit?"
  type: short-answer
  answer: "Fiscal sustainability is fundamentally a question about debt dynamics over time, not a snapshot comparison. The debt-to-GDP ratio evolves according to: Δ(D/Y) ≈ (r − g)(D/Y) − primary surplus/Y. When r < g, the (r − g) term is negative, which means debt compounds more slowly than the economy grows — even a primary deficit leaves the ratio trending downward. When r > g, every dollar of debt compounds faster than the tax base grows, creating explosive dynamics that require primary surpluses to counteract. The absolute debt level matters only in proportion to this dynamic: a 120% debt ratio is benign with r − g = −1%, dangerous with r − g = +4%. The current deficit similarly says nothing about sustainability without knowing the long-run r − g environment."
  explanation: "This is why standard fiscal rules based on deficit-to-GDP or debt-to-GDP thresholds (like the EU's 3% and 60% rules) are theoretically unsatisfying: they fix on static levels rather than the dynamic forces that actually determine whether a debt path converges or diverges. The r − g comparison gives the correct analytical foundation, even though projecting it 30–50 years into the future involves large uncertainty about future growth rates and interest rates."
```

## Explainer

From your study of government deficit and debt dynamics, you know how the debt-to-GDP ratio evolves over time: it rises when the primary deficit (spending minus revenue, excluding interest payments) is positive, and when the interest rate on existing debt exceeds the economy's growth rate. **Fiscal sustainability** asks a more pointed question than "is the deficit large?" — it asks whether the government can credibly service its obligations over the long run without resorting to measures that would constitute a form of failure. A government that runs large deficits but is growing rapidly may be perfectly sustainable; one running a small deficit in a stagnant economy with high debt may not be.

The theoretical foundation is the **intertemporal government budget constraint** (IGBC). This says that the current stock of outstanding debt must equal the present value of all future **primary surpluses** — the excess of revenues over non-interest spending in every future period. Written informally: Debt today = PV(future revenues) - PV(future non-interest spending). If this constraint is satisfied, the government is solvent in principle: markets can expect it to repay. If the IGBC is violated — if the present value of projected primary surpluses falls short of current debt — then something must give. The adjustment options form a taxonomy of fiscal distress: **austerity** (raise taxes or cut spending to generate primary surpluses), **financial repression** (force domestic institutions to hold low-yield government debt), **inflation** (if the central bank monetizes deficits, eroding the real value of nominal debt), or **explicit default** (restructuring or repudiation). Which adjustment occurs depends on institutional constraints — central bank independence, legal protections for creditors, political economy of tax increases versus spending cuts.

The critical ratio in sustainability analysis is the comparison of **r - g**: the interest rate on government debt minus the GDP growth rate. When r < g, the economy grows faster than debt accumulates, and even a government running a primary deficit can see its debt-to-GDP ratio stabilize or fall — the denominator expands faster than the numerator. This was the situation in many advanced economies for decades after WWII, and arguably in the 2010s when interest rates were near zero. When r > g, debt dynamics are explosive without primary surpluses: each dollar of debt compounds faster than the economy that supports it, and the debt-to-GDP ratio rises without bound. The r - g comparison is thus the first diagnostic for fiscal sustainability — not the level of debt in isolation, but whether the dynamics are self-correcting or self-reinforcing.

Assessing sustainability in practice requires **fiscal projection models** that combine baseline assumptions about demographics (aging populations raise pension and healthcare costs), productivity growth, interest rates, and the political feasibility of revenue increases. These projections are inherently uncertain — a 1 percentage point change in the assumed long-run growth rate can swing the 30-year debt trajectory by tens of percentage points of GDP. The IMF's and Congressional Budget Office's fiscal sustainability reports illustrate how sensitive conclusions are to these assumptions. The practical implication for fiscal policy analysis: sustainability is not a binary assessment but a range of scenarios, and the relevant policy question is whether *current* policy, projected forward, converges to a stable debt ratio under reasonable assumptions — or whether it requires future adjustments whose political feasibility is doubtful. Countries that habitually rely on optimistic growth assumptions to declare sustainability are essentially deferring the adjustment, with compound interest accruing on the delay.
