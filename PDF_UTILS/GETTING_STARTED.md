# Getting Started with Interactive PDF Splitter

## 🚀 Quick Start (3 Easy Steps)

### Step 1: Navigate to the PDF_UTILS directory
```bash
cd /Users/shakil/Development/OWN/python-scripts/PDF_UTILS
```

### Step 2: Run the interactive splitter
```bash
./run_splitter.sh
```

### Step 3: Follow the prompts!
The tool will guide you through:
- Selecting your PDF file
- Choosing how to split it
- Specifying output location

That's it! 🎉

---

## 📖 Detailed Usage Examples

### Example 1: Split a PDF at the Middle

```
📄 Interactive PDF Splitter

📂 Enter the PDF file path:
   → ~/Documents/report.pdf

✅ PDF loaded successfully!
   📄 File: report.pdf
   📖 Total pages: 20

🔧 Choose a split option:
   1. Split into TWO parts (at middle)
   → 1

📁 Output directory:
   1. Same as input file (default)
   → 1

✂️  Splitting into two parts at the middle (page 10)...

✅ Success! Created:
   📄 /Users/shakil/Documents/report_part1.pdf
   📄 /Users/shakil/Documents/report_part2.pdf
```

### Example 2: Split at Specific Page

```
🔧 Choose a split option:
   2. Split into TWO parts (at specific page)
   → 2

📖 Total pages in PDF: 50
   Enter page number to split at (1-49): 25

✅ Success! Created:
   📄 document_part1.pdf (Pages 1-25)
   📄 document_part2.pdf (Pages 26-50)
```

### Example 3: Split into Multiple Parts

```
🔧 Choose a split option:
   3. Split into N equal parts
   → 3

📖 Total pages in PDF: 30
   How many parts? (2-30): 3

✅ Success! Created 3 files
   Part 1: document_part1.pdf (Pages 1-10)
   Part 2: document_part2.pdf (Pages 11-20)
   Part 3: document_part3.pdf (Pages 21-30)
```

### Example 4: Extract Specific Pages

```
🔧 Choose a split option:
   5. Extract specific pages
   → 5

📖 Total pages in PDF: 100
Enter page numbers to extract:
   Examples: '1,3,5,7' or '1, 3, 5, 7'
   → 1, 5, 10, 15, 20

✂️  Will extract 5 pages: [1, 5, 10, 15, 20]

   Output filename (press Enter for default): important_pages.pdf

✅ Success!
   📄 important_pages.pdf
```

---

## 💡 Tips & Tricks

### Drag and Drop Support (macOS/Linux)
Instead of typing the file path, you can drag the PDF file from Finder directly into the terminal window!

```
📂 Enter the PDF file path:
   → [Drag file here]
```

### Custom Output Directory
When asked for output directory:
- Press `1` or just Enter to save in the same folder as input
- Press `2` to specify a custom folder (will be created if it doesn't exist)

### Multiple Operations
After each operation, you'll be asked:
```
Perform another operation on this PDF? (y/n):
```
- Type `y` to do more operations on the same PDF
- Type `n` to exit

### Keyboard Shortcuts
- Press `Ctrl+C` to cancel at any time
- Type `0` in the main menu to exit

---

## 🐛 Troubleshooting

### "Virtual environment not found"
Make sure you're in the project root and the `env` folder exists:
```bash
ls -la /Users/shakil/Development/OWN/python-scripts/env
```

### "File not found"
- Make sure the PDF path is correct
- Use absolute paths or relative paths from the current directory
- Remove any quotes around the path if copying from somewhere

### "Permission denied"
Make the script executable:
```bash
chmod +x /Users/shakil/Development/OWN/python-scripts/PDF_UTILS/run_splitter.sh
chmod +x /Users/shakil/Development/OWN/python-scripts/PDF_UTILS/interactive_splitter.py
```

---

## 📝 Manual Usage (Without Script)

If you prefer to run it manually:

```bash
# Navigate to project root
cd /Users/shakil/Development/OWN/python-scripts

# Activate virtual environment
source env/bin/activate

# Navigate to PDF_UTILS
cd PDF_UTILS

# Run the interactive splitter
python interactive_splitter.py

# When done, deactivate
deactivate
```

---

## 🎓 Next Steps

- Check out `example_usage.py` for programmatic usage
- Read `README.md` for comprehensive documentation
- Explore other PDF packages (pdfplumber, PyMuPDF, reportlab)

---

## 📞 Need Help?

The interactive tool includes:
- ✅ Input validation
- ✅ Error messages with suggestions
- ✅ Confirmation prompts for destructive actions
- ✅ Clear success/failure indicators

Just follow the prompts and the tool will guide you! 🎉

