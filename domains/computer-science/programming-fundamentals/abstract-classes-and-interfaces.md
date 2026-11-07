---
id: abstract-classes-and-interfaces
title: Abstract Classes and Interfaces
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: inheritance-and-subclasses
  type: hard
- id: method-overriding-and-dynamic-dispatch
  type: hard
- id: function-design-and-contracts
  type: soft
builds-toward: []
tags:
- abstract-classes
- interfaces
- OOP
- object-oriented
- abstraction
- contracts
stage: formal-systems
status: validated
---
# Abstract Classes and Interfaces

## Core Idea
An abstract class is a class that cannot be instantiated and may declare abstract methods, which have a name and parameters but no body. Every concrete subclass must supply bodies for those methods. An interface goes further: it names a set of methods that any class can promise to provide, without saying how. Both tools let code depend on what an object can do rather than on which exact class it belongs to.

## How It's Best Learned
Start with a Shape superclass whose `area()` has no sensible default, and show that making it abstract stops anyone from creating a plain Shape. Then introduce a Java interface such as `Comparable` and show that unrelated classes (Student, Song, Date) can all be sorted by the same library method once they implement it. Finish by asking students to choose between an abstract class and an interface for a few small designs and to defend the choice.

## Common Misconceptions
- An abstract class cannot contain any code. (It can have fields, constructors and fully written methods; only the methods marked abstract lack bodies.)
- A Java class can extend several abstract classes if it needs their methods. (A Java class extends at most one class, abstract or not, but it can implement any number of interfaces.)
- Interfaces are just a weaker kind of inheritance and are rarely needed. (Interfaces let unrelated classes share a type, which is how library code such as sorting works on objects it has never seen.)

## Questions

```yaml
- question: "In Java, Shape is declared as `public abstract class Shape` with an abstract method area(). What happens with the statement `Shape s = new Shape();`?"
  type: multiple-choice
  options:
    - "It creates a Shape whose area() returns 0"
    - "It compiles, but calling s.area() throws an exception"
    - "It does not compile, because an abstract class cannot be instantiated"
    - "It creates an object of the first subclass of Shape"
  answer: 2
  explanation: "The abstract keyword tells the compiler that Shape is incomplete, so new Shape() is rejected at compile time. A variable of type Shape is still allowed: Shape s = new Circle(1.0); compiles if Circle is a concrete subclass."

- question: "Circle extends the abstract class Shape but does not provide a body for Shape's abstract method area(), and Circle is not itself marked abstract. What does the Java compiler do?"
  type: multiple-choice
  options:
    - "It reports an error, because a concrete class must implement every inherited abstract method"
    - "It accepts the class and uses an empty area() method"
    - "It accepts the class and makes area() return 0.0"
    - "It accepts the class but prevents Circle objects from calling area()"
  answer: 0
  explanation: "A non-abstract class must provide bodies for all abstract methods it inherits. Circle must either implement area() or be declared abstract itself, in which case its own subclasses must implement it."

- question: "A single Java class can implement more than one interface."
  type: true-false
  answer: true
  explanation: "Java allows a class to extend only one superclass, but it can implement many interfaces, for example `class Song implements Comparable<Song>, Serializable`. This is how a class can belong to several unrelated types at once."

- question: "You are designing classes Dog, Cat and Robot. All three must provide a method makeSound(). Dog and Cat also share name and age fields with identical code. Which tools would you use, and why?"
  type: short-answer
  answer: "Put the shared fields and code in an abstract class such as Animal that Dog and Cat extend. Define an interface such as SoundMaker with makeSound(), and have Animal (or Dog and Cat) and Robot implement it. Robot is not an animal, so it should not extend Animal, but it can still share the SoundMaker type."
  explanation: "Abstract classes are a good fit when related classes share state and code in an 'is-a' family. Interfaces are a good fit when unrelated classes need to promise the same capability."
```

## Explainer

From polymorphism you know that code like `shape.area()` runs the right version for each subclass. But what should `area()` do in the `Shape` class itself? There is no correct formula for a generic shape. Returning 0 would hide bugs. An **abstract class** solves this. In Java you write `public abstract class Shape` and declare `public abstract double area();` with a semicolon instead of a body. Two rules follow. No one can write `new Shape()`. And every concrete subclass, such as `Circle`, must provide a body for `area()`, or the compiler refuses it.

An abstract class is still a real class. It can hold fields such as `color`, a constructor that sets them, and finished methods such as `describe()` that call `area()`. Subclasses inherit all of that. The abstract class is a partly built template that the subclasses complete.

An **interface** is a pure promise. In Java, `interface Comparable<T> { int compareTo(T other); }` says that any class implementing it can compare itself to another object of that type. A `Student` class can write `implements Comparable<Student>`, define `compareTo`, and then the library method `Collections.sort` can sort a list of students. The sort method was written long before `Student` existed. It depends only on the interface. Since Java 8, interfaces may also contain default methods with bodies, but most interfaces are still mainly lists of required methods.

The key difference is what each one allows. A Java class extends at most one class, so an abstract class is the right choice for one family that shares state and code. A class can implement many interfaces, so interfaces fit capabilities that cut across families. A `Robot` and a `Dog` are not related, yet both might implement `SoundMaker`.

Python expresses the same ideas with the `abc` module. A class that inherits from `ABC` and marks a method with `@abstractmethod` cannot be instantiated until a subclass overrides that method; trying raises a `TypeError`. Python has no separate interface keyword, so abstract base classes with only abstract methods play that role.

Both tools serve the same design rule: write code against what an object can do, not against its exact class.
