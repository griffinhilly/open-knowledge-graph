---
id: method-overriding-and-dynamic-dispatch
title: Method Overriding and Polymorphism
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: inheritance-and-subclasses
  type: hard
- id: functions-defining-calling
  type: soft
builds-toward:
- abstract-classes-and-interfaces
tags:
- polymorphism
- overriding
- dynamic-dispatch
- OOP
- object-oriented
- super
stage: formal-systems
status: validated
---
# Method Overriding and Polymorphism

## Core Idea
A subclass can override an inherited method by defining a method with the same name and parameters. When the method is called, the version that runs is chosen by the actual type of the object at run time, not by the type of the variable that holds it. This run-time choice is called dynamic dispatch, and it is what makes subtype polymorphism work: one call such as `shape.area()` gives the right answer for a circle, a square or any future shape class.

## How It's Best Learned
Build a small hierarchy (Shape, Circle, Rectangle) where each subclass overrides `area()`, then loop over a mixed list and call `area()` on each item. Trace Java examples that separate the declared type from the actual type, such as `Shape s = new Circle(2);`, and ask which method runs and which calls the compiler accepts. Compare overriding with overloading side by side so the two terms do not blur.

## Common Misconceptions
- The variable's declared type decides which overridden method runs. (The object's actual run-time type decides; the declared type only decides which methods the compiler allows you to call.)
- Overriding and overloading mean the same thing. (Overriding replaces an inherited method with the same signature; overloading defines several methods with the same name but different parameter lists in one class.)
- Overriding a method deletes the superclass version. (The superclass version still exists and the subclass can call it with `super.method()` in Java or `super().method()` in Python.)

## Questions

```yaml
- question: "In Java, Dog extends Animal and overrides speak(). Animal's speak() returns \"...\" and Dog's returns \"Woof\". What does this code print?\n\nAnimal a = new Dog();\nSystem.out.println(a.speak());"
  type: multiple-choice
  options:
    - "..."
    - "Woof"
    - "Nothing, because the code does not compile"
    - "Both \"...\" and \"Woof\""
  answer: 1
  explanation: "The variable a has declared type Animal, but the object it refers to is a Dog. Java chooses an overridden instance method by the object's run-time type, so Dog's speak() runs and prints Woof. This is dynamic dispatch."

- question: "Continuing the example, Dog also defines a method fetch() that Animal does not have. What happens with this Java code?\n\nAnimal a = new Dog();\na.fetch();"
  type: multiple-choice
  options:
    - "It runs Dog's fetch(), because the object is a Dog"
    - "It runs Animal's fetch(), because the variable is an Animal"
    - "It causes a compile-time error, because Animal has no fetch() method"
    - "It compiles but always throws an exception at run time"
  answer: 2
  explanation: "The compiler checks method calls against the declared type of the variable. Animal has no fetch(), so the call is rejected before the program runs. The run-time type decides which version of a method runs only after the compiler has accepted the call. A cast, ((Dog) a).fetch(), would compile."

- question: "Writing two methods named area in the same class, one taking (double r) and one taking (double w, double h), is an example of overriding."
  type: true-false
  answer: false
  explanation: "Same name with different parameter lists in one class is overloading, and the compiler picks the version from the argument types. Overriding is a subclass redefining an inherited method with the same name and parameters."

- question: "A program stores Circle, Square and Triangle objects in one list of type Shape and computes the total area with a single loop that calls shape.area(). Explain why the loop needs no if-statements to check each object's type."
  type: short-answer
  answer: "Each subclass overrides area(). When the loop calls shape.area(), dynamic dispatch runs the version that belongs to the object's actual class, so each shape computes its own area. A new subclass such as Hexagon will work in the same loop without changing it."
  explanation: "This is the practical value of polymorphism: code written against the superclass works for every subclass, including ones written later, because method choice happens at run time."
```

## Explainer

From inheritance you know a subclass gets every method of its superclass. Sometimes the inherited behavior is wrong for the subclass. Every `Shape` might have an `area()` method, but a circle and a rectangle compute area differently. The subclass fixes this by **overriding**: it defines a method with the same name and the same parameters. In Java you can mark it with `@Override`, which asks the compiler to confirm that a matching superclass method really exists.

Overriding becomes powerful through **dynamic dispatch**. In Java you may write `Shape s = new Circle(2.0);`. The variable has declared type `Shape`, but the object is a `Circle`. When you call `s.area()`, Java looks at the object, finds that it is a `Circle`, and runs `Circle`'s `area()`. Python works the same way: the method is looked up on the object's class at the moment of the call.

Keep two questions apart. First, will the call compile? In Java, the compiler checks the declared type, so `s.area()` compiles only if `Shape` declares `area()`. Second, which version runs? That is decided at run time by the object's actual class. Students who mix these up expect `s.radius()` to compile because the object is a circle, or expect `Shape`'s `area()` to run because the variable says `Shape`.

This is **subtype polymorphism**, from Greek words meaning "many forms". A single line, `total += shape.area()`, gives the correct result for circles, squares and triangles. Better still, a programmer can add a `Hexagon` class next year and the same loop handles it without any edits. That is why large programs are often written against a superclass rather than against each concrete class.

An overriding method can still use the superclass version. In Java, `super.describe()` calls the parent's method. In Python, `super().describe()` does the same. A common pattern is to call the parent version and then add the subclass's extra detail.

Do not confuse overriding with **overloading**. Overloading means one class has several methods with the same name but different parameter lists, such as `print(int)` and `print(String)`. The compiler picks among overloads from the argument types at compile time. Overriding is chosen at run time from the object's type.
