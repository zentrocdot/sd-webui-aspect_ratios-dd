#!/usr/bin/python3
'''sd-webui-aspect_ratios-dd
Extension for AUTOMATIC1111.

Version 0.0.0.3

Description
The aspect ratios are given in a list. From this list a dictionary 
is created, in which e.g. the key is "1:1" and the value is 1.0. This
dictionary is required in my approach to get the value on base of the 
key.
'''
# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods
# pylint: disable=attribute-defined-outside-init
# pylint: disable=import-error
# pylint: disable=consider-using-from-import
# pylint: disable=trailing-whitespace
# pylint: disable=unused-argument
# pylint: disable=too-many-instance-attributes
# pylint: disable=no-self-use
# pylint: disable=bad-indentation
# pylint: disable=unused-variable

# Import the Python modules.
import contextlib
import gradio as gr
import modules.scripts as scripts
from modules.ui_components import ToolButton, InputAccordion

# Define module variables.
_width = 512
_height = 512

# Define the list with the aspect ratios.
arlist = ["1:1", "1.5:1", "2:1", "3:1", "3:2", "4:1", "4:3", "5:1",
          "5:3", "5:4", "6:1", "6:5", "7:1", "7:4", "7:5", "7:5.5",
          "8:3", "8:5", "9:7", "10:1", "10:7", "11:5", "11.85:3", 
          "12:1", "12:5", "12:9", "12:10", "13∶6", "13:18", "13:19",
          "14:9", "15:8", "15:9", "15:10", "16:9", "16:10", "17:9",
          "18:5", "18:9", "18.5:9", "18:10", "19:9", "19.5:9", "20:9",
          "21:9", "21.5:9", "22:9", "22:17", "24:9", "25:16", "28:13",
          "32:9", "32:25", "35:26", "36:10", "37∶18", "37:20", "43:18",
          "45:35", "47:20", "51:20", "55:23", "64:27", "69:25", "70:27",
          "79:20", "128:75", "192:145", "239:100", "256:135", "1.19:1",
          "1.20:1", "1.25:1", "1.27:1", "1.30:1", "1.33:1", "1.37:1",
          "1.375:1", "1.38:1", "1.40:1", "1.41:1", "1.4142:1", "1.43:1",
          "1.54:1", "1.55:1", "1.59:1", "1.60:1", "1.618:1", "1.66:1",
          "1.75:1", "1.77:1", "1.78:1", "1.85:1", "1.875:1", "1.896:1",
          "1.90:1", "1.91:1", "2.125:1", "2.16:1", "2.165:1", "2.20:1",
          "2.208:1", "2.21:1", "2.35:1", "2.37:1", "2.38:1", "2.39:1",
          "2.40:1", "2.55:1", "2.66:1", "2.75:1", "2.76:1", "3.2:1",
          "3.55:1", "3.58:1", "3.60:1", "3.95:1"]

# Create a dictionary.
ardict = dict()
for ele in arlist:
    templist = ele.split(":")
    fval = float(templist[0]) / float(templist[1])       
    ardict[str(ele)] = fval 

# Define class ARDDButton.
class  ARDDButton(ToolButton):
    '''New button class.'''
    def __init__(self, ar=1.0, **kwargs):
        '''Class init method.'''
        super().__init__(**kwargs)
        self.ar = ar

    def apply(self, w, h):
        '''Class method apply.'''
        # Initialise height and width.
        w = _width
        h = _height
        # Calculate new width and height.
        if self.ar > 1.0:  # fixed height, change width
            w = self.ar * h
        elif self.ar < 1.0:  # fixed width, change height
            h = w / self.ar
        else:  # set minimum dimension to both
            min_dim = min([w, h])
            w, h = min_dim, min_dim
        # Create a new list.
        retlst = list(map(round, [w, h]))
        # Return the list with width and height.
        return retlst

