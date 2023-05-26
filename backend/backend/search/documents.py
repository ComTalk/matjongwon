from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from places.models import Place

@registry.register_document
class PlaceDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = "place"
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Place # The model associated with this Document

        fields = [
            'name',
            'category',
            'address',
            'menu',
            'description',
        ]
        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True

        # Configure how the index should be refreshed after an update.
        # See Elasticsearch documentation for supported options:
        # https://www.elastic.co/guide/en/elasticsearch/reference/master/docs-refresh.html
        # This per-Document setting overrides settings.ELASTICSEARCH_DSL_AUTO_REFRESH.
        # auto_refresh = False

        # Paginate the django queryset used to populate the index with the specified size
        # (by default it uses the database driver's default setting)
        # queryset_pagination = 5000

