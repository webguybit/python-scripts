# PDF_UTILS - PDF Splitter Module

A Python utility package for splitting PDF files into multiple pieces with various options.

## Installation

The required packages are already installed in the `env` virtual environment:
- PyPDF2
- pdfplumber
- PyMuPDF (fitz)
- reportlab

## Quick Start

### Option 1: Interactive CLI (Easiest - Like a Web App!)

The easiest way to use the PDF splitter is through the interactive command-line interface:

```bash
# Method 1: Using the launcher script (automatically activates env)
./PDF_UTILS/run_splitter.sh

# Method 2: Manual activation
cd PDF_UTILS
source ../env/bin/activate
python interactive_splitter.py
```

**Features of Interactive Mode:**
- 🎯 User-friendly prompts and menus
- 📂 Drag-and-drop file support
- ✅ Input validation and error handling
- 🔄 Perform multiple operations on the same PDF
- 💡 Helpful hints and examples

**Interactive Menu Options:**
1. Split into TWO parts (at middle)
2. Split into TWO parts (at specific page)
3. Split into N equal parts
4. Split by custom page ranges
5. Extract specific pages

### Option 2: Python Code (Programmatic)

```python
from PDF_UTILS import PDFSplitter

# Initialize with a PDF file
splitter = PDFSplitter("document.pdf")

# Get total pages
print(f"Total pages: {splitter.get_total_pages()}")

# Split into two pieces at the middle
part1, part2 = splitter.split_into_two()

# Split at a specific page (e.g., page 10)
part1, part2 = splitter.split_into_two(split_at_page=10)

# Split and save to a custom directory
part1, part2 = splitter.split_into_two(split_at_page=5, output_dir="output")
```

## Features

### 1. Split into Two Pieces (Primary Feature)

```python
splitter = PDFSplitter("document.pdf")

# Split at middle (default)
part1, part2 = splitter.split_into_two()

# Split at specific page
part1, part2 = splitter.split_into_two(split_at_page=15)

# Custom output directory
part1, part2 = splitter.split_into_two(
    split_at_page=10, 
    output_dir="split_output"
)
```

### 2. Split into N Equal Parts

```python
# Split into 3 parts
parts = splitter.split_into_n_parts(n_parts=3)

# Split into 5 parts with custom output directory
parts = splitter.split_into_n_parts(
    n_parts=5, 
    output_dir="multi_parts"
)
```

### 3. Split by Custom Page Ranges

```python
# Define page ranges (1-based, inclusive)
ranges = [
    (1, 10),    # Pages 1-10
    (11, 25),   # Pages 11-25
    (26, 50)    # Pages 26-50
]

parts = splitter.split_by_ranges(ranges)
```

### 4. Extract Specific Pages

```python
# Extract pages 1, 5, 10, 15
output = splitter.extract_pages([1, 5, 10, 15])

# With custom output file
output = splitter.extract_pages(
    pages=[2, 4, 6, 8],
    output_file="even_pages.pdf"
)
```

## Class Reference

### PDFSplitter

#### Constructor
```python
PDFSplitter(pdf_path: str)
```
- **pdf_path**: Path to the input PDF file

#### Methods

##### `get_total_pages() -> int`
Returns the total number of pages in the PDF.

##### `split_into_two(split_at_page=None, output_dir=None) -> Tuple[str, str]`
Splits the PDF into two pieces.
- **split_at_page**: Page number to split at (1-based). If None, splits at middle.
- **output_dir**: Output directory. If None, uses input file's directory.
- **Returns**: Tuple of (part1_path, part2_path)

##### `split_into_n_parts(n_parts: int, output_dir=None) -> List[str]`
Splits the PDF into N equal parts.
- **n_parts**: Number of parts (must be >= 2)
- **output_dir**: Output directory
- **Returns**: List of output file paths

##### `split_by_ranges(page_ranges: List[Tuple[int, int]], output_dir=None) -> List[str]`
Splits by custom page ranges.
- **page_ranges**: List of (start, end) tuples (1-based, inclusive)
- **output_dir**: Output directory
- **Returns**: List of output file paths

##### `extract_pages(pages: List[int], output_file=None) -> str`
Extracts specific pages into a new PDF.
- **pages**: List of page numbers (1-based)
- **output_file**: Output file path
- **Returns**: Output file path

## Output File Naming

- Two pieces: `{original_name}_part1.pdf`, `{original_name}_part2.pdf`
- N parts: `{original_name}_part1.pdf`, `{original_name}_part2.pdf`, ...
- By ranges: `{original_name}_pages1-10.pdf`, `{original_name}_pages11-20.pdf`, ...
- Extracted: `{original_name}_extracted.pdf` (or custom name)

## Error Handling

The class includes comprehensive error handling:
- File not found errors
- Invalid PDF format errors
- Invalid page range errors
- Invalid split parameters

## Example Usage

See `example_usage.py` for complete examples.

---

## Quick Usage Guide for All PDF Packages

