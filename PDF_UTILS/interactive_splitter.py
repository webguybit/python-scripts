#!/usr/bin/env python3
"""
Interactive PDF Splitter - Command Line Interface
A user-friendly CLI tool for splitting PDFs with interactive prompts
"""

import os
import sys
from pdf_splitter import PDFSplitter


def print_header():
    """Print a nice header"""
    print("\n" + "="*70)
    print("📄 Interactive PDF Splitter".center(70))
    print("="*70 + "\n")


def print_separator():
    """Print a separator line"""
    print("-" * 70)


def get_pdf_path():
    """Get and validate PDF file path from user"""
    while True:
        print("\n📂 Enter the PDF file path:")
        print("   (You can drag and drop the file here, or type the path)")
        pdf_path = input("   → ").strip().strip("'\"")  # Remove quotes if drag-dropped
        
        if not pdf_path:
            print("   ❌ Please enter a valid path!")
            continue
        
        # Expand user path if needed
        pdf_path = os.path.expanduser(pdf_path)
        
        if not os.path.exists(pdf_path):
            print(f"   ❌ File not found: {pdf_path}")
            retry = input("   Try again? (y/n): ").strip().lower()
            if retry != 'y':
                return None
            continue
        
        if not pdf_path.lower().endswith('.pdf'):
            print("   ⚠️  Warning: This doesn't appear to be a PDF file!")
            confirm = input("   Continue anyway? (y/n): ").strip().lower()
            if confirm != 'y':
                continue
        
        return pdf_path


def display_split_options():
    """Display available split options"""
    print("\n🔧 Choose a split option:")
    print("   1. Split into TWO parts (at middle)")
    print("   2. Split into TWO parts (at specific page)")
    print("   3. Split into N equal parts")
    print("   4. Split by custom page ranges")
    print("   5. Extract specific pages")
    print("   0. Exit")
    print_separator()


def get_output_directory():
    """Get output directory from user"""
    print("\n📁 Output directory:")
    print("   1. Same as input file (default)")
    print("   2. Specify custom directory")
    
    choice = input("   → ").strip()
    
    if choice == '2':
        output_dir = input("   Enter output directory path: ").strip().strip("'\"")
        output_dir = os.path.expanduser(output_dir)
        
        if not os.path.exists(output_dir):
            create = input(f"   Directory doesn't exist. Create it? (y/n): ").strip().lower()
            if create == 'y':
                os.makedirs(output_dir, exist_ok=True)
                return output_dir
            else:
                return None
        return output_dir
    
    return None


def split_into_two_middle(splitter):
    """Split PDF into two parts at the middle"""
    print(f"\n✂️  Splitting into two parts at the middle (page {splitter.total_pages // 2})...")
    
    output_dir = get_output_directory()
    if output_dir is False:  # User cancelled
        return
    
    try:
        part1, part2 = splitter.split_into_two(output_dir=output_dir)
        print("\n✅ Success! Created:")
        print(f"   📄 {part1}")
        print(f"   📄 {part2}")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


def split_into_two_custom(splitter):
    """Split PDF into two parts at specific page"""
    print(f"\n📖 Total pages in PDF: {splitter.total_pages}")
    
    while True:
        try:
            split_page = input(f"   Enter page number to split at (1-{splitter.total_pages - 1}): ").strip()
            split_page = int(split_page)
            
            if split_page < 1 or split_page >= splitter.total_pages:
                print(f"   ❌ Page must be between 1 and {splitter.total_pages - 1}")
                continue
            
            break
        except ValueError:
            print("   ❌ Please enter a valid number!")
    
    output_dir = get_output_directory()
    if output_dir is False:
        return
    
    try:
        part1, part2 = splitter.split_into_two(split_at_page=split_page, output_dir=output_dir)
        print("\n✅ Success! Created:")
        print(f"   📄 {part1}")
        print(f"   📄 {part2}")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


def split_into_n_parts(splitter):
    """Split PDF into N equal parts"""
    print(f"\n📖 Total pages in PDF: {splitter.total_pages}")
    
    while True:
        try:
            n_parts = input(f"   How many parts? (2-{splitter.total_pages}): ").strip()
            n_parts = int(n_parts)
            
            if n_parts < 2 or n_parts > splitter.total_pages:
                print(f"   ❌ Number of parts must be between 2 and {splitter.total_pages}")
                continue
            
            break
        except ValueError:
            print("   ❌ Please enter a valid number!")
    
    output_dir = get_output_directory()
    if output_dir is False:
        return
    
    try:
        parts = splitter.split_into_n_parts(n_parts=n_parts, output_dir=output_dir)
        print(f"\n✅ Success! Created {len(parts)} files")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


