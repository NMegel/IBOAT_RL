import math

import matplotlib.pyplot as plt
import mdp_realistic
import numpy as np

# %%
TORAD = math.pi / 180
SIMULATION_TIME = 10

'''
MDP PARAMETERS
'''
history_duration = 3
mdp_duration = SIMULATION_TIME
mdp_step = 1
time_step = 0.1

hdg0 = 2
speed0 = 1

mdp = mdp_realistic.mdp_realistic(mdp_duration, history_duration, mdp_step, time_step)

'''
WIND CONDITIONS
'''
truewindheading = 60
truewindheading_std = 3

'''
MDP INIT
'''
sailpos = 40
truewaterheading = 0
truewaterspeed = 0
truewindspeed = 10
state = mdp.initializeMDP(hdg0, sailpos, speed0, truewaterheading, truewaterspeed, truewindspeed, truewindheading)

'''
Generation of a simulation
'''
i = np.ones(0)
sog = np.ones(0)

for time in range(SIMULATION_TIME):
    print('t = {0} s'.format(time))
    action = 0

    if time < SIMULATION_TIME / 4:
        action = 0
    elif time < SIMULATION_TIME / 2:
        action = 1
    elif time < 3 * SIMULATION_TIME / 4:
        action = 0
    else:
        action = 1

    next_state, reward = mdp.transition(action)
    state = next_state
    i = np.concatenate([i, mdp.extractSimulationData()[0, :]])
    sog = np.concatenate([sog, mdp.extractSimulationData()[1, :]])

time_vec = np.linspace(0, SIMULATION_TIME, int((SIMULATION_TIME) / time_step))

f, axarr = plt.subplots(2, sharex=True)
i_plot = axarr[0].plot(time_vec, i)
sog_plot = axarr[1].plot(time_vec, sog)
plt.show()
