# automatic-tank-gauging
Modbus protocol communication using Haiwell SCADA


This chapter is about the gerenal procedure.

General procedures of project development

Step one： Double click the develop icon.

Step two：Click “Create a new project”，and confirm the project settings.

Step three：Expand the plc node and find the plc node,do the settings and then click “Add”.

Step four：Choose “Yes” in the reminder window to add the variable.

Step five： There is a default mian picture when create a new project,here we can edit on the main  picture directly,the image element can be dragged to the main picture window and do the settings.

Step Six：Click the “Compile” in the toolbars,the user will see a pop-up window of saving project,save project to target place. Close the Compile window after checking that there is no error or warning. Click the “Simulation run”of the toolbar and enter the Designer running environment to run the project.

Tips：There are two forms of simulation tools, which are divided into [online simulation] and [offline simulation].

(1) Online simulation: Online simulation needs to be connected to the PLC, and the PC running end functions as a touch screen, which can control the PLC. Click the [Online Simulation] tool in the toolbar，a registration prompt box pops up, click [No Registration] to enter the operating environment and run the project.

(2)Offline simulation: Offline simulation does not need to be connected to the PLC, and the operating environment is equivalent to a simulation device. Click the [Offline Simulation] tool in the toolbar，a registration prompt box pops up, click [No Registration] to enter the operating environment and run the project.

Step one：Open software 

Double click the develop icon：



Figure-- Start page

Step two：New project 

Click “Create a new Project”，and confirm the project settings.

    

Figure-- Project property  

1. Input the Unamed project in the “project name”.

Set other attributes parameters as default value.About the project property parameter,refer to  the chapter of " Project management——New project——Project property ".


Step three：Add device 

Expand the plc node and find the plc node,do the settings and then click “Add” button. 

  

Figure-- Add device 

1. Input " PLC_1" in the "device name". 

Set other attributes parameters as default value.About the device property parameter,refer to  the chapter of “Device configuration and management——Device configure——Device property ”. 

Step four：Add Variable  

Chose “Yes” in the reminder window to add the variable. 

   

Figure-- Add variable  

1、Choose the “Y (digital output)” in the "Register type" ,keep other parameters as default. 

2、Choose the “Y (digital output)” in the "Register type" ,keep other parameters as default. 

3、Choose the “AQ (Analog output)” in the "Register type" ,keep other parameters as default.   

Set other attributes parameters as default value.About the variable property parameter,refer to  the chapter of “Variables configuration and management——Configurre the variables——Variable configration”. 

Step five：Add and edit picture 

  There is a default main picture when create a new project,here we can edit on the main picture directly,the image element can be dragged to the main picture window and do the settings. 

1.Add "value display input" primitive 

(1) Click [Function Element] in the gallery to find the "Value Display Input" graphic element, drag it to the screen window and release the left mouse button at a suitable position;

(2) Select the primitive, right-click, and click [Properties] to pop up the property setting window of the "Value Display Input" primitive;

(3) Click the button at [Read Variable] , a variable selector pops up, select "AQ0", and click [OK];

(4) Check the [Input] box and enter "Maximum Value", "Minimum Value", "Integer Digits", "Decimal Digits".

The other attribute parameters of "Numerical Display Input" are set to the default values and will not be modified. As shown below: 

 

Figure Add value to display input primitives 

Related topic：How to display input primitives with numerical values? 

2.Add "switch 1" primitive 

(1)Click the [switch] in the gallery to find the "switch 1" element, drag it to the screen window and release the left mouse button at the appropriate position; 

(2)Slect the primitive, right-click, and click [Properties] to pop up the property setting window of the "Switch 1" primitive;

(3)Click the button at [Write Variable], a variable selector pops up, select "Y0", and click [OK].

The other attribute parameters of "Switch 1" are set to default values, and they are not modified. As shown below: 

  

Figure Add switch 1 element   

Related Topic：How to use switch primitives? 

3.Add the "indicator 1" picture element

(1)Click the [indicator] in the gallery to find the "indicator 1" picture element, drag it to the picture window and release the left mouse button at the appropriate position; 