def split_by_ranges(splitter):
    """Split PDF by custom page ranges"""
    print(f"\n📖 Total pages in PDF: {splitter.total_pages}")
    print("\nEnter page ranges (e.g., '1-5, 6-10, 11-20')")
    print("Or enter them one by one (press Enter after each range, empty line to finish)")
    
    ranges = []
    print("\nOption 1 - Enter all at once (e.g., '1-5, 6-10, 11-20'):")
    all_ranges = input("   → ").strip()
    
    if all_ranges:
        # Parse comma-separated ranges
        try:
            for range_str in all_ranges.split(','):
                range_str = range_str.strip()
                if '-' in range_str:
                    start, end = map(int, range_str.split('-'))
                    ranges.append((start, end))
        except ValueError:
            print("   ❌ Invalid format! Please use format like '1-5, 6-10'")
            return
    else:
        # Get ranges one by one
        print("\nOption 2 - Enter one by one:")
        while True:
            range_str = input(f"   Range {len(ranges) + 1} (e.g., '1-10', or press Enter to finish): ").strip()
            if not range_str:
                break
            
            try:
                if '-' in range_str:
                    start, end = map(int, range_str.split('-'))
                    ranges.append((start, end))
                else:
                    print("   ❌ Use format like '1-10'")
            except ValueError:
                print("   ❌ Invalid format!")
    
    if not ranges:
        print("   ❌ No ranges specified!")
        return
    
    print(f"\n✂️  Will create {len(ranges)} files with ranges:")
    for i, (start, end) in enumerate(ranges):
        print(f"   {i+1}. Pages {start}-{end}")
    
    confirm = input("\n   Continue? (y/n): ").strip().lower()
    if confirm != 'y':
        return
    
    output_dir = get_output_directory()
    if output_dir is False:
        return
    
    try:
        parts = splitter.split_by_ranges(page_ranges=ranges, output_dir=output_dir)
        print(f"\n✅ Success! Created {len(parts)} files")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


def extract_specific_pages(splitter):
    """Extract specific pages"""
    print(f"\n📖 Total pages in PDF: {splitter.total_pages}")
    print("\nEnter page numbers to extract:")
    print("   Examples: '1,3,5,7' or '1, 3, 5, 7'")
    
    pages_str = input("   → ").strip()
    
    try:
        pages = [int(p.strip()) for p in pages_str.split(',')]
    except ValueError:
        print("   ❌ Invalid format! Please use comma-separated numbers like '1,3,5'")
        return
    
    # Validate pages
    invalid_pages = [p for p in pages if p < 1 or p > splitter.total_pages]
    if invalid_pages:
        print(f"   ❌ Invalid page numbers: {invalid_pages}")
        return
    
    print(f"\n✂️  Will extract {len(pages)} pages: {pages}")
    
    output_file = input("\n   Output filename (press Enter for default): ").strip()
    if not output_file:
        output_file = None
    
    try:
        output = splitter.extract_pages(pages=pages, output_file=output_file)
        print(f"\n✅ Success!")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


def main():
    """Main interactive loop"""
    print_header()
    
    # Get PDF file
    pdf_path = get_pdf_path()
    if not pdf_path:
        print("\n👋 Goodbye!")
        return
    
    # Initialize splitter
    try:
        splitter = PDFSplitter(pdf_path)
        print(f"\n✅ PDF loaded successfully!")
        print(f"   📄 File: {os.path.basename(pdf_path)}")
        print(f"   📖 Total pages: {splitter.total_pages}")
    except Exception as e:
        print(f"\n❌ Error loading PDF: {str(e)}")
        return
    
    # Main loop
    while True:
        display_split_options()
        
        choice = input("   Your choice: ").strip()
        
        if choice == '0':
            print("\n👋 Goodbye!")
            break
        elif choice == '1':
            split_into_two_middle(splitter)
        elif choice == '2':
            split_into_two_custom(splitter)
        elif choice == '3':
            split_into_n_parts(splitter)
        elif choice == '4':
            split_by_ranges(splitter)
        elif choice == '5':
            extract_specific_pages(splitter)
        else:
            print("   ❌ Invalid choice! Please enter 0-5")
        
        if choice != '0':
            print("\n" + "="*70)
            another = input("\nPerform another operation on this PDF? (y/n): ").strip().lower()
            if another != 'y':
                print("\n👋 Goodbye!")
                break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        sys.exit(1)

