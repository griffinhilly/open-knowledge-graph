---
id: electoral-systems
title: Electoral Systems
domain: social-sciences
course: political-science
prerequisites:
- id: democracy-types-and-theory
  type: hard
- id: constitutionalism
  type: soft
- id: ratios
  type: soft
- id: percent-concept
  type: soft
- id: proportions
  type: soft
builds-toward:
- political-parties-and-party-systems
- political-culture-and-participation
tags:
- elections
- proportional representation
- plurality
- FPTP
- electoral design
stage: advanced
status: validated
---

# Electoral Systems

## Core Idea
Electoral systems are the rules that translate votes into seats or offices, and they profoundly shape party systems, representation, and government stability. Plurality systems (first-past-the-post) award seats to whoever gets the most votes, tending to produce two-party systems but disproportionate outcomes. Proportional representation (PR) allocates seats in proportion to vote shares, producing multiparty systems and more inclusive parliaments. Mixed systems combine both elements. Duverger's Law is the classic proposition that plurality systems produce two-party systems while PR produces multiparty systems. Electoral rules also determine district magnitude, ballot structure, electoral thresholds, and the timing of elections.

## How It's Best Learned
Compare the UK (FPTP) and Germany (mixed-member proportional) to see how electoral rules shape party systems. Use simulated election data to show how the same vote totals produce radically different seat distributions under different systems.

## Common Misconceptions
- No electoral system is objectively 'best' — each involves tradeoffs between proportionality, accountability, governability, and minority representation.
- FPTP can produce strong majority governments even when the winning party received a minority of votes, which raises democratic legitimacy questions.

## Questions

```yaml
- question: "In an election under first-past-the-post, a third party consistently wins 20% of the national vote but only 3% of parliamentary seats. A supporter concludes the system is broken and switches to voting for their second-choice major party. According to Duverger's Law, what does this individual's behavior illustrate?"
  type: multiple-choice
  options:
    - "Rational ignorance — the voter doesn't understand how many seats the third party actually holds"
    - "Strategic voting — the voter abandons their sincere preference to avoid wasting their vote on a party that cannot win the local plurality"
    - "Expressive voting — the voter is making a symbolic statement rather than trying to influence the outcome"
    - "Proportional defection — a normal feature of all electoral systems that corrects for overrepresentation"
  answer: 1
  explanation: "Duverger's Law explains why FPTP tends to produce two-party systems: voters who prefer a third party that cannot win the local plurality face a strategic incentive to defect. Their vote for the third party doesn't help elect anyone — it's 'wasted.' Over many elections, this strategic pressure squeezes third parties out and consolidates support around two major parties. The voter in this scenario is acting exactly as Duverger's Law predicts: rational strategic behavior aggregates into a two-party equilibrium."

- question: "Germany's mixed-member proportional system includes a 5% electoral threshold. What is the primary purpose of this threshold?"
  type: multiple-choice
  options:
    - "To ensure that every party wins at least 5% of seats, preventing tiny parties from being shut out entirely"
    - "To prevent extreme fragmentation by excluding very small parties from seat allocation, while still allowing proportionality among parties above the threshold"
    - "To limit the number of parties to exactly 20, since 100% ÷ 5% = 20"
    - "To require candidates to win at least 5% of their local district vote before they qualify for list seats"
  answer: 1
  explanation: "Electoral thresholds are a deliberate correction to the fragmentation risk in PR systems. Without a threshold, even a party with 0.5% of the vote could win seats in a large parliament, leading to dozens of parties with minimal coherence. Germany's 5% threshold excludes parties below that level from proportional seat distribution, concentrating representation among parties with meaningful support. The tradeoff is reduced proportionality for small parties — but the intent is governability and stability rather than maximal proportionality."

- question: "Under first-past-the-post, a party that wins 40% of the national vote can win a majority of parliamentary seats."
  type: true-false
  answer: true
  explanation: "This is one of FPTP's defining features — and a major source of controversy about its democratic legitimacy. Because each seat is won by the local plurality, a party whose support is efficiently distributed across many districts can win far more seats than its national vote share suggests. In the UK, parties have repeatedly won large parliamentary majorities with 35–43% of the national vote. The flip side is that a party with 20% of votes spread evenly across all districts may win very few seats. This disproportionality is why FPTP is criticized as unrepresentative even as it is praised for producing clear governing mandates."

- question: "Proportional representation systems tend to produce stronger, more accountable single-party governments than first-past-the-post systems."
  type: true-false
  answer: false
  explanation: "This has it backwards. PR systems typically produce multiparty coalition governments, not single-party governments, precisely because no party wins a majority of seats when votes are translated proportionally. Coalition governments involve multiple parties sharing executive power, which can make accountability harder — voters struggle to assign credit or blame among coalition partners. FPTP tends to produce single-party majority governments, which are more directly accountable (voters know exactly who to reward or punish). The tradeoff is that this accountability in FPTP comes with severe disproportionality in representation."

- question: "Why does first-past-the-post tend to produce two-party systems while proportional representation tends to produce multiparty systems? Explain the mechanism, not just the outcome."
  type: short-answer
  answer: "In FPTP, each district has one winner — whoever gets the most votes. A voter who prefers a third party that cannot win the local plurality accomplishes nothing by voting for it; their vote is 'wasted.' Rational voters therefore defect to whichever major party they dislike less. Over many election cycles, this strategic pressure drains support from third parties and concentrates it in two. In PR, even a party with 10% of the vote wins roughly 10% of seats, so voters face no strategic incentive to abandon sincere preferences. Small parties can survive and grow, producing stable multiparty systems."
  explanation: "The mechanism is strategic voting under FPTP (the 'wasted vote' logic) versus sincere voting under PR. Duverger's Law identifies this as a sociological regularity, not a logical necessity — there can be exceptions. But the incentive structure is clear: FPTP punishes voters for supporting parties that cannot win locally, while PR rewards any party with broad enough support to clear a threshold. District magnitude amplifies this: larger multi-member districts behave more like PR even within formally plurality systems."
```

