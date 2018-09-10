import argparse
from PacmanGym.gym_pacman.envs.game import Agent
from PacmanGym.gym_pacman.envs.pacman import Directions
import time


class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace. Built from both main command-line parser
                  and command-line parser built by `arg_parser`
        """
        pass

    def getAction(self, state):
        """
        Given a pacman game state, returns a legal move. Called on-game.
        !!! Constrained computational time (see `args.timeout` parameter)

        Parameters:
        -----------
        - `state`: the current game state. See class pacman.GameState.

        Return:
        -------
        - A legal move as defined in game.Directions.
        """
        while True : time.sleep(1)
        return Directions.STOP

    def registerInitialState(self, state):
        """
        Procedure called before the game
        with the initial game state `state`.
        !!! Not called in the online setting (See instructions).

        Parameters:
        -----------
        - `state`: the current game state. See class pacman.GameState.

        """
        return

    @staticmethod
    def arg_parser(parser):
        """
        Return a command line parser based on the arguments needed both
        from this agent and the command line. See python module `argparse`.
        """
        return parser