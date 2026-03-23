---
id: bioethics
title: Bioethics
domain: philosophy
course: ethics
prerequisites:
- id: applied-ethics-intro
  type: hard
- id: contractualism
  type: soft
- id: trolley-problem
  type: soft
tags:
- applied-ethics
- bioethics
- medicine
- autonomy
- justice-in-healthcare
stage: formal-systems
status: validated
---
# Bioethics

## Core Idea
Bioethics examines moral questions arising in medicine, biology, and healthcare: informed consent, end-of-life decisions, resource allocation, genetic enhancement, research ethics, and reproductive technologies. The Belmont Report (1979) established three foundational principles: respect for persons (autonomy), beneficence (do good, avoid harm), and justice (fair distribution of burdens and benefits). Beauchamp and Childress expanded this into the four-principles approach (adding non-maleficence). Bioethics must navigate conflicts between patient autonomy and paternalism, individual benefit and public health, and the moral status of embryos, fetuses, and non-human animals.

## How It's Best Learned
Study landmark cases: the Tuskegee syphilis study (research ethics), Karen Ann Quinlan (end of life), and the case for and against physician-assisted suicide. Apply the four principles to each case and identify where they conflict.

## Common Misconceptions
- Informed consent is not merely signing a form; it requires that the patient understands relevant information, is competent to decide, and chooses voluntarily.
- Bioethics is not reducible to medical law; something can be legally permitted but ethically questionable, or legally prohibited but potentially justified.

## Questions

```yaml
- question: "A competent adult Jehovah's Witness refuses a life-saving blood transfusion on religious grounds, having been fully informed of the consequences. Should the physician administer the transfusion anyway?"
  type: multiple-choice
  options:
    - "Yes — beneficence and non-maleficence together outweigh autonomy when a life is at stake"
    - "No — respecting the informed refusal of a competent patient is required by the principle of autonomy, even when the physician disagrees"
    - "Yes — justice requires using available resources when they can save a life"
    - "It depends on whether the patient has signed a legally binding advance directive"
  answer: 1
  explanation: "The four-principles approach does not automatically rank beneficence above autonomy. A competent, informed, voluntary refusal is the paradigm case of autonomous decision-making that bioethics was developed to protect. Strong paternalism — overriding a competent refusal 'for the patient's own good' — is deeply contested precisely because it treats the patient as a means to an outcome they have rejected. Option A restates paternalism without engaging the philosophical challenge. Option C introduces justice in a way that is irrelevant here. The legal question in D is distinct from the ethical one."

- question: "The Tuskegee syphilis study is paradigmatic in bioethics because it illustrates that:"
  type: multiple-choice
  options:
    - "Research ethics violations only occur when studies lack proper control groups"
    - "Medical authority without ethical constraint can systematically exploit vulnerable populations, destroying the trust that medicine depends on"
    - "The Belmont principles were already in place but were simply ignored by researchers"
    - "Consent requirements should be stricter for experimental treatments than for standard ones"
  answer: 1
  explanation: "The Tuskegee study (1932–72) withheld treatment from Black men with syphilis without their knowledge or consent, and continued even after penicillin became available. It illustrates what happens when medical authority operates without ethical constraint — particularly on a population that was already vulnerable and distrustful of medical institutions. The study directly motivated the Belmont Report (1979), so Option C has the causation backwards: the Belmont principles were developed *in response to* Tuskegee. The lesson is about systemic power and the necessity of principled ethical oversight."

- question: "Under the four-principles approach, the principle of autonomy does not automatically override beneficence — each case requires weighing which principle applies with greater force given the specific circumstances."
  type: true-false
  answer: true
  explanation: "This is the foundational feature of Beauchamp and Childress's framework: the four principles (autonomy, beneficence, non-maleficence, justice) are *prima facie* obligations, meaning each has genuine weight but none has absolute priority. They can conflict, and resolving conflicts requires contextual judgment about which principle is most weighty in this type of case. For a competent patient's refusal, autonomy typically prevails; for a patient lacking decision-making capacity, beneficence may take precedence. The framework provides vocabulary for identifying the conflict, not an algorithm for resolving it."

- question: "Informed consent is satisfied as long as the patient signs a consent form and has received written information about the relevant procedure."
  type: true-false
  answer: false
  explanation: "This is explicitly flagged in the Common Misconceptions: informed consent requires three conditions — that the patient has *understood* the relevant information (not merely received it), that they are *competent* to make decisions, and that their choice is *voluntary* (free from coercion or undue influence). Signing a form documents consent but does not constitute it. A patient can sign without understanding; a coerced patient can sign voluntarily-appearing forms. The philosophical content of consent is about genuinely autonomous decision-making, not the bureaucratic record of it."

- question: "Explain why the four principles of bioethics cannot simply be ranked in a fixed hierarchy, and what happens when they conflict in practice."
  type: short-answer
  answer: "The four principles — autonomy, beneficence, non-maleficence, justice — are prima facie obligations: each has genuine moral weight, but none is lexically prior to the others in all cases. They conflict in structurally different ways in different situations. Respecting a patient's informed refusal (autonomy) may conflict with preventing serious harm (non-maleficence). Allocating scarce ICU beds by likelihood of survival (justice) may conflict with giving every patient the maximum possible benefit (beneficence). A fixed ranking would resolve these conflicts mechanically, but different cases call for different weightings. A paternalistic override of a competent refusal treats autonomy as subordinate to beneficence; most contemporary bioethics rejects this. But for an incompetent patient, beneficence may appropriately override what the patient once expressed. The framework requires judgment about the type of case, not application of a priority rule."
  explanation: "The absence of a fixed hierarchy is sometimes criticized as leaving bioethics without action-guiding force. But defenders argue that this flexibility is a feature: it acknowledges that moral life involves genuine, context-dependent tradeoffs, and that any fixed ranking would produce clearly wrong verdicts in the cases that fall outside the paradigm the ranking was designed for."
```

