# DataForge: Synthetic Data Generator & File Obfuscator Tool

**DataForge** is a production-grade, enterprise-ready Python CLI utility designed for developers, QA engineers, and data privacy officers. It serves a dual unique purpose: 
1. **Synthetic Data Generation**: Creates structurally sound, massive datasets (CSV, JSON, SQL) mimicking real-world patterns without using real user info.
2. **Deterministic Data Obfuscation (Masking)**: Safely anonymizes existing sensitive structural files using cryptographically secure tokenization methods, preserving data formats for testing environments.

## 🚀 Key Features

- **High-Performance Synthesis**: Generates millions of rows of mock profiles (Names, Emails, UUIDs, Phonenumber, IP addresses, Financials) leveraging vectorized operations.
- **Advanced Obfuscation Engine**: Multi-column text and numeric masking rules using SHA-256 seed-based salts ensuring deterministic mapping (same input -> same anonymous output).
- **Format Preservation**: Retains string layouts (e.g., matching email domains or specific prefix formats) during masking.
- **Export Control**: Direct structural streaming output into custom JSON arrays, flattened CSVs, or raw database-injectable `.sql` insert streams.
- **Zero Heavy Dependencies**: Built entirely using native Python libraries (`json`, `csv`, `hashlib`, `random`, `argparse`, `os`) to maximize portability and deployment simplicity.

---

## 🛠️ Installation & Setup

No complex system configurations or heavy virtual environments are required.

```bash
# Clone the repository
git clone https://github.com/your-username/dataforge-tool.git
cd dataforge-tool

# Verify your Python version (Requires Python 3.8+)
python --version
```

---

## 💻 Usage Instructions

The utility executes through an interactive and powerful command-line interface.

### 1. Generating Mock Datasets
Generate fake enterprise logs or user profile metrics dynamically:
```bash
python dataforge.py --mode generate --count 50000 --format csv --output mock_users.csv
```

### 2. Obfuscating Sensitive Data
Mask an existing production sample seamlessly:
```bash
python dataforge.py --mode obfuscate --input local_sensitive_data.csv --cols email,phone,salary --output masked_data.csv
```

### Supported Arguments Reference
| Argument | Description | Default |
|---|---|---|
| `--mode` | The operation to perform (`generate` or `obfuscate`). | **Required** |
| `--count` | Number of data rows to generate. | `1000` |
| `--format` | Output file structure format (`csv`, `json`, `sql`). | `csv` |
| `--output` | Destination path for the produced file output. | `output.[format]` |
| `--input` | Source file pathway when executing masking/obfuscation. | `None` |
| `--cols` | Comma-separated listing of column names targeted for masking. | `None` |

---

## 📁 Repository Blueprint
```text
dataforge-tool/
│
├── dataforge.py      # Core CLI Utility engine & structural algorithms
└── README.md         # Detailed installation and architecture documentation
```