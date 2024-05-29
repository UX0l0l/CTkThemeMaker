# CTkThemeMaker
A quick and easy theme builder for customtkinter!

## To-do list

- [ ] ~~Add support for CTkTable~~
- [ ] ~~Add support for other widgets (not sure which ones yet)~~
- [x] Fix color palette button
- [x] Replace default tkinter askcolor with CTkColorPicker
    - [x] Use forked [CTkColorPicker](https://github.com/UX0l0l/CTkColorPicker) with added RGB and Hex color inputs (until the pull request is merged into the main origin branch)
- [x] Replace traditional tkinter messagebox with CTkMessagebox

Note: Support for custom widgets was hard to implement due to changes not being detected from the JSON file, only the default CTk widgets are supported for now (and some custom widgets such as CTkMessageBox or CTkMenuBar which take on attributes of buttons and other default CTk widgets)

## Features
- Create custom themes
- Save themes
- Load themes
- **Quickly test** your themes with a built-in example
- Simple interface
- Color Palette for quick color replacements
- No extra package installation required, just run the program and make your theme 😤

## Download

Simply clone the repository using `git clone https://github.com/UX0l0l/CTkThemeMaker`, or download the zip folder by clicking "Code > Download ZIP" on the top right corner.

**Compatible ctk version: 5.2.0+**

Extract the zip file and run `CTkThemeMaker.py`
### [<img src="https://img.shields.io/badge/Contribute-Theme-informational?&color=c8ab09&style=for-the-badge" width="150">](https://github.com/Akascape/CTkThemeMaker/discussions/new?category=contribute-theme)

![Screenshot](https://github.com/Akascape/CTkThemeMaker/assets/89206401/69f91aa8-377e-4017-8a7d-9c7fb0ce110d)