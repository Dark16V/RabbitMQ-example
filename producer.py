from pika import BlockingConnection, ConnectionParameters, PlainCredentials


connection_params = ConnectionParameters(
    host='localhost',
    port=5672,
    credentials=PlainCredentials("admin", "admin")
)

def main():
    with BlockingConnection(connection_params) as connection:
        with connection.channel() as channel:
            channel.queue_declare(queue='messages')
            
            channel.basic_publish(
                exchange='',
                routing_key='messages',
                body='Hello World!'
            )
            print('Message sent')


if __name__ == '__main__':
    main()