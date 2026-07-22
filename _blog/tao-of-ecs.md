---
layout: post
title:  "The TAO of ECS"
category: research
publish: True
date: 2026-07-22
---

Add methods to an entity-component system and someone will tell you that you have reinvented object-oriented programming. The remark is meant as an accusation. I think it is an accurate observation attached to a wrong conclusion, and the difference between those two things is what this post is about.

The claim: trait-actor is to ECS what OOP is to imperative programming. When a component carries methods and a prefab carries dispatched behaviour, the paradigm has not been betrayed. It has been extended by the same transformation that turned procedural programming into OOP fifty years ago, and it succeeds or fails by the same rule: the lower tier has to survive intact.

Some terms first. A *trait* is a component that can carry methods, so any entity that has the trait has the behaviour. An *actor* is a prefab that can carry methods and an inheritance chain, so instances spawned from it share dispatched behaviour. I'll call the pattern trait-actor (TA), and the resulting style TAO, for trait-actor orientation. Trait comes before actor in the name because traits are the primitive: actors are assembled from traits, in the same way that ECS puts the entity before the system. I'll use Rite, a scripting language I am building for game simulation, for the code examples. The argument does not depend on Rite, but Rite is designed around this analogy on purpose, which makes it a convenient demonstration.

## What OOP added

Strip OOP down to what it mechanically added to the procedural languages it grew out of. C++ extended C with a short list of moves:

1. Behaviour bound to a data type. A method is declared on a struct, not merely near it.
2. Dispatch. A call site names an operation, and the receiver's runtime type selects the implementation.
3. Inheritance. Types form chains, and a subtype reuses and overrides its parent's behaviour.
4. Nothing was removed. Free functions survived, plain structs survived, and a C++ program drops to the procedural tier at any call site, with no bridge and no ceremony.

The fourth point is the one people forget. OOP as practised in systems languages is a superset discipline: the new tier is used where behaviour belongs to a type, and the old tier remains first-class where it does not. The famous failures of OOP, the everything-is-an-object doctrine and the towering inheritance hierarchies, were failures of totalising the new tier rather than failures of the tier itself.

It also helps to remember what a method is. Under every object system, a method desugars to a function with the receiver passed as the first argument:

```text
obj.damage(10)   ≡   damage(obj, 10)
```

A method is not a new kind of computation. It is a binding decision: the same function, attached to a type, selected by dispatch. This becomes relevant again below.

## What an ECS is

