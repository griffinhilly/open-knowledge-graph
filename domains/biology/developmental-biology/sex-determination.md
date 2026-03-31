---
id: sex-determination
title: Sex Determination
domain: biology
course: developmental-biology
prerequisites:
- id: cell-fate-determination
  type: hard
- id: developmental-signaling-pathways
  type: hard
builds-toward: []
tags:
- sex-determination
- SRY
- dosage-compensation
- gonad-development
- environmental-sex-determination
stage: expert
status: validated
---
# Sex Determination

## Core Idea
Sex determination is the developmental process that directs an initially bipotential gonad to develop as either a testis or an ovary, which then drives secondary sexual differentiation of the entire body. In mammals, the SRY gene on the Y chromosome activates Sox9 in the bipotential gonad, initiating a testis-determining cascade (Sertoli cell differentiation, testosterone production, Mullerian duct regression). In the absence of SRY, the default pathway (Wnt4/RSPO1/beta-catenin) drives ovarian development. Other animals use different mechanisms: ZW chromosomal system in birds, X:autosome ratio in Drosophila, temperature-dependent determination in many reptiles. Sex determination reveals how a single genetic or environmental signal can redirect an entire developmental trajectory.

## Questions

```yaml
- question: "In mammals, the bipotential gonad develops as an ovary unless SRY is expressed. If SRY is experimentally expressed in an XX mouse embryo's gonad, what develops?"
  type: multiple-choice
  options:
    - "A normal ovary, because XX chromosomes override SRY"
    - "A testis, because SRY is sufficient to initiate the testis-determining cascade regardless of chromosomal sex"
    - "A mixed gonad with both testicular and ovarian tissue"
    - "The gonad degenerates because of the conflict between SRY and XX chromosomes"
  answer: 1
  explanation: "This experiment (transgenic XX mice carrying the Sry gene) was performed by Robin Lovell-Badge's group and demonstrated that SRY is sufficient for testis determination. The XX mice with SRY developed testes, male internal anatomy, and male external appearance (though they were infertile because spermatogenesis requires Y-linked genes beyond SRY). This proved that mammalian sex determination is a binary switch triggered by a single gene — SRY activates Sox9, which drives Sertoli cell differentiation and the downstream testis program, overriding the default ovarian pathway."

- question: "Temperature-dependent sex determination (TSD) in reptiles demonstrates that genetic factors play no role in reptilian sex determination."
  type: true-false
  answer: false
  explanation: "While incubation temperature is the primary sex-determining signal in many reptiles (higher temperatures produce females in some species, males in others), this temperature signal acts through the same molecular pathways (aromatase, Sox9, DMRT1, Foxl2) used in genetic sex determination. Temperature influences the expression or activity of these conserved sex-determination genes. Furthermore, some reptile species have genetic sex determination (GSD), some have TSD, and some have both. The molecular toolkit for gonad differentiation is conserved; what differs is the upstream trigger — a genetic signal (SRY, ZW) versus an environmental signal (temperature)."

- question: "Why must sex determination include active maintenance of the chosen sex throughout life, rather than being a single irreversible decision?"
  type: short-answer
  answer: "Adult gonads continuously maintain their sexual identity through mutual antagonism between testis-maintaining and ovary-maintaining transcription factor programs. DMRT1 maintains testis identity by repressing Foxl2 (an ovarian transcription factor); Foxl2 maintains ovary identity by repressing Sox9 (a testis transcription factor). If DMRT1 is deleted in adult mouse testes, Sertoli cells transdifferentiate into granulosa-like cells and the testis begins to adopt ovarian features. If Foxl2 is deleted in adult ovaries, granulosa cells transdifferentiate into Sertoli-like cells. This reveals that sex determination is not a one-time event but an ongoing active process — adult gonadal identity requires continuous transcriptional reinforcement, and the alternative sexual program remains latent and ready to activate if the repressive barrier is removed."
  explanation: "This discovery (Matson et al., 2011; Uhlenhaut et al., 2009) was surprising because it overturned the assumption that adult cell fates are permanently fixed. It also has implications for disorders of sex development and for understanding how environmental endocrine disruptors might affect gonadal function."
```

## Explainer

The development of sex is one of the most dramatic binary decisions in biology — from a single undifferentiated primordium, the gonad becomes either a testis or an ovary, and this choice cascades through the entire body to produce male or female anatomy, physiology, and behavior. The mechanisms that drive this decision vary remarkably across the animal kingdom, but the downstream effectors — the transcription factors and signaling pathways that build testes versus ovaries — are deeply conserved.

In **mammals**, the bipotential gonad develops from intermediate mesoderm and initially contains both the potential testis-forming cells (supporting cell precursors) and the potential ovary-forming cells. The switch is **SRY** (Sex-determining Region of the Y chromosome), a transcription factor that activates **Sox9** in the gonadal somatic cells. Sox9 drives their differentiation into **Sertoli cells** — the key orchestrators of testis development. Sertoli cells organize the gonad into testis cords, produce Anti-Mullerian Hormone (AMH, which degenerates the female reproductive tract precursor), and signal to Leydig cells to produce testosterone (which drives male external genital development and brain masculinization). Without SRY (XX genotype), the gonad follows the ovarian pathway: **Wnt4** and **RSPO1** activate beta-catenin signaling, driving **Foxl2** expression and granulosa cell differentiation. The ovary produces estrogen, which drives female tract development and secondary sexual characteristics.

In **birds**, the system is chromosomally reversed: females are ZW and males are ZZ. The dosage of the Z-linked gene **DMRT1** determines sex — two copies (ZZ) drive testis development, one copy (ZW) permits ovary development. In **Drosophila**, sex is determined by the ratio of X chromosomes to autosomes (not by the Y chromosome), acting through the Sex-lethal (Sxl) RNA splicing cascade. In **many reptiles and some fish**, **temperature** during a critical developmental window determines sex — typically by influencing the expression of aromatase (which converts testosterone to estrogen) or other components of the conserved sex-determination molecular toolkit.

A remarkable recent discovery is that sex determination is not a one-time event. In adult mouse gonads, testis identity requires continuous expression of **DMRT1**, which represses the ovarian program (Foxl2). Deleting DMRT1 in adult testes causes Sertoli cells to transdifferentiate into granulosa-like (ovarian) cells. Conversely, deleting **Foxl2** in adult ovaries causes granulosa cells to transdifferentiate into Sertoli-like (testicular) cells. The two sexual programs are in continuous mutual antagonism, and the adult gonad actively maintains its identity rather than passively retaining it. This ongoing maintenance requirement means that adult gonadal sex is more plastic than previously assumed — a finding with implications for understanding disorders of sex development, the effects of endocrine disruptors, and the remarkable natural sex changes observed in some fish species.
