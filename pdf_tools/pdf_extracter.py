import concurrent.futures
from multiprocessing import freeze_support
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

def pdf_extract(pdf, segments):
    """
    pdf: str | Path
    segments: [(start, end), {'start': int, 'end': int}]

    if segments is empty, then all pages must be extracted individually

    """
    with open(pdf, 'rb') as read_stream:
        pdf_reader = PdfFileReader(read_stream)
        if len(segments) == 0:
            segments = [(i+1, i+1) for i in range(pdf_reader.numPages)]
        for segment in segments:
            pdf_writer = PdfFileWriter()
            # support {'start': 3, 'end': 3} or (start, end)
            try:
                start_page, end_page = segment['start'], segment['end']
            except TypeError:
                start_page, end_page = segment
            for page_num in range(start_page - 1, end_page):
                pdf_writer.addPage(pdf_reader.getPage(page_num))
            p = Path(pdf)
            ouput = p.parent / (p.with_stem(f'{p.stem}_' + (f'pages_{start_page}-{end_page}' if start_page != end_page else f'page_{start_page}')))
            with open(ouput, 'wb') as out:
                pdf_writer.write(out)

def __pdf_extract(pair):
    return pdf_extract(*pair)

freeze_support()
pdf_name = r"C:\Users\user\Downloads\doc.pdf"
segments = [(2,3)]  # leave empty to extract all pages individually
pdf_extract(pdf_name, segments)
