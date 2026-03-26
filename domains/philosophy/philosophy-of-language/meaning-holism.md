---
id: meaning-holism
title: Meaning Holism
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: meaning-and-reference-basics
  type: hard
- id: compositionality-principle
  type: soft
- id: philosophy-of-language-intro
  type: soft
- id: rule-following-and-meaning
  type: soft
- id: meaning-convention-vs-intention
  type: soft
builds-toward:
- semantic-content-externalism
tags:
- holism
- semantics
- meaning
- interconnection
stage: formal-systems
status: validated
---
# Meaning Holism

## Core Idea
Meaning holism claims that the meaning of a term is determined by its entire network of relationships within a conceptual scheme, not by isolated definitions or references. No word can be fully understood in isolation; to grasp "electron" requires understanding physics, mathematics, and empirical methods. This challenges compositional semantics and raises questions about meaning change and concept individuation.

## How It's Best Learned
Start with cases where changing peripheral beliefs seems to change a word's meaning: if physics discovered electrons weren't fundamental, would "electron" refer to something else? Develop holism gradually from atomism, examining how meaning depends on conceptual roles. Then consider the regress: if meanings require whole systems, can we ever learn new words? Study responses like molecularism (only core beliefs determine meaning) that seek middle ground.

## Common Misconceptions
- Thinking holism makes meaning indeterminate; it's determinate relative to the whole system.
- Assuming holism contradicts compositionality; they conflict but holists can accommodate some compositional structure.
- Overlooking that holism was developed to explain language understanding, not just reference.

## Questions

```yaml
- question: "Scientists discover that electrons behave in ways radically different from everything previously believed — the entire theoretical picture is overturned. A meaning holist and a meaning atomist would interpret this differently. Which describes the holist position?"
  type: multiple-choice
  options:
    - "The meaning of 'electron' is fixed by its reference to the same particles; only our beliefs changed, not the meaning"
    - "The meaning of 'electron' changed, but only if physicists issued a formal redefinition"
    - "Since the term's inferential connections — its role in theory, links to other concepts, ties to observation — have substantially changed, the meaning of 'electron' has partially changed; meaning and belief revision cannot be cleanly separated"
    - "Holism is silent on this case because it only applies to non-scientific language"
  answer: 2
  explanation: "The holist holds that meaning is constituted by inferential role — the web of connections a term has to other terms, theories, and observations. Change enough of those connections (as a radical revision of physics would) and you have changed the meaning. The atomist, by contrast, holds that meaning is anchored by direct reference or analytic definition, so belief change doesn't touch meaning. This difference has real consequences: the holist must explain how communication survives theory change; the atomist must explain how purely referential or definitional meaning can account for the conceptual depth of scientific terms."

- question: "What is the 'incommensurability' problem that meaning holism creates for inter-theoretic communication?"
  type: multiple-choice
  options:
    - "Two scientists speaking different languages cannot translate their results without a common formal language"
    - "If a term's meaning depends on each speaker's entire web of beliefs, then two scientists with different theoretical commitments may mean slightly different things by the same term, making full translation and genuine shared understanding uncertain"
    - "Holism implies that scientific theories in different domains cannot make contact with each other"
    - "Incommensurability means that older theories are simply false rather than partly correct"
  answer: 1
  explanation: "If 'electron' means something slightly different to a classical physicist and a quantum physicist — because their surrounding belief-webs differ — then they are, in a strict holistic sense, not talking about exactly the same thing. This threatens the idea of scientific progress as accumulation and raises puzzles about how scientists across different theoretical generations can learn from one another. Kuhn and Feyerabend used incommensurability to argue that paradigm shifts are not purely rational; holism provides one semantic foundation for that claim."

- question: "Meaning holism implies there is no sharp boundary between changing what a word means and changing one's beliefs about the thing the word refers to."
  type: true-false
  answer: true
  explanation: "This is Quine's central argument in 'Two Dogmas of Empiricism.' If meaning is constituted by inferential role in a web of beliefs, then there is no principled distinction between analytic truths (true by meaning alone) and synthetic truths (true by the world). Any statement can be held true in the face of contrary evidence by revising surrounding beliefs instead. Conversely, any belief change ripples through the web and potentially shifts meanings. The analytic/synthetic distinction — and with it, the clean separation of meaning-change from belief-change — dissolves."

- question: "Meaning holism is logically incompatible with the compositionality principle — if holism is true, sentences can rarely have meanings composed from the meanings of their parts."
  type: true-false
  answer: false
  explanation: "Holism and compositionality are in tension but are not strictly incompatible. Compositionality says the meaning of a complex expression is determined by the meanings of its parts plus their mode of combination. Holism says the meaning of each part is determined by its role in the entire web. These two claims conflict in various ways — if parts' meanings are holistically sensitive, composing them becomes complicated — but philosophers like Dummett have explored molecularist positions that preserve compositionality for core inferential commitments while acknowledging holistic pressures. The incompatibility is not a logical consequence but a practical challenge requiring careful accommodation."

- question: "Explain why Quine's holism implies there is no principled distinction between analytic truths (true by meaning alone) and synthetic truths (true by the world)."
  type: short-answer
  answer: "Quine argued that our beliefs form a web in which individual statements do not face experience one by one but as a corporate body. When experience conflicts with our beliefs, we can revise any part of the web — including what we took to be definitional truths. For example, if empirical results seemed to violate the law of excluded middle, we might revise it rather than abandon the empirical data (as some have argued in quantum mechanics). This means no statement is immune from revision on empirical grounds, so none is 'true by meaning alone' in a way that insulates it from the world. The analytic/synthetic distinction requires that some truths are fixed by meanings regardless of experience — but holism says all truths are revisable given sufficient pressure from the total web."
  explanation: "The classic analytic truth is 'All bachelors are unmarried.' Quine would say: in principle, if radical enough reasons arose, we could revise even this by changing what we mean by 'bachelor' or revising surrounding logical principles. The revision is always possible; what varies is its cost in terms of further adjustments to the web."
```

