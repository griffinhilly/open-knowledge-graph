---
id: testing-and-improving
title: Testing and Improving
domain: engineering
course: design-and-build
prerequisites:
- id: building-prototypes
  type: hard
- id: engineering-design-process
  type: soft
builds-toward:
- combining-simple-machines
- materials-and-strength-testing
tags:
- engineering
- design-process
- testing
- iteration
stage: concrete-operations
status: validated
---
# Testing and Improving

## Core Idea
Testing means trying out a prototype to see if it actually solves the problem, and improving means using what you learned from testing to make the design better. Good testing is fair and specific: you test one thing at a time, measure the results, and compare them to your goal. When something does not work, you do not throw away the whole design — you figure out exactly what failed and fix just that part. This cycle of test-learn-improve is called iteration, and it is the engine of engineering. The best designs are not the ones that worked perfectly the first time; they are the ones that were improved the most times.

## How It's Best Learned
After students build prototypes, have them write down what they expect will happen before testing (a prediction). Then test and record actual results. Compare prediction to reality — the gap is where learning happens. Require students to identify one specific thing to change (not "make it better" but "make the base wider so it does not tip"). Then rebuild, retest, and compare. Two or three rounds of this cycle teach the iterative mindset better than any lecture.

## Common Misconceptions
- If something fails, start over from scratch. (Most of the time, you only need to change one or two things. Starting over wastes the good parts of your design.)
- Testing means just trying it once to see if it works. (Good testing means testing multiple times, testing specific features, and measuring results — not just a single pass/fail check.)
- A good engineer gets things right on the first try. (No engineer does. Iteration is not a sign of failure; it is the standard process.)
- Improving means changing everything. (Good improvement is targeted — change one thing at a time so you know what actually helped.)

## Questions

```yaml
- question: "Your paper bridge held 15 pennies but your goal was 30. What is the best next step?"
  type: multiple-choice
  options: ["Give up because the design failed", "Build a completely different bridge from scratch", "Look at where the bridge bent or broke, change that part, and test again", "Add more pennies and hope it holds"]
  answer: 2
  explanation: "The bridge held 15 pennies — it is halfway to the goal, not a failure. The smart engineering move is to observe where it bent or broke, strengthen that specific part, and retest. Starting over throws away the parts that already worked. Adding more pennies without changing anything will just break the bridge."

- question: "When improving a design, you should change as many things as possible at once to save time."
  type: true-false
  answer: false
  explanation: "If you change five things at once and the design gets better, you do not know which change helped — and some of the changes might have actually made things worse but were hidden by the one good change. Change one thing at a time, test, and see the effect. This is slower per round but much faster overall because you learn what actually works."

- question: "Why is it important to write down your test results instead of just remembering them?"
  type: short-answer
  answer: "Written records let you compare results across multiple tests accurately. Memory is unreliable — you might forget how the first version performed by the time you are testing the third version. Written data helps you see whether each change actually improved the design."
  explanation: "Engineering is evidence-based. Without written records, you are relying on feelings and impressions, which can be misleading. A simple table showing 'version 1 held 15 pennies, version 2 held 22 pennies, version 3 held 31 pennies' tells a clear story of improvement that memory alone cannot provide."
```

## Explainer
You have built a prototype. Now comes the moment of truth: **does it actually work?** Testing answers this question, but good testing is more specific than just "try it and see." Good testing means deciding *what* you are testing, *how* you will measure success, and *what* you will do with the results.

Before you test, write down your **prediction**: what do you think will happen? Maybe your bridge prototype will hold 25 pennies, or your egg drop container will survive a three-foot fall. Having a prediction before testing forces you to think carefully about your design, and comparing prediction to reality is where the most learning happens. If your bridge held 25 pennies and you predicted 25, great — your understanding matches reality. If it held only 8, something important is different from what you expected, and figuring out what teaches you more than success would.

When your prototype does not meet the goal — and it usually will not on the first try — the next step is not to throw it away. The next step is to **observe carefully**. Where exactly did it fail? Did the bridge bend in the middle or collapse at the ends? Did the egg container crack on one side? The location and type of failure tells you exactly what to fix. If the bridge bent in the middle, you need to add support there. If it collapsed at the ends, the connections need to be stronger. A specific diagnosis leads to a specific fix.

Now comes **improvement**: change one thing, rebuild that part, and test again. The key rule is to change **one thing at a time**. If you change the material, the shape, and the size all at once, and the design gets better, you have no idea which change helped. Maybe two of the three changes actually made things worse, but the third one was so good it compensated. By changing one variable at a time, you learn what actually matters.

This cycle — test, observe, diagnose, fix, retest — is called **iteration**, and it is the most powerful idea in engineering. Every product you use daily went through this cycle many times. Your phone, your sneakers, your bicycle — none of them worked well in their first version. They were tested, broken, fixed, tested again, broken again, and fixed again until they were good enough to use. The best engineers are not the ones who get it right the first time. They are the ones who learn the most from each round of testing.
