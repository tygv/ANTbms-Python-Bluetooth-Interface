# ANT BMS Python Bluetooth Interface 🚀🔵

Welcome to the **ANT BMS Python Bluetooth Interface** project! This repository contains a Python-based interface for communicating with an ANT Battery Management System (BMS) using a Bluetooth connection on a Windows PC.

---

## 📖 Overview

This project implements a Python script that:

- Uses a Bluetooth connection (via a virtual COM port) to interface with the ANT BMS.
- Sends commands to request data (e.g., hardware info, cell voltages, status).
- Verifies response integrity with checksum calculations.
- Parses the response data based on a protocol specification originally designed for RS485/UART/RS232 interfaces.

Even though the physical connection is via Bluetooth, the underlying protocol remains consistent. For detailed protocol specifications (frame structure, command codes, checksum calculation, and data interpretation), please refer to the document provided in the `docs/` folder.

---

## 🗂️ Repository Structure

```
ANTbms-Python-Bluetooth-Interface/
├── README.md                          # Detailed project documentation (you are here!)
├── .gitignore                         # Python-specific ignore file
├── ant_bms_interface.py               # Main Python script for Bluetooth communication
└── docs/
    └── RS485-UART-RS232-Communication-protocol.pdf  # Protocol specification document
```

---

## 🔧 Prerequisites

Before you begin, ensure you have the following:

- **Hardware:**  
  - A Windows PC  
  - ANT BMS device  
  - Bluetooth adapter (configured as a virtual COM port)

- **Software:**  
  - Python 3.x  
  - [pyserial](https://pyserial.readthedocs.io/) library  
    Install via pip:
    ```bash
    pip install pyserial
    ```

---

## ⚙️ Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/ANTbms-Python-Bluetooth-Interface.git
   cd ANTbms-Python-Bluetooth-Interface
   ```

2. **Configure the Script:**
   - Open `ant_bms_interface.py` in your favorite code editor.
   - Update the `COM_PORT` variable to match your Bluetooth virtual COM port (e.g., `"COM3"`).
   - Verify that the baud rate (default is 9600) and other settings match your device’s specifications.

3. **Review Protocol Documentation:**
   - Open the file [RS485-UART-RS232-Communication-protocol.pdf](docs/RS485-UART-RS232-Communication-protocol.pdf) located in the `docs/` folder.
   - This document details the frame structure, command codes, checksum calculations, and data interpretation.
   - **Note:** Although the connection is via Bluetooth, the same protocol rules apply.

---

## ▶️ Running the Project

To run the interface script, execute the following command in your repository folder:

```bash
python ant_bms_interface.py
```

The script will:
- Open the Bluetooth serial connection.
- Send a command to the ANT BMS.
- Read and verify the response using a checksum.
- Parse and display the data.

Watch the console output for details on the communication and any potential errors.

---

## 🛠️ Troubleshooting

- **No Response Received:**  
  Make sure the ANT BMS is powered, in range, and that your Bluetooth adapter is properly configured.
  
- **Checksum Verification Failure:**  
  Verify that the command is formatted correctly and that your ANT BMS adheres to the expected protocol.
  
- **Serial Port Issues:**  
  Confirm that the COM port number is correct and that your Bluetooth adapter is functioning properly.

---

## 🤝 Contributing

Contributions, suggestions, and feedback are always welcome! If you have ideas to improve this project or encounter any issues, please submit an [issue](https://github.com/tygv/ANTbms-Python-Bluetooth-Interface/issues) or create a pull request.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the license terms.

---

## 💬 Contact

If you have any questions or need further assistance, please feel free to reach out via the repository’s [issues](https://github.com/tygv/ANTbms-Python-Bluetooth-Interface/issues).

Happy coding! 😊
