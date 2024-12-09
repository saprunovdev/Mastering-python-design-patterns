## Single Responsibility Principle (SRP)

When defining a class, that class should have only one reason to exist and should be responsible for only one aspect of the functionality.

In simple terms, each class should have one job or responsibility, and that job should be encapsulated within that class.

Thus, by adhering to the SRP, we are essentially striving for classes that are focused, cohesive, and specialized in their functionality. When each class has a well-defined and single purpose, it becomes easier to manage, understand, and extend the code.

In practice, applying the SRP often leads to smaller, more focused classes, which can be combined and composed to create complex systems while maintaining a clear and organized structure.

## Open-Closed Principle (OCP)

This principle emphasizes that software entities, such as classes and modules, should be open for extension but closed for modification. It means that once a software entity is defined and implemented, it should not be changed to add new functionality. Instead, the entity should be extended through inheritance or interfaces to accommodate new requirements and behaviors.

Modifying an entity introduces the risk of breaking other parts of the codebase that rely on it.

## Liskov Substitution Principle (LSP)

This concept dictates how subclasses should relate to their superclasses.

If a program uses objects of a superclass, substituting them with objects of a subclass should not affect the correctness or expected behavior of the program.

In simple terms, if a program works with objects of a parent class, replacing them with objects of a child class should not break the program or change how it is expected to function.

When using inheritance, subclasses extend their parent classes without altering their external behavior. For example, if a function works correctly with an object of a superclass, it should also work correctly with objects of any subclass of that superclass.

## Interface Segregation Principle (ISP)

This concept advocates creating more specific interfaces rather than broad, general-purpose ones. A class should not be forced to implement interfaces it does not use.

When designing software, we should avoid creating large, monolithic interfaces. Instead, the focus should be on creating smaller, more focused interfaces. This ensures that classes inherit or implement only what they actually need.

## Dependency Inversion Principle (DIP)

This principle advocates that high-level modules should not depend directly on low-level modules. Instead, both should rely on abstractions or interfaces. By doing so, we decouple the high-level components from the details of the low-level components.

This approach reduces coupling between different parts of the system, making it more maintainable and extendable.

Following the Dependency Inversion Principle (DIP) promotes loose coupling within a system by encouraging the use of interfaces as intermediaries between its components.

When high-level modules depend on interfaces, they remain isolated from the specific implementations of low-level modules.

DIP is closely tied to the principle of loose coupling.