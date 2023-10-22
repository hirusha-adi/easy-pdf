import os
import random
import string
import sys

from pikepdf import PasswordError, Pdf
from PyPDF2 import PdfFileReader, PdfFileWriter
from tqdm import tqdm


def combine_pdfs(files, reverse=False):
    pdf_writer = PdfFileWriter()
    
    if reverse:
        files = files[::-1]
    
    for pdf_file in files:
        with open(pdf_file, 'rb') as pdf:
            pdf_reader = PdfFileReader(pdf)
            for page_num in range(pdf_reader.getNumPages()):
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

def display_help():
    print("Usage: easy-pdf [command] [options]")
    print("Commands:")
    print("  combine [files]    Combine PDF files.")
    print("     -r, --reverse     Combine files in reverse order.")
    print("  split <pdf_file>   Split a PDF file into pages.")
    print("  crack <pdf_file> --wordlist <wordlist_file>")
    print("                     Attempt to crack a password-protected PDF.")
    print("                     --wordlist specifies the wordlist file.")

def main():
    if len(sys.argv) < 2:
        print("Usage: easy-pdf [combine|split|crack] [options]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "combine":
        files = sys.argv[2:]
        reverse = False
        if '-r' in files or '--reverse' in files:
            reverse = True
            files.remove('-r' if '-r' in files else '--reverse')
        combine_pdfs(files, reverse)

    elif command == "split":
        if len(sys.argv) != 3:
            print("Usage: easy-pdf split <pdf_file>")
            sys.exit(1)
        pdf_file = sys.argv[2]
        split_pdf(pdf_file)

    elif command == "crack":
        if len(sys.argv) != 4:
            print("Usage: easy-pdf crack <pdf_file> --wordlist <wordlist_file>")
            sys.exit(1)
        pdf_file = sys.argv[2]
        wordlist_file = sys.argv[4]
        crack_pdf(pdf_file, wordlist_file)

    elif command == "help":
        display_help()

    else:
        print("Unknown command:", command)
        display_help()

if __name__ == "__main__":
    main()
