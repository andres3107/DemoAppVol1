import PyPDF2
import re
import os

def pdf_to_text(pdf_path, text_path):
    # Verificar si el archivo de texto ya existe y contiene la misma información
    if os.path.exists(text_path):
        with open(text_path, 'r', encoding='utf-8') as text_file:
            existing_text = text_file.read()

        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ''
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

        # Verificar si el texto extraído coincide con el texto existente
        if existing_text.strip() == text.strip():
            print("El archivo de texto ya contiene la información del PDF.")
            return

    # Si el archivo de texto no existe o no coincide, extraer el texto del PDF y escribirlo en el archivo
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    # Eliminar caracteres no alfanuméricos o espacios
    clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    with open(text_path, 'w', encoding='utf-8') as text_file:
        text_file.write(clean_text)

    print("La información del PDF ha sido guardada en el archivo de texto.")

# Ruta del archivo PDF de entrada y ruta del archivo de texto de salida
pdf_input_path = 'demo1.pdf'
text_output_path = 'infoempresa.txt'

# Llama a la función para convertir el PDF a texto
pdf_to_text(pdf_input_path, text_output_path)