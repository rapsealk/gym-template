#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from gym.envs.registration import register

register(
    id='example-v0',
    entry_point='gym_example.envs:ExampleEnv'
)
