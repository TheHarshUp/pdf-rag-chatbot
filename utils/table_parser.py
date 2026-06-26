import pdfplumber


def extract_tables(pdf_path):
    all_tables = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            tables = page.extract_tables()

            for table in tables:
                if table:
                    all_tables.append({
                        "page": page_num,
                        "table": table
                    })

    return all_tables