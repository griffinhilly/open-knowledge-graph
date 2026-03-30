---
id: cellular-hypertrophy-hyperplasia-pathophysiology
title: Cellular Hypertrophy and Hyperplasia in Disease
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: cell-injury-and-adaptation
  type: hard
- id: cell-cycle-overview
  type: hard
- id: left-ventricular-hypertrophy
  type: soft
builds-toward:
- cardiac-hypertrophy-left-ventricular-remodeling
- vascular-smooth-muscle-remodeling
tags:
- cellular-adaptation
- hypertrophy
- hyperplasia
stage: advanced
status: validated
---
# Cellular Hypertrophy and Hyperplasia in Disease

## Core Idea
Hypertrophy is increase in cell size through accumulation of contractile proteins and organelles; hyperplasia is increase in cell number through proliferation. Both represent compensatory responses to increased workload but can become pathologic if uncontrolled, leading to organ dysfunction.

## Questions

```yaml
- question: "A patient with long-standing hypertension develops a markedly thickened left ventricular wall. Biopsy reveals enlarged individual myocytes. Why does the heart adapt this way rather than generating new myocytes?"
  type: multiple-choice
  options:
    - "Hypertension specifically inhibits the cell cycle in cardiac myocytes through a feedback mechanism"
    - "Cardiac myocytes are permanent cells that have largely exited the cell cycle and cannot undergo mitosis"
    - "Generating new myocytes would require more energy than simply enlarging existing ones"
    - "Hyperplasia is always pathological in the heart, so the body suppresses it by design"
  answer: 1
  explanation: "Cardiac myocytes are permanent (non-dividing) cells. From cell cycle biology: they have largely exited the cycle and lack the CDK-cyclin machinery needed to reenter and complete mitosis. When workload increases due to hypertension, the only adaptive response available is hypertrophy — increasing cell size by synthesizing more contractile proteins (actin, myosin) and adding sarcomeres. This constraint, not metabolic efficiency or a regulatory prohibition, determines which adaptation occurs."

- question: "A patient's endometrial hyperplasia, driven by unopposed estrogen, resolves completely after hormonal correction. What does this indicate about the nature of the hyperplastic tissue?"
  type: multiple-choice
  options:
    - "The hyperplasia was benign neoplasia that spontaneously regressed when the trigger was removed"
    - "The hyperplasia was pathologic but retained normal growth-control mechanisms — it regressed when the proliferative stimulus was withdrawn"
    - "The hyperplasia was physiologic because normal tissue does not persist without a stimulus"
    - "The cells had undergone neoplastic transformation but reverted to normal differentiation"
  answer: 1
  explanation: "The defining characteristic of hyperplasia (versus neoplasia) is that it retains normal growth controls: it requires a sustained stimulus and regresses when the stimulus is removed. Neoplastic cells acquire autonomous growth-promoting mutations and proliferate without external signal. Pathologic hyperplasia is clinically important not because it is itself uncontrolled, but because it creates an expanded population of proliferating cells in which subsequent mutations can accumulate, increasing cancer risk — but it has not yet crossed the threshold to autonomy."

- question: "Hypertrophy and hyperplasia are both adaptive responses available to most cell types in the body, including neurons and cardiac myocytes."
  type: true-false
  answer: false
  explanation: "The available adaptive response depends on whether the cell can divide. Permanent cells — neurons, cardiac myocytes, and skeletal muscle fibers — have exited the cell cycle and cannot re-enter it to proliferate. These cells can only hypertrophy. Labile cells (intestinal epithelium, bone marrow) cycle continuously and can undergo hyperplasia. Stable cells (hepatocytes, smooth muscle) are quiescent in G0 but can re-enter the cycle when stimulated and can do both. This cell-type classification directly determines the pathology observed in different organs."

- question: "Pathologic hyperplasia increases cancer risk in part because a larger population of actively proliferating cells provides more opportunities for oncogenic mutations to arise and accumulate."
  type: true-false
  answer: true
  explanation: "Each cell division carries some probability of replication error. Hyperplasia expands the dividing cell population and may sustain elevated proliferative signaling (e.g., chronic estrogen exposure in endometrial hyperplasia), both of which increase the statistical likelihood of acquiring mutations in proto-oncogenes or tumor suppressor genes. Pathologic hyperplasia thus represents a risk state even though it retains growth control — it is the substrate on which neoplastic transformation is more likely to occur."

- question: "Distinguish hypertrophy from hyperplasia at the cellular level and explain why the cell type determines which response is possible when tissue faces increased demand."
  type: short-answer
  answer: "Hypertrophy is an increase in cell size without division: the cell synthesizes more protein (especially contractile or structural proteins) than it degrades, accumulates more organelles, and grows larger while remaining a single cell. Hyperplasia is an increase in cell number through mitotic division: cells re-enter the cell cycle, replicate their DNA, and divide. Which response is possible depends on whether the cell can divide. Permanent cells (cardiac myocytes, neurons) have exited the cell cycle irreversibly and can only hypertrophy. Stable and labile cells retain the capacity to re-enter the cycle and can undergo hyperplasia. Increased demand — whether mechanical (pressure load on the heart) or hormonal (estrogen on the endometrium) — triggers the response available to that cell type."
  explanation: "This cell-type dependency has direct clinical consequences: cardiac hypertrophy is the only response the heart can mount to chronic pressure overload, and when it becomes maladaptive it leads to heart failure rather than proliferative disease. Endometrial hyperplasia, by contrast, involves actual cell division and creates the cancer risk substrate. Understanding which mechanism is operating is essential for predicting both the physiological consequences and the long-term clinical trajectory."
```

