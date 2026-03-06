from pypdf import PdfWriter
import os
import sys
from natsort import natsorted

if __name__ == '__main__':
    route = os.path.join(os.path.dirname(__file__), 'files')
    docs = os.listdir(route)
    pdfs = []
    for doc in docs:
        if '.pdf' in doc:
            pdfs.append(os.path.join(route, doc))

    natsorted(pdfs)
    print(f"Documents to process: {pdfs}")

    # Crear objeto PdfWriter
    writer = PdfWriter()

    # Añadir cada PDF a la fusión
    for pdf in pdfs:
        writer.append(pdf)

    # Guardar el archivo fusionado
    with open('final_document.pdf', 'wb') as output:
        writer.write(output)

    print("PDFs joined")
