# Repository Guidelines

## API Doc
请严格遵守一下文档约束。

### Tooltips Code
== <code>abs(number)</code> ==
Computes the absolute value of a <code>number</code>.

returns <code>number</code> if <code>number</code> is positive, <code>-number</code> otherwise.

takes the time of <code>1</code> operation to execute.

example usage:
<syntaxhighlight lang="python">
abs(-69)
</syntaxhighlight>

== <code>add(element)</code> ==
Adds <code>element</code> to the set.

returns <code>None</code>

takes the time of <code>1</code> operations to execute.

example usage:
<syntaxhighlight lang="python">
set = {0}
set.add(1)
</syntaxhighlight>

== <code>append</code> ==

<code>list.append(element)</code> adds <code>element</code> to the end of the <code>list</code>.

== <code>break</code> ==

Breaks out of a loop and continues executing the statements after the loop. If there are nested loops this always affects the innermost loop.

== <code>can_harvest()</code> ==
Used to find out if plants are fully grown.

returns <code>True</code> if there is an entity under the drone that is ready to be harvested, <code>False</code> otherwise.

takes the time of <code>1</code> operation to execute.

example usage:
<syntaxhighlight lang="python">
if can_harvest():
    harvest()
</syntaxhighlight>

== <code>clear()</code> ==
Removes everything from the farm, and resets the drone position to <code>(0,0)</code>.

returns <code>None</code>

takes the time of <code>200</code> operations to execute.

example usage:
<syntaxhighlight lang="python">
clear()
</syntaxhighlight>

== <code>continue</code> ==

Continues to the next loop iteration immediately. If there are nested loops this always affects the innermost loop.

== <code>def</code> ==

Defines a function.

== <code>do_a_flip()</code> ==
Makes the drone do a flip! This action is not affected by speed upgrades.

returns <code>None</code>

takes 1s to execute.

example usage:
<syntaxhighlight lang="python">
while True:
    do_a_flip()
</syntaxhighlight>

== <code>[[Entities]]</code> ==

Contains all plants and other entities that can be on a ground tile of the farm. Can be iterated using a <code>for</code> loop.
<div class="toccolours mw-collapsible mw-collapsed" data-expandtext="show values" data-collapsetext="hide values" style="max-width:32em"><code>values</code>
<div class="mw-collapsible-content">
: .Bush
: .Carrot
: .Grass
: .Hedge
: .Pumpkin
: .Sunflower
: .Treasure
: .Tree
</div></div>

== <code>False</code> ==

A boolean value that is always false.

== <code>for</code> ==

A loop that iterates all elements of a sequence. Some languages call this a "foreach" loop.

== <code>get_companion()</code> ==
Get the companion preference of the plant under the drone.

returns a list of the form <code>[companion_type, companion_x_position, companion_y_position]</code>

takes the time of <code>1</code> operation to execute.

example usage:
<syntaxhighlight lang="python">
companion = get_companion()
if companion != None:
	print(comp)
</syntaxhighlight>

== <code>get_cost(thing)</code> ==
Gets the cost of a <code>thing</code>

If <code>thing</code> is an item get the cost of buying it when using <code>trade(item)</code>.
<br>
If <code>thing</code> is an entity get the seed needed to plant it.
<br>
If <code>thing</code> is an unlock get the cost of unlocking it.

returns a dictionary with items as keys and numbers as values. Each item is mapped to how much of it is needed.

takes the time of <code>1</code> operation to execute.

example usage:
<syntaxhighlight lang="python">
cost = get_cost(Unlocks.Carrots)
for item in cost:
    if num_items(item) < cost[item]:
        print("not enough items to unlock carrots")
</syntaxhighlight>

== <code>get_entity_type()</code> ==
Find out what entity is under the drone.

returns <code>None</code> if the tile is empty, otherwise returns the type of the entity under the drone.

takes the time of <code>1</code> operation to execute.

example usage:
<syntaxhighlight lang="python">
if get_entity_type() == Entities.Grass:
    harvest()
</syntaxhighlight>

== <code>get_ground_type()</code> ==
Find out what ground is under the drone.

returns the type of the ground under the drone.

takes the time of <code>1</code> operation to execute.

example usage:
<syntaxhighlight lang="python">
if get_ground_type() != Grounds.Soil:
    till()
</syntaxhighlight>

== <code>get_pos_x()</code> ==
Gets the current x position of the drone.
<br>
The x position starts at <code>0</code> in the <code>West</code> and increases in the <code>East</code> direction.

returns a number that is the current x coordinate of the drone.

takes the time of <code>1</code> operation to execute.

example usage:
<syntaxhighlight lang="python">
x, y = get_pos_x(), get_pos_y()
</syntaxhighlight>

== <code>get_pos_y()</code> ==
Gets the current y position of the drone.
<br>
The y position starts at <code>0</code> in the <code>South</code> and increases in the <code>North</code> direction.

returns a number that is the current x coordinate of the drone.

