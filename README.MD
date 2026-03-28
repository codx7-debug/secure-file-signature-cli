# 🔐 Secure File Signature CLI

A Python-based Command Line Interface (CLI) tool for verifying file integrity and authenticity using **SHA-256 hashing** and **RSA digital signatures**.

---

## 📌 Features

* ✅ Generate SHA-256 hash for any file
* 📁 Create a manifest (`metadata.json`) for a directory
* 🔍 Detect file tampering (modified, deleted, or new files)
* 🔑 Generate RSA public/private key pair
* ✍️ Sign files using a private key
* ✔️ Verify authenticity using a public key

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/secure-file-signature-cli.git
cd secure-file-signature-cli
```

2. Create virtual environment (optional but recommended):

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 🔹 Generate Hash

```bash
py main.py hash -p test_files/file1.txt
```

---

### 🔹 Create Manifest

```bash
py main.py manifest -p test_files
```

---

### 🔹 Check Integrity

```bash
py main.py check -p test_files
```

---

### 🔹 Generate RSA Keys

```bash
py main.py genkeys
```

---

### 🔹 Sign Manifest

```bash
py main.py sign
```

---

### 🔹 Verify Signature

```bash
py main.py verify
```

---

## 🧠 How It Works

1. Files are hashed using SHA-256
2. Hashes are stored in `metadata.json`
3. The manifest is signed using a private key
4. The receiver verifies using the public key

---

## 🔐 Security Concepts

### ✔ Integrity

Ensures files have not been modified using hashing.

### ✔ Authenticity

Ensures the file came from the correct sender using digital signatures.

### ✔ Non-Repudiation

The sender cannot deny signing the file because only they have the private key.

---

## ⚠️ Important Notes

* ❌ Never share `private_key.pem`
* ✅ `public_key.pem` can be shared safely
* `.gitignore` excludes sensitive files

---

## 📂 Project Structure

```
secure-file-signature-cli/
│
├── main.py
├── hashing/
├── crypto/
├── data/
├── test_files/
├── README.md
└── requirements.txt
```

---

## 🎥 Demo

(Attach your YouTube video link here)

---

## 📄 License

This project is for educational purposes.
