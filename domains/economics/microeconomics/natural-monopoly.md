---
id: natural-monopoly
title: Natural Monopoly and Regulation
domain: economics
course: microeconomics
prerequisites:
- id: monopoly-microeconomics
  type: hard
- id: long-run-costs-economies-of-scale
  type: hard
builds-toward:
- externalities-and-market-failure
- public-goods-and-common-resources
tags:
- natural monopoly
- regulation
- marginal cost pricing
- average cost pricing
stage: formal-systems
status: validated
---

# Natural Monopoly and Regulation

## Core Idea
A natural monopoly arises when a single firm can serve an entire market at lower cost than multiple firms, due to large economies of scale relative to market demand (declining LRAC throughout the relevant range). Unregulated, a natural monopoly produces at MR = MC but prices above MC, creating deadweight loss. Marginal-cost pricing (P = MC) achieves efficiency but causes losses when LRAC is declining; average-cost pricing (P = LRAC) eliminates losses while reducing (but not eliminating) deadweight loss. Regulators face a tradeoff between efficiency and firm viability.

## How It's Best Learned
Draw the natural monopoly diagram carefully, identifying the unregulated monopoly outcome, the efficient (MC pricing) outcome with its losses, and the regulated (AC pricing) compromise. Connect to real-world utility regulation.

## Common Misconceptions
- Not every monopoly is a natural monopoly; natural monopoly is a cost-structure concept, not simply the presence of one firm.
- Marginal-cost regulation seems optimal but is impractical when it forces firms to operate at a loss indefinitely.

## Questions

```yaml
- question: "A regulator sets price equal to marginal cost for a natural monopoly with declining long-run average cost. What outcome should the regulator expect?"
  type: multiple-choice
  options:
    - "The firm earns zero economic profit and serves consumers efficiently"
    - "The firm earns positive economic profit, since low prices attract more customers"
    - "The firm suffers losses on every unit sold and will exit unless subsidized"
    - "Deadweight loss is maximized because the price is set too low"
  answer: 2
  explanation: "When LRAC is still declining at the efficient output, marginal cost lies below average cost (MC < LRAC is what causes LRAC to decline). Setting P = MC means P < LRAC, so the firm earns negative economic profit — it loses money on every unit. Without a subsidy, the firm exits. This is the core regulatory dilemma: marginal-cost pricing is socially efficient but financially unsustainable. Option A describes the desired outcome but ignores the financial impossibility. Real utility regulation usually settles for average-cost pricing instead."

- question: "A city has one water utility serving all households. A new firm tries to enter and compete. Which explanation best captures why competition is unlikely to succeed?"
  type: multiple-choice
  options:
    - "The existing firm uses predatory pricing to drive out competitors"
    - "Government licensing prevents new firms from entering"
    - "High infrastructure fixed costs mean two firms would each face higher average costs than one firm serving the whole market"
    - "Consumers prefer dealing with a single provider out of habit"
  answer: 2
  explanation: "A natural monopoly is a cost-structure phenomenon, not the result of predatory behavior or legal barriers. When fixed costs (pipes, treatment plants) are very high and marginal costs are low, a single firm spreading those fixed costs over all customers achieves much lower average cost than two firms each building their own infrastructure. Any entrant would have higher costs and would be undercut. This is what 'natural' means — the monopoly emerges from the economics of production, not from anticompetitive conduct. Option A describes a behavioral monopoly, which is a different concept."

- question: "Average-cost pricing for a natural monopoly eliminates all deadweight loss."
  type: true-false
  answer: false
  explanation: "Average-cost pricing (P = LRAC) sets price above marginal cost — the firm covers all costs including a normal return, but P > MC means consumers who would have bought at MC don't buy at the higher price. This creates a deadweight loss triangle, smaller than under unregulated monopoly pricing but still present. Only marginal-cost pricing (P = MC) eliminates deadweight loss, but it causes losses for the firm when LRAC is declining. Average-cost pricing is the practical compromise that accepts some deadweight loss in exchange for financial viability without subsidy."

- question: "A natural monopoly can emerge even when the dominant firm has never engaged in predatory or anticompetitive behavior."
  type: true-false
  answer: true
  explanation: "Natural monopoly is defined by cost structure: a single firm can serve the entire market at lower total cost than any combination of multiple firms. This occurs because of large economies of scale relative to market size — declining LRAC throughout the relevant output range. No predatory conduct is required. The market naturally converges to one firm because any competitor would face higher average costs and be undercut on price by the incumbent simply operating at greater scale. This is why 'natural' monopoly is contrasted with monopoly achieved through deliberate exclusion."

- question: "Why can't a regulator simply require a natural monopoly to price at marginal cost, and what alternative do most real-world regulators use instead?"
  type: short-answer
  answer: "When LRAC is declining at the relevant output, MC < LRAC. Setting P = MC means the firm earns less per unit than its average cost — it loses money and will shut down without a subsidy. Most regulators instead use average-cost pricing (P = LRAC), which allows the firm to earn zero economic profit (covering all costs including a fair return) while remaining financially viable. This accepts some deadweight loss (P > MC) in exchange for sustainability without subsidy."
  explanation: "The tradeoff is efficiency vs. viability. MC pricing is Pareto-efficient but requires the government to subsidize the firm indefinitely to cover its losses. Average-cost pricing ('fair rate of return' regulation) is the standard approach for electricity, water, and gas utilities: set rates to cover costs including an allowed return on capital, let the firm break even, accept the residual inefficiency. This is a genuine second-best solution — the first-best (MC pricing + subsidy) has its own political and fiscal costs, and the choice involves value judgments about who bears the burden."
```

