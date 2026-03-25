---
id: big-data-social-science
title: Big Data Collection and Analysis in Social Science
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: computational-social-science-intro
  type: hard
- id: research-design-advanced
  type: soft
- id: matrices-intro
  type: soft
- id: statistics-descriptive
  type: soft
- id: discrete-math-overview
  type: soft
builds-toward:
- algorithmic-auditing
- data-ethics-governance
tags:
- big-data
- computational
- digital-traces
- scale
stage: formal-systems
status: validated
---

# Big Data Collection and Analysis in Social Science

## Core Idea
Big data in social science harnesses digital traces—social media, search logs, transaction records, mobile location data—to study behavior and social patterns at scale and in real time. Advantages include coverage of large populations and continuous observation; disadvantages include selection bias (who uses digital platforms?), privacy concerns, and validity issues (digital behavior ≠ all social behavior). Methodologically, big data demands new approaches to causality, privacy, and representation.

## Questions

```yaml
- question: "A researcher scrapes 50 million tweets to study public opinion on immigration policy. She finds 62% of tweets express negative views and concludes that most people oppose more permissive immigration policy. What is the most significant flaw in this reasoning?"
  type: multiple-choice
  options:
    - "The sample size is too small — she needs at least 100 million tweets for reliable conclusions"
    - "Twitter users are not representative of the general population, so the data suffers from selection bias unrelated to sample size"
    - "Sentiment analysis tools cannot accurately classify tweets, introducing measurement error"
    - "She should have used a different platform with more users, like Facebook, for better coverage"
  answer: 1
  explanation: "This is the selection bias problem endemic to big data. Twitter users are systematically younger, more urban, more politically engaged, and more extreme in expressed opinions than the general population. No amount of additional tweets fixes this — the bias comes from who generates Twitter data in the first place, not how much of it you collect. Switching to Facebook (option D) would have different but equally systematic biases. This is fundamentally different from survey sampling bias: you cannot correct for platform selection bias by collecting more data from the same platform."

- question: "A study using social media data finds that people who post frequently about social activities report higher loneliness on follow-up surveys. A researcher concludes that active social media use causes loneliness. What is the primary methodological concern?"
  type: multiple-choice
  options:
    - "The study should have used a control group of people with no social media accounts"
    - "Posting frequency is a behavioral metric that may not validly represent social engagement or loneliness as theoretical constructs"
    - "The sample size is insufficient for causal claims about such a complex phenomenon"
    - "Longitudinal designs cannot establish causation — only experimental designs can"
  answer: 1
  explanation: "This is the construct validity problem. Posting frequency is a digital behavior metric, not a direct measure of social engagement or loneliness. People post frequently for many reasons — performance, boredom, professional necessity — that have no connection to how socially connected they feel. The gap between what the data records (posting behavior) and what the researcher wants to measure (loneliness) is a construct validity problem that cannot be fixed by having more data. Big data provides scale but not automatic validity — connecting digital behavior metrics to underlying social constructs requires careful theoretical justification."

- question: "Collecting a larger dataset in big data research eliminates selection bias by including more observations from the target population."
  type: true-false
  answer: false
  explanation: "False. Selection bias in big data operates at the platform level, not the sample level. If Twitter users are systematically different from the general population, then collecting every single tweet ever posted still gives you a biased picture of that general population — because the bias comes from who uses Twitter, not from sampling within the Twitter population. More observations from a biased source gives you a more precise measure of the biased population, not a less biased measure of the target population. This is different from traditional random sampling, where increasing N does reduce sampling error."

- question: "Big data's scale can reveal patterns impossible to detect in smaller datasets, but it amplifies the consequences of poor research design rather than compensating for it."
  type: true-false
  answer: true
  explanation: "True. Scale is a double-edged property. With millions of observations, researchers can detect tiny effect sizes that would be statistically undetectable in smaller samples — including trivially small effects that are theoretically meaningless. Statistical significance becomes nearly guaranteed at large N even for noise. Meanwhile, systematic biases (selection bias, measurement invalidity) are not reduced by scale — they are replicated consistently across millions of observations. The principle that a large N does not substitute for a clear research question or valid measurement instrument is fundamental to responsible big data social science."

- question: "Explain why selection bias in big data research is different from selection bias in traditional survey research, and why increasing the dataset size cannot fix it."
  type: short-answer
  answer: "In traditional survey research, selection bias arises from who responds to an invitation — and you can potentially reduce it by improving response rates or weighting by known population characteristics. In big data, selection bias arises from who uses the platform at all — who generates the digital traces in the first place. Twitter users, credit card holders, and smartphone location data sources are systematically non-representative subpopulations defined by age, income, geography, and technology access. No amount of additional data from the same platform closes this gap, because the unrepresented people are simply absent from the data-generating process entirely."
  explanation: "This distinction matters because it means the traditional 'more data = less bias' intuition breaks down for big data. A 50-million-tweet dataset has exactly the same structural selection bias as a 1,000-tweet dataset on Twitter. The fix is not to collect more data from the same source but to understand the population that source represents, be explicit about that population in claims, or supplement with data from other sources that cover the underrepresented groups."
```