# Define class ARDDScript.
class ARDDScript(scripts.Script):
    '''Class for selecting the aspect ratio.'''
    
    def title(self):
        '''Class method title.'''
        return "Aspect Ratio Selector"

    def show(self, is_img2img):
        '''Class method show.'''
        return scripts.AlwaysVisible  # hide this script in the Scripts dropdown

    def image_resolution(self, is_img2img):
        '''Get the image resolution from container and return the values.'''
        if is_img2img:
            imgres = [self.i2i_w, self.i2i_h]
        else:
            imgres = [self.t2i_w, self.t2i_h]
        return imgres    

    def ui(self, is_img2img):
        '''Class method ui.'''
        # Set the css format strings.
        css_acc = f'{"img" if is_img2img else "txt"}2img_ARDD_accordion_aspect_ratio' 
        css_col = f'{"img" if is_img2img else "txt"}2img_ARDD_column_aspect_ratio'
        css_row = f'{"img" if is_img2img else "txt"}2img_ARDD_row_aspect_ratio'
        # Create a column.
        with gr.Column(elem_id=css_col):
            with InputAccordion(value=False,
                label="Common Landscape Aspect Ratios", 
                elem_id=css_acc
            ) as enabled:
                with gr.Row(elem_id=css_row):      
                    arval = gr.Dropdown(arlist, label="Aspect Ratios", value="1:1")
                    exact = gr.Textbox(value="EXACT", lines=1, render=True,
                            interactive=True, label="Calculation of Width/Height")
                with gr.Row(elem_id=css_row):
                    rst = ARDDButton(ar=1.0, value="Reset")
                    btn = ARDDButton(ar=1.0, value="Apply")
                    chg = ARDDButton(ar=1.0, value="Change Orientation")
                    with contextlib.suppress(AttributeError):
                        imgres = self.image_resolution(is_img2img)
                        def update_button(arstr):
                            btn.ar = ardict[arstr]
                            return btn.apply(_width, _height)
                        def check_calc(arstr):    
                            retval = "ROUNDED"      
                            ar = ardict[arstr]
                            x = _width
                            y = x * ar
                            print(x, y)      
                            if float(y).is_integer():
                                retval = "EXACT"        
                            return retval          
                        btn.click(update_button, inputs=[arval], outputs=imgres)
                        btn.click(check_calc, inputs=[arval], outputs=exact)      
                        def update_rst0(arstr): 
                            rst.ar = 1.0
                            return rst.apply(_width, _height)
                        def update_rst1(arstr): 
                            rst = "1:1"
                            return rst
                        rst.click(update_rst0, inputs=[arval], outputs=imgres)
                        rst.click(update_rst1, inputs=[arval], outputs=[arval])
                        def update_chg(arstr):
                            chg.ar = 1/ardict[arstr]
                            return chg.apply(_width, _height)
                        chg.click(update_chg, inputs=[arval], outputs=imgres)
                              
    # Class method after_component.
    def after_component(self, component, **kwargs):
        '''Class method after_component.

        This method is used to generalize the existing code. It is detected if 
        one is in the txt2img tab or the img2img tab. Then the corresponding self
        variables can be used in the same code for both tabs.
        '''
        if kwargs.get("elem_id") == "txt2img_width":
            self.t2i_w = component
        if kwargs.get("elem_id") == "txt2img_height":
            self.t2i_h = component
        if kwargs.get("elem_id") == "img2img_width":
            self.i2i_w = component
        if kwargs.get("elem_id") == "img2img_height":
            self.i2i_h = component
        if kwargs.get("elem_id") == "img2img_image":
            self.image = [component]
        if kwargs.get("elem_id") == "img2img_sketch":
            self.image.append(component)
        if kwargs.get("elem_id") == "img2maskimg":
            self.image.append(component)
        if kwargs.get("elem_id") == "inpaint_sketch":
            self.image.append(component)
        if kwargs.get("elem_id") == "img_inpaint_base":
            self.image.append(component)
