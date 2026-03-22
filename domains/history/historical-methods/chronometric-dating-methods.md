---
id: chronometric-dating-methods
title: Chronometric Dating Methods
domain: history
course: historical-methods
prerequisites: []
builds-toward:
- radiocarbon-and-scientific-dating
- stratigraphic-interpretation-archaeology
tags:
- chronology
- dating
- time
- sequence
stage: formal-systems
status: draft
---

# Chronometric Dating Methods

## Core Idea
Absolute and relative dating situate events and artifacts in time. Relative methods (stratigraphy, typology, paleography) establish sequence without precise dates. Absolute methods (radiocarbon, dendrochronology, historic calendars) assign calendar years. Every dating technique has margins of error, assumptions about preservation, and potential for contamination or misinterpretation.

## Questions

```yaml
- question: "An archaeologist finds a Roman coin (known to circulate between 50 BCE and 100 CE) in stratum 3 of an excavation and concludes stratum 3 dates to that period. What assumption makes this conclusion potentially wrong?"
  type: multiple-choice
  options:
    - "She assumes the coin was minted locally rather than imported from elsewhere"
    - "She assumes the coin was deposited when it was still in active use; the error would be if it was an heirloom deposited centuries later, or if the stratum was disturbed"
    - "She assumes radiocarbon dating would confirm the stratigraphic date, ignoring that coins contain no organic material"
    - "She assumes typology is less reliable than stratigraphy and should have used stratigraphy alone"
  answer: 1
  explanation: "Typological dating assumes the object was deposited when it was contemporary — still in active use. But coins were often kept as antiques or curiosities for centuries after they stopped circulating; a Roman coin in a 5th-century context does not prove a 1st-century deposit. Stratified disturbance is the other major risk: pits dug later can redeposit older material into younger layers. This is why combining multiple independent lines of evidence matters more than relying on a single dating anchor."

- question: "Radiocarbon dating gives a date of 1200 BCE ± 200 years for a wooden beam. Dendrochronology on the same beam gives an exact felling date of 980 BCE. These results conflict. What is the most appropriate response?"
  type: multiple-choice
  options:
    - "Accept the radiocarbon date because it is grounded in physics and is more reliable than tree rings"
    - "Accept the dendrochronological date because it is more precise, and dismiss the radiocarbon result as error"
    - "Treat the conflict as evidence to investigate: check for old-wood effect, reused timber, or contamination, and report both dates with their assumptions"
    - "Average the two dates to produce a best estimate of approximately 1090 BCE"
  answer: 2
  explanation: "When methods conflict, that conflict is itself important evidence — not a problem to paper over by choosing the 'better' method. The radiocarbon date could reflect old-wood effect (the beam came from inner rings of a long-lived tree that died long before the tree was felled) or reused timber from an older structure. Dendrochronology measures the felling year precisely but requires a matching ring sequence. The correct response is to investigate the source of the discrepancy and report both results honestly, which is itself an informative finding."

- question: "Radiocarbon dating directly measures the calendar year when an artifact was made or used, giving a precise absolute date with no margin of error."
  type: true-false
  answer: false
  explanation: "Radiocarbon dating measures the amount of carbon-14 remaining in organic material and uses the known decay rate to estimate when the organism died — not necessarily when an artifact was made or used. The method has several layers of uncertainty: atmospheric C-14 concentrations have varied over time (requiring calibration curves), the decay process produces inherent statistical uncertainty (results are expressed as a range, e.g., ± 150 years), and the date reflects biological death, not human crafting or use. It is a powerful absolute method, but never an exact one."

- question: "Stratigraphic analysis can establish the relative sequence of archaeological deposits but cannot by itself assign calendar dates to those deposits."
  type: true-false
  answer: true
  explanation: "Stratigraphy is a relative dating method: the law of superposition tells you that lower layers were deposited before upper ones, establishing temporal sequence. But sequence alone does not tell you when something happened in calendar years — only that it happened before something else. To get calendar dates, you need an absolute method (radiocarbon, dendrochronology, historical records) to anchor one or more layers to a specific year, from which the sequence can be resolved into a calendar chronology."

- question: "Why do careful historians and archaeologists use multiple dating methods rather than relying on a single technique, even when one method seems highly reliable for their material?"
  type: short-answer
  answer: "Every dating method rests on assumptions that can be violated in specific contexts. Radiocarbon assumes relatively constant atmospheric C-14 (not always true; calibration corrects for this) and uncontaminated organic material. Stratigraphy assumes undisturbed deposits (but sites are excavated, pits are dug, material is reused). Typology assumes styles spread and went out of fashion uniformly (peripheral regions may preserve old styles long after they're obsolete elsewhere). When independent methods agree, confidence is higher because their different assumptions would have to fail simultaneously in the same direction. When methods conflict, the conflict often reveals something genuinely unexpected — contamination, disturbance, or unusual preservation — that a single-method approach would have silently misrepresented as a settled date."
  explanation: "Triangulation — agreement among independent lines of evidence — is stronger than any single line. It also converts dating from a black-box answer into an honest account of what the evidence shows, how reliable it is, and what would change the conclusion. This is the core intellectual practice the topic is trying to teach."
```

