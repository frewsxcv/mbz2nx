from mbz2nx.mbz import MusicBrainz
from mbz2nx.nx import Graph


def _default_pgconfig(pgconfig):
    pgconfig["database"] = pgconfig.get("database", "musicbrainz_db")
    pgconfig["user"] = pgconfig.get("user", "musicbrainz")
    pgconfig["password"] = pgconfig.get("password", "musicbrainz")
    pgconfig["host"] = pgconfig.get("host", "localhost")
    pgconfig["port"] = pgconfig.get("port", 5432)

def label_graph(pgconfig={}):
    _default_pgconfig(pgconfig)
    mbz = MusicBrainz()
    graph = Graph()
    mbz.connect(pgconfig)
    graph.add_labels(mbz.labels)
    graph.add_relations(mbz.relations)
    mbz.disconnect()
    return graph.graph


# {"database": "musicbrainz_db", "user": "musicbrainz", "password": "musicbrainz"}
