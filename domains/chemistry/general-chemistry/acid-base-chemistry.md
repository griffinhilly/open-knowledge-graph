---
id: acid-base-chemistry
title: Acid-Base Chemistry
domain: chemistry
course: general-chemistry
prerequisites:
- id: solution-concentration
  type: hard
- id: chemical-equilibrium
  type: soft
- id: logarithms-intro
  type: hard
- id: acid-base-neutralization-reactions
  type: soft
builds-toward:
- ph-and-acid-base-calculations
tags:
- Bronsted-Lowry
- Arrhenius
- Lewis-acid-base
- conjugate-pairs
- strong-acid
- weak-acid
- amphoteric
stage: formal-systems
status: validated
---
# Acid-Base Chemistry

## Core Idea
Acids are proton donors and bases are proton acceptors (Brønsted-Lowry definition), a more general framework than the Arrhenius model (acids produce H⁺, bases produce OH⁻ in water). Every acid-base reaction involves two conjugate pairs: acid₁/base₁ and acid₂/base₂. Strong acids (HCl, HNO₃, H₂SO₄, HClO₄, HBr, HI) ionize essentially completely in water, while weak acids establish equilibrium characterized by Ka. The Lewis definition — acid as electron-pair acceptor, base as electron-pair donor — further generalizes acid-base behavior to non-proton-transfer reactions.

## How It's Best Learned
Memorize the six common strong acids and strong bases, then focus deeply on weak acid/base equilibria. Identify conjugate pairs in any acid-base equation and practice predicting the direction of proton transfer (reaction favors the weaker acid and weaker base as products).

## Common Misconceptions
- Acid 'strength' refers to degree of ionization, not concentration — a weak acid can be very concentrated and a strong acid can be dilute.
- The conjugate base of a strong acid is an extremely weak base (negligible in water), while the conjugate base of a weak acid is a relatively stronger base.

## Questions

```yaml
- question: "A 1.0 M solution of acetic acid (Ka = 1.8 × 10⁻⁵) and a 0.001 M solution of HCl are compared. Which statement is correct?"
  type: multiple-choice
  options: ["HCl is the stronger acid because its solution is more concentrated", "Acetic acid is the stronger acid because its concentration is higher", "HCl is the stronger acid because it ionizes completely regardless of concentration", "They are equally strong because Ka and concentration balance out"]
  answer: 2
  explanation: "Acid strength refers to the degree of ionization, not concentration. HCl is a strong acid that ionizes essentially 100% in water regardless of how dilute it is. Acetic acid is a weak acid — it partially ionizes (Ka = 1.8 × 10⁻⁵ means very little dissociation). A dilute solution of HCl is still a stronger acid than a concentrated solution of acetic acid. These two concepts — strength and concentration — must be kept separate."

- question: "In the reaction CH₃COOH + H₂O ⇌ CH₃COO⁻ + H₃O⁺, water is acting as an acid."
  type: true-false
  answer: false
  explanation: "In this reaction, water accepts a proton from acetic acid, making water the Brønsted-Lowry base (proton acceptor), not the acid. Acetic acid (CH₃COOH) donates the proton, so it is the acid. Water is amphoteric — it can act as either an acid or a base depending on its reaction partner — but in this specific reaction it acts as the base."

- question: "HCl ionizes completely in water, producing Cl⁻ as its conjugate base. Why is Cl⁻ an extremely weak base?"
  type: short-answer
  answer: "Because Cl⁻ has almost no tendency to accept a proton from water. The stronger an acid, the weaker its conjugate base — since HCl is a very strong acid, it releases its proton very easily and has essentially no desire to reclaim it."
  explanation: "Conjugate acid-base strength is inversely related. A strong acid ionizes completely because the bond to H⁺ is weak — the conjugate base has little affinity for the proton. Cl⁻ is so stable after losing H⁺ that it essentially never recaptures one in aqueous solution, making it a negligible base. This is why HCl solutions don't revert to HCl once dissolved."
```

## Explainer

Before the Brønsted-Lowry model, the Arrhenius definition covered the basics: acids produce H⁺ in water, bases produce OH⁻. This works for many common reactions but fails for substances like ammonia (NH₃), which makes solutions basic without containing OH⁻. The Brønsted-Lowry framework extends the model by focusing on proton transfer: an acid is any proton donor, and a base is any proton acceptor. This definition works in any solvent, not just water, and correctly classifies NH₃ as a base because it accepts a proton from water to form NH₄⁺ and OH⁻.

Every Brønsted-Lowry acid-base reaction involves two conjugate pairs. When acetic acid (CH₃COOH) donates a proton to water, it becomes the acetate ion (CH₃COO⁻) — its conjugate base. Water, having accepted the proton, becomes hydronium (H₃O⁺) — water's conjugate acid. The four species form two pairs: CH₃COOH/CH₃COO⁻ and H₃O⁺/H₂O. Identifying conjugate pairs is a powerful analytical tool: it lets you predict the direction a reaction favors. Proton transfer proceeds toward the weaker acid and weaker base as products, meaning equilibrium lies on whichever side has the species with lower tendency to donate or accept protons.

The distinction between strong and weak acids is one of the most commonly confused concepts in chemistry. "Strong" and "weak" describe the degree of ionization — not the concentration of the solution and not its corrosiveness. A strong acid like HCl ionizes essentially completely: every molecule donates its proton to water. A weak acid like acetic acid reaches an equilibrium where most molecules remain un-ionized, characterized by the acid dissociation constant Ka. A small Ka (like 1.8 × 10⁻⁵ for acetic acid) means very little ionization. You can have a highly concentrated weak acid solution that is less acidic (higher pH) than a dilute strong acid — because what determines proton concentration is the product of concentration and ionization fraction, not concentration alone.

The Lewis definition extends acid-base chemistry further still: a Lewis acid accepts an electron pair, and a Lewis base donates one. This subsumes Brønsted-Lowry (a proton acceptor is an electron-pair donor to the proton) while covering reactions with no proton transfer at all, such as the reaction between BF₃ and NH₃. You will encounter Lewis acid-base theory frequently in organic chemistry, where carbocations and electrophiles act as Lewis acids. For now, the key insight is that the three frameworks (Arrhenius, Brønsted-Lowry, Lewis) are nested: each is more general than the previous one, and they do not contradict each other.

Because you have covered logarithms, you are ready to quantify these concepts. The pH scale — defined as −log[H⁺] — compresses the enormous range of proton concentrations into a manageable 0–14 range for aqueous solutions. Ka and pKa (= −log Ka) play the same role for acid strength. A lower pKa means a stronger acid (more ionization). When you begin calculating equilibrium concentrations and pH for weak acid solutions in the next topic, the conceptual framework here — conjugate pairs, Ka, degree of ionization — will provide the structure the math sits on.
