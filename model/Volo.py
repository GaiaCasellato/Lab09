from dataclasses import dataclass

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Volo:
    id: int
    airline_id : int
    flight_number : int
    tail_numer : str
    origin_airport_id :int
    destination_airport_id : int
    scheduled_departure_date : datetime
    departure_delay : float
    elapsed_time : float
    distance : int
    arrival_date : datetime
    arrival_delay : float

    def __hash__(self):
        return self.id

    def __str__(self):
        return f"Il numero del volo è : {self.id}"
