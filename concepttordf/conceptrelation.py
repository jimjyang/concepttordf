from abc import ABC
from datetime import date
from rdflib import Graph, Literal, BNode, Namespace

SKOSNO = Namespace('http://difi.no/skosno#')
DCT = Namespace('http://purl.org/dc/terms/')
XSD = Namespace('http://www.w3.org/2001/XMLSchema#')


class ConceptRelation(ABC):

    def __init__(self, cr: dict = None):
        self._g = Graph()
        self._relation = BNode()
        self._g.bind('skosno', SKOSNO)
        self._g.bind('dct', DCT)
        self._g.bind('xsd', XSD)

        if cr is not None:
            if 'modified' in cr:
                self.modified = cr['modified']

    @property
    def modified(self) -> date:
        return self._modified

    @modified.setter
    def modified(self, modified: date):
        self._modified = modified

# ---
    def _add_relation_to_graph(self):

        # modified
        if hasattr(self, 'modified'):
            self._g.add((self._relation, DCT.modified,
                         Literal(self.modified, datatype=XSD.date)))
