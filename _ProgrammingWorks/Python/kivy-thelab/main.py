from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

Builder.load_file("layout_examples.kv")

class WidgetsExample(GridLayout):
    counter = 0
    my_text = StringProperty("clicks: " + str(counter))
    count_enabled = BooleanProperty(False)
    slider_enabled = BooleanProperty(False)
    text_input_str = StringProperty("Foo")

    def on_button_click(self):
        print("Button clicked")
        if self.count_enabled == True:
            self.counter += 1
            self.my_text = "clicks: " + str(self.counter)

    def on_toggle_button_state(self, widget):
        print("Toggle State: " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        elif widget.state == "down":
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))
        if widget.active == False:
            self.slider_enabled = False
        elif widget.active == True:
            self.slider_enabled = True

    def on_slider_value(self, widget):
        print("Slider: " + str(int(widget.value)))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text


class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()