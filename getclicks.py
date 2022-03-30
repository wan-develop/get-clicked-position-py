import pyautogui as pg
import mouse
import time
import json

class GetClicks:

    def __init__(self, clicks: list, save_file: bool =True,custom_dir:str = "", file_name: str = "clicks_config"):
        '''
            clicks -> is a list with all positions needed
            save_file -> if you want to save in a file or just get the raw text
            file_name -> you can change this to give the file a custom name
        '''
        self.clicks = clicks
        self.save_file = save_file
        self.file_name = file_name
        self.custom_dir = custom_dir
    
    def _get_click_position(self):
        """
        returns a truple with (x,y) mouse position when
        the mouse left button is pressed
        """
        while not mouse.is_pressed("left"):
            #wait the user clicks
            pass

        time.sleep(0.2) # this delay avoid the first click to be saved into all positions

        return mouse.get_position()



    def _get_clicks(self):
        """
        returns a python dict with all positions

        exemple: 
        ...
            {
                'button_exemple': (322, 1230),
            }
        ... 
        """
        if len(self.clicks) <= 0: return

        result_object = {}

        for click_name in self.clicks:
            print(f"click on {click_name} position.")
            result_object[click_name] = self._get_click_position()

        #print(result_object)

        return result_object


    def init(self):
        """
            if -> save_file is True the class will generate a json file in 
                  the same directory with all positions.
            
            else -> it will return a string in json format
        """

        json_file = json.dumps(self._get_clicks())

        
        if self.save_file:
            with open(self.custom_dir + self.file_name+".json", 'w') as file:
                file.write(json_file)
        else:
            return json_file


if __name__ == "__main__":

    test = GetClicks(["main","nextButton"])
    test.init()