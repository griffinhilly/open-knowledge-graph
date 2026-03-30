---
id: online-algorithms-competitive-analysis
title: Online Algorithms and Competitive Analysis
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: greedy-algorithms
  type: hard
- id: amortized-analysis
  type: hard
- id: randomized-algorithms
  type: soft
tags:
- online-algorithms
- competitive-analysis
- competitive-ratio
- adversarial-model
stage: expert
status: validated
---

# Online Algorithms and Competitive Analysis

## Core Idea
Online algorithms must make irrevocable decisions as input arrives, without knowledge of future requests. Competitive analysis measures performance by comparing the online algorithm's cost to the optimal offline algorithm (which sees the entire input in advance). The competitive ratio is the worst-case ratio of online cost to offline optimal cost. The ski rental problem illustrates the core tension: buy skis (high upfront cost, free future use) or rent (low per-use cost, no commitment). The deterministic optimal strategy achieves competitive ratio 2; randomization improves this to e/(e-1) ≈ 1.58. For paging (cache management), LRU achieves optimal deterministic competitive ratio k (cache size), while randomized marking algorithms achieve O(log k). These results reveal a fundamental gap between deterministic and randomized online computation.

## Questions

```yaml
- question: "In the ski rental problem, skis cost $B to buy and $1/day to rent. What is the optimal deterministic strategy and its competitive ratio?"
  type: multiple-choice
  options:
    - "Rent for B-1 days, then buy on day B; competitive ratio 2 - 1/B"
    - "Buy immediately on day 1; competitive ratio B"
    - "Rent forever; competitive ratio is unbounded"
    - "Alternate between renting and buying; competitive ratio sqrt(B)"
  answer: 0
  explanation: "If the ski season lasts fewer than B days, renting is optimal (cost < B) and the algorithm rents the whole time (cost < B), so the ratio is at most 1. If the season lasts B or more days, the algorithm rents for B-1 days (cost B-1) then buys (cost B), total 2B-1, while the optimal strategy buys on day 1 (cost B). The ratio is (2B-1)/B = 2 - 1/B. No deterministic strategy can do better: any strategy that buys on day t can be forced to pay t-1 + B by an adversary who ends the season on day t, while the optimum pays min(t, B)."

- question: "For the paging problem with cache size k, no deterministic online algorithm can achieve a competitive ratio better than k."
  type: true-false
  answer: true
  explanation: "An adversary can always request the page that is NOT in the cache, forcing every request to be a fault for the online algorithm. Among any k+1 pages, the adversary requests whichever the algorithm evicts. Over n requests to k+1 pages, the online algorithm faults every time (n faults), while an optimal offline algorithm (Bélády's MIN, which evicts the page used farthest in the future) faults at most n/k times. The competitive ratio is n/(n/k) = k. LRU and FIFO achieve this ratio, making them optimal among deterministic policies. This lower bound uses an adversarial argument specific to deterministic algorithms — randomization breaks it."

- question: "Randomized online algorithms can achieve strictly better competitive ratios than deterministic ones against an oblivious adversary. Explain why, using the paging problem as an example."
  type: short-answer
  answer: "Against an oblivious adversary (who must fix the entire request sequence before the algorithm's random choices), the adversary cannot adaptively target the algorithm's eviction decisions. In paging, the randomized marking algorithm achieves competitive ratio O(log k), exponentially better than the deterministic lower bound of k. The algorithm works in phases: it marks pages as they are requested, and when a fault occurs on an unmarked page, it evicts a uniformly random UNMARKED page. The adversary, who commits to the request sequence in advance, cannot know which unmarked page will be evicted, so cannot consistently force faults. This randomization breaks the adversarial construction that proves the deterministic lower bound."
  explanation: "The distinction between adversary types matters: against an adaptive adversary (who sees the algorithm's random bits), randomization provides no benefit and the deterministic lower bound applies. The O(log k) randomized bound versus the Theta(k) deterministic bound for paging is one of the most dramatic separations between deterministic and randomized online algorithms."

- question: "The competitive ratio of an online algorithm can be improved by allowing the algorithm to see a constant number of future requests (lookahead)."
  type: true-false
  answer: true
  explanation: "Even a small lookahead of L future requests can significantly improve competitive ratios. For paging, lookahead L = k (seeing the next k requests) allows the algorithm to simulate Bélády's MIN over a local window, improving the competitive ratio. For some problems like the online matching problem, O(1) lookahead already provides a strict improvement. However, the improvement is problem-specific — some problems have competitive ratio lower bounds that hold even with polynomial lookahead. The relationship between lookahead, advice complexity, and competitive ratio is an active research area."
```

## Explainer

Many real-world computational problems are inherently online: a cache manager decides which page to evict before knowing future accesses; a scheduler assigns jobs to machines as they arrive; a market maker sets prices before seeing orders. Online algorithm theory provides a framework for reasoning about irrevocable decisions under uncertainty, with competitive analysis as the primary performance measure.

The ski rental problem is the simplest interesting example. You need skis for an unknown number of days. Buying costs B; renting costs 1/day. The optimal deterministic strategy rents for B-1 days, then buys — this guarantees a competitive ratio of 2 - 1/B against any season length. The proof that no deterministic strategy does better uses an adversarial argument: whatever day t the algorithm plans to buy, the adversary ends the season on day t to maximize the ratio. Randomization helps: by buying on a randomly chosen day drawn from an appropriate distribution, the expected competitive ratio drops to e/(e-1) ≈ 1.58. This gap between 2 and 1.58 illustrates a recurring theme — randomization fundamentally helps in online settings.

The paging problem is the canonical online problem with deep results. With a cache of size k, the deterministic competitive ratio is exactly k: LRU, FIFO, and CLOCK all achieve it, and no deterministic algorithm does better. The lower bound proof constructs an adversarial sequence on k+1 pages that forces k times more faults than the offline optimal (Bélády's MIN algorithm). Randomization dramatically improves this: the randomized marking algorithm achieves competitive ratio H_k = O(log k), and this is tight against oblivious adversaries. The exponential gap (k vs log k) shows that hiding eviction decisions from the adversary is enormously valuable.

Competitive analysis has limitations. It measures worst-case performance against the omniscient offline optimum, which can be overly pessimistic — real inputs are rarely adversarial. This has motivated alternative frameworks: resource augmentation (give the online algorithm more resources than the offline optimum), smoothed competitive analysis (add random noise to adversarial inputs), and beyond-worst-case models using predictions or advice. These extensions bridge the gap between the clean theoretical framework of competitive analysis and the practical reality that online algorithms often perform much better than their competitive ratios suggest.
