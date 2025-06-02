from azure.search.documents.indexes import SearchIndexClient
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes.models import (
    SearchIndex, SearchField, SearchFieldDataType, SimpleField, SearchableField
)

endpoint = "https://<seu-servico>.search.windows.net"
admin_key = "<sua-chave-de-admin>"

client = SearchIndexClient(endpoint, AzureKeyCredential(admin_key))

# Criar índice
index = SearchIndex(
    name="documentos-index",
    fields=[
        SimpleField(name="id", type=SearchFieldDataType.String, key=True),
        SearchableField(name="content", type=SearchFieldDataType.String, analyzer_name="pt.microsoft"),
        SimpleField(name="fileName", type=SearchFieldDataType.String),
    ]
)

client.create_index(index)