(2)Select the picture element, right-click and click [Properties], the property setting window of the "indicator 1" picture element will pop up;

(3)Click the button at [Read Variable], a variable selector pops up, select "Y0", and click [OK].

The other attribute parameters of "Indicator 1" are set to the default values and will not be modified. As shown below:

  

Figure Add indicator 1 pixel 

Related Topic：How to use indicator primitives? 

4.Add the "Valve 1" graphic element

(1)Click [Valve] in the gallery to find the "Valve 1" graphic element, drag it to the picture window and release the left mouse button at the appropriate position;

(2)Select the primitive, right-click, and click [Properties] to pop up the "valve 1" primitive attribute setting window;

(3)Click the button at [Write Variable], a variable selector pops up, select "Y0", and click [OK].

The other attribute parameters of "Valve 1" are set to the default values and will not be modified. As shown below:

  

Figure Add valve 1 element 

5.Add "Reactor 2" graphic element

(1)Click [Tank] in the gallery to find the "Reactor 2" primitive, drag it to the picture window and release the left mouse button at a suitable position; 

(2)Select the primitive, right-click, and click [Properties] to pop up the property setting window of the "Reactor 2" primitive; 

(3)Click the button at [Read Variable], a variable selector pops up, select "AQ0", and click [OK]; 

(4)Input "maximum value" and "minimum value". 

The other attribute parameters of "Reactor 2" are set to the default values and will not be modified. As shown below:

  

Figure Add Reactor 2 Graph 

6.Add "blade 1" primitive

(1)Click [Motor·Fan Leaf] in the gallery to find the "Fan Leaf 1" primitive, drag it to the picture window and release the left mouse button at a suitable position;

(2)Select the primitive, right-click, and click [Properties] to pop up the property setting window of the "Fan Ye 1" primitive;

(3)Click to select "Start Rotation", click the button at [Rotation Variable], a variable selector pops up, select "Y0", and click [OK].

The other attribute parameters of "Fan Leaf 1" are set to the default values and will not be modified. As shown below: 

  

Figure Add fan blade 1 primitive 

7.Add "real-time trend" primitive

(1) Click [Advanced Controls ] in the gallery to find the "real-time trend" graphic element, drag it to the picture window and release the left mouse button at a suitable position;

(2)Open the variable manager in the project browser and set the input range of the variable that needs to be added to the real-time curve (ie, the maximum and minimum values);

(3)Select the primitive, right-click, and click [Properties] to pop up the property setting window of the "real-time trend" primitive;

(4)Click the [Edit Collection] button to pop up the collection editor, click the [Add] button to add a collection member; 

(5)Click the button at the member variable to open the variable selector, select "AQ0", and click [OK]. 

The other property parameters of the "real-time trend" are set to default values, and they are not modified. As shown below:

  

Figure Add real-time trend curve primitive 

Related topic: How to configure real-time trend? 

8.Add "instrument 1" graphic element

(1) Click [Instrument·Cursor] in the gallery to find the "Instrument 1" graphic element, drag it to the screen window and release the left mouse button at a suitable position;

(2) Select the graphic element, right-click, and click [Properties] to pop up the property setting window of the "Instrument 1" graphic element;

(3) Click the button at [Read Variable], a variable selector pops up, select "AQ0", and click [OK].

The other attribute parameters of "Instrument 1" are set to the default values and will not be modified. As shown below:

  

Figure Add meter 1 element 

Related topic:How to edit the attributes of elements in the element library?

Related topic:Screen configuration and properties?

Step six: Debugging and running 

Click the “Compile” in the toolbars,the user will see a pop-up window of saving project,save project to target place. Close the "Compile" window after checking that there is no error or warning. Click the “Simulation run” of the toolbar and enter the configuration software running environment to run the project.



Figure-- Compile




Figure-- Project running

1、Click the Style switch 2” and you will find that the "switch button1" and "indicator 5" changes while clicking.

2、Click the “New analog button 1” and decrease button",and you will find that the "instrument 2" and"Real-time curve" changes while clicking.
