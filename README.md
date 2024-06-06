# Easy-PDF

Easy-PDF is a Python command-line application for working with PDF files. It provides a set of convenient features to manipulate and manage PDF files.

## Features

- **Combine PDFs:** Merge multiple PDF files into one, either in the order they are provided or in reverse order.
- **Split PDF:** Split a PDF file into individual pages and organize them in a folder named after the original PDF. If the folder already exists, a unique identifier is added to its name.
- **Crack PDF Password:** Attempt to crack the password of a password-protected PDF using a wordlist.
- **Merge PDFs with Specific Page Range:** Specify a page range to merge from each PDF.
- **Encrypt PDF:** Encrypt a combined PDF with a password.
- **Decrypt PDF:** Decrypt a PDF given a password.
- **Rotate Pages:** Rotate individual pages or all pages in a PDF.
- **Add Watermark:** Add a watermark to all pages of a PDF.

## Requirements

Before using Easy-PDF, ensure you have the required Python libraries installed. You can install them using pip:

```bash
pip install -r requirements.txt
```

- or

```bash
pip install PyPDF2 pikepdf tqdm
```

## Usage

### Combine PDFs

Combine multiple PDF files into one.

```bash
easy-pdf combine [files] [-r|--reverse] [--range start1-end1 start2-end2 ...]
```

- `[files]`: List of PDF files to combine.
- `-r` or `--reverse`: Combine files in reverse order.
- `--range start1-end1 start2-end2 ...`: Specify page ranges to combine from each PDF file.

### Split PDF

Split a PDF file into individual pages.

```bash
easy-pdf split <pdf_file>
```

- `<pdf_file>`: The PDF file to split.

### Crack PDF Password

Attempt to crack the password of a password-protected PDF using a wordlist.

```bash
easy-pdf crack <pdf_file> --wordlist <wordlist_file>
```

- `<pdf_file>`: The PDF file to crack.
- `--wordlist <wordlist_file>`: Specifies the wordlist file.

### Encrypt PDF

Encrypt a combined PDF with a password.

```bash
easy-pdf encrypt <pdf_file> --password <password>
```

- `<pdf_file>`: The PDF file to encrypt.
- `--password <password>`: The password to set for the encrypted PDF.

### Decrypt PDF

Decrypt a PDF given a password.

```bash
easy-pdf decrypt <pdf_file> --password <password>
```

- `<pdf_file>`: The PDF file to decrypt.
- `--password <password>`: The password for the encrypted PDF.

### Rotate Pages

Rotate individual pages or all pages in a PDF.

```bash
easy-pdf rotate <pdf_file> --rotation <angle> [--pages <page_nums>]
```

- `<pdf_file>`: The PDF file to rotate.
- `--rotation <angle>`: The angle to rotate pages (e.g., 90, 180, 270).
- `--pages <page_nums>`: (Optional) Specific page numbers to rotate.

### Add Watermark

Add a watermark to all pages of a PDF.

```bash
easy-pdf watermark <pdf_file> --watermark <watermark_pdf>
```

- `<pdf_file>`: The PDF file to watermark.
- `--watermark <watermark_pdf>`: The PDF file to use as the watermark.

### Help

For detailed usage instructions, run:

```bash
easy-pdf help
```

## Example Usage

```bash
# Combine PDFs
easy-pdf combine file1.pdf file2.pdf file3.pdf

# Combine PDFs in reverse order
easy-pdf combine file1.pdf file2.pdf file3.pdf -r

# Combine PDFs with specific page ranges
easy-pdf combine file1.pdf file2.pdf file3.pdf --range 1-3 2-4 1-2

# Split a PDF
easy-pdf split file1.pdf

# Crack PDF password using a wordlist
easy-pdf crack file1.pdf --wordlist wordlist.txt

# Encrypt a PDF
easy-pdf encrypt file1.pdf --password mypassword

# Decrypt a PDF
easy-pdf decrypt file1.pdf --password mypassword

# Rotate all pages in a PDF by 90 degrees
easy-pdf rotate file1.pdf --rotation 90

# Rotate specific pages in a PDF
easy-pdf rotate file1.pdf --rotation 90 --pages 1 3 5

# Add a watermark to a PDF
easy-pdf watermark file1.pdf --watermark watermark.pdf
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Note

- This README.md file was generated with the help of ChatGPT on `6/6/2024`.
