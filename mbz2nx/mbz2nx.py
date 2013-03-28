from mbz import MusicBrainz
from nx import Graph


def label_graph(pg_config):
    mbz = MusicBrainz()
    graph = Graph()
    mbz.connect(pg_config)
    graph.add_labels(mbz.labels)
    graph.add_relations(mbz.relations)
    mbz.disconnect()
    return graph.graph


# {"database": "musicbrainz_db", "user": "musicbrainz", "password": "musicbrainz"}
