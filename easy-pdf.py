import os
import random
import string
import sys

from pikepdf import PasswordError, Pdf
from PyPDF2 import PdfFileReader, PdfFileWriter
from tqdm import tqdm

def combine_pdfs(files, reverse=False, page_ranges=None):
    pdf_writer = PdfFileWriter()
    
    if reverse:
        files = files[::-1]
    
    for idx, pdf_file in enumerate(files):
        with open(pdf_file, 'rb') as pdf:
            pdf_reader = PdfFileReader(pdf)
            start_page, end_page = (0, pdf_reader.getNumPages())
            if page_ranges and idx < len(page_ranges):
                start_page, end_page = page_ranges[idx]
            
            for page_num in range(start_page, end_page):
                page = pdf_reader.getPage(page_num)
                pdf_writer.addPage(page)
    
    output_pdf = "combined.pdf"
    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def split_pdf(pdf_file):
    folder_name = pdf_file.replace('.pdf', '')
    
    if os.path.exists(folder_name):
        folder_name += f"-easy-pdf-{generate_random_string(3)}"
    
    os.mkdir(folder_name)

    with open(pdf_file, 'rb') as pdf:
        pdf_reader = PdfFileReader(pdf)
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            output_pdf = os.path.join(folder_name, f"{folder_name}-{page_num + 1}.pdf")
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(page)
            with open(output_pdf, 'wb') as output_file:
                pdf_writer.write(output_file)

def crack_pdf(pdf_file, wordlist_file):
    if not os.path.exists(wordlist_file):
        print("Wordlist file not found.")
        return
    
    password_list = [line.strip() for line in open(wordlist_file, "r")]
    with Pdf.open(pdf_file) as pdf:
        for password in tqdm(password_list, "Cracking Password"):
            try:
                pdf.authenticate(password)
                print("+ Password found:", password)
                with open(f"{pdf_file}_password.txt", "w", encoding="utf-8") as lgf:
                    lgf.write(password)
                break
            except PasswordError:
                continue
            except Exception as e:
                print("- Error:", e)

def encrypt_pdf(input_pdf, password):
    output_pdf = f"encrypted_{os.path.basename(input_pdf)}"
    with open(input_pdf, 'rb') as pdf:
        pdf_reader = PdfFileReader(pdf)
        pdf_writer = PdfFileWriter()
        
        for page_num in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page_num))
        
        pdf_writer.encrypt(user_pwd=password, use_128bit=True)
        with open(output_pdf, 'wb') as output:
            pdf_writer.write(output)
    
    print(f"Encrypted PDF saved as {output_pdf}")

def decrypt_pdf(input_pdf, password):
    output_pdf = f"decrypted_{os.path.basename(input_pdf)}"
    try:
        with Pdf.open(input_pdf, password=password) as pdf:
            pdf.save(output_pdf)
        print(f"Decrypted PDF saved as {output_pdf}")
    except PasswordError:
        print("Incorrect password.")

def rotate_pages(input_pdf, rotation, page_nums=None):
    output_pdf = f"rotated_{os.path.basename(input_pdf)}"
    with open(input_pdf, 'rb') as pdf:
        pdf_reader = PdfFileReader(pdf)
        pdf_writer = PdfFileWriter()
        
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            if page_nums is None or page_num in page_nums:
                page.rotateClockwise(rotation)
            pdf_writer.addPage(page)
        
        with open(output_pdf, 'wb') as output:
            pdf_writer.write(output)
    
    print(f"Rotated PDF saved as {output_pdf}")

def add_watermark(input_pdf, watermark_pdf):
    output_pdf = f"watermarked_{os.path.basename(input_pdf)}"
    with open(input_pdf, 'rb') as pdf, open(watermark_pdf, 'rb') as watermark:
        pdf_reader = PdfFileReader(pdf)
        watermark_reader = PdfFileReader(watermark)
        watermark_page = watermark_reader.getPage(0)
        pdf_writer = PdfFileWriter()
        
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            page.mergePage(watermark_page)
            pdf_writer.addPage(page)
        
        with open(output_pdf, 'wb') as output:
            pdf_writer.write(output)
    
    print(f"Watermarked PDF saved as {output_pdf}")

