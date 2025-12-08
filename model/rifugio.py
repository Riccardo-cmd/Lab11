from dataclasses import dataclass


@dataclass
class Rifugio:
    id: int
    nome: str
    localita: str
    altitudine: int
    capienza: int
    aperto: int

    # Metodo necessario per usare l'oggetto come nodo in NetworkX
    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if not isinstance(other, Rifugio):
            return False
        return self.id == other.id

    def __str__(self):
        return f"{self.nome}"