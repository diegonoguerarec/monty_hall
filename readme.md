[![en](https://img.shields.io/badge/lang-en-blue.svg)](readme.md)
[![es](https://img.shields.io/badge/lang-es-red.svg)](readme.es.md)

# Monty Hall

Imagine you are on a TV show playing a game where you can win a brand-new car. There are three doors, and only behind one of them is the prize. The host tells you to choose one of the doors. You make your choice. Next, the host (who knows where the prize is) opens one of the empty doors and asks you a question:

**Contestant, do you want to switch doors or stick with your choice?**

At this point, there are still two closed doors. Behind one of them is the brand-new car. The host opened one of the empty doors to show you there’s nothing behind it. You have two options:

1) Stick with your choice  
2) Switch to the other door  

Remember that the host knows where the prize is, so he could be trying to trick you into choosing the wrong door.

**What do you do?**

You might think about not switching doors because you believe the host wants you to lose. You might also think it doesn’t matter whether you switch or not, since only one door has the car, and the probability of winning is always 1/3 or 33.33%.

---

## Switching Choice

In reality, the best thing you can do is switch doors.

When you first pick a door, the probability of winning is 1/3 or 33.33%, and the probability of losing is 2/3 or 66.66%, because only one of the three doors has the prize. If you decide not to switch, you keep that 1/3 chance of winning.

When the host opens a door, the probability of your chosen door being correct is still 1/3. What happens is that the other unopened door now concentrates the remaining 2/3 probability.

By switching, you are not betting that you chose correctly the first time (which was unlikely, 1/3), but rather that you chose incorrectly (which was more likely, 2/3). Since the host always eliminates one wrong option, that probability transfers to the other closed door.

---

## Conclusion

By switching doors, your chances of winning increase to 2/3 or 66.66%, instead of the 1/3 or 33.33% you had at the beginning.

---

## Implementation

In the file `monty_hall.py` you’ll find the implementation of this game.

To run the program on Windows:
``` python monty_hall.py <number_of_iterations> ```

On Linux:

``` python3 monty_hall.py <number_of_iterations> ```

Example:

``` python monty_hall.py 1000 ```

The program simulates the Monty Hall game and prints how many times it results in a win, first when you don’t switch doors, and then when you do.

When you don’t switch doors, the game ends in a win about 33.33% of the time. When you do switch doors, the game ends in a win about 66.66% of the time.
