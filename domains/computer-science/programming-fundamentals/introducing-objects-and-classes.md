---
id: introducing-objects-and-classes
title: Introducing Objects and Classes
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: intro-to-classes
  type: hard
builds-toward:
- methods-objects-and-messages
- object-oriented-thinking-and-design
tags:
- objects
- classes
- oop
stage: formal-systems
status: draft
---

# Introducing Objects and Classes

## Core Idea
A class is a blueprint for objects. An object is an instance of a class containing data (attributes) and behavior (methods). Creating objects enables modeling real-world entities and their relationships in code.

## How It's Best Learned
Define simple classes with attributes and methods; create multiple instances; modify instance data and verify independence; trace method calls to understand behavior.

## Common Misconceptions
That classes and objects are the same (classes are blueprints, objects are instances); that a class needs every method of its instances (shared methods can be defined once); that modifying one object's data changes other objects (each instance has its own data).

## Questions

```yaml
- question: "A programmer runs the following code:\n\n    dog1 = Dog('Rex', 'Labrador', 3)\n    dog2 = Dog('Luna', 'Poodle', 5)\n    dog1.age = 7\n\nWhat is the value of dog2.age after this code executes?"
  type: multiple-choice
  options:
    - "7 — because both objects were created from the same Dog class and share their data"
    - "5 — because each object has its own independent copy of its attributes"
    - "3 — because dog2 inherits its initial values from dog1"
    - "The code raises an error because you cannot modify object attributes directly"
  answer: 1
  explanation: "Each object created from a class is an independent instance with its own copy of the attributes. When you write dog1.age = 7, you are modifying only dog1's age attribute. dog2 was created separately and has its own age — which remains 5. This independence of instances is fundamental: the class is a shared blueprint, but each object's data is its own. A common misconception is that because both objects came from the same class, they somehow share state."

- question: "A class Dog defines a bark() method. A programmer creates 50 Dog objects. How many copies of the bark() method exist in memory?"
  type: multiple-choice
  options:
    - "50 — one copy per object instance, so each dog has its own bark"
    - "1 — the method is defined once in the class and shared by all instances"
    - "0 — methods must be attached to each object individually after creation"
    - "2 — one original in the class definition and one shared runtime copy"
  answer: 1
  explanation: "Methods are defined in the class and shared by all instances — only one copy of bark() exists in memory, no matter how many Dog objects are created. When you call my_dog.bark(), the language looks up bark on the Dog class and runs it with my_dog as the target. This is the efficiency of object-oriented design: behavior is defined once and reused by every instance. Only the data (attributes like name, age) is stored separately per instance."

- question: "When you create a new object using a class constructor, that object is completely independent — modifying its attributes does not affect other objects created from the same class."
  type: true-false
  answer: true
  explanation: "This is the independence of instances. The constructor allocates a new object in memory, initializes its attributes, and returns it. From that point, the object lives independently. Changing one Dog's age attribute does not affect any other Dog object. This makes object-oriented programs predictable: each object encapsulates its own state, and changes to one cannot unexpectedly alter another."

- question: "You can use a class directly as an object — storing data in it and calling its methods — without needing to create instances."
  type: true-false
  answer: false
  explanation: "A class is a blueprint, not an object. Using the cookie-cutter analogy: you cannot eat the cutter — you must stamp out a cookie first. The class defines what attributes and methods instances will have, but the class itself does not hold instance data. You must call the constructor (e.g., Dog('Rex', 'Labrador', 3)) to create an actual object in memory before you can store data or call instance methods. (Note: some languages support class-level or static attributes and methods, but these are advanced features that do not change the basic class-vs-instance distinction.)"

- question: "Explain the difference between a class and an object using the cookie-cutter analogy. Why is it important that each object instance has its own independent copy of its attributes?"
  type: short-answer
  answer: "A class is like a cookie cutter: it defines the shape and structure (what attributes and methods every instance will have), but the cutter itself is not a cookie — you cannot use it directly. An object (instance) is a cookie stamped from that cutter: a real, independent thing in memory with its own data. Independence matters because it means each object maintains its own state without interfering with others. If all instances shared data, modifying one Dog's name would change every Dog's name — making it impossible to represent multiple distinct entities of the same type."
  explanation: "This independence is what makes OOP practical for modeling real-world problems. You can create a list of 100 Student objects, each with a different name and GPA, all sharing the Student class's methods. The class defines the structure once; instances are the actual things. The constructor is what creates each new independent cookie from the cutter, initializing its attributes with the specific values passed in."
```

## Explainer

You have already encountered the idea that a class defines a template. Now let's make that concrete. Think of a class as a cookie cutter and objects as the cookies. The cookie cutter defines the shape — what attributes every cookie will have and what methods it can perform — but the cookie cutter itself is not a cookie. You cannot eat the cutter. You use it to *stamp out* individual cookies, each of which is a real, independent thing with its own data.

Consider a `Dog` class. The class says every dog has a `name`, a `breed`, and an `age`, and every dog can `bark()` and `fetch()`. When you write `my_dog = Dog("Rex", "Labrador", 3)`, you are creating an **instance** — a specific dog object with its own name, breed, and age stored in memory. If you create `your_dog = Dog("Luna", "Poodle", 5)`, that is a second, completely independent object. Changing `my_dog.age = 4` does not affect `your_dog.age` — each object carries its own copy of the attributes. The methods, however, are defined once in the class and shared by all instances. When you call `my_dog.bark()`, Python (or whatever language you are using) looks up the `bark` method on the `Dog` class and runs it with `my_dog` as the target object.

This pattern — bundling data and behavior together into objects — lets you model problems in a way that mirrors how you think about the real world. A bank account has a balance and can accept deposits. A student has a GPA and can enroll in courses. A game character has hit points and can attack. In each case, the class defines the *kind* of thing, and objects are the *specific* things. You can have a list of a hundred `Student` objects, each with different names and GPAs, all sharing the same set of methods defined once in the `Student` class.

The most important thing to internalize at this stage is the distinction between the class (the blueprint) and its instances (the objects). When you call the class like a function — `Dog("Rex", "Labrador", 3)` — you are invoking the **constructor**, which allocates a new object, initializes its attributes, and returns it. From that point on, the object lives independently in memory. You can pass it to functions, store it in lists, and modify its attributes without affecting any other object. This independence of instances is what makes object-oriented code powerful: each object encapsulates its own state and exposes its behavior through methods.
