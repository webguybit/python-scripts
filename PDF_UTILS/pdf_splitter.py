"""
PDF Splitter Module
A utility class for splitting PDF files into multiple pieces
"""

import os
from PyPDF2 import PdfReader, PdfWriter
from typing import Optional, List, Tuple


class PDFSplitter:
    """
    A class to split PDF files into multiple pieces based on various options.
    
    Attributes:
        pdf_path (str): Path to the input PDF file
        reader (PdfReader): PyPDF2 reader object
        total_pages (int): Total number of pages in the PDF
    """
    
    def __init__(self, pdf_path: str):
        """
        Initialize the PDFSplitter with a PDF file.
        
        Args:
            pdf_path (str): Path to the PDF file to be split
            
        Raises:
            FileNotFoundError: If the PDF file doesn't exist
            Exception: If the file is not a valid PDF
        """
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        self.pdf_path = pdf_path
        try:
            self.reader = PdfReader(pdf_path)
            self.total_pages = len(self.reader.pages)
        except Exception as e:
            raise Exception(f"Error reading PDF file: {str(e)}")
    
    def get_total_pages(self) -> int:
        """
        Get the total number of pages in the PDF.
        
        Returns:
            int: Total number of pages
        """
        return self.total_pages
    
    def split_into_two(self, split_at_page: Optional[int] = None, 
                       output_dir: Optional[str] = None) -> Tuple[str, str]:
        """
        Split the PDF into two pieces.
        
        Args:
            split_at_page (int, optional): Page number to split at (1-based index).
                                          If None, splits at the middle.
            output_dir (str, optional): Directory to save output files.
                                       If None, uses the same directory as input.
        
        Returns:
            Tuple[str, str]: Paths to the two output PDF files
        
        Example:
            splitter = PDFSplitter("document.pdf")
            part1, part2 = splitter.split_into_two(split_at_page=5)
        """
        # Determine split point
        if split_at_page is None:
            split_at_page = self.total_pages // 2
        else:
            if split_at_page < 1 or split_at_page >= self.total_pages:
                raise ValueError(f"split_at_page must be between 1 and {self.total_pages - 1}")
        
        # Determine output directory
        if output_dir is None:
            output_dir = os.path.dirname(self.pdf_path)
        else:
            os.makedirs(output_dir, exist_ok=True)
        
        # Get base filename
        base_name = os.path.splitext(os.path.basename(self.pdf_path))[0]
        
        # Create output file paths
        output_file1 = os.path.join(output_dir, f"{base_name}_part1.pdf")
        output_file2 = os.path.join(output_dir, f"{base_name}_part2.pdf")
        
        # Create first part (pages 0 to split_at_page-1)
        writer1 = PdfWriter()
        for i in range(split_at_page):
            writer1.add_page(self.reader.pages[i])
        
        with open(output_file1, 'wb') as f:
            writer1.write(f)
        
        # Create second part (pages split_at_page to end)
        writer2 = PdfWriter()
        for i in range(split_at_page, self.total_pages):
            writer2.add_page(self.reader.pages[i])
        
        with open(output_file2, 'wb') as f:
            writer2.write(f)
        
        print(f"✓ Split complete!")
        print(f"  Part 1: {output_file1} (Pages 1-{split_at_page})")
        print(f"  Part 2: {output_file2} (Pages {split_at_page + 1}-{self.total_pages})")
        
        return output_file1, output_file2
    
    def split_into_n_parts(self, n_parts: int, 
                          output_dir: Optional[str] = None) -> List[str]:
        """
        Split the PDF into N equal (or nearly equal) parts.
        
        Args:
            n_parts (int): Number of parts to split the PDF into
            output_dir (str, optional): Directory to save output files
        
        Returns:
            List[str]: List of paths to the output PDF files
        """
        if n_parts < 2:
            raise ValueError("n_parts must be at least 2")
        
        if n_parts > self.total_pages:
            raise ValueError(f"Cannot split {self.total_pages} pages into {n_parts} parts")
        
        # Determine output directory
        if output_dir is None:
            output_dir = os.path.dirname(self.pdf_path)
        else:
            os.makedirs(output_dir, exist_ok=True)
        
        # Get base filename
        base_name = os.path.splitext(os.path.basename(self.pdf_path))[0]
        
        # Calculate pages per part
        pages_per_part = self.total_pages // n_parts
        remainder = self.total_pages % n_parts
        
        output_files = []
        current_page = 0
        
        for part_num in range(n_parts):
            # Add one extra page to first 'remainder' parts
            pages_in_this_part = pages_per_part + (1 if part_num < remainder else 0)
            
            # Create writer for this part
            writer = PdfWriter()
            for i in range(current_page, current_page + pages_in_this_part):
                writer.add_page(self.reader.pages[i])
            
            # Save this part
            output_file = os.path.join(output_dir, f"{base_name}_part{part_num + 1}.pdf")
            with open(output_file, 'wb') as f:
                writer.write(f)
            
            output_files.append(output_file)
            print(f"  Part {part_num + 1}: {output_file} (Pages {current_page + 1}-{current_page + pages_in_this_part})")
            
            current_page += pages_in_this_part
        
        print(f"✓ Split into {n_parts} parts complete!")
        return output_files
    
    def split_by_ranges(self, page_ranges: List[Tuple[int, int]], 
                       output_dir: Optional[str] = None) -> List[str]:
        """
        Split the PDF by specific page ranges.
        
        Args:
            page_ranges (List[Tuple[int, int]]): List of (start, end) page tuples (1-based, inclusive)
            output_dir (str, optional): Directory to save output files
        
        Returns:
            List[str]: List of paths to the output PDF files
        
        Example:
            splitter.split_by_ranges([(1, 5), (6, 10), (11, 20)])
        """
        # Determine output directory
        if output_dir is None:
            output_dir = os.path.dirname(self.pdf_path)
        else:
            os.makedirs(output_dir, exist_ok=True)
        
        # Get base filename
        base_name = os.path.splitext(os.path.basename(self.pdf_path))[0]
        
        output_files = []
        
        for idx, (start, end) in enumerate(page_ranges):
            # Validate range
            if start < 1 or end > self.total_pages or start > end:
                raise ValueError(f"Invalid page range: ({start}, {end})")
            
            # Create writer for this range
            writer = PdfWriter()
            for i in range(start - 1, end):  # Convert to 0-based index
                writer.add_page(self.reader.pages[i])
            
            # Save this part
            output_file = os.path.join(output_dir, f"{base_name}_pages{start}-{end}.pdf")
            with open(output_file, 'wb') as f:
                writer.write(f)
            
            output_files.append(output_file)
            print(f"  Range {idx + 1}: {output_file} (Pages {start}-{end})")
        
        print(f"✓ Split by ranges complete!")
        return output_files
    
    def extract_pages(self, pages: List[int], 
                     output_file: Optional[str] = None) -> str:
        """
        Extract specific pages into a new PDF.
        
        Args:
            pages (List[int]): List of page numbers to extract (1-based)
            output_file (str, optional): Output file path
        
        Returns:
            str: Path to the output PDF file
        """
        # Validate pages
        for page in pages:
            if page < 1 or page > self.total_pages:
                raise ValueError(f"Invalid page number: {page}")
        
        # Determine output file
        if output_file is None:
            base_name = os.path.splitext(os.path.basename(self.pdf_path))[0]
            output_dir = os.path.dirname(self.pdf_path)
            output_file = os.path.join(output_dir, f"{base_name}_extracted.pdf")
        
        # Create writer
        writer = PdfWriter()
        for page_num in pages:
            writer.add_page(self.reader.pages[page_num - 1])  # Convert to 0-based
        
        # Save
        with open(output_file, 'wb') as f:
            writer.write(f)
        
        print(f"✓ Extracted {len(pages)} pages to: {output_file}")
        return output_file

