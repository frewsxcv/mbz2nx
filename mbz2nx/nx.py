import networkx

class Graph():
    def __init__(self):
        self.graph = networkx.MultiDiGraph()

    def add_labels(self, labels):
        for label in labels:
            attrs = {"name": label.name, "mbid": label.mbid}
            if label.country:
                attrs["country"] = label.country
            self.graph.add_node(label.id, attrs)

    def add_relations(self, relations):
        for relation in relations:
            self.graph.add_edge(relation.child, relation.parent,
                    attr_dict={"rel": relation.type})
