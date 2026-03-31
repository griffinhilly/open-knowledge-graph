---
id: ca-flatness
title: Flatness
domain: mathematics
course: commutative-algebra
prerequisites:
- id: ca-tensor-products
  type: hard
- id: ca-exact-sequences
  type: hard
- id: ca-localization
  type: soft
builds-toward:
- ca-going-up-going-down
- ca-completion
- ca-regular-sequences
tags:
- flat-module
- faithful-flatness
- flatness-criterion
- tor
- base-change
- going-down
stage: expert
status: validated
---

# Flatness

## Core Idea
An R-module M is flat if tensoring with M preserves exact sequences -- that is, M ⊗_R - is an exact functor. Flatness is weaker than freeness or projectivity but is the "right" condition for many purposes: flat base change preserves kernels, localizations are always flat, and flat morphisms in algebraic geometry correspond to families with continuously varying fibers. Faithful flatness (flat plus tensoring detects zero) is even more powerful, enabling descent arguments and guaranteeing the going down property for the associated ring map.

## Questions

```yaml
- question: "Which of the following R-modules is always flat?"
  type: multiple-choice
  options:
    - "R/I for any ideal I"
    - "Any localization S^{-1}R of R"
    - "The residue field R/m of a local ring (R, m)"
    - "Any finitely generated module over a non-field domain"
  answer: 1
  explanation: "Localization is always flat. The functor S^{-1}R ⊗_R - is naturally isomorphic to S^{-1}(-), which is exact because localization is exact. In contrast, R/I is generally not flat (tensoring with R/I kills I-torsion, which can destroy injectivity), and the residue field of a local ring is flat only if R is a field."

- question: "Over a PID, a module is flat if and only if it is torsion-free."
  type: true-false
  answer: true
  explanation: "This is a standard characterization. Over a PID, flat = torsion-free. The proof: flat implies torsion-free (if am = 0 with a ≠ 0, tensoring 0 → R →^a R with M gives 0 → M →^a M exact, so m = 0). Conversely, torsion-free modules over a PID are directed unions of free modules, hence flat (flatness is preserved under directed colimits)."

- question: "Let R → S be a flat ring homomorphism. Does going down hold for this map?"
  type: short-answer
  answer: "Yes. Flat ring maps always satisfy the going down property: if Q_1 in Spec S lies over P_1 in Spec R, and P_2 ⊆ P_1 is a prime of R, then there exists Q_2 ⊆ Q_1 lying over P_2."
  explanation: "This is a key theorem connecting flatness to prime ideal behavior. The proof uses the fact that flat base change preserves injectivity of maps, which forces the fiber over P_2 to be nonempty in Spec S_{Q_1}. This result is strictly more general than the going down theorem for integral extensions of integrally closed domains."

- question: "A module M over a local ring (R, m) is flat if and only if Tor_1^R(R/m, M) = 0."
  type: true-false
  answer: true
  explanation: "This is the local criterion for flatness. Over a local ring, flatness can be tested using a single Tor group -- Tor_1 with the residue field. The proof is a delicate induction argument using Nakayama's lemma and the long exact sequence of Tor. This criterion is far more practical than verifying exactness for all short exact sequences."

- question: "Explain the difference between flat and faithfully flat, and give an example of a flat module that is not faithfully flat."
  type: short-answer
  answer: "Flat means M ⊗_R - preserves exact sequences. Faithfully flat means additionally that M ⊗_R N = 0 implies N = 0 (equivalently, a sequence is exact iff it becomes exact after tensoring with M). Example: Q is flat over Z (it is torsion-free over a PID) but not faithfully flat, since Q ⊗_Z (Z/2Z) = 0 yet Z/2Z ≠ 0."
  explanation: "Faithful flatness adds the 'conservativity' condition: tensoring with M detects zero modules (and hence detects exactness). Localizations S^{-1}R are flat but faithfully flat only if every prime of R meets S or is 'seen' by the localization. Completion of a Noetherian local ring is faithfully flat, which is why properties can be checked after completing."
```

## Explainer

**Flatness** is one of the most important and subtle concepts in commutative algebra. An R-module M is **flat** if for every injective homomorphism of R-modules A → B, the induced map A ⊗_R M → B ⊗_R M is also injective. Equivalently, the functor M ⊗_R - is exact (it automatically preserves surjections and cokernels; flatness adds preservation of injectivity and kernels). Free modules are flat, projective modules are flat, and localizations S^{-1}R are flat over R. In general, flatness is strictly weaker than projectivity.

Over specific classes of rings, flatness has elegant characterizations. Over a PID, flat is equivalent to torsion-free. Over a local ring (R, m), the **local criterion for flatness** says M is flat if and only if Tor_1^R(R/m, M) = 0. Over a Noetherian local ring, a finitely generated module is flat if and only if it is free -- this dramatic simplification means flatness is most interesting for infinitely generated modules or for module-like objects (ring extensions). Lazard's theorem provides a general characterization: an R-module is flat if and only if it is a directed colimit of free modules.

The algebraic geometry of flat morphisms is central to modern scheme theory. A morphism of schemes f: X → Y is flat if O_{X,x} is flat over O_{Y,f(x)} for every point x. Flat morphisms are the algebraic analogue of "fiber bundles" or "smooth families" -- the fibers vary continuously (in an algebraic sense). Specifically, flat morphisms satisfy the **going down** property, preserve dimension of fibers, and interact well with base change. Localization, completion, and extension of scalars are all flat operations, which is why they preserve so many algebraic properties.

**Faithful flatness** adds a conservativity condition: M is **faithfully flat** if M is flat and M ⊗_R N = 0 implies N = 0. Equivalently, a sequence of R-modules is exact if and only if it becomes exact after tensoring with M. Faithful flatness enables **descent**: properties of modules (or algebras) over S can be descended to properties over R when R → S is faithfully flat. The completion of a Noetherian local ring is faithfully flat over the original ring, which is why the Cohen structure theorem for complete local rings has consequences for non-complete rings. Faithfully flat descent is one of the key technical tools in Grothendieck's approach to algebraic geometry.
