# Design Patterns Overview

Design patterns are proven solutions to common software design problems. They help us write code that is reusable, maintainable, and scalable.

---

## 🏗️ Categories of Design Patterns

### 1. **Creational Patterns** (Object Creation)
These patterns deal with object instantiation mechanisms. They aim to make a system independent of how its objects are created, composed, and represented.

- **Abstract Factory** – Create families of related objects without specifying their concrete classes.
- **Builder** – Construct complex objects step by step.
- **Prototype** – Clone existing objects without making the code dependent on their classes.
- **Singleton** – Ensure a class has only one instance and provide a global point of access to it.

---

### 2. **Structural Patterns** (Class and Object Composition)
These patterns focus on how classes and objects are composed to form larger structures.

- **Adapter** – Convert one interface to another expected by the client.
- **Bridge** – Separate abstraction from implementation so both can vary independently.
- **Composite** – Treat individual objects and compositions of objects uniformly.
- **Facade** – Provide a simplified interface to a complex system.
- **Flyweight** – Use sharing to support large numbers of fine-grained objects efficiently.
- **Proxy** – Provide a placeholder to control access to another object.

---

### 3. **Behavioral Patterns** (Interaction Between Objects)
These patterns are concerned with how objects interact and share responsibility.

- **Chain of Responsibility** – Pass a request along a chain of handlers.
- **Command** – Encapsulate a request as an object, allowing parameterization and queuing.
- **Interpreter** – Define a language's grammar and interpret sentences in the language.
- **Iterator** – Access elements of a collection sequentially without exposing the underlying structure.
- **Mediator** – Centralize communication between objects to reduce coupling.
- **Memento** – Capture and restore an object’s internal state.
- **Observer** – Notify multiple objects about changes in another object.
- **State** – Allow an object to change its behavior when its internal state changes.
- **Strategy** – Define a family of algorithms and make them interchangeable.
- **Visitor** – Separate algorithms from object structures they operate on.
- **Template Method** – Define the program skeleton in a method, allowing subclasses to redefine certain steps.

---

## ⚙️ Core Concepts & Principles

### 🧱 **Scope: Class vs Object**
- **Class-based patterns**: Use inheritance (static binding, compile-time).
- **Object-based patterns**: Use object composition (dynamic binding, runtime).

### ✅ **Program to an interface, not an implementation**
- Design code to depend on **abstractions (interfaces)** rather than concrete implementations.
- This enables flexibility and reuse.

---

## 🧬 Inheritance vs Composition

### 🔹 Class Inheritance
- **What**: One class inherits from another.
- **When**: You want to reuse implementation.
- **Downside**: Tightly coupled, inflexible.

### 🔹 Interface Inheritance (Subtype Polymorphism)
- **What**: One class implements an interface.
- **When**: You want to use one object in place of another.
- **Benefit**: Promotes polymorphism and decoupling.

> ❗ Class inheritance is **compile-time** and rigid.  
> 🧩 Object composition is **runtime** and more flexible.

---

## 🤝 Favor Object Composition Over Class Inheritance

Instead of creating rigid class hierarchies:
- Compose objects with defined interfaces.
- Delegate tasks to these objects.

### 🎭 Delegation
- An object handles a request by **delegating** it to a second object (its delegate).
- Promotes reuse, flexibility, and encapsulation.

---