## Explainer

From your study of monopoly, you know that a monopolist sets MR = MC and charges a price above marginal cost, creating deadweight loss. From long-run costs and economies of scale, you know that some industries have declining long-run average cost (LRAC) throughout the relevant range of output — meaning the more they produce, the cheaper each unit becomes. A **natural monopoly** combines these two ideas: it is an industry where the efficient cost structure itself makes competition unstable.

Here is the intuition: suppose a city needs a water distribution network. Building the pipes, treatment plants, and pumping stations requires enormous fixed costs. But once built, the marginal cost of serving one more household is very low. If two firms tried to compete, each would build its own network — duplicating the fixed costs — and each would serve fewer customers at a higher average cost than a single firm serving everyone. Any firm that achieves scale will inevitably undercut the other. The market *naturally* converges to one firm, not because of predatory behavior, but because the cost structure rewards concentration. This is the definition: a single firm can serve the entire market at lower total cost than any combination of multiple firms.

The regulatory dilemma follows directly. Left unregulated, the natural monopolist behaves like any monopolist: it finds MR = MC and charges P > MC. This creates the familiar deadweight loss triangle. The socially efficient solution — **marginal-cost pricing** (P = MC) — eliminates deadweight loss but creates a new problem. When LRAC is still declining at the quantity produced, MC lies below LRAC, so P = MC means P < LRAC. The firm loses money on every unit and will shut down without a subsidy. Efficiency and financial viability cannot both be achieved at once.

**Average-cost pricing** (P = LRAC) is the practical compromise. Setting price equal to average cost means the firm earns zero economic profit — it covers all costs including a fair return on capital, but earns nothing extra. Deadweight loss is not eliminated (price still exceeds MC), but it is reduced compared to the unregulated outcome. Real utility regulators use this logic: electricity, natural gas, water, and telecommunications are often regulated to a "fair rate of return" on invested capital, which approximates average-cost pricing. The remaining deadweight loss is the cost of keeping the firm financially viable without subsidy.

The policy tradeoff is therefore: full efficiency requires a subsidy (MC pricing with a transfer from taxpayers); no subsidy requires accepting some inefficiency (AC pricing); and no regulation produces the most inefficiency of all (monopoly pricing). Understanding a natural monopoly means recognizing that the problem is not a bad actor but a cost structure — and that no regulatory solution eliminates the tradeoff entirely. The choice between these options involves value judgments about who should bear costs, not just technical optimization.
