---
id: total-average-marginal-product-labor
title: Total, Average, and Marginal Product of Labor
domain: economics
course: microeconomics
prerequisites:
- id: production-function-microeconomics
  type: hard
builds-toward:
- marginal-revenue-product-factor
tags:
- production
- productivity
- labor
stage: formal-systems
status: draft
---

# Total, Average, and Marginal Product of Labor

## Core Idea
Total Product (TP) is total output from a given amount of labor. Average Product (AP) is output per worker (TP/L). Marginal Product (MP) is the additional output from one more worker. Typically, AP and MP initially rise (specialization gains) then fall (congestion, diminishing returns). The MP curve intersects AP at its maximum, fundamental to understanding hiring decisions.

## How It's Best Learned
Create a table with workers (1,2,3...), total output, AP, and MP. Plot both curves. See that MP rises then falls, and where MP cuts AP.

## Common Misconceptions
- Diminishing returns means output falls (it means the rate of increase slows; output still rises).
- Firms hire workers until MP = 0 (they stop when MP falls below wage relative to price of output).

## Questions

```yaml
- question: "A firm currently employs 8 workers with an average product of 30 units per worker. The 9th worker would add 24 units of output. What happens to the average product after hiring the 9th worker?"
  type: multiple-choice
  options:
    - "AP rises, because the firm is producing more total output"
    - "AP falls, because the marginal worker produces less than the current average"
    - "AP stays the same, because average product depends only on capital, not labor"
    - "AP rises to 24, matching the marginal worker's output"
  answer: 1
  explanation: "When marginal product is below average product (24 < 30), the new worker pulls the average down — just as a below-average test score lowers your overall average. AP will fall. This is a mathematical identity: MP > AP implies AP is rising; MP < AP implies AP is falling; MP = AP at exactly AP's peak. Option A confuses rising total output (which is true — output went from 240 to 264) with rising average output per worker (which is false)."

- question: "A bakery employs 10 workers. The 11th worker would add 45 loaves per day. Each loaf sells for $2, and the daily wage is $120. Should the bakery hire the 11th worker?"
  type: multiple-choice
  options:
    - "Yes — marginal product is still positive, so the worker adds to total output"
    - "Yes — the firm should hire until output is maximized"
    - "No — the value of the 11th worker's output is less than the wage"
    - "No — diminishing returns means the bakery is already overstaffed"
  answer: 2
  explanation: "The marginal revenue product of the 11th worker is MP × price = 45 × $2 = $90, which is less than the $120 wage. Hiring this worker adds $90 in revenue but costs $120, reducing profit by $30. The firm stops hiring when MRP = wage, not when MP = 0. Option A is the classic misconception: positive MP means output rises, but the worker may still cost more than they produce. Diminishing returns (option D) is irrelevant on its own — what matters is whether MRP covers the wage."

- question: "Diminishing marginal returns occurs when additional workers cause total output to fall."
  type: true-false
  answer: false
  explanation: "Diminishing marginal returns means each additional worker adds less output than the one before — MP is declining but still positive. Total output continues to rise, just at a decreasing rate. Output only falls if MP becomes negative, which requires additional workers to actively impede production (e.g., severe crowding). The distinction matters: a firm experiencing diminishing returns still benefits from each worker; it just benefits less with each hire."

- question: "The marginal product curve must intersect the average product curve exactly at average product's maximum."
  type: true-false
  answer: true
  explanation: "This is a mathematical identity, not a coincidence. When a new worker produces more than the current average (MP > AP), they pull the average up — AP is rising. When a new worker produces less than the average (MP < AP), they drag it down — AP is falling. Therefore, at the exact moment AP transitions from rising to falling (its maximum), MP must equal AP. This logic applies to any average-marginal pair: class averages, batting averages, etc."

- question: "Why do profit-maximizing firms stop hiring workers before marginal product reaches zero?"
  type: short-answer
  answer: "A firm compares the value of an additional worker's output — the marginal revenue product (MP × output price) — against the wage. When MRP exceeds the wage, hiring adds more to revenue than to cost. When MRP falls below the wage, the last worker costs more than they generate. The firm stops where MRP = wage. Since wages are positive and output prices are positive, MRP reaches zero only when MP = 0, so firms always stop well before MP hits zero."
  explanation: "The intuition 'hire until MP = 0' ignores the cost of labor. Diminishing returns drive MP down, but the firm must stop as soon as the dollar value of that declining MP falls below the wage — typically at a substantial positive MP level. Only if labor were free (wage = 0) would a firm rationally hire until MP = 0."
```

## Explainer

From the production function, you know that output Q depends on inputs like capital K and labor L. When capital is fixed in the short run, only labor varies — and the three product curves describe exactly how output responds to adding more workers to a fixed production facility. Think of a restaurant kitchen with a fixed number of stoves and worktables. The first few cooks dramatically increase meals produced (specialization: one handles prep, another grills, another plates). But eventually the kitchen fills up — the 10th cook is bumping into the 9th, sharing equipment, waiting for burners — and each additional worker adds less than the one before.

**Total product (TP)** is simply the total meals produced at each staffing level. **Average product (AP)** is meals per cook: if 8 cooks produce 240 meals, AP = 30 meals/cook. **Marginal product (MP)** is the addition to output from the last cook hired: if the 9th cook raises daily meals from 240 to 264, their MP = 24. These three quantities are mathematically linked. When the marginal worker produces more than the average worker, they pull the average up — MP > AP implies AP is rising. When the marginal worker produces less than average, they drag the average down — MP < AP implies AP is falling. Therefore, MP must equal AP exactly at AP's maximum, which is why the MP curve intersects the AP curve at the peak of the AP curve. This relationship is a mathematical identity, not a coincidence — it holds for any average-marginal pair (exam grades, batting averages, etc.).

**Diminishing marginal returns** sets in when MP begins to decline — a critical point, because output is still rising, just at a decreasing rate. This is not the same as output falling, which would require MP to become negative. The confusion matters: a firm experiencing diminishing returns is still benefiting from each additional worker; it just benefits less and less. Output only falls if MP goes negative, which typically happens when the workforce is so large that additional workers actively impede production (too many cooks spoiling the broth, literally).

The hiring decision connects these curves to firm behavior. A profit-maximizing firm hires workers until the value of the last worker's output equals the wage — that is, until **marginal revenue product** (MP × output price) equals the wage. When MP > wage/price, hiring more adds more to revenue than cost. When MP < wage/price, the last worker costs more than they generate. The firm stops where these are equal, which is typically well above MP = 0 (unless the wage is zero, which it never is). This is why the common intuition — "hire until marginal product is zero" — is wrong: a firm stops long before MP hits zero, as soon as the diminishing returns have driven the value of MP below the wage.
