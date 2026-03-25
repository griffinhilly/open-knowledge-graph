---
id: earnings-multiple-valuation
title: Price-to-Earnings Multiples and Comparable Company Valuation
domain: economics
course: financial-economics
prerequisites:
- id: price-earnings-valuation
  type: hard
- id: stock-valuation-fundamentals
  type: soft
- id: equity-valuation-growth-phases
  type: soft
- id: financial-ratio-framework
  type: soft
builds-toward:
- equity-valuation-multiples
tags:
- equity
- valuation
- multiples
- fundamentals
stage: formal-systems
status: validated
---
# Price-to-Earnings Multiples and Comparable Company Valuation

## Core Idea
Earnings multiples (P/E, PEG, EV/EBITDA) provide simple relative valuation by comparing companies to peers. Theoretical P/E depends on growth, risk, and payout ratio: P/E = (payout ratio × (1 + g)) / (r - g). Multiples work best when comparing similar firms, but ignore differences in quality, growth prospects, and risk that drive fundamental value differences.

## How It's Best Learned
Compare valuation multiples across a peer group and create a simple model linking multiples to fundamentals like growth and ROE.

## Questions

```yaml
- question: "Company A and Company B are in the same industry and both trade at a P/E of 20. An analyst concludes they are equally valued by the market. What is wrong with this conclusion?"
  type: multiple-choice
  options:
    - "Nothing — identical P/E ratios in the same industry confirm equivalent valuation"
    - "P/E should be compared to EV/EBITDA before drawing any conclusions"
    - "The identical multiple could reflect completely different growth rates, risk profiles, or payout ratios that happen to produce the same P/E"
    - "P/E is only valid for companies with positive earnings, so one company may have negative earnings"
  answer: 2
  explanation: "The theoretical P/E = payout ratio / (r - g). Two firms can reach P/E = 20 via very different combinations: high payout + low growth + low risk might equal 20, as could low payout + high growth + high risk. The multiple compresses all these drivers into one number, hiding what actually explains the valuation. Equal P/E ratios do not imply equivalent businesses, equivalent risk, or equivalent future returns — they only indicate the market currently prices each dollar of earnings at 20 dollars. Understanding what drives the multiple is essential before acting on a comparison."

- question: "An analyst is comparing a heavily leveraged company to a competitor with no debt. Why is EV/EBITDA generally preferred over P/E for this comparison?"
  type: multiple-choice
  options:
    - "EV/EBITDA is always higher than P/E, making it easier to spot undervaluation"
    - "EV/EBITDA uses enterprise value and pre-financing earnings, removing the distortion caused by different capital structures"
    - "P/E is affected by accounting choices for depreciation, while EV/EBITDA is not"
    - "EV/EBITDA is the only multiple accepted by regulators for public company comparisons"
  answer: 1
  explanation: "P/E is an equity multiple — it measures market cap divided by net income, which sits below interest expense on the income statement. A highly leveraged company has large interest charges that depress net income, making its P/E look artificially inflated relative to an unlevered peer. EV/EBITDA sidesteps this by using enterprise value (equity + net debt) in the numerator and EBITDA (earnings before interest and taxes, plus D&A) in the denominator. Both numerator and denominator are capital-structure-neutral, so the multiple reflects operating performance independent of financing choices. Option C is partially true but secondary to the leverage distortion."

- question: "All else being equal, a company with a lower required rate of return (r) should trade at a higher P/E ratio."
  type: true-false
  answer: true
  explanation: "The theoretical P/E = payout ratio / (r - g). The required return r appears in the denominator: as r decreases, the denominator shrinks and P/E rises. A lower required return means investors need less compensation for holding the stock — typically because it has lower risk (lower beta, more stable earnings). Lower-risk stocks are worth more relative to their current earnings because the future earnings stream is discounted less severely. This is why low-volatility, blue-chip companies often command premium P/E multiples even with modest growth expectations."

- question: "A stock trading at a P/E below its industry peers is necessarily undervalued and represents a buying opportunity."
  type: true-false
  answer: false
  explanation: "This is the central misconception of simple multiple analysis. The theoretical P/E = payout ratio / (r - g). A below-peer P/E could reflect: lower expected growth g (making the denominator larger), higher required return r due to higher risk, lower payout ratio, or genuine mispricing. The multiple alone cannot distinguish these. A company with a P/E of 10 vs. a peer P/E of 15 might be cheap — or it might have lower growth prospects, higher leverage risk, or structural competitive disadvantages that fully justify the discount. Multiples are starting points for investigation, not conclusions."

- question: "Why do equity analysts use multiples-based valuation alongside DCF analysis rather than relying on one method alone?"
  type: short-answer
  answer: "Each method has distinct failure modes. DCF is highly sensitive to terminal growth rate and discount rate assumptions — small changes in inputs produce large swings in value, so the output can be precisely wrong. Multiples-based analysis is grounded in what the market actually pays for comparable businesses, but it assumes the peer group is correctly priced and that the subject company is genuinely comparable. Using both methods together provides triangulation: if the DCF says a stock is worth $50 but comparable companies imply $25, the analyst must explain the gap — perhaps the DCF growth assumptions are too optimistic, or the company has genuine advantages not reflected in the peer median. Agreement between methods increases confidence; divergence flags assumptions to scrutinize."
  explanation: "The triangulation principle is key: relative valuation (multiples) anchors analysis in market reality; intrinsic valuation (DCF) anchors it in fundamental cash flows. Neither is authoritative alone. Multiples can be uniformly wrong if the entire peer group is mispriced (as in bubbles). DCFs can be uniformly wrong if the analyst's model misspecifies growth or risk. Analysts present both because the overlap and divergence between them is itself informative about where risk and uncertainty in the valuation lie."
```

