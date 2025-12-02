"""
Example usage of the PDFSplitter class
"""

from pdf_splitter import PDFSplitter
import os


def example_split_into_two():
    """Example: Split a PDF into two pieces"""
    print("\n" + "="*60)
    print("Example 1: Split PDF into Two Pieces")
    print("="*60)
    
    # Replace with your actual PDF path
    pdf_path = "sample.pdf"
    
    if not os.path.exists(pdf_path):
        print(f"⚠ Please provide a valid PDF path. '{pdf_path}' not found.")
        return
    
    # Initialize the splitter
    splitter = PDFSplitter(pdf_path)
    print(f"Total pages in PDF: {splitter.get_total_pages()}")
    
    # Option 1: Split at the middle (default)
    print("\n→ Splitting at the middle...")
    part1, part2 = splitter.split_into_two()
    
    # Option 2: Split at a specific page
    # print("\n→ Splitting at page 5...")
    # part1, part2 = splitter.split_into_two(split_at_page=5)
    
    # Option 3: Split and save to a specific directory
    # print("\n→ Splitting and saving to 'output' directory...")
    # part1, part2 = splitter.split_into_two(split_at_page=10, output_dir="output")


def example_split_into_n_parts():
    """Example: Split a PDF into N equal parts"""
    print("\n" + "="*60)
    print("Example 2: Split PDF into N Parts")
    print("="*60)
    
    pdf_path = "sample.pdf"
    
    if not os.path.exists(pdf_path):
        print(f"⚠ Please provide a valid PDF path. '{pdf_path}' not found.")
        return
    
    splitter = PDFSplitter(pdf_path)
    print(f"Total pages in PDF: {splitter.get_total_pages()}")
    
    # Split into 3 parts
    print("\n→ Splitting into 3 equal parts...")
    parts = splitter.split_into_n_parts(n_parts=3)


def example_split_by_ranges():
    """Example: Split PDF by specific page ranges"""
    print("\n" + "="*60)
    print("Example 3: Split PDF by Custom Page Ranges")
    print("="*60)
    
    pdf_path = "sample.pdf"
    
    if not os.path.exists(pdf_path):
        print(f"⚠ Please provide a valid PDF path. '{pdf_path}' not found.")
        return
    
    splitter = PDFSplitter(pdf_path)
    print(f"Total pages in PDF: {splitter.get_total_pages()}")
    
    # Define custom page ranges (1-based, inclusive)
    print("\n→ Splitting by custom ranges: (1-5), (6-10), (11-15)...")
    ranges = [(1, 5), (6, 10), (11, 15)]
    parts = splitter.split_by_ranges(ranges)


def example_extract_specific_pages():
    """Example: Extract specific pages"""
    print("\n" + "="*60)
    print("Example 4: Extract Specific Pages")
    print("="*60)
    
    pdf_path = "sample.pdf"
    
    if not os.path.exists(pdf_path):
        print(f"⚠ Please provide a valid PDF path. '{pdf_path}' not found.")
        return
    
    splitter = PDFSplitter(pdf_path)
    print(f"Total pages in PDF: {splitter.get_total_pages()}")
    
    # Extract pages 1, 3, 5, 7
    print("\n→ Extracting pages 1, 3, 5, 7...")
    output = splitter.extract_pages([1, 3, 5, 7])


if __name__ == "__main__":
    print("\n🔧 PDF Splitter - Example Usage")
    print("="*60)
    print("Before running, please update 'pdf_path' with your actual PDF file.")
    print("="*60)
    
    # Run the examples
    # Uncomment the ones you want to test
    
    example_split_into_two()
    # example_split_into_n_parts()
    # example_split_by_ranges()
    # example_extract_specific_pages()
    
    print("\n" + "="*60)
    print("✓ Examples complete!")
    print("="*60 + "\n")

