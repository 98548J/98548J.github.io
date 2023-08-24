---
title: Programming Paradigm / Architecture Development
parent: Programming
notebook: programming
date: 2023-06-06
signatures:
- "Ayla Clark"
- "Caleb Carlson"
- "Tucker Nielson"
nav_order: 1
has_children: false
---

{: .design}
Define Problem

With the completion of the test bed robot, we need to decide how we will program the test bed and any other robots we build. 

The problem is, that we do not know what software architecture to use for any of our programs.

{: .design}
Constraints

We intend to use the same **architecture** for any prototypes and/or competition robots. Because of this, we will need to adhere to the constraints for competition programs. The main requirement for competition programs is that the program uses the **Competition Template**.

{: .design}
Generate Concepts

Here is a list of paradigms we could use for our robot:

* Imperative programming.
* Functional programming.
* Object Oriented programming (OOP).

Also, below is a list of architectures we could use for our robot. These architectures can be described at [Towards Data Science](https://towardsdatascience.com/10-common-software-architectural-patterns-in-a-nutshell-a0b47a1e9013).

* Layered Pattern.
* Event-Bus Pattern.
* Broker Pattern.

{: .design}
Our Decision

After evaluating each option, I have decided to use:

**Object Oriented programming** style for the majority of the program.
**Imperative** programming style for autonomous routines.
**Layered Pattern** Architecture.

I did not think a **Functional** style of programming would be appropriate, because it is common for functions to behave differently depending on when they are called. 

An example of this could be an “Update()” function or method for a PID. This “Update()” function would simply allow the PID to adapt to any changes in the **robot’s position or velocity**. However, the result, or effect, of the function **depends** on the robot’s position or velocity! 

This dependency on the environment or situation at hand is exactly opposite of what a functional programming style would be. This is **not** to say that functional programming doesn’t have its uses; functional programming styles **work very well for mathematical applications**.

**Object oriented** programming works very well for robots; the structure of object oriented programs parallels almost perfectly with the structure of a robot:

![idk]()

Now, as far as **Imperative** programming is concerned, by looking at an autonomous routine from last season, we can see how this parallels an imperative programming style.

![idk]()

It is evident that this is almost exactly how an **imperative** program would look; the code is laid out in a series of distinct steps.

As far as **software architectures** are concerned, the decision on which one to use wasn’t as easy. Each one of these architectures has the potential to work just fine. Since this is the case, we have to narrow our options down by getting rid of the architectures that might overcomplicate the program. Keeping a software model simple is a great way to keep code maintained properly.

The first one to go would probably be the **broker pattern**. While this could potentially work, there is one aspect of the broker pattern that could overcomplicate things. This aspect is where “services” will “publish” their capabilities to a broker. This could work well in applications where the software is used by many different organizations; each one submitting their own capabilities to the broker, however, this is not the case with our robot. It will have predefined capabilities that won’t change very much over time. Even if it does change, there would be no reason to have the extra layer to heighten compatibility.

The next architecture to go is decided to be the **event-bus pattern**. This pattern is great for things like notification services. Although this pattern could work pretty well in handling events like controller input or changes in game state, this is still an over-complication.

This leaves the **layered pattern**. The layered pattern is very adaptable to different situations, usually you have a top-level UI layer and then each layer down handles continually lower-level responsibilities. For our robot I would probably make one change, the top layer wouldn’t contain UI, rather, it would watch for changes in match state (disablement, autonomous, driver control, etc…) Then, the next layer down would handle any UI: (things like an autonomous selector or information displayed on the brain screen.) Finally, the bottom-most layer would handle the actual robot motion. Any layers below this will probably be method calls to any classes we make.

