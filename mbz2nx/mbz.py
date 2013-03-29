import psycopg2


class Label():
    def __init__(self, id, mbid, name, country):
        self.id = id
        self.mbid = mbid
        self.name = name
        self.country = country

    def __repr__(self):
        return "<Label '{0}: {1}'>".format(self.name, self.mbid)


class LabelRelation():
    _rel_rules = {
        "label ownership": (1, "owned_by"),
        "label reissue": (1, "catalog_reissued_by"),
        "label rename": (0, "renamed_to"),
        "label distribution": (1, "catalog_distributed_by"),
        "business association": (0, "business_association_with")
    }

    def __init__(self, type, id1, id2):
        rel_rule = self._rel_rules[type]
        self.type = rel_rule[1]
        self.child, self.parent = (id1, id2) if rel_rule[0] == 0 else (id2, id1)

    def __repr__(self):
        return "<LabelRelation '{0} {1} {2}'>".format(self.child, self.type, self.parent)


class MusicBrainz():
    def __init__(self):
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)

    def connect(self, pgconfig):
        self._conn = psycopg2.connect(**pgconfig)

    def disconnect(self):
        self._conn.close()

    def _query(self, sql):
        curr = self._conn.cursor()
        curr.execute(sql)
        results = curr.fetchall()
        curr.close()
        return results

    @property
    def labels(self):
        sql = """
            SELECT label.id, label.gid, label_name.name, country.iso_code
                FROM label LEFT OUTER JOIN country ON
                        label.country = country.id,
                     label_name
                WHERE label.name = label_name.id;"""
        return [Label(*row) for row in self._query(sql)]

    @property
    def relations(self):
        sql = """
            SELECT link_type.name, l_l_l.entity0, l_l_l.entity1
            FROM l_label_label AS l_l_l, link, link_type
            WHERE l_l_l.link = link.id
                AND link.link_type = link_type.id"""
        return [LabelRelation(*row) for row in self._query(sql)]
