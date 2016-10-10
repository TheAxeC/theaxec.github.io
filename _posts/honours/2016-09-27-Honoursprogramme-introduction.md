---
layout: post
title:  "Honoursprogramme introduction"
category: honoursprogramme
tags: eff kuleuven honoursprogramma
---

During my Masters, I chose to participate in the [Honoursprogramme of the Faculty of Engineering Science (dutch link)](https://eng.kuleuven.be/studenten/engineering-essentials-ingenieurscompetenies/honoursprogramma/honoursprogramma). The Honoursprogramme is a new programme, starting from 2016-2017, provided by the Faculty of Engineering Science of KULeuven. In the Honoursprogramme students add 18 ECTS to their education. These credits can be accumulated starting from their second bachelor year. The student can choose between two tracks. They can choose the Research track or the Interdisciplinairy track. I am most interested in research and as such, choose to participate in the Research track. In order to participate in the Honoursprogramme, students have to find a professor that is willing to be their advisor. A lot of initiative is expected from the students. 

## Beginning

Since I am interested in research and planning to start a PhD, I thought the Honoursprogramme would be a good idea to delve into research. My first course of action was to find a professor that would want to guide me. In order to do that, I needed to have an idea of what I wanted to do. I have an interest in multiple fields. Programming languages, Artificial intelligence and Distributed systems are all fields that interest me. I made an appointment with professor Tom Schrijvers. 

He was interested in being my advisor for the Honoursprogramme and invited me to the [IFL 2016](https://dtai.cs.kuleuven.be/events/ifl2016/), a symposium on Implementation and Application of Functional Languages that was being held at KULeuven. There were a lot of interesting talks during this symposium, but what intrigued me the most, were talks about Effect Handlers.

Now that I had decided I wanted to work on a project about Effect Handlers, prof. Tom Schrijvers and I could look for a specific project. Prof. Tom Schrijvers suggested the project: Algebraic Effect Handlers: Harnessing the Fundamental Power of Effects. The project uses a programming language called [Eff](http://www.eff-lang.org/). My project centers around the development of an optimized compiler for the Eff programming language.

## Development of an optimized compiler for Eff
My task is to work on optimizations for the Eff compiler. Another goal is to publish a paper on this project. More concretely I have the following tasks:

1. Literature study to find elements to optimize
2. Designing the optimization
3. Implementation
4. Evaluating the optimization
5. Formal proof of the optimization

## First steps
My first steps are to get familiar with the Eff compiler. The compiler does it's normal work and composes an Abstract Syntax Tree, an AST. The AST is fed to the optimization module. Optimizations work bottom-up. For example:
{% highlight ocaml %}
and optimize_comp c = reduce_comp (optimize_sub_comp c)
{% endhighlight %}
When we want to optimize a computation, first the "inside" of the computation is optimized and afterwards the "outer". 

Currently, I still have to go through many of the existing optimizations. Once I am able to understand the current optimizations, I can start looking for other possible optimizations.