## 1. Encapsulate What Varies

Isolate the parts of your code that are most likely to change and encapsulate them. This approach enables you to modify one part of your system without affecting others.

### Benefits
- **Ease of Maintenance**: Changes are isolated, so only the encapsulated parts need to be updated.  
- **Enhanced Flexibility**: Encapsulated components can be easily swapped or extended.  
- **Improved Readability**: Isolating varying elements makes your code more organized and easier to understand.

### Polymorphism
In programming, **polymorphism** allows objects of different classes to be treated as objects of a common superclass. It can be achieved through **getters** and **setters**. 

In Python, we can use the `@property` decorator to simplify this process. A setter can be defined as follows:

```python
class Example:
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
```

## 2. Favor Composition Over Inheritance

In Object-Oriented Programming (OOP), inheritance often leads to tightly coupled code that is hard to maintain and extend. Instead, **favor composition** by building complex objects by combining simpler ones.

### Benefits
- **Flexibility**: Composition allows you to change object behavior at runtime.  
- **Reusability**: Smaller, simpler components can be reused across the application.  
- **Ease of Maintenance**: Individual components can be swapped or updated without affecting the entire system.


## 3. Program to Interfaces, Not Implementations

Define an **interface** as a contract specifying a set of methods that must be implemented by classes. This approach reduces dependency on specific implementations.

### Benefits
- **Flexibility**: Easily switch between different implementations without altering the code.  
- **Maintainability**: Decoupled code is easier to update or replace.  
- **Testability**: Interfaces simplify unit testing.

### Implementing Interfaces in Python
#### Abstract Base Classes (ABCs)
Use the `abc` module to define abstract methods that subclasses must implement.

#### Protocols
Protocols offer more flexibility than ABCs by implementing duck typing. An object is considered valid if it has the required attributes or methods, regardless of inheritance.

The key advantage of using **Protocols** is that they focus on what an object can do rather than what it is. In other words, if an object walks like a duck and quacks like a duck, it's a duck, regardless of its actual inheritance hierarchy.

For example, let's say we have a Protocol named `Flyer` with a method `fly`. If we implement a new class with the method `fly`, it will be considered a `Flyer`, even if it does not explicitly inherit from the `Flyer` class.

## 4. Loose Coupling Principle

The **Loose Coupling Principle** helps address issues in software systems with complicated relationships between components that are difficult to maintain. Loose coupling refers to minimizing dependencies between different parts of a program. In a loosely coupled system, components are independent and interact through well-defined interfaces, making it easier to make changes to one part without affecting others.

### Benefits
- **Maintainability**: With fewer dependencies, it is easier to update or replace individual components.  
- **Extensibility**: A loosely coupled system can be easily extended.  
- **Testability**: Independent components are easier to test in isolation.

### Techniques for Achieving Loose Coupling
#### Dependency Injection
**Dependency injection** allows a component to receive its dependencies from an external source instead of creating them internally. This approach makes it easier to swap or mock dependencies.

```python
class Database:
    def query(self):
        return "Data from the database"

class Service:
    def __init__(self, database):
        self.database = database

db = Database()
service = Service(db)  # Inject the dependency
```

#### Observer Pattern
**The Observer Pattern**  allows an object to publish changes to its state so other objects can react accordingly, without being tightly bound to one another.

```python
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

class Observer:
    def update(self):
        print("Observer notified!")

# Usage
subject = Subject()
observer = Observer()
subject.attach(observer)
subject.notify()
```