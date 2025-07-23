from utils.file_parser import parse_file
from agents.message_protocol import MCPMessage
import uuid
import re

class IngestionAgent:
    def process(self, file_path):
        trace_id = str(uuid.uuid4())
        parsed_text = parse_file(file_path)

        if not isinstance(parsed_text, str) or len(parsed_text.strip()) < 10:
            return MCPMessage(
                sender="IngestionAgent",
                receiver="RetrievalAgent",
                type_="INGESTION_RESULT",
                trace_id=trace_id,
                payload={
                    "chunks": ["[Warning] Document content is too short or invalid."],
                    "file": file_path
                }
            )

        sentences = re.split(r'(?<=[.!?]) +', parsed_text.strip())
        chunks = []
        current_chunk = ""

        for sentence in sentences:
            if len(current_chunk) + len(sentence) <= 400:
                current_chunk += sentence + " "
            else:
                chunks.append(current_chunk.strip())
                current_chunk = sentence + " "

        if current_chunk:
            chunks.append(current_chunk.strip())

        if not chunks:
            chunks = [parsed_text[:400]]

        return MCPMessage(
            sender="IngestionAgent",
            receiver="RetrievalAgent",
            type_="INGESTION_RESULT",
            trace_id=trace_id,
            payload={
                "chunks": chunks,
                "file": file_path
            }
        )
