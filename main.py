import numpy as np
import time


def random():
    return np.random.random()


width = 1.0
needle = 0.5

num_hits = 0
num_misses = 0

mass = []

for j in range(10):
    for i in range(100000):
        x = (3.0 - 0.0) * random() + 0.0
        y = (4.0 - 0.0) * random() + 0.0

        angle = np.radians(360.0 * random())
        xx = x + needle * np.cos(angle)
        yy = y + needle * np.sin(angle)

        if xx < x:
            (x, xx) = (xx, x)
            (y, yy) = (yy, y)
        if (x < 0.0 < xx) or (x < 1.0 < xx) or (x < 2.0 < xx) or (x < 3.0 < xx):
            num_hits += 1
        else:
            num_misses += 1

    pi_est = (2.0 * needle) / ((num_hits * 1.0) / (num_hits + num_misses) * width)

    mass.append(float("%0.4f" % pi_est))
    print("%0.4f" % pi_est, end=" ")

    num_hits = 0
    num_misses = 0

    time.sleep(random())
print()

a = 0
for k in range(10):
    a += mass[k]
a /= 10

b = np.std(mass)
print(f"Stdev: {b} ~~ {'%.4f' % b}\n"
      f"Average: {a} ~~ {'%.4f' % a}\n"
      f"Min/Max value of pi: {a - b} / {a + b}")