takes the time of <code>1</code> operation to execute.

example usage:
<syntaxhighlight lang="python">
x, y = get_pos_x(), get_pos_y()
</syntaxhighlight>

== <code>get_time()</code> ==
Get the current game time.

returns the time since the start of the game in seconds.

takes the time of <code>1</code> operation to execute.

example usage:
<syntaxhighlight lang="python">
start = get_time()

do_something()

time_passed = get_time() - start
</syntaxhighlight>

== <code>get_water</code> ==
Get the current water level under the drone.

returns the water level under the drone as a number between <code>0</code> and <code>1</code>.

takes the time of <code>1</code> operation to execute.

example usage:
<syntaxhighlight lang="python">
if get_water() < 0.5:
    use_item(Items.Water_Tank)
</syntaxhighlight>

== <code>get_world_size()</code> ==
Get the current size of the farm.

returns the size of the grid east to west.

takes the time of <code>1</code> operation to execute.

example usage:
<syntaxhighlight lang="python">
for i in range(get_world_size()):
    move(North)
</syntaxhighlight>

== <code>[[Grounds]]</code> ==

Contains all possible ground tiles. Can be iterated using a <code>for</code> loop.
<div class="toccolours mw-collapsible mw-collapsed" data-expandtext="show values" data-collapsetext="hide values" style="max-width:32em"><code>values</code>
<div class="mw-collapsible-content">
: .Soil
: .Grassland
</div></div>

== <code>harvest()</code> ==
Harvests the entity under the drone.
<br>
If you harvest an entity that isn't harvestable it just gets destroyed.

returns <code>True</code> if an entity was removed, <code>False</code> otherwise.

takes the time of <code>200</code> operations to execute if an entity was removed, <code>1</code> operation otherwise.

example usage:
<br>
<code>harvest()</code>

== <code>[[if]]</code> ==

Executes code if the condition is <code>True</code>.

== <code>insert</code> ==

<code>list.insert(i, element)</code> inserts <code>element</code> into the <code>list</code> at index <code>i</code>.

== <code>[[Items]]</code> ==

Contains all items that can be in the inventory. Can be iterated using a <code>for</code> loop.
<div class="toccolours mw-collapsible mw-collapsed" data-expandtext="show values" data-collapsetext="hide values" style="max-width:32em"><code>values</code>
<div class="mw-collapsible-content">
: .Carrot
: .Carrot_Seed
: .Empty_Tank
: .Fertilizer
: .Gold
: .Hay
: .Piggy
: .Power
: .Pumpkin
: .Pumpkin_Seed
: .Sunflower_Seed
: .Water_Tank
: .Wood
</div></div>

== <code>len(collection)</code> ==
Get the number of elements in a list, set, dict or tuple.

returns the length of the <code>collection</code>

takes the time of <code>1</code> operation to execute.

example usage:
<syntaxhighlight lang="python">
for i in range(len(list)):
    list[i] += 1
</syntaxhighlight>

== <code>max(a,b)</code> ==
Gets the maximum of a sequence of elements or several passed arguments.
<br>
Can be used on numbers and strings.

overloads:
<br>
<code>max(a,b,c)</code>: Returns the maximum of the passed arguments.
<br>
<code>max(sequence)</code>: Returns the maximum of all values in a sequence.

takes the time of <code>1</code> operation to execute.

example usage:
<syntaxhighlight lang="python">
max([3,6,34,16])
</syntaxhighlight>

== <code>measure()</code> ==
Can measure some values on some entities. The effect of this depends on the entity.

returns the number of petals when measuring a sunflower.
<br>
returns <code>None</code> for all other entities.

takes the time of <code>1</code> operations to execute.

example usage:
<syntaxhighlight lang="python">
num_petals = measure()
</syntaxhighlight>

== <code>min(a,b)</code> ==
Gets the minimum of a sequence of elements or several passed arguments.
<br>
Can be used on numbers and strings.

overloads:
<br>
<code>min(a,b,c)</code>: Returns the minimum of the passed arguments.
<br>
<code>min(sequence)</code>: Returns the minimum of all values in a sequence.

takes the time of <code>1</code> operation to execute.

example usage:
<syntaxhighlight lang="python">
min([3,6,34,16])
</syntaxhighlight>

== <code>move(direction)</code> ==
Moves the drone into the specified <code>direction</code> by one tile.
<br>
If the drone moves over the edge of the farm it wraps back to the other side of the farm.
{|
|<code>East</code>||= right
|-
|<code>West </code>||= left
|-
| <code>North</code>||= up
|-
| <code>South</code>||= down
|}

returns <code>True</code> if the drone moved, <code>False</code> otherwise.

takes the time of <code>200</code> operations to execute if the drone moved, <code>1</code> operation otherwise.

example usage:
<syntaxhighlight lang="python">
move(North)
</syntaxhighlight>

== <code>None</code> ==

A value that represents that there is no value.

== <code>num_items(item)</code> ==
Find out how much of <code>item</code> you currently have.

