---
layout: post
title:  "Cardinal: Scripting Language"
picture: /assets/images/projects/default.webp
duration: Jan. 2015 - Current
role: Lead Developer
---

# Cardinal: A Powerful and Lightweight Scripting Language

## Introduction

Welcome to the world of **Cardinal**, a small, fast, class-based concurrent scripting language that brings together the best features of Smalltalk, Lua, and Erlang. Developed with high performance in mind, Cardinal is written in C and, since 2023, in C++14. It is designed to be embedded in applications, offering a compact yet powerful tool for developers. 

<p align="center">
<img src="/assets/images/projects/cardinal.png" alt="Cardinal Logo" width="500"/>
</p>

## Project Overview

**Title:** Cardinal: Scripting Language  
**URL:** [Cardinal on GitHub](https://github.com/TheAxeC/Cardinal)  
**Duration:** January 2015 - Current  
**Role:** Lead Developer  

Cardinal is known for its high performance, which is comparable to Luajit 2.1 with just-in-time compilation turned off (-joff). Here’s a brief rundown of what makes Cardinal stand out:

## Key Features

### 1. Small and Readable

Cardinal's virtual machine (VM) implementation is under 4,000 semicolons, making it both small and readable. Despite its size, the code is well-documented, ensuring that developers can easily understand and navigate through it.

### 2. Fast Execution

Cardinal boasts a fast single-pass compiler that generates tight bytecode, coupled with a compact object representation. These features enable Cardinal to compete with other dynamic languages in terms of speed.

### 3. Class-Based Structure

In contrast to many scripting languages with unusual or non-existent object models, Cardinal places classes at the forefront. This class-based structure makes it easier for developers who are familiar with object-oriented programming to adopt and use Cardinal.

### 4. Concurrent Execution

Lightweight fibers are integral to Cardinal's execution model. These fibers allow developers to organize programs into a multitude of communicating coroutines, facilitating concurrent execution.

### 5. Scripting Language for Embedding

Cardinal is designed for embedding in applications. It has no dependencies, a small standard library, and a user-friendly C++ API. The language compiles cleanly as C++11, making it a convenient choice for integration into various applications.

### 6. Header-Only API

For those who prefer a header-only API, Cardinal offers a single header-only file of the entire language. This option, while increasing compile times and causing a slight performance decrease (about 15%) in Foreign Method calling, provides flexibility and ease of use. Note that this requires C++17 due to the usage of inline variables.

## Sample Code

Here’s a quick example of Cardinal in action:

```dart
System.print("Hello, world!")

class Cardinal {
  flyTo(city) {
    System.print("Flying to %(city)")
  }
}

var adjectives = Fiber.new {
  ["small", "clean", "fast"].each {|word| Fiber.yield(word) }
}

while (!adjectives.isDone) System.print(adjectives.call())
```

This code snippet demonstrates the simplicity and elegance of Cardinal’s syntax, allowing developers to create powerful scripts with minimal effort.

## Conclusion

Cardinal is a versatile and efficient scripting language tailored for embedding in applications. Its combination of speed, readability, and modern features makes it a compelling choice for developers seeking a robust scripting solution. As the Lead Developer, I am excited to continue enhancing Cardinal and expanding its capabilities to meet the evolving needs of the developer community.

For more information and to get started with Cardinal, visit the [GitHub repository](https://github.com/TheAxeC/Cardinal). Happy coding!