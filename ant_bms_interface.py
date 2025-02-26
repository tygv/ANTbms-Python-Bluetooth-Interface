import serial
import time
import sys

# ----- Configuration -----
# Update COM_PORT to the Bluetooth virtual COM port on your Windows PC.
COM_PORT = "COM3"         # Example: "COM3"
BAUD_RATE = 9600          # Baud rate for ANT BMS communication
TIMEOUT = 1               # Timeout in seconds

# Command to request hardware info (example: "DD A5 05 00 FF FB 77")
REQUEST_CMD = bytes([0xDD, 0xA5, 0x05, 0x00, 0xFF, 0xFB, 0x77])

# ----- Helper Functions -----
def verify_checksum(packet: bytes) -> bool:
    """
    Verifies that the checksum in the received packet is correct.
    Calculation:
      - Sum all bytes in packet[2:-3]
      - Subtract each from 0x10000 (65536)
      - Convert the result to 2 bytes (big endian)
    The two checksum bytes in the packet are located immediately before the end byte (0x77).
    """
    if len(packet) < 6:
        return False  # Packet too short
    data_for_crc = packet[2:-3]
    expected_checksum = packet[-3:-1]
    crc = 0x10000
    for b in data_for_crc:
        crc -= b
    calculated = crc.to_bytes(2, byteorder='big')
    return calculated == expected_checksum

def parse_packet(packet: bytes) -> dict:
    """
    Parses a received packet with the assumed format:
      - Start byte: 0xDD
      - Command/Response ID: Byte 1
      - Status: Byte 2 (0x00 means OK)
      - Data Length: Byte 3 (N bytes, excluding itself)
      - Data: Bytes 4 to 4+N-1
      - Checksum: 2 bytes immediately before the end
      - End byte: 0x77
    Returns a dictionary with parsed elements.
    """
    if len(packet) < 7:
        raise ValueError("Packet too short to parse")
    if packet[0] != 0xDD or packet[-1] != 0x77:
        raise ValueError("Packet framing error (incorrect start/end byte)")
    
    cmd = packet[1]
    status = packet[2]
    data_length = packet[3]
    data = packet[4:4 + data_length]
    
    return {
        "command": cmd,
        "status": status,
        "data_length": data_length,
        "data": data
    }

def display_parsed_data(parsed: dict):
    """
    Displays the parsed packet content.
    Attempts to decode data as ASCII; if it fails, shows hexadecimal values.
    """
    print("Parsed Packet:")
    print("  Command ID: 0x{:02X}".format(parsed["command"]))
    print("  Status: 0x{:02X}".format(parsed["status"]))
    print("  Data Length: {}".format(parsed["data_length"]))
    
    try:
        data_str = parsed["data"].decode('ascii')
        print("  Data (ASCII):", data_str)
    except UnicodeDecodeError:
        data_hex = " ".join("{:02X}".format(b) for b in parsed["data"])
        print("  Data (Hex):", data_hex)

# ----- Main Routine -----
def main():
    print(f"Opening serial port {COM_PORT} at {BAUD_RATE} baud...")
    try:
        ser = serial.Serial(port=COM_PORT, baudrate=BAUD_RATE, timeout=TIMEOUT)
    except serial.SerialException as e:
        print("Error opening serial port:", e)
        sys.exit(1)

    time.sleep(2)  # Allow time for connection stabilization

    try:
        print("Sending command to request hardware info...")
        ser.write(REQUEST_CMD)
        time.sleep(0.5)  # Pause for response
        
        response = ser.read(64)  # Read expected response bytes (adjust as needed)
        if not response:
            print("No response received from the BMS.")
            return

        print("Raw response (hex):", " ".join("{:02X}".format(b) for b in response))
        
        if not verify_checksum(response):
            print("Checksum verification FAILED!")
        else:
            print("Checksum verification passed.")
        
        try:
            parsed = parse_packet(response)
            display_parsed_data(parsed)
        except ValueError as ve:
            print("Error parsing packet:", ve)
    finally:
        ser.close()
        print("Serial port closed.")

if __name__ == "__main__":
    main()
