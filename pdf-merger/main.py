import PyPDF2

def merge_pdfs(input_paths, output_path):
    try:
        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Iterate through each input PDF and add its pages to the writer
        for path in input_paths:
            with open(path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                # Add all pages to the writer
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    pdf_writer.add_page(page)

        # Write the merged PDF to the output file
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

        print("PDFs merged successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
input_paths = ["COVID.pdf", "english.pdf"]  # Replace with the paths to your input PDFs
output_path = "merged_output.pdf"  # Replace with the desired output path

merge_pdfs(input_paths, output_path)