## Explainer

From your prerequisite work on P/E valuation and stock fundamentals, you understand that a stock's intrinsic value depends on the cash flows it is expected to generate and the discount rate that reflects its risk. The dividend discount model gives us P = D/(r - g), where D is the next dividend, r is the required return, and g is the perpetual growth rate. Dividing both sides by earnings E gives the theoretical P/E ratio: P/E = (D/E) / (r - g) = (payout ratio) / (r - g). This formula is the bridge between **relative valuation** (comparing P/E multiples across companies) and **fundamental valuation** (discounting cash flows at a risk-adjusted rate). A stock trading at a higher P/E than peers is either expected to grow faster, has lower risk, or is simply overvalued — the multiple alone cannot distinguish these.

**Comparable company analysis (comps)** is the practical application of this logic. The process begins by assembling a peer group of companies with similar business models, competitive positions, and capital structures. You then compute standardized multiples — P/E (market cap divided by net income), **EV/EBITDA** (enterprise value divided by earnings before interest, taxes, depreciation, and amortization), PEG (P/E divided by expected growth rate) — for each peer and construct a distribution. The subject company's implied value range is derived by applying the peer median or mean multiple to its own earnings. EV/EBITDA is often preferred over P/E because it is capital-structure-neutral: using enterprise value (equity plus net debt) and EBITDA (pre-financing earnings) removes the distortions from different leverage levels, making cross-company comparison cleaner.

The theoretical P/E formula reveals exactly what drives multiple differences across firms. Higher expected growth g raises P/E because future earnings streams are larger. Lower required return r (lower risk, perhaps lower beta) raises P/E because those streams are discounted at a lower rate. A higher payout ratio mechanically raises P/E, though this is partly offset by the growth foregone from paying out rather than reinvesting. The **PEG ratio** — P/E divided by expected growth — is an attempt to control for growth differences, putting high-growth and low-growth firms on the same footing. A PEG below 1 is traditionally interpreted as potentially undervalued (you are paying less than one unit of P/E for each percentage point of growth), though this is a heuristic rather than a rigorous result.

The critical limitation of multiples is that they summarize everything into one number, hiding the underlying drivers. Two firms with identical P/E ratios can have completely different growth prospects, risk profiles, and return-on-equity characteristics that will lead to very different fundamental values. Comps analysis is most reliable when the peer group is genuinely comparable — similar industry economics, growth stage, and risk — and weakest when applied across companies with structural differences. In practice, equity analysts use multiples as a **sanity check** alongside DCF valuation: if the DCF says a stock is worth $50 but every comparable trades at a multiple implying $25, the analyst needs to explain that gap or revisit the DCF assumptions. The two methods triangulate rather than substitute for each other.
