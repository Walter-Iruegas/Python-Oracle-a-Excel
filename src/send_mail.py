import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def enviar_correo():
    try:
        # Configuración del servidor SMTP y credenciales
        smtp_server = 'smtp.office365.com'
        smtp_port = 587
        smtp_username = 'walter.iruegas@outlook.com'
        smtp_password = 'retlawcinder91'
        from_email = 'walter.iruegas@outlook.com'
        to_email = 'Bertin.garcia@reconext.com'
        
        
        # Crear el mensaje de correo electrónico
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = 'Este es un correo de prueba para el perrilo de Bertin'
        
        # Cuerpo del correo electrónico
        body = 'Eh perrillo adjunto esta el archivo excel abrelo o abrete motherfucker XD  i love you papi'
        msg.attach(MIMEText(body, 'plain'))
        
        # Adjuntar el archivo de Excel
        filename = 'usuarios.xlsx'
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename= ' + filename)
        msg.attach(part)
        
        # Iniciar sesión en el servidor SMTP y enviar el correo electrónico
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        print('Correo electrónico enviado correctamente.')
        server.quit()
    except Exception as e:
        print('Error al enviar el correo electrónico:', e)
