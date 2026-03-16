---
id: attribute-grammar-framework
title: Attribute Grammar Framework
domain: computer-science
course: compilers
prerequisites:
- id: ast-node-representation
  type: hard
- id: parse-trees-derivations
  type: soft
builds-toward:
- semantic-error-detection-reporting
tags:
- semantic-analysis
- attributes
- grammars
stage: advanced
status: draft
---

# Attribute Grammar Framework

## Core Idea
Attribute grammars associate attributes (semantic values) with grammar symbols and define rules for computing attributes. Synthesized attributes are computed from children; inherited attributes from parents. This framework elegantly separates parsing from semantic analysis.

## How It's Best Learned
Write attribute grammars for a small language using tools like Antlr. Implement both bottom-up and top-down attribute evaluators.

## Common Misconceptions
Attribute grammars are the only way to do semantic analysis (they are one useful approach; ad-hoc traversal is simpler for many tasks). All attributes must be computed in one pass (multiple passes can be clearer).

## Explainer

You know from parse trees and ASTs that parsing gives you the syntactic structure of a program — which tokens group together and how. But syntax alone cannot answer questions like "is this variable declared?" or "do the types in this expression match?" These are **semantic** questions, and attribute grammars provide a formal framework for computing semantic information directly on the parse tree. The idea is to attach **attributes** — named values like types, scope levels, or computed results — to grammar symbols, and define rules that specify how to compute each attribute from other attributes in the tree.

There are two kinds of attributes, and the distinction matters for evaluation order. **Synthesized attributes** flow upward: a parent node's attribute is computed from its children's attributes. Think of evaluating an arithmetic expression tree — the value of an addition node is synthesized from the values of its left and right children. **Inherited attributes** flow downward or sideways: a child's attribute is computed from its parent or siblings. For example, a declaration like `int x, y, z;` might have the type `int` as an inherited attribute that flows from the type specifier down to each variable in the list. A grammar where every attribute is synthesized is called an **S-attributed grammar** and can be evaluated in a single bottom-up pass. When inherited attributes are involved, you need an **L-attributed grammar** (where inherited attributes depend only on left siblings and the parent), which can still be evaluated left-to-right in a single pass.

Consider a concrete example: type checking in a simple expression language. You might attach a `type` synthesized attribute to every expression node. For a rule like `Expr → Expr₁ + Expr₂`, the semantic rule says: if both children have type `int`, the result has type `int`; if both are `float`, the result is `float`; if one is `int` and the other `float`, insert a coercion and the result is `float`; otherwise, it is a type error. Each production in the grammar gets its own set of semantic rules, and together they define how type information propagates through the entire tree. The attribute grammar framework makes these rules explicit and composable rather than scattered through ad-hoc visitor code.

In practice, many compilers use ad-hoc AST traversals instead of formal attribute grammar tools, because the framework can feel heavyweight for simple analyses. But the conceptual model remains valuable even when the implementation is informal. Thinking in terms of synthesized and inherited attributes clarifies the information flow in any semantic analysis pass: what information do you need from children (synthesize it), and what information must come from context (inherit it). This mental model helps you design clean, predictable compiler passes whether or not you use a formal attribute grammar evaluator.
