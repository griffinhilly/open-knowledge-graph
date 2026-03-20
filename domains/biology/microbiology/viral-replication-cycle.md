---
id: viral-replication-cycle
title: Viral Replication Cycle
domain: biology
course: microbiology
prerequisites:
  - id: dna-structure
    type: hard
  - id: dna-replication
    type: hard
builds-toward:
  - host-pathogen-interactions
  - emerging-infectious-diseases
tags: [virus, lytic-cycle, lysogenic-cycle, bacteriophage, replication, assembly]
stage: advanced
status: validated
---

# Viral Replication Cycle

## Core Idea
Viruses are obligate intracellular parasites — they cannot reproduce independently and must hijack a host cell's machinery. The replication cycle follows a sequence: attachment (virus binds to specific host cell receptors), penetration (viral genome enters the cell), replication (host machinery copies viral nucleic acid and synthesizes viral proteins), assembly (new viral particles are constructed), and release (virions exit the cell, often by lysis). Bacteriophages — viruses that infect bacteria — demonstrate two distinct strategies: the lytic cycle (immediate replication and host cell destruction) and the lysogenic cycle (viral DNA integrates into the host genome as a prophage, replicating passively with each cell division until triggered to enter the lytic cycle). RNA viruses like influenza and retroviruses like HIV add additional complexity through reverse transcriptase and error-prone replication that drives rapid mutation.

## How It's Best Learned
Use bacteriophages as the model system — they're simpler and illustrate both lytic and lysogenic pathways cleanly. Animated step-by-step diagrams of each stage are essential because the process is sequential and spatial. Compare the two cycles side by side, emphasizing the "decision point" where a phage enters lysis vs. lysogeny. Then extend to animal viruses (influenza for RNA viruses, HIV for retroviruses) to show variations. Connect receptor specificity to host range — why can't you catch a plant virus? Because the attachment step fails.

## Common Misconceptions
- Thinking viruses are alive — they lack metabolism and cannot reproduce outside a host cell, placing them at the boundary of life.
- Confusing the lysogenic cycle with latency in animal viruses — similar concept but different mechanisms.
- Assuming all viruses lyse their host cell — some exit by budding, and lysogenic viruses can persist indefinitely without killing the host.
- Believing viral mutations are intentional adaptations — they result from replication errors, and most are neutral or harmful to the virus.

## Questions

```yaml
- question: "During the lysogenic cycle in a bacteriophage infection, what happens to the viral genome immediately after it enters the host cell?"
  type: multiple-choice
  options: ["It is immediately replicated and new virions are assembled", "It integrates into the host chromosome as a prophage and replicates passively with cell division", "It remains in the cytoplasm as an autonomous episome", "It is degraded by host restriction enzymes"]
  answer: 1
  explanation: "In the lysogenic cycle, the phage genome integrates into the bacterial chromosome as a prophage. It then replicates silently with every cell division — the host does all the work. The phage can persist this way for many generations until an inducing signal (such as UV damage) triggers excision and entry into the lytic cycle. Options A describes the lytic cycle, C is incorrect (integration into the chromosome is the defining feature), and D would prevent lysogeny from occurring."

- question: "All viruses must kill their host cell as part of their replication cycle in order to release new virions."
  type: true-false
  answer: false
  explanation: "Lysis is only one release mechanism. Many enveloped viruses (including HIV and influenza) exit by budding — the virus acquires a membrane envelope as it pushes through the host cell membrane, and the host cell survives the process, at least initially. Lysogenic phages can persist indefinitely in the host chromosome without killing the cell at all. Killing the host is the lytic strategy, not a universal feature of viral replication."

- question: "Why can a human virus not infect a plant cell, even if the viral particles were artificially injected directly into the plant's cytoplasm?"
  type: short-answer
  answer: "Attachment depends on specific receptor-ligand binding between viral surface proteins and host cell receptors. Plant cells lack the receptors that human viruses recognize, so the attachment step fails. However, if particles were injected past this step, replication might partly proceed — the deeper constraint is that the host replication machinery must also be compatible."
  explanation: "Receptor specificity is the primary determinant of host range and tissue tropism. This is why HIV only infects cells expressing CD4 receptors, why influenza targets cells with specific sialic acid residues, and why most viruses cannot cross species barriers without mutations to their attachment proteins. The injection caveat is important for teaching: if you bypassed attachment, some replication factors might work, but viruses are also adapted to exploit species-specific cellular machinery throughout the replication cycle."
```

## Explainer

Viruses are not cells, do not metabolize, and cannot reproduce on their own — they are genetic parasites that commandeer the machinery of living cells. Understanding their replication cycle means following the viral genome from outside the cell to the production of hundreds of new copies, and then back outside again. The sequence is the same across nearly all viruses: attach, enter, replicate, assemble, release.

Attachment is not random. Viral surface proteins (capsid proteins or glycoproteins in enveloped viruses) bind with high specificity to particular receptor molecules on the host cell surface. This specificity is the entire explanation for host range and tissue tropism: HIV infects only cells with CD4 receptors (T-helper cells and macrophages), influenza targets cells with certain sialic acid residues on the airway epithelium, and no human virus infects plants because none of their attachment proteins recognize plant cell receptors. After attachment, the viral genome enters the cell — either the whole virus is engulfed, or (in many phages) the capsid stays outside and only the nucleic acid is injected. Inside, the host's ribosomes, polymerases, and energy systems are exploited to transcribe viral genes and replicate the viral genome. New capsid proteins are made, assembled around new copies of the genome, and packaged into progeny virions.

Release varies. Non-enveloped viruses typically lyse the cell — they build up until the membrane ruptures, releasing hundreds to thousands of virions at once and killing the host cell. Enveloped viruses often bud out gradually, wrapping themselves in a piece of the host membrane as they exit; the cell may survive for a time. This distinction matters clinically: lytic infections tend to cause acute, destructive disease, while budding infections can be persistent.

Bacteriophages demonstrate an additional strategy that has no direct parallel in simple lytic infections: the lysogenic cycle. After entering the bacterial cell, some phages integrate their DNA into the host chromosome as a prophage. The host cell divides normally, copying the prophage along with its own genome — the virus gets replicated for free, without the cost of making new virions. The prophage is essentially invisible. But under stress — DNA damage, nutrient deprivation — the prophage excises itself, enters the lytic cycle, makes hundreds of copies, and lyses the cell. This is a bet-hedging strategy: persist harmlessly when the host is healthy, but switch to rapid replication and dispersal when the host is doomed anyway.

RNA viruses add a layer of complexity your knowledge of DNA replication doesn't fully cover. RNA polymerases lack the proofreading mechanisms of DNA polymerases, so RNA viruses mutate at rates 10,000 to 1,000,000 times higher than DNA viruses. Most mutations are harmful or neutral, but the sheer volume means rare beneficial mutations (such as those that improve receptor binding or evade antibodies) appear rapidly. This is why influenza requires a new vaccine each year and why SARS-CoV-2 generated successive variants. Retroviruses like HIV go further: they use reverse transcriptase to convert their RNA genome into DNA before integration, exploiting the host's DNA replication machinery while still benefiting from the mutation rate of RNA replication during the early stages.
