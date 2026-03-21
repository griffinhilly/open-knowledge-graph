---
id: supply-curve-individual-firm
title: 'Individual Supply Curves: Quantity Supplied vs. Price'
domain: economics
course: microeconomics
prerequisites:
- id: scarcity-choice-production-tradeoff
  type: hard
builds-toward:
- market-equilibrium
- profit-maximization-microeconomics
tags:
- supply
- firm
- production-decision
stage: abstract-reasoning
status: draft
---

# Individual Supply Curves: Quantity Supplied vs. Price

## Core Idea
A supply curve shows the relationship between the price of a good and the quantity a firm is willing to produce and sell, holding input prices and technology constant. Supply curves typically slope upward: higher prices make production more profitable, incentivizing greater output. Supply reflects firms' production and pricing decisions.

## Questions

```yaml
- question: "The price of flour doubles, raising the bakery's cost of producing each loaf. What happens to the bakery's supply curve?"
  type: multiple-choice
  options:
    - "The bakery moves up along its existing supply curve, supplying fewer loaves at the higher cost"
    - "The supply curve shifts leftward — higher input costs raise marginal cost at every output level, so the bakery is willing to supply less at every price"
    - "The supply curve shifts rightward — the bakery will produce more to compensate for the higher costs"
    - "Nothing changes — supply curves only shift when the price of the good itself changes"
  answer: 1
  explanation: "Input cost changes shift the supply curve because they change the marginal cost at every output level. Higher flour costs make each loaf more expensive to produce, so the bakery's MC curve rises — meaning the bakery is willing to supply less at every given price. This is a leftward shift of the supply curve (a decrease in supply). Note that option A describes movement along the curve, which only occurs when the price of the bakery's output changes, not its inputs."

- question: "When the market price of a good rises from $5 to $8, a student says 'supply has increased because producers are now making more.' Which best evaluates this claim?"
  type: multiple-choice
  options:
    - "Correct — producers making more at a higher price is the definition of supply increasing"
    - "Wrong — supply refers to the entire price-quantity relationship (the curve); a price change causes movement along the existing curve, increasing quantity supplied, not supply itself"
    - "Correct — supply and quantity supplied mean the same thing in practice"
    - "Partially correct — supply increases only if a new producer entered the market, not if existing producers expand"
  answer: 1
  explanation: "This is the supply-side version of the most common misconception in supply-demand analysis. 'Supply' refers to the entire supply curve — the relationship between all prices and the quantities producers are willing to offer. 'Quantity supplied' is the specific amount offered at one particular price. A price change moves producers along their existing supply curve (quantity supplied changes), but the curve itself — supply — doesn't shift. Supply only shifts when a non-price factor changes: input costs, technology, number of producers, expectations."

- question: "For a competitive firm, the supply curve is equivalent to the firm's marginal cost curve above the point where price covers variable costs."
  type: true-false
  answer: true
  explanation: "This is the key microeconomic identity linking supply curves to cost theory. A competitive firm (a price-taker) will produce additional units whenever the market price at least covers the marginal cost of that unit. So the firm chooses quantity where P = MC. Mapping out 'what quantity does the firm choose at each possible price?' traces the MC curve directly. The supply curve IS the MC curve (above the shutdown point), which explains why supply shifts whenever input costs change — because input cost changes shift the MC curve."

- question: "When the price of the good a firm sells rises, the firm's supply curve shifts rightward."
  type: true-false
  answer: false
  explanation: "A price change for the firm's own output causes movement along the existing supply curve — quantity supplied increases, but the supply curve itself does not shift. This is the same distinction as on the demand side: price changes cause movement along the curve; non-price factors (input costs, technology, number of producers, regulatory changes) shift the curve. The supply curve shifts rightward when, for example, input prices fall or technology improves — not when the output price rises."

- question: "Explain why the individual firm's supply curve slopes upward. What is the underlying economic mechanism?"
  type: short-answer
  answer: "The supply curve slopes upward because of rising marginal cost. As a firm expands output, it must use increasingly scarce or costly inputs — overtime labor, less efficient equipment, higher-priced raw materials. Each additional unit produced costs more than the previous one (marginal cost rises). A profit-maximizing firm will only produce an additional unit if the market price at least covers that unit's marginal cost. So at a low price, only the cheapest units are worth producing; at a higher price, it's profitable to expand output until MC rises to meet the new price. More output is supplied at higher prices, producing the upward slope."
  explanation: "The upward slope is not arbitrary — it follows directly from the law of increasing marginal cost (a consequence of diminishing returns to variable inputs). This is why the supply curve and the marginal cost curve are equivalent for a competitive firm: both trace the same relationship between output and the minimum price required to make that output profitable. Understanding this connection links the market-level supply curve to the firm-level cost analysis studied in microeconomics."
```

## Explainer

Your prerequisite — scarcity, choice, and production tradeoffs — established that producing more of anything means using resources that have alternative uses. The supply curve makes this intuition precise: it translates the production tradeoff into a specific price-quantity relationship that describes a firm's willingness to produce.

Think about a simple case: a bakery. To produce ten loaves a day, the baker uses an oven, flour, and labor at a certain cost. To produce twenty loaves, she needs more flour, more labor hours, and perhaps overtime. The cost of each additional loaf — the **marginal cost** of production — tends to rise as output expands, because the baker must use inputs (her own time, specialized labor) that become increasingly scarce. This rising marginal cost is the underlying engine of the upward-sloping supply curve. The firm will produce an additional unit whenever the price it receives for that unit at least covers the marginal cost of producing it. So at a low price, only the cheapest units are worth producing; at a higher price, it's profitable to expand output further. Mapping out "how much would we produce at each possible price?" traces the supply curve.

The **supply curve as a marginal cost curve** is a key insight. For a competitive firm (one that cannot affect the market price), the supply curve is literally the firm's marginal cost curve above the point where price covers variable costs. At a price of $2 per loaf, she produces where MC = $2. At $3, she expands until MC = $3. This equivalence — supply = MC — is what links the supply curve you see in market diagrams to the cost structure you study in firm-level analysis. It also explains *why* supply curves shift: if input prices fall (cheaper flour), marginal cost falls at every output level, and the firm is willing to supply more at every price — a rightward shift. If input prices rise, the curve shifts left.

The supply curve holds many things constant — technology, input prices, expectations, and the number of producers. These **ceteris paribus** conditions define what counts as a shift versus a movement. A price change for the firm's own output causes movement *along* the existing curve — quantity supplied changes, but supply itself does not. A change in input prices, technology, or regulatory environment shifts the entire curve. This distinction — which you've already seen on the demand side — is equally important for supply. The supply curve is not a fixed physical fact about the world; it is a summary of cost conditions at a point in time, and it changes whenever those conditions change.
