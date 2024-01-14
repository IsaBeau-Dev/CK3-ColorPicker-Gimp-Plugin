# CK3 ColorPicker Gimp Plugin

The CK3 ColorPicker Gimp Plugin simplifies the process of selecting and applying colors to provinces in your CK3 (Crusader Kings III) map. If you're a modder or map creator, this plugin streamlines the color-picking workflow.

## Installation

1. **Download the Plugin**:
   - Visit the CK3 ColorPicker Gimp Plugin repository.
   - Click on the green "Code" button and select "Download ZIP."
   - Extract the ZIP file to a location on your computer.

2. **Place the Plugin File**:
   - Locate the `.py` file within the plugin folder.
   - Move or copy this `.py` file to the appropriate GIMP plugins directory:
     - On Linux: `~/.config/GIMP/2.10/plug-ins/`
     - On Windows: `C:\Users\USERNAME\AppData\Roaming\GIMP\2.10\plug-ins\`
   - You can also check the location of the plugins directory within GIMP by going to `Edit > Preferences > Folders > Plug-Ins`.
      - Select the path `C:\Users\USERNAME\AppData\Roaming\GIMP\2.10\plug-ins\` and click on the marked button to open it in explorer
      - ![image](https://github.com/IsaBeau-Dev/CK3-ColorPicker-Gimp-Plugin/assets/90000605/5019b0b7-0e92-4f79-b850-83ad27ecee27)

## Usage
1. **Edit the .py File**:
   - Locate the `.py` file within the plugin folder.
   - Open it in a text editor.
   - Get the path to your modded CK3 definition.csv file. For example: `C:\\Users\\isabeau\\Documents\\Paradox Interactive\\Crusader Kings III\\mod\\alagasia\\map_data\\definition.csv`
   - Look for the line that specifies the `path` to your definition.csv file in the `.py`. It should be line **4**.
   - Update the path to match the location of your `definition.csv` on your system. `path = "PATH_TO_YOUR_MODDED_DEFINITON.CSV"`
   - **YOU ONLY HAVE TO DO THIS STEP ONCE**(AS LONG AS YOU DONT WANT TO USE A DIFFERENT `DEFINITION.CSV FILE`)

2. **Access the Plugin**:
   
   - Run the CK3 ColorPicker Gimp Plugin. (You can find it in the menu bar (bar at the top) under `CK3`)
   - (https://github.com/IsaBeau-Dev/CK3-ColorPicker-Gimp-Plugin/assets/90000605/771a576d-1c16-4b02-8b23-74eeaa71c27d)
   - A window will appear, allowing you to search for provinces by name (You will see a list with all entries of definition.csv and can scroll trough it.).
   - For now just ignore the `terminal/console` that pops up and **DONT CLOSE IT** please.

3. **Select a Province**:
   - Find the name of the province you want to work with and click it.
   - The plugin will retrieve the color defined for that province in your definition.csv and add to the gimp color tool foreground color.
   - If you dont know what i mean by that look at the screenshot:
   - ![image](https://github.com/IsaBeau-Dev/CK3-ColorPicker-Gimp-Plugin/assets/90000605/a22bb41f-7a41-4060-aab1-289ad30eb98d)

4. **Apply the Color**:
   - Use the retrieved color in your GIMP color tool.
   - Draw the corresponding province directly on your provinces.png map.

## Contributing

Contributions are welcome! If you encounter any issues or have ideas for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to customize this template further to suit your project's specific needs. Happy modding! 🌟🎨