## Explainer

From your study of democracy types and constitutional design, you know that democratic systems vary in how power is organized and constrained. Electoral systems are one of the most consequential constitutional choices a democracy makes, because they determine not just who wins elections but what kinds of parties exist, how voters behave, and what coalitions govern. The same set of votes, run through different electoral rules, produces radically different political outcomes.

**First-past-the-post (FPTP)**, also called plurality voting, is the simplest rule: the candidate with the most votes in a single-member district wins, regardless of whether they have a majority. Its main structural consequence is **Duverger's Law**: FPTP tends to produce two-party systems. The mechanism is strategic voting — voters who prefer a third party learn that voting for it is "wasted" when the third party cannot win the local plurality. Over many elections, third parties are squeezed out as voters defect to the viable alternatives. The UK, Canada, and the United States show this pattern clearly. The tradeoff is stark: FPTP typically produces single-party majority governments with a clear electoral mandate (strong accountability — you know who to blame) but severe disproportionality (a party can win 40% of votes and 60% of seats, while another wins 25% of votes and 10% of seats).

**Proportional representation (PR)** allocates seats in proportion to vote totals, typically using multi-member districts or party list systems. If a party wins 30% of the vote, it gets roughly 30% of the seats. This produces multiparty systems — small parties can win seats, so voters face no strategic incentive to abandon their sincere preference. The tradeoff runs the other way: PR parliaments typically require coalition governments (because no party wins a majority), which can be slow to form, subject to internal negotiations, and harder to hold accountable when multiple parties share executive power. Netherlands, Sweden, and Denmark use PR systems.

**Mixed-member proportional (MMP)** systems, like Germany's, attempt to capture benefits of both: voters cast two votes, one for a local candidate (FPTP-style) and one for a party list. The party-list vote determines the overall seat distribution, with local wins "topped up" by list seats to produce proportionality overall. This maintains local representation while correcting FPTP's disproportionality.

The deeper insight is that electoral rules shape *political culture itself* over time, not just seat distributions. FPTP systems tend to produce adversarial two-party politics (winners govern, losers oppose) because the game is winner-take-all. PR systems tend to produce consensual multiparty politics because governing requires coalition-building and compromise from the start. **District magnitude** — how many seats are awarded per district — is the crucial variable: small districts tend toward plurality-like effects even in nominally PR systems, while large districts produce higher proportionality. **Electoral thresholds** (Germany's 5% threshold, for instance) prevent extreme fragmentation in PR systems by excluding parties below a minimum vote share.

No system solves all problems simultaneously. Proportionality, accountability, governability, minority representation, and voter-party linkage trade off against each other. Understanding electoral systems means understanding these tradeoffs — and recognizing that every democracy's electoral rules embody a set of political choices about which values to prioritize.
