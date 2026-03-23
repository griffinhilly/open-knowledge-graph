---
id: gastric-secretion-digestion-physiology
title: Gastric Secretion and Digestion Physiology
domain: biology
course: physiology
prerequisites:
- id: gastric-parietal-cell-secretion
  type: hard
- id: gut-motility-and-secretion
  type: soft
builds-toward:
- gastrointestinal-secretion-motility
- nutrient-digestion-absorption
tags:
- gastric
- secretion
- acid
- pepsin
- digestion
stage: formal-systems
status: validated
---

# Gastric Secretion and Digestion Physiology

## Core Idea
Gastric parietal cells secrete hydrochloric acid and intrinsic factor; chief cells secrete pepsinogen. Acid activates pepsinogen to pepsin, which initiates protein digestion. Gastric motility churns food into a liquid bolus (chyme) for controlled release into the small intestine. Hormonal and neural signals coordinate acid secretion and motility in response to meal composition, preventing reflux and optimizing digestion.

## Questions

```yaml
- question: "A patient regularly takes ibuprofen (an NSAID that inhibits prostaglandin synthesis) for chronic pain and develops a gastric ulcer. The most likely mechanism is:"
  type: multiple-choice
  options:
    - "Decreased gastric acid production, because prostaglandins are required for parietal cell activation"
    - "Impaired mucosal barrier — prostaglandins normally stimulate mucus and bicarbonate secretion and maintain mucosal blood flow"
    - "Delayed gastric emptying, because prostaglandins control pyloric sphincter relaxation"
    - "Excessive pepsin activity, because prostaglandins normally inhibit chief cell pepsinogen secretion"
  answer: 1
  explanation: "Prostaglandins protect the gastric mucosa by stimulating surface epithelial cells to secrete mucus and bicarbonate, and by maintaining the mucosal microcirculation that clears any acid penetrating the barrier. NSAIDs inhibit COX enzymes, blocking prostaglandin synthesis and stripping away this protection. The result is that even the normally manageable level of gastric acid erodes the now-unprotected epithelium. Acid production is actually increased or unchanged — the problem is lost protection, not reduced acid."

- question: "Chief cells secrete pepsinogen rather than active pepsin. Why is this arrangement physiologically necessary?"
  type: multiple-choice
  options:
    - "Pepsin is too large a molecule to be secreted by exocytosis and must be cleaved to a smaller form first"
    - "Active pepsin secretion would digest the chief cells themselves and the gastric epithelium before reaching the luminal contents"
    - "Pepsinogen must first bind to intrinsic factor in the lumen before it can acquire protease activity"
    - "Pepsin is only effective at neutral pH, so it must be stored as pepsinogen and converted to its active form outside the acidic stomach"
  answer: 1
  explanation: "This is a safety mechanism against autodigestion. Pepsin is a potent protease that works optimally at pH 1.5–2.5. If chief cells secreted it in active form, pepsin would digest the cellular machinery producing it and erode the surrounding mucosa. By secreting the inactive zymogen pepsinogen instead, the cell is protected. Pepsinogen is only converted to pepsin in the gastric lumen when it encounters the low pH created by parietal cells — a tight functional coupling that ensures enzyme activation occurs only where it can safely work."

- question: "The cephalic phase of gastric acid secretion begins only after food physically enters the stomach and distends the gastric wall."
  type: true-false
  answer: false
  explanation: "The cephalic phase is a feedforward response triggered by the sight, smell, taste, or even the thought of food — before food reaches the stomach at all. Vagal activation directly stimulates parietal cells (via acetylcholine) and triggers gastrin release from antral G cells, accounting for roughly 30% of total acid output. It is the gastric phase that begins when food physically arrives and distends the stomach. The cephalic phase is the stomach anticipating and preparing for the meal."

- question: "The intestinal phase of gastric secretion serves primarily as an inhibitory feedback mechanism — duodenal hormones like secretin and CCK slow gastric acid secretion and gastric emptying when chyme enters the duodenum."
  type: true-false
  answer: true
  explanation: "The intestinal phase is the stomach's feedback shutoff. When acidic, fat- and protein-rich chyme enters the duodenum, S cells release secretin (in response to acid) and I cells release CCK (in response to fats and proteins). Secretin inhibits gastric acid secretion; CCK slows gastric emptying by reducing antral contractions and increasing pyloric tone. Together these hormones prevent the small intestine from being overwhelmed by more chyme than it can neutralize and absorb — matching delivery rate to processing capacity."

- question: "Explain the functional logic of pepsinogen secretion — why is secreting an inactive protease precursor a better design than secreting the active enzyme directly?"
  type: short-answer
  answer: "Secreting pepsinogen rather than active pepsin prevents autodigestion. If chief cells secreted active pepsin, it would digest the protein machinery of the secreting cells and the surrounding gastric epithelium before reaching the luminal food. Pepsinogen is an inactive zymogen that only converts to active pepsin in the acidic gastric lumen (pH < 2), where low pH cleaves the inhibitory peptide. Active pepsin then autocatalytically activates more pepsinogen, rapidly amplifying enzyme activity in the lumen — the one place where proteolysis is useful and safe."
  explanation: "This zymogen strategy is used throughout the digestive system (trypsinogen, chymotrypsinogen, proelastase) and illustrates a general principle: dangerous enzymes are stored and transported in inactive forms, activated only at the site of action. The tight functional coupling here — parietal cells create the acidic environment that activates the chief-cell enzyme — means pepsin activity is automatically localized to the gastric lumen when acid is present. Proton pump inhibitors (PPIs) exploit this coupling: by raising intragastric pH, they indirectly reduce pepsin activity even though they don't target pepsinogen or pepsin directly."
```

