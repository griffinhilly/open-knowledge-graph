---
id: objects-and-instances
title: Objects and Instances
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: intro-to-classes
  type: hard
builds-toward:
- methods-and-attributes
tags:
- objects
- instances
- instantiation
- constructors
- __init__
stage: abstract-reasoning
status: validated
---

# Objects and Instances

## Core Idea
An object is a specific instance of a class, created by calling the class as a function (e.g., obj = MyClass()). The constructor method (__init__ in Python, or similar in other languages) runs automatically at instantiation to initialize the object's attributes. Each instance maintains its own independent copy of instance attributes, even though all instances share the class's method definitions. Objects are the fundamental unit of computation in object-oriented programs.

## How It's Best Learned
Create multiple instances of the same class with different initial data and print their attributes. Modify one instance's attribute and verify the other is unaffected. Step through a constructor call in a debugger.

## Common Misconceptions
- Thinking instances share attribute values — each has its own.
- Calling __init__ explicitly rather than letting instantiation trigger it.
- Confusing class attributes (shared across all instances) with instance attributes (unique per object).

## Questions

```yaml
- question: "Consider this code: dog1 = Dog('Rex', 5); dog2 = Dog('Luna', 3); dog1.age = 10. After these three lines run, what is dog2.age?"
  type: multiple-choice
  options:
    - "10, because dog1 and dog2 are instances of the same class and share attribute values"
    - "3, because each instance maintains its own independent copy of its instance attributes"
    - "None, because the age attribute was modified and no longer has a valid value"
    - "5, because dog2 was created before dog1's age was changed"
  answer: 1
  explanation: "Each instance occupies separate memory and owns its own copy of instance attributes. Modifying dog1.age = 10 changes only the slot in dog1's memory — dog2 has an entirely separate age slot that remains 3. This is the core concept: instances are like two houses built from the same blueprint — painting one house does not change the other's color. The most common misconception (option A) treats instances as sharing a single set of values, which would make OOP far less useful."

- question: "A student writes 'dog1.__init__(\"Rex\", 5)' to manually set up a dog object's attributes after creating it. Why is this the wrong approach?"
  type: multiple-choice
  options:
    - "Because __init__ does not accept arguments in Python"
    - "Because __init__ is called automatically when you instantiate the class — calling it explicitly would run initialization twice and bypasses the intended creation pattern"
    - "Because constructors can only be invoked by the Python interpreter, never directly by user code"
    - "Because you must use the Dog() syntax and cannot call __init__ with dot notation"
  answer: 1
  explanation: "When you write dog1 = Dog('Rex', 5), Python automatically calls __init__(self, 'Rex', 5) on the newly created object. You do not need to call __init__ again — and doing so would run the initialization logic a second time on an already-initialized object. The constructor's purpose is to set up the object the moment it comes into existence, triggered by instantiation. Calling __init__ manually after the fact is like using a house blueprint to redecorate a house that's already been fully built."

- question: "All instances of the same class share the class's method definitions, but each instance has its own independent copy of its instance attributes."
  type: true-false
  answer: true
  explanation: "Method definitions (like bark, fetch, __init__) live in the class itself — there is one copy shared by all instances, which is efficient. When you call my_dog.bark(), Python looks up bark in the Dog class and runs it with self = my_dog. But instance attributes (name, age) are stored in each instance's own memory. This design — shared behavior, independent data — is what makes object-oriented programming powerful: the same code operates on each object's specific state."

- question: "When you call a method on an object (e.g., my_dog.bark()), Python stores a separate copy of the bark method in the instance's memory for each invocation."
  type: true-false
  answer: false
  explanation: "Methods are stored once in the class definition and looked up there at call time — no copy is made in the instance's memory. Python passes the instance as the implicit first argument (self), allowing the method to access that instance's attributes. This lookup-at-call-time behavior is part of Python's descriptor protocol. Storing methods in each instance would waste memory and defeat the purpose of class-based organization. Only instance attributes (set via self.x = ...) are stored in the instance's own namespace."

- question: "What is the difference between a class and an instance, and why does this distinction matter when you modify an attribute on one instance?"
  type: short-answer
  answer: "A class is the blueprint — it defines the structure (what attributes objects will have) and the shared behavior (method definitions). An instance is a concrete object created from that blueprint, holding its own memory with its own attribute values. Because instances own their data independently, modifying dog1.age only changes that specific object's age slot in memory; dog2 has a completely separate age slot that is unaffected. The class is shared; the data is not. This independence is what allows multiple objects to represent distinct real-world entities even though they were built from the same template."
  explanation: "The class/instance distinction is foundational to all object-oriented design. As programs grow more complex — a Veterinarian examining a Dog, a Kennel holding a list of Dogs — each object needs to maintain its own state independently. If instances shared attribute values, you could not model multiple distinct dogs (or patients, or bank accounts) simultaneously. The blueprint/house analogy captures this: one blueprint, many independent houses."
```

## Explainer

You have learned that a class is a blueprint — it defines what attributes an object will have and what methods it can perform. But a blueprint is not a house. An **object** (or **instance**) is a specific, concrete thing created from that blueprint, with its own particular data. When you write `my_dog = Dog("Rex", 5)`, you are calling the Dog class to create one specific dog object with the name "Rex" and age 5. You can create as many instances as you want from the same class, each with different data: `another_dog = Dog("Luna", 3)` is a completely separate object that happens to share the same structure.

The creation process — called **instantiation** — triggers a special method known as the **constructor**. In Python, this is `__init__`. When you call `Dog("Rex", 5)`, Python first allocates memory for a new object, then calls `__init__(self, name, age)` with `self` pointing to that fresh object. Inside `__init__`, you assign the passed-in values to instance attributes: `self.name = "Rex"` and `self.age = 5`. The constructor's job is to put the new object into a valid initial state so it is ready to use. Every attribute you want the object to carry should be set up here.

The crucial concept is that each instance maintains **independent copies** of its instance attributes. If you change `my_dog.age = 6`, `another_dog.age` remains 3. They are separate objects occupying separate memory, like two houses built from the same blueprint — painting one house red does not change the color of the other. However, both instances share the same **method definitions** from the class. When you call `my_dog.bark()`, Python looks up the `bark` method in the Dog class (not in the instance) and runs it with `self` set to `my_dog`. This sharing of methods is efficient: the code exists in one place, but each call operates on the specific instance's data.

Understanding the distinction between the class and its instances is the foundation of object-oriented thinking. The class is the abstract description — Dog has a name and an age and can bark. Each instance is a concrete realization — this particular dog is Rex, age 5. As you build more complex programs, you will create objects that interact with each other: a Veterinarian object that examines a Dog object, a Kennel object that holds a list of Dog objects. The power of objects is that they bundle data and behavior together into self-contained units that model the entities in your problem domain.
