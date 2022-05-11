# Monte-Carlo-Simulation

Problem Description: 
A mosquito is born in a puddle at [0,0]. She will live for ten days. At the beginning of each day, she will try to smell a host. If see can smell a host, she will find them, game over. If see cannot, she will “turn off” her sense of smell for the rest of the day and fly 250 m in a random direction. Next morning, GOTO ‘1’.
Obviously, after ten days, if she does not find a host, she dies without taking a blood meal. A mosquito can smell a human at 50 meters.

Day 1: Mosquito is born, she cannot smell a host; she flies 250 m in a random direction.
Day 2: Mosquito cannot smell a host; she flies 250 m in a random direction.
Day 3: Mosquito cannot smell a host; she flies 250 m in a random direction. When she wakes up on Day four, she finds the host.



Monte-Carlo-Problem_1:

What is the probability that the mosquito will find the host before she dies?
What is the probability that the mosquito will die outside the red region. Note that I am not asking what is the probability she will visit outside the red region. I.e. what is the probability the mosquito will die more that a kilometer from its birthplace?

Monte-Carlo-Problem_2:

Suppose the mosquito lives for 100 days. Create a plot showing the probably that the insect finds the host by day K.


Monte-Carlo-Problem_3:

In our assumption, we assume that the mosquito turn off its sense of smell as it makes a random flight. However, suppose that was not the case. That would mean that even if it flies over the yellow circle, it will find the host. Compute this probability.

Monte-Carlo-Problem_4:

Suppose that the center of the yellow circle can move along the Y axis, form as little as zero to at most 2,525 m (at which point, the mosquito cannot reach it), Create a plot showing the probably that the (ten day) insect finds the host, as a function of K.