## Explainer

Every historical claim about *when* something happened rests on a dating method, whether or not historians make that method explicit. Understanding how dates are established — and where they can go wrong — is one of the most practically important skills in historical methods, because a misdated document, artifact, or site can cascade into a wrong account of causation, chronology, and context. Dating methods fall into two fundamental categories, and the distinction between them matters: **relative dating** tells you the order of things; **absolute dating** tells you the calendar year.

Relative dating methods establish sequence without assigning specific dates. **Stratigraphy** — the geological principle that in undisturbed deposits, lower layers are older — is the backbone of archaeological chronology. A pot found beneath another layer of occupation predates whatever was deposited above it. **Typology** compares the forms of artifacts (pottery shapes, coin styles, weapon designs) to established sequences: if you know that a particular style of brooch was fashionable in a specific century, finding that brooch style helps date the layer containing it. **Paleography** — the analysis of historical handwriting styles — works similarly for documents: the shape of letters, abbreviation conventions, and parchment preparation all changed over time, allowing trained scholars to assign a manuscript to a period even without any explicit date in the text. These relative methods are indispensable but have a vulnerability: they depend on comparison sequences that themselves had to be established through some other means.

Absolute methods assign actual calendar years, usually with margins of error. **Radiocarbon dating** is the most famous: living organisms incorporate atmospheric carbon-14, which begins decaying at a known rate after death. By measuring how much carbon-14 remains in organic material (wood, bone, charcoal, grain), scientists can calculate when the organism died — typically with an uncertainty of decades to a few centuries depending on the age and calibration method. **Dendrochronology** — tree-ring dating — is often more precise: trees grow one ring per year, and the pattern of thick and thin rings records climate variation. When the rings of ancient timber overlap with a continuous ring record, the timber can be dated to the exact year it was felled. **Calendrical synchronizations** use dated historical records (eclipses, royal regnal years, astronomical events that can be calculated backward) to anchor floating chronologies to absolute years.

The crucial insight is that every method embeds assumptions that can be violated. Radiocarbon assumes that atmospheric carbon-14 concentrations have been constant (they haven't been, which is why calibration curves are essential). Stratigraphy assumes undisturbed deposition (but sites are dug up, pits are dug, material is reused). Typological dating assumes that object styles spread uniformly and don't persist in peripheral areas long after they've gone out of fashion elsewhere. A good historian or archaeologist is not someone who applies dating methods mechanically but someone who understands which assumptions apply to a particular context, what the margin of error actually means, and how to triangulate across multiple methods to build a convergent and honest chronology. When methods conflict, that conflict is itself important evidence — it often signals contamination, disturbance, or something genuinely unexpected about the site or material.
