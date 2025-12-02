# 🎬 Interactive PDF Splitter Demo

## Visual Walkthrough

Here's what you'll see when you run the interactive splitter:

### 1. Welcome Screen
```
======================================================================
                      📄 Interactive PDF Splitter
======================================================================

📂 Enter the PDF file path:
   (You can drag and drop the file here, or type the path)
   → 
```

### 2. PDF Loaded Successfully
```
✅ PDF loaded successfully!
   📄 File: document.pdf
   📖 Total pages: 50

🔧 Choose a split option:
   1. Split into TWO parts (at middle)
   2. Split into TWO parts (at specific page)
   3. Split into N equal parts
   4. Split by custom page ranges
   5. Extract specific pages
   0. Exit
----------------------------------------------------------------------
   Your choice: 
```

### 3. Example: Split into Two Parts
```
   Your choice: 2

📖 Total pages in PDF: 50
   Enter page number to split at (1-49): 25

📁 Output directory:
   1. Same as input file (default)
   2. Specify custom directory
   → 1

✂️  Splitting into two parts at page 25...

✓ Split complete!
  Part 1: /path/to/document_part1.pdf (Pages 1-25)
  Part 2: /path/to/document_part2.pdf (Pages 26-50)

✅ Success! Created:
   📄 /path/to/document_part1.pdf
   📄 /path/to/document_part2.pdf
```

### 4. Continue or Exit
```
======================================================================

Perform another operation on this PDF? (y/n): y

🔧 Choose a split option:
   1. Split into TWO parts (at middle)
   2. Split into TWO parts (at specific page)
   3. Split into N equal parts
   4. Split by custom page ranges
   5. Extract specific pages
   0. Exit
----------------------------------------------------------------------
```

---

## 🎮 Try These Examples

### Example 1: Quick Split at Middle
```bash
./run_splitter.sh

# Then follow prompts:
1. Enter PDF path: ~/Documents/my_document.pdf
2. Choose option: 1 (split at middle)
3. Choose output: 1 (same directory)
```

### Example 2: Extract Specific Pages
```bash
./run_splitter.sh

# Then follow prompts:
1. Enter PDF path: ~/Documents/report.pdf
2. Choose option: 5 (extract specific pages)
3. Enter pages: 1, 5, 10, 15, 20
4. Enter output name: important_pages.pdf
```

### Example 3: Split into 3 Parts
```bash
./run_splitter.sh

# Then follow prompts:
1. Enter PDF path: ~/Documents/long_book.pdf
2. Choose option: 3 (split into N parts)
3. Enter number: 3
4. Choose output: 1
```

---

## 🎨 Features Showcase

### ✅ Smart File Detection
```
📂 Enter the PDF file path:
   → /path/to/file.txt

   ⚠️  Warning: This doesn't appear to be a PDF file!
   Continue anyway? (y/n): 
```

### ✅ Error Handling
```
📂 Enter the PDF file path:
   → /nonexistent/file.pdf

   ❌ File not found: /nonexistent/file.pdf
   Try again? (y/n): 
```

### ✅ Input Validation
```
📖 Total pages in PDF: 50
   Enter page number to split at (1-49): 75

   ❌ Page must be between 1 and 49
   Enter page number to split at (1-49): 
```

### ✅ Directory Creation
```
📁 Output directory:
   2. Specify custom directory
   → 2
   Enter output directory path: ~/Documents/split_pdfs

   Directory doesn't exist. Create it? (y/n): y
   ✅ Directory created!
```

---

## 🔥 Pro Tips

1. **Drag & Drop**: On macOS, drag the PDF file directly into the terminal window instead of typing the path

2. **Quick Exit**: Press `Ctrl+C` at any time to exit immediately

3. **Batch Processing**: After splitting, choose 'y' to perform another operation on the same PDF

4. **Custom Names**: When extracting pages, you can specify a custom output filename

5. **Relative Paths**: Use `~` for home directory: `~/Documents/file.pdf`

---

## 🎯 Common Use Cases

### Use Case 1: Split Large Document for Email
If you have a 100-page PDF that's too large to email:
- Choose option 3 (split into N parts)
- Enter 4 or 5 parts
- Send each part separately

### Use Case 2: Extract Important Pages
From a report, extract only summary pages:
- Choose option 5 (extract specific pages)
- Enter page numbers: 1, 2, 15, 20
- Save as "summary.pdf"

### Use Case 3: Separate Sections
Document with intro (10 pages) and content:
- Choose option 2 (split at specific page)
- Enter page 10
- Get intro_part1.pdf and content_part2.pdf

---

## 🚀 Ready to Try?

Run this command now:
```bash
cd /Users/shakil/Development/OWN/python-scripts/PDF_UTILS && ./run_splitter.sh
```

Or read `GETTING_STARTED.md` for more detailed instructions!

---

Enjoy your new interactive PDF splitter! 🎉

