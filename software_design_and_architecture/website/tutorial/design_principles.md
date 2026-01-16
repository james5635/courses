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
