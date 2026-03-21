---
id: periodic-trends-and-properties
title: 'Periodic Table Trends: Atomic Radius, Ionization Energy, and Electronegativity'
domain: chemistry
course: general-chemistry
prerequisites:
- id: electron-configuration-principles
  type: hard
builds-toward:
- ionic-bonding-formation
- covalent-bonding-formation
- bond-classification
tags:
- periodic trends
- periodic table
- atomic radius
- ionization energy
- electronegativity
stage: advanced
status: draft
---

# Periodic Table Trends: Atomic Radius, Ionization Energy, and Electronegativity

## Core Idea
Properties of elements follow periodic patterns due to electron configuration. Atomic radius decreases across a period and increases down a group. Ionization energy increases across a period and decreases down a group. Electronegativity measures how strongly an atom attracts electrons in a bond. These trends explain reactivity and bonding behavior.

## Questions

```yaml
- question: "Chlorine (Cl, period 3, group 17) and sodium (Na, period 3, group 1) are in the same period. A student claims chlorine must be larger because it has more electrons. What is actually true?"
  type: multiple-choice
  options:
    - "The student is correct — more electrons always means a larger electron cloud"
    - "Chlorine is smaller because across a period, nuclear charge increases while electrons enter the same shell without effectively shielding each other, pulling the valence electrons closer"
    - "They are approximately the same size because they share the same principal quantum number for their valence shell"
    - "Sodium is larger because metal atoms are always bigger than nonmetal atoms due to their loosely held electrons"
  answer: 1
  explanation: "This is the most counterintuitive aspect of atomic radius trends. Across a period, you add both electrons AND protons. The new electrons enter the same valence shell and do not effectively shield each other from the nucleus. The growing nuclear charge therefore pulls all valence electrons progressively closer, shrinking the atom. Chlorine (Z=17) has a much smaller atomic radius than sodium (Z=11) despite having more electrons. Option D contains a real pattern (metals tend to be larger) but gives the wrong reason and doesn't explain the within-period trend."

- question: "Potassium (K, period 4, group 1) has a much lower first ionization energy than chlorine (Cl, period 3, group 17), even though potassium has more protons. What best explains this?"
  type: multiple-choice
  options:
    - "Potassium has more electrons that repel each other, weakening the nuclear hold on the outermost electron"
    - "Potassium's valence electron sits in the fourth shell, far from the nucleus and shielded by three complete inner shells, so the effective nuclear charge it experiences is low"
    - "Chlorine's ionization energy is inflated because nonmetals are inherently reluctant to lose electrons regardless of nuclear charge"
    - "Potassium is a more reactive metal, and high reactivity always corresponds to low ionization energy by definition"
  answer: 1
  explanation: "Moving down a group adds entire electron shells, and each new inner shell substantially shields the outer electron from the nucleus. Potassium's 4s valence electron is shielded by three complete inner shells (n=1, 2, 3) and sits far from the nucleus — so despite having 19 protons, the effective nuclear charge experienced by that electron is low. Chlorine's valence electrons in n=3 experience a much higher effective nuclear charge (17 protons, less shielding) and are held much more tightly. Option D is circular reasoning, not an explanation."

- question: "Atomic radius decreases as you move left to right across a period, even though the total number of electrons in the atom increases."
  type: true-false
  answer: true
  explanation: "True — and this is the key counterintuitive insight. Across a period, electrons are added to the same valence shell, where they do not effectively shield each other from the nucleus. Simultaneously, each step adds another proton, increasing nuclear charge. The net effect is that the growing nuclear charge pulls all valence electrons progressively tighter, shrinking the atom. Adding electrons to the same shell does not compensate for the increasing nuclear pull."

- question: "Electronegativity and ionization energy follow opposite trends across the periodic table — when one increases, the other decreases."
  type: true-false
  answer: false
  explanation: "False — both electronegativity and ionization energy increase across a period and decrease down a group. Both reflect how tightly an atom holds onto electrons: higher effective nuclear charge means electrons are both harder to remove (high IE) and more strongly attracted in bonding (high electronegativity). The property that follows the opposite trend from IE and electronegativity is atomic radius, which decreases across a period and increases down a group."

- question: "Explain in terms of nuclear charge and electron shielding why atomic radius decreases across a period but increases down a group."
  type: short-answer
  answer: "Across a period: proton number increases while new electrons enter the same valence shell and do not effectively shield each other from the nucleus. The increasing nuclear charge pulls all valence electrons progressively closer, shrinking the atom. Down a group: each new row adds a complete inner electron shell farther from the nucleus. These inner shells provide substantial shielding that partially offsets the increased nuclear charge, so the outermost electron experiences a lower effective nuclear charge and sits farther from the nucleus — the atom expands."
  explanation: "The unified explanation is effective nuclear charge (Z_eff = Z − shielding). Across a period, Z increases and shielding stays roughly constant → Z_eff rises → radius shrinks. Down a group, Z increases but new complete shells add shielding that outpaces the nuclear charge increase → Z_eff stays roughly constant or rises slowly → radius grows because each new shell is inherently farther from the nucleus."
```

## Explainer

Now that you understand electron configurations, you can see why the periodic table is periodic: elements in the same column have the same number of valence electrons, and it is the valence electrons that determine chemical behavior. But the periodic table also encodes smooth trends in physical properties across rows and down columns, all driven by two competing forces — the increasing positive charge of the nucleus (more protons) and the shielding effect of inner electron shells.

**Atomic radius** decreases as you move left to right across a period. This seems counterintuitive — you are adding more electrons, so shouldn't the atom get bigger? No, because you are also adding more protons. Across a period, electrons enter the same shell and do not effectively shield each other from the growing nuclear charge. Each additional proton pulls all the valence electrons a little closer, shrinking the atom. Moving down a group, however, each new row adds an entire electron shell farther from the nucleus. The additional shielding from inner shells outweighs the increased nuclear charge, so atoms get larger. Potassium is much bigger than lithium even though it has more protons, because its valence electron sits in the fourth shell, far from the nucleus and well shielded by three inner shells.

**Ionization energy (IE)** — the energy required to remove the outermost electron — follows the opposite trend across a period: it increases from left to right because the shrinking atomic radius means the valence electron is held more tightly. It takes much more energy to pull an electron off fluorine than off sodium. Down a group, ionization energy decreases because the outermost electron is farther from the nucleus and more shielded. There are minor exceptions to the smooth increase across a period — IE dips slightly from group 2 to group 3 (because the new electron enters a higher-energy p sublevel) and from group 5 to group 6 (because the new electron must pair up in an already-occupied p orbital, suffering extra repulsion). These dips reinforce that the trend is driven by electron configuration details, not just atomic number.

**Electronegativity** measures how strongly an atom attracts shared electrons in a chemical bond, and it follows the same pattern as ionization energy: increasing across a period and decreasing down a group. Fluorine, in the upper right corner, is the most electronegative element. This makes intuitive sense: a small atom with high nuclear charge and a nearly full valence shell pulls hard on bonding electrons. Noble gases are typically excluded from electronegativity scales because they rarely form bonds. Together, these three trends — atomic radius, ionization energy, and electronegativity — form a coherent picture: moving across a period, atoms become smaller, harder to ionize, and more electron-hungry, all because of increasing effective nuclear charge. Moving down a group, the opposite occurs as distance and shielding weaken the nucleus's grip. These trends will directly predict how elements bond when you study ionic and covalent bonding next.
