
# sd-webui-aspect_ratios-dd Version 0.0.0.6 
#### Extension for the AUTOMATIC1111 Web UI

<p align="justify">sd-webui-aspect_ratios-dd is an <i>Extension</i> for the <a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui">AUTOMATIC1111/stable-diffusion-webui</a>, which is adding the new functionality to the AUTOMATIC1111 web UI to select predefined or userdefeind aspect ratios.<i>aspect ratios</i>.</p>

---

## Preface

<p align="justify">After writing my first <i>Extension</i> the realisation of this <i>Extension</i> was a little bit more complicated. 
But I had a steep learning curve in <i>gradio</i> programming. But it works as expected at the end of the day.</p>

## Motivation

<p align="justify">This statement is correct in relation to the painters of the Middle Ages, pictures by photographers and in AI image creation as well.</p>

<p align="justify">This statement is correct in relation to the painters of the Middle Ages, pictures by photographers and in AI image creation as well. The <i>Extensions</i> I found did not fulfil their purpose. So this is an attempt to provide quick access to suitable <i>Aspect Ratios</i>.</p>

## Explanation

<p align="justify">The tool should be as simple as possible and at the same time provide all the necessary information. Via a dropdown menu one can select a predefined <i>Aspect Ratio</i>. Using the button Apply, The Width and Height are calculated and taken over in the main UI. A Reset button is resetting the <i>Aspect Ratio</i> back to 1:1 and Width and Height back to 512. The orientation can be switched by the button Change Orientation. An additional information is available if the calculation of the new resolution is exact or if one value is a rounded number. The resolution can be checked in the terminal window.</p>

## Implemented Aspect Ratios

<p align="justify">The given <i>Aspect Ratios</i> are basically sorted into two blocks. First come the <i>Aspect Ratios</i> with integer numbers and then the <i>Aspect Ratios</i> with floating point numbers.</p>

* 1:1
* 1.5:1
* 2:1
* 2.4:1
* 3:1
* 3:2
* 3.2:1
* 3.6:1
* 4:1
* 4:3
* 5:1
* 5:3
* 5:4
* 6:1
* 6:5
* 7:1
* 7:4
* 7:5
* 7:5.5
* 8:5
* 9:16
* 10:12
* 11:5
* 12:5
* 13:18
* 13:19
* 14:9
* 15:9
* 16:9
* 16:10
* 17:22
* 18:5
* 18:9
* 18.5:9
* 19.5:9
* 20:9
* 21:9
* 22:9
* 32:9
* 36:10
* 45:35
* 55:23
* 64:27
* 69:25
* 239:100
* 256:135
* 1.19:1
* 1.25:1
* 1.3:1
* 1.33:1
* 1.37:1
* 1.375:1
* 1.40:1
* 1.41:1
* 1.43:1
* 1.54:1
* 1.59:1
* 1.6:1
* 1.618:1
* 1.66:1
* 1.75:1
* 1.77:1
* 1.78:1
* 1.85:1
* 1.875:1
* 2.125
* 2.16:1
* 2.20:1
* 2.21:1
* 2.35:1
* 2.37:1
* 2.38:1
* 2.39:1
* 2.40:1
* 2.66:1
* 2.75:1
* 2.76:1
* 3.55:1
* 3.58:1

# Calculation of Width and Height

<p align="justify">Depending on the orientation is Width or Height set to 512 pixel.</p>

<pre>
   Width = 512 pixel
   Height = Width * Aspect Ratio
</pre>

<pre>
   Height = 512 pixel
   Width = Height * Aspect Ratio
</pre>

<p align="justify">The second and calculated value is an integer or an floating point number.</p>

<p align="justify">Both values are printed into the terminal window and can be checked there.</p>

# Support Request 

<p align="justify">If there are aspect ratios in the extension that I do not yet know, but which were or are common, please let me know so that I can take them into account.</p>  

# To-Do

<p align="justify">Improvement of this documentation. Aspect ratios of interest from a text file should be used for the dropdown menu. Maintenance of the aspect ratios of interest is then easier for me. And the user can customise the file to suit their own needs.</p>   

<p align="justify">Write a tool that takes into account the fact that the calculation of <code>Width</code> or <code>Height</code> can be a floating point number.</p>   

# References

[1] https://github.com/AUTOMATIC1111/stable-diffusion-webui

[2] https://github.com/AUTOMATIC1111/stable-diffusion-webui-extensions
