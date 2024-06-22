import pika

def send_message(message):
    # Conexión al servidor de RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Asegurarse de que la cola existe
    channel.queue_declare(queue='email_queue')

    # Enviar el mensaje a la cola
    channel.basic_publish(exchange='', routing_key='email_queue', body=message)
    print(f" [x] Sent '{message}'")

    # Cerrar la conexión
    connection.close()

# Ejemplo de uso
send_message('Hola, este es un mensaje para enviar por correo electrónico')