## Explainer

From applied ethics, you know that moral theories — consequentialism, deontology, virtue ethics — can be brought to bear on practical problems. Bioethics is perhaps the richest testing ground for these frameworks because medical decisions involve real stakes, genuine value conflicts, and institutional power. The field developed its modern form partly in response to specific historical outrages: the Tuskegee syphilis study (1932–72), in which researchers withheld treatment from Black men with syphilis without their knowledge or consent, demonstrated what happens when medical authority operates without ethical constraint. The **Belmont Report** (1979) established the principles now governing research ethics: respect for persons (protect autonomy, especially of vulnerable populations), beneficence (do good and prevent harm), and justice (distribute research burdens and benefits fairly).

Beauchamp and Childress's **four-principles approach** — autonomy, beneficence, **non-maleficence** (do no harm), and justice — became the dominant framework in clinical bioethics. These principles do not form a hierarchy; they are prima facie obligations that must be weighed against each other in each specific case. This is where your understanding of the trolley problem becomes directly relevant. In trolley cases, you faced whether it is permissible to harm one to save five — a pure consequentialist calculation. Bioethics raises structurally similar questions: is it permissible to override a patient's informed refusal of treatment to prevent serious harm to that patient (autonomy versus beneficence)? Is it permissible to allocate scarce organs using criteria that disadvantage some populations (justice versus beneficence)? The four principles give you a vocabulary for identifying the conflict but do not automatically resolve it — resolution requires judgment about which principle takes priority in this type of case.

**Informed consent** is the institutional expression of autonomy — the requirement that patients be adequately informed, mentally competent, and free from coercion before any medical intervention. The philosophical content connects to deontological ethics: treating patients as autonomous agents means giving them the information they need to make their own decisions, not managing them for their supposed benefit. **Paternalism** — overriding a person's choices for their benefit — is sometimes defensible (for patients lacking decision-making capacity), but strong paternalism (overriding a competent, informed refusal) is deeply contested. The moral status questions in bioethics — when does personhood begin? do embryos have moral standing? what do we owe to non-human animals used in research? — connect back to metaethics and moral metaphysics, making bioethics simultaneously a practical and deeply theoretical field. Your background in contractualism is also relevant here: questions of fair resource allocation under scarcity — who gets the last ventilator, who is prioritized for organ transplants — are precisely the kinds of questions contractualist frameworks are designed to address by asking what principles no one could reasonably reject.
