---
id: ellingham-diagrams-metal-extraction
title: Ellingham Diagrams and the Extraction of Metals
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: gibbs-free-energy-spontaneity
  type: hard
- id: entropy-and-gibbs-free-energy
  type: soft
- id: oxidation-reduction-reactions
  type: soft
- id: electrolytic-cells-and-electrolysis
  type: soft
builds-toward: []
tags:
- Ellingham diagram
- extractive metallurgy
- carbothermal reduction
- metal oxides
- free energy
stage: advanced
status: validated
---

# Ellingham Diagrams and the Extraction of Metals

## Core Idea
An Ellingham diagram plots the standard Gibbs energy of formation of metal oxides against temperature, with every reaction written per mole of O₂. Because ΔG° = ΔH° − TΔS°, each line is close to straight with slope −ΔS°. A metal can reduce the oxide of any metal whose line lies above its own at that temperature, and the line for carbon forming CO slopes downward, so carbon becomes a stronger reducing agent as temperature rises. The diagram explains why iron is smelted with carbon while aluminum is made by electrolysis.

## How It's Best Learned
Sketch three lines by hand: a typical metal oxide, C → CO₂, and C → CO, and work out each slope from the change in moles of gas. Then read crossings: where the C → CO line drops below a metal oxide line, carbon reduction of that oxide becomes favorable. Finish by placing real processes on the diagram, such as the thermite reaction, the blast furnace and the Hall–Héroult cell.

## Common Misconceptions
- A lower line means the metal reacts faster with oxygen. (The diagram is purely thermodynamic; it says which oxide is more stable, not how fast it forms.)
- All Ellingham lines slope upward. (Most metal oxide lines do, because gaseous O₂ is consumed, but 2C + O₂ → 2CO slopes downward because it makes two moles of gas from one.)
- If carbon cannot reduce an oxide at 1500 K, no chemical reductant can. (A metal whose line lies lower, such as aluminum or magnesium, can still reduce it, as in the thermite reaction.)

## Questions

```yaml
- question: "Why do most lines on an Ellingham diagram for metal oxides slope upward as temperature increases?"
  type: multiple-choice
  options: ["Because ΔH° becomes more negative at high temperature", "Because the reactions consume gaseous O₂, so ΔS° is negative and the slope (−ΔS°) is positive", "Because metal oxides melt at high temperature", "Because the equilibrium constant increases with temperature"]
  answer: 1
  explanation: "The slope of ΔG° against T is −ΔS°. Forming a solid oxide from a solid metal and O₂ gas removes gas, so ΔS° is negative and the line rises with temperature."
- question: "The line for 2C(s) + O₂(g) → 2CO(g) slopes downward, so carbon becomes a more effective reducing agent at higher temperatures."
  type: true-false
  answer: true
  explanation: "This reaction turns one mole of gas into two, so ΔS° is positive and ΔG° falls as T rises. At high enough temperature the CO line passes below many metal oxide lines, and carbon can then reduce those oxides."
- question: "At a given temperature, metal A can reduce the oxide of metal B under standard conditions when:"
  type: multiple-choice
  options: ["A's line lies above B's line", "A's line lies below B's line", "Both lines have the same slope", "B's line crosses ΔG° = 0"]
  answer: 1
  explanation: "Subtracting the two formation reactions gives the displacement reaction. Its ΔG° is the lower line minus the upper line, which is negative, so the metal with the lower line takes the oxygen."
- question: "Explain, using the Ellingham diagram, why aluminum is produced by electrolysis rather than by heating alumina with carbon."
  type: short-answer
  answer: "The Al₂O₃ line lies far below the carbon lines at practical furnace temperatures, so carbon reduction of alumina is not favorable there. Electrolysis of alumina dissolved in molten cryolite (the Hall–Héroult process) supplies the needed free energy electrically."
  explanation: "The diagram shows the free-energy gap directly. When no affordable chemical reductant lies below an oxide's line, an electrical driving force is used instead."
```

## Explainer

Most metals occur in nature as oxides, sulfides or other compounds, so making the metal means reducing it. The question is what can do the reducing and at what temperature. Harold Ellingham answered this in 1944 with a simple graph.

Write every oxide formation per mole of O₂, for example 2Ni + O₂ → 2NiO or 4/3 Al + O₂ → 2/3 Al₂O₃. Plot ΔG° for each against temperature. Since ΔG° = ΔH° − TΔS°, and ΔH° and ΔS° change only slowly with temperature, each line is nearly straight with slope −ΔS°. Most metal oxide lines slope upward because the reaction consumes a gas. A kink appears where the metal melts or boils, since the entropy change shifts at a phase transition.

The vertical position tells you oxide stability. The lower the line, the more negative ΔG°, and the more stable the oxide. Subtracting two lines gives a displacement reaction. If metal A has a lower line than metal B, then A can strip oxygen from B's oxide. Aluminum lies far below iron, which is why aluminum powder reduces iron(III) oxide in the strongly exothermic thermite reaction.

Carbon is the cheapest reductant, and its lines behave differently. The line for C + O₂ → CO₂ is nearly flat because the moles of gas do not change. The line for 2C + O₂ → 2CO slopes downward because one mole of gas becomes two. As temperature rises, this line cuts below the lines for oxides of iron, zinc and many other metals. Above each crossing, carbon or carbon monoxide can reduce that oxide. This is the thermodynamic basis of the blast furnace.

Some oxides lie so low that the carbon line would cross them only at impractically high temperatures. Aluminum and magnesium fall in this group. Titanium has a further problem: heated with carbon, it forms titanium carbide, so carbon cannot give the pure metal. For these metals, industry uses other routes. Aluminum is made by electrolysis of alumina dissolved in molten cryolite, the Hall–Héroult process. Titanium is made by the Kroll process, in which TiCl₄ is reduced with magnesium.

At the top of the diagram, a few lines, such as those for silver and mercury oxides, cross ΔG° = 0 at moderate temperatures. Above that point the oxide is unstable, so simply heating it releases the metal. Like all free-energy arguments, the diagram tells you what is possible, not how fast it happens.