## Explainer

From computational social science, you already know that digital systems generate behavioral traces as a byproduct of their operation — every search query, every purchase, every location ping is a record of human action. Big data methods treat these exhaust streams as primary data sources rather than supplements to surveys or experiments. The scale is genuinely transformational: where a traditional survey might capture a few thousand responses, Twitter's API can yield millions of posts per day, and credit card transaction records span the full purchasing behavior of entire populations over years. This is not simply "more survey data" — it is a qualitatively different kind of observation.

The promise of this scale is that rare events become analyzable, time dynamics become visible, and natural experiments become easier to find. Researchers studying how social networks spread misinformation, for example, can trace the actual diffusion path of a specific claim across millions of accounts in real time — something impossible with any retrospective survey. The matrices you've encountered in prior work become essential here: large-scale co-occurrence matrices capture which users interact with which content, adjacency matrices represent social networks, and document-term matrices underlie text analysis. Operations like dimensionality reduction (PCA, SVD) and clustering let researchers find structure in datasets with millions of rows and thousands of columns.

The critical limitation to internalize is **selection bias** — and it operates differently than in traditional sampling. Survey sampling bias arises from who responds to your invitation; big data bias arises from who uses the platform in the first place. Twitter users are younger, more urban, more politically engaged, and more English-speaking than the general population. Transaction data covers only those with bank accounts. Search data covers only people with internet access and literacy. When you use these sources to make claims about "human behavior," you are actually making claims about a specific subpopulation, and that subpopulation may differ from your target population in ways that matter for your research question.

A second challenge is **construct validity** — the gap between what the data records and what you want to measure. Likes, shares, and comments are behavioral proxies for attitudes and engagement, but they are imperfect. People share content they find outrageous rather than content they agree with; people like posts for social reasons, not epistemic ones. Your descriptive statistics tools help you characterize what the data actually shows, but translating from digital behavior metrics to underlying social constructs requires careful theoretical work. Big data gives you enormous power to observe *what people do in digital contexts*, but sociological explanation requires connecting those behaviors to mechanisms, meanings, and structures that the data alone cannot reveal.

The methodological frontier involves combining big data's scale with traditional methods' validity. **Computational grounded approaches** use algorithmic pattern-finding (clustering, topic modeling, network analysis) to generate hypotheses that qualitative fieldwork or survey experiments then test. **Digital trace linkage** connects online behavior to administrative records (voter rolls, tax records, hospital data) to study offline consequences of online activity. Throughout, your research design training matters more, not less — a large N does not substitute for a clear research question, a credible identification strategy, or a valid measurement instrument. Big data amplifies both the reach of good designs and the misleadingness of bad ones.
