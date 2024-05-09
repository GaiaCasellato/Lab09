from dataclasses import dataclass

from dataclasses import dataclass

@dataclass
class Areoporto:
    id: int
    iata_code: str
    airport: str
    city: str
    state : str
    country : str
    latitude : float
    longitude : float
    timezone_offset : float


    def __hash__(self):
        return self.id

    def __str__(self):
        return f"Nome areoporto: {self.airport}"
