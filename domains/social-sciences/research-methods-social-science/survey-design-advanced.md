---
id: survey-design-advanced
title: Advanced Survey Design
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: measurement-validity-social-science
  type: hard
- id: sampling-strategies-social-research
  type: hard
- id: sampling-distributions-theory
  type: soft
builds-toward:
- linear-regression-social-science
- structural-equation-modeling-latent
tags:
- survey
- questionnaire
- response-bias
- modes
stage: expert
status: draft
---

# Advanced Survey Design

## Core Idea
Addresses design of effective surveys for social research, covering question construction, response option design, scale development, survey modes (paper, online, phone), non-response bias, and data collection best practices. Emphasizes reducing response and coverage error.

## How It's Best Learned
Develop and pilot a questionnaire, test question wording variants, conduct cognitive interviews with respondents, analyze response patterns and missing data.

## Common Misconceptions
- Any set of questions is a survey
- Online surveys are faster so they're better
- Low response rates automatically bias results

## Questions

```yaml
- question: "Survey A on voting intentions achieves an 85% response rate but recruits participants primarily through civic associations, overrepresenting politically engaged citizens. Survey B on the same topic achieves a 30% response rate, but analysis shows that non-respondents are similar to respondents across income, age, and prior voting behavior. Which survey is likely more biased?"
  type: multiple-choice
  options:
    - "Survey B, because a 30% response rate is too low to support valid inference regardless of who responds"
    - "Survey A, because an 85% response rate is suspiciously high and likely reflects poor sampling"
    - "Survey A, because its non-response is systematic — the missing 15% are not randomly distributed on the variable of interest"
    - "Both equally — response rate and non-response patterns are independent sources of error that always matter equally"
  answer: 2
  explanation: "Non-response bias depends on whether those who don't respond differ from those who do on the variable of interest — not on response rate alone. Survey A's high response rate does not protect it from bias if the recruitment mechanism systematically excludes low-engagement voters. Survey B's 30% rate could be unbiased if the non-respondents are genuinely random with respect to voting intention. The key diagnostic question is always: do non-respondents differ systematically from respondents on the outcome variable?"

- question: "A researcher surveys 1,000 adults about their use of social media and gets a 60% response rate. She later finds that heavy social media users were significantly more likely to complete the survey. What is the most accurate description of the situation?"
  type: multiple-choice
  options:
    - "The results are reliable because 600 respondents is a large sample"
    - "There is likely non-response bias — heavy users are overrepresented because they differ systematically from non-respondents on the key variable"
    - "The 40% non-response rate guarantees bias; the only solution is to re-survey all non-respondents"
    - "Since response rate is above 50%, statistical inference is valid and no adjustment is needed"
  answer: 1
  explanation: "Non-response bias is present when non-respondents differ from respondents on the variable being measured. Here, social media use itself predicts survey completion — exactly the situation where bias is most severe. Sample size is irrelevant: a large biased sample is still biased. The 40% non-response rate is not automatically damning (it depends on who the 40% are), but finding that they differ systematically on the key variable confirms bias. No response-rate threshold automatically guarantees validity."

- question: "A double-barreled question ('Do you support raising the minimum wage and strengthening unions?') can produce misleading data even if every respondent answers completely honestly."
  type: true-false
  answer: true
  explanation: "A double-barreled question asks about two distinct issues in a single item. Respondents who support one but not the other must choose a single answer that misrepresents their view. The resulting data conflates agreement with two separate policies, making it impossible to know which sub-question the respondent was answering. Even perfectly honest responses produce uninterpretable data. This is a question construction error, not a respondent error — it is caught through cognitive interviewing before fieldwork begins."

- question: "A survey with a low response rate is always more biased than one with a high response rate, because fewer respondents means less representation of the population."
  type: true-false
  answer: false
  explanation: "Response rate alone does not determine bias. Bias depends on whether non-respondents differ systematically from respondents on the variables of interest. A survey with a 25% response rate may produce unbiased estimates if non-response is random. A survey with an 80% response rate may be severely biased if the 20% who did not respond share a systematic characteristic relevant to the outcome. Researchers assess non-response bias by comparing respondents to known population benchmarks and by characterizing non-respondents through follow-up — not simply by checking the response rate."

- question: "How can a researcher assess whether non-response has biased a survey, even when the non-respondents themselves cannot be surveyed?"
  type: short-answer
  answer: "Compare the demographic and behavioral profile of respondents to known population benchmarks from census or administrative data. If respondents match the population on observable characteristics (age, income, education, geography), bias on unobservables is less likely. Additionally, follow up with a random subsample of non-respondents using a shorter instrument or incentive, and compare their responses to those of original respondents on key variables. Large differences signal bias; similarity suggests the non-response may be ignorable."
  explanation: "This strategy — benchmark comparison plus non-respondent follow-up — is the standard approach precisely because you cannot survey people who decline to participate. Neither method is perfect: population benchmarks only cover observable variables, and non-respondent follow-up reaches only the more cooperative non-respondents. But together they give a much more informative picture than the response rate alone. The core principle is: assess bias by examining what you know about the non-respondents, not just how many of them there are."
```

## Explainer

Your prerequisite work on measurement validity taught you that a measure is only as good as how well it captures the underlying construct — and surveys are especially vulnerable to this problem because every methodological choice, from the wording of a single question to the medium of delivery, can distort what respondents report. Advanced survey design is the discipline of systematically anticipating and minimizing these distortions before data collection begins.

**Question construction** is where most measurement error originates. Leading questions prime respondents toward particular answers ("Do you agree that the government wastes too much money?"). Double-barreled questions ask about two things at once ("Do you support raising the minimum wage and strengthening unions?"), making it impossible to know which sub-question the respondent is answering. **Response option design** compounds these problems: a five-point Likert scale with no neutral midpoint forces fence-sitters to choose a side; a scale that runs from "strongly agree" to "somewhat disagree" without a "strongly disagree" anchor compresses one end of the distribution. Getting question and option design right requires **cognitive interviewing** — talking through each question with representative respondents to surface where they interpret phrasing differently than intended. This connects directly to your validity training: cognitive interviews are a form of think-aloud validity checking at the item level.

**Survey mode** — the channel through which the survey is administered — interacts with everything else. Online panels are cheap and fast but systematically underrepresent elderly, lower-income, and less digitally connected populations, creating coverage error that no statistical adjustment fully fixes. Phone surveys once reached nearly everyone but now face declining response and cell-phone sampling complications. In-person interviewing gives enumerators the ability to clarify questions and reduces item non-response, but is expensive and introduces **social desirability bias** — respondents adjust answers to appear favorable to an interviewer. Sensitive topics (income, substance use, political extremism) often require modes that give respondents privacy, like self-administered questionnaires or audio-assisted self-interview formats.

**Non-response bias** is subtler than it appears. Your sampling prerequisite covered how to draw a representative sample from a population; advanced survey design deals with what happens when the people you selected refuse to participate or can't be reached. Low response rate alone does not guarantee bias — what matters is whether non-respondents differ systematically from respondents on the variables of interest. A 30% response rate survey about TV preferences may be unbiased if non-response is random; a 70% response rate survey about vaccination attitudes may be severely biased if vaccine skeptics disproportionately decline. Analysts assess non-response bias by comparing respondents to known population benchmarks (from census data) and by following up with a random subsample of non-respondents to characterize how they differ. Scale development — building multi-item instruments for latent constructs like "trust" or "anxiety" — adds another layer, requiring item analysis, factor analysis, and test-retest reliability checks to ensure the scale consistently and validly measures what it claims to.
