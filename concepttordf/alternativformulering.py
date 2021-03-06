from .betydningsbeskrivelse import Betydningsbeskrivelse
from rdflib import Namespace

SKOSNO = Namespace('http://difi.no/skosno#')


class AlternativFormulering(Betydningsbeskrivelse):

    def __init__(self, alternativformulering: dict = None):
        self.type = SKOSNO.AlternativFormulering
        super().__init__(alternativformulering)
