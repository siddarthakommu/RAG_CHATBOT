class MCPMessage:
    def __init__(self, sender, receiver, type_, trace_id, payload):
        self.sender = sender
        self.receiver = receiver
        self.type = type_
        self.trace_id = trace_id
        self.payload = payload

    def to_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "type": self.type,
            "trace_id": self.trace_id,
            "payload": self.payload
        }

    @staticmethod
    def from_dict(data):
        return MCPMessage(
            sender=data["sender"],
            receiver=data["receiver"],
            type_=data["type"],
            trace_id=data["trace_id"],
            payload=data["payload"]
        )