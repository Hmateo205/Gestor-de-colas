import pika
import smtplib
from email.mime.text import MIMEText

def send_email(message):
    # Configuración del servidor de correo
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'carlos.guagrilla100@gmail.com'
    smtp_password = 'egnw cvcs lcnk vira'

    # Crear el mensaje de correo
    msg = MIMEText(message)
    msg['Subject'] = 'Nuevo Mensaje de la Cola'
    msg['From'] = smtp_user
    msg['To'] = 'socialwave2024@gmail.com'

    # Enviar el correo
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, 'destinatario@example.com', msg.as_string())
        print("Correo enviado")

def callback(ch, method, properties, body):
    message = body.decode()
    print(f" [x] Received '{message}'")
    send_email(message)

def start_consumer():
    # Conexión al servidor de RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Asegurarse de que la cola existe
    channel.queue_declare(queue='email_queue')

    # Configurar el consumidor
    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

# Ejemplo de uso
start_consumer()