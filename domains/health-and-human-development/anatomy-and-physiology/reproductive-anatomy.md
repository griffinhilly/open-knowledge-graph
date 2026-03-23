---
id: reproductive-anatomy
title: Reproductive System Anatomy and the Hormonal Cycle
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: body-organization-and-terminology
  type: hard
- id: endocrine-glands-and-hormones
  type: hard
- id: positive-feedback-mechanisms
  type: hard
- id: meiosis
  type: soft
tags:
- reproductive-organs
- menstrual-cycle
- spermatogenesis
- oogenesis
- gonadal-hormones
- HPG-axis
stage: formal-systems
status: validated
---

# Reproductive System Anatomy and the Hormonal Cycle

## Core Idea
Male reproductive anatomy centers on testes (spermatogenesis, testosterone production), epididymis (sperm maturation), vas deferens, and accessory glands (seminal vesicles, prostate, bulbourethral glands) that contribute to semen. Female reproductive anatomy includes ovaries (oogenesis, estrogen and progesterone production), fallopian tubes, uterus, cervix, and vagina. The hypothalamic-pituitary-gonadal (HPG) axis regulates both sexes: GnRH drives FSH and LH release, which regulate gonadal function. The female menstrual cycle integrates follicular phase, ovulation (triggered by the LH surge — a rare positive feedback loop), and luteal phase, with cyclical changes in the uterine endometrium. Fertilization, implantation, and pregnancy involve dramatic hormonal shifts that override the normal cycle.

## How It's Best Learned
Graph estrogen, progesterone, LH, and FSH levels across the ~28-day menstrual cycle on the same timeline. Identify the key events (follicular development, ovulation, corpus luteum formation/regression) and link each to the hormonal changes driving them.

## Common Misconceptions
- Ovulation does not occur mid-cycle in all women — the 'day 14' rule assumes a 28-day cycle and is often inaccurate.
- The LH surge is one of the few positive feedback loops in physiology; most hormonal axes use negative feedback, so this exception is worth noting explicitly.

## Questions

```yaml
- question: "During the follicular phase, rising estrogen levels initially suppress FSH and LH secretion. Yet just before ovulation, surging estrogen triggers a massive LH spike. What explains this reversal?"
  type: multiple-choice
  options:
    - "Estrogen switches from negative to positive feedback on the pituitary once it exceeds a sustained threshold (~200 pg/mL for ~36 hours), triggering the LH surge"
    - "A separate hypothalamic surge center activates on day 14 of every cycle, independent of estrogen levels"
    - "The follicle physically stimulates the ovary, which directly causes LH release through a local reflex"
    - "Progesterone from the corpus luteum triggers the LH surge by overriding the estrogen-based negative feedback"
  answer: 0
  explanation: "The LH surge is one of the most important positive feedback loops in physiology. For most of the follicular phase, estrogen exerts negative feedback on the pituitary, suppressing gonadotropin release. When the dominant follicle matures sufficiently, estrogen rises above ~200 pg/mL and is sustained there for approximately 36 hours — this crosses a threshold that switches the pituitary response from suppression to amplification. The pituitary now releases a massive surge of LH that ruptures the dominant follicle and triggers ovulation. The corpus luteum does not yet exist before ovulation, ruling out option D."

- question: "A sexually active woman receives a positive home pregnancy test 10 days after ovulation. What is the test detecting, and what does it tell us about what has happened biologically?"
  type: multiple-choice
  options:
    - "Progesterone — elevated progesterone indicates the luteal phase is extended, which correlates with pregnancy"
    - "LH — the LH surge persists through early pregnancy and is detected by home tests"
    - "hCG — the embryo has implanted and is actively secreting human chorionic gonadotropin to rescue the corpus luteum"
    - "Estrogen — the placenta begins estrogen production at implantation, which home tests detect"
  answer: 2
  explanation: "Home pregnancy tests detect hCG (human chorionic gonadotropin), a hormone secreted specifically by the embryo/trophoblast after successful implantation. hCG acts like LH to rescue the corpus luteum from the regression that would normally occur ~14 days after ovulation, maintaining progesterone production and preventing menstruation. A positive test therefore confirms not just fertilization but successful implantation — the embryo is actively signaling its presence to the maternal endocrine system."

- question: "The LH surge that triggers ovulation operates through the same negative feedback mechanism that governs GnRH, FSH, and LH throughout the rest of the menstrual cycle."
  type: true-false
  answer: false
  explanation: "The LH surge is a rare example of positive feedback in physiology. Throughout most of the cycle, the HPG axis runs on negative feedback: elevated estrogen and progesterone suppress GnRH and gonadotropin secretion — the standard regulatory pattern. Near ovulation, estrogen crosses a sustained threshold and the pituitary response switches: instead of suppressing LH release, high estrogen now stimulates it, producing the LH surge. Positive feedback loops are unusual in physiology because they amplify rather than stabilize — they are appropriate here precisely because ovulation requires a brief, explosive signal rather than steady-state regulation."

- question: "A positive pregnancy test detects hCG because the embryo secretes this hormone to prevent the corpus luteum from regressing, thereby maintaining progesterone production."
  type: true-false
  answer: true
  explanation: "After ovulation, the corpus luteum normally regresses after ~14 days if no pregnancy occurs, causing progesterone and estrogen to fall and triggering menstruation. If the embryo implants, it secretes hCG, which acts on LH receptors in the corpus luteum to maintain its function — progesterone production continues, the endometrium is preserved, and menstruation is prevented. This is the embryo's first hormonal signal to the mother, making hCG the earliest detectable marker of pregnancy. The placenta eventually takes over progesterone production around week 10."

- question: "Explain why the LH surge is described as a positive feedback mechanism and why positive feedback is unusual in reproductive physiology."
  type: short-answer
  answer: "Positive feedback occurs when a signal amplifies its own production rather than suppressing it. During the follicular phase, estrogen initially suppresses LH release (negative feedback, which maintains stability). When estrogen rises above ~200 pg/mL and is sustained for ~36 hours, the pituitary switches response and begins secreting more LH in response to the high estrogen — the output amplifies the input until the follicle ruptures. Positive feedback is unusual in physiology because it is inherently destabilizing: left unchecked, it would produce runaway amplification. It is appropriate here because ovulation requires a brief, explosive LH surge rather than a steady signal — after the follicle ruptures, estrogen drops, and the feedback loop self-terminates."
  explanation: "Understanding this switch from negative to positive feedback at a threshold is essential for understanding the timing of ovulation. It also explains why cycle length is variable: the timing of the LH surge depends on when the dominant follicle produces sufficient sustained estrogen, which varies across cycles and individuals — making the '14 days' rule an approximation."
```

