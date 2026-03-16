---
id: financial-analysis-valuation-fundamentals
title: Financial Statement Analysis for Valuation
domain: economics
course: financial-economics
prerequisites:
- id: stock-valuation-fundamentals
  type: hard
builds-toward:
- free-cash-flow-dcf-valuation
tags:
- financial-analysis
- accounting
- valuation
stage: formal-systems
status: draft
---

# Financial Statement Analysis for Valuation

## Core Idea
Proper valuation requires understanding balance sheet items, income statement quality, and cash flow statement structure. Adjustments for one-time items, working capital changes, and capitalization policies ensure comparability across firms and over time.

## How It's Best Learned
Analyze income statements and balance sheets to compute operating margins, asset turnover, and return on equity. Reconcile net income to operating cash flow to assess earnings quality.

## Explainer

From your work on stock valuation, you know that a firm's value equals the present value of its future cash flows. Financial statement analysis is the discipline of extracting reliable estimates of those cash flows from the three accounting statements a company publishes: the income statement, the balance sheet, and the cash flow statement. Each statement answers a different question, and each contains different kinds of distortions that analysts must unwind before they can be used for valuation.

The **income statement** shows revenues, expenses, and profit over a period. Its central problem is that it follows **accrual accounting**: revenue is recognized when earned, not when cash is received, and expenses when incurred, not when paid. A company that books $100M in sales but collects $70M in cash has a more precarious position than the income statement suggests. Analysts also flag **non-recurring items** — asset sale gains, restructuring charges, litigation settlements — that inflate or deflate a single year's earnings without reflecting the firm's ongoing earning power. Stripping out one-time items yields **normalized earnings**, a more stable base for projection.

The **balance sheet** snapshot shows assets, liabilities, and equity at a point in time. For valuation, the key concerns are **working capital dynamics** and **capitalization policies**. Changes in accounts receivable, inventory, and accounts payable affect how much of operating profit becomes actual cash. A firm with rising receivables is recognizing revenue it has not yet collected — a potential red flag. Capitalization policy governs which costs are expensed (reducing current profit) versus capitalized (appearing as assets and depreciated over time). Software companies that capitalize development costs can report higher short-term profits; normalizing these choices is essential when comparing firms.

The **cash flow statement** reconciles net income to actual cash generated, divided into operating, investing, and financing activities. **Free cash flow** — operating cash flow minus capital expenditures — is the number that matters most for valuation, because it represents cash the firm generates that is not needed to sustain the business. A firm reporting high net income but negative free cash flow may be growing profitably on paper while burning cash in reality. The quality of earnings check is simple: how closely does net income track operating cash flow? Persistent large divergences suggest aggressive accounting or working capital problems.

The goal of financial statement analysis is to arrive at comparable, economically meaningful numbers. **Return on equity**, **operating margin**, and **asset turnover** computed directly from reported statements may be distorted by one-time items, varying accounting choices, or different capital structures. By restating financials — stripping non-recurrings, normalizing working capital, adjusting for operating leases — analysts put firms on a level playing field. Only then can you meaningfully apply valuation multiples or build a discounted cash flow model with confidence that the inputs reflect economic reality rather than accounting convention.
