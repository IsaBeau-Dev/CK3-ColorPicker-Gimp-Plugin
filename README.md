# CK3 ColorPicker Gimp Plugin

The CK3 ColorPicker Gimp Plugin simplifies the process of selecting and applying colors to provinces in your CK3 (Crusader Kings III) map. If you're a modder or map creator, this plugin streamlines the color-picking workflow.

## Installation

1. **Download the Plugin**:
   - Visit the CK3 ColorPicker Gimp Plugin repository.
   - Click on the green "Code" button and select "Download ZIP."
   - Extract the ZIP file to a location on your computer.

2. **Install in GIMP**:
   - Open GIMP.
   - Go to `Edit > Preferences > Folders > Plug-ins`.
   - Add the folder containing the extracted plugin files to the list of plugin folders.
   - Restart GIMP.

3. **Edit the .py File**:
   - Locate the `.py` file within the plugin folder.
   - Open it in a text editor.
   - Look for the line that specifies the path to your `definition.csv` file.
   - Update the path to match the location of your `definition.csv` on your system.

## Usage

1. **Access the Plugin**:
   - Open your CK3 definition.csv file (which contains province-color mappings).
   - Run the CK3 ColorPicker Gimp Plugin.
   - A window will appear, allowing you to search for provinces by name (you need to scroll and find).

2. **Select a Province**:
   - Select the name of the province you want to work with.
   - The plugin will retrieve the color defined for that province in your definition.csv.

3. **Apply the Color**:
   - Use the retrieved color in your GIMP color tool.
   - Draw the corresponding province directly on your provinces.png map (preferably also opened in gimp).

## Contributing

Contributions are welcome! If you encounter any issues or have ideas for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to customize this template further to suit your project's specific needs. Happy modding! 🌟🎨
