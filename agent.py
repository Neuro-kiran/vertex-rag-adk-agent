"""Document Q&A agent grounded on Vertex AI RAG Engine, built with Google ADK."""
import os

from google.adk.agents import Agent
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from vertexai.preview import rag

MODEL = os.getenv("MODEL", "gemini-2.5-flash")
RAG_CORPUS = os.getenv("RAG_CORPUS", "")

retrieval_tool = VertexAiRagRetrieval(
    name="retrieve_documents",
    description="Retrieves relevant passages from the private document corpus.",
    rag_resources=[rag.RagResource(rag_corpus=RAG_CORPUS)],
    similarity_top_k=5,
    vector_distance_threshold=0.5,
)

root_agent = Agent(
    name="rag_agent",
    model=MODEL,
    description="Answers questions using only the private document corpus.",
    instruction=(
        "Answer using ONLY information returned by retrieve_documents. "
        "Cite the source document for each claim. If the documents do not "
        "contain the answer, say you could not find it - do not guess."
    ),
    tools=[retrieval_tool],
)
