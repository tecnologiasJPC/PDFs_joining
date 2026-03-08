from pypdf import PdfWriter, PdfReader
from natsort import natsorted
import warnings
import os

if __name__ == '__main__':
    route = os.path.dirname(__file__)
    docs = os.listdir(route)
    pdfs = []
    for doc in docs:
        if '.pdf' in doc and not 'joined_document' in doc:
            pdfs.append(os.path.join(route, doc))

    natsorted(pdfs)
    print(f"Documents to process: {pdfs}")

    warnings.filterwarnings("ignore")

    # crear objeto PdfWriter
    writer = PdfWriter()

    # añadir cada PDF a la fusión
    for pdf in pdfs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            if "/Annots" in page:
                try:
                    annots = page["/Annots"]
                    # si es un objeto indirecto, resolverlo primero
                    if hasattr(annots, 'get_object'):
                        annots = annots.get_object()
                    page.pop("/Annots", None)
                except Exception:
                    pass
        writer.append(pdf)

    # Guardar el archivo fusionado
    with open(os.path.join(route,'joined_document.pdf'), 'wb') as output:
        writer.write(output)

    print("PDFs joined")
