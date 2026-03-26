---
id: ionization-energy-and-electron-removal
title: Ionization Energy
domain: chemistry
course: general-chemistry
prerequisites:
- id: periodic-trends
  type: hard
- id: electron-configuration
  type: soft
builds-toward:
- ion-formation
- electronegativity
tags:
- ionization energy
- periodic trends
- cations
stage: formal-systems
status: validated
---

# Ionization Energy

## Core Idea
Ionization energy is the minimum energy needed to remove an electron from a gaseous atom. It increases across a period and decreases down a group, reflecting nuclear charge and electron shielding.

## Questions

```yaml
- question: "Oxygen (Group 16) has a slightly lower first ionization energy than nitrogen (Group 15), despite being further right in the same period. What is the best explanation?"
  type: multiple-choice
  options:
    - "Oxygen has more inner-shell electrons that shield its valence electrons more effectively than nitrogen's"
    - "Nitrogen's half-filled 2p subshell (three unpaired electrons) is unusually stable; oxygen's 2p has one paired electron whose electron-electron repulsion makes that electron easier to remove"
    - "Oxygen's additional proton reduces effective nuclear charge by attracting inner electrons more strongly"
    - "The 2p electrons in oxygen are in a lower-energy orbital than those in nitrogen, requiring less energy to remove"
  answer: 1
  explanation: "Nitrogen has the electron configuration [He] 2s² 2p³ — three 2p electrons, one per orbital, all unpaired. No electron-electron repulsion occurs within the 2p subshell. Oxygen has [He] 2s² 2p⁴ — one 2p orbital must hold a pair. The repulsion between paired electrons in that orbital makes one of them easier to remove than any of nitrogen's unpaired 2p electrons, despite oxygen's higher nuclear charge. This is the Group 15–16 exception — one of two systematic dips in the otherwise rising IE trend across a period."

- question: "Moving down Group 1 from Li to Cs, first ionization energy decreases even though nuclear charge increases substantially. Which factor is responsible?"
  type: multiple-choice
  options:
    - "The nucleus becomes less stable with more protons, weakening the nuclear force on outer electrons"
    - "Each successive period adds a new electron shell, placing the valence electron farther from the nucleus and behind more inner-electron shielding — these effects outweigh the increase in nuclear charge"
    - "Each Group 1 element has fewer total electrons than the previous one, reducing the nuclear attraction"
    - "The s orbital becomes more stable with increasing nuclear charge, paradoxically reducing ionization energy"
  answer: 1
  explanation: "Going down Group 1, nuclear charge increases, which would increase ionization energy in isolation. But each new period adds an entire new electron shell. The valence electron sits farther from the nucleus and behind a larger number of inner-shell electrons that shield it from the nuclear charge. Both the increased distance (the force weakens as 1/r²) and the increased shielding reduce the effective nuclear charge experienced by the outermost electron. The shielding and distance effects dominate, so ionization energy falls from Li to Cs."

- question: "Boron (Group 13) has a lower first ionization energy than beryllium (Group 2), even though boron has one more proton."
  type: true-false
  answer: true
  explanation: "Beryllium's outermost electron is in a 2s orbital. Boron's outermost electron is in a 2p orbital, which is higher in energy and has less penetration toward the nucleus than 2s. Even though boron has one more proton (higher Z), the electron being removed is in a less-stable, more-shielded orbital, making it easier to remove. This is the Group 2–13 exception — one of two systematic dips in the period trend."

- question: "Ionization energy increases smoothly and without exception from left to right across nearly every period of the periodic table."
  type: true-false
  answer: false
  explanation: "There are two notable dips in the otherwise rising trend across each period: (1) IE drops from Group 2 to Group 13 because the Group 13 element loses a p electron (higher energy than the s electron lost from Group 2); (2) IE drops from Group 15 to Group 16 because the Group 16 element's 2p subshell has a paired electron with added repulsion, making it easier to remove. These exceptions are not random — they reflect subshell structure and are reproducible across periods."

- question: "Explain why sodium (Na) has a much lower first ionization energy than chlorine (Cl), even though both are in period 3."
  type: short-answer
  answer: "Both Na and Cl have their valence electrons in the n = 3 shell, but effective nuclear charge (Z_eff) differs dramatically. As protons are added from Na (Z = 11) to Cl (Z = 17) across period 3, electrons are added to the same 3s and 3p subshells. Electrons in the same shell shield each other poorly, so Z_eff rises steadily across the period. Na's single 3s electron experiences a Z_eff of roughly 2.5; Cl's 3p electrons experience a Z_eff of roughly 6. Cl's valence electrons feel far greater nuclear pull and require much more energy to remove."
  explanation: "This also explains why Na readily forms Na+ cations while Cl tends not to lose electrons. The periodic trend in ionization energy directly predicts electronegativity, reactivity, and ion formation tendencies. The same underlying logic — effective nuclear charge and electron shielding — governs all of these properties simultaneously."
```

## Explainer

From your study of periodic trends and electron configuration, you know that electrons occupy specific energy levels around the nucleus and that the number of protons increases steadily across a period. **Ionization energy** (IE) puts a number on how tightly an atom holds its outermost electron — specifically, it is the minimum energy required to completely remove that electron from a gaseous atom in its ground state. The atom starts neutral and ends as a cation with a +1 charge. This is always an endothermic process: you must supply energy to pull an electron away from the attractive force of the nucleus.

The trend across a period is straightforward once you think about it in terms of **effective nuclear charge** (Z_eff). As you move from left to right across a period, protons are added to the nucleus and electrons are added to the *same* shell. Electrons in the same shell are poor at shielding each other from the nucleus, so Z_eff increases steadily. The outermost electron feels a stronger pull, and it takes more energy to remove it — ionization energy rises. Sodium (first element of period 3) has a low ionization energy because its single valence electron is loosely held; argon (end of period 3) has a high ionization energy because its valence electrons experience much greater effective nuclear charge.

Moving down a group, ionization energy *decreases* even though the nuclear charge increases. The reason is that each new period adds a whole new electron shell, placing the outermost electron farther from the nucleus and behind more layers of inner-electron shielding. The increased distance and shielding outweigh the extra protons, so the outermost electron is easier to remove. This is why cesium, at the bottom of Group 1, has one of the lowest ionization energies of any element — its valence electron is far from the nucleus and heavily shielded.

Two notable exceptions disrupt the smooth trend across a period. First, Group 13 elements (like B, Al) have slightly *lower* ionization energy than the preceding Group 2 elements (Be, Mg), because the electron being removed from Group 13 is in a higher-energy p subshell rather than an s subshell — it is easier to remove. Second, Group 16 elements (like O, S) have slightly lower ionization energy than Group 15 (N, P), because in Group 16 one p orbital contains a *paired* electron, and electron-electron repulsion within that orbital makes it easier to remove. These dips are not random — they reflect the subshell structure you learned in electron configurations and reinforce that ionization energy is ultimately governed by how strongly the nucleus grips each specific electron.
