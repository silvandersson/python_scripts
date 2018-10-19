"""
Module Docstring
"""
# =========
# Balls
# Urn contains N balls numbered 1..N
# Draw n < N balls without replacement.
# What is the expected value of the maximum number drawn?
# ==============================================================================

import random
N = 10
n = 2
balls = [i for i in range(1, N + 1)]
maximum_nbr = 0
for k in range(1, n + 1):
    ball = balls[random.randint(1, N - k)]
    balls.remove(ball)
    if ball > maximum_nbr:
        maximum_nbr = ball
    print(balls)
print(maximum_nbr)
