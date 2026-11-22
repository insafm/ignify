#!/usr/bin/env python3
"""
combine_pdf.py
Combines IGNOU Previous Question Paper (PQP) PDFs in chronological or reverse-chronological order.
Supports pdfunite and ghostscript backends.
"""

import os
import sys
import re
import argparse
import subprocess

def parse_session(filename):
    """
    Extracts (year, month_num) from standard filename pattern like 'BCS-040_June_2023.pdf'
    or 'BCS-040_Dec_2024.pdf'.
    Returns a sortable tuple: (year, month_num, set_num).
    """
    basename = os.path.basename(filename)
    m = re.search(r'_(June|Dec(?:ember)?)[_](\d{4})(?:_Set-(\d+))?\.pdf', basename, re.IGNORECASE)
    if m:
        month_str = m.group(1).lower()
        month_num = 6 if 'jun' in month_str else 12
        year = int(m.group(2))
        set_num = int(m.group(3)) if m.group(3) else 1
        return (year, month_num, set_num)
    return (9999, 12, 1)

def combine_pdfs(input_dir, output_path=None, order="asc"):
    if not os.path.isdir(input_dir):
        print(f"Error: Directory not found: {input_dir}", file=sys.stderr)
        sys.exit(1)

    # Collect matching PDFs (exclude symlinks and previous combined outputs)
    pdf_files = []
    course_code = None

    for fname in os.listdir(input_dir):
        fpath = os.path.join(input_dir, fname)
        if not fname.endswith(".pdf") or os.path.islink(fpath):
            continue
        if "combined" in fname.lower() or "all_papers" in fname.lower():
            continue

        # Extract course code prefix e.g. BCS-040
        if not course_code and "_" in fname:
            course_code = fname.split("_")[0]

        pdf_files.append(fpath)

    if not pdf_files:
        print(f"No previous question paper PDFs found in {input_dir}", file=sys.stderr)
        sys.exit(1)

    # Sort files by session date
    reverse = (order.lower() == "desc")
    pdf_files.sort(key=parse_session, reverse=reverse)

    first_session = parse_session(pdf_files[0])
    last_session = parse_session(pdf_files[-1])
    min_year = min(first_session[0], last_session[0])
    max_year = max(first_session[0], last_session[0])

    if not output_path:
        code = course_code or "PQP"
        output_name = f"{code}_Combined_{min_year}-{max_year}.pdf"
        output_path = os.path.join(input_dir, output_name)

    print(f"Found {len(pdf_files)} paper PDFs to merge ({order.upper()} order):")
    for idx, f in enumerate(pdf_files, 1):
        sess = parse_session(f)
        sess_str = f"{'June' if sess[1] == 6 else 'Dec'} {sess[0]}"
        print(f"  {idx:2d}. {os.path.basename(f):30} [{sess_str}]")

    print(f"\nMerging into: {output_path}...")

    # Check for pdfunite
    has_pdfunite = subprocess.run(["which", "pdfunite"], capture_output=True).returncode == 0
    has_gs = subprocess.run(["which", "gs"], capture_output=True).returncode == 0

    if has_pdfunite:
        cmd = ["pdfunite"] + pdf_files + [output_path]
        res = subprocess.run(cmd)
        if res.returncode != 0:
            print("pdfunite failed, falling back to ghostscript...", file=sys.stderr)
        else:
            size_mb = os.path.getsize(output_path) / (1024 * 1024)
            print(f"SUCCESS: Created combined PDF using pdfunite ({size_mb:.2f} MB)")
            return output_path

    if has_gs:
        cmd = [
            "gs", "-dBATCH", "-dNOPAUSE", "-q",
            "-sDEVICE=pdfwrite",
            f"-sOutputFile={output_path}"
        ] + pdf_files
        res = subprocess.run(cmd)
        if res.returncode == 0:
            size_mb = os.path.getsize(output_path) / (1024 * 1024)
            print(f"SUCCESS: Created combined PDF using ghostscript ({size_mb:.2f} MB)")
            return output_path
        else:
            print(f"ghostscript failed with code {res.returncode}", file=sys.stderr)
            sys.exit(1)

    print("Error: Neither pdfunite nor ghostscript found on system.", file=sys.stderr)
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Combine IGNOU Previous Question Paper PDFs into one document.")
    parser.add_argument("--dir", default="bca_new/bcs040/pqp", help="Directory containing PQP PDFs (default: bca_new/bcs040/pqp)")
    parser.add_argument("--out", default=None, help="Output PDF file path (optional)")
    parser.add_argument("--order", choices=["asc", "desc"], default="asc", help="Order: asc (oldest first: 2013->2026) or desc (newest first: 2026->2013)")

    args = parser.parse_args()
    combine_pdfs(args.dir, args.out, args.order)

if __name__ == "__main__":
    main()

