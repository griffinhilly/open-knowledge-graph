---
id: prioritarianism
title: Prioritarianism
domain: philosophy
course: political-philosophy
prerequisites:
- id: distributive-justice
  type: hard
- id: difference-principle
  type: soft
tags:
- prioritarianism
- Parfit
- worst-off
- weighted-benefits
- distributive-justice
stage: formal-systems
status: validated
---

# Prioritarianism

## Core Idea
Prioritarianism, most associated with Derek Parfit, holds that benefits matter more the worse off the person receiving them is. Unlike strict egalitarianism, it does not value equality for its own sake — it would not endorse leveling down (making everyone worse off to achieve equality). Unlike utilitarianism, it does not treat a unit of benefit to a billionaire as equivalent to the same unit given to someone in poverty. The priority view assigns greater moral weight to improvements in well-being for those at lower absolute levels. This captures the intuition behind Rawls's difference principle while avoiding some of its structural rigidities, though it raises its own difficulties about how steeply to weight benefits to the worst-off.

## How It's Best Learned
Compare prioritarianism side by side with utilitarianism and egalitarianism on a distribution problem — e.g., a fixed budget that could give 10 units to a rich person or 8 units to a poor person. Utilitarianism picks the 10; egalitarianism may pick the 8 to reduce the gap; prioritarianism picks the 8 because benefits to the worse-off carry greater moral weight. Then examine Parfit's leveling-down objection to pure egalitarianism.

## Common Misconceptions
- Prioritarianism is not maximin (Rawls) — it weights benefits to the worst-off more heavily but does not exclusively focus on the worst-off group.
- It does not ignore benefits to the well-off; it merely discounts them relative to equivalent benefits at lower levels.
- The 'priority' is about absolute position, not relative position — what matters is how badly off someone is, not how much worse off they are than others.

## Questions

```yaml
- question: "A public health budget can fund either Program A (gives 10 welfare units to a person at baseline well-being of 80) or Program B (gives 8 welfare units to a person at baseline well-being of 20). A utilitarian picks A. A prioritarian picks B. Why?"
  type: multiple-choice
  options:
    - "The prioritarian thinks equality has intrinsic value, so reducing the gap between rich and poor is always preferred"
    - "The prioritarian assigns greater moral weight to benefits received at lower levels of well-being, making the weighted value of 8 units to the worse-off person exceed the weighted value of 10 units to the better-off person"
    - "The prioritarian follows Rawls's maximin rule and always benefits the worst-off person regardless of magnitude"
    - "The prioritarian believes well-off people do not deserve welfare improvements"
  answer: 1
  explanation: "Prioritarianism weights welfare improvements by a factor that increases as the recipient's baseline well-being decreases. Because the person at well-being level 20 is much worse off than the person at level 80, the same quantum of benefit counts for more morally. The 8 units to the worse-off person, once weighted, outweigh the 10 units to the better-off person. This is NOT because equality has intrinsic value (that's egalitarianism) or because we must benefit the worst-off exclusively (that's maximin). It is because absolute position determines moral weight."

- question: "How does prioritarianism differ from Rawls's difference principle (maximin)?"
  type: multiple-choice
  options:
    - "Prioritarianism ignores the worst-off group; maximin focuses exclusively on it"
    - "Prioritarianism gives extra moral weight to all worse-off people (with weight increasing at lower levels); maximin focuses exclusively on improving the position of the worst-off group"
    - "Prioritarianism is concerned with relative inequality; maximin is concerned with absolute levels of welfare"
    - "They are equivalent — both instruct us to maximize the welfare of the least well-off"
  answer: 1
  explanation: "Rawls's maximin principle focuses entirely on the worst-off group: inequalities are just only if they benefit those at the bottom. Prioritarianism gives extra weight to benefits to all worse-off people, with weight smoothly increasing as well-being decreases. A benefit to the second-poorest matters more than a benefit to someone in the middle, even if the absolute worst-off is unaffected. Prioritarianism is sensitive to the entire distribution weighted by absolute level, not just its minimum."

- question: "Prioritarianism holds that equality has intrinsic moral value — a perfectly equal distribution is always preferable to an unequal one, even if the equal distribution leaves everyone worse off."
  type: true-false
  answer: false
  explanation: "This describes strict egalitarianism, not prioritarianism. Prioritarianism explicitly rejects intrinsic concern with equality. Parfit's leveling-down objection exposes the problem: pure egalitarianism seems to endorse making everyone equally miserable rather than allowing an unequal but Pareto-superior distribution. Prioritarianism avoids this by focusing on absolute well-being levels rather than the gap between people — it cares about how badly off someone is, not how much worse off they are than others."

- question: "In prioritarianism, what makes a benefit more morally weighty is the recipient's absolute level of well-being — not how much worse off they are relative to others."
  type: true-false
  answer: true
  explanation: "This is a crucial distinction from egalitarianism. Egalitarians care about relative position — the gap between people. Prioritarians care about absolute position — how badly off someone is in absolute terms. If a person has very low well-being, benefits to them carry extra moral weight regardless of whether others are similarly or more badly off. Prioritarianism focuses on absolute suffering, not relative inequality, which is why it can recommend distributions that increase inequality while remaining defensible."

- question: "What is the leveling-down objection to egalitarianism, and how does prioritarianism respond to it?"
  type: short-answer
  answer: "The leveling-down objection: pure egalitarianism implies that an equal distribution where everyone has 5 welfare units is morally superior to an unequal distribution where one person has 10 and another has 8 — even though in the equal distribution the better-off person has been made worse off and no one has gained. Egalitarianism seems to endorse this because equality has intrinsic value. Prioritarianism responds by denying that equality has intrinsic value: it cares only about absolute levels of well-being, so making someone worse off is never an improvement — there is no benefit to leveling down."
  explanation: "Parfit used this objection to distinguish genuine concern for the badly-off (captured by prioritarianism) from mere concern for equality (which he thought was confused). A prioritarian world with slight inequality but higher absolute well-being for all is unambiguously better than a perfectly equal world where everyone is worse off. This makes prioritarianism more defensible than strict egalitarianism while still capturing the intuition that improving the lives of the worst-off matters more than equivalent improvements for the well-off."
```

