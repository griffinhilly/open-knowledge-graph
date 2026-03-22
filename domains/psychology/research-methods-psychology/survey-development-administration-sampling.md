---
id: survey-development-administration-sampling
title: Survey Design, Construction, and Administration
domain: psychology
course: research-methods-psychology
prerequisites:
- id: variable-definition-and-operational-measurement
  type: hard
builds-toward:
- measurement-reliability-estimation
- measurement-validity-evidence
tags:
- surveys
- questionnaires
- item-construction
- large-scale-data
stage: formal-systems
status: draft
---

# Survey Design, Construction, and Administration

## Core Idea
Surveys collect self-reported data on attitudes, behaviors, or experiences from large samples via questionnaires. Survey quality depends on clear wording, appropriate response scales, logical order, and piloting. Sampling strategy determines whether results generalize; response rate and representativeness affect validity. Surveys are cost-effective for descriptive and correlational research.

## How It's Best Learned
Critique published survey instruments for clarity, response bias, and relevance. Draft a brief survey and pilot it with colleagues, noting confusion or skip patterns. Compare online, paper, and in-person administration modes.

## Common Misconceptions
- Any list of questions is a valid survey; - Higher response rates always mean better data; - Self-report data are inherently unreliable; - Surveys are easy to design well.

## Questions

```yaml
- question: "Researcher A surveys 10,000 people from a carefully constructed probability sample and gets a 40% response rate. Researcher B posts a survey link on social media and gets 2,000 voluntary responses — a much higher effective rate. Whose results are more generalizable to the general population?"
  type: multiple-choice
  options:
    - "Researcher B, because more responses and a higher participation rate always mean better data"
    - "Researcher A, because probability sampling — not response rate — determines generalizability"
    - "Neither, because 40% is too low to draw any conclusions regardless of sampling method"
    - "They are equivalent because sample size and response rate compensate for each other"
  answer: 1
  explanation: "Generalizability depends on whether every member of the target population had a known, nonzero chance of being selected — that is, probability sampling. Researcher A used probability sampling, so statistical inference to the population is valid despite the moderate response rate. Researcher B's volunteers are self-selected; there is no way to calculate or correct for selection bias because the sampling frame is undefined. A high response rate from a biased pool is less valuable than a moderate rate from a proper probability sample."

- question: "A survey item reads: 'Don't you agree that the current administration has done a poor job managing the economy?' What is the primary flaw in this question?"
  type: multiple-choice
  options:
    - "Acquiescence bias — the yes/no format causes respondents to agree regardless of their true opinion"
    - "Double-barreled question — it asks about two separate issues in one item"
    - "Leading question — it embeds an evaluative frame that pulls responses toward a predetermined answer"
    - "Social desirability bias — respondents will answer based on what they think the researcher wants to hear"
  answer: 2
  explanation: "A leading question contains language that signals the 'correct' or expected answer, distorting responses away from genuine opinion. 'Don't you agree' presupposes agreement, and 'poor job' is an explicit negative evaluation embedded in the question stem. Acquiescence bias (A) is a respondent tendency to agree with any statement, which interacts with this flaw but is not the flaw itself. Social desirability bias (D) applies to sensitive self-disclosures, not to politically framed evaluations of others."

- question: "Acquiescence bias — the tendency to agree with survey statements regardless of content — can be partially controlled by including reverse-scored items in the instrument."
  type: true-false
  answer: true
  explanation: "Reverse-scored items state the opposite of what the positive items state. If a respondent agrees with everything, their agreement on the reverse item contradicts their agreement on the positive item, revealing the bias statistically. By comparing scores on positively and negatively worded versions of the same construct, researchers can detect and partially correct for acquiescence. This is why well-designed attitude scales often include both 'I feel confident in social situations' and 'I often feel uncomfortable in social situations.'"

- question: "A high survey response rate is the most important indicator of data quality because it ensures the respondents represent the target population."
  type: true-false
  answer: false
  explanation: "Response rate measures how many of the contacted people responded — it says nothing about whether the contacted people were the right people. A 95% response rate from a non-representative sampling frame produces systematically biased data. Representativeness is determined by the sampling method (probability vs. non-probability) and whether the sampling frame covers the target population. What matters is not how many responded, but whether the people who responded are representative of the people the researcher wanted to describe."

- question: "Why is 'a high response rate' insufficient to guarantee that a survey's results are valid or generalizable to the target population?"
  type: short-answer
  answer: "Response rate only tells you what fraction of the people you contacted actually responded. It says nothing about whether those contacted people were the right people — whether the sampling frame represents the target population. If you survey a convenience sample (e.g., social media followers, mall intercepts) and get a 90% response rate, you have a complete picture of a biased subset, not the population. Generalizability requires probability sampling, where every member of the target population has a known, nonzero selection probability. A moderate response rate from a probability sample produces valid inferences; a high response rate from a poorly defined frame does not."
  explanation: "The misconception equates participation with representation. These are independent dimensions: participation (response rate) measures effort and engagement; representation (sampling method) measures whether the right people were contacted in the first place. A truly random sample of 60% respondents is more valuable than a self-selected 90% because statistical theory can quantify uncertainty around the random sample — no such theory applies to unknown selection biases in the volunteer sample."
```

