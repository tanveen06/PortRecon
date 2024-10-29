# PortRecon

PortRecon is a simple and effective port scanning tool built using Python and the Nmap library. It allows users to scan a specified target for open ports, along with detailed information about the services running on those ports and the operating system of the target.

## Features

- **Comprehensive Scanning**: Performs SYN scans to identify open ports.
- **Service and Version Detection**: Detects services and their versions on open ports.
- **Operating System Detection**: Identifies the operating system of the target.
- **Custom Port Scanning**: Allows users to specify individual ports or port ranges.
- **User-Friendly Output**: Displays results in a clear and readable format.

## Requirements

- Python 3.x
- Nmap installed on your system
- `python-nmap` library

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tanveen06/portrecon.git
   cd portrecon
   ```

2. **Install the required Python library**:
   ```bash
   pip install python-nmap
   ```

3. **Ensure Nmap is installed**:
   - For macOS, use Homebrew:
     ```bash
     brew install nmap
     ```
   - For Linux, install via your package manager:
     ```bash
     sudo apt-get install nmap  # Ubuntu/Debian
     sudo yum install nmap      # CentOS/RHEL
     ```

## Usage

Run the script directly from the command line:
```bash
python portrecon.py
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the Nmap team for creating such a powerful network scanning tool.
- Thanks to the `python-nmap` library for making Nmap accessible from Python.

## Notes

- Make sure to replace `tanveen06` in the Git clone URL with your actual GitHub username.
- Adjust any sections as needed based on your project's specifics or preferences. 

Let me know if you need any further adjustments!
