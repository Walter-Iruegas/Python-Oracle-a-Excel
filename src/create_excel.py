from openpyxl import Workbook

def crear_excel(rows):
    try:
        # Crear un nuevo libro de Excel
        wb = Workbook()
        # Activar la primera hoja
        ws = wb.active
        
        # Iterar sobre las filas y escribirlas en Excel
        for row_index, row_data in enumerate(rows, start=1):
            for column_index, cell_data in enumerate(row_data, start=1):
                ws.cell(row=row_index, column=column_index, value=str(cell_data))
        
        # Guardar el libro de Excel
        wb.save("usuarios.xlsx")
        print("Tabla exportada exitosamente a usuarios.xlsx")
    except Exception as e:
        print("Error al crear el archivo Excel:", e)
