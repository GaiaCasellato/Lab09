from dataclasses import dataclass

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Rotta:
    origin_airport_id :int
    destination_airport_id : int
    avg_distance : int


    def __hash__(self):
        return self.origin_airport_id

    def __str__(self):
        return f"La tua rotta inizia a  {self.origin_airport_id} e finisce a {self.destination_airport_id}: "
