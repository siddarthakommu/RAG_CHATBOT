from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent

ingestor = IngestionAgent()
retriever = RetrievalAgent()
responder = LLMResponseAgent()

def pipeline(file_paths, user_query):
    all_chunks = []
    for file_path in file_paths:
        ingest_msg = ingestor.process(file_path)
        chunks = ingest_msg.payload["chunks"]
        all_chunks.extend(chunks)
    
    print(" Total Chunks to Index:", len(all_chunks))
    print(" Sample chunk:", repr(all_chunks[0]) if all_chunks else "None")

    retriever.index_chunks(all_chunks)
    retrieval_msg = retriever.retrieve(user_query)
    final_msg = responder.respond(retrieval_msg)
    return final_msg.payload