takes the time of <code>1</code> operation to execute.

returns the number of <code>item</code> currently in your inventory.

example usage:
<syntaxhighlight lang="python">
if num_items(Items.Fertilizer) == 0:
    trade(Items.Fertilizer)
</syntaxhighlight>

== <code>num_unlocked(thing)</code> ==
Used to check if an unlock, entity, ground or item is already unlocked.

returns <code>1</code> plus the number of times <code>thing</code> has been upgraded if <code>thing</code> is upgradable. Otherwise returns <code>1</code> if thing is unlocked, <code>0</code> otherwise.

takes the time of <code>1</code> operation to execute.

example usage:
<syntaxhighlight lang="python">
if num_unlocked(Unlocks.Multi_Trade) > 0:
    trade(Items.Carrot_Seed, 10)
else:
    for i in range(10):
        trade(Items.Carrot_Seed)
</syntaxhighlight>

== <code>plant(entity)</code> ==
Plants the specified entity under the drone if it can be planted.
<br>
Otherwise it just does nothing.

returns <code>True</code> if it succeeded, <code>False</code> otherwise.

takes the time of <code>200</code> operations to execute if it succeeded, <code>1</code> operation otherwise.

example usage:
<syntaxhighlight lang="python">
plant(Entities.Bush)
</syntaxhighlight>

== <code>pop</code> ==

<code>list.pop()</code> removes the last element from the <code>list</code>.
<br>
<code>list.pop(i)</code> removes the element at the index <code>i</code> from the <code>list</code>.

== <code>print(something)</code> ==
Prints <code>something</code> into the air above the drone using smoke. This action is not affected by speed upgrades.
<br>
Multiple values can be printed at once.

returns <code>None</code>

takes 1s to execute.

example usage:
<syntaxhighlight lang="python">
print("ground:", get_ground_type())
</syntaxhighlight>

== <code>quick_print()</code> ==
Prints a value just like print() but it doesn't stop to write it into the air so it can only be found in the output page.

returns <code>None</code>

takes the time of <code>1</code> operations to execute.

example usage:
<syntaxhighlight lang="python">
quick_print("hi mom")
</syntaxhighlight>

== <code>range()</code> ==
Creates a sequence of numbers.

overloads:
<br>
<code>range(end)</code> returns a sequence of numbers from <code>0</code>(inclusive) to <code>end</code>(exclusive).
<br>
<code>range(start,end)</code> returns a sequence of numbers from <code>start</code>(inclusive) to <code>end</code>(exclusive).
<br>
<code>range(start,end,step)</code> returns a sequence of numbers from <code>start</code>(inclusive) to <code>end</code>(exclusive) going at steps of size <code>step</code>

takes the time of <code>1</code> operation to execute.

example usage:
<syntaxhighlight lang="python">
for i in range(10):
	print(i)

for i in range(2,6):
	print(i)

for i in range(10, 0, -1):
	print(i)
</syntaxhighlight>

== <code>remove</code> ==

<code>list.remove(element)</code> removes the first occurrence of <code>element</code> from the <code>list</code>.

== <code>till()</code> ==
Tills the ground under the drone if it isn't tilled yet.
<br>
Otherwise it turns it back into grassland.

returns <code>None</code>

takes the time of <code>200</code> operations to execute.

Usage:
<syntaxhighlight lang="python">
till()
</syntaxhighlight>

== <code>timed_reset()</code> ==
Starts a timed run for the leaderboard. Saves the game before the run and then loads that save afterwards so you can't gain any items during the run.

returns <code>None</code>

takes the time of <code>200</code> operations to execute.

example usage:
<syntaxhighlight lang="python">
timed_reset()
</syntaxhighlight>

== <code>trade(item)</code> ==
Tries to buy the specified item.
<br>
If the <code>item</code> cannot be bought or you don't have the required resources it simply does nothing.

overloads:
<br>
<code>trade(item)</code>: Buy the <code>item</code> once.
<br>
<code>trade(item, n)</code>: If <code>Unlocks.Multi_Trade</code> is unlocked this buys the <code>item</code> <code>n</code> times immediately. If you can't afford all <code>n</code> items it buys none at all. If <code>Unlocks.Multi_Trade</code> is not unlocked it throws an error.

returns <code>True</code> if it was able to buy the items, <code>False</code> otherwise.

takes the time of <code>200</code> operations to execute if it succeeded, <code>1</code> operation otherwise.

example usage:
<syntaxhighlight lang="python">
if num_unlocked(Unlocks.Multi_Trade) > 0:
    trade(Items.Carrot_Seed, 10)
else:
    for i in range(10):
        trade(Items.Carrot_Seed)
</syntaxhighlight>

== <code>True</code> ==

A boolean value that is always true.

== <code>unlock(unlock)</code> ==
Has exactly the same effect as clicking the button corresponding to <code>unlock</code> in the research tree.

returns <code>True</code> if it succeeded unlocking it, <code>False</code> otherwise.

