# AES Implementation - InfoSec Work 

## Description

An simple implementation of an AES encryption algorithm in Python. To be used as an study in symetric encryption.

## Installation

To install the dependencies, run the following command:

If using **nix** (or **NixOS**):
```bash
nix-develop --command <your_shell>
```

Then create a [Virtual Environment (venv)](https://docs.python.org/3/library/venv.html) and install the dependencies:

```bash
python3 -m venv ./venv
source ./venv/bin/activate # or ./venv/activate.fish if using fish shell
pip install -r requirements.txt
```

## Usage

To run it you can use the following command on the [aes](./aes) directory:

```bash
python3 aes.py
```

It generates cipher files on the [files](./aes/files) directory and cipher images on the [images](.aes/images) directory.
