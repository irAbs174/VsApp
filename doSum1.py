import time
from datetime import datetime as dt


class DoApp:


        def App(self):
            print(str(dt.now()) +'\n' +'Welcome to DoSUM !'
            +'\n' +'V 0.0.1 Beta' +'\n' +'for help: Help()')
            while self :
                DoApp.DoWork(input('Enter Task: '))
                time.sleep(.174)


        def DoWork(self):
            if str(self) == 'Help()':
                DoApp.Help(True)
            elif str(self).isnumeric():
                for xs in range(1, int(self) + 1 , 1):
                    if xs < int(self) + 1:
                        
                        xs += 1
                        if xs > int(self):
                            print('end')
            else:
                return print('Error : ------------- number not valid -------------'
                + '\n' + "Please enter number bigerthan ziro and number can't be empty space"
                )
        

        def Help(self):
            if self:
                print('seucces')


DoApp.App(True)