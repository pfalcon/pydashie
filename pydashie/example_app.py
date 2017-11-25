from example_samplers import *

def run(xyzzy):
    samplers = [
        SynergySampler(xyzzy, 3),
        BuzzwordsSampler(xyzzy, 2), # 10
        ConvergenceSampler(xyzzy, 1),
    ]
