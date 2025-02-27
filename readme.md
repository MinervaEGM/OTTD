
# Experimental Replication and Further Analysis of OTTD Based on 'Target Networks and Over-parameterization Stabilize Off-policy Bootstrapping' 

This repository contains all the scripts used to replicate the experiments described on [Target Networks and Over-parameterization Stabilize Off-policy Bootstrapping with Function Approximation](https://arxiv.org/pdf/2405.21043) by Che et. al. and an additional experiment to assess the impact of varying step size on TD target.

## Baird's counterexample algorithm comparison
The script `baird.py` compares the following algorithms on the Baird's counterexample:
- Temporal Difference (TD)
- Temporal Difference with target networks (TD-target) 
- Residual Minimization (RM) 
- Baird Residual Minimization (Baird RM)
- Gradient Temporal Difference 2 (GTD2) 
- Linear TD with gradient Correction (TDC) 


## Four room environment
The script `four_room.py` defines the four room gridworld where an agent starts at a random location and must reach a goal state while navigating walls and hallways through four rooms.
The script `learn_four_room.py` trains an agent in the four room enviornment that was defined previously. 

## Baird's counterexample with varying target update step sizes
Finally, the script `TDtarget_Checkpoint.py` evaluates TD target on Baird's counterexample using different target update step sizes.
