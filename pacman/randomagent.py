import numpy as np

from pacman_module.game import Agent
from pacman_module.pacman import Directions


class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.prob_dir = {}
        WestProb, SouthProb, EastProb, NorthProb = [.25, .25, .25, .25]
        self.prob_dir["West"] = WestProb
        self.prob_dir["South"] = SouthProb
        self.prob_dir["North"] = EastProb
        self.prob_dir["East"] = NorthProb
        self._rng = np.random.RandomState(args.seed)

    def get_action(self, state):
        """
        Given a pacman game state, returns a legal move.

        Arguments:
        ----------
        - `state`: the current game state. See FAQ and class
                   `pacman.GameState`.

        Return:
        -------
        - A legal move as defined in `game.Directions`.
        """
        legals = state.getLegalPacmanActions()

        if Directions.STOP in legals:
            legals.remove(Directions.STOP)

        probs = [self.prob_dir[x] for x in legals]
        probs = [x / sum(probs) for x in probs]
        a = self._rng.choice(legals, 1, replace=False, p=probs)

        return a[0]
