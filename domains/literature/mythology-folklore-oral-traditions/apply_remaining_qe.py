#!/usr/bin/env python3
"""Apply Q+E to remaining mythology files - Part 3."""

import os
import sys

os.chdir("C:/Users/griff/Projects/griffin/open-knowledge-graph/domains/literature/mythology-folklore-oral-traditions")

# Comprehensive mapping
CONTENT = {
    "fairy-tale-oral-literary-roots": ("""```yaml
- question: "Fairy tales emerge from oral folk traditions but differ from their oral origins because:"
  type: multiple-choice
  options:
    - "They were translated into different languages"
    - "They were collected, edited, and published as literature, modifying structure, morality, and content from oral versions"
    - "Oral fairy tales contained no magic or supernatural elements"
    - "Modern versions are identical to ancient oral versions"
  answer: 1
  explanation: "Literary publication transformed fairy tales. Oral versions were adapted for print audiences; morality was shifted; structure was standardized. The Grimm Brothers and Perrault edited tales they collected, creating the literary versions we know. Understanding fairy tales requires acknowledging this transformation from oral to literary."

- question: "In oral fairy tales, magic and supernatural reward typically function to:"
  type: multiple-choice
  options:
    - "Provide scientifically accurate explanations of natural phenomena"
    - "Illustrate reward for virtue and punishment for vice within the narrative logic"
    - "Entertain without any moral or pedagogical function"
    - "Obscure the tale's actual meaning"
  answer: 1
  explanation: "Oral fairy tales use magic to enforce moral outcomes. The virtuous are rewarded supernaturally; the wicked are punished. This magical enforcement of morality distinguishes fairy tales from realistic fiction and makes them pedagogical."

- question: "Fairy tales in their oral form and their published literary form are essentially identical narratives."
  type: true-false
  answer: false
  explanation: "Literary publication significantly modified oral tales. Editors shaped structure, emphasized morality, and altered content for print audiences. Published versions differ substantially from oral originals."

- question: "Magic and supernatural elements in fairy tales serve to reward virtue and punish vice within the narrative logic."
  type: true-false
  answer: true

- question: "Explain the significance of the transition from oral fairy tales to published literary versions. How did this transformation change the tales?"
  type: short-answer
  answer: "Oral tales were adapted for publication: structure was standardized, morality was made more explicit, content was modified for print audiences. Editors shaped the tales. This is why modern versions differ from oral originals. Understanding fairy tales requires recognizing that published versions are literary reconstructions, not unmediated transmissions."
  explanation: "Published fairy tales are artifacts of literary editing, reflecting publication-era values and editorial decisions."
```""", """## Explainer

Fairy tales emerge from oral folk traditions but the fairy tales we know are literary versions shaped by editing and publication. The Grimm Brothers collected and published German oral tales; Perrault published French tales. These published versions differ significantly from their oral origins.

Oral fairy tales are structured around magic and supernatural reward. Virtue is rewarded supernaturally; vice is punished. This magical enforcement of morality makes fairy tales pedagogical—teaching moral principles through narrative that transcends realistic causation.

Literary publication transformed oral tales. Editors standardized structure, emphasized moral lessons, modified content for print audiences, and removed elements considered inappropriate. Modern fairy tales are literary reconstructions, not unmediated folklore.

The distinction matters for analysis. Understanding fairy tales requires recognizing both their folk origins and their literary transformation."""),

    "flood-narrative-universal-pattern": ("""```yaml
- question: "Flood narratives appear across cultures, typically depicting:"
  type: multiple-choice
  options:
    - "Random violent weather with no cosmic significance"
    - "A deluge that destroys corrupt populations or restores cosmic order, with survivors repopulating the world"
    - "A purely geographical event with no mythological function"
    - "Identical narratives copied from a single source"
  answer: 1
  explanation: "Flood narratives depict cosmos-renewing cataclysm. A deluge eliminates corruption and allows renewal. This pattern appears across cultures, suggesting universal concerns about order/chaos or historical transmission. The narrative function is theological: the flood enacts cosmic reset."

- question: "The widespread appearance of flood narratives in geographically separated cultures suggests:"
  type: multiple-choice
  options:
    - "All cultures copied from a single original source"
    - "Flood narratives are meaningless and recur purely by coincidence"
    - "Universal concerns about destruction, renewal, and moral accountability"
    - "Modern floods are caused by ancient mythological events"
  answer: 2
  explanation: "Recurrence across separated cultures suggests universal concerns (all societies contend with water/chaos) or meaningful patterns in how cultures conceptualize renewal. This invites explanation, not proof of single origin."

- question: "Flood narratives universally depict moral judgment—the flood destroys the wicked and preserves the virtuous."
  type: true-false
  answer: false
  explanation: "Some flood narratives include moral dimensions; others depict purely cosmic processes. Moral judgment is not universal; variation reveals culturally specific emphases."

- question: "Flood narratives serve primarily to explain the geological origins of water and landforms."
  type: true-false
  answer: false
  explanation: "Flood narratives are primarily theological—enacting cosmic reset or struggle—not geological explanations."

- question: "Explain why flood narratives appear across numerous cultures and what this recurrence reveals about human concerns."
  type: short-answer
  answer: "Flood narratives depict cataclysmic destruction followed by renewal—a cosmos-reset mechanism. This pattern appears widely, suggesting universal concerns (all societies contend with water/chaos) or cultural transmission. The narrative function is theological: establishing that chaos can be overcome, corrupt orders destroyed and renewed, survival depends on virtue or selection. This reveals deep human concerns about cosmic order, moral accountability, and renewal possibility."
  explanation: "Recurrence is not proof of sameness but indication of shared concerns addressed through similar patterns."
```""", """## Explainer

Flood narratives appear worldwide: Mesopotamian (Gilgamesh), Hebrew (Noah), Hindu (Matsya), Greek (Deucalion), Indigenous traditions. These depict a deluge destroying the existing world, eliminating corruption or restoring cosmic order, with a remnant surviving to repopulate.

**The flood functions as a cosmic reset mechanism.** It establishes that chaos (overwhelming water) can be contained, corrupt orders destroyed, and renewal is possible. This is not merely environmental disaster but cosmos-altering event—one world ending, another beginning.

**Flood narratives often incorporate moral dimensions.** Some depict the flood as punishment for wickedness; others as natural cosmic renewal. These variations reveal culturally specific emphases on divine justice or human moral responsibility.

**Universal recurrence suggests either shared human concerns or cultural transmission.** All societies contend with water and catastrophic flooding. Flood narratives express universal concerns about destruction and survival. Alternatively, patterns may have spread through contact. The key is meaningful recurrence, inviting explanation of why cultures structure renewal through flood."""),
}

processed = 0
for file_id, (questions, explainer) in CONTENT.items():
    fname = f"{file_id}.md"
    if not os.path.exists(fname):
        print(f"NOTFOUND: {fname}")
        continue

    content = open(fname, 'r', encoding='utf-8').read()
    if '## Questions' in content:
        print(f"SKIP: {file_id} (already has Questions)")
        continue

    new_content = content.rstrip() + f"\n\n## Questions\n\n{questions}\n\n## Explainer\n\n{explainer}\n"
    open(fname, 'w', encoding='utf-8').write(new_content)
    processed += 1
    print(f"DONE: {file_id}")

print(f"\nApplied Q+E to {processed} files")
