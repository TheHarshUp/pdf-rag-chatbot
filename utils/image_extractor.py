import fitz
import os

def extract_images(pdf_path):
    image_paths = []

    doc = fitz.open(pdf_path)

    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_folder = f"extracted_images/{pdf_name}"
    os.makedirs(output_folder, exist_ok=True)

    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images(full=True)

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)

            image_bytes = base_image["image"]
            ext = base_image["ext"]

            width = base_image["width"]
            height = base_image["height"]

            ratio = width / height

            if width < 400 or height < 300:
                continue

            if ratio > 4 or ratio < 0.25:
                continue

            image_path = os.path.join(
                output_folder,
                f"page_{page_num+1}_{img_index}.{ext}"
            )

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            image_paths.append({
                "path": image_path,
                "page": page_num + 1,
                "width": width,
                "height": height,
                "ratio": ratio
            })

    return image_paths