## Explainer

The key to understanding hypertrophy versus hyperplasia is recognizing that not all cells can divide. From your study of the cell cycle, you know that progression through G1, S, G2, and M requires growth factor signaling, adequate nutrients, and CDK-cyclin complexes to be active. **Permanent cells** — neurons, cardiac myocytes, and skeletal muscle fibers — have largely exited the cell cycle and cannot proliferate in response to injury or increased demand. **Stable (quiescent) cells** — hepatocytes, smooth muscle cells, fibroblasts — are in G0 but can re-enter the cycle when stimulated. **Labile cells** — intestinal epithelium, bone marrow precursors, skin keratinocytes — cycle continuously. This division determines which adaptive response is available: permanent cells can only hypertrophy; labile and stable cells can do both.

**Hypertrophy** is the increase in cell size without cell division, driven by increased protein synthesis exceeding protein degradation. The cardiac myocyte is the paradigm case. When left ventricular afterload increases — due to hypertension or aortic stenosis — myocytes synthesize more contractile proteins (actin, myosin heavy chains) and add more sarcomeres. The result is a thicker, heavier ventricle that can generate more force. Growth factor signaling (IGF-1, angiotensin II, endothelin) activates the PI3K/Akt/mTOR pathway, which drives ribosomal biogenesis and protein translation. In the early compensatory phase, hypertrophy maintains cardiac output. But sustained hypertrophy is maladaptive: the enlarged myocyte outgrows its capillary supply, mitochondrial density falls relative to cell volume, and the tissue becomes stiff, predisposing to diastolic dysfunction, arrhythmia, and eventually heart failure.

**Hyperplasia** is increase in cell number through mitosis, available only to cells capable of re-entering the cell cycle. From your cell cycle knowledge, you know this requires cyclin D upregulation, Rb phosphorylation, and E2F transcriptional activation of S-phase genes. Growth factor receptors — EGFR, PDGFR, estrogen receptor — drive this process in hormone-responsive or injury-stimulated tissues. Physiologic hyperplasia is beneficial: bone marrow hyperplasia in response to anemia, compensatory liver hyperplasia after partial hepatectomy. Pathologic hyperplasia — endometrial hyperplasia driven by unopposed estrogen, prostatic hyperplasia, or thyroid goiter — occurs when the proliferative signal is chronically elevated. Pathologic hyperplasia is clinically important because, unlike neoplasia, it retains normal growth-control mechanisms and regresses when the stimulus is removed; but it creates a substrate of increased cell number in which subsequent mutations can more easily accumulate, increasing cancer risk.

The boundary between adaptation and pathology is defined by control: hypertrophy and hyperplasia become pathologic when growth is disproportionate to the functional demand, when the structural changes impair organ function rather than enhance it, or when proliferative control is lost. The final step toward malignancy — which neither hypertrophy nor hyperplasia represents — occurs when cells acquire autonomous growth-promoting mutations and lose the ability to stop. Understanding where on this continuum a given cellular change sits is fundamental to pathologic diagnosis.
