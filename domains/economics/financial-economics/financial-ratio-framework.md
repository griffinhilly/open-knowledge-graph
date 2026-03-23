---
id: financial-ratio-framework
title: Financial Ratio Analysis and Comparative Valuation
domain: economics
course: financial-economics
prerequisites:
- id: financial-analysis-valuation-fundamentals
  type: hard
- id: stock-valuation-fundamentals
  type: soft
builds-toward:
- equity-valuation-growth-phases
tags:
- financial-analysis
- ratios
- fundamentals
- valuation
stage: formal-systems
status: validated
---

# Financial Ratio Analysis and Comparative Valuation

## Core Idea
Financial ratios distill accounting information into dimensionless measures for comparability across firms and time. Profitability ratios (ROE, ROA, margins), leverage ratios (debt/equity, interest coverage), efficiency ratios (asset turnover, receivables days), and valuation ratios (P/E, Price/Book) reveal financial health and cheapness. Ratio analysis is most powerful when tracking changes over time and comparing to peers and benchmarks.

## How It's Best Learned
Build a financial ratio spreadsheet for a peer group of companies, calculate historical trends, and correlate ratios to stock returns.

## Questions

```yaml
- question: "Company A reports a 20% Return on Equity. An analyst concludes this is strong performance. What critical piece of information is missing from this analysis?"
  type: multiple-choice
  options:
    - "The company's absolute net income in dollars"
    - "The industry average ROE and the company's historical ROE trend"
    - "The number of shares outstanding"
    - "Whether the company pays a dividend"
  answer: 1
  explanation: "A ratio in isolation tells you almost nothing. 20% ROE is extraordinary in capital-intensive regulated industries like utilities where 8-10% is typical, but mediocre in software where 30%+ is achievable. Without the peer group median and the firm's own trend, you cannot evaluate whether 20% represents strength or underperformance. This is the central insight of ratio analysis: ratios derive meaning from comparison, not from the number itself. The analyst's mistake is treating the ratio as self-interpreting."

- question: "A company has an interest coverage ratio (EBIT / interest expense) of 1.2x. What does this most directly signal to a credit analyst?"
  type: multiple-choice
  options:
    - "The company is over-leveraged relative to its equity base"
    - "The company may struggle to meet its interest payments from operating earnings"
    - "The company has excessive cash holdings relative to its debt"
    - "The company's stock is likely overvalued relative to peers"
  answer: 1
  explanation: "Interest coverage measures whether operating earnings (EBIT) cover interest obligations. A ratio of 1.2x means EBIT exceeds interest by only 20% — a thin cushion. Credit analysts treat coverage below 1.5x as a warning sign because any deterioration in operating performance could leave the firm unable to service debt. Note that coverage is a flow measure (earnings vs. interest expense) rather than a stock measure (total debt vs. equity), making it more immediately relevant to near-term payment ability than the debt-to-equity ratio."

- question: "A company with a very high ROE could actually be in a weaker financial position than a company with a moderate ROE."
  type: true-false
  answer: true
  explanation: "ROE = net income / equity. Equity can be artificially small if the company is heavily leveraged — substantial debt replaces equity on the balance sheet. A highly leveraged firm can show an impressive ROE not because operations are efficient but because the equity denominator is small. This leverage amplifies both returns and risk: in a downturn, the same leverage that inflated ROE now amplifies losses. A complete picture requires examining leverage ratios alongside ROE. DuPont decomposition explicitly links ROE to profit margin, asset turnover, and leverage to reveal these drivers."

- question: "A high Price-to-Earnings (P/E) ratio means the market considers the stock expensive and investors should avoid it."
  type: true-false
  answer: false
  explanation: "A high P/E reflects market expectations of future earnings growth, not necessarily overvaluation. Growth companies justifiably trade at high P/E multiples because investors are paying for future earnings power, not just current earnings. A 'cheap' P/E stock might be cheap because the market expects earnings to decline. P/E interpretation requires context: is this firm growing faster than peers? Is high P/E justified by a strong competitive position? P/E is a starting point for valuation analysis, not a direct buy/sell signal. Low P/E can be a value opportunity or a value trap; high P/E can be reasonable growth pricing or genuine overvaluation."

- question: "Why is a single financial ratio, even one calculated correctly, insufficient to evaluate a company's financial health?"
  type: short-answer
  answer: "Each ratio family captures only one dimension of financial health: profitability, leverage, efficiency, or valuation. These dimensions can conflict — a company can be highly profitable but dangerously leveraged, or efficiently run but overvalued. Ratios are also meaningless without benchmarks: a ratio only signals 'high' or 'low' relative to industry peers and the firm's own history. A complete picture requires reading multiple ratio families together and comparing across time and competitors."
  explanation: "This is the core discipline of ratio analysis as a framework rather than a checklist. ROE alone might look strong while interest coverage signals danger. Asset turnover might be high while receivables days signal customers are slow to pay. No single number captures the full financial picture, which is exactly why analysts build ratio dashboards across all four families — profitability, leverage, efficiency, and valuation — and interpret them as an integrated system rather than individually."
```

## Explainer

Raw accounting numbers — $4 billion in net income, $80 billion in assets — tell you little on their own. Is $4 billion impressive? It depends on how much capital was deployed to generate it and how the figure compares to competitors. **Financial ratios** convert these absolute numbers into dimensionless measures that are comparable across firms of different sizes and across time. Building on the valuation fundamentals you already know, ratios are the working toolkit of equity analysts, credit officers, and corporate strategists.

The ratio landscape organizes naturally into four families. **Profitability ratios** measure how efficiently the firm converts resources into earnings. Return on Equity (ROE = net income / equity) tells shareholders how much profit was generated per dollar they own. Return on Assets (ROA = net income / total assets) abstracts from financing to measure operational efficiency. Net margin (net income / revenue) tells you what fraction of each revenue dollar survives as profit. These ratios are meaningless in isolation; a 12% ROE is outstanding in regulated utilities but mediocre in software. Comparison to peers and to the firm's own history is essential.

**Leverage ratios** measure financial risk — how much of the firm's assets are financed by debt rather than equity. Debt-to-equity (total debt / equity) and interest coverage (EBIT / interest expense) reveal whether the firm can service its obligations. High leverage amplifies both returns and risk: a firm with 50% debt/capital magnifies equity returns in good times and magnifies losses in downturns. Credit analysts focus heavily on interest coverage because a ratio below 1.5x signals the firm may struggle to meet interest payments. **Efficiency ratios** measure how productively the firm uses its assets — asset turnover (revenue / assets) measures sales generated per dollar of assets, while receivables days (accounts receivable / daily sales) measures how quickly customers pay.

**Valuation ratios** link market prices to fundamentals, connecting accounting statements to the stock valuation models you know. Price-to-Earnings (P/E) tells you how many dollars investors pay per dollar of current earnings — high P/E implies expectations of future growth. Price-to-Book compares market value to accounting book value; P/B above 1 means the market believes the firm earns above its cost of capital. These multiples are the foundation of **comparable company analysis**: you value a private firm or assess whether a public firm is cheap by computing the median P/E of peers and applying it to the target's earnings. The power of ratio analysis is that it reduces a complex financial statement to a handful of numbers that reveal, when read together, whether a business is profitable, efficient, financially safe, and reasonably priced.
