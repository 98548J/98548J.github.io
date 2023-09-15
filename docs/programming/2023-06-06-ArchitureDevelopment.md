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
# Define Problem

With the completion of the test bed robot, we need to decide how we will program the test bed and any other robots we build. 

The problem is, that we do not know what software architecture to use for any of our programs.

{: .design}
# Constraints

We intend to use the same **architecture** for any prototypes and/or competition robots. Because of this, we will need to adhere to the constraints for competition programs. The main requirement for competition programs is that the program uses the **Competition Template**.

{: .design}
# Generate Concepts

Here is a list of paradigms we could use for our robot:

* Imperative programming.
* Functional programming.
* Object Oriented programming (OOP).

Also, below is a list of architectures we could use for our robot. These architectures can be described at [Towards Data Science](https://towardsdatascience.com/10-common-software-architectural-patterns-in-a-nutshell-a0b47a1e9013).

* Layered Pattern.
* Event-Bus Pattern.
* Broker Pattern.

{: .design}
# Our Decision

## Programming Paradigm -

I did not think a **Functional** style of programming would be appropriate, because it is common for functions to behave differently depending on when they are called. 

An example of this could be an “Update()” function or method for a PID. This “Update()” function would simply allow the PID to adapt to any changes in the **robot’s position or velocity**. However, the result, or effect, of the function **depends** on the robot’s position or velocity! 

This dependency on the environment or situation at hand is contrary to a functional programming style.

**Object oriented** programming works very well for robots; the structure of object oriented programs parallels almost perfectly with the structure of a robot:

{: .emphasize}
* A robot is made up of **subsystems** that each have specific **functionalities**.
* A robot can be modeled with multiple **classes** that have specific **methods**.


Now, as far as **Imperative** programming is concerned, by looking at an autonomous routine from last season, we can see how this parallels an imperative programming style.

Below you can see a simple autonomous routine that we used last season:

```cpp
void rightSimple()
{
    //Reset sensors:
    Inertial.setHeading(0, deg);

    //Drive twenty inches at a heading of zero degrees:
    DriveWithAngles({{20, 0}}, 100, true, false, 1.25);

    //Face towards the roller:
    TurnAt(90, 100, true, false, 1);

    //Spin roller to correct color:
    SetRoller(globalColor, false);
}
```

It is evident that this is almost exactly how an **imperative** program would look; the code is laid out in a series of distinct steps.

## Software Architecture -

As far as **software architectures** are concerned, the decision on which one to use wasn’t as easy. Each one of these architectures has the potential to work just fine. Since this is the case, we have to narrow our options down by getting rid of the architectures that might overcomplicate the program. Keeping a software model simple is a great way to keep code maintained properly.

The first one to go would probably be the **broker pattern**. While this could potentially work, there is one aspect of the broker pattern that could overcomplicate things. This aspect is where “services” will “publish” their capabilities to a broker. This could work well in applications where the software is used by many different organizations; each one submitting their own capabilities to the broker, however, this is not the case with our robot. It will have predefined capabilities that won’t change very much over time. Even if it does change, there would be no reason to have the extra layer to heighten compatibility.

The next architecture to go is decided to be the **event-bus pattern**. This pattern is great for things like notification services. Although this pattern could work pretty well in handling events like controller input or changes in game state, this is still an over-complication.

This leaves the **layered pattern**. The layered pattern is very adaptable to different situations, usually you have a top-level UI layer and then each layer down handles continually lower-level responsibilities. For our robot I would probably make one change, the top layer wouldn’t contain UI, rather, it would watch for changes in match state (disablement, autonomous, driver control, etc…) Then, the next layer down would handle any UI (things like an autonomous selector or information displayed on the brain screen). Finally, the bottom-most layer would handle the actual robot motion. Any layers below this will probably be method calls to any classes we make.

{: .decision}
> Here is a summary of what we decided to use:
> * Concept [#3]({{site.url}}/docs/programming/2023-06-06-ArchitureDevelopment.html#:~:text=Object%20Oriented%20programming%20(OOP).), an ***Object Oriented*** paradigm for robot functions.
> * Concept [#1]({{site.url}}/docs/programming/2023-06-06-ArchitureDevelopment.html#:~:text=Imperative%20programming.), an ***Imperative*** paradigm for robot autonomouses.
> * Concept [#1]({{site.url}}/docs/programming/2023-06-06-ArchitureDevelopment.html#:~:text=Data%20Science.-,Layered%20Pattern.,-Event%2DBus%20Pattern), a ***Layered*** software architecture.

{: .design}
# Develop Solution

The next step is to begin deciding exactly how we will program this.

First I will outline what the layered pattern will look and behave like.

Below you can see how the layered pattern will most likely behave. Keep in mind that this is our first look at the layered architecture of our program and it is likely to change:

![LayeredPattern](/assets/programming/Layered%20Architecture.png){: width="75%"}

Whenever the mode changes, the **mode handling layer** (first layer) will recognize this and switch modes. Switching modes will probably involve ending certain tasks that are no longer needed and starting new ones that are used for the current mode.

The **UI layer** (second layer) will handle any UI required for the current mode, this could include buttons for an autonomous selector, or simply information displayed during driver control.

The **robot operation layer** (third layer) is the layer where any commands to move the robot or operate any of its functions will take place.

Finally, below we can see a basic **UML** diagram showing the structure of the various classes we will use for our first [testbed robot]({{site.url}}/docs/engineering/2023-06-05-OdometryTestRig.html): 

![RobotClassUML](/assets/programming/UML%20Odometry.png)

{: .design}
# Implement Solution


