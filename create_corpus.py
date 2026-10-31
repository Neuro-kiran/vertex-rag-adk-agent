"""Create a Vertex AI RAG Engine corpus and import documents from Cloud Storage.

Usage: python create_corpus.py gs://your-bucket/docs/
Prints the corpus resource name -> put it in RAG_CORPUS in .env
"""
import os
import sys

import vertexai
from vertexai.preview import rag

vertexai.init(
    project=os.environ["GOOGLE_CLOUD_PROJECT"],
    location=os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1"),
)

corpus = rag.create_corpus(display_name="adk-rag-corpus")
rag.import_files(
    corpus.name,
    [sys.argv[1]],
    transformation_config=rag.TransformationConfig(
        chunking_config=rag.ChunkingConfig(chunk_size=512, chunk_overlap=100)
    ),
)
print(corpus.name)
