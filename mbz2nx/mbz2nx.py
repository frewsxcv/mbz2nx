from mbz2nx.mbz import MusicBrainz
from mbz2nx.nx import Graph


def _default_pgconfig(pgconfig):
    newconfig = {
        "database": "musicbrainz_db",
        "user": "musicbrainz",
        "password": "musicbrainz",
        "host": "localhost",
        "port": 5432,
    }
    newconfig.update(pgconfig)
    return newconfig

def label_graph(pgconfig={}):
    pg_config = _default_pgconfig(pgconfig)
    mbz = MusicBrainz()
    graph = Graph()
    mbz.connect(pg_config)
    graph.add_labels(mbz.labels)
    graph.add_relations(mbz.relations)
    mbz.disconnect()
    return graph.graph


# {"database": "musicbrainz_db", "user": "musicbrainz", "password": "musicbrainz"}