## Explainer

You've studied the relationship between meaning and reference — how words connect to the world — and you've seen the compositionality principle: the meaning of a complex expression is determined by the meanings of its parts and how they're combined. Meaning holism challenges a deeper assumption that both of those ideas often carry: that individual words or expressions have meanings that are, in some important sense, self-contained. Holism says this is wrong. The meaning of a term is not an isolated package — it is constituted by its entire network of relations to other terms and beliefs within a conceptual system.

The best entry point is through belief revision. Suppose you know what "electron" means, and then particle physicists overturn their understanding of electron behavior. Did the meaning of "electron" change, or did your beliefs about electrons change while the meaning stayed fixed? **Meaning atomism** says meanings are fixed by direct reference or by analytic definitions, so belief change doesn't touch meaning. But holism says meaning is partly constituted by the inferential roles a term plays — its connections to other terms, its role in theories, its links to observation. Change enough of those connections, and you have changed the meaning. This is why Quine argued that there's no sharp distinction between **analytic** truths (true by meaning alone) and **synthetic** truths (true by the world): any statement can be revised in response to recalcitrant experience if we're willing to revise enough surrounding beliefs.

The holism picture is compelling but creates a serious puzzle about language learning and communication. If the meaning of "electron" depends on everything else in a physicist's conceptual scheme, how do two physicists with slightly different theoretical commitments ever manage to communicate successfully? They presumably mean slightly different things by "electron" — their terms are **incommensurable** to some degree. Worse, how does anyone ever *learn* a new word? You can't learn "electron" one term at a time if its meaning requires the whole of physics. Holism seems to make language acquisition and translation deeply mysterious.

Responses to these problems have generated a spectrum of positions. **Molecularism** (associated with Michael Dummett) holds that only a *core* cluster of beliefs — the most fundamental inferential commitments — determine meaning, not the entire web. This preserves much of holism's insight while making translation and learning tractable. **Two-factor theories** distinguish a narrow semantic content (roughly, reference) from a wide conceptual role (the inferential web), allowing two speakers to share the referential component while differing in the holistic conceptual component. The debate between these positions shapes how philosophers and cognitive scientists think about concept individuation, language change, and what it means for two people to really be talking about the same thing.