## Explainer

The stomach is both a chemical reactor and a mechanical mixer, and understanding gastric physiology means understanding how these two functions are coordinated. From your study of parietal cell secretion, you know that parietal cells use a proton pump (H⁺/K⁺-ATPase) to generate hydrochloric acid at a pH near 1 — one of the most acidic environments in biology. But acid production is not constant; it ramps up and down through three overlapping phases that match the stages of a meal, each regulated by different signals.

The **cephalic phase** begins before food even reaches the stomach. The sight, smell, or thought of food activates the vagus nerve, which directly stimulates parietal cells (via acetylcholine) and triggers gastrin release from G cells in the antrum. This accounts for roughly 30% of total acid output and explains why anticipation of a meal "gets your stomach ready." The **gastric phase** begins when food physically arrives, distending the stomach wall and raising intragastric pH (because food buffers the acid). Stretch receptors activate local and vagovagal reflexes, while proteins and peptides stimulate G cells to release more gastrin. This phase produces the bulk of acid secretion — around 60%. The **intestinal phase** contributes the remaining 10% as partially digested food enters the duodenum, but this phase also initiates the shutdown signals: secretin and cholecystokinin (CCK) released by the duodenal mucosa inhibit gastric acid secretion and slow gastric emptying, preventing the small intestine from being overwhelmed by acidic chyme.

**Chief cells** secrete pepsinogen, the inactive precursor to the protein-digesting enzyme pepsin. This is a safety mechanism: if chief cells secreted active pepsin directly, it could digest the cells that produce it. Instead, pepsinogen is activated only after it encounters the acidic environment of the gastric lumen, where low pH cleaves the inhibitory peptide fragment, converting pepsinogen to active pepsin. Pepsin then autocatalytically activates more pepsinogen, creating a rapid amplification of enzyme activity within the lumen. Pepsin works optimally at pH 1.5–2.5, which is precisely the environment that parietal cells create — a tight functional coupling between acid secretion and protein digestion.

The stomach protects itself from its own secretions through a **mucosal barrier**: surface epithelial cells secrete a thick layer of bicarbonate-rich mucus that maintains a near-neutral pH at the cell surface even while luminal pH is below 2. Prostaglandins stimulate both mucus and bicarbonate secretion and promote mucosal blood flow, which rapidly clears any acid that penetrates the barrier. This explains why nonsteroidal anti-inflammatory drugs (NSAIDs), which inhibit prostaglandin synthesis, increase the risk of gastric ulcers. Meanwhile, gastric motility — coordinated waves of smooth muscle contraction — churns food against the gastric wall, mixing it with acid and pepsin to produce **chyme**, a semifluid mass. The pyloric sphincter releases chyme into the duodenum in small, controlled pulses, ensuring that the rate of delivery matches the small intestine's capacity for neutralization and digestion.
