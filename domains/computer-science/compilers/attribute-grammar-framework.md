---
id: attribute-grammar-framework
title: Attribute Grammar Framework
domain: computer-science
course: compilers
prerequisites:
- id: abstract-syntax-trees
  type: hard
- id: parse-trees-ambiguity-and-derivation
  type: soft
builds-toward:
- semantic-analysis
tags:
- semantic-analysis
- attributes
- grammars
stage: advanced
status: validated
---

# Attribute Grammar Framework

## Core Idea
Attribute grammars associate attributes (semantic values) with grammar symbols and define rules for computing attributes. Synthesized attributes are computed from children; inherited attributes from parents. This framework elegantly separates parsing from semantic analysis.

## How It's Best Learned
Write attribute grammars for a small language using tools like Antlr. Implement both bottom-up and top-down attribute evaluators.

## Common Misconceptions
Attribute grammars are the only way to do semantic analysis (they are one useful approach; ad-hoc traversal is simpler for many tasks). All attributes must be computed in one pass (multiple passes can be clearer).

## Questions

```yaml
- question: "In a compiler implementing type checking, the rule 'Expr → Expr₁ + Expr₂' computes the type of the parent Expr from the types of its two children. This is an example of:"
  type: multiple-choice
  options:
    - "An inherited attribute, because type information flows from the expression node to its children"
    - "A synthesized attribute, because the parent's value is computed from its children's values"
    - "A synthesized attribute, because type checking always flows upward in the AST"
    - "An inherited attribute, because the grammar rule defines the parent's type"
  answer: 1
  explanation: "A synthesized attribute is computed from the attributes of children and flows upward to the parent. Here the parent Expr's type is computed from Expr₁.type and Expr₂.type — a classic synthesized attribute. Option A reverses the direction: inherited attributes flow downward from parent to children. Option C has the right answer but the wrong reasoning; synthesized attributes flow up, but not all upward-flowing information is about type checking specifically."

- question: "A grammar rule declares 'int x, y, z;' where the type 'int' must be propagated to each variable in the declarator list. This type-propagation attribute is most naturally represented as:"
  type: multiple-choice
  options:
    - "A synthesized attribute computed bottom-up from the variable names"
    - "An inherited attribute passed down from the type specifier to each variable"
    - "A synthesized attribute, because the type is determined once and flows to later uses"
    - "An inherited attribute that flows from z back toward x through the sibling list"
  answer: 1
  explanation: "The type 'int' is known at the type-specifier node (a parent or left sibling) and needs to flow DOWN to each variable in the list — this is a classic inherited attribute. Synthesized attributes flow upward from children; inherited attributes flow downward from parents or from left siblings. Option D describes an impossible direction: inherited attributes can flow from parents or left siblings (in L-attributed grammars) but not from right siblings back to left ones."

- question: "A grammar where nearly every attribute is synthesized (S-attributed) can be evaluated in a single top-down pass over the parse tree."
  type: true-false
  answer: false
  explanation: "S-attributed grammars are evaluated in a single BOTTOM-UP pass, not top-down. Because synthesized attributes flow upward (children to parent), you must evaluate children before their parents. In a bottom-up traversal, you process leaves first and work toward the root — which is exactly the right order. A top-down (root-first) pass would try to compute parents before their children's values are known."

- question: "In an L-attributed grammar, an attribute on a node can depend on the attributes of its right siblings."
  type: true-false
  answer: false
  explanation: "L-attributed grammars allow inherited attributes to depend only on the PARENT's attributes and on LEFT siblings' attributes (already processed in a left-to-right traversal). Dependence on right siblings would require knowing those attributes before they've been processed, violating the left-to-right evaluation order. This restriction is precisely what allows L-attributed grammars to be evaluated in a single left-to-right pass — making them compatible with top-down parsing."

- question: "What is the practical difference between a synthesized and an inherited attribute, and why does this distinction affect how you can evaluate a grammar in a single pass?"
  type: short-answer
  answer: "A synthesized attribute is computed from a node's children and flows upward to the parent; it can be evaluated in a single bottom-up pass because children are always ready before their parents. An inherited attribute is computed from a node's parent or left siblings and flows downward; it requires that context above or to the left already be processed. When a grammar mixes both, the evaluation order must respect all dependencies — which may require multiple passes or a carefully constrained dependency structure (like L-attributed grammars) to ensure a single pass remains possible."
  explanation: "The distinction directly determines pass structure. Pure synthesized (S-attributed): one bottom-up pass. Mixed with inherited but L-attributed: one left-to-right pass. Arbitrary inherited attributes with cycles or right-sibling dependencies: multiple passes or might be unevaluable. Compiler designers care because one-pass evaluation is fast and simple; multi-pass evaluation adds complexity."
```

## Explainer

You know from parse trees and ASTs that parsing gives you the syntactic structure of a program — which tokens group together and how. But syntax alone cannot answer questions like "is this variable declared?" or "do the types in this expression match?" These are **semantic** questions, and attribute grammars provide a formal framework for computing semantic information directly on the parse tree. The idea is to attach **attributes** — named values like types, scope levels, or computed results — to grammar symbols, and define rules that specify how to compute each attribute from other attributes in the tree.

There are two kinds of attributes, and the distinction matters for evaluation order. **Synthesized attributes** flow upward: a parent node's attribute is computed from its children's attributes. Think of evaluating an arithmetic expression tree — the value of an addition node is synthesized from the values of its left and right children. **Inherited attributes** flow downward or sideways: a child's attribute is computed from its parent or siblings. For example, a declaration like `int x, y, z;` might have the type `int` as an inherited attribute that flows from the type specifier down to each variable in the list. A grammar where every attribute is synthesized is called an **S-attributed grammar** and can be evaluated in a single bottom-up pass. When inherited attributes are involved, you need an **L-attributed grammar** (where inherited attributes depend only on left siblings and the parent), which can still be evaluated left-to-right in a single pass.

Consider a concrete example: type checking in a simple expression language. You might attach a `type` synthesized attribute to every expression node. For a rule like `Expr → Expr₁ + Expr₂`, the semantic rule says: if both children have type `int`, the result has type `int`; if both are `float`, the result is `float`; if one is `int` and the other `float`, insert a coercion and the result is `float`; otherwise, it is a type error. Each production in the grammar gets its own set of semantic rules, and together they define how type information propagates through the entire tree. The attribute grammar framework makes these rules explicit and composable rather than scattered through ad-hoc visitor code.

In practice, many compilers use ad-hoc AST traversals instead of formal attribute grammar tools, because the framework can feel heavyweight for simple analyses. But the conceptual model remains valuable even when the implementation is informal. Thinking in terms of synthesized and inherited attributes clarifies the information flow in any semantic analysis pass: what information do you need from children (synthesize it), and what information must come from context (inherit it). This mental model helps you design clean, predictable compiler passes whether or not you use a formal attribute grammar evaluator.
