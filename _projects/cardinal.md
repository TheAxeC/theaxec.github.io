---
layout: post
title:  "Cardinal: Scripting Language"
picture: /assets/images/projects/default.webp
duration: Jan. 2015 - Current
role: Lead Developer
publish: True
---

# Introducing Cardinal: A Lightweight Scripting Language for Education and Research

If you've ever wanted to peek under the hood of a programming language—to really understand how virtual machines work, how concurrency models are implemented, or how compilers translate high-level code into bytecode—you need a codebase that's both powerful enough to be interesting and clean enough to be comprehensible. That's where **Cardinal** comes in.

Cardinal is a lightweight concurrent scripting language that brings together the elegance of Wren with the clarity needed for education and research. In this post, I'll introduce you to what makes Cardinal special, explore its syntax and design philosophy, and explain why it might be the perfect tool for your next language implementation course, research project, or embedded scripting needs.

## What is Cardinal?

Cardinal is a C++ rewrite of the Wren programming language, designed with a specific focus: making language implementation accessible for students, researchers, and anyone curious about how programming languages work under the hood. While it preserves Wren's core goals of minimalism, speed, and expressive object-oriented design, Cardinal goes further by prioritizing code readability and educational value.

The language draws inspiration from several influential languages:
- **Wren** provides the core syntax and design philosophy
- **Smalltalk** influences the pure object-oriented approach
- **Lua** inspires the embeddability and lightweight runtime
- **Erlang** contributes to the concurrency model through lightweight fibers

What sets Cardinal apart is its implementation philosophy. The entire VM and runtime are compact, heavily commented, and written in modern C++20. There are no external dependencies, making it trivial to build and study. Whether you're teaching a programming languages course, conducting research on type systems, or just want to embed a scripting language in your application, Cardinal provides a clean foundation to build upon.

## A Taste of Cardinal Syntax

Cardinal's syntax will feel immediately familiar if you've worked with languages like JavaScript, Python, or Ruby. Here's the classic first program:

```dart
System.print("Hello, world!")
```

Classes are first-class citizens in Cardinal, forming the core abstraction of the language:

```dart
class Bird {
  construct new(species) {
    _species = species
  }
  
  species { _species }
  
  sing() {
    System.print("The %(_species) sings!")
  }
}

var cardinal = Bird.new("cardinal")
cardinal.sing()  // The cardinal sings!
```

Notice the string interpolation with `%(_species)`—a clean way to embed expressions directly in strings. Cardinal uses a constructor pattern with `construct new()` and private fields prefixed with underscores. Getters can be defined simply by writing a method without parameters.

One of Cardinal's most interesting features is its built-in support for lightweight concurrency through **fibers**. Fibers enable coroutine-style concurrency without the complexity of threads:

```dart
class Counter {
  static countTo(n) {
    return Fiber.new {
      for (i in 1..n) {
        Fiber.yield(i)
      }
    }
  }
}

var counter = Counter.countTo(5)
while (!counter.isDone) {
  System.print(counter.call())
}
// Prints: 1, 2, 3, 4, 5
```

This example demonstrates how fibers can yield values, allowing you to write generator-style code that's both elegant and efficient. The fiber suspends execution at each `yield`, returning control to the caller, and resumes where it left off on the next `call()`.

## The Connection to Wren

Cardinal is more than just inspired by Wren—it's a deliberate C++ reimplementation that maintains compatibility with Wren's syntax and semantics while improving on the educational and research aspects. The original Wren is written in C and focuses on being a minimal, fast embeddable scripting language.

Cardinal takes Wren's solid foundation and asks: "What if we rebuilt this with modern C++, extensive comments, and education as a first-class goal?" The result is a codebase that:

- Uses modern C++20 features for clearer code structure
- Includes extensive inline documentation explaining design decisions
- Separates concerns in a way that maps naturally to programming language curricula
- Maintains the single-pass compilation to bytecode that makes Wren fast
- Preserves Wren's compact object representation

For researchers and educators, this means you can use Cardinal to teach the same concepts you'd teach with Wren, but with a codebase that's more approachable for study and modification. Students can trace through the code and understand not just *what* it does, but *why* particular design decisions were made.

## Why Cardinal Excels in Education and Research

Cardinal was designed from the ground up with academic use cases in mind. Here's why it's particularly well-suited for educational and research contexts:

### For Teaching Programming Languages

The VM and runtime are deliberately kept small and readable. Each component is heavily commented, making it suitable for:
- Courses on programming language implementation
- Virtual machine design and optimization
- Compiler construction
- Concurrency models and implementation

The clean separation of concerns means you can focus on one aspect at a time—study the garbage collector without getting lost in parser details, or examine the bytecode compiler without worrying about the runtime.

### For Research Projects

Cardinal provides an excellent platform for:
- **Master's thesis projects** on type systems, effect handlers, memory models, GC strategies, and concurrency paradigms
- **Rapid prototyping** of new language features thanks to the higher-level C++ implementation
- **Experimental implementations** of novel ideas without the overhead of building infrastructure from scratch

The small footprint enables fast iteration—you can modify the language, rebuild, and test your changes in seconds rather than minutes. And because it compiles to bytecode, you can experiment with runtime optimizations and see their effects immediately.

### For Labs and Capstone Projects

Cardinal is sized perfectly for semester-long projects:
- Extend the language with new features (pattern matching, optional types, etc.)
- Implement different garbage collection strategies
- Add new concurrency primitives beyond fibers
- Optimize specific aspects of the VM or compiler

The codebase is large enough to be interesting but small enough that students can grasp the whole system by the end of a semester.

## Practical Features

Beyond its educational value, Cardinal is a fully functional language suitable for real-world embedding:

- **No external dependencies**: The entire language requires only a C++20 compiler
- **Embeddable by design**: Clean C++ API for integrating into your applications
- **Header-only option**: A single-header amalgamation is available for rapid prototyping (perfect for quick experiments, though it trades some performance for convenience)
- **Cross-platform**: Builds on Linux, macOS, and Windows with standard toolchains
- **Minimal standard library**: Small footprint keeps things simple

## Getting Started

Building Cardinal is straightforward. The project includes a helpful Python build script that handles everything:

```bash
# Build Cardinal
python3 utils/build.py --build

# Run tests
python3 utils/build.py --test

# Run benchmarks
python3 utils/build.py --benchmark
```

You can also use CMake directly if you prefer. The project is well-documented with clear build instructions for multiple platforms and toolchains.

## What's Next?

In future posts, I'll dive deeper into Cardinal's implementation:
- How the single-pass compiler generates bytecode
- The design and implementation of the fiber-based concurrency system
- Exploring the garbage collection strategy
- The advanced feature: algebraic effect handlers with multishot continuations
- Extending Cardinal with custom foreign classes and methods

Cardinal represents a unique intersection: a language that's simple enough to understand fully, yet sophisticated enough to explore real implementation challenges. Whether you're teaching the next generation of language implementers, researching novel language features, or just curious about how scripting languages work, Cardinal provides a clean, approachable foundation.

If you're interested in programming language implementation, I encourage you to check out [Cardinal on GitHub](https://github.com/TheAxeC/cardinal-revamped). The codebase is waiting to be explored, modified, and extended—and that's exactly what it was designed for.

---

*In the next post, we'll take a deeper look at Cardinal's bytecode compiler and see how it transforms source code into executable instructions in a single pass.*