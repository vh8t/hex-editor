# Command Line Hex Editor

## Overview

This project is a simple command line hex editor implemented in Python for educational and fun purposes. The hex editor provides basic functionality to manipulate binary files through the command line.

## Features

1. **Insert:** Insert a specified number of bytes at a given offset.
2. **Delete:** Remove a specified number of bytes from a given offset.
3. **Replace:** Replace bytes at a specific offset with a given set of bytes.
4. **Save:** Save the changes made to the file.
5. **Read:** Display the full file in hexadecimal bytes or show bytes from a specific offset with a specified amount.

## Usage

To run the hex editor, execute the Python script in the command line. Follow the on-screen prompts to perform various operations.

```bash
python main.py <file>
```

## Commands

- **insert:** Insert bytes at a specific offset.
```bash
insert <offset> <bytes>
```

- **delete:** Delete bytes from a specific offset.
```bash
delete <offset> [length]
```

- **replace:** Replace bytes at a specific offset with new bytes.
```bash
replace <offset> <bytes>
```

- **save:** Save the changes made to the file.
```bash
save
```

- **read:** Display the full file in hexadecimal bytes or show bytes from a specific offset with a specified amount.
```bash
read [offset] [length]
```

## Example Usage

1. Insert 4 bytes at offset `0x10`:
```bash
insert 10 D4 0F 00 00
```

2. Delete 8 bytes from offset `0x20`:
```bash
delete 20 8
```

3. Replace bytes from offset `0x30` with new bytes:
```bash
replace 30 7F C3 00
```

4. Save the changes made to the file:
```bash
save
```

5. Display the full file in hexadecimal bytes:
```bash
read
```

6. Display 16 bytes from offset `0x40`:
```bash
read 40 16
```

## Note

This hex editor is created for educational and entertainment purposes and may not be suitable for real-world use. Use it with caution and be aware of potential issues. Contributions and improvements are welcome.

## License

This project is licensed under the `Apache License 2.0` - see the [LICENSE](LICENSE) file for details.