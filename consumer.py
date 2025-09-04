from pika import BlockingConnection, ConnectionParameters, PlainCredentials


connection_params = ConnectionParameters(
    host='localhost',
    port=5672,
    credentials=PlainCredentials("admin", "admin")
)


def proccess_message(ch, method, body):
    print(f'Received message: {body.decode()}')
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    with BlockingConnection(connection_params) as connection:
        with connection.channel() as channel:
            channel.queue_declare(queue='messages')
            
            channel.basic_consume(
                queue='messages',
                on_message_callback=proccess_message
            )
            print('Wait for messages')
            channel.start_consuming()
            


if __name__ == '__main__':
    main()