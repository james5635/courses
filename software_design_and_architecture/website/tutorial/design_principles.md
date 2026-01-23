---
sidebar_position: 4
---

# Design Principles
## SOLID

SOLID is an acronym that stands for five principles of object-oriented software development, which were first introduced by Robert C. Martin in the early 2000s. These principles are:

- Single Responsibility Principles (SRP)
- Open/Closed Principle (OCP)
- Liskov Substitution Principles (LSP)
- Interface Segregation Principle (ISP)
- Dependency Inversion Principle (DIP)

## DRY

DRY (Don't Repeat Yourself) is a software development principle that suggests that code should not have duplicate functionality. The idea is to keep the codebase as simple as possible by eliminating redundancy and duplication. The goal is to reduce complexity and improve maintainability by ensuring that each piece of knowledge is expressed in a single, unambiguous way within the system.

The DRY principle is closely related to the Single Responsibility Principle (SRP) and the Open-Closed Principle (OCP), which are part of the SOLID principles. The DRY principle aims to reduce the amount of duplicate code by creating abstractions that can be reused across the system.

## YAGNI

YAGNI (You Ain't Gonna Need It) is a software development principle that suggests that developers should not add functionality to a codebase unless it is immediately necessary. The idea is to avoid creating unnecessary complexity in the codebase by only adding features that are actually needed.

The YAGNI principle is closely related to the Single Responsibility Principle (SRP) and the Open-Closed Principle (OCP), which are part of the SOLID principles. YAGNI aims to keep the codebase as simple as possible by avoiding the creation of unnecessary abstractions and functionality.

## Law of Demeter
Also called “Principle of Least Knowledge”, it states:

### In Practice
- Avoid chaining calls deep into the internals of other objects.
- Restrict communication to objects you directly manage.

### ❌ Bad Example (Violation)
```js
// Controller
total = order.customer.address.getRegionTaxRate() * order.amount
```

### ✅ Good Example
```js
// Controller
total = order.calculateTotal()
```

### Why It Matters
- Reduces coupling → fewer dependencies between classes.
- Increases maintainability → changes in one class don’t affect distant classes.
- Improves readability → clear boundaries of responsibility.
## Tell Don't Ask

The Tell, Don’t Ask principle emphasizes that objects should be told what to do rather than being queried for their state and having decisions made externally. This promotes encapsulation and reduces coupling by keeping logic within the objects that own the data.
### Key Concepts
- Instead of pulling data out of objects to make decisions, push the behavior into the object itself.
- Objects should be responsible for their own logic and state management.

Asking style (bad):
```js
if (user.profile.isComplete()) {
    // allow checkout
}
```
Telling style (good):
```js
if (user.canCheckout()) {
    // allow checkout
}
```
## Hollywood Principle
The Hollywood Principle is a software development principle that states: "Don't call us, we'll call you." It suggests that high-level components should dictate the flow of control in an application, rather than low-level components.

This principle is often used in the context of inversion of control (IoC) and dependency injection. In traditional software development, low-level components are responsible for creating and managing the high-level components that they depend on. With IoC, the high-level components dictate the flow of control, and the low-level components are created and managed by a separate mechanism.

## Composition over Inheritance
Composition over inheritance is a programming principle that suggests that it is better to use composition, a mechanism for assembling objects, to create complex objects, rather than using inheritance, which is a mechanism for creating new classes based on existing ones.

Inheritance is a powerful mechanism for creating reusable code, but it can also lead to tightly coupled, hard-to-maintain code. This is because inherited classes are tightly bound to their parent classes and any changes made to the parent class will affect all of its child classes. This makes it hard to change or extend the code without affecting the entire class hierarchy.

## Encapsulate What Varies
Encapsulate what varies is a programming principle that suggests that code should be organized in such a way that the parts that are likely to change in the future are isolated from the parts that are unlikely to change. This is accomplished by creating interfaces and classes that separate the varying parts of the code from the stable parts.

Encapsulating what varies allows for more flexibility in the code. When changes are needed, they can be made to the encapsulated parts without affecting the rest of the code. This makes it easier to understand, test, and maintain the code.

## Program Against Abstractions

Programming against abstractions is a programming principle that suggests that code should be written in such a way that it is not tied to specific implementations, but rather to abstractions. This is accomplished by defining interfaces or abstract classes that define the behavior of a group of related classes without specifying their implementation.

Programming against abstractions allows for more flexibility in the code. When changes are needed, they can be made to the implementation of the abstractions without affecting the code that uses them. This makes it easier to understand, test, and maintain the code.

