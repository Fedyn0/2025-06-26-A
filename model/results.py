from dataclasses import dataclass

@dataclass
class Results:
    idPilota: int
    posizione: int

    def __hash__(self):
        return hash(self.idPilota)

    def __eq__(self, other):
        return self.idPilota == other.idPilota