## Explainer

Your prerequisite on variable definition and operational measurement established that psychological constructs — anxiety, motivation, trust, satisfaction — must be operationalized: translated from abstract concepts into concrete, observable, measurable responses. Surveys are the most widely used operationalization vehicle in social science. Building a good survey means solving the operationalization problem at the item level, for every question on the instrument, while simultaneously managing the conditions under which responses are collected.

Every survey item is an attempt to extract a reliable signal about some internal state. The challenge is that the path from internal state to recorded response passes through several steps: the participant must interpret the question, retrieve relevant information from memory, form a judgment, and map that judgment onto the provided response options. Each step introduces potential distortion. **Response biases** — systematic tendencies to respond in ways unrelated to the true construct — are the primary threat. **Acquiescence bias** is the tendency to agree with statements regardless of content; it inflates positively worded items and can be partially controlled by including reverse-scored items. **Social desirability bias** is the tendency to present oneself favorably rather than accurately — particularly strong for sensitive topics like drug use, sexual behavior, income, and prejudiced attitudes. Both biases produce systematic error that mimics real variation in the construct, making them harder to detect than random error.

Question wording is the most controllable source of bias. **Double-barreled questions** ("How satisfied are you with the price and quality?") force a single response to two distinct questions and produce uninterpretable data — a respondent who loves the quality but hates the price cannot answer honestly. **Leading questions** ("Don't you agree that the policy was unfair?") embed an evaluative frame that pulls responses toward a predetermined answer. **Loaded terms** and abstract language trigger idiosyncratic interpretations: if one participant reads "frequently" as "more than once a week" and another reads it as "more than once a day," their responses are not measuring the same thing. Best-practice item writing uses specific, neutral, concrete language that a thoughtful stranger with no context would read in only one way.

**Response scales** shape the distribution and meaning of responses as much as question wording does. The number of scale points, the presence or absence of a neutral midpoint, and the verbal labels on endpoints all matter. A 5-point scale with a labeled neutral midpoint gives genuinely indifferent respondents a valid option; a forced-choice 4-point scale requires a lean in one direction — appropriate when you believe "neutral" is actually avoidance rather than genuine ambivalence. **Order effects** operate at both the item and survey levels: early items prime the cognitive context for later ones, and demographic questions at the beginning can activate identity-based response patterns that color substantive answers. Standard practice places sensitive items after rapport-building items and demographics at the end.

**Sampling** links instrument quality to research validity. A perfectly constructed survey administered to a non-representative sample produces internally valid but ungeneralizable findings. **Probability sampling** — where every unit in the target population has a known, nonzero chance of selection — is the basis for statistical generalizability. Simple random sampling gives equal probability to every unit; **stratified sampling** ensures adequate representation of key subgroups by sampling within strata separately; **cluster sampling** draws entire naturally occurring groups (schools, neighborhoods) when individual-level sampling is impractical. Non-probability samples (convenience, snowball) are common in practice but require explicit acknowledgment of generalizability limits. Response rate interacts with representativeness in a non-obvious way: a high response rate from a poorly defined sampling frame is less valuable than a moderate response rate from a probability sample of the actual target population. What matters is not how many people responded, but whether the people who responded are representative of the people you wanted to describe.
