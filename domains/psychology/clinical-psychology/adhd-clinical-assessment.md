---
id: adhd-clinical-assessment
title: Attention-Deficit/Hyperactivity Disorder
domain: psychology
course: clinical-psychology
prerequisites:
- id: dsm-5-diagnostic-criteria-and-classification
  type: hard
- id: dopamine-system
  type: soft
builds-toward:
- comorbidity-complex-presentations
tags:
- ADHD
- neurodevelopmental
stage: expert
status: draft
---

# Attention-Deficit/Hyperactivity Disorder

## Core Idea
Attention-Deficit/Hyperactivity Disorder is a neurodevelopmental disorder characterized by inattention and/or hyperactivity-impulsivity affecting functioning or development. ADHD involves executive function dysregulation and impaired impulse control. Often undetected in adults and girls, ADHD frequently co-occurs with mood and anxiety disorders.

## Questions

```yaml
- question: "A parent asks why stimulant medications have a 'paradoxical calming effect' on their child with ADHD, since stimulants are supposed to increase arousal. What is the correct explanation?"
  type: multiple-choice
  options:
    - "Children with ADHD have reversed dopamine receptors that respond oppositely to stimulation compared to neurotypical individuals"
    - "Stimulants increase dopamine and norepinephrine availability in prefrontal circuits, optimizing the catecholamine signal levels needed for executive control — the result is improved regulation, not sedation"
    - "Methylphenidate primarily acts on brainstem arousal centers, suppressing the hyperactivity response"
    - "The calming effect is behavioral rather than pharmacological — children respond to the increased structure that comes with taking medication"
  answer: 1
  explanation: "ADHD involves dysregulation of prefrontal dopamine and norepinephrine signaling. The prefrontal cortex requires precisely calibrated catecholamine levels for executive function — planning, sustained attention, impulse control, and working memory. In ADHD, this calibration is disrupted. Stimulants (methylphenidate, amphetamines) increase dopamine and norepinephrine availability in prefrontal circuits, pushing levels toward the optimal range. The result is better executive control — not sedation or suppression of arousal. The 'calming' appearance reflects improved self-regulation, not a sedative effect."

- question: "A clinician evaluates a college student with persistent distractibility and poor concentration and, after a brief intake interview, concludes the student has ADHD and prescribes stimulants. What is most problematic about this approach?"
  type: multiple-choice
  options:
    - "ADHD cannot be diagnosed in adults — it is strictly a childhood disorder"
    - "Stimulant medications are not approved for college-age patients"
    - "Inattention and poor concentration are nonspecific symptoms produced by many conditions — anxiety, depression, sleep disorders, trauma, and learning disabilities — all of which require ruling out; a valid ADHD diagnosis also requires evidence of onset before age 12 and impairment across multiple settings"
    - "The clinician should have used neuroimaging before making a diagnosis"
  answer: 2
  explanation: "The core problem is diagnostic specificity. Inattentive symptoms are not unique to ADHD — they are a common feature of anxiety, depression, sleep deprivation, trauma, and learning disabilities. A proper ADHD assessment integrates multiple informants, multiple methods (structured interview + rating scales + records review), rules out differential diagnoses, and verifies DSM-5 criteria including onset before age 12 and impairment in two or more settings. Prescribing stimulants without this rigor risks treating secondary symptoms while missing the primary condition — or correctly identifying a stimulant responder who nonetheless doesn't have ADHD."

- question: "According to DSM-5 criteria, ADHD cannot be diagnosed in an adult who reports no clear symptoms or functional impairment before age 12."
  type: true-false
  answer: true
  explanation: "The DSM-5 requires that several inattentive or hyperactive-impulsive symptoms be present before age 12. This criterion reflects ADHD's classification as a neurodevelopmental disorder — it emerges during development, not as an adult-onset condition. This doesn't mean childhood symptoms must have been severe or professionally identified; many adults seeking diagnosis recall childhood difficulties that were masked or compensated for. But the onset criterion must be satisfied, which is why collateral information (school records, parent reports) is valuable in adult assessments."

- question: "Girls with ADHD are typically diagnosed earlier than boys because ADHD symptoms are equally observable across genders."
  type: true-false
  answer: false
  explanation: "Girls with ADHD are systematically diagnosed later than boys, often not until adolescence or adulthood. The primary reason is presentation asymmetry: boys more commonly show hyperactive-impulsive symptoms (fidgeting, blurting, disruptive behavior) that are visible to teachers and trigger referrals. Girls more commonly show the inattentive presentation — daydreaming, disorganization, internal distractibility — which is less disruptive and more easily missed. This diagnostic asymmetry produces real harm: girls with ADHD often accumulate years of academic underperformance, internalized shame, and secondary anxiety or depression before receiving a correct diagnosis."

- question: "Why is a symptom checklist alone insufficient for an ADHD diagnosis, and what does a proper clinical assessment need to establish?"
  type: short-answer
  answer: "Inattention, distractibility, and impulsivity are nonspecific symptoms that occur across many conditions — anxiety, depression, sleep disorders, trauma, learning disabilities, and others. A symptom checklist cannot distinguish primary ADHD from attentional difficulties secondary to these conditions, which require different interventions. A proper ADHD assessment must: (1) use multiple informants (self-report plus collateral reports from parents, partners, or teachers) to verify impairment across settings; (2) use multiple methods including structured diagnostic interviews and standardized rating scales; (3) review historical records to establish onset before age 12; (4) systematically rule out differential diagnoses. The DSM-5 requires symptoms in two or more settings and significant functional impairment. This rigor is necessary to avoid over-diagnosing context-specific problems and to avoid missing genuine ADHD masked by comorbidities."
```