## Explainer

From your study of endocrine glands and hormones, you know that the body's regulatory axes follow a hierarchical pattern: a hypothalamic releasing hormone drives pituitary hormone release, which drives a target gland, which feeds back negatively to suppress the hypothalamus and pituitary. The **hypothalamic-pituitary-gonadal (HPG) axis** follows exactly this logic. **GnRH** (gonadotropin-releasing hormone), secreted in pulses from hypothalamic neurons, drives the anterior pituitary to release **FSH** (follicle-stimulating hormone) and **LH** (luteinizing hormone). These gonadotropins act on the gonads to produce both gametes and sex steroids, which then feed back to suppress GnRH and gonadotropin secretion — negative feedback that keeps the system in steady state most of the time. What makes the female reproductive system remarkable is that this negative feedback is briefly overridden at a critical moment in the cycle.

In the male, the HPG axis runs as a steady-state negative feedback loop. Leydig cells in the testes produce **testosterone** in response to LH; testosterone feeds back to suppress GnRH and LH. Sertoli cells in the seminiferous tubules support **spermatogenesis** in response to FSH and locally high testosterone. Sperm produced in the testes are immature and non-motile; they mature and acquire motility during their two-week passage through the **epididymis** — a coiled tubule along the posterior testis. At ejaculation, sperm travel through the **vas deferens** and mix with secretions from the **seminal vesicles** (fructose for energy), **prostate** (alkaline fluid that neutralizes vaginal acidity), and **bulbourethral glands** (pre-ejaculatory mucus). Testosterone has effects far beyond the testes: it drives muscle growth, bone density, libido, and secondary sexual characteristics, all mediated by androgen receptors expressed throughout the body.

In the female, the HPG axis operates cyclically. During the **follicular phase**, rising FSH recruits a cohort of primordial follicles. One dominant follicle emerges, secreting increasing amounts of estrogen, which initially exerts negative feedback — suppressing FSH to prevent further follicle recruitment. As ovulation approaches, estrogen rises above a threshold (sustained at ~200 pg/mL for roughly 36 hours), and the pituitary response *switches*. Using your understanding of positive feedback mechanisms: the same signal that was being suppressed now amplifies its own production, triggering the **LH surge** — a massive spike in LH that induces rupture of the dominant follicle and release of the secondary oocyte. This switch is mediated by estrogen acting on different pituitary cell populations and is a genuinely rare positive feedback loop in physiology.

After ovulation, the ruptured follicle becomes the **corpus luteum**, which secretes both progesterone and estrogen during the **luteal phase**. Progesterone prepares the uterine endometrium for implantation: it thickens the lining, increases vascularization, promotes secretory gland development, and suppresses uterine contractions. If fertilization does not occur, the corpus luteum regresses after approximately 14 days, progesterone and estrogen fall, the endometrium sheds (menstruation), and the next cycle begins. If implantation occurs, the embryo secretes **hCG** (human chorionic gonadotropin), which acts like LH to rescue the corpus luteum, maintaining progesterone production until the placenta takes over at around week 10. This is why a positive pregnancy test — which detects hCG — confirms successful implantation: the embryo is actively signaling its presence to prevent menstruation.
