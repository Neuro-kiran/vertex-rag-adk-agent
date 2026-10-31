# Vertex AI RAG Engine + ADK Agent

A grounded document Q&A agent: documents in Cloud Storage -> **Vertex AI RAG Engine** corpus -> **Gemini** agent built with Google's **Agent Development Kit (ADK)**. Answers cite sources and refuse to guess.

## Run
```bash
pip install -r requirements.txt
cp .env.example .env && export $(grep -v '^#' .env | xargs)
gcloud auth application-default login
python create_corpus.py gs://your-bucket/docs/   # copy the printed name into RAG_CORPUS
python run.py "What does our refund policy say?"
```

## Test
```bash
RAG_CORPUS=projects/p/locations/us-central1/ragCorpora/1 pytest
```

## Stack
Python, google-adk, Vertex AI RAG Engine, Gemini, Cloud Storage.