Entity-component-system architecture is usually introduced through what it rejects: no inheritance, no fat game objects, data separated from behaviour. Its positive structure is more interesting. The [established analogy](https://github.com/SanderMertens/ecs-faq) in the field describes it well: an ECS is an in-memory relational database with a scheduler.

- An *entity* is not a container. It is an identity, a key. It holds nothing itself; the world's per-type storage holds data about it.
- A *component* is a typed attribute, a column entry keyed by entity.
- A *system* is a query with a body: for every entity having Position and Velocity, run this. Data is addressed associatively, by shape, rather than by name or ownership.

Now place that beside procedural programming. Components are the raw variables. Systems are the free functions. Prefabs, template entities whose component values are copied or inherited at instantiation, are the structs. There is no dispatch and no binding of logic to type; logic lives in free-standing bodies that operate over whatever data matches. This is the procedural model with one amendment: the data model underneath is relational rather than lexical. Variables are not owned by scopes and objects. They are rows selected by query.

So a more precise characterisation is that ECS is imperative programming over a relational data model. That is why it feels familiar (you write loops that mutate data) and strange (nobody *has* the data) at the same time. It also explains why systems look like free functions but are declared as queries: in a relational model, the query is how you name data.

## The same transformation

Line the two paradigms up and apply OOP's moves to the ECS column:

| procedural | → OOP | ECS | → trait-actor |
| --- | --- | --- | --- |
| raw variables | instance fields | components | trait fields |
| structs | classes | prefabs | actors |
| a struct instance | an object | an entity's component set | a spawned actor instance |
| free functions | methods | systems | methods on traits/actors |
| function call | virtual call | system tick over a query | dispatch on the runtime actor |
| — | inheritance chains | — | actor `extends` chains |
| free functions survive | | systems survive | |

Every move from the first transition reappears in the second: behaviour bound to type, runtime dispatch, inheritance, and, if the design is any good, nothing removed.

Here is the same fragment of game logic at both tiers. First the procedural-ECS form, plain data and free-standing logic:

```clojure
(def-trait Health [hp :i32])

(defn take-damage [e amount]                    ; a free function over world data
  (field! e Health :hp (max 0 (- (field e Health :hp) amount))))

(defsystem Regen :on-update e [Health]          ; a free-standing per-frame query
  (field! e Health :hp (+ (field e Health :hp) 1)))
```

Then the TA form, the same data with behaviour bound to type:

```clojure
(def-trait Health [hp :i32]
  (method take-damage [self amount]             ; behaviour ON the trait
    (field! self Health :hp (max 0 (- (field self Health :hp) amount)))))

(def-actor Boss (with Health)
  (method regen :every-frame self [Health]      ; the per-frame loop, as a scheduled method
    (field! self Health :hp (+ (field self Health :hp) 1))))

(.take-damage (spawn Boss) 10)                  ; a dispatched call
```

Same components, same world, same machine code on the hot path. The only thing that moved is the attachment of behaviour, which is exactly what distinguishes an OOP program from its procedural equivalent.

## The desugaring is literal

Analogies between paradigms are easy to make. This one holds at the level of implementation, not just vocabulary.

Recall that a method is a function with the receiver as argument zero. In Rite, a *scheduled* method, one that runs every frame over a type's instances, is not merely analogous to a system. It compiles to one: the method body becomes a system whose query matches the actor's instances, with `self` as the per-row entity binding. The desugaring has the same shape in both paradigm shifts:

```text
OOP:   obj.m(x)                  ≡   m(obj, x)              method = function + explicit receiver
TAO:   (method m :every-frame …) ≡   defsystem + self row   scheduled method = system + explicit receiver
```

In both cases the new construct is a view over the old one, a binding-and-dispatch layer over the same underlying computation. That is why, in both cases, the old tier can remain first-class with zero interop cost. C++ methods and free functions call each other freely because a method *is* a function. Rite methods and systems coexist on the same entity because a scheduled method *is* a system.

## Prototype, not class

The obvious version of the analogy says TA gives you Java on an ECS. It does not, and the correction matters.

In class-based OOP, a class is a compile-time construct. Objects carry a pointer to it, and the class and its instances live in different worlds: you cannot hand a Java class a component, and editing a class at runtime is either impossible or an exotic reflection feature. In prototype-based languages, a "class" is itself a live object, a template instance, and inheritance means delegating to it at runtime. Self is the research lineage here (Ungar and Smith's work in the late 1980s); JavaScript is the mainstream one.

Look at what an actor is. Its "class" is a prefab: a real entity in the world. Instances relate to it by an `is-a` edge and inherit data through that edge, not method tables through a vtable. A static field needs no special mechanism; it is an ordinary component whose one copy lives on the prefab, shared by instances through the same machinery everything else uses. Because the type is a live entity, you can edit it at runtime: add a component to the actor, and every live instance acquires it immediately. This is also what makes deep hot-reload tractable. Reloading a type means editing an entity, not regenerating a class, so a running game can absorb the change without restarting.

So the ladder has four distinct rungs, not a repeated pair:

> imperative : class-based OOP :: relational-imperative (ECS) : prototype-based OOP (TAO)

Prototype-based objects are a road not taken in language design: academically respected, mainstream mostly by accident of JavaScript. Meanwhile every game engine reinvents their core idea the moment it needs templates, because a prefab is a prototype, a live instance you copy from and delegate to. When you then bind behaviour to prefabs, you do not get Java on an ECS. You get Self on a database. As far as I can tell this point in the design space has no name, and engines have been drifting toward it for years without one, which is part of why the arguments about it go in circles.

## Two object models

Mature OOP languages ended up with two kinds of object, not one. C++ has objects with identity, held behind pointers and compared by address, and it has plain values, copied on assignment and compared by content. The split is cultural as much as technical, and it is load-bearing: a 3D vector wants to be a value, a network connection wants to be an identity, and confusing the two produces either aliasing bugs or pointless indirection.

TAO replays this split as well. Rite has records alongside actors. A record is a value-tier object with a fixed shape, structural equality, a structural hash, and no identity. It can carry methods and type methods like an actor can, but copying it copies it, and two records with equal fields are the same value:

```clojure
(record Point [x y]
  (method mag-sq [self] (+ (* (:x self) (:x self)) (* (:y self) (:y self)))))

(.mag-sq (Point 3 4))          ; => 25
(= (Point 1 2) (Point 1 2))    ; => true, structural: a record is a value
```

An entity is the opposite in every one of those respects: it has identity, no structural equality, durable mutable state, and it participates in queries. The rule for choosing between them is the one C++ programmers already know: values for the small things you pass around (a vector, a colour, a configuration blob), identities for the things that exist in the world. So the transformation does not just add a class-analogue to the ECS. It reproduces the whole shape of a mature object system: an identity model and a value model, methods on both, and the discipline of knowing which one a thing is.

## What survives

The success condition, in both transitions, is that nothing is removed. This deserves to be stated as a design rule rather than left as an accident of implementation, because it is the difference between a superset and a replacement.

Rite states it as a language rule and calls it the interop invariant: no capability is gated on a paradigm. `def-actor` only assembles primitives; anything an actor can do is available to a raw spawned entity that opts in by carrying the same trait or method. Equal capability, not equal ergonomics. The sugar is convenience, never exclusive power.

TA relates to its ECS the way C++ relates to C. You drop down a tier at any call site, and the tiers compose on a single entity: one boss can be moved by a batched physics system, carry reusable trait behaviour shared with every other damageable thing in the game, and run its own dispatched methods, with no glue code, because every tier reads and writes the same components. There is no bridge to cross because there is nothing to bridge.

## Consequences

The analogy is useful because it answers design questions that otherwise get argued from taste.

*When should logic be a system, and when a method?* This is the same question as "when should this be a free function, and when a method?", and it has the same answer. Bind behaviour to a type when the behaviour belongs to the type: few instances, bespoke logic, identity that matters. The boss, the quest NPC, the UI panel. Keep behaviour free-standing when it is a transformation over many values: movement, physics, AI ticking over five hundred enemies. Reusable behaviour across many kinds of entity goes on a trait, which is where the composition-first instinct of ECS survives inside TAO.

*Where will it go wrong?* In the same place it went wrong last time. OOP's historical pathology was totalisation: every loop a method call, data hidden behind accessors until batch processing became impossible. That is the disease ECS was invented to cure, and TA inherits the vulnerability in the same spot. Put a hot per-frame loop in per-instance dispatched methods and you have rebuilt the problem, one virtual call per entity per frame. The cure is also unchanged: the tiers must coexist, and the throughput tier must remain the default for bulk work. An engine that makes the actor tier mandatory has repeated 1990s OOP. An engine that forbids it has repeated 2010s ECS purism. The design target is the superset.

*What about the accusation?* "You reinvented OOP" is exactly as true, and exactly as damning, as telling a C++ programmer they reinvented C with extra steps. The interesting question was never whether behaviour would get bound to types; every large ECS codebase grows some version of it, because some behaviour does belong to types. The interesting questions are whether the binding is principled (what are the dispatch semantics, the inheritance rules, the collision behaviour when two traits define the same method) and whether the lower tier survives undamaged. Those are engineering questions with checkable answers, and they are more productive than the ideological version of the argument.

## Objections

Three pushbacks come up whenever I explain this, and they deserve answers.

*"Traits are just mixins."* At the surface, yes: reusable behaviour attached to many types is what a mixin is for. The difference is the substrate. A mixin changes what a class is, at definition time. A trait changes what an entity is, at runtime, one entity at a time, and the attachment is visible to the query engine: add a trait and the entity starts matching different systems. A mixin also brings no storage discipline, while a trait is a column, so the data it carries participates in the batched tier. Name collisions are handled differently too: in Rite, a composed trait is not in the dispatch chain, so two traits with the same method name never silently collide; you qualify the call to say which one you mean. "Mixin" describes the reuse pattern. It does not describe a live, queryable, batched substrate.

*"Engines already have prefabs with methods."* They do, and that supports the claim rather than undermining it: the ladder is being climbed everywhere, ad hoc. I am not arguing that behaviour on templates is new. I am arguing that it is a specific, nameable transformation with a known success condition, and that recognising it changes how you build it. The test is the superset rule: can the plain-data tier still do everything, on the same entities, with no bridge? Where the object tier is a separate model bolted beside the ECS, the bridge between them is where the complexity and the performance loss accumulate. Where the object tier is a view over the ECS, there is no bridge to maintain.

*"The relational framing is doing all the work."* The objection goes: if an ECS is a database, then methods on components are just stored procedures, and the OOP ladder is decoration. But the two framings answer different questions. The relational framing explains where data lives and why batching wins. It does not tell you what dispatch should mean, how inheritance should work, or what happens when two traits define the same method; those are object-model questions, and the ladder is what predicts their answers and their failure modes. The database world has its own name for binding objects to relational data without a superset discipline: the object-relational mismatch, where the object tier hides the query tier and performance dies behind the abstraction. TA done right avoids that for a structural reason. Objects do not wrap rows. They are rows.

## Prior art

I tried to find this stated before and failed, which I say cautiously, since paradigm-level observations are rarely new.

What I can find are three adjacent framings. The relational analogy (ECS as database, systems as queries) is well established; it appears in the [ECS FAQ](https://github.com/SanderMertens/ecs-faq) and on [Wikipedia](https://en.wikipedia.org/wiki/Entity_component_system), and I lean on it above. The opposition framing (ECS versus OOP, composition versus inheritance, data versus encapsulation) is everywhere, in conference talks and forum threads alike, and treats the two as rivals. The critique framing treats methods-on-components as contamination, the ladder's second step as a regression.

What I have not found is the claim made here: that ECS-to-TA is the same transformation as procedural-to-OOP, with the superset discipline as its success condition, landing on prototype-based rather than class-based semantics. If someone has written this down before, I would like to read it, and I will add the reference here.

## Rite

Most systems climb this ladder ad hoc. Behaviour attachment grows feature by feature, and the interop between tiers is whatever it happens to be. The premise of Rite is to climb it deliberately: an ECS the compiler understands natively, the trait-actor tier designed as a strict superset from day one, the interop invariant enforced as a rule of the language, and the desugarings above implemented literally. Scheduled methods are systems. The class is a prefab. Hot reload edits types as live data, and reaches running instances. Rite is not yet released; when it is, it will be the executable version of this argument.

Until then: ECS is imperative programming over a relational data model, and trait-actor is its object orientation, prototype-based rather than class-based. C++ did not betray C, and methods on components do not betray the ECS.

---

*References: [ECS FAQ (Sander Mertens, author of flecs)](https://github.com/SanderMertens/ecs-faq) · [Entity component system, Wikipedia](https://en.wikipedia.org/wiki/Entity_component_system) · [Ungar & Smith, "Self: The Power of Simplicity", OOPSLA '87](https://dl.acm.org/doi/10.1145/38765.38828)*
