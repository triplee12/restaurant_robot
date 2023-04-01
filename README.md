# Humanoid Robots

Let’s be frank for a moment—you really don’t want to use Curio. All things equal, you
should probably be programming with threads. Yes, threads. THOSE threads. Seri‐
ously. I’m not kidding.
—Dave Beazley, “Developing with Curio”

## Case Study: The resturant with the humanoid robots

The Restaurant of ThreadBots

The year is 2051, and you find yourself in the restaurant business. Automation,
largely by robot workers, powers most of the economy, but it turns out that humans
still enjoy going out to eat once in a while. In your restaurant, all the employees are
robots—humanoid, of course, but unmistakably robots. The most successful manu‐
facturer of robots is Threading Inc., and robot workers from this company have come
to be called “ThreadBots.”

Except for this small robotic detail, your restaurant looks and operates like one of
those old-time establishments from, say, 2020. Your guests will be looking for that
vintage experience. They want fresh food prepared from scratch. They want to sit at
tables. They want to wait for their meals—but only a little. They want to pay at the
end, and they sometimes even want to leave a tip, for old times’ sake.

Being new to the robotic restaurant business, you do what every other restaurateur
does and hire a small fleet of robots: one to greet diners at the front desk (GreetBot),
one to wait tables and take orders (WaitBot), one to do the cooking (ChefBot), and
one to manage the bar (WineBot).

Hungry diners arrive at the front desk and are welcomed by GreetBot, your front-of-
house ThreadBot. They are then directed to a table, and once they are seated, WaitBot
takes their order. Then WaitBot brings that order to the kitchen on a slip of paper
(because you want to preserve that old-time experience, remember?). ChefBot looks
at the order on the slip and begins preparing the food. WaitBot will periodically check
whether the food is ready, and when it is, will immediately take the dishes to the cus‐
tomers’ table. When the guests are ready to leave, they return to GreetBot, who calcu‐
lates the bill, takes their payment, and graciously wishes them a pleasant evening.

## Codes Explanation For ThreadBot Class

- A ThreadBot is a subclass of a thread.

- The target function of the thread is the manage_table().

- This bot is going to be waiting tables and will need to be responsible for some cutlery. Each bot keeps track of the cutlery that it took from the kitchen here.

- The bot will also be assigned tasks. They will be added to this task queue, and the bot will perform them during its main processing loop, next.

- The primary routine of this bot is this infinite loop. If you need to shut down a bot, you have to give them the shutdown task.

- There are only three tasks defined for this bot. This one, (i) prepare table, is what the bot must do to get a new table ready for service. For our test, the only
requirement is to get sets of cutlery from the kitchen and place them on the table.
(ii) clear table is used when a table is to be cleared: the bot must return the used cutlery back to the kitchen.(iii) shutdown just shuts down the bot.

## Codes Explanation For Cutlery Class

- attrs, which is an open source Python library that has nothing to do with threads or asyncio, is a really wonderful library for making class creation easy.
Here, the @attrs decorator will ensure that this Cutlery class will get all the usual boilerplate code (like __init__()) automatically set up.

- The attrib() function provides an easy way to create attributes, including defaults, which you might normally have handled as keyword arguments in the __init__() method.

- This method is used to transfer knives and forks from one Cutlery object to another. Typically, it will be used by bots to obtain cutlery from the kitchen for
new tables, and to return the cutlery back to the kitchen after a table is cleared.

- This is a very simple utility function for altering the inventory data in the object instance.

- We’ve defined kitchen as the identifier for the kitchen inventory of cutlery. Typically, each of the bots will obtain cutlery from this location. It is also required that they return cutlery to this store when a table is cleared.

- This script is executed when testing. For our test, we’ll be using 10 ThreadBots.

- We get the number of tables as a command-line parameter, and then give each bot that number of tasks for preparing and clearing tables in the restaurant.

- The shutdown task will make the bots stop (so that bot.join() a bit further down will return). The rest of the script prints diagnostic messages and starts up the bots.

Your strategy for testing the code basically involves running a group of ThreadBots over a sequence of table service. Each ThreadBot must do the following:

- Prepare a “table for four,” which means obtaining four sets of knives and forks from the kitchen.

- Clear a table, which means returning the set of four knives and forks from a table back to the kitchen.
