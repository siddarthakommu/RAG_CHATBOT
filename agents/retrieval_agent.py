from agents.message_protocol import MCPMessage
from utils.embedding_helper import load_embedding_model
from db.chroma_setup import collection
import uuid

class RetrievalAgent:
    def __init__(self):
        self.model = load_embedding_model()

    def index(self, message):
        chunks = message.payload["chunks"]
        self.index_chunks(chunks)

    def index_chunks(self, chunks):
        print(" Received chunks for indexing:")
        for i, c in enumerate(chunks[:5]):
            print(f"Chunk {i+1}: {repr(c[:100])}")  # show first 100 chars

        embeddings = self.model.encode(chunks)
        for chunk, emb in zip(chunks, embeddings):
            collection.add(
                documents=[chunk],
                embeddings=[emb.tolist()],
                ids=[str(uuid.uuid4())]
            )

    def retrieve(self, query):
        trace_id = str(uuid.uuid4())
        q_embedding = self.model.encode([query])[0]
        results = collection.query(query_embeddings=[q_embedding.tolist()], n_results=3)
        chunks = results["documents"][0]
        return MCPMessage(
            sender="RetrievalAgent",
            receiver="LLMResponseAgent",
            type_="RETRIEVAL_RESULT",
            trace_id=trace_id,
            payload={
                "retrieved_context": chunks,
                "query": query
            }
        )
