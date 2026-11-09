#!/usr/bin/env python3
"""
DataForge: Enterprise-Grade Synthetic Data Generator & Deterministic Obfuscator Tool
Author: AI Collaborator
Version: 1.0.0 (Production Release)
"""

import os
import sys
import csv
import json
import math
import random
import hashlib
import argparse
from datetime import datetime, timedelta

# --- SEED & CORPA DATA FOR DETERMINISTIC SYNTHESIS ---
FIRST_NAMES = ["Amit", "Rahul", "Priyanka", "Sneha", "Vikram", "Rajesh", "Anjali", "Arjun", "Neha", "Vijay", "John", "Emma", "Michael", "Sophia", "David"]
LAST_NAMES = ["Sharma", "Verma", "Gupta", "Kumar", "Singh", "Joshi", "Mehta", "Patel", "Reddy", "Nair", "Smith", "Jones", "Brown", "Davis", "Miller"]
DOMAINS = ["enterprise.local", "securemail.net", "datacore.org", "cloudfirm.io", "globalhub.com"]
DEPARTMENTS = ["Engineering", "Human Resources", "Finance", "CyberSecurity", "Legal", "Product Management", "Operations"]
CITIES = ["Mumbai", "Bengaluru", "Delhi", "San Francisco", "London", "Tokyo", "Berlin", "Sydney"]

