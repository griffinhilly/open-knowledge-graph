---
id: sustainable-growth-rate
title: Sustainable Growth Rate and Retention Policy
domain: economics
course: financial-economics
prerequisites:
- id: stock-valuation-fundamentals
  type: hard
builds-toward:
- dividend-growth-valuation-model
tags:
- equity-valuation
- dividends
- growth
stage: formal-systems
status: draft
---

# Sustainable Growth Rate and Retention Policy

## Core Idea
Sustainable growth rate = ROE × retention ratio; it is the maximum rate a firm can grow using only retained earnings without external financing. Higher payout ratios reduce growth but may signal confidence or target mature companies.

## How It's Best Learned
Calculate sustainable growth for several companies with different payout policies. Observe how retention and ROE interact to determine dividend policy feasibility.

## Questions

```yaml
- question: "Firm A has ROE = 15% and a 40% dividend payout ratio. Firm B has ROE = 20% and an 80% dividend payout ratio. Which firm has the higher sustainable growth rate?"
  type: multiple-choice
  options:
    - "Firm B — it has the higher ROE regardless of payout policy"
    - "Firm A — SGR = 15% × 60% = 9% versus Firm B's 20% × 20% = 4%"
    - "Firm B — SGR = 20% × 80% = 16% versus Firm A's 15% × 40% = 6%"
    - "They are equal since both can issue equity to supplement internal growth"
  answer: 1
  explanation: "SGR = ROE × retention ratio = ROE × (1 − payout ratio). Firm A: 15% × 0.60 = 9%. Firm B: 20% × 0.20 = 4%. Despite Firm B's higher ROE, it retains only 20% of earnings, severely limiting self-financed growth. The common trap is focusing only on ROE — the interaction between ROE and retention determines SGR, and a high payout can overwhelm a high ROE."

- question: "A technology firm has ROE = 25% and retains all earnings (payout ratio = 0). Its actual revenue is growing at 40% annually. What must be true?"
  type: multiple-choice
  options:
    - "The firm's SGR is 40%, matching actual growth — high-growth firms automatically expand their SGR"
    - "The firm's SGR = 25%; since actual growth exceeds this, it must be increasing debt or issuing new equity"
    - "The firm is unsustainable and must immediately cut growth to 25%"
    - "SGR does not apply to firms with zero dividend payout"
  answer: 1
  explanation: "SGR = ROE × retention ratio = 25% × 1.0 = 25%. This is the maximum growth rate achievable using only retained earnings while keeping financial ratios constant. Actual growth of 40% exceeds this, meaning internal equity generation is insufficient. The gap must be funded by external equity (new share issuance) or additional debt — the firm's capital structure is changing, whether intentionally or not."

- question: "A firm that raises its dividend payout ratio will typically increase its sustainable growth rate, because investors respond positively to higher dividends."
  type: true-false
  answer: false
  explanation: "Raising the payout ratio lowers the retention ratio, which directly reduces SGR = ROE × retention ratio. More dividends mean less retained earnings available to fund future growth internally. The claim confuses investor signaling effects (possible stock price reactions) with the mechanical relationship between retention and growth capacity. SGR purely reflects how much equity the firm accumulates through retained earnings — higher payout unambiguously reduces it."

- question: "A firm consistently growing faster than its sustainable growth rate without issuing new equity will see its debt-to-equity ratio rise over time."
  type: true-false
  answer: true
  explanation: "SGR is defined as the growth rate at which all financial ratios — including leverage — remain constant. Growth faster than SGR means retained earnings alone cannot fund all new assets. The shortfall must come from debt, which grows the liability side faster than equity. Each year, debt-to-equity rises. If unchecked, this rising leverage can become financially unsustainable — making SGR a useful warning signal for credit analysis, not just equity valuation."

- question: "A mature utility company and a high-growth technology startup both have ROE = 18%. Explain why it might make financial sense for them to have very different dividend payout ratios."
  type: short-answer
  answer: "The key is the return available on reinvested earnings relative to shareholders' opportunity cost. The utility has limited high-return reinvestment opportunities — retaining earnings to fund mediocre projects destroys value compared to distributing them. A high payout is appropriate. The tech startup likely has abundant projects earning well above its cost of capital; retaining earnings to fund those creates value. A low payout (high retention) maximizes SGR and compounds value internally. Payout policy should match the firm's investment opportunity set."
  explanation: "SGR = ROE × retention ratio. Same ROE × different retention = different SGR. The utility's high payout yields low SGR, which is fine since it doesn't need rapid growth. The startup's low payout yields high SGR, funding the growth that generates its value. Forcing the startup to pay dividends would require it to reissue equity at a cost to fund projects it should have funded with retained earnings — value destruction. This is why dividend policy cannot be evaluated independently of investment opportunities."
```

## Explainer

From stock valuation fundamentals, you learned that a firm's value depends on its future cash flows, which depend in part on how fast it can grow. But growth does not come for free — it requires capital. A firm can finance growth by retaining earnings, issuing new equity, or borrowing. This topic asks a foundational question: **how fast can a firm grow using only the profits it generates internally, without changing its capital structure or issuing new shares?**

The answer is the **sustainable growth rate (SGR) = ROE × b**, where **ROE** (return on equity) measures the rate at which the firm converts its equity base into new earnings, and **b** is the **retention ratio** (the fraction of earnings kept rather than paid out as dividends). The logic is direct: if a firm earns 20% on equity and retains 60% of those earnings, it adds 12% to its equity base from internal sources each year. If assets, revenues, and liabilities all grow proportionally to equity, the firm can sustain 12% growth without external financing. Growth beyond this rate requires issuing new equity or taking on additional debt — either of which changes the firm's financial structure.

Since retention ratio = 1 − payout ratio, SGR = ROE × (1 − payout ratio). This reveals the fundamental trade-off in dividend policy: every dollar paid as a dividend is a dollar not reinvested to fund growth. A **mature firm** with few high-return investment opportunities should pay high dividends — retaining earnings to reinvest at mediocre returns destroys value compared to distributing them. A **high-growth firm** with abundant opportunities earning returns well above its cost of capital should retain most earnings rather than paying dividends and then reissuing equity at a cost. The payout ratio is not just a distribution decision; it implicitly determines how much growth the firm can self-finance.

The SGR formula also embeds **DuPont decomposition** insights. ROE = profit margin × asset turnover × financial leverage (Net Income/Sales × Sales/Assets × Assets/Equity). A firm can improve its SGR by improving operating margins, using assets more efficiently, or taking on more leverage — though leverage raises financial risk and is not free. This makes SGR useful as a diagnostic: two firms with identical SGRs may achieve them through very different means, one through operational excellence and the other through high leverage, with very different risk profiles and sustainability.

Crucially, SGR assumes the firm maintains its current financial ratios. If actual growth exceeds the SGR, something must give: the firm must issue new equity, increase its debt ratio, or accept that some ratios will change. Firms that consistently grow faster than their SGR without raising equity are implicitly accumulating debt — their leverage is rising with each passing year. If this trajectory is not corrected, it can become financially unsustainable. SGR is therefore a valuable benchmark not just for equity valuation but for credit analysis: a firm whose planned growth far exceeds its SGR deserves scrutiny about how that gap will be financed.
