# import serial

# arduino = serial.Serial(port='/dev/ttyACM1', baudrate=9600)
# # # # # import pygame

# # # # # # Initialize Pygame
# # # # # def controller():
# # # # #     pygame.init()

# # # # #     # Initialize the joysticks
# # # # #     pygame.joystick.init()

# # # # #     # Get the first joystick
# # # # #     joystick = pygame.joystick.Joystick(0)
# # # # #     joystick.init()

# # # # #     right_trigger_pressed = False
# # # # #     left_trigger_pressed = False
# # # # #     up_pressed=False

# # # # #     # Run the game loop
# # # # #     running = True
# # # # #     while running:
# # # # #         for event in pygame.event.get():
# # # # #             if event.type == pygame.QUIT:
# # # # #                 running = False
# # # # #             # Check if the A button is pressed
# # # # #             if event.type == pygame.JOYBUTTONDOWN and event.button == 0:
# # # # #                 arm('I')
# # # # #             if event.type == pygame.JOYBUTTONDOWN and event.button == 1:
# # # # #                 arm('H')
# # # # #             if event.type == pygame.JOYBUTTONDOWN and event.button == 2:
# # # # #                 arm('G')
# # # # #             if event.type == pygame.JOYBUTTONDOWN and event.button == 3:
# # # # #                 arm('J')
# # # # #             if event.type == pygame.JOYBUTTONDOWN and event.button == 4:
# # # # #                 arm('C')
# # # # #             if event.type == pygame.JOYBUTTONDOWN and event.button == 5:
# # # # #                 arm('D')
# # # # #             if event.type == pygame.JOYBUTTONDOWN and event.button == 6:
# # # # #                 arm('E')
# # # # #             if event.type == pygame.JOYBUTTONDOWN and event.button == 7:
# # # # #                 arm('F')
# # # # #             if event.type == pygame.JOYBUTTONDOWN and event.button == 8:
# # # # #                 arm('K')
# # # # #             if event.type == pygame.JOYBUTTONDOWN and event.button == 9:
# # # # #                 arm('L')
            
# # # # #             right_trigger = joystick.get_axis(5)
# # # # #             if right_trigger > 0.5 and not right_trigger_pressed:
# # # # #                 arm('B')
# # # # #                 right_trigger_pressed = True
# # # # #             elif right_trigger <= 0.5:
# # # # #                 right_trigger_pressed = False
# # # # #             left_trigger = joystick.get_axis(4)
# # # # #             if left_trigger > 0.5 and not left_trigger_pressed:
# # # # #                 arm('A')
# # # # #                 left_trigger_pressed = True
# # # # #             elif left_trigger <= 0.5:
# # # # #                 left_trigger_pressed = False
            
# # # # #             hat = joystick.get_hat(0)
# # # # #             if hat[1] == 1 and not up_pressed:
# # # # #                 arm('X')
# # # # #                 up_pressed = True
# # # # #             elif hat == (0, 0):
# # # # #                  up_pressed = False
# # # # #     # Quit Pygame
# # # # #     pygame.quit()


# def arm(var):
#     if (var == 'A'):  # if the value is f
#         print("m1-forward")
#     if (var == 'S'):  # if the value is b
#         print("m1-backward")
#     if (var == 'D'):  # if the value is l
#         print("m2-forward")
#     if (var == 'F'):  # if the value is r
#         print("m2-backward")
# #     if (var == 'E'):  # if the value is s
# #         print("m3-forward")
# #     if (var == 'F'):
# #         print("m3-backward")
# #     if (var == 'G'):
# #         print("m4-forward")
# #     if (var == 'H'):
# #         print("m4-backward")
# #     if (var == 'I'):
# #         print("m5-forward")
# #     if (var == 'J'):
# #         print("m5-backward")
# #     if (var == 'K'):
# #         print("m6-forward")
# #     if (var == 'L'):
# #         print("m6-backward")   
# #     if (var == 'X'):
# #         print("stop")
#     arduino.write(str.encode(var))
