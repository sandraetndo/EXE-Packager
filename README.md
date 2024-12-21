# EXE Packager

## Description

The **EXE Packager** is a simple tool that allows users to combine multiple executable files (.exe) into a single standalone EXE. The tool provides a GUI to manage the files and package them with a simple launcher for easy execution.

## Features

- Add multiple `.exe` files to a list.
- Remove unwanted files before packaging.
- Package all selected `.exe` files into a single standalone `.exe`.
- Easy-to-use GUI.

## How to Use

1. **Launch the Tool**:
   - Run the `exe_packager.py` script or the packaged executable.

2. **Add Executables**:
   - Click the "Add EXE" button and select executable files from your system.

3. **Remove Executables**:
   - Select unwanted files from the list and click "Remove Selected."

4. **Package Files**:
   - Click "Package EXEs" and save the packaged executable file to your desired location.

5. **Run the Packaged EXE**:
   - The packaged EXE includes a launcher that allows you to choose and run any of the included executables.

## Requirements

- Python 3.x
- `tkinter` (comes pre-installed with Python)
- `PyInstaller` (install with `pip install pyinstaller`)

## Notes

- The packaged EXE will include a launcher that lists all the executables. Users can choose which one to run from the list.
- Ensure that the added `.exe` files are accessible at the time of packaging.

## License

This project is licensed under the MIT License.
