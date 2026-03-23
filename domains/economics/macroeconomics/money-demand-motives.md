---
id: money-demand-motives
title: Money Demand and Its Motives
domain: economics
course: macroeconomics
prerequisites:
- id: money-and-its-functions
  type: hard
builds-toward:
- loanable-funds-equilibrium
- monetary-policy-transmission
tags:
- money
- financial-markets
stage: formal-systems
status: draft
---

# Money Demand and Its Motives

## Core Idea
Agents demand money for three motives: transactions (to facilitate exchange), precautionary (to handle unexpected needs), and speculative (to take advantage of expected changes in asset prices). The transactions and precautionary demands increase with income, while speculative demand depends on interest rates and expectations of future interest rate movements. The aggregate money demand function M_d/P = L(Y, i) is increasing in output and decreasing in the nominal interest rate.

## Questions

```yaml
- question: "The central bank raises the nominal interest rate sharply. According to the three-motive theory of money demand, what should happen to speculative money demand?"
  type: multiple-choice
  options:
    - "It rises, because higher interest rates signal economic strength and encourage holding liquid assets"
    - "It falls, because higher current rates make bonds more attractive than holding cash, reducing the incentive to hold money speculatively"
    - "It stays the same, because speculative demand depends only on income, not interest rates"
    - "It rises, because agents need more liquidity to service higher-interest debt obligations"
  answer: 1
  explanation: "Speculative money demand is inversely related to the interest rate. When rates are high, bonds offer attractive yields — so agents prefer bonds over cash. When current rates are high, they are also more likely to fall in the future, meaning bond prices will rise, offering capital gains for bond holders. Both effects push speculative money demand down. Options C and D confuse speculative demand with other motives: transactions and precautionary demand primarily respond to income."

- question: "A severe recession reduces national income and output. What happens to aggregate money demand according to the money demand function L(Y, i)?"
  type: multiple-choice
  options:
    - "Money demand rises — people hoard cash when the economy is uncertain"
    - "Money demand rises — lower income means people need more liquidity to meet basic expenses"
    - "Money demand falls — lower output means fewer transactions and smaller precautionary reserves, shrinking both the transactions and precautionary motives"
    - "Money demand is unchanged — only interest rate changes affect money demand"
  answer: 2
  explanation: "The money demand function L(Y, i) is increasing in real output Y. In a recession, Y falls — fewer goods are being produced and exchanged, so there is less need to hold transaction balances. Lower incomes also reduce precautionary reserves (smaller expected unexpected expenses). The result is a leftward shift in money demand. Option A describes an informal behavioral tendency not captured in the core Keynesian three-motive framework."

- question: "Holding money has an opportunity cost equal to the interest foregone by not investing in interest-bearing assets like bonds."
  type: true-false
  answer: true
  explanation: "This is the foundational premise of money demand theory. If you hold $10,000 in cash when bonds yield 5%, you forgo $500 per year. This opportunity cost is what makes money demand an interesting economic puzzle: why hold money at all? The three motives — transactions, precautionary, and speculative — each identify what money can do that bonds cannot (facilitate exchange instantly, provide perfect liquidity), justifying its demand despite the cost."

- question: "The speculative motive for holding money increases when interest rates are high, because agents want to take advantage of the high returns available in the economy."
  type: true-false
  answer: false
  explanation: "This reverses the relationship. Money itself pays no interest — the speculative motive concerns the choice between holding money versus holding bonds. When interest rates are high, bonds offer high yields and are therefore attractive. Agents shift from money into bonds, reducing speculative money demand. Speculative demand is high when rates are LOW (or expected to rise, making bonds risky) and low when rates are HIGH. Confusing 'high rates in the economy' with 'money generates high returns' is a common error."

- question: "Why do the transactions and precautionary motives for money demand both increase with income, while the speculative motive responds to the interest rate instead?"
  type: short-answer
  answer: "Transactions and precautionary demands scale with the volume of exchange and the size of potential unexpected expenses — both of which grow proportionally with income. The speculative motive is a portfolio decision: how much wealth to hold in money versus bonds. This choice depends on the relative return of bonds (the interest rate) and expectations about future rate changes, not on income."
  explanation: "The key distinction is what each motive responds to. Transactions and precautionary demands are driven by the need for liquidity in proportion to economic activity — income scales this need. Speculative demand is driven by portfolio optimization — the tradeoff between money's perfect liquidity and bonds' yield. These are fundamentally different economic forces, which is why the aggregate money demand function L(Y, i) must include both income and the interest rate as separate arguments."
```

## Explainer

From your prerequisite study of money and its functions, you know that money serves as a medium of exchange, a store of value, and a unit of account. But this raises a puzzle: why do people hold money at all when they could hold interest-bearing assets like bonds? Holding money has an **opportunity cost** — the interest you forgo by keeping wealth in cash rather than invested. The theory of money demand is essentially an answer to the question: given this cost, why do rational agents still demand money, and how much of it?

Keynes identified three distinct motives, each driven by a different logic. The **transactions motive** is the most intuitive: you need money to buy things. Between paychecks or income receipts, you hold a buffer of cash to cover everyday purchases. The size of this buffer grows with your income — higher-income people make larger and more frequent transactions and need proportionally more money on hand. This motive treats money purely as a medium of exchange, demanded because exchange requires it. The **precautionary motive** extends this: beyond planned transactions, people hold extra money to handle unexpected needs — a sudden medical expense, a car repair, an unexpected opportunity. Like transactions demand, precautionary demand rises with income, because larger income implies larger potential unexpected expenses and larger precautionary reserves.

The **speculative motive** introduces the interest rate as a key determinant. Bond prices move inversely with interest rates — when rates rise, existing bond prices fall. If you expect interest rates to rise (bond prices to fall) in the near future, holding bonds means capital losses, and you'd prefer to hold money instead until the price decline occurs. Conversely, if rates are expected to fall (bond prices to rise), you'd rather hold bonds and capture the capital gain. In aggregate, the higher the current interest rate, the more likely it is that rates will fall in the future, so the more attractive bonds become and the less money people wish to hold speculatively. This generates the inverse relationship between speculative demand and the current interest rate.

Combining all three, the **aggregate money demand function** is written L(Y, i): demand for real money balances rises with real output Y (through transactions and precautionary motives) and falls with the nominal interest rate i (through the speculative motive). This function is the foundation for the LM curve in IS-LM analysis and for understanding monetary policy transmission. When the central bank changes the money supply, it shifts the equilibrium on the money market — and since money demand slopes downward in the interest rate, the adjustment clears through interest rate changes that then propagate to investment, consumption, and output. The three-motive framework thus connects the microeconomics of portfolio choice to the macroeconomics of monetary policy.
