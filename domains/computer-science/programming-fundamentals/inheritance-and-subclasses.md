---
id: inheritance-and-subclasses
title: Inheritance and Subclasses
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: intro-to-classes
  type: hard
- id: methods-and-attributes
  type: hard
- id: objects-and-instances
  type: soft
builds-toward:
- method-overriding-and-dynamic-dispatch
- abstract-classes-and-interfaces
tags:
- inheritance
- subclasses
- superclass
- OOP
- object-oriented
- code-reuse
stage: formal-systems
status: validated
---
# Inheritance and Subclasses

## Core Idea
Inheritance lets a new class (the subclass) be defined as an extension of an existing class (the superclass). The subclass automatically gets the superclass's attributes and methods, and it can add new ones of its own. Inheritance models an "is-a" relationship: a SavingsAccount is a BankAccount, so it should do everything a BankAccount does and possibly more. Shared code then lives in one place instead of being copied into every related class.

## How It's Best Learned
Start from two classes that share obvious duplicated code, such as Car and Truck that both track speed and fuel, and refactor the shared part into a Vehicle superclass. Trace object creation step by step to show that the subclass constructor must make sure the superclass part of the object is set up, using `super()`. Contrast "is-a" with "has-a" (composition) using concrete examples so students do not use inheritance for every relationship.

## Common Misconceptions
- A subclass is a copy of the superclass code. (The subclass reuses the superclass definition; a later change to a superclass method affects every subclass that does not replace it.)
- Inheritance should be used whenever two classes are related. (Use it only for "is-a" relationships; a Car has an Engine, so Engine belongs in a field, not in a superclass.)
- In Java, a subclass can read its superclass's private fields directly. (Private members are not accessible by name in the subclass; it must use the superclass's public or protected methods.)
- Constructors are inherited like other methods. (In Java, constructors are not inherited; a subclass constructor calls the superclass constructor with `super(...)`.)

## Questions

```yaml
- question: "Which pair of classes is the best fit for an inheritance (superclass/subclass) relationship?"
  type: multiple-choice
  options:
    - "Car and Engine"
    - "Library and Book"
    - "Shape and Circle"
    - "Student and Classroom"
  answer: 2
  explanation: "Inheritance models an 'is-a' relationship. A Circle is a Shape, so Circle can extend Shape. A Car has an Engine, a Library has Books, and a Classroom has Students; those are 'has-a' relationships, which are modeled by storing one object inside another (composition), not by inheritance."

- question: "In Python, class Animal has an __init__ that sets self.name. Class Dog(Animal) defines its own __init__(self, name, breed) that sets only self.breed and never calls super().__init__(name). What happens when code later reads my_dog.name?"
  type: multiple-choice
  options:
    - "It returns the name, because Dog inherits Animal's attributes automatically"
    - "It raises an AttributeError, because Animal's __init__ never ran, so name was never set"
    - "It returns None, because inherited attributes default to None"
    - "It returns the breed, because Dog's __init__ replaces name with breed"
  answer: 1
  explanation: "Defining __init__ in Dog replaces Animal's __init__ for Dog objects. Attributes in Python are created when code assigns them, so if Animal's __init__ never runs, self.name is never assigned. Calling super().__init__(name) inside Dog's __init__ runs the superclass setup and fixes the problem."

- question: "In Java, a subclass can directly read and assign a private instance variable declared in its superclass."
  type: true-false
  answer: false
  explanation: "Private members are visible only inside the class that declares them. A subclass object still contains that data, but subclass code must reach it through the superclass's public or protected methods (or a protected field), not by name."

- question: "Two classes, Teacher and Student, both store a name and an email address and both have an identical send_email method. Explain how inheritance improves this design."
  type: short-answer
  answer: "Create a superclass such as Person that holds name, email and send_email. Teacher and Student then extend Person and add only what is specific to each. The shared code exists once, so a bug fix or change to send_email happens in one place and applies to both subclasses."
  explanation: "Removing duplicated code is the main practical benefit of inheritance. It also passes the 'is-a' test: a Teacher is a Person and a Student is a Person."
```

## Explainer

You already know how to write a class with attributes and methods. Now suppose you write a `BankAccount` class with a balance, a `deposit` method and a `withdraw` method. Later you need a `SavingsAccount` that does all of that and also earns interest. Copying the whole class and adding one method would work, but then every bug fix must be made twice. Inheritance solves this.

In Python you write `class SavingsAccount(BankAccount):`. In Java you write `class SavingsAccount extends BankAccount`. `BankAccount` is the **superclass** (also called the parent or base class) and `SavingsAccount` is the **subclass** (child or derived class). A `SavingsAccount` object can call `deposit` and `withdraw` even though the subclass never defines them, because it inherits them. The subclass adds only what is new, such as an `interest_rate` attribute and an `add_interest` method.

Construction needs care. A subclass object contains a superclass part, and that part must be set up too. In Python, the subclass `__init__` usually begins with `super().__init__(owner, balance)` and then sets its own attributes. In Java, the subclass constructor calls `super(owner, balance)`. Before Java 25 that call had to be the first statement; Java 25 allows some statements before it, but they cannot use the object being built. If a Java subclass constructor has no explicit `super(...)` call, the compiler inserts a call to the superclass's no-argument constructor.

The test for using inheritance is the **"is-a" rule**. A savings account is a bank account, so inheritance fits. A car has an engine, but a car is not an engine, so the engine should be an attribute of the car. Storing one object inside another is called **composition**, and it models "has-a" relationships.

Inheritance can be chained: `Animal` to `Mammal` to `Dog`. Each level inherits everything above it. In Java every class ultimately extends `Object`, and in Python 3 every class ultimately inherits from `object`. That is why even a brand-new class already has some methods, such as `toString()` in Java or `__str__` in Python.

Inheritance is also the base for the next idea. A subclass can replace an inherited method with its own version. That is called overriding, and it lets one line of code behave differently depending on the type of object it runs on.