Below are usage examples for all installed PDF processing packages:

### 1. PyPDF2 - Basic PDF Operations

#### Merge PDFs
```python
from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append("file1.pdf")
merger.append("file2.pdf")
merger.append("file3.pdf")
merger.write("merged_output.pdf")
merger.close()
```

#### Read PDF and Extract Text
```python
from PyPDF2 import PdfReader

reader = PdfReader("document.pdf")
print(f"Number of pages: {len(reader.pages)}")

# Extract text from first page
page = reader.pages[0]
text = page.extract_text()
print(text)

# Extract text from all pages
for page_num, page in enumerate(reader.pages):
    text = page.extract_text()
    print(f"Page {page_num + 1}: {text[:100]}...")
```

#### Rotate and Save Pages
```python
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("input.pdf")
writer = PdfWriter()

# Rotate first page by 90 degrees
page = reader.pages[0]
page.rotate(90)
writer.add_page(page)

# Add remaining pages
for page in reader.pages[1:]:
    writer.add_page(page)

with open("rotated.pdf", "wb") as output_file:
    writer.write(output_file)
```

#### Extract Specific Pages
```python
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("document.pdf")
writer = PdfWriter()

# Extract pages 1, 3, 5 (0-indexed: 0, 2, 4)
for page_num in [0, 2, 4]:
    writer.add_page(reader.pages[page_num])

with open("extracted_pages.pdf", "wb") as output_file:
    writer.write(output_file)
```

#### Add Password Protection
```python
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("document.pdf")
writer = PdfWriter()

# Add all pages
for page in reader.pages:
    writer.add_page(page)

# Encrypt with password
writer.encrypt(user_password="user123", owner_password="owner456")

with open("encrypted.pdf", "wb") as output_file:
    writer.write(output_file)
```

---

### 2. pdfplumber - Extract Text, Tables & Metadata

#### Extract Text from PDF
```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    # Extract text from first page
    first_page = pdf.pages[0]
    text = first_page.extract_text()
    print(text)
    
    # Extract text from all pages
    full_text = ""
    for page in pdf.pages:
        full_text += page.extract_text()
    print(full_text)
```

#### Extract Tables from PDF
```python
import pdfplumber
import pandas as pd

with pdfplumber.open("document.pdf") as pdf:
    # Extract tables from first page
    first_page = pdf.pages[0]
    tables = first_page.extract_tables()
    
    for i, table in enumerate(tables):
        # Convert to pandas DataFrame
        df = pd.DataFrame(table[1:], columns=table[0])
        print(f"Table {i + 1}:")
        print(df)
        
        # Save to CSV
        df.to_csv(f"table_{i + 1}.csv", index=False)
```

#### Extract Words with Coordinates
```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    page = pdf.pages[0]
    
    # Extract words with their positions
    words = page.extract_words()
    for word in words[:10]:  # First 10 words
        print(f"Text: {word['text']}, "
              f"Position: ({word['x0']}, {word['top']})")
```

#### Get PDF Metadata
```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    print(f"Total pages: {len(pdf.pages)}")
    print(f"Metadata: {pdf.metadata}")
    
    # Page dimensions
    page = pdf.pages[0]
    print(f"Page width: {page.width}")
    print(f"Page height: {page.height}")
```

#### Search for Specific Text
```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    search_term = "invoice"
    
    for page_num, page in enumerate(pdf.pages):
        text = page.extract_text()
        if search_term.lower() in text.lower():
            print(f"Found '{search_term}' on page {page_num + 1}")
```

---

### 3. PyMuPDF (fitz) - Advanced PDF Manipulation

#### Read and Extract Text
```python
import fitz  # PyMuPDF

# Open PDF
doc = fitz.open("document.pdf")

print(f"Number of pages: {doc.page_count}")

# Extract text from all pages
for page_num in range(doc.page_count):
    page = doc[page_num]
    text = page.get_text()
    print(f"Page {page_num + 1}:\n{text}\n")

doc.close()
```

#### Convert PDF Pages to Images
```python
import fitz

doc = fitz.open("document.pdf")

# Convert first page to image
page = doc[0]
pix = page.get_pixmap(dpi=150)  # Higher DPI for better quality
pix.save("page_1.png")

# Convert all pages
for page_num in range(doc.page_count):
    page = doc[page_num]
    pix = page.get_pixmap(dpi=150)
    pix.save(f"page_{page_num + 1}.png")

doc.close()
```

#### Extract Images from PDF
```python
import fitz

doc = fitz.open("document.pdf")

for page_num in range(doc.page_count):
    page = doc[page_num]
    image_list = page.get_images()
    
    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        
        # Save image
        with open(f"page{page_num + 1}_img{img_index + 1}.png", "wb") as img_file:
            img_file.write(image_bytes)

doc.close()
```

#### Add Annotations and Highlights
```python
import fitz

doc = fitz.open("document.pdf")
page = doc[0]

# Add text annotation
annot = page.add_text_annot((100, 100), "This is a note")

# Add highlight
text_instances = page.search_for("important")
for inst in text_instances:
    highlight = page.add_highlight_annot(inst)

# Save modified PDF
doc.save("annotated.pdf")
doc.close()
```

