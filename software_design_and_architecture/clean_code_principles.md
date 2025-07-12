# Clean Code Principles
Clean code is code that is easy to read, understand, and maintain. It follows a set of principles that are designed to make the code more readable, testable, and less error-prone. Some of the key principles of clean code include:
- Clarity: The code should be easy to read and understand.
- Simplicity: The code should be as simple as possible, avoiding unnecessary complexity.
- Comments: Comments should be used sparingly and only when necessary to explain complex or non-obvious code.
-  Naming: Variables, functions, and classes should have meaningful and descriptive names.
- Formatting: The code should be consistently formatted to improve readability.
- Functionality: The code should be organized into small, single-purpose functions and classes.
- Error handling: The code should handle errors in a consistent and predictable way.
- Testing: The code should be testable and have a high test coverage.
- Reusability: The code should be designed to be reusable and modular.
- Performance: The code should be designed to be efficient and performant.
## Be Consistent
Being consistent refers to maintaining a consistent pattern. This can include using consistent naming conventions, data structures, and interfaces throughout the system, as well as adhering to established design principles and best practices. Consistency can help to make the system more maintainable, understandable, and extendable.
## Meaningful Names
You should follow the practice of giving clear and descriptive names to different components of a system, such as variables, functions, and classes. This can help to make the system more understandable and maintainable by clearly communicating the purpose of each component and its intended usage. 
## Indentation and Code Style
Indentation is the practice of using whitespace to visually group related lines of code together, making it easier to read and understand the structure of the code. Code style refers to the conventions and guidelines used to format and structure code, such as naming conventions, commenting, and use of whitespace.

Having a consistent indentation and code style can help to make the code more readable and understandable, which can improve the maintainability of the system.
## Keep it Small
You should design and implement small, focused components that serve a specific purpose, rather than large, monolithic components that try to do everything. This can help to improve the maintainability and scalability of the system by making it easier to understand, test, and modify individual components.
## Pure Functions
A pure function is a specific type of function that meets the following criteria:
- It takes some input, known as arguments, and returns a value or output.
- It does not cause any observable side effects, such as modifying the state of the system or interacting with external resources.
- Given the same input, it will always return the same output.
- It does not depend on any state or variables that are outside of its scope.

Pure functions are considered to be more predictable and easier to test, as their behavior is determined solely by the input they receive and their internal logic. They also make it easier to reason about the behavior of a program, since the output of a pure function is not affected by any external factors. Pure functions are often used in functional programming, where they are considered a key principle. They are also useful in concurrent and parallel programming, as they are less prone to race conditions and other concurrency-related issues.
## Minimize Cyclomatic Complexity
Cyclomatic complexity is a measure of the structural complexity of a program, which is determined by the number of linearly independent paths through a program's control flow. High cyclomatic complexity can make a program difficult to understand, test, and maintain, so it's often desirable to minimize it in system architecture.

Here are some ways to minimize cyclomatic complexity in system architecture:
- Break down complex functions into smaller, simpler functions that perform specific tasks.
- Use control structures, such as if-else statements and loops, in a consistent and predictable way.
- Use functional programming concepts and techniques, such as immutability and pure functions, to reduce the need for complex control flow.
- Use design patterns, such as the state pattern, to simplify complex control flow.
- Regularly review the code and refactor it to simplify the control flow.
- Use static code analysis tools that can detect and report high cyclomatic complexity in the code.

By following these best practices, the system architecture will be more maintainable, testable, and less error-prone.
## Avoid Passing Nulls Booleans
Passing nulls or Booleans can lead to unexpected behavior and difficult-to-debug errors in a program. Here are some ways to avoid passing nulls or Booleans in system architecture:
- Use Optionals or Maybe types instead of nulls to indicate the absence of a value. This makes it clear when a value is missing and prevents null reference exceptions.
- Use a default value for function arguments instead of allowing them to be null or Boolean. This eliminates the need to check for null or Boolean values and reduces the potential for errors.
- Use the Null Object pattern to replace null values with a special object that has a defined behavior. This eliminates the need to check for null values and makes the code more readable.
- Use the Ternary operator (?:) instead of if-else statements when working with Booleans. This can make the code more concise and easier to read.
- Use the assert function to check the validity of function arguments and throw an exception if they are invalid.

By following these best practices, the system architecture will be more robust and less error-prone.
## Keep Framework Code Distant
Keeping framework code distant refers to separating the application's code from the framework's code. By doing so, it makes it easier to maintain, test, and upgrade the application's codebase and the framework independently.

Here are some ways to keep framework code distant in system architecture:
1. Use an abstraction layer to separate the application code from the framework code. This allows the application code to be written without the need to know the specifics of the framework.
2. Use dependency injection to decouple the application code from the framework code. This allows the application code to use the framework's functionality without having to instantiate the framework objects directly.
3. Avoid using framework-specific libraries or classes in the application code. This makes it easier to switch to a different framework in the future if needed.
4. Use a standard interface for the application code to interact with the framework. This allows the application code to be written without the need to know the specifics of the framework.
5. Keep the application and the framework code in separate projects and/or repositories.


By following these best practices, the system architecture will be more maintainable, testable, and less error-prone, and it will be easier to upgrade or switch the framework if needed.
## Use Correct Constructs
In the context of clean code principles, "using correct constructs" refers to using appropriate programming constructs, such as loops, conditionals, and functions, in a way that makes the code easy to understand, maintain, and modify.

When using correct constructs, the code should be organized in a logical and intuitive way, making use of appropriate control flow statements and data structures to accomplish the task at hand. This also means that the code should avoid using unnecessary or overly complex constructs that make the code harder to understand or reason about.

Additionally, correct constructs also means to use the right constructs for the right problem, for example, if you want to iterate over an array, use a for loop instead of recursion and also, you should avoid using global variables and instead use function arguments and return values to pass data between different parts of the code.

By using correct constructs, the code will be more readable, more maintainable, and less prone to bugs, making it easier for other developers to understand, debug and extend the code.
## Command Query Separation
Command-Query Separation (CQS) is a software design principle that separates the responsibilities of a method or function into two categories: commands and queries. Commands are methods that change the state of the system, while queries are methods that return information but do not change the state of the system.
