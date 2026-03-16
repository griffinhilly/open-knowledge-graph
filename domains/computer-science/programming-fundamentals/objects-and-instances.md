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

## Explainer

You have learned that a class is a blueprint — it defines what attributes an object will have and what methods it can perform. But a blueprint is not a house. An **object** (or **instance**) is a specific, concrete thing created from that blueprint, with its own particular data. When you write `my_dog = Dog("Rex", 5)`, you are calling the Dog class to create one specific dog object with the name "Rex" and age 5. You can create as many instances as you want from the same class, each with different data: `another_dog = Dog("Luna", 3)` is a completely separate object that happens to share the same structure.

The creation process — called **instantiation** — triggers a special method known as the **constructor**. In Python, this is `__init__`. When you call `Dog("Rex", 5)`, Python first allocates memory for a new object, then calls `__init__(self, name, age)` with `self` pointing to that fresh object. Inside `__init__`, you assign the passed-in values to instance attributes: `self.name = "Rex"` and `self.age = 5`. The constructor's job is to put the new object into a valid initial state so it is ready to use. Every attribute you want the object to carry should be set up here.

The crucial concept is that each instance maintains **independent copies** of its instance attributes. If you change `my_dog.age = 6`, `another_dog.age` remains 3. They are separate objects occupying separate memory, like two houses built from the same blueprint — painting one house red does not change the color of the other. However, both instances share the same **method definitions** from the class. When you call `my_dog.bark()`, Python looks up the `bark` method in the Dog class (not in the instance) and runs it with `self` set to `my_dog`. This sharing of methods is efficient: the code exists in one place, but each call operates on the specific instance's data.

Understanding the distinction between the class and its instances is the foundation of object-oriented thinking. The class is the abstract description — Dog has a name and an age and can bark. Each instance is a concrete realization — this particular dog is Rex, age 5. As you build more complex programs, you will create objects that interact with each other: a Veterinarian object that examines a Dog object, a Kennel object that holds a list of Dog objects. The power of objects is that they bundle data and behavior together into self-contained units that model the entities in your problem domain.
