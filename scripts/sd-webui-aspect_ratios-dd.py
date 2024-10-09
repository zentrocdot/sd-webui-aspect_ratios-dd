'''sd-webui-uncommon_aspect_ratios
Extension for AUTOMATIC1111.

Version 0.0.0.1
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

# Import the Python modules.
import contextlib
import gradio as gr
import modules.scripts as scripts
from modules.ui_components import ToolButton, InputAccordion

# Define module variables.
_width = 512
_height = 512

# Define the module aspect ratio dictionary.
ardict = {"1:1   ": 1.0,    "1.19:1": 1.19,  "1.25:1": 1.25,   "1.3:1 ": 1.3, 
          "1.33:1": 1.33,   "1.37:1": 1.37,  "1.375:1": 1.375, "1.41:1": 1.41,
          "1.43:1": 1.43,   "1.5:1 ": 1.5,   "1.54:1": 1.54,   "1.59:1": 1.59,
          "1.6:1 ": 1.6,    "1.66:1": 1.66,  "1.75:1": 1.75,   "1.77:1": 1.77,
          "1.78:1": 1.78,   "1.85:1": 1.85,  "1.875:1": 1.875, "2:1   ": 2.0, 
          "2.125": 2.125,   "2.16:1": 2.16,   "2.20:1": 2.20,  "2.21:1": 2.21,
          "2.35:1": 2.35,   "2.37:1": 2.37,   "2.38:1": 2.38,  "2.39:1": 2.39, 
          "2.4:1": 2.4,     "2.40:1": 2.40,   "2.66:1": 2.66,  "2.75:1": 2.75,
          "2.76:1": 2.76,   "3:1   ": 3.0,    "3:2   ": 3/2,   "3.2:1 ": 3.2,  
          "3.55:1": 3.55,   "3.58:1": 3.58,   "3.6:1 ": 3.6,   "4:1   ": 4.0, 
          "4:3   ": 4/3,    "5:1   ": 5.0,    "5:3   ": 5/3,   "5:4   ": 5/4,   
          "6:1   ": 6.0,    "6:5   ": 6/5,    "7:1   ": 7.0,   "7:4   ": 7/4,   
          "7:5   ": 7/5,    "8:5": 8/5,       "10:12 ": 10/12, "11:5  ": 11/5, 
          "12:5  ": 12/5,   "13:18": 13/18,   "13:19 ": 13/19, "14:9  ": 14/9,  
          "16:9  ": 16/9,   "16:10": 16/10,   "17:22 ": 17/22, "18:5  ": 18/5, 
          "18:9  ": 18/9,   "18.5:9": 18.5/9, "19.5:9": 19.5/9, "20:9  ": 20/9,
          "21:9  ": 21/9,   "22:9  ": 22/9,   "32:9  ": 32/9,   "36:10 ": 3.6, 
          "45:35 ": 45/35,  "55:23": 55/23,   "64:27": 64/27,   "69:25 ": 69/25, 
          "256:135": 256/135}

# Declare the aspect ratio list.
arlist = []

# Create the aspect ratio list.
for key, value in ardict.items():
    arlist.append(key)  

# Define class AspectRatioButton.
class  AspectRatioButton(ToolButton):
    '''Class for calculating the new Width and new Height for
       use in the web UI from the chosen aspect ratio.
    '''
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

# Define class AspectRatioScript.
class AspectRatioScript(scripts.Script):
    '''Class for selecting the aspect ratio.'''
    
    def title(self):
        '''Class method title.'''
        return "Aspect Ratio Selector"

    def show(self, is_img2img):
        '''Class method show.'''
        return scripts.AlwaysVisible  # hide this script in the Scripts dropdown

    def ui(self, is_img2img):
        '''Class method ui.'''
        # Loop over the columns.
        with gr.Column(
            elem_id=f'{"img" if is_img2img else "txt"}2img_container_aspect_ratio'
        ):
            with InputAccordion(
                False, label="Utilised Aspect Ratios (Landscape Orientation)", 
                elem_id=f'{"img" if is_img2img else "txt"}2img_row_aspect_ratio'
            ) as enabled:
                arval = gr.Dropdown(arlist, label="Aspect Ratios", value="1:1")
                with gr.Row(
                    elem_id=f'{"img" if is_img2img else "txt"}2img_container_aspect_ratio'
                ):
                  rst = AspectRatioButton(ar=1.0, value="Reset")
                  btn = AspectRatioButton(ar=1.0, value="Apply")
                  chg = AspectRatioButton(ar=1.0, value="Change Orientation")
                  with contextlib.suppress(AttributeError):
                    if is_img2img:
                        imgres = [self.i2i_w, self.i2i_h]
                    else:
                        imgres = [self.t2i_w, self.t2i_h]
                    def update_button(arstr):      
                        btn.ar = ardict[arstr]
                        return btn.apply(_width, _height)
                    btn.click(
                        update_button,
                        inputs=[arval],
                        outputs=imgres
                    )
                    def update_rst(arstr):      
                        rst.ar = 1.0
                        return rst.apply(_width, _height)
                    rst.click(
                        update_rst,
                        inputs=[arval],
                        outputs=imgres
                    )
                    def update_chg(arstr):      
                        chg.ar = 1/ardict[arstr]
                        return chg.apply(_width, _height)
                    chg.click(
                        update_chg,
                        inputs=[arval],
                        outputs=imgres
                    )
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
