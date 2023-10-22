# Easy-PDF

Easy-PDF is a Python command-line application for working with PDF files. It provides a set of convenient features to manipulate and manage PDF files.

## Features

- **Combine PDFs:** Merge multiple PDF files into one, either in the order they are provided or in reverse order.

- **Split PDF:** Split a PDF file into individual pages and organize them in a folder named after the original PDF. If the folder already exists, a unique identifier is added to its name.

- **Crack PDF Password:** Attempt to crack the password of a password-protected PDF using a wordlist.

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
easy-pdf combine [files] [-r|--reverse]
```

- `[files]`: List of PDF files to combine.
- `-r` or `--reverse`: Combine files in reverse order.

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

# Split a PDF
easy-pdf split file1.pdf

# Crack PDF password using a wordlist
easy-pdf crack file1.pdf --wordlist wordlist.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Note

- this README.md file was generated with the help of ChatGPT on `10/22/2023`

