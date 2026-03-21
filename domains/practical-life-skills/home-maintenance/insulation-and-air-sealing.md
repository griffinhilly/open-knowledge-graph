---
id: insulation-and-air-sealing
title: Insulation Materials and Air Sealing
domain: practical-life-skills
course: home-maintenance
prerequisites:
- id: attic-ventilation-insulation
  type: hard
- id: caulking-and-weatherstripping
  type: soft
- id: area-of-rectangles
  type: soft
- id: volume-of-rectangular-prisms
  type: soft
builds-toward: []
tags:
- insulation
- air-sealing
- energy-efficiency
- thermal-envelope
stage: abstract-reasoning
status: draft
---

# Insulation Materials and Air Sealing

## Core Idea
Insulation slows heat transfer through the building envelope, but its effectiveness depends on eliminating air leaks first — air movement bypasses insulation entirely, like wearing an unzipped jacket in winter. Common insulation materials each have distinct strengths: fiberglass batts are inexpensive and DIY-friendly but leave gaps at framing; blown-in cellulose fills irregular cavities completely; and spray foam both insulates and air-seals in a single application but costs significantly more. Thermal bridging — heat conducting through studs, joists, and other framing members that interrupt the insulation layer — reduces effective R-value by 10-25% in typical wood-frame walls and must be addressed in high-performance applications with continuous exterior insulation.

## How It's Best Learned
Before adding insulation, conduct an air-sealing pass: use canned spray foam to seal gaps around plumbing penetrations, electrical boxes, and ductwork in the attic and basement. These penetrations are where the most conditioned air escapes. An incense stick or smoke pencil at these locations on a windy day reveals leaks you would never find by visual inspection alone.

## Common Misconceptions
- Adding more insulation always reduces energy bills proportionally — if air leaks are not sealed first, warm air bypasses the insulation through gaps and penetrations, and doubling R-value in a leaky envelope yields diminishing returns.
- Fiberglass batts are a poor insulation choice — properly installed fiberglass batts (no compression, no gaps, vapor retarder facing the correct direction) perform close to their rated R-value; the problem is that poor installation is extremely common.
- Spray foam insulation makes ventilation unnecessary — spray foam creates a tight envelope, which makes mechanical ventilation (like an HRV or ERV) more important, not less, to maintain indoor air quality and prevent moisture buildup.

## Questions

```yaml
- question: "A homeowner's attic has R-19 fiberglass batts and high heating bills. A contractor recommends upgrading to R-38 batts. What should the homeowner do FIRST?"
  type: multiple-choice
  options:
    - "Install the R-38 batts immediately — doubling R-value will cut heat loss in half"
    - "Inspect for and seal air leaks around plumbing penetrations, electrical boxes, and ductwork before adding insulation"
    - "Replace all fiberglass with closed-cell spray foam for maximum performance"
    - "Add a second vapor barrier beneath the existing batts"
  answer: 1
  explanation: "Air leaks allow warm air to bypass insulation entirely through convection. Doubling R-value in a leaky envelope produces diminishing returns — the heat escaping through gaps is unaffected by additional insulation on either side. Sealing penetrations first ensures the insulation you add (or already have) is actually doing its job. This is why building scientists say: 'seal, then insulate.'"

- question: "A wall is framed with 2x6 studs 16 inches on center and filled with R-19 fiberglass batts. Why does its real-world thermal performance fall significantly short of R-19?"
  type: multiple-choice
  options:
    - "Fiberglass batts degrade rapidly due to moisture and lose R-value within a few years"
    - "Wood studs conduct heat at roughly R-1 per inch and interrupt the insulation layer every 16 inches, reducing the effective R-value of the full wall assembly"
    - "R-19 is a nominal rating that only applies in laboratory conditions, not real installations"
    - "The vapor barrier on the batts blocks heat flow in the wrong direction during winter"
  answer: 1
  explanation: "Thermal bridging through framing members is the gap between rated and actual R-value. About 25% of a typical stud wall is wood framing, which conducts heat at ~R-1 per inch — far worse than R-3 per inch for fiberglass. In practice, a nominally R-19 wall may perform at R-14 or R-15 system-wide. The solution in high-performance construction is continuous exterior insulation that breaks the thermal bridge at each stud."

- question: "Sealing air leaks around plumbing penetrations and electrical boxes provides more energy savings in a leaky home than simply increasing the insulation's R-value."
  type: true-false
  answer: true
  explanation: "In a home with significant air leaks, warm conditioned air escapes through gaps regardless of the R-value of the insulation flanking those gaps. Air carries heat by convection, which bypasses insulation's resistance to conduction entirely. Air sealing addresses the actual escape route; adding more insulation leaves the escape route open. The practical test: an incense stick near penetrations on a windy day reveals leaks that visual inspection misses entirely."

- question: "Because spray foam creates such a tight building envelope, homes insulated with spray foam no longer need mechanical ventilation systems like HRVs or ERVs."
  type: true-false
  answer: false
  explanation: "This reverses the logic. Spray foam creates a tight envelope, which eliminates natural infiltration of fresh outdoor air — making mechanical ventilation MORE important, not less. Without it, indoor air quality deteriorates and moisture can accumulate, leading to mold. Heat Recovery Ventilators (HRVs) and Energy Recovery Ventilators (ERVs) provide controlled fresh-air exchange while recovering most of the energy from the outgoing air."

- question: "Explain why doubling the R-value of attic insulation in a home with significant air leaks might produce only modest reductions in energy bills."
  type: short-answer
  answer: "Insulation resists heat transfer by conduction through solid materials. Air leaks allow heat to escape by convection — warm air physically moving through gaps in the building envelope. Convection bypasses insulation entirely, so the insulation's R-value is irrelevant to that portion of heat loss. Doubling R-value reduces the conductive heat loss through the insulated assembly, but the convective loss through gaps remains unchanged. If a large fraction of total heat loss comes from air leakage, the savings from better insulation are proportionally small."
  explanation: "The key insight is that R-value only addresses one of the three heat transfer mechanisms (conduction). Air leaks exploit a completely different mechanism (convection) that insulation cannot address. A leaky envelope is like wearing a thick wool sweater with a large unzipped opening — the wool doesn't help where the gap is. Sealing the gap (air sealing) addresses the mechanism; adding more wool (higher R-value) does not."
```

