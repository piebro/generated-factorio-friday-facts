<!-- Command for generating this post: python create_new_blogpost.py --blogpost_number 417 --prev_blogpost_as_examples 373 381 411 --bullet_points "Space-based energy collection (e.g. Dyson swarms)" -->

# Friday Facts #417 - Space-based Energy Collection

Hello, engineers! Today we're excited to share some details about one of the late-game energy solutions coming in the Space Age expansion: space-based energy collection, or as we like to call it, the Dyson swarm.

*Image fff-417-dyson-swarm-concept* 

_Concept art of the Dyson swarm by Earendel_

### Why go solar in space?kovarex

As you venture further into the cosmos, energy demands skyrocket. Powering advanced space platforms, interplanetary logistics, and resource-hungry research becomes increasingly challenging. While nuclear power serves well in the early space game, we wanted to provide a truly ambitious late-game energy solution that would push players to think on a stellar scale.

Enter the Dyson swarm - a vast array of solar collectors orbiting close to the star, beaming collected energy back to your platforms and planets. Unlike a solid Dyson sphere, our swarm consists of many individual components that can be incrementally built and expanded.

### Building the swarmV453000

Constructing a Dyson swarm is no small feat. It requires significant infrastructure and a multi-step production chain:

1. Launch specialized rockets carrying swarm components
2. Assemble components into collectors in a designated orbital construction area
3. Move completed collectors into their final orbits around the star

*video fff-417-swarm-construction*

_Orbital construction of Dyson swarm collectors_

The process starts with manufacturing swarm components on planets or space platforms. These are then packaged into special cargo rockets and launched towards the star. An orbital construction platform intercepts these payloads and uses robotic assemblers to construct the actual solar collectors.

Once complete, small ion engines on the collectors activate, slowly moving them into their designated orbits. As more collectors are added, you'll see the swarm grow visually around the star.

### Energy transmissionPosila

Of course, collecting energy is only half the battle - we need to get that power back to where it's needed. For this, we've introduced a new long-range wireless power transmission system.

*Image fff-417-energy-transmission*

_Diagram of the energy transmission network_

Large receiver arrays can be built on planets or platforms to intercept the energy beamed from the swarm. These connect to your power grid like any other generator. The catch is that transmission efficiency drops over extreme distances, so positioning your receivers strategically becomes important.

We've had to develop some new underlying systems to handle the vast scales involved:

- A custom coordinate system to track object positions across the entire star system
- Optimization of energy calculations to handle potentially thousands of collectors and receivers
- Visual effects to represent the energy beams without killing performance

### Balancing act Earendel

Introducing such a powerful energy source late in the game presents some interesting balancing challenges. We want the Dyson swarm to feel appropriately rewarding for the massive investment required, while still preserving interesting choices in your power infrastructure.

Some key balancing points we're working on:

- Swarm components require exotic materials only found on distant planets, encouraging exploration
- Maintenance costs increase with swarm size, preventing unlimited scaling
- Efficiency gains from upgrading collectors and receivers, providing a long-term optimization path
- Integration with the existing power network, allowing for hybrid setups

*Image fff-417-power-graph*

_Power production graph showing Dyson swarm contribution_

### The futureFearghall

While we're excited about the current implementation, we have more ideas we'd like to explore if time permits:

- Visual customization options for the swarm's appearance
- Special events like solar flares that affect swarm performance
- Using the swarm as a power source for experimental late-game technologies

We're also curious to see what creative uses players might find for nearly unlimited energy in space. Will you build massive automated factory platforms? Power exotic matter research? Or perhaps attempt to move entire planets?

* * *

That's all for this week! We're looking forward to seeing your solar empires spread across the stars. As always, let us know your thoughts and ideas in the usual places.

[Discuss on our forums](https://forums.factorio.com/viewtopic.php?f=38&t=12345) [Discuss on Reddit](https://www.reddit.com/r/factorio/comments/abcdef)
[Subscribe by email](https://newsletter.factorio.com/subscription/Km9uSnxm9)