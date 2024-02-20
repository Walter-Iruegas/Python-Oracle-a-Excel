import schedule
import time
from connect_oracle import conectar_oracle
from create_excel import crear_excel
# from send_mail import enviar_correo

# Función que ejecuta todo el proceso
def job():
    print("Ejecutando proceso...")
    # Conecta a la Base de Datos Oracle
    connection = conectar_oracle()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()
        connection.close()

        # Crea el archivo Excel
        crear_excel(rows)

        print("Proceso completado exitosamente.") 

        # Envia el archivo por correo electrónico
       # enviar_correo()
    else:
        print("No se pudo establecer conexión con Oracle.")

#  Programación del cronograma para ejecución automática del trabajo

schedule.every().monday.at("08:00").do(job)
schedule.every().tuesday.at("08:00").do(job)
schedule.every().wednesday.at("08:00").do(job)
schedule.every().thursday.at("08:00").do(job)


# Bucle principal para ejecutar la planificación
while True:
    schedule.run_pending()
    time.sleep(60)  # Esperar 60 segundos antes de verificar si hay tareas programadas