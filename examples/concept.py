from concepttordf.concept import Concept

concept = Concept()
concept.identifier = "http://example.com/concepts/1"
concept.term = {}
concept.term['en'] = "concept"
concept.term['nb'] = "begrep"
concept.definition = {}
concept.definition['en'] = (
    "an abstract or generic idea generalized from particular instances"
    )
concept.definition['nb'] = (
    "mental forestilling om et konkret eller abstrakt"
    "fenomen i den virkelige verden"
    )
concept.publisher = "https://example.com/publishers/1"

print(concept.to_rdf().decode())

# prints:
# @prefix dct: <http://purl.org/dc/terms/> .
# @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
# @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
# @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
# @prefix skosno: <http://difi.no/skosno#> .
# @prefix skosxl: <http://www.w3.org/2008/05/skos-xl#> .
# @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
# @prefix xml: <http://www.w3.org/XML/1998/namespace> .
# @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
#
# <http://example.com/concepts/1> a skos:Concept ;
#     skosno:betydningsbeskrivelse [ a skosno:Definisjon ;
#             rdfs:label "an abstract or generic idea generalized from particular instances"@en,
#                 "mental forestilling om et konkret eller abstraktfenomen i den virkelige verden"@nb ] ;
#     dct:publisher <https://example.com/publishers/1> ;
#     skosxl:prefLabel [ a skosxl:Label ;
#             skosxl:literalForm "concept"@en,
#                 "begrep"@nb ] .
#