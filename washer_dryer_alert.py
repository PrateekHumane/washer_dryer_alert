import Adafruit_ADS1x15
import time
from enum import Enum
import numpy as np

adc = Adafruit_ADS1x15.ADS1115()

THRESHOLD = 1000

class washer_dryer_state(Enum):
    ON = 1
    OFF = 0
state = washer_dryer_state.OFF 

samples = np.array([])
SAMPLE_SIZE = 100

def getNoise():
    start = time.time()
    smax = 0
    smin = 1000000
    while time.time()-start<.05:
        sample = adc.read_adc(0,gain=1)
        if sample > smax:
            smax = sample
        if sample < smin:
            smin = sample
    amplitude = smax-smin
    return amplitude

while True:
    samples = np.append(samples,getNoise())
    if len(samples) > SAMPLE_SIZE:
        samples = np.delete(samples,0)
    moving_average = np.mean(samples)
    print(moving_average)
    
    if moving_average > THRESHOLD and state is washer_dryer_state.OFF: # if the washer is on change the state
        state = washer_dryer_state.ON
        #alert user the washer is on
        print('Washer On!')
    elif moving_average < THRESHOLD and state is washer_dryer_state.ON: # if the state is on but it turned off then switch the state and alert the user
        state = washer_dryer_state.OFF
        print('Washer Off!')