## Explainer

Your study of distributive justice has given you the basic toolkit: utilitarian theories maximize aggregate welfare, egalitarian theories prioritize equality, and Rawls's difference principle demands that inequalities benefit the worst-off members of society. Prioritarianism, developed by Derek Parfit, can be understood as a careful attempt to extract the genuine moral insight from each of these views while avoiding their characteristic problems.

Start with a thought experiment. You have a fixed budget of welfare units to distribute. You can give 10 units to a wealthy person or 8 units to someone in poverty. **Utilitarianism** says: give the 10 units, because more total welfare is better. **Strict egalitarianism** might say: give the 8, because reducing the gap matters independently of total welfare. But notice the egalitarian claim is strange — it seems to say equality has intrinsic value even if we could make someone better off at no cost. Parfit calls this the **leveling-down objection**: pure egalitarianism sometimes implies making some people worse off just to achieve equality, which seems perverse. If everyone is equally miserable, that is a strange kind of success.

**Prioritarianism** resolves this by saying: the 8 units to the poor person are worth *more* morally than the 10 units to the wealthy person, because benefits to people at lower levels of well-being carry greater **moral weight**. It is not that equality matters intrinsically; it is that the same quantum of welfare improvement has a higher priority when it goes to someone who is badly off. This generates a weighted welfare function: rather than summing raw welfare levels, you sum welfare weighted by a factor that increases as well-being decreases. The poor person's 8 units, once weighted, outweigh the wealthy person's 10.

The key distinctions from adjacent views are worth fixing clearly. Prioritarianism differs from **maximin** (Rawls's difference principle) because it does not focus exclusively on the worst-off person — it gives extra weight to *all* worse-off people, with the weight increasing as you go lower on the scale. A benefit to the second-poorest matters more than a benefit to the middle, even if the absolute poorest is not affected. It differs from **egalitarianism** because it has no intrinsic concern with the gap between people — it only cares about absolute levels, not relative positions. And it differs from **utilitarianism** because it does not treat a unit of welfare as equivalent across all persons. What makes prioritarianism philosophically attractive is precisely this combination: it captures the intuition that improving the lives of the worst-off matters most, without collapsing into the structural rigidities of maximin or the paradoxes of leveling-down egalitarianism. The remaining challenge is determining *how steeply* to weight benefits at lower levels — a question that admits no purely principled answer and forces prioritarianism to confront its own parameter choices.
