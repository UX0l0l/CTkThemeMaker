from tkinter import *
from customtkinter import *
from CTkTable import *
import os

class CTkExample(CTkToplevel):
    def __init__(self):
        super().__init__()
        DIRPATH = os.path.dirname(os.path.abspath(__file__))
        themepath = os.path.join(DIRPATH, "CTkTheme_test.json")
        set_default_color_theme(themepath if os.path.exists(themepath) else "blue")

        # configure window
        self.title("CustomTkinter Example")
        self.geometry("1000x580")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<1>", lambda event: event.widget.focus_set())
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        # create sidebar frame with widgets
        self.sidebar_frame = CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = CTkLabel(self.sidebar_frame, text="CustomTkinter", font=CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = CTkButton(self.sidebar_frame)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = CTkButton(self.sidebar_frame)
        self.sidebar_button_2.grid(row=3, column=0, padx=20, pady=10)

        CTkTable(self.sidebar_frame, width=50, row=3, column=3, values=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]).grid(row=4, column=0)
        
        self.appearance_mode_label = CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = CTkOptionMenu(self.sidebar_frame, values=["System", "Light", "Dark"], command=set_appearance_mode)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=lambda new_scaling: set_widget_scaling(int(new_scaling.replace("%", "")) / 100))
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = CTkButton(master=self, fg_color="transparent", border_width=2)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.tabview = CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("CTkTabview")
        self.tabview.add("Frame")
        self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Frame").grid_columnconfigure(0, weight=1)

        self.optionmenu_1 = CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False, values=["Value 1", "Value 2"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.combobox_1 = CTkComboBox(self.tabview.tab("CTkTabview"), values=["Value 1", "Value 2"])
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.string_input_button = CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog", command=lambda: CTkInputDialog(text="Type in a number:", title="CTkInputDialog"))
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.label_tab_2 = CTkFrame(self.tabview.tab("Frame"), height=150)
        self.label_tab_2.grid(row=0, column=0, padx=(5,0), pady=20)
    
        self.scrollbar = CTkScrollbar(self.tabview.tab("Frame"), height=150)
        self.scrollbar.grid(row=0, column=1, padx=5, pady=20, sticky="nse")
        
        self.scrollbar.set(1,0.1)
        
        # create radiobutton frame
        self.radiobutton_frame = CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = IntVar(value=0)
        self.label_radio_group = CTkLabel(master=self.radiobutton_frame, text="CTkRadioButtons")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        
        # create checkbox and switch frame
        self.checkbox_slider_frame = CTkFrame(self)
        self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.checkbox_1 = CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_1.grid(row=1, column=0, pady=(20, 10), padx=20, sticky="n")
        self.checkbox_2 = CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_2.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        self.switch_1 = CTkSwitch(master=self.checkbox_slider_frame)
        self.switch_1.grid(row=3, column=0, pady=10, padx=20, sticky="n")
        self.switch_2 = CTkSwitch(master=self.checkbox_slider_frame)
        self.switch_2.grid(row=4, column=0, pady=(10, 20), padx=20, sticky="n")

        # create slider and progressbar frame
        self.slider_progressbar_frame = CTkFrame(self)
        self.slider_progressbar_frame.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.seg_button_1 = CTkSegmentedButton(self.slider_progressbar_frame)
        self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1 = CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_2 = CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_1 = CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_2 = CTkSlider(self.slider_progressbar_frame, orientation="vertical")
        self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        self.progressbar_3 = CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
        self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")
            
        label = CTkLabel(self.sidebar_frame, text="create toplevel", font=("",13))
        label.grid()

        label.bind("<Button-1>", lambda event: self.new_window())
        label.bind("<Enter>", lambda event: label.configure(font=("",13,"underline"), cursor="hand2"))
        label.bind("<Leave>", lambda event: label.configure(font=("",13), cursor="arrow"))

        # set default values
        self.sidebar_button_2.configure(state="disabled", text="Disabled CTkButton")
        self.checkbox_2.configure(state="disabled")
        self.switch_2.configure(state="disabled")
        self.checkbox_1.select()
        self.switch_1.select()
        self.radio_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("System")
        self.scaling_optionemenu.set("100%")
        self.optionmenu_1.set("CTkOptionmenu")
        self.combobox_1.set("CTkComboBox")
        self.slider_1.configure(command=self.progressbar_2.set)
        self.slider_2.configure(command=self.progressbar_3.set)
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()
        self.textbox.insert("0.0", "Write Something...")
        self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        self.seg_button_1.set("Value 2")

    def new_window(self):
        top_level = CTkToplevel()
        CTkLabel(top_level, text="A TopLevel Window").grid(padx=100, pady=100)
        top_level.attributes("-topmost", 1)
        self.after(100, lambda: top_level.attributes("-topmost", 0))

    def on_closing(self):
        set_appearance_mode("System")
        set_widget_scaling(1)
        self.destroy()