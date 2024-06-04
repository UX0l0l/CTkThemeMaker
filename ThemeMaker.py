import json
import os
from tkinter import filedialog
from customtkinter import *
from ctk_color_picker import AskColor
from CTkExample import CTkExample
from CTkMessagebox import CTkMessagebox

"""
Author: Akash Bora (Akascape)
License: MIT
Quick Guide:
This program can be used to create custom themes for customtkinter.
You can easily create and edit themes for your applications.
Customtkinter themefiles are .json files that can be used with customtkinter using the 'set_default_color_theme' method.
Example: set_default_color_theme("Path//my_theme.json")
A customtkinter theme has one dark and one light color attribute for each widget type and you have to choose the 2 colors for each widget type.
(You can switch between them with the 'set_appearance_mode' method)
Currently it is not possible to switch themes, so only appearance_mode can be changed.
Default reset color is "transparent" which has no color, means it take the color from the background instead.
(transparent is not supported in all widgets)
"""

class App(CTk):

    #--------------------Main Structure of the Theme File--------------------#
    
    json_data = {
                  "CTk": {
                    "fg_color": ["gray92", "gray14"]
                  },
                  "CTkToplevel": {
                    "fg_color": ["gray92", "gray14"]
                  },
                  "CTkFrame": {
                    "corner_radius": 6,
                    "border_width": 0,
                    "fg_color": ["gray86", "gray17"],
                    "top_fg_color": ["gray81", "gray20"],
                    "border_color": ["gray65", "gray28"]
                  },
                  "CTkButton": {
                    "corner_radius": 6,
                    "border_width": 0,
                    "fg_color": ["#3B8ED0", "#1F6AA5"],
                    "hover_color": ["#36719F", "#144870"],
                    "border_color": ["#3E454A", "#949A9F"],
                    "text_color": ["#DCE4EE", "#DCE4EE"],
                    "text_color_disabled": ["gray74", "gray60"]
                  },
                  "CTkLabel": {
                    "corner_radius": 0,
                    "fg_color": "transparent",
                    "text_color": ["gray10", "#DCE4EE"]
                  },
                  "CTkEntry": {
                    "corner_radius": 6,
                    "border_width": 2,
                    "fg_color": ["#F9F9FA", "#343638"],
                    "border_color": ["#979DA2", "#565B5E"],
                    "text_color":["gray10", "#DCE4EE"],
                    "placeholder_text_color": ["gray52", "gray62"]
                  },
                  "CTkCheckBox": {
                    "corner_radius": 6,
                    "border_width": 3,
                    "fg_color": ["#3B8ED0", "#1F6AA5"],
                    "border_color": ["#3E454A", "#949A9F"],
                    "hover_color": ["#3B8ED0", "#1F6AA5"],
                    "checkmark_color": ["#DCE4EE", "gray90"],
                    "text_color": ["gray10", "#DCE4EE"],
                    "text_color_disabled": ["gray60", "gray45"]
                  },
                  "CTkSwitch": {
                    "corner_radius": 1000,
                    "border_width": 3,
                    "button_length": 0,
                    "fg_color": ["#939BA2", "#4A4D50"],
                    "progress_color": ["#3B8ED0", "#1F6AA5"],
                    "button_color": ["gray36", "#D5D9DE"],
                    "button_hover_color": ["gray20", "gray100"],
                    "text_color": ["gray10", "#DCE4EE"],
                    "text_color_disabled": ["gray60", "gray45"]
                  },
                  "CTkRadioButton": {
                    "corner_radius": 1000,
                    "border_width_checked": 6,
                    "border_width_unchecked": 3,
                    "fg_color": ["#3B8ED0", "#1F6AA5"],
                    "border_color": ["#3E454A", "#949A9F"],
                    "hover_color": ["#36719F", "#144870"],
                    "text_color": ["gray10", "#DCE4EE"],
                    "text_color_disabled": ["gray60", "gray45"]
                  },
                  "CTkProgressBar": {
                    "corner_radius": 1000,
                    "border_width": 0,
                    "fg_color": ["#939BA2", "#4A4D50"],
                    "progress_color": ["#3B8ED0", "#1F6AA5"],
                    "border_color": ["gray", "gray"]
                  },
                  "CTkSlider": {
                    "corner_radius": 1000,
                    "button_corner_radius": 1000,
                    "border_width": 6,
                    "button_length": 0,
                    "fg_color": ["#939BA2", "#4A4D50"],
                    "progress_color": ["gray40", "#AAB0B5"],
                    "button_color": ["#3B8ED0", "#1F6AA5"],
                    "button_hover_color": ["#36719F", "#144870"]
                  },
                  "CTkOptionMenu": {
                    "corner_radius": 6,
                    "fg_color": ["#3B8ED0", "#1F6AA5"],
                    "button_color": ["#36719F", "#144870"],
                    "button_hover_color": ["#27577D", "#203A4F"],
                    "text_color": ["#DCE4EE", "#DCE4EE"],
                    "text_color_disabled": ["gray74", "gray60"]
                  },
                  "CTkComboBox": {
                    "corner_radius": 6,
                    "border_width": 2,
                    "fg_color": ["#F9F9FA", "#343638"],
                    "border_color": ["#979DA2", "#565B5E"],
                    "button_color": ["#979DA2", "#565B5E"],
                    "button_hover_color": ["#6E7174", "#7A848D"],
                    "text_color": ["gray10", "#DCE4EE"],
                    "text_color_disabled": ["gray50", "gray45"]
                  },
                  "CTkScrollbar": {
                    "corner_radius": 1000,
                    "border_spacing": 4,
                    "fg_color": "transparent",
                    "button_color": ["gray55", "gray41"],
                    "button_hover_color": ["gray40", "gray53"]
                  },
                  "CTkSegmentedButton": {
                    "corner_radius": 6,
                    "border_width": 2,
                    "fg_color": ["#979DA2", "gray29"],
                    "selected_color": ["#3B8ED0", "#1F6AA5"],
                    "selected_hover_color": ["#36719F", "#144870"],
                    "unselected_color": ["#979DA2", "gray29"],
                    "unselected_hover_color": ["gray70", "gray41"],
                    "text_color": ["#DCE4EE", "#DCE4EE"],
                    "text_color_disabled": ["gray74", "gray60"]
                  },
                  "CTkTextbox": {
                    "corner_radius": 6,
                    "border_width": 0,
                    "fg_color": ["#F9F9FA", "#1D1E1E"],
                    "border_color": ["#979DA2", "#565B5E"],
                    "text_color":["gray10", "#DCE4EE"],
                    "scrollbar_button_color": ["gray55", "gray41"],
                    "scrollbar_button_hover_color": ["gray40", "gray53"]
                  },
                  "CTkScrollableFrame": {
                    "label_fg_color": ["gray78", "gray23"]
                  },
                  "DropdownMenu": {
                    "fg_color": ["gray90", "gray20"],
                    "hover_color": ["gray75", "gray28"],
                    "text_color": ["gray10", "gray90"]
                  },
                  "CTkFont": {
                    "macOS": {
                      "family": "SF Display",
                      "size": 13,
                      "weight": "normal"
                    },
                    "Windows": {
                      "family": "Roboto",
                      "size": 13,
                      "weight": "normal"
                    },
                    "Linux": {
                      "family": "Roboto",
                      "size": 13,
                      "weight": "normal"
                    }
                  }
                }

    #--------------------Widget Type and Content--------------------#
    
    widgets = {'CTk':['fg_color'],
             'CTkToplevel':['fg_color'],
             'CTkFrame':['fg_color', 'top_fg_color', 'border_color'],
             'CTkButton':['fg_color','hover_color','border_color','text_color','text_color_disabled'],
             'CTkCheckBox':["fg_color", "border_color", "hover_color","checkmark_color", "text_color",
                            "text_color_disabled"],
             'CTkEntry':['fg_color','text_color','border_color','placeholder_text_color'],
             'CTkLabel':['fg_color', 'text_color'], 
             'CTkProgressBar':['fg_color','progress_color','border_color'],
             'CTkSlider':["fg_color", "progress_color", "button_color", "button_hover_color"],
             'CTkSwitch':["fg_Color", "progress_color", "button_color", "button_hover_color",
                          "text_color", "text_color_disabled"],
             'CTkOptionMenu':["fg_color", "button_color", "button_hover_color","text_color",
                              "text_color_disabled"],
             'CTkComboBox':["fg_color", "border_color", "button_color", "button_hover_color",
                            "text_color", "text_color_disabled"],
             'CTkScrollbar':["fg_color", "button_color", "button_hover_color"],
             'CTkRadioButton':["fg_color", "border_color", "hover_color", "text_color", "text_color_disabled"],
             'CTkTextbox':["fg_color", "border_color", "text_color", "scrollbar_button_color",
                           "scrollbar_button_hover_color"],
             'CTkSegmentedButton':["fg_color", "selected_color", "selected_hover_color", "unselected_color",
                                   "unselected_hover_color", "text_color", "text_color_disabled"],
             'CTkScrollableFrame':["label_fg_color"],
             'DropdownMenu':["fg_color", "hover_color", "text_color"]}

    widgetlist = list(widgets.keys())
    current = widgetlist[0]

    for widget_data in json_data.values():
        for key, value in widget_data.items():
            if value == "transparent":
                widget_data[key] = ["transparent", "transparent"]
            
    def __init__(self):
        #--------------------Main root Window--------------------#
        super().__init__(fg_color=ThemeManager.theme["CTkFrame"]["top_fg_color"])
        set_appearance_mode("System")
        set_default_color_theme("blue")
        self.title("CustomTkinter ThemeMaker")
        self.geometry("500x450")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        self.frame_info = CTkFrame(master=self, height=80)
        self.frame_info.grid(row=0, column=0, columnspan=6, sticky="nswe", padx=20, pady=20)
        self.frame_info.grid_columnconfigure(0, weight=1)

        self.widget_type = CTkLabel(master=self.frame_info, text=self.current, corner_radius=10, width=200, height=20, fg_color=("white", "gray38"))
        self.widget_type.grid(row=0, column=0, sticky="nswe", padx=80, pady=20)

        self.left_button = CTkButton(master=self.frame_info, text="<", width=20, height=20, corner_radius=10, fg_color=("white", "gray38"), command=lambda: self.change_mode("left"), text_color=("black","white"))
        self.left_button.grid(row=0, column=0, sticky="nsw", padx=20, pady=20)

        self.right_button = CTkButton(master=self.frame_info, text=">", width=20, height=20, corner_radius=10, fg_color=("white", "gray38"), command=lambda: self.change_mode("right"), text_color=("black","white"))
        self.right_button.grid(row=0, column=0, sticky="nse", padx=20, pady=20)

        self.menu = CTkOptionMenu(master=self, fg_color=("white", "gray38"), button_color=("white", "gray38"), text_color=("black","white"), height=30, values=self.widgets[self.current], command=self.update)
        self.menu.grid(row=1, column=0, columnspan=6, sticky="nswe", padx=20)

        self.button_light = CTkButton(master=self, height=100, width=200, corner_radius=10, border_color="white", text_color="grey50", border_width=2, text="Light", hover=False, command=lambda: self.change_color("Light"))
        self.button_light.grid(row=2, column=0, sticky="nswe", columnspan=3, padx=(20,5), pady=20)
    
        self.button_dark = CTkButton(master=self, height=100, width=200, corner_radius=10, border_color="white", text_color="gray80", border_width=2, text="Dark", hover=False, command=lambda: self.change_color("Dark"))
        self.button_dark.grid(row=2, column=3, sticky="nswe", columnspan=3, padx=(5,20), pady=20)

        self.button_load = CTkButton(master=self, height=40, width=110, text="Load Theme", command=self.load)
        self.button_load.grid(row=3, column=0,  columnspan=2, sticky="nswe", padx=(20,5), pady=(0,20))

        self.button_export = CTkButton(master=self, height=40, width=110, text="Save Theme", command=self.save)
        self.button_export.grid(row=3, column=2,  columnspan=2, sticky="nswe", padx=(5,5), pady=(0,20))
    
        self.button_reset = CTkButton(master=self, height=40, width=110, text="Reset", command=self.reset)
        self.button_reset.grid(row=3, column=4,  columnspan=2, sticky="nswe", padx=(5,20), pady=(0,20))
        
        self.palette = CTkButton(master=self, height=40, width=110, text="Color Palette", command=self.show_colors)
        self.palette.grid(row=4, column=0, columnspan=3, sticky="nswe", padx=(20,5), pady=(0,20))

        self.quick_test = CTkButton(master=self, height=40, width=110, text="Quick Test", command=self.test)
        self.quick_test.grid(row=4, column=3, columnspan=3, sticky="nswe", padx=(5,20), pady=(0,20))

        self.update()

    #--------------------App Functions--------------------#

    def change_mode(self, direction):
        # Changing current widget type based on direction
        self.widgetlist = self.widgetlist[1:] + [self.widgetlist[0]] if direction == "right" else [self.widgetlist[-1]] + self.widgetlist[:-1]

        self.current = self.widgetlist[0]
        self.widget_type.configure(text=self.current)
        self.menu.configure(values=self.widgets[self.current])
        self.menu.set(self.widgets[self.current][0])
        self.update()

    def update(self, *args):
        # Updating the widgets and their colors
        current_data = self.json_data[self.current]
        selected_item = self.menu.get()
        
        if selected_item in current_data:
            light_color, dark_color = current_data[selected_item]
            self.button_light.configure(fg_color=light_color if light_color != "transparent" else "transparent")
            self.button_dark.configure(fg_color=dark_color if dark_color != "transparent" else "transparent")
                    
    def change_color(self, mode):
        # Determine which button and JSON index to use
        button = self.button_light if mode == "Light" else self.button_dark
        json_index = 0 if mode == "Light" else 1
        
        # Choosing the color for the specified mode of the theme
        default = button._apply_appearance_mode(button._fg_color)
        default = "white" if default == "transparent" else default
        pick_color = AskColor()
        color = pick_color.get()
        
        if color:
            button.configure(fg_color=color)
            self.json_data[self.current][self.menu.get()][json_index] = color

    def save(self):
        save_file = filedialog.asksaveasfilename(initialfile="Untitled.json", defaultextension=".json", filetypes=[('JSON', ['*.json']),('All Files', '*.*')])
        if not save_file:
            return
        
        export_data = {}
        for widget, data in self.json_data.items():
            widget_data = {}
            for key, value in data.items():
                widget_data[key] = "transparent" if value == ["transparent", "transparent"] else value
            export_data[widget] = widget_data
        
        try:
            with open(save_file, "w") as f:
                json.dump(export_data, f, indent=2)
            CTkMessagebox(title="Exported!", message="Theme saved successfully!")
        except (IOError, json.JSONDecodeError) as e:
            CTkMessagebox(title="Error!", message=f"Failed to save theme file: {e}", icon="cancel")
                       
    def load(self):
        open_json = filedialog.askopenfilename(filetypes=[('JSON', ['*.json']),('All Files', '*.*')])
        if not open_json:
            return
        
        try:
            with open(open_json) as f:
                self.json_data = json.load(f)
            
            for widget_data in self.json_data.values():
                widget_data.update((k, ["transparent", "transparent"]) for k, v in widget_data.items() if v == "transparent")
            
            self.update()

        except (FileNotFoundError, json.JSONDecodeError) as e:
            CTkMessagebox(title="Error!", message=f"Unable to load this theme file! {e}", icon="cancel")

    def reset(self):
        # Resetting the current colors of the widget to null (default value)
        current_data = self.json_data[self.current]
        selected_item = self.menu.get()
        
        if selected_item in current_data:
            current_data[selected_item] = ["transparent", "transparent"]
            self.button_light.configure(fg_color="transparent")
            self.button_dark.configure(fg_color="transparent")

    def test(self):
        export_data = {widget: {key: "transparent" if value == ["transparent", "transparent"] else value for key, value in data.items()} for widget, data in self.json_data.items()}
        
        DIRPATH = os.path.dirname(os.path.abspath(__file__))
        test_theme_path = os.path.join(DIRPATH, "CTkTheme_test.json")
        with open(test_theme_path, "w") as f:
            json.dump(export_data, f)
        
        try:
            CTkExample()
        except Exception as e:
            CTkMessagebox(title="Error!", message=e, icon="cancel")
        finally:
            os.remove(test_theme_path)
            
    def replace_color(self, color, button, mode):
        # Replace a specific color
        default = "white" if color == "transparent" else color
        pick_color = AskColor()
        new_color = pick_color.get()
        new_color = "transparent" if new_color is None else new_color
        
        index = 1 if mode else 0
        for widget_data in self.json_data.values():
            for value in widget_data.values():
                if isinstance(value, list) and value[index] == color:
                    value[index] = new_color
        
        button.configure(text=new_color, fg_color=new_color)
        self.update()
            
    def show_colors(self):
        # Show the color palette for the theme
        toplevel = CTkToplevel(self)
        toplevel.title("Color Palette")
        toplevel.geometry("500x700")
        toplevel.resizable(True, True)
        toplevel.transient(self)
        self.update_idletasks()

        frame_light = CTkScrollableFrame(toplevel, label_text="Light Colors")
        frame_light.pack(fill="both", expand=True, side="left", padx=(10, 5), pady=10)

        frame_dark = CTkScrollableFrame(toplevel, label_text="Dark Colors")
        frame_dark.pack(fill="both", expand=True, side="right", padx=(5, 10), pady=10)

        colors = set()
        for data in self.json_data.values():
            for value in data.values():
                if isinstance(value, list):
                    colors.update(value)

        for color in colors:
            is_dark_color = any(color == value[1] if isinstance(value[0], str) else color in value[1] for data in self.json_data.values() for value in data.values() if isinstance(value, list))
            frame = frame_dark if is_dark_color else frame_light
            button = CTkButton(frame, text=color, fg_color=color, hover=False)
            button.configure(command=lambda c=color, b=button, m=is_dark_color: self.replace_color(c, b, 1 if m else 0))
            button.pack(fill="x", expand=True, padx=10, pady=5)
     
    def on_closing(self):
        quit = CTkMessagebox(title="Exit?", message= "Do you want to exit?", icon="question", option_1="No", option_2="Yes")
        if quit.get() == "Yes":
            self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()