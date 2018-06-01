﻿<h1>Emotion Synthesis</h1>
<h2>Intelligent Interactive Systems - Uppsala University</h2>

<img src="https://i.imgur.com/vaEwpcK.png" width=500px>

<h3>Group Members</h3>
<ul>
    <li>Christina Bremer</li>
    <li>Mauro José Pappaterra</li>
    <li>Hassam Odimi</li>
    <li>Amanda Larruy Bergqvist</li>
</ul>

<hr>
<h3>Video Demonstration</h3>
<a href="https://www.youtube.com/watch?v=y0tf02Du5eE&feature=youtu.be"><img src="https://i.imgur.com/jUZb4OC.png" width=1000px> </a>
<h4>Click on the thumbnail to play the Demo video for irisTK agent implementation</h4>
<hr>
<h3 id="help">General Instructions to run the programs</h3>
-Clone or download this repository<br>
-To run these programs in your computer you need to <a href="https://www.python.org/downloads/">download and install Python 3.</a><br>
-To execute from the command line on a Ms Windows system you need to <a href="https://docs.python.org/2/using/windows.html">add Python and Pip to the PATH environmental variable.</a><br>
-Do not hesitate to contact me if you have any problems running these programs or if you find any bugs!

<h3 id="help">Instructions for video emotion synthesis </h3>
-The video-based emotion synthesis can be found inside the <i>video</i> folder<br>
-Install <a href="https://opencv.org/">OpenCV</a> and <a href="http://www.numpy.org/">Numpy</a> Python libraries. You can do this by opening a terminal and executing: <br>
&nbsp &nbsp &nbsp <code>> pip install numpy opencv-python </code> <br>
-Follow the instructions below to execute <i>emotion_sysnthesis.py</i>

<h3 id="help">Instructions for iristk (virtual agent) emotion synthesis </h3>
-The iristk virtual-agent-based emotion synthesis can be found inside the <i>iristk</i> folder <br>
-On your Iristtk installation modify the emotions .xml file by appending the contents of the file new_gestures.xml. Make sure you paste the contents of the file between the xml tags <'gestures><'/gestures> <br>
-Run the Iristk Java Server on Eclipse or similar SDK. <br>
-Follow the instructions below to execute <i>furnet.py</i> (notice that this file has been modified from the original version)<br>

<h3 id="help">General Instructions to execute the Python scripts</h3>
<h4>From the command line:</h4>
1. Open a terminal <br>
2. Navigate to the folder where the files are located <br>
3. On the command line execute: <br>
&nbsp &nbsp &nbsp <code>> python3 <i>script</i>.py </code> <br>
&nbsp &nbsp &nbsp <b>Notice: Replace <i>script</i> with the name of the file you want to execute e.g. furnet.py</b> <br>

<h4>From the Python interpreter:</h4>
1. Open Python <br>
2. On the prompt execute: <br>
&nbsp &nbsp &nbsp <code>> exec(open("<i>path</i>/<i>script</i>.py").read())</code> <br>
&nbsp &nbsp &nbsp <b>Notice: Replace <i>path</i> with the local path to the folder that contains the script you want to execute</b> <br>
&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp<b>Replace <i>script</i> with the name of the file you want to execute e.g. PancakeFlipper.py</b> <br>