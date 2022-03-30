# autoclicker_py

## getclicks.py
 > This class generate a `json` file that store all your clicks coordinates, because computers has different screen size.
 > it's userful when developing bots or automation programs.


## How to use this class
 
 > This class is easy to use, you just need to specify the list of positions name you want to use
 
 ### Import
 ```
 from getclicks import GetClicks
 ```
 
 ### Exemple:
 ```
 my_positions: list = ["text_input", "confirm_button", "ok_button", "exit_button"]
 
 getclicks = GetClicks(clicks= my_positions, file_name="my_positions")
 
 ```
 ### Generating the json:
 
 ```
 getclicks.init()
 ```
 
 ### Then:
 > This init method will create a `json` file in the class directory, you can change the default directory:
 
 ### How to change the output directory:
 _The class has a parameter named: `custom_dir` it default value is a empty string, but as the name suggests you may need to change:_
 
 ```
 my_dir: str = "C:/pythonProjects/my_directory/"
 getclicks = GetClicks(clicks= my_positions, file_name="my_positions", custom_dir= my_dir)
 ```
 
 
