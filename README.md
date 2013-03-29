# mbz2nx
Python library that generates NetworkX graphs from the MusicBrainz database

Right now, the library is pretty limited and only generates graphs of music label relations.

To use the library, do:

```python
import mbz2nx

# MusicBrainz Database PostgreSQL settings
pg_config = {
    "database": ,  # default: "musicbrainz_db"
    "user": ,  # default: "musicbrainz"
    "password": ,  # default: "musicbrainz"
    "host": ,  # default: "localhost"
    "port": ,  # default: 5432
}

my_label_graph = mbz2nx.label_graph(pg_config)
```