class DataForgeEngine:
    def __init__(self):
        self.salt = "DataForgeCryptographySecureSalt2026"

    def _generate_deterministic_hash(self, val: str, length: int = 12) -> str:
        """Generates a unique deterministic string format based on sha256 hashing."""
        hash_obj = hashlib.sha256((str(val) + self.salt).encode('utf-8'))
        hex_digest = hash_obj.hexdigest()
        return hex_digest[:length]

    def mask_value(self, column_name: str, value: str) -> str:
        """Applies targeted obfuscation algorithms preserving semantic structures."""
        if not value or str(value).strip() == "":
            return ""
        
        col_lower = column_name.lower()
        
        # 1. Email Masking (Preserving domain structure for syntax check validation)
        if "@" in value and ("email" in col_lower or "mail" in col_lower):
            parts = value.split("@")
            masked_user = self._generate_deterministic_hash(parts[0], 8)
            return f"{masked_user}@{parts[1]}"
            
        # 2. Numeric / Salary / Financial Masking (Adding bounded variations)
        elif value.isdigit() or ("salary" in col_lower or "amount" in col_lower or "balance" in col_lower):
            try:
                num = float(value)
                # Deterministic shuffle factor between -15% and +15%
                factor = 0.85 + (int(self._generate_deterministic_hash(value, 3), 16) % 31) / 100.0
                return f"{round(num * factor, 2)}"
            except ValueError:
                pass
                
        # 3. Generic Text Masking (Names, Identifiers, PII)
        return "MSK_" + self._generate_deterministic_hash(value, 10).upper()

    def generate_synthetic_data(self, count: int) -> list:
        """Generates high-fidelity mock enterprise records utilizing memory buffers optimized streams."""
        records = []
        start_date = datetime(2020, 1, 1)
        
        print(f"[*] Compiling and generating {count} secure records...", file=sys.stderr)
        
        for i in range(1, count + 1):
            emp_id = f"EMP-{100000 + i}"
            first = random.choice(FIRST_NAMES)
            last = random.choice(LAST_NAMES)
            full_name = f"{first} {last}"
            email = f"{first.lower()}.{last.lower()}@{random.choice(DOMAINS)}"
            phone = f"+91-{random.randint(70000, 99999)}-{random.randint(10000, 99999)}"
            dept = random.choice(DEPARTMENTS)
            city = random.choice(CITIES)
            salary = round(random.uniform(45000, 220000), 2)
            
            # Generate random active joining timestamp
            days_offset = random.randint(0, 2500)
            join_date = (start_date + timedelta(days=days_offset)).strftime("%Y-%m-%d")
            
            records.append({
                "EmployeeID": emp_id,
                "FullName": full_name,
                "Email": email,
                "Phone": phone,
                "Department": dept,
                "Location": city,
                "Salary": str(salary),
                "JoiningDate": join_date
            })
        return records

    def export_data(self, data: list, file_format: str, output_path: str):
        """Streams memory buffer payloads directly into structured serialization configurations."""
        if not data:
            print("[-] Error: Buffer stream empty. Generation lifecycle halted.", file=sys.stderr)
            return

        file_format = file_format.lower()
        print(f"[*] Stream writing file metrics into '{output_path}' via format ({file_format})...", file=sys.stderr)
        
        if file_format == 'csv':
            keys = data[0].keys()
            with open(output_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)
                
        elif file_format == 'json':
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
                
        elif file_format == 'sql':
            table_name = "synthetic_employees"
            keys = data[0].keys()
            columns_str = ", ".join([f"`{k}`" for k in keys])
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"-- DataForge Auto-Generated SQL Stream Injection\n")
                f.write(f"-- Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                for row in data:
                    vals = []
                    for k in keys:
                        escaped_val = str(row[k]).replace("'", "\'")
                        vals.append(f"'{escaped_val}'")
                    vals_str = ", ".join(vals)
                    f.write(f"INSERT INTO `{table_name}` ({columns_str}) VALUES ({vals_str});\n")
        
        print(f"[+] Operational transaction completed. Saved successfully.", file=sys.stderr)

    def obfuscate_file(self, input_path: str, target_cols: list, output_path: str, file_format: str = 'csv'):
        """Reads structural architecture parameters from file system records and masks them dynamically."""
        if not os.path.exists(input_path):
            print(f"[-] Error: Target file path footprint not detected at '{input_path}'", file=sys.stderr)
            sys.exit(1)
            
        print(f"[*] Initializing ingestion pipelines for pipeline file: '{input_path}'", file=sys.stderr)
        obfuscated_records = []
        
        # Currently supporting structured CSV processing pipelines
        with open(input_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            
            if not fieldnames:
                print("[-] Error: Missing header structural schema framework mapping definitions.", file=sys.stderr)
                sys.exit(1)
                
            # Cross-verify targeting tags columns metrics mapping matrix
            valid_targets = [c for c in target_cols if c in fieldnames]
            if not valid_targets:
                print(f"[-] Warning: None of target columns {target_cols} were matched in file columns: {fieldnames}.", file=sys.stderr)
                print("[*] Proceeding with exact duplicate structural cloning operation rules instead.", file=sys.stderr)

            for row in reader:
                new_row = {}
                for col in fieldnames:
                    if col in valid_targets:
                        new_row[col] = self.mask_value(col, row[col])
                    else:
                        new_row[col] = row[col]
                obfuscated_records.append(new_row)
                
        self.export_data(obfuscated_records, file_format, output_path)

def main():
    parser = argparse.ArgumentParser(
        description="DataForge CLI Engine: High-fidelity synthetic record synthesizer and dynamic PII anonymization stack CLI tool.",
        epilog="Enterprise security tool pipeline automation system."
    )
    
    parser.add_argument('--mode', type=str, required=True, choices=['generate', 'obfuscate'], help="Operational workflow execution criteria pattern definition.")
    parser.add_argument('--count', type=int, default=1000, help="Total capacity scaling units targeted inside synthetic generation cycles.")
    parser.add_argument('--format', type=str, default='csv', choices=['csv', 'json', 'sql'], help="Export structural presentation layout mapping logic format setup matrix.")
    parser.add_argument('--output', type=str, help="Destination target filepath location footprint layout rule mapping parameter.")
    parser.add_argument('--input', type=str, help="Path blueprint of production database sample targeted during obfuscation pipelines workflows.")
    parser.add_argument('--cols', type=str, help="Comma-delimited targeting matrix fields definitions designated for structural token masking masking configurations.")

    args = parser.parse_args()
    engine = DataForgeEngine()
    
    # Establish dynamic defaults for targets if none provided
    out_file = args.output if args.output else f"output.{args.format}"

    if args.mode == 'generate':
        synthetic_pool = engine.generate_synthetic_data(args.count)
        engine.export_data(synthetic_pool, args.format, out_file)
        
    elif args.mode == 'obfuscate':
        if not args.input:
            print("[-] Structural Syntax Error: Obfuscation criteria routines require fully explicit '--input' tracking routes parameter definitions.", file=sys.stderr)
            sys.exit(1)
        if not args.cols:
            print("[-] Structural Syntax Error: Targeted pipeline transformations require explicit target column strings mappings via '--cols'.", file=sys.stderr)
            sys.exit(1)
            
        target_columns = [c.strip() for c in args.cols.split(",")]
        engine.obfuscate_file(args.input, target_columns, out_file, args.format)

if __name__ == '__main__':
    main()