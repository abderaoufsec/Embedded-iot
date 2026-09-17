# consumer/consumer.py
import sys
from kafka import KafkaConsumer
from consumer.processor import process_parking_message
from consumer.alerts import AlertSystem
from consumer.dlq_handler import DeadLetterQueueHandler
def main():
    bootstrap_servers = ['localhost:9092']
    input_topic = 'parking-data'
    
    print("🚀 Initializing Student 2 Core Consumer Subsystem...")
    
    # 1. Initialize our helper modules
    alert_sys = AlertSystem(bootstrap_servers=bootstrap_servers)
    dlq_sys = DeadLetterQueueHandler(bootstrap_servers=bootstrap_servers)
    
    # 2. Configure Consumer with a Consumer Group name
    # Assigning a group_id enables Kafka to scale horizontally and provide fault tolerance.
    consumer = KafkaConsumer(
        input_topic,
        bootstrap_servers=bootstrap_servers,
        group_id='parking-processors', 
        auto_offset_reset='latest',
        enable_auto_commit=True,
        value_deserializer=lambda x: x.decode('utf-8') # Keep raw string format for parsing safety
    )
    
    print(f"📥 Listening for sensor streams on topic '{input_topic}' [Group: parking-processors]...")
    
    try:
        for message in consumer:
            raw_val = message.value
            print(f"\n📥 Received message from Partition {message.partition}")
            
            try:
                # Step A: Run real-time processing rules
                processed_data, alert_needed, alert_reason = process_parking_message(raw_val)
                print(f"✅ Processed data safely: Spot {processed_data['spot_id']} is {processed_data['status']}.")
                
                # (Optional hook for Student 3): At this point, processed_data can be pushed 
                # to SQLite database or local socket for real-time visualization.
                
                # Step B: Route alerts if threshold violated
                if alert_needed:
                    alert_sys.send_alert(
                        spot_id=processed_data['spot_id'], 
                        reason=alert_reason, 
                        original_data=processed_data
                    )
                    
            except Exception as err:
                # Step C: Fallback to Dead Letter Queue on parsing/processing runtime errors
                print(f"❌ Processing error encountered: {err}")
                dlq_sys.handle_failure(raw_message=raw_val, error_exception=err)
                
    except KeyboardInterrupt:
        print("\n👋 Consumer stopped manually. Exiting gracefully.")
    finally:
        consumer.close()

if __name__ == "__main__":
    main()