def display_help():
    print("Usage: easy-pdf [command] [options]")
    print("Commands:")
    print("  combine [files] [-r, --reverse] [--range start1-end1 start2-end2 ...] Combine PDF files.")
    print("  split <pdf_file>   Split a PDF file into pages.")
    print("  crack <pdf_file> --wordlist <wordlist_file> Attempt to crack a password-protected PDF.")
    print("  encrypt <pdf_file> --password <password> Encrypt a PDF file with a password.")
    print("  decrypt <pdf_file> --password <password> Decrypt a PDF file with a password.")
    print("  rotate <pdf_file> --rotation <angle> [--pages <page_nums>] Rotate pages in a PDF.")
    print("  watermark <pdf_file> --watermark <watermark_pdf> Add a watermark to a PDF.")
    print("  help Display this help message.")

def main():
    if len(sys.argv) < 2:
        print("Usage: easy-pdf [combine|split|crack|encrypt|decrypt|rotate|watermark|help] [options]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "combine":
        files = sys.argv[2:]
        reverse = False
        page_ranges = None
        
        if '-r' in files or '--reverse' in files:
            reverse = True
            files.remove('-r' if '-r' in files else '--reverse')
        
        if '--range' in files:
            range_idx = files.index('--range')
            page_ranges = [
                tuple(map(int, r.split('-'))) for r in files[range_idx + 1:]
            ]
            files = files[:range_idx]
        
        combine_pdfs(files, reverse, page_ranges)

    elif command == "split":
        if len(sys.argv) != 3:
            print("Usage: easy-pdf split <pdf_file>")
            sys.exit(1)
        pdf_file = sys.argv[2]
        split_pdf(pdf_file)

    elif command == "crack":
        if len(sys.argv) != 5 or sys.argv[3] != '--wordlist':
            print("Usage: easy-pdf crack <pdf_file> --wordlist <wordlist_file>")
            sys.exit(1)
        pdf_file = sys.argv[2]
        wordlist_file = sys.argv[4]
        crack_pdf(pdf_file, wordlist_file)

    elif command == "encrypt":
        if len(sys.argv) != 5 or sys.argv[3] != '--password':
            print("Usage: easy-pdf encrypt <pdf_file> --password <password>")
            sys.exit(1)
        pdf_file = sys.argv[2]
        password = sys.argv[4]
        encrypt_pdf(pdf_file, password)

    elif command == "decrypt":
        if len(sys.argv) != 5 or sys.argv[3] != '--password':
            print("Usage: easy-pdf decrypt <pdf_file> --password <password>")
            sys.exit(1)
        pdf_file = sys.argv[2]
        password = sys.argv[4]
        decrypt_pdf(pdf_file, password)

    elif command == "rotate":
        if len(sys.argv) < 5 or sys.argv[3] != '--rotation':
            print("Usage: easy-pdf rotate <pdf_file> --rotation <angle> [--pages <page_nums>]")
            sys.exit(1)
        pdf_file = sys.argv[2]
        rotation = int(sys.argv[4])
        page_nums = None
        if '--pages' in sys.argv:
            pages_idx = sys.argv.index('--pages')
            page_nums = list(map(int, sys.argv[pages_idx + 1:]))
        rotate_pages(pdf_file, rotation, page_nums)

    elif command == "watermark":
        if len(sys.argv) != 5 or sys.argv[3] != '--watermark':
            print("Usage: easy-pdf watermark <pdf_file> --watermark <watermark_pdf>")
            sys.exit(1)
        pdf_file = sys.argv[2]
        watermark_pdf = sys.argv[4]
        add_watermark(pdf_file, watermark_pdf)

    elif command == "help":
        display_help()

    else:
        print("Unknown command:", command)
        display_help()

if __name__ == "__main__":
    main()
