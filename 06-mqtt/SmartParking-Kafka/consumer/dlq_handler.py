# consumer/dlq_handler.py
from kafka import KafkaProducer

class DeadLetterQueueHandler:
    def __init__(self, bootstrap_servers=['localhost:9092'], dlq_topic='parking-dlq'):
        self.dlq_topic = dlq_topic
        # Keep serializers raw bytes since it could be malformed string/bytes data
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    def handle_failure(self, raw_message, error_exception):
        """
        Forwards unprocessable/corrupted messages to the DLQ topic.
        """
        error_info = f"Error: {str(error_exception)}".encode('utf-8')
        
        # We craft a wrapper payload or send the raw bytes with headers if needed.
        # For simplicity, we forward the raw faulty bytes message to the DLQ topic.
        try:
            # If raw_message is already string/bytes, send it
            payload = raw_message if isinstance(raw_message, bytes) else str(raw_message).encode('utf-8')
            
            # Send to DLQ
            self.producer.send(self.dlq_topic, value=payload)
            self.producer.flush()
            print(f"💾 [DLQ] Malformed message safely routed to '{self.dlq_topic}'. Reason: {error_exception}")
        except Exception as e:
            print(f"🚨 [CRITICAL] DLQ Failed to save corrupt message: {e}")