takes the time of <code>200</code> operations to execute if it succeeded, <code>1</code> operation otherwise.

example usage:
<syntaxhighlight lang="python">
unlock(Unlocks.Carrots)
</syntaxhighlight>

== <code>[[Unlocks]]</code> ==

Contains all the unlocks and upgrades in the research menu. Can be iterated using a <code>for</code> loop.
<div class="toccolours mw-collapsible mw-collapsed" data-expandtext="show values" data-collapsetext="hide values" style="max-width:32em"><code>values</code>
<div class="mw-collapsible-content">
: .Auto_Unlock
: .Carrots
: .Cost_Lists
: .Debug
: .Expand
: .Fertilizer
: .Grass
: .Lists
: .Loops
: .Mazes
: .Multi_Trade
: .Operators
: .Plant
: .Polyculture
: .Pumpkins
: .Reset
: .Senses
: .Speed
: .Sunflowers
: .Timed_Reset
: .Trees
: .Variables
: .Watering
</div></div>

== <code>use_item(item)</code> ==
Uses up one of the specified item. Can only be used with some items like <code>Items.Water_Tank</code>.

returns <code>True</code> if an item was used, <code>False</code> otherwise.

takes the time of <code>200</code> operations to execute if it succeeded, <code>1</code> operation otherwise.

example usage:
<syntaxhighlight lang="python">
use_item(Items.Fertilizer)
</syntaxhighlight>

== <code>while</code> ==

Keeps looping until the condition is false.

### Entities
== <code>Grass</code> ==

Grows automatically. Harvest it to obtain <code>Items.Hay</code>.

Average seconds to grow: 0.5<br>
Grows on: turf or soil

== <code>Bush</code> ==

A small bush that drops <code>Items.Wood</code>.

Average seconds to grow: 4
Grows on: turf or soil

== <code>Tree</code> ==

Trees drop more wood than bushes. They take longer to grow if other trees grow next to them.

Average seconds to grow: 7<br>
Grows on: turf or soil

== <code>Carrots</code> ==

Carrots!

