---
id: migration-and-development
title: Migration, Remittances, and Development
domain: economics
course: development-economics
prerequisites:
- id: demographic-transition-model
  type: hard
- id: labor-market-signaling
  type: soft
- id: labor-migration-development
  type: soft
- id: environmental-sustainability-development
  type: soft
builds-toward:
- inequality-kuznets-curve
tags:
- migration
- remittances
- development
stage: expert
status: validated
---
# Migration, Remittances, and Development

## Core Idea
International migration reallocates labor from low-wage to high-wage economies, benefiting migrants and receiving countries but creating selection (high-ability emigrate) and skill-drain risks for sending countries. Remittances supplement household income in sending countries and now exceed official aid. Internal migration (rural-to-urban) drives urbanization and structural transformation; quality of urban institutions determines whether migrants thrive or end in slums.

## Questions

```yaml
- question: "A developing country experiences significant emigration of its most educated workers. A policymaker argues this is unambiguously harmful because the country loses the return on its educational investment. What does development economics research suggest about this assessment?"
  type: multiple-choice
  options:
    - "It is correct — brain drain always reduces long-term growth in sending countries"
    - "It is incomplete — returning migrants, diaspora networks, and remittances may offset or exceed the losses"
    - "It is incorrect — emigration of educated workers has no measurable effect on sending country GDP"
    - "It is correct, but only when remittances constitute less than 5% of GDP"
  answer: 1
  explanation: "Brain drain is a real cost, but it is not the whole story. Migrants who return bring skills, networks, and capital. Diaspora communities generate trade and investment links. And remittances now exceed $600 billion annually — dwarfing official development aid — directly reducing poverty at the household level. The correct view is that migration's net effect on sending countries depends on migration rates, return patterns, remittance levels, and institutional capacity, not a simple subtraction of human capital."

- question: "In the Harris-Todaro model, rural workers migrate to cities even when urban unemployment is high. What best explains this apparently irrational behavior?"
  type: multiple-choice
  options:
    - "Migrants are uninformed about actual conditions in cities"
    - "Migrants compare certain rural wages against expected urban wages — the urban wage weighted by the probability of finding employment"
    - "Migrants value urban amenities enough to accept lower expected income"
    - "The model assumes migrants will eventually find employment regardless of current unemployment rates"
  answer: 1
  explanation: "Harris-Todaro is an expected-value model. A rational migrant compares what they earn for certain in agriculture against the wage they would earn in a formal urban job multiplied by the probability of actually getting one. If formal urban wages are high enough, this product can exceed rural wages even when urban unemployment is substantial. The decision is not irrational — it reflects a probabilistic bet on better prospects. The model's power is that it explains persistent rural-urban migration even when cities visibly cannot absorb all arrivals."

- question: "Remittances are generally less valuable for development than official aid because they flow to households rather than public investment."
  type: true-false
  answer: false
  explanation: "This gets the comparison backwards. Remittances flow directly to households, which does mean they bypass public investment — but this is both a limitation and an advantage. Unlike aid, remittances go directly to families who can spend or invest them according to their own priorities. They reduce poverty, fund education, and improve nutrition with minimal administrative overhead. The argument that household targeting makes them inferior assumes public investment is more efficient, which is contested. Globally, remittances exceed official aid by a large margin and have grown faster and more reliably."

- question: "Whether rural-to-urban migration drives development or merely relocates poverty depends critically on the quality of urban institutions, not just on the volume of migrants."
  type: true-false
  answer: true
  explanation: "This is the central institutional insight about internal migration. When cities have functioning land markets, accessible public services, infrastructure investment, and a path to formal employment, migrants become productive citizens and structural transformation occurs. When cities lack these — poor governance, inadequate housing, absent sanitation — migrants end up in informal settlements with underemployment and urban poverty. The migration flow itself is neutral; the urban context determines whether it is developmentally beneficial."

- question: "Why does the selective nature of international migration create a tension for sending countries, even when total remittance flows are large?"
  type: short-answer
  answer: "Migration is not random — migrants tend to be younger, healthier, more educated, and more entrepreneurial than those who stay. This 'positive selection' means sending countries lose their most capable workers, who are also the most likely to generate innovation, entrepreneurship, and high productivity at home. Even if remittances are large in aggregate, they flow to households rather than rebuilding the human capital base that left. The tension is that the same people whose departure generates remittances are the people whose presence would most directly improve productive capacity in the sending economy."
  explanation: "This is the brain drain paradox. The development gain from remittances is real but operates through a different channel (household income) than the loss (human capital stock and growth potential). Countries like Nepal and Tajikistan with remittances above 20% of GDP simultaneously face severe shortages of skilled workers. Whether the exchange is net positive depends on whether migrants return, whether diaspora investment substitutes for local talent, and whether remittances fund human capital formation (education) in the next generation."
```

## Explainer

Migration — both within and across national borders — is one of the most powerful forces in economic development. From your study of the **demographic transition**, you know that developing countries experience rapid population growth as death rates fall before birth rates adjust. This population pressure, combined with limited rural opportunities, creates strong incentives for people to move. Understanding migration's effects on development requires thinking about who moves, what they send back, and what happens to the places they leave and the places they arrive.

**International migration** moves workers from low-wage to high-wage economies, and the wage gains are enormous — often a 3x to 10x increase for the same worker doing the same job in a richer country. But migration is not random. It is **selective**: migrants tend to be younger, healthier, more educated, and more entrepreneurial than those who stay behind. This selection creates a tension. The migrant benefits individually, and the receiving country gains a productive worker. But the sending country loses some of its most capable people — the phenomenon known as **brain drain**. When a country that invested in training a doctor or engineer loses that person to a wealthier nation, the return on that educational investment is captured abroad. However, brain drain is not the whole story. Migrants who return bring skills, networks, and capital. And diaspora communities create trade and investment links between sending and receiving countries.

The most concrete channel through which migration benefits sending countries is **remittances** — money migrants send home to families. Global remittance flows to developing countries now exceed $600 billion annually, dwarfing official development aid. For many countries (Nepal, Haiti, Tajikistan), remittances constitute over 20% of GDP. At the household level, remittances reduce poverty, fund education, improve nutrition, and provide a buffer against income shocks. At the national level, they provide foreign exchange and stimulate local demand. But remittances also have limitations: they flow to households rather than public investment, they can create dependency, and they may appreciate the local currency, making exports less competitive.

**Internal migration** — particularly rural-to-urban movement — is the engine of structural transformation within countries. As workers move from low-productivity agriculture to higher-productivity urban employment, national output rises. This is the Harris-Todaro model in action: migrants compare expected urban wages (adjusted for the probability of finding employment) against certain rural wages, and move when the urban option looks better. The challenge is that urbanization can outpace the creation of formal jobs and adequate infrastructure. When cities cannot absorb migrants with productive employment and basic services — housing, sanitation, transport — the result is informal settlements, underemployment, and urban poverty. Whether migration drives development or merely relocates poverty depends critically on urban governance: cities with functioning land markets, infrastructure investment, and accessible public services turn migrants into productive citizens; cities without these institutions trap them in slums.
