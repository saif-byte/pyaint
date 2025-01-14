from .settings import *
from .button import *


class Theme(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Theme, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.isLightMode = True
        self.BG_COLOR = WHITE
        self.BORDER_COLOR = BLACK
        self.BG_TEXTCOLOR = BLACK
        self.DARK_THEME_COLOR = (20, 20, 20)
        self.DARK_THEME_TEXT_BACKGROUND_COLOR = (81, 81, 81)
        self.GRID_COLOR = WHITE
        self.GRID_LINES_COLOR = SILVER
        self.GRID_COLOR_DARK_THEME = (189, 191, 189)

    def toggle(
        self,
        buttons,
        colorModeButtons,
        colorMixerButtons,
        colorWindowButtons,
        custom_color_count,
        paletteWindowButtons,
        colorGradientButtons,
    ):
        if self.isLightMode:
            self.BG_COLOR = self.DARK_THEME_COLOR
            self.BORDER_COLOR = WHITE
            self.BG_TEXTCOLOR = WHITE
            self.GRID_COLOR = self.GRID_COLOR_DARK_THEME
            self.GRID_LINES_COLOR = WHITE
            count = 0
            for button in buttons:
                button.border_color = WHITE
                if button.name and button.name.startswith("custom_colors_"):
                    count = count + 1
                    if count > custom_color_count:
                        button.color = BLACK
                if button.text:
                    button.color = self.DARK_THEME_TEXT_BACKGROUND_COLOR
                    button.text_color = WHITE
                if button.name == "switchForeBack":
                    button.image_url = "assets/white-switch_foreback.png"
            for button in colorModeButtons:
                button.border_color = WHITE
                if button.text:
                    button.color = self.DARK_THEME_TEXT_BACKGROUND_COLOR
                    button.text_color = WHITE
            for button in colorGradientButtons:
                button.border_color = WHITE
                if button.name and button.name.startswith("gradient"):
                    if button.color == WHITE:
                        button.color = BLACK
                if button.text:
                    button.color = self.DARK_THEME_TEXT_BACKGROUND_COLOR
                    button.text_color = WHITE
            for button in colorMixerButtons:
                button.border_color = WHITE
                if button.text:
                    button.color = self.DARK_THEME_TEXT_BACKGROUND_COLOR
                    button.text_color = WHITE
            for button in colorWindowButtons:
                button.border_color = WHITE
                if button.text:
                    button.color = self.DARK_THEME_TEXT_BACKGROUND_COLOR
                    button.text_color = WHITE
            for button in paletteWindowButtons:
                button.border_color = WHITE
                if button.text:
                    button.color = self.DARK_THEME_TEXT_BACKGROUND_COLOR
                    button.text_color = WHITE
                if button.name == "TickPalette":
                    button.image_url = "assets/white-tick.png"
                if button.name == "Error Message":
                    button.text_color = WHITE
                if button.name == "PaletteName":
                    button.color = self.DARK_THEME_TEXT_BACKGROUND_COLOR
                    button.text_color = WHITE

        else:
            self.BG_COLOR = WHITE
            self.BORDER_COLOR = BLACK
            self.BG_TEXTCOLOR = BLACK
            self.GRID_COLOR = WHITE
            self.GRID_LINES_COLOR = SILVER
            count = 0
            for button in buttons:
                button.border_color = BLACK
                if button.name and button.name.startswith("custom_colors_"):
                    count = count + 1
                    if count > custom_color_count:
                        button.color = WHITE
                if button.text:
                    button.color = WHITE
                    button.text_color = BLACK
                if button.name == "switchForeBack":
                    button.image_url = "assets/switch_foreback.png"
            for button in colorModeButtons:
                if button.color == BLACK:
                    button.border_color = GRAY
                else:
                    button.border_color = BLACK
                if button.text:
                    button.color = WHITE
                    button.text_color = BLACK
            for button in colorGradientButtons:
                if button.color == BLACK:
                    button.border_color = GRAY
                else:
                    button.border_color = BLACK
                if button.name and button.name.startswith("gradient"):
                    if button.color == BLACK:
                        button.color = WHITE
                if button.text:
                    button.color = WHITE
                    button.text_color = BLACK
            for button in colorMixerButtons:
                if button.color == BLACK:
                    button.border_color = GRAY
                else:
                    button.border_color = BLACK
                if button.text:
                    button.color = WHITE
                    button.text_color = BLACK
            for button in colorWindowButtons:
                button.border_color = BLACK
                if button.text:
                    button.color = WHITE
                    button.text_color = BLACK
            for button in paletteWindowButtons:
                button.border_color = BLACK
                if button.text:
                    button.color = WHITE
                    button.text_color = BLACK
                if button.name == "TickPalette":
                    button.image_url = "assets/tick.png"
                if button.name == "Error Message":
                    button.text_color = BLACK
                if button.name == "PaletteName":
                    button.color = WHITE
                    button.text_color = BLACK

        self.isLightMode = not self.isLightMode
