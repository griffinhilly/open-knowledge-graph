---
id: research-ethics-human-subjects
title: Research Ethics in Social Science
domain: social-sciences
course: research-methods-social-science
prerequisites: []
builds-toward:
- ethnography-advanced-methods
- interview-methods-social-science
- focus-group-research
tags:
- ethics
- IRB
- consent
- integrity
- vulnerable-populations
stage: abstract-reasoning
status: validated
---

# Research Ethics in Social Science

## Core Idea
Covers ethical principles governing human subjects research: informed consent, confidentiality, minimizing harm, and justice. Examines institutional review processes, special considerations for vulnerable populations, and emerging challenges in digital/digital ethnography and secondary data research.

## How It's Best Learned
Review actual IRB protocols and exemption determinations, debate borderline cases (online observation, incentive structures), design consent processes for specific study populations.

## Common Misconceptions
- Ethics applies only to experimental research
- Confidentiality is purely technical
- Vulnerable populations should be excluded rather than protected

## Questions

```yaml
- question: "A researcher offers impoverished participants $500 to join a low-risk survey study about financial stress. An IRB reviewer flags the payment as an ethical concern. What is the specific problem?"
  type: multiple-choice
  options:
    - "Any payment to research participants is unethical because it introduces selection bias"
    - "The payment may constitute an undue inducement, effectively purchasing consent from people who cannot reasonably decline due to financial need"
    - "The study violates beneficence because surveys cannot directly benefit low-income populations"
    - "Confidentiality cannot be guaranteed when participants are financially motivated to share information"
  answer: 1
  explanation: "The concern is undue inducement: a payment large enough that economically disadvantaged people feel they cannot reasonably decline compromises the voluntariness that informed consent requires — the 'free from coercion' component of respect for persons. Option A is wrong: modest compensation is standard and appropriate. The ethical issue is not payment itself but whether the payment overwhelms participants' capacity to decline. Researchers must calibrate incentives to compensate for time and inconvenience without effectively purchasing consent."

- question: "A researcher conducts an anonymous online survey where participants provide no names or contact information. Which statement best describes the privacy protection?"
  type: multiple-choice
  options:
    - "The study provides confidentiality, because the researcher commits not to disclose responses"
    - "The study provides anonymity, because the researcher never knew who participated"
    - "The study provides both confidentiality and anonymity, since no names are collected"
    - "Online surveys provide no meaningful privacy protection because IP addresses can be traced"
  answer: 1
  explanation: "Anonymity means the researcher genuinely never knew who participated — no identifying information was ever collected, so there is no link to protect. Confidentiality is different: it applies when the researcher does know who participants are and commits to protecting that information. When participants provide no names or contact information, the study is anonymous, not merely confidential. Options A and C confuse the two: anonymity and confidentiality are mutually exclusive — you either know who they are (confidentiality) or you don't (anonymity)."

- question: "Because children can rarely give legal consent to research participation, they should generally be excluded from studies to protect them from potential harm."
  type: true-false
  answer: false
  explanation: "This reasoning gets ethics backwards. Excluding vulnerable populations from research is itself an ethical problem: it builds a scientific literature on convenient populations while leaving out people who may most need the benefits of research. The Belmont principle of justice requires fair distribution of the burdens and benefits of research. Children and other vulnerable groups receive heightened protections — parental consent, child assent for those old enough to understand, enhanced IRB scrutiny — not blanket exclusion. The goal is tailored procedures that restore genuine voluntariness."

- question: "A study that collects participants' first names and zip codes is confidential (not anonymous) even if no other direct identifiers are recorded."
  type: true-false
  answer: true
  explanation: "Confidentiality applies whenever the researcher retains any information that could link data back to individuals — including partial identifiers. Modern re-identification research shows that combinations of name, zip code, age, or sex alone can uniquely identify many individuals in a dataset. 'De-identified' is not a fixed category achieved by withholding one identifier; it requires ongoing assessment. Any study where the researcher holds linking information, even partial, is confidential rather than anonymous and requires active protective measures."

- question: "Explain the difference between anonymity and confidentiality in human subjects research, and give one example of each."
  type: short-answer
  answer: "Anonymity means the researcher never collected identifying information — there is no link between participant identity and their data. Example: a ballot-box survey where respondents drop in completed forms with no names. Confidentiality means the researcher knows who participants are but commits to protecting that information from disclosure. Example: an interview study where participants are identified in research records but appear only by pseudonym in publications and stored transcripts."
  explanation: "The distinction matters practically: truly anonymous studies offer the strongest privacy protection but cannot permit follow-up contact or longitudinal tracking. Confidential studies enable richer designs but require active data security (separate storage of identifiers, secure destruction protocols, restricted access). Misrepresenting a confidential study as anonymous — because no names were collected, even though emails were — is an error that undermines the accuracy of participants' informed consent."
```

## Explainer

Research ethics in social science isn't a bureaucratic obstacle — it's a response to real history. The mid-twentieth century produced a series of research scandals that revealed how badly science could harm people when investigators prioritized knowledge production over participant welfare. The Tuskegee Syphilis Study (1932–1972) withheld treatment from Black men with syphilis without their knowledge or consent. Stanley Milgram's obedience experiments (1960s) deceived participants and caused genuine psychological distress. The Belmont Report (1979) emerged from this history, establishing the three principles that still organize research ethics: **respect for persons** (autonomy, informed consent), **beneficence** (maximize benefits, minimize harms), and **justice** (fair distribution of the burdens and benefits of research). Understanding ethics means understanding what these principles are trying to prevent, not just what they require.

**Informed consent** is the operational expression of respect for persons. It requires that participants understand what they're agreeing to, have genuine capacity to consent, and are free from coercion. Each component matters. "Understanding" means disclosure in accessible language, not legal fine print. "Capacity" means the person can process and evaluate the information — children, individuals with cognitive impairments, and people in crisis may lack full capacity, which requires substitution procedures or special protections. "Free from coercion" is subtler: a modest gift card in a survey study is a convenience; a large payment to an impoverished population creates an **undue inducement** that compromises voluntariness. Researchers must calibrate incentives to attract participation without effectively purchasing consent.

**Confidentiality** and **anonymity** are related but distinct concepts that researchers frequently conflate. Anonymity means you never knew who the participant was — you collected no identifying information. Confidentiality means you do know who they are, but you commit to protecting that information from disclosure. Most social science research involves confidentiality, not anonymity: interview studies, surveys with contact information for follow-up, observational studies with field notes. Protecting confidentiality requires active measures: data stored separately from identifiers, pseudonyms in transcripts, aggregate reporting of sensitive findings, secure data destruction protocols. Digital data raises new challenges — supposedly de-identified datasets can often be re-identified by combining variables, so "confidential" requires ongoing vigilance, not a one-time de-identification step.

**Vulnerable populations** — children, prisoners, pregnant women, individuals with impaired decision-making, economically disadvantaged groups — receive heightened protections not because they should be excluded from research, but because the ordinary consent framework may not fully protect them. Children cannot give legal consent; their parents consent on their behalf, but children old enough to understand must also give **assent**. Prisoners face coercive institutional pressures that make "voluntary" participation ambiguous. The solution is not exclusion — that would simply reproduce a research literature built on convenient populations while ignoring the people who most need to benefit from research findings. The solution is tailored procedures that restore genuine voluntariness and proportionality between risks and benefits. Institutional Review Boards (IRBs) exist to make these judgments systematically, but researchers must arrive at IRB review with principled reasoning, not just hoping for approval.
