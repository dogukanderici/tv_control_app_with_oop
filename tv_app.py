import random
import time


# we created RemoteControl Class
class RemoteControl():

    def __init__(self, tv_state="Off", tv_vol=0, channel_list=["trt"], channel="trt"):

        self.tv_state = tv_state
        self.tv_vol = tv_vol
        self.channel_list = channel_list
        self.channel = channel

    # It controls the state of tv.
    def tv_open(self):

        if (self.tv_state == "open"):

            print("Tv is already open.")

        else:

            self.tv_state = "open"
            print("Tv is starting...")
            time.sleep(1)
            print("Tv was opened.. Have a good day..")

    def tv_close(self):

        if (self.tv_state == "off"):

            print("Tv is already off.")

        else:

            self.tv_state = "off"
            print("Tv is shutting down...")
            time.sleep(1)
            print("Tv turned off..")

    # This method configures the tv volume level.
    def vol_config(self):

        while True:

            input1 = input("Vol Up: '>'\nVol Down: '<'\nQuit: 'Q'")
            if (input1 == "<"):

                if (self.tv_vol != 0):
                    self.tv_vol -= 2
                    print("Volume: ", self.tv_vol)
            elif (input1 == ">"):

                if (self.tv_vol != 32):
                    self.tv_vol += 2
                    print("Volume: ", self.tv_vol)
            else:

                print("Volume settings updated...", self.tv_vol)
                break

    # This method adds a new channel to channel list.
    def channel_add(self, new_ch):

        print("New channel is adding..")
        time.sleep(1)
        # The program wait for it to be more realistic.
        self.channel_list.append(new_ch)
        print("New channel added....")

    # This methdd chooses random channel form channel list.
    def random_channel(self):

        rnd = random.randint(0, len(self.channel_list) - 1)
        self.channel = self.channel_list[rnd]
        print("Channel watched: ", self.channel)

    # We modified the length method at our own request. where the length method will return the length of the channel list.
    def __len__(self):

        return len(self.channel_list)

    # We modified this method to see the tv status.
    def __str__(self):

        return "Tv State: {}\nTv Vol: {}\nChannel List: {}\nchannel watched: {}".format(self.tv_state, self.tv_vol,
                                                                                        self.channel_list, self.channel)

cmd = RemoteControl()
print("""

TELEVISION APPLICATION

1- TV OPEN
2- TV OFF
3- VOLUME SETTINGS
4- ADD CHANNEL
5- NUMBER OF CHANNEL
6- RANDOM CHANNEL 
7- TV INFO

PRESS 'Q' FOR EXIT...


""")

while True:

    process = input("Please enter a process: ")

    if (process == "Q"):

        print("Program is shutting down...Please wait...")
        time.sleep(1)
        print("Program ended...")
        break

    elif (process == "1"):

        cmd.tv_open()


    elif (process == "2"):

        cmd.tv_close()


    elif (process == "3"):

        cmd.vol_config()

    elif (process == "4"):

        channel_names = input("Enter the channel names separated by commas... : ")
        channel_list = channel_names.split(",")

        for i in channel_list:
            cmd.channel_add(i)

    elif (process == "5"):

        print("Number of Channel: ", len(cmd))

    elif (process == "6"):

        cmd.random_channel()

    elif (process == "7"):

        print(cmd)

    else:

        print("Invalid Operation... Please try again.")