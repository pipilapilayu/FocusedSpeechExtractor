import torch
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)


macs = [
    3.6,
    1.8,
    2.7,
    3.0,
    3.7,
    19.7,
    60.7,
    60.7,
    42.8,
    29.8,
    228.2,
    3.7,
    3.7,
    3.7,
    3.7,
    8.5,
    8.6,
    8.5,
    8.6,
    21.9,
    22.0,
    21.9,
    22.0,
    63.6,
    63.9,
    63.6,
    63.9,
    10,
]
params = [
    5.1,
    57.5,
    2.7,
    3.6,
    3.6,
    5.9,
    25.6,
    25.6,
    42.1,
    6.8,
    14.3,
    1.8,
    1.8,
    1.8,
    1.8,
    6.7,
    6.8,
    6.7,
    6.8,
    25.9,
    26.2,
    25.9,
    26.2,
    102.2,
    102.7,
    102.2,
    102.7,
    2.69,
]
w2mix = [
    15.6,
    10.8,
    17,
    15.6,
    17.2,
    18.3,
    20.4,
    22.3,
    22.8,
    22.0,
    23.4,
    15.8,
    15.9,
    17.4,
    17.5,
    17.7,
    17.8,
    18.1,
    18.8,
    19.5,
    19.7,
    20.3,
    20.2,
    20.4,
    20.3,
    21.1,
    21.2,
    20.2,
]

plt.scatter(
    params,
    w2mix,
    s=list(map(lambda r: 30 * r, macs)),
    c=np.random.rand(len(params)),
    alpha=0.5,
)
plt.ylim(bottom=0)
plt.xscale("log")
plt.xlabel("params (M)")
plt.ylabel("w2mix ΔSI-SDR")
plt.show()
