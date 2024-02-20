import cx_Oracle
from openpyxl import Workbook

try:
    connection = cx_Oracle.connect(
        user='ADMIN',
        password='123',
        dsn='localhost:1521/ORCL',
        encoding='UTF-8'
    )
    print(connection.version)
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()
    
    # Crear un nuevo libro de Excel
    wb = Workbook()
    # Activar la primera hoja
    ws = wb.active
    
    # Iterar sobre las filas de la tabla Oracle y escribirlas en Excel
    for row_index, row_name in enumerate(rows, start=1):
        for column_index, cell_data in enumerate(row_name, start=1):
            ws.cell(row=row_index, column=column_index, value=str(cell_data))
    
    # Guardar el libro de Excel
    wb.save("usuarios.xlsx")
    print("Tabla exportada exitosamente a usuarios.xlsx")
    
except Exception as ex:
    print("Error:", ex)
finally:
    if connection:
        connection.close()
        print("Conexión finalizada")
