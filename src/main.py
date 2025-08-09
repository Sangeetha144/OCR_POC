import os
from src.ocr_processor import process_file

def main():
    input_file = "input/Rental-City Plus.pdf"
    # input_file = "input/Rental-City Scape.pdf"
    # input_file = "input/Rental-Pacific Mall Jasola.pdf"
    # input_file = "input/Rental-AMRI Hospital.pdf"

    if not os.path.exists(input_file):
        print(f"File not found: {input_file}")
        return
 
    print(f"Processing file: {input_file}")
    extracted_text = process_file(input_file)
 
    output_file = "output/Rental-AMRI Hospital.txt"
   
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(extracted_text)
       
    print(f"OCR Extraction complete! Text saved to: {output_file}")  
 
if __name__ == "__main__":
    main()