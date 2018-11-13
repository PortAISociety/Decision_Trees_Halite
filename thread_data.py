import threading
import model
import numpy as np

class DataThread(threading.Thread):
    def __init__(self,game_map,moves,ships,other_ships,dropoffs,other_dropoffs,turn_number,ship):
        threading.Thread.__init__(self)
        self.game_map = game_map
        self.moves = moves
        self.ships = ships
        self.other_ships = other_ships
        self.dropoffs = dropoffs
        self.other_dropoffs = other_dropoffs
        self.turn_number = turn_number
        self.ship = ship

        self.calculated_data = []
        self.calculated_labels = []

        self.HaliteModel = model.HaliteModel()

    def run(self):
        #print("Generating Training Data")
        #print("Starting DATATHREAD " + self.name)
        move = "o" if self.ship.id not in self.moves else self.moves[self.ship.id]
        # Throw away movements that take us closer to base. We will let logic take care of returning to base
        if move is not "o" and (
                self.game_map.calculate_distance(self.ship.position.directional_offset(self.HaliteModel.MOVE_TO_DIRECTION[move]),
                                            self.dropoffs[0].position) <
                self.game_map.calculate_distance(self.ship.position, self.dropoffs[0].position)
        ):
        #    print("Exiting " + self.name)
            return

        move_id = self.HaliteModel.MOVE_TO_OUTPUT[move]
        for rot in range(4):  # do all 4 rotations for each game state
            self.calculated_data.append(self.HaliteModel.input_for_ship(self.game_map,
                                            self.ship,
                                            [s2.position for s2 in self.ships.values() if s2.id != self.ship.id],
                                            [s2.position for s2 in self.other_ships.values()],
                                            [d.position for d in self.dropoffs],
                                            [d.position for d in self.other_dropoffs],
                                            self.turn_number,
                                            rotation=rot))
            self.calculated_labels.append(np.array(move_id))
            move_id = 0 if move_id == 0 else (move_id % 4) + 1
        #print("Exiting " + self.name)

    def output(self):
        return self.calculated_data, self.calculated_labels
