# python-ethereum-address-generator-csv

This project is a Python tool for generating Ethereum addresses in batch and saving them as a CSV file.

## Installation

To use this tool, you need to have Python installed on your system. You also need to install the required dependencies. You can do this by running the following command:

```
pip install -r requirements.txt
```

## Usage

1. Run the `ethereum_address_generator.py` script:
```
python ethereum_address_generator.py
```

2. Enter the number of addresses you want to generate when prompted.

3. The program will generate the specified number of Ethereum addresses and their private keys, and save them in a CSV file named `ethereum_addresses.csv`.

4. The CSV file will contain two columns: "Address" and "Private Key".

## File Structure

- `ethereum_address_generator.py`: The main script for generating Ethereum addresses.
- `requirements.txt`: A file containing the required dependencies.

## License

[MIT License](LICENSE)