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

## Explainer

From the production function, you know that output Q depends on inputs like capital K and labor L. When capital is fixed in the short run, only labor varies — and the three product curves describe exactly how output responds to adding more workers to a fixed production facility. Think of a restaurant kitchen with a fixed number of stoves and worktables. The first few cooks dramatically increase meals produced (specialization: one handles prep, another grills, another plates). But eventually the kitchen fills up — the 10th cook is bumping into the 9th, sharing equipment, waiting for burners — and each additional worker adds less than the one before.

**Total product (TP)** is simply the total meals produced at each staffing level. **Average product (AP)** is meals per cook: if 8 cooks produce 240 meals, AP = 30 meals/cook. **Marginal product (MP)** is the addition to output from the last cook hired: if the 9th cook raises daily meals from 240 to 264, their MP = 24. These three quantities are mathematically linked. When the marginal worker produces more than the average worker, they pull the average up — MP > AP implies AP is rising. When the marginal worker produces less than average, they drag the average down — MP < AP implies AP is falling. Therefore, MP must equal AP exactly at AP's maximum, which is why the MP curve intersects the AP curve at the peak of the AP curve. This relationship is a mathematical identity, not a coincidence — it holds for any average-marginal pair (exam grades, batting averages, etc.).

**Diminishing marginal returns** sets in when MP begins to decline — a critical point, because output is still rising, just at a decreasing rate. This is not the same as output falling, which would require MP to become negative. The confusion matters: a firm experiencing diminishing returns is still benefiting from each additional worker; it just benefits less and less. Output only falls if MP goes negative, which typically happens when the workforce is so large that additional workers actively impede production (too many cooks spoiling the broth, literally).

The hiring decision connects these curves to firm behavior. A profit-maximizing firm hires workers until the value of the last worker's output equals the wage — that is, until **marginal revenue product** (MP × output price) equals the wage. When MP > wage/price, hiring more adds more to revenue than cost. When MP < wage/price, the last worker costs more than they generate. The firm stops where these are equal, which is typically well above MP = 0 (unless the wage is zero, which it never is). This is why the common intuition — "hire until marginal product is zero" — is wrong: a firm stops long before MP hits zero, as soon as the diminishing returns have driven the value of MP below the wage.
