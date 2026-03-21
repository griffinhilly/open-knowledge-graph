---
id: survey-research-methods
title: Survey and Questionnaire Design
domain: psychology
course: research-methods-psychology
prerequisites:
- id: descriptive-research-methods
  type: hard
- id: sampling-in-psychology
  type: soft
- id: operational-definitions
  type: soft
- id: sampling-methods
  type: soft
- id: sample-vs-population
  type: soft
builds-toward:
- reliability-in-measurement
- validity-in-measurement
tags:
- survey
- Likert-scale
- response-bias
- questionnaire
- self-report
stage: formal-systems
status: validated
---

# Survey and Questionnaire Design

## Core Idea
Surveys use structured questions to collect self-reported data from many participants quickly and inexpensively. Question wording, response format (Likert, forced-choice, open-ended), and order can dramatically affect responses through acquiescence bias, social desirability bias, and question order effects. Standardized questionnaires with established reliability and validity are preferred over ad hoc measures. Surveys are strong on breadth but weak on depth and cannot determine causation.

## How It's Best Learned
Critique a poorly designed survey — identify leading questions, double-barreled items, and ambiguous wording — then rewrite it. Test your revised survey on classmates and note unexpected interpretations.

## Common Misconceptions
- More questions do not make a survey more valid; poorly worded items reduce validity regardless of length.
- Self-report data is not inherently unreliable — its quality depends on question design and the construct being measured.

## Questions

```yaml
- question: "A survey asks: 'Given the well-documented health benefits of regular exercise, how many times per week do you work out?' This question is an example of:"
  type: multiple-choice
  options:
    - "Social desirability bias — it implies an admirable behavior respondents feel pressured to report"
    - "A leading question — it embeds an assumption ('well-documented benefits') that will inflate reported exercise frequency"
    - "Acquiescence bias — respondents will tend to agree with the embedded premise regardless of their behavior"
    - "A double-barreled item — it asks about both frequency and type of exercise simultaneously"
  answer: 1
  explanation: "The phrase 'well-documented health benefits' presupposes both that exercise is beneficial and that respondents should be exercising. This framing makes respondents more likely to overreport exercise frequency to align with the embedded assumption. Leading questions do not measure the true construct — they measure the construct contaminated by the question's framing."

- question: "A researcher asks about general life satisfaction at the end of a long section about recent personal setbacks and regrets. Compared to placing the life satisfaction question first, this order will likely:"
  type: multiple-choice
  options:
    - "Have no effect, since life satisfaction is a stable trait unaffected by question order"
    - "Produce lower satisfaction ratings, because the preceding questions prime negative thoughts that are still cognitively accessible"
    - "Produce higher satisfaction ratings, because participants feel relief and contrast their hardships against their baseline"
    - "Produce more honest responses, since participants are in a more reflective and introspective state"
  answer: 1
  explanation: "This is a question order effect driven by the availability heuristic: the preceding questions about setbacks make negative experiences cognitively accessible, so they are disproportionately weighted when assessing overall life satisfaction. Survey responses are not retrieved from a stable mental file — they are constructed in the moment from whatever is most accessible. Randomizing question order within sections is a practical defense against the worst of these effects."

- question: "A question about general happiness placed after several questions about recent disappointments will tend to produce lower happiness ratings than the same question placed at the beginning of the survey."
  type: true-false
  answer: true
  explanation: "Question order effects are well-documented and operate through priming and the availability heuristic. Questions that activate negative affect or make negative memories cognitively salient raise the weight of those experiences in subsequent judgments. This is not random noise — it is a predictable psychological mechanism that must be controlled for in survey design."

- question: "Adding more questions to a survey increases its validity by providing more data points about the construct being measured."
  type: true-false
  answer: false
  explanation: "Validity is about whether questions accurately measure the intended construct, not about quantity. Poorly worded items — leading questions, double-barreled items, ambiguous phrasing — reduce validity regardless of how many items are included. A short survey of well-designed questions is more valid than a long survey contaminated by bias. Length can improve reliability (by averaging over more observations) but does not guarantee validity."

- question: "What is acquiescence bias, and how does including reverse-keyed items in a Likert-scale survey help detect and correct for it?"
  type: short-answer
  answer: "Acquiescence bias is the tendency to agree with survey items regardless of content — respondents systematically lean toward 'agree' or 'strongly agree' independent of what the item says. Reverse-keyed items state the opposite of the measured construct, so a high scorer on the trait should *disagree* with them. If a respondent agrees with both regular and reverse-keyed items equally, that pattern flags acquiescence. Researchers can identify affected respondents and correct scores accordingly."
  explanation: "Acquiescence bias is particularly problematic for agree/disagree and true/false formats. If all items on a scale point the same direction, there is no way to distinguish genuine agreement from systematic acquiescence. Reverse-keyed items create an internal consistency check and allow researchers to separate authentic responses from response style artifacts."
```

## Explainer

Surveys are the workhorse of descriptive research in psychology because they let you collect self-reported data from many people quickly and cheaply. But the speed and scale that make surveys attractive also make them treacherous: poor question design systematically biases responses, and those biases are invisible in the final dataset unless you know what to look for. Your prerequisite in descriptive research methods gives you the framework; your work on operational definitions tells you why precise question wording matters; and your background in sampling helps you think about who is actually answering your questions.

The most fundamental design challenge is that survey questions are not neutral windows onto mental states — they are **stimuli that produce responses**. The same underlying attitude can generate dramatically different responses depending on how the question is phrased, what comes before it, and what response options are offered. **Leading questions** embed assumptions ("How often do you exercise?" presupposes you exercise at all). **Double-barreled items** ask two questions at once ("I find this class interesting and useful" — what does agreement mean when someone finds it useful but boring?). **Acquiescence bias** is the tendency to agree with statements regardless of content — a problem for True/False or agree/disagree formats that can be partially addressed by including reverse-keyed items. **Social desirability bias** inflates reports of admirable behaviors (voting, helping others) and deflates reports of stigmatized ones (drug use, racist attitudes).

**Response format** shapes what gets measured. Likert-type scales (Strongly Disagree to Strongly Agree) are the most common format for attitude measurement, but the number of response options, whether to include a midpoint, and whether to label all points or only the endpoints all affect responses. Forced-choice formats (choose between two options) avoid acquiescence bias but may feel artificial. Open-ended questions produce richer data but require coding for analysis. No format is universally best — the choice depends on the construct, the population, and whether you need numbers for statistical analysis or narrative for understanding.

Question order effects illustrate how much context shapes response. A question about general happiness asked *after* a question about recent relationship problems will receive lower ratings than the same question asked first — the relationship question primes negative affect and makes it accessible when the happiness question arrives. This is not randomness; it is a predictable psychological mechanism (the **availability heuristic**) operating on your survey instrument. Randomizing item order within sections is a practical defense against the worst order effects. Your prerequisite in sampling matters here too: even a beautifully designed survey generalizes only to the population your sample represents, and convenience samples (introductory psychology students, online platform workers) limit the conclusions you can draw about broader populations.