#### Insert Text or Shapes
```python
import fitz

doc = fitz.open("document.pdf")
page = doc[0]

# Insert text
text = "Watermark - Confidential"
point = fitz.Point(100, 100)
page.insert_text(point, text, fontsize=20, color=(1, 0, 0))  # Red color

# Draw rectangle
rect = fitz.Rect(50, 50, 200, 100)
page.draw_rect(rect, color=(0, 0, 1), width=2)  # Blue border

# Draw circle
point = fitz.Point(300, 300)
page.draw_circle(point, 50, color=(0, 1, 0))  # Green circle

doc.save("modified.pdf")
doc.close()
```

#### Merge PDFs
```python
import fitz

result = fitz.open()

pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]

for pdf_file in pdf_files:
    doc = fitz.open(pdf_file)
    result.insert_pdf(doc)
    doc.close()

result.save("merged_output.pdf")
result.close()
```

#### Get PDF Information
```python
import fitz

doc = fitz.open("document.pdf")

# Metadata
metadata = doc.metadata
print(f"Title: {metadata.get('title')}")
print(f"Author: {metadata.get('author')}")
print(f"Subject: {metadata.get('subject')}")
print(f"Creator: {metadata.get('creator')}")

# Table of Contents
toc = doc.get_toc()
for level, title, page in toc:
    print(f"{'  ' * level}{title} (Page {page})")

doc.close()
```

---

### 4. reportlab - Create PDFs from Scratch

#### Create Simple PDF
```python
from reportlab.pdfgen import canvas

c = canvas.Canvas("hello.pdf")
c.drawString(100, 750, "Hello, World!")
c.drawString(100, 730, "This is a simple PDF created with ReportLab")
c.save()
```

#### Create PDF with Multiple Pages
```python
from reportlab.pdfgen import canvas

c = canvas.Canvas("multi_page.pdf")

# Page 1
c.drawString(100, 750, "Page 1")
c.drawString(100, 700, "This is the first page")
c.showPage()  # Create new page

# Page 2
c.drawString(100, 750, "Page 2")
c.drawString(100, 700, "This is the second page")
c.showPage()

# Page 3
c.drawString(100, 750, "Page 3")
c.drawString(100, 700, "This is the third page")

c.save()
```

#### Add Text with Different Fonts and Sizes
```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

c = canvas.Canvas("styled_text.pdf", pagesize=letter)

# Different font sizes
c.setFont("Helvetica-Bold", 24)
c.drawString(100, 750, "Large Bold Title")

c.setFont("Helvetica", 16)
c.drawString(100, 700, "Medium text")

c.setFont("Helvetica-Oblique", 12)
c.drawString(100, 650, "Italic text")

c.setFont("Courier", 10)
c.drawString(100, 600, "Monospace text")

c.save()
```

#### Draw Shapes and Lines
```python
from reportlab.pdfgen import canvas
from reportlab.lib.colors import red, blue, green

c = canvas.Canvas("shapes.pdf")

# Draw rectangle
c.setStrokeColor(red)
c.setFillColor(blue)
c.rect(100, 700, 200, 100, fill=1)

# Draw circle
c.setStrokeColor(green)
c.circle(300, 600, 50)

# Draw line
c.setStrokeColor(red)
c.line(100, 500, 400, 500)

c.save()
```

#### Add Images to PDF
```python
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

c = canvas.Canvas("image_pdf.pdf")

c.drawString(100, 750, "PDF with Image")

# Add image
c.drawImage("logo.png", 100, 500, width=200, height=100)

c.save()
```

#### Create Table/Grid Layout
```python
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

doc = SimpleDocTemplate("table.pdf", pagesize=letter)
elements = []

# Data for table
data = [
    ['Name', 'Age', 'City'],
    ['John', '25', 'New York'],
    ['Jane', '30', 'Los Angeles'],
    ['Bob', '35', 'Chicago']
]

# Create table
table = Table(data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))

elements.append(table)
doc.build(elements)
```

#### Create PDF with Paragraphs and Styles
```python
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

doc = SimpleDocTemplate("styled_document.pdf", pagesize=letter)
styles = getSampleStyleSheet()
story = []

# Title
title_style = styles['Heading1']
story.append(Paragraph("Document Title", title_style))
story.append(Spacer(1, 0.2 * inch))

# Body text
body_text = """
This is a paragraph with styled text. ReportLab is a powerful library
for creating PDFs programmatically. You can add various elements like
paragraphs, tables, images, and more.
"""
story.append(Paragraph(body_text, styles['Normal']))
story.append(Spacer(1, 0.2 * inch))

# Another section
story.append(Paragraph("Section 2", styles['Heading2']))
story.append(Paragraph("More content here...", styles['Normal']))

doc.build(story)
```

---

## License

MIT License

