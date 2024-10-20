# sd-webui-aspect_ratios-dd Version 0.0.0.6 
#### Extension for the AUTOMATIC1111 Web UI

<p align="justify">sd-webui-aspect_ratios-dd is an <i>Extension</i> for the <a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui">AUTOMATIC1111</a>, which is adding the new functionality for the selection of predefined or user defined <i>aspect ratios</i> to the AUTOMATIC1111 web UI.</p>

---

## Preface

<p align="justify">After writing my first <i>Extension</i> the realisation of this <i>Extension</i> was a little bit more complicated. I had a steep learning curve while programming using <i>gradio</i>. At the end of the day everything works as expected.</p>

<p align="justify">This will be the last version I have programmed for the time being. It fulfils its purpose and can be adapted to personal requirements. Maintenance and bug fixing are not affected by this statement.</p>

---

## Motivation

<p align="justify">The <i>aspect ratio</i> plays a crucial role when dealing with images. This statement is correct in relation to the paintings of the middle ages, pictures by photographers and in AI image creation as well.</p>
   
<p align="justify">While using AUTOMATIC1111 I missed a tool selecting the common <i>aspect ratios</i>. The tools I found did not fulfil my needs. This <i>Extension</i> is the attempt to provide a quick access to suitable <i>aspect ratios</i>.</p>

## Goal

<p align="justify">The tool should be as simple as possible and at the same time provide all the necessary information.</p>


## What the Extension Does

After installation, you will find a panel in the AUTOMATIC1111 web UI that looks like the following image when opened.

<a target="_blank" href=""><img src="./images/drop_down_panel_new.png" alt="button panel"></a>

<p align="justify">To keep the handling of the <i>Extension</i> simple I decided, that I focus on <i>aspect ratios</i> of the orientation landscape. Orientation portrait can be accessed by a change of the orientation.</p>

## Explanation

<p align="justify">The tool should be as simple as possible and at the same time provide all the necessary information. A drop-down menu allows you to select a predefined <i>aspect ratio</i> from a large number of <i>aspect ratios</i>. Using the button <code>Apply</code>, the Width and Height are calculated from the given <i>aspect ratio</i> and taken over in the main UI. A <code>Reset</code> button is resetting the <i>Aspect Ratio</i> back to 1:1 and Width and Height back to 512. The orientation can be switched by the button <code>Change Orientation</code>. An additional information is available if the calculation of the new resolution is exact or if one value is a rounded number. The resolution can be checked in the terminal window. Th used aspect ratio data file is noted ist the last line.</p>

## Calculation of Width and Height

<p align="justify">Depending on the orientation Width or Height is set to 512 pixel.</p>

<pre>
   Width = 512 pixel
   Height = Width * Aspect Ratio (as quotient) in pixel
</pre>

<pre>
   Height = 512 pixel
   Width = Height * Aspect Ratio (as quotient) in pixel
</pre>

<p align="justify">The first value is all the time set to 512. The second and calculated value is an integer or an floating point number. Both values are printed into the terminal window and can be checked there.</p>

## Implemented Aspect Ratios

<p align="justify">The given <i>Aspect Ratios</i> are basically sorted into two blocks. First come the <i>Aspect Ratios</i> with integer numbers and then the <i>Aspect Ratios</i> with floating point numbers.</p>

* 1:1
* 1.5:1
* 2:1
* 3:1
* 3:2
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
* 8:3
* 8:5
* 9:7
* 10:1
* 10:7
* 11:5
* 11.85:3
* 12:1
* 12:5
* 12:9
* 12:10
* 13:6
* 13:18
* 13:19
* 14:9
* 14:11
* 15:8
* 15:9
* 15:10
* 16:9
* 16:10
* 17:9
* 18:5
* 18:9
* 18.5:9
* 18:10
* 19:9
* 19.5:9
* 20:9
* 21:9
* 21.5:9
* 22:9
* 22:17
* 24:9
* 25:16
* 28:13
* 32:9
* 32:25
* 35:26
* 36:10
* 37:18
* 37:20
* 40:21
* 43:18
* 45:35
* 47:20
* 51:20
* 55:23
* 64:27
* 69:25
* 70:27
* 79:20
* 128:75
* 192:145
* 239:100
* 256:135
* 300:157
* 540:283
* 1.19:1
* 1.20:1
* 1.25:1
* 1.27:1
* 1.30:1
* 1.33:1
* 1.37:1
* 1.375:1
* 1.38:1
* 1.40:1
* 1.41:1
* 1.4142:1
* 1.43:1
* 1.54:1
* 1.55:1
* 1.59:1
* 1.60:1
* 1.618:1
* 1.66:1
* 1.75:1
* 1.77:1
* 1.78:1
* 1.85:1
* 1.875:1
* 1.896:1
* 1.90:1
* 1.91:1
* 2.125:1
* 2.16:1
* 2.165:1
* 2.20:1
* 2.208:1
* 2.21:1
* 2.35:1
* 2.37:1
* 2.38:1
* 2.39:1
* 2.40:1
* 2.44:1
* 2.55:1
* 2.59:1
* 2.66:1
* 2.75:1
* 2.76:1
* 3.2:1
* 3.55:1
* 3.58:1
* 3.60:1
* 3.95:1

## Origin of the Aspect Ratios

<p align="justify">Aspect ratios are a recurring theme for a photographer. Whenever I come across an aspect ratio that I don't know yet, I make a note of it.</p> 

<p align="justify">Since it makes no sense to cite the sources, I will refrain from doing so. Most of the listed page ratios can be verified via an internet search.</p> 

## User Data

<p align="justify">It is intended that the user can set aspect ratios of his own choice. This can be explained looking at the tree structure of the <i>Extension</i>.</p> 

```bash
    ├── stable-diffusion-webui
    └── extensions
        └── sd-webui-aspect_ratios-dd
            ├── json
            ├── images
            ├── scripts
            ├── extension_data
            │   └── aspect_ratio.data
            └── user_data
                 └── aspect_ratio.data
```

<p align="justify">If the file aspect_ratio.data in the user_data directory exists, this file is used as the source for the drop-down menu data. Otherwise the file aspect_ratio.data in the extension_data directory is used.</p> 

## Support Request 

<p align="justify">If there are <i>aspect ratios</i> in the <i>Extension</i> that I do not yet consider, but which were or are common, please let me know about them, that I can take them into account and that I can add them to the predefined list.</p>  

## To-Do

<p align="justify">Improvement of this documentation.</p>    

## Known Problems

<p align="justify">No problems known yet.</p>

## Development and Test Environment

<p align="justify">The <i>Extension</i> was devolped and tested on a machine with a Debian based Linux distribution istalled using the web UI AUTOMATIC111 with following specification:</p>

* API: v1.10.0
* Python: 3.10.14
* torch: 2.1.2+cu121
* xformers: 0.0.23.post1
* gradio: 3.41.2

## Points of Criticism AUTOMATIC1111

<p align="justify">AUTOMATIC1111 uses Gradio to programme the web interface. The Gradio used is extremely buggy and outdated. Currently local version 5.0.1 is installed, AUTOMATIC1111 uses 3.41.2. In forum posts it can be read that the outdated version is given priority over an adaptation. This does not really motivate users to programme extensions.</p>

# References

[1] https://github.com/AUTOMATIC1111/stable-diffusion-webui

[2] https://github.com/AUTOMATIC1111/stable-diffusion-webui-extensions

[3] https://www.gradio.app/docs/gradio/interface
