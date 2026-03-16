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
stage: advanced
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

## Explainer

Your prerequisite work on measurement validity taught you that a measure is only as good as how well it captures the underlying construct — and surveys are especially vulnerable to this problem because every methodological choice, from the wording of a single question to the medium of delivery, can distort what respondents report. Advanced survey design is the discipline of systematically anticipating and minimizing these distortions before data collection begins.

**Question construction** is where most measurement error originates. Leading questions prime respondents toward particular answers ("Do you agree that the government wastes too much money?"). Double-barreled questions ask about two things at once ("Do you support raising the minimum wage and strengthening unions?"), making it impossible to know which sub-question the respondent is answering. **Response option design** compounds these problems: a five-point Likert scale with no neutral midpoint forces fence-sitters to choose a side; a scale that runs from "strongly agree" to "somewhat disagree" without a "strongly disagree" anchor compresses one end of the distribution. Getting question and option design right requires **cognitive interviewing** — talking through each question with representative respondents to surface where they interpret phrasing differently than intended. This connects directly to your validity training: cognitive interviews are a form of think-aloud validity checking at the item level.

**Survey mode** — the channel through which the survey is administered — interacts with everything else. Online panels are cheap and fast but systematically underrepresent elderly, lower-income, and less digitally connected populations, creating coverage error that no statistical adjustment fully fixes. Phone surveys once reached nearly everyone but now face declining response and cell-phone sampling complications. In-person interviewing gives enumerators the ability to clarify questions and reduces item non-response, but is expensive and introduces **social desirability bias** — respondents adjust answers to appear favorable to an interviewer. Sensitive topics (income, substance use, political extremism) often require modes that give respondents privacy, like self-administered questionnaires or audio-assisted self-interview formats.

**Non-response bias** is subtler than it appears. Your sampling prerequisite covered how to draw a representative sample from a population; advanced survey design deals with what happens when the people you selected refuse to participate or can't be reached. Low response rate alone does not guarantee bias — what matters is whether non-respondents differ systematically from respondents on the variables of interest. A 30% response rate survey about TV preferences may be unbiased if non-response is random; a 70% response rate survey about vaccination attitudes may be severely biased if vaccine skeptics disproportionately decline. Analysts assess non-response bias by comparing respondents to known population benchmarks (from census data) and by following up with a random subsample of non-respondents to characterize how they differ. Scale development — building multi-item instruments for latent constructs like "trust" or "anxiety" — adds another layer, requiring item analysis, factor analysis, and test-retest reliability checks to ensure the scale consistently and validly measures what it claims to.