## Explainer

From your study of the DSM-5 framework, you know that diagnoses are organized around symptom clusters with specific duration, severity, and impairment criteria. **ADHD** is classified as a **neurodevelopmental disorder**, meaning it emerges during development and reflects differences in how the brain matures rather than being an acquired or late-onset condition. This matters clinically: ADHD is not caused by poor parenting, lack of effort, or moral failing. It is a genuine neurological difference with a clear biological basis — yet it is also one of the most heterogeneous, frequently misunderstood, and contextually variable diagnoses in practice.

The DSM-5 defines three presentations: **predominantly inattentive**, **predominantly hyperactive-impulsive**, and **combined**. The inattentive symptoms — difficulty sustaining attention, losing materials, failing to follow through on tasks, becoming easily distracted — are often less visible than hyperactive symptoms and go undiagnosed for longer, particularly in girls and adults. By the time an adult presents for assessment, they may have accumulated years of academic underperformance, occupational difficulty, and internalized shame without understanding the underlying cause. Hyperactive-impulsive symptoms — fidgeting, blurting, difficulty waiting — tend to be more observable in childhood and more often trigger referrals, particularly in boys. This diagnostic asymmetry produces real harm: the people who present later are often those who needed help earliest.

Connecting to the dopamine system from your prerequisites: the leading neurobiological account of ADHD involves dysregulation of **prefrontal dopamine and norepinephrine signaling**. The prefrontal cortex depends on precisely calibrated catecholamine levels for executive function — planning, inhibition, sustained attention, and working memory. In ADHD, this calibration is disrupted, producing the executive function deficits that are now considered the core cognitive impairment. This mechanism explains why stimulant medications work: methylphenidate and amphetamines increase dopamine and norepinephrine availability in prefrontal circuits, restoring signal levels toward optimal and improving executive control. The counterintuitive "calming" effect of stimulants in ADHD makes sense once you understand it as optimizing prefrontal signal, not sedating.

A proper clinical ADHD assessment goes far beyond a symptom checklist. It integrates multiple informants (self-report, plus collateral reports from parents, partners, or teachers), multiple methods (structured diagnostic interviews, standardized rating scales, records review), and systematic ruling out of alternatives. The DSM-5 criteria require symptoms present in two or more settings, onset before age 12, and significant functional impairment — these requirements guard against over-diagnosing context-specific behavior that mimics ADHD but isn't. Sleep disorders, anxiety, learning disabilities, and trauma all produce attentional difficulties that can superficially resemble ADHD but require different interventions.

The frequent co-occurrence of ADHD with mood and anxiety disorders is not coincidental. Years of ADHD-related failures and frustrations generate secondary depression and anxiety; conversely, anxiety and depression produce distractibility and poor concentration that mimic ADHD inattention. Clinical skill lies in disentangling what is primary and what is secondary — and recognizing that treating only the comorbidity while missing the ADHD, or vice versa, typically produces incomplete improvement. ADHD is a window into the complexity of neurodevelopmental diagnosis: biologically real, contextually variable, diagnostically demanding, and consequential if missed.