## Explainer

From your study of attic ventilation and caulking, you understand two complementary strategies: managing how air moves through the building assembly and sealing the gaps that allow uncontrolled air movement. Insulation and air sealing are the systematic application of both strategies across the entire building envelope — the shell that separates conditioned interior space from the unconditioned outdoors. Getting this right is one of the highest-leverage improvements you can make to a home's energy performance.

The fundamental physics: heat moves from warm to cool by three mechanisms — conduction (through solid materials), convection (carried by moving air), and radiation. Insulation primarily resists conduction. But air leaks bypass insulation entirely through convection. If warm indoor air can find a path through gaps in the building envelope, it carries heat with it regardless of how much insulation is present on either side. This is why building scientists have a saying: "seal, then insulate." Sealing air leaks first ensures that the insulation you install is actually doing its job rather than being circumvented by drafts.

**R-value** is the standard measure of thermal resistance for insulation materials. Higher R-value means more resistance to heat flow. Fiberglass batts (the pink or yellow fluffy rolls) are the most familiar type: inexpensive, widely available, and rated roughly R-3 per inch. Their weakness is installation sensitivity — if they are compressed, cut short, or leave gaps at the edges, their effective R-value drops significantly. Blown-in **cellulose** (recycled newsprint treated with fire retardant) fills around obstructions and into irregular cavities that batts cannot reach cleanly, making it better for retrofitting older homes. **Closed-cell spray foam** is the premium option: it provides R-6 or more per inch *and* acts as an air barrier simultaneously, which is why it is particularly valuable at detail points like rim joists (the framing at the top of the foundation wall) where both insulation and air sealing are needed in a tight space.

**Thermal bridging** is the gap between rated R-value and real-world performance. Wood studs, which interrupt the insulation layer every 16 inches, conduct heat far better than the insulation between them — roughly R-1 per inch versus R-3 or more for the insulation. In a typical 2x6 framed wall (nominally R-19), about 25% of the wall area is framing, pulling the effective R-value down to around R-14 or 15. The solution in high-performance construction is **continuous exterior insulation** — a layer of rigid foam over the entire exterior of the wall — which eliminates the thermal breaks at each stud. For most existing homes, this is a major renovation, but it explains why "add more insulation to the walls" rarely delivers as much savings as expected without also addressing the framing.

Your math prerequisites apply directly to estimating insulation jobs. Area calculations tell you how many square feet of attic floor or wall cavity you need to cover; volume calculations help with blown-in estimates, where installers work from bags-per-square-foot at a given depth. Before calling an insulation contractor, doing this arithmetic yourself tells you whether the quote you receive is in the right order of magnitude.