Average seconds to grow: 6<br>
Grows on: soil
{| class="wikitable"
|+Plant Cost
|1||[[Tooltips_Items#Carrot_Seed|Items.Carrot_Seed]]
|}

== <code>Pumpkin</code> ==

Pumpkins grow together when they are next to other fully grown pumpkins. About 1 in 5 pumpkins dies when it grows up.<br>
When you harvest a pumpkin you get <code>Items.Pumpkin</code> equal to the side length of the mega pumpkin cubed. (A 2x2 pumpkin yields 8 Items.Pumpkin)

Average seconds to grow: 2<br>
Grows on: soil
{| class="wikitable"
|+Plant Cost
|1||[[Tooltips_Items#Pumpkin_Seed|Items.Pumpkin_Seed]]
|}

== <code>Sunflower</code> ==

Sunflowers collect the power from the sun. Harvesting them will give you <code>Items.Power</code> equal to the square root of the number of sunflowers in the farm.<br>
If you harvest a sunflower that doesn't have the maximum number of petals all the sunflowers will die.

Average seconds to grow: 5<br>
Grows on: soil
{| class="wikitable"
|+Plant Cost
|1||[[Tooltips_Items#Sunflower_Seed|Items.Sunflower_Seed]]
|}

== <code>Cactus</code> ==

Cacti come in 10 different sizes. When harvested, all cacti on the field will be harvested. Only those that are in sorted order will drop <code>Items.Cactus</code>.

Average seconds to grow: 1<br>
Grows on: soil
{| class="wikitable"
|+Plant Cost
|1||[[Tooltips_Items#Cactus_Seed|Items.Cactus_Seed]]
|}

== <code>Hedge</code> ==

Part of the maze. Grow a maze by fertilizing a fully grown bush.

== <code>Treasure</code> ==

A treasure that contains gold equal to the area of the maze in which it is hidden (25 gold on a 5x5 maze). It can be harvested like a plant.

== <code>Dinosaur</code> ==

A majestic dinosaur. It moves around randomly but won't move for a while after being measured. Harvesting it harvests all adjacent dinosaurs of the same type and makes them drop <code>Items.Bone</code>.

Average seconds to grow: 0.2<br>
Grows on: turf or soil

### Grounds
== <code>Grassland</code> ==

The default ground. Grass will automatically grow on it.

== <code>Soil</code> ==

Calling <code>till()</code> turns the ground into this. Calling <code>till()</code> again changes it back to turf.

### Items
== <code>Carrot</code> ==

Obtained by harvesting carrots.

== <code>Carrot_Seed</code> ==

Used to grow carrots by calling <code>plant(Entities.Carrot)</code> on empty soil.
{| class="wikitable"
|+Trade Cost<ref name="trade_cost">The cost shown is only the base cost. It can increase based on the upgrade level of what you're buying.</ref>
|1||Wood
|-
|1||Hay
|}

== <code>Empty_Tank</code> ==

Empty tanks automatically turn into water tanks over time.
{| class="wikitable"
|+Trade Cost
|5||Wood
|}

== <code>Fertilizer</code> ==

Call <code>use_item(Items.Fertilizer)</code> to instantly grow the plant under the drone by 2s.
{| class="wikitable"
|+Trade Cost
|10||Pumpkin
|}

== <code>Gold</code> ==

Found in treasure chests in mazes.

== <code>Hay</code> ==

Obtained by cutting grass.

== <code>Power</code> ==

Obtained by harvesting sunflowers. The drone automatically uses this to move twice as fast.

== <code>Pumpkin</code> ==

Obtained when harvesting pumpkins.

== <code>Pumpkin_Seed</code> ==

Used to grow pumpkins by calling <code>plant(Entities.Pumpkin)</code> on empty soil.
{| class="wikitable"
|+Trade Cost<ref name="trade_cost">The cost shown is only the base cost. It can increase based on the upgrade level of what you're buying.</ref>
|1||Carrot
|}

== <code>Sunflower_Seed</code> ==

Used to grow sunflowers by calling <code>plant(Entities.Sunflower)</code> on empty soil.
{| class="wikitable"
|+Trade Cost<ref name="trade_cost">The cost shown is only the base cost. It can increase based on the upgrade level of what you're buying.</ref>
|1||Carrot
|}

== <code>Water</code> ==

Used to water the ground by calling <code>use_item(Items.Water)</code>.

== <code>Wood</code> ==

Obtained from bushes and trees.

== <code>Cactus</code> ==

Obtained when harvesting sorted cacti.

== <code>Cactus_Seed</code> ==

Used to grow cacti by calling <code>plant(Entities.Cactus)</code> on empty soil.

== <code>Egg</code> ==

Call <code>use_item(Items.Egg)</code> to hatch a majestic dinosaur.

== <code>Bones</code> ==

The bones of an ancient creature.

== Footnotes ==
<references />

### Unlocks
== <code>Auto_Unlock</code> ==

Automatically unlock things.

== <code>Benchmark</code> ==

Functions to help measure performance.

== <code>Cactus</code> ==

Unlock: Cactus!
Upgrade: Increases the yield of cactus and the cost of cactus seeds."""

== <code>Carrots</code> ==

Unlock: Till the soil and plant carrots.
Upgrade: Increases the yield of carrots and the cost of carrot seeds.

== <code>Costs</code> ==

Allows access to the cost of things.

== <code>Debug</code> ==

Tools to help with debugging programs.

== <code>Debug_2</code> ==

Functions to temporarily slow down the execution and make the grid smaller.

== <code>Dictionaries</code> ==

Get access to dictionaries and sets.

== <code>Dinosaurs</code> ==

Unlock: Majestic ancient creatures.
Upgrade: Increases the yield of dinosaurs and the cost of eggs.

== <code>Expand</code> ==

Unlock: Expands the farm land and unlocks movement.
Upgrade: Expands the farm. This also clears the farm.

== <code>Fertilizer</code> ==

<s>Grow plants instantly.</s><ref>Text is incorrect, needs to be updated in-game.</ref>
Instantly reduces time to maturity.<ref>Possible corrected text.</ref>

== <code>Functions</code> ==

Define your own functions.

== <code>Grass</code> ==

Increases the yield of grass.

== <code>Leaderboard</code> ==

Join the leaderboard for the fastest reset time.

== <code>Lists</code> ==

Use lists to store lots of values.

== <code>Loops</code> ==

Unlocks a simple while loop.

== <code>Mazes</code> ==

Unlock: A maze with a treasure in the middle.
Upgrade: Increases the gold in treasure chests.

== <code>Multi_Trade</code> ==

Trade multiple items at once.

== <code>Operators</code> ==

Arithmetic, comparison and logic operators.

== <code>Plant</code> ==

Unlocks planting.

== <code>Polyculture</code> ==

Use companion planting to increase the yield.

== <code>Pumpkin</code> ==

Unlock: Pumpkins!
Upgrade: Increases the yield of pumpkins and the cost of pumpkin seeds.

== <code>Senses</code> ==

The drone can see what's under it and where it is.

== <code>Speed</code> ==

Increases the speed of the drone.

== <code>Sunflowers</code> ==

Unlock: Sunflowers and Power.
Upgrade: Increases the power gained from sunflowers.

== <code>Trees</code> ==

Unlock: Unlocks trees.
Upgrade: Increases the yield of bushes and trees.

== <code>Utilities</code> ==

Unlocks the <code>min()</code>, <code>max()</code> and <code>abs()</code> functions.

== <code>Variables</code> ==

Assign values to variables.

== <code>Watering</code> ==

Water the plants to make them grow faster.

### Plant growth
This page documents information about plant growth that the game doesn't provide.

== Plant growth time distribution ==
The growth time of each plant is a random number with a uniform distribution within a range depending on the plant. The ranges are provided by the following table:
{| class="wikitable"
|+ Growth Time (in seconds)
|-
! Plant !! Minimum !! Maximum
|-
| [[Grass]] || 0.5 || 0.5
|-
| [[Bush]] || 3.2 || 4.8
|-
| [[Carrots]] || 4.8 || 7.2
|-
| [[Tree]] || 5.6 || 8.4
|-
| [[Pumpkins|Pumpkin]] || 0.2 || 3.8
|-
| [[Cactus]] || 0.9 || 1.1
|-
| [[Sunflowers|Sunflower]] || 4.0 || 6.0
|-
| [[Dinosaurs|Dinosaur]] || 0.18 || 0.22
|}

### Execution Details
This page documents details about how the game executes instructions, which the game does not provide.

===The Base Operation Time is 2.5ms===
This equates to 0.5 seconds for a 200-operation "action" such as <code>harvest</code> at the beginning of the game. All upgrades reduce this time linearly, so 500% speed upgrade means all operations take 1/5th the normal time, or 0.5ms. Having [[Sunflowers|Sunflower]] power doubles speed.

===All Side-Effects Happen at the Start of the Function===
For instance: When <code>harvest()</code> is called, the harvesting action happens immediately, then 200 operations of delay pass. When <code>plant()</code> is called, the entity is planted and then 200 operations (during which the plant grows) pass. Similarly, when <code>get_time()</code> is called, the time is gotten immediately, and then 1 operation passes.

===Power is Burned Faster with More Speed Upgrades===
1 [[Sunflowers|Sunflower]] power lasts 30 "actions," or 6000 total operations. Since operations pass at a constant rate, power is also consumed at a constant rate, as long as code is executing. This rate is proportional to how many speed upgrades you have.

===Operations Add Up Faster than you Think===
There is (at least) one operation for every "step" you see when single-stepping code with the single-step arrow. This allows you to get a feel for how many operations there are, and the order they execute in. For instance, in the following code can you guess how many operations the following code takes?

<syntaxhighlight lang="python">
my_list = list(range(20))
my_list.insert(3, 30)
</syntaxhighlight>

The answer is 50!
The order of operations is:
* <code>list</code> (Variable lookup)
* <code>range</code> (Variable lookup)
* <code>20</code> (Constant evaluation)
* <code>range()</code> (Function call, costing 1)
* <code>list()</code> (Function call, costing 21)
* <code>my_list =</code> (Assignment)
* <code>my_list</code> (Variable lookup)
* <code>insert</code> (Variable lookup(!))
* <code>.</code> (Method operator)
* <code>3</code>
* <code>30</code>
* <code>insert()</code> (Function call, costing 19)

Note that the <code>insert()</code> took one more operation than is documented - this shows the importance of checking operation counts carefully if you are doing things cycle-exactly.

Other interesting things to note: <code>if</code>, <code>else</code> and <code>while</code> do '''not''' take any operations (themselves) to execute. The only operations they take are what is consumed to evaluate their conditions, which might be as little as 1 for a simple variable lookup. This also means if-chaining is more efficient than using the <code>and</code>, <code>or</code> and <code>not</code> operators.

### Operation Costs
Note: Last Updated 2024/8/25, information transcribed from 2024/8/23. Credit: [https://discord.com/users/963434203402358834 kit !!] from discord. [https://discord.com/channels/988081966035402783/1276266294416637962/1276325129193787525 original message]

Note: The following table only includes the cost of the operation itself; not any of its operands. The cost of the operands must be included. For example:
* <code>return 1 + 1</code> costs 4 ops, as <code>return</code> costs 1, its operand <code>1 + 1</code> costs 1 from the <code>+</code> and 1 from each of the <code>1</code>s.

{| class="wikitable" style="background: none; border: none;"
! Operation
! Cost (ops)
|-
| Any simple literal (<code>1</code>, <code>True</code>, <code>North</code>, etc)
| 1
|-
| Any list, tuple, set, or dict literal
| 1
|-
| Variable assignment
| 1
|-
| Any of <code>+</code> <code>-</code> <code>*</code> <code>%</code> <code>**</code> <code>and</code> <code>or</code> <code>not</code>
| 1
|-
| Unary <code>+</code> or <code>-</code>
| 1
|-
| Any of <code>break</code> <code>continue</code> <code>pass</code> <code>def</code> <code>return</code>
| 1
|-
| List or tuple indexing (<code>list_or_tuple[index]</code>)
| 1
|-
| Getter functions (<code>get_pos_x()</code>, <code>can_harvest()</code>, <code>measure()</code>, etc)
| 1
|-
| Failed fallible operating functions (<code>move()</code>, <code>trade()</code>, <code>use_item()</code>, etc)
| 1
|-
| Successful operating function (<code>move()</code>, <code>clear()</code>, <code>swap()</code>, etc)
| 200
|-
| Any of <code>==</code> <code>>=</code> <code><=</code> <code>></code> <code><</code> <code>!=</code>
| See [[#Comparisons|comparisons]] section
|-
| <code>min()</code> or <code>max()</code>
| See [[#Comparisons|comparisons]] section
|-
| Concatenation (<code>+</code>) on lists, strings, or tuples
| 1 + <code>len(arg1)</code> + <code>len(arg2)</code>
|-
| <code>in</code> on list or tuple where item exists
| 1 + <code>indexof(item)</code>
|-
| <code>in</code> on list or tuple where item doesn't exist
| 1 + <code>len(list_or_tuple)</code>
|-
| <code>in</code> on sets or dictionaries
| 2
|-
| List slicing (<code>lst[from:to:step]</code> or <code>lst[from:to]</code>)
| 1 + <code>len(result_of_slice)</code>
|-
| <code>.insert()</code>
| 1 + <code>len(tuple_or_list)</code> - <code>insertion_index</code>
|-
| <code>.remove()</code>
| 1 + <code>indexof(item)</code>
|-
| <code>set()</code> or <code>list()</code> with one argument
| 1 + <code>len(arg)</code>
|-
|}

== Comparisons ==

Comparison costs are surprisingly complicated in this game. The following are the rules to comparison, where <code>a</code> and <code>b</code> are the arguments:
# <code>a</code> and <code>b</code> are different types: 1 op
# both are numbers, enums (<code>North</code>, <code>Items</code>, etc): 1 op
# both are sets: 1 op
# both are lists or tuples, and they have different lengths: 1 op
# both are lists or tuples, but same length: 1 + sum of ops of comparing all elements up to and including the first different element.
# both are dictionaries: I don't actually know, if you know, edit this wiki!

Examples:
* Comparing <code>(1, (2, 3), 4)</code> and <code>(1, (2, 3), 5)</code>
** They are both tuples, of length 3. Thus, use rule 5. Their first different element the last element, so it's the sum of all element costs. The first elements are both numbers, so 1 op; the second is a tuple, with 2 elements, all the same, so 1 + 2 op; the third is another number, so 1 op. This totals to 5 ops, add 1 for tuple itself, to get 6 ops.

###  Unlocks Data
Here is a function that returns all relevant costs for unlocks during a timed run

<syntaxhighlight lang="python">
def GetUnlocksData():
	grass = [
		{Items.Hay: 100},
		{Items.Hay: 300},
		{Items.Hay: 450},
		{Items.Hay: 675},
		{Items.Hay: 1010},
		{Items.Hay: 1520},
		{Items.Hay: 2280},
		{Items.Hay: 3420},
		{Items.Hay: 5130},
		{Items.Hay: 7690},
		{Items.Hay: 11500},
		{Items.Hay: 17300}
	]

	speed = [
		{Items.Hay: 20},
		{Items.Wood: 10},
		{Items.Wood: 50, Items.Carrot: 100},
		{Items.Wood: 100, Items.Carrot: 200},
		{Items.Carrot: 350},
		{Items.Carrot: 500},
		{Items.Carrot: 800},
		{Items.Carrot: 1100},
		{Items.Carrot: 1400},
		{Items.Carrot: 1700},
		{Items.Carrot: 2100},
		{Items.Carrot: 2500},
		{Items.Power: 2000},
		{Items.Power: 2600},
		{Items.Power: 3380},
		{Items.Power: 4390},
		{Items.Power: 5710},
		{Items.Power: 7430},
		{Items.Power: 9650},
		{Items.Power: 12500}
	]

	trees = [
		{Items.Wood: 50, Items.Carrot: 200},
		{Items.Hay: 300},
		{Items.Hay: 480},
		{Items.Hay: 768},
		{Items.Hay: 1230},
		{Items.Hay: 1970},
		{Items.Hay: 3150},
		{Items.Hay: 5030},
		{Items.Hay: 8050},
		{Items.Hay: 12900},
		{Items.Hay: 20600},
		{Items.Hay: 33000}
	]

	carrots = [
		{Items.Wood: 100},
		{Items.Wood: 300},
		{Items.Wood: 480},
		{Items.Wood: 768},
		{Items.Wood: 1230},
		{Items.Wood: 1970},
		{Items.Wood: 3150},
		{Items.Wood: 5030},
		{Items.Wood: 8050},
		{Items.Wood: 12900},
		{Items.Wood: 20600},
		{Items.Wood: 33000}
	]

	expand = [
		{Items.Hay: 30},
		{Items.Wood: 20},
		{Items.Wood: 50, Items.Carrot: 50},
		{Items.Wood: 100, Items.Pumpkin: 200},
		{Items.Pumpkin: 500},
		{Items.Pumpkin: 1750},
		{Items.Pumpkin: 6120},
		{Items.Pumpkin: 21400},
		{Items.Pumpkin: 75000}
	]

	pumpkins = [
		{Items.Wood: 500, Items.Carrot: 1000},
		{Items.Carrot: 1200},
		{Items.Carrot: 1920},
		{Items.Carrot: 3070},
		{Items.Carrot: 4920},
		{Items.Carrot: 7860},
		{Items.Carrot: 12600},
		{Items.Carrot: 20100},
		{Items.Carrot: 32200},
		{Items.Carrot: 51500}
	]

	mazes = [
		{Items.Carrot: 2000, Items.Pumpkin: 3000},
		{Items.Pumpkin: 4000},
		{Items.Pumpkin: 8000},
		{Items.Pumpkin: 16000},
		{Items.Pumpkin: 32000}
	]

	sunflowers = [
		{Items.Carrot: 500},
		{Items.Gold: 1000},
		{Items.Gold: 2000},
		{Items.Gold: 4000},
		{Items.Gold: 8000},
		{Items.Gold: 16000}
	]

	cactus = [
		{Items.Gold: 5000},
		{Items.Gold: 10000},
		{Items.Gold: 20000},
		{Items.Gold: 40000}
	]

	dinosaurs = [
		{Items.Cactus: 5000},
		{Items.Cactus: 1000},
		{Items.Cactus: 2000}
	]

	data = {
		Unlocks.Grass: grass,
		Unlocks.Speed: speed,
		Unlocks.Trees: trees,
		Unlocks.Carrots: carrots,
		Unlocks.Expand: expand,
		Unlocks.Pumpkins: pumpkins,
		Unlocks.Mazes: mazes,
		Unlocks.Sunflowers: sunflowers,
		Unlocks.Cactus: cactus,
		Unlocks.Dinosaurs: dinosaurs,

		Unlocks.Plant: {Items.Hay: 50},
		Unlocks.Fertilizer: {Items.Pumpkin: 1000},

		Unlocks.Polyculture: {
			Items.Hay: 3000,
			Items.Wood: 3000,
			Items.Carrot: 3000
		},

		Unlocks.Leaderboard: {Items.Bone: 2000}
	}

	return data
</syntaxhighlight>

### Item Costs
This function returns all the item costs for the game:

<syntaxhighlight lang="python">
def GetItemCosts():
	_item_costs = {
		Items.Empty_Tank: [{Items.Wood: 5}],
		Items.Fertilizer: [{Items.Pumpkin: 10}],

		Items.Carrot_Seed: [{Items.Hay: 1, Items.Wood: 1},
					  		{Items.Hay: 2, Items.Wood: 2},
					  		{Items.Hay: 3, Items.Wood: 3},
					  		{Items.Hay: 4, Items.Wood: 4},
					  		{Items.Hay: 5, Items.Wood: 5},
					  		{Items.Hay: 6, Items.Wood: 6},
					  		{Items.Hay: 7, Items.Wood: 7},
					  		{Items.Hay: 8, Items.Wood: 8},
					  		{Items.Hay: 9, Items.Wood: 9},
					  		{Items.Hay: 10, Items.Wood: 10},
					  		{Items.Hay: 11, Items.Wood: 11},
					  		{Items.Hay: 12, Items.Wood: 12}],
		Items.Sunflower_Seed: [{Items.Carrot: 1},
						 	   {Items.Carrot: 2},
						 	   {Items.Carrot: 3},
						 	   {Items.Carrot: 4},
						 	   {Items.Carrot: 5},
						 	   {Items.Carrot: 6}],
		Items.Pumpkin_Seed: [{Items.Carrot: 1},
					   		 {Items.Carrot: 2},
					   		 {Items.Carrot: 3},
					   		 {Items.Carrot: 4},
					   		 {Items.Carrot: 5},
					   		 {Items.Carrot: 6},
					   		 {Items.Carrot: 7},
					   		 {Items.Carrot: 8},
					   		 {Items.Carrot: 9},
					   		 {Items.Carrot: 10}],
		Items.Cactus_Seed: [{Items.Gold: 10},
					  		{Items.Gold: 20},
							{Items.Gold: 30},
							{Items.Gold: 40}],
		Items.Egg: [{Items.Cactus: 20},
			  		{Items.Cactus: 40},
					{Items.Cactus: 60}]
	}
	return _item_costs
</syntaxhighlight>


## Coding Style & Naming Conventions
- 使用四个空格缩进，遵循接近 PEP 8 的行宽（最长 100 列）与空行规则。
- 函数名采用 `snake_case`，常量与枚举维持游戏 API 既有命名，例如 `Entities.Sunflower`。
- 将策略性阈值与魔术数字提取为顶层常量，便于调参与复用。
- 对复杂路径规划或资源分配逻辑添加简短行内注释说明原因，而非步骤。

## Commit & Pull Request Guidelines
- 现有历史使用简短小写动词（如 `first init`）；保持 50 字符以内的祈使句摘要，例如 `optimize harvest window`。
- 每个提交聚焦单一改动：算法调优、参数更新或文档。
- PR 描述包含动机、主要变更点、验证方式；若涉及地图或 UI，附加截图或重播链接。
- 关联相关 issue 或讨论串，便于追踪。
