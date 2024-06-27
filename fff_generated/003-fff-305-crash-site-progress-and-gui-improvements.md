<!-- Command for generating this post: python create_new_blogpost.py --blogpost_number 305 --prev_blogpost_as_examples 301 302 303 304 -->

# Friday Facts #305 - Crash site progress and GUI improvements

### Crash site progress Albert, V453000

Over the past few weeks, we've been hard at work on finalizing the new crash site for the introduction campaign. As mentioned in FFF-301, this is one of the last major tasks before we can call 0.17 stable. We're excited to share some of the progress we've made.

The main crashed spaceship is now fully modeled and textured:

*Image fff-305-crashed-spaceship*

We've put a lot of effort into making it look appropriately damaged and worn, while still maintaining a sleek sci-fi aesthetic that contrasts with the more rugged look of the player's crafted machines. Various debris and smaller crashed components are scattered around the site to really sell the impact.

We've also been populating the area with more environmental details:

*Image fff-305-crash-site-environment*

Scorched earth, fallen trees, and impact craters help tell the story of the crash. We're still iterating on the exact placement to guide the player's initial exploration in an intuitive way.

The new crash site entities mentioned in FFF-301 have received some polish as well:

*Image fff-305-crash-site-entities*

We've adjusted their color schemes and added some weathering effects to make them feel more integrated with the environment. The goal is to make them recognizable as advanced versions of machines the player will craft later, while still feeling alien and mysterious.

### GUI improvements Twinsen

While working on stabilizing 0.17, we've also been making some quality-of-life improvements to the game's interface. One area we've focused on is the research screen:

*Image fff-305-research-gui*

We've added the ability to search and filter technologies, making it easier to find what you're looking for in the later stages of the game. The layout has also been tweaked to show more information at a glance, including clearer prerequisite connections.

Another small but oft-requested feature is the ability to see the contents of pipes when hovering over them:

*Image fff-305-pipe-contents*

This should make it easier to debug issues with your fluid systems without needing to place pumps everywhere.

### Ongoing optimization Rseding

Performance is always a priority for us, and we're continuously looking for ways to improve it. This week, we've made some optimizations to how circuit networks are processed:

*Image fff-305-circuit-network-performance*

By caching some commonly accessed data and reducing unnecessary recalculations, we've seen up to a 15% improvement in update time for large circuit networks. This should be especially noticeable in complex combinator setups.

We're also investigating ways to further optimize belt performance, as this continues to be one of the most CPU-intensive parts of the game in large factories. Early experiments with a new compression algorithm for belt item data look promising, but we need to do more testing before we can commit to implementing it.

### Looking ahead

With the crash site nearing completion and these various improvements in place, we're getting closer to calling 0.17 stable. Once that milestone is reached, we'll be able to focus more on new features and content for future updates.

As always, we're grateful for the community's patience and feedback as we work towards making Factorio the best it can be. Let us know what you think about these changes on our [forum](https://forums.factorio.com/73700).

[Discuss on our forums](https://forums.factorio.com/73700) [Discuss on Reddit](https://www.reddit.com/r/factorio/comments/cgy3jk/friday_facts_305_crash_site_progress_and_gui/)
[ Subscribe by email ](https://newsletter.factorio.com/subscription/Km9uSnxm9)