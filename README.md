<h1>RasPin</h1>
<span style="color:#4E342E;font-size:17px">Raspberry Pi Pins Control , Easy Access for Beginners use.</span><br>
<hr style="width:50%;margin-left:0px">
<pre>
 __________________________________________________________ 
|  RRRRR                         PPPPP                     |
|  R    R                        P    P   ii               |
|  R     R   aaaaa      ssssss   P     P       n nnnnnn    |
|  R    R   a     a    s         P    p   ii   nn      nn  |
|  RRRRR   a       a    ssssss   PPPPP    ii   n        n  |
|  R    R   a     aa          s  P        ii   n        n  |
|  R     R   aaaaa aa   ssssss   P        ii   n        n  |
|__________________________________________________________|
|                                                          |
|         All Rights Reserved © 2017 SaeedEY.com           |
|  RasPin is an Open Source Script to Provide You an Easy  |
|  Access to your RaspberryPi Pins Just to send out Power  |
|  from Specified Pin.                                     |
|                                                          |
|  details:                                                |
|          Version: 1                                      |
|          Last Modify: 11/April/2017                      |
|  Find Me@:                                               |
|          https://SaeedEY.com                             |
|          https://github.com/SaeedEY                      |
|  USAGE:                                                  |
|          python Pins [PinNumber] on/off/r [sleep/s]      |
|  ValidPinsNumber:                                        |
|        [3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,26,  |
|         29,31,32,33,35,37,38,40]                         |
|__________________________________________________________|

</pre>
<h2>Introduce</h2>
Easy access to <b>RaspberryPi's</b> Pins just with <i><a href='#use'>Calling</a></i> the script.<br>
It could control all the <b><a href='#pins'>PossiblePins</a></b> in your gadget.<br>
The RasPin has Written in <i><b>Python</b> Programming Language.</i><br>
<h2>Notice</h2>
It has too many Bugs And i didnt fix them , so apologize me.<br>
<b>do not try to <i>Find</i> and <i>Fix</i> the Bugs , unless you are genius Programmer , because it could Harm your Device hardly</b><br>
<h2>Usage</h2>
[!] - For using this Script:<ul>
<li> You must have Installed <b><i><a href='https://www.python.org/downloads/'>Python3</a></i></b>.</li><br>
<li> You must have Providing a <b><i><a href='https://www.raspberrypi.org/products/raspberry-pi-3-model-b/'>RaspberryPi</a></i></b> [GPIO support series].</li><br>
<li> You may need <b><i><a href='https://en.wikipedia.org/wiki/Breadboard'>BreadBoard</a></i></b> Electronic Boards.</li><br>
<li> You may need <b><i><a href='https://www.adafruit.com/category/469'>Male/Female</a></i></b> Electronic Connectors.</li>
</ul>
<h4 id='use'>How To Use:</h4>
<ol>
<li>Open Console in Raspberry Pi OS</li>
<li>Run Command: <i>Python Pins.py [Port] [on/off/r] [sleep/s]</i></li>
</ol>
<h5>OR</h5>
<ol>
<li>Open Console in Raspberry Pi OS</li>
<li>Run Command: <i>Python Pins.py</i></li>
</ol>
<hr style='width:40%;margin-left:0px'>
<ul>
<li><b>[Port]</b> => one of <a href='#pins'><b>Available Port</b></a>.</li><li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if port == <b><i>0</i></b>, it would do action for all Ports.</li>
<li><b>[On/Off/R]</b> => it do | ON <small>or</small> OFF <small>or</small> RESET | action.</li>
<li><b>[Sleep/]</b> => this was delay befor start Action | SLEEP | as second .</li>
<li>exmple :  <b>python Pins.py 3 on 1</b> <small>means: "Turn on port 3 after 1 second"</small></li>
<li>exmple :  <b>python Pins.py 0 on 1</b> <small>means: "Turn on all the ports after 1 second"</small></li>
<li>exmple :  <b>python Pins.py 0 r 0</b> <small>means: "Reset the pins after 0 second"</small></li>
<li>exmple :  <b>python Pins.py 0 on 10</b> <small>means: "Turn on all the pins after 10 second"</small></li>
</ul>
<h2 id='pins'>Avalable Pins</h2>
<img src='http://saeedey.com/images/pi3_gpio.png'  style='width:350px'/><br>
AND These Pins Can Use as your +/Possitive port (the green ones):<br>
<ul><li>3</li>
<li>5</li>
<li>7</li>
<li>8</li>
<li>10</li>
<li>11</li>
<li>12</li>
<li>13</li>
<li>15</li>
<li>16</li>
<li>18</li>
<li>19</li>
<li>21</li>
<li>22</li>
<li>23</li>
<li>24</li>
<li>26</li>
<li>29</li>
<li>31</li>
<li>32</li>
<li>33</li>
<li>35</li>
<li>36</li>
<li>37</li>
<li>38</li>
<li>40</li>
(know more at <a href='https://www.raspberrypi.org/documentation/usage/gpio/'>here</a>)
</ul>
