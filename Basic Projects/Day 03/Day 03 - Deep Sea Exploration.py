#!/usr/bin/env python
# coding: utf-8

# In[ ]:


logo = '''
                                            W E L C O M E
                                                to the
         _____     ______     ______     ______         ______     ______     ______                               
        /\  __-.  /\  ___\   /\  ___\   /\  == \       /\  ___\   /\  ___\   /\  __ \                          
        \ \ \/\ \ \ \  __\   \ \  __\   \ \  _-/       \ \___  \  \ \  __\   \ \  __ \                             
         \ \____-  \ \_____\  \ \_____\  \ \_\          \/\_____\  \ \_____\  \ \_\ \_\                          
          \/____/   \/_____/   \/_____/   \/_/           \/_____/   \/_____/   \/_/\/_/                         
                                                                                                                     
 ______     __  __     ______   __         ______     ______     ______    ______   __     ______     __   __     
/\  ___\   /\_\_\_\   /\  == \ /\ \       /\  __ \   /\  == \   /\  __ \  /\__  _\ /\ \   /\  __ \   /\ "-.\ \       
\ \  __\   \/_/\_\/_  \ \  _-/ \ \ \____  \ \ \/\ \  \ \  __<   \ \  __ \ \/_/\ \/ \ \ \  \ \ \/\ \  \ \ \-.  \  
 \ \_____\   /\_\/\_\  \ \_\    \ \_____\  \ \_____\  \ \_\ \_\  \ \_\ \_\   \ \_\  \ \_\  \ \_____\  \ \_\\"\_\    
  \/_____/   \/_/\/_/   \/_/     \/_____/   \/_____/   \/_/ /_/   \/_/\/_/    \/_/   \/_/   \/_____/   \/_/ \/_/  
                                     
'''


# In[ ]:


print(logo)
print("Your mission is to find the lost treasure from a ship that sank 200 years ago.") 

direc = input('You\'re on a boat in the middle of the ocean. Do you want to "dive" or "stay" on the boat? \n')
if direc.lower() == 'stay':
    print('There was a leak in the boat - it sinks. Game over!')
else:
    cave = input('You\'ve descended into the depths. You see a cave ahead. Type "enter" to explore the cave. Type "swim" to continue swimming forward. \n')
    if cave.lower() == 'swim':
        print('You get attacked by a great white shark. Game Over!')
    else:
        paths = input('You enter the cave and see two paths. One is narrow and dark, the other is wide and well-lit. Do you choose the "narrow" path or the "wide" path? \n')
        if paths.lower() == 'narrow':
            print('You get lost in a dark maze. Game Over!')
        else:
            treasure = input('You navigate through the wide path and discover three underwater temples: one made of coral, one of crystal and one of pearls. Which temple do you explore? Type "coral", "crystal" or "pearls". \n')
            if treasure.lower() == 'coral':
                print('The coral temple is filled with sea urchins. Game Over!')
            elif treasure.lower() == 'crystal':
                print('The crystal temple collapses around you. Game Over!')
            elif treasure.lower() == 'pearls':
                print('You\'ve found the lost treasure - mission successful! You Win!')

