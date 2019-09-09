################################################################################
# set_clock.py
# Original code from A. Hornof - Sept 2017
#
#
# Last Edit by Priya Kudva Oct. 2, 2017
#
#
# A sample program to show how to move through a list of sound objects with
# single keystrokes.
#
################################################################################
__author__ = 'kudva'

# Package imports
import readchar
import time         # for time.sleep()

# Local imports
import sound        # sound.py accompanies this file

################################################################################
# main()
################################################################################
def main():
    create_sound_filenames()
    verify_sound_filenames()
    create_menu_globals()
    run_menu()

################################################################################
# Create the sound objects for the auditory menus and display.
################################################################################
def create_sound_filenames():

    # Declare global variables.

    #Added PM wav file
    global INTRO_WAV, YOU_SELECTED_WAV, HOURS_WAV, AMPM_WAV, PRESS_AGAIN_TO_QUIT_WAV,\
        EXITING_PROGRAM_WAV, EXITING_PROGRAM_WAV_DURATION, TMP_FILE_WAV, DAYS_WAV, MINUTES_WAV, \
        SET_HOUR_WAV, SET_MINUTES_WAV, HELP_WAV, PRESS_AGAIN_FOR_HELP_WAV, SET_DAY_WAV, \
        UP_WAV, DOWN_WAV, SELECT_WAV, CURRENT_DAY_WAV, CURRENT_HOUR_WAV, CURRENT_MINUTE_WAV, \
        CURRENT_AMPM_WAV, SET_PERIOD_WAV, QUIT_WAV, OH_WAV

    # Create  sounds.
    day_path = "wav_files_provided/days_of_week_f/"
    nav_path = "wav_files_provided/miscellaneous_f/"
    audio_path = "my_wav_files/"
    num_path = "wav_files_provided/numbers_f/"
    INTRO_WAV = nav_path + "Intro_f.wav"
    YOU_SELECTED_WAV = nav_path + "you_selected_f.wav"
    SET_HOUR_WAV = nav_path + "Set_hour_f.wav"
    SET_MINUTES_WAV = nav_path + "Set_minutes_f.wav"
    SET_DAY_WAV = nav_path + "Set_day_of_week_f.wav"


    #Added days of week
    DAYS_WAV = [day_path + "sunday_f.wav", day_path + "monday_f.wav",
                day_path + "tuesday_f.wav", day_path + "wednesday_f.wav",
                day_path + "thursday_f.wav", day_path + "friday_f.wav",
                day_path + "saturday_f.wav"]

    #Added the number 1-12 for hours
    HOURS_WAV = [num_path + "12_f.wav", num_path + "01_f.wav",
                 num_path + "02_f.wav", num_path + "03_f.wav",
                 num_path + "04_f.wav", num_path + "05_f.wav",
                 num_path + "06_f.wav", num_path + "07_f.wav",
                 num_path + "08_f.wav", num_path + "09_f.wav",
                 num_path + "10_f.wav", num_path + "11_f.wav"]

    #Separated hours and minutes
    MINUTES_WAV = [num_path + "00_f.wav", num_path + "01_f.wav",
                   num_path + "02_f.wav", num_path + "03_f.wav",
                   num_path + "04_f.wav", num_path + "05_f.wav",
                   num_path + "06_f.wav", num_path + "07_f.wav",
                   num_path + "08_f.wav", num_path + "09_f.wav",
                   num_path + "10_f.wav", num_path + "11_f.wav",
                   num_path + "12_f.wav", num_path + "13_f.wav",
                   num_path + "14_f.wav", num_path + "15_f.wav",
                   num_path + "16_f.wav", num_path + "17_f.wav",
                   num_path + "18_f.wav", num_path + "19_f.wav",
                   num_path + "20_f.wav", num_path + "21_f.wav",
                   num_path + "22_f.wav", num_path + "23_f.wav",
                   num_path + "24_f.wav", num_path + "25_f.wav",
                   num_path + "26_f.wav", num_path + "27_f.wav",
                   num_path + "28_f.wav", num_path + "29_f.wav",
                   num_path + "30_f.wav", num_path + "31_f.wav",
                   num_path + "32_f.wav", num_path + "33_f.wav",
                   num_path + "34_f.wav", num_path + "35_f.wav",
                   num_path + "36_f.wav", num_path + "37_f.wav",
                   num_path + "38_f.wav", num_path + "39_f.wav",
                   num_path + "40_f.wav", num_path + "41_f.wav",
                   num_path + "42_f.wav", num_path + "43_f.wav",
                   num_path + "44_f.wav", num_path + "45_f.wav",
                   num_path + "46_f.wav", num_path + "47_f.wav",
                   num_path + "48_f.wav", num_path + "49_f.wav",
                   num_path + "50_f.wav", num_path + "51_f.wav",
                   num_path + "52_f.wav", num_path + "53_f.wav",
                   num_path + "54_f.wav", num_path + "55_f.wav",
                   num_path + "56_f.wav", num_path + "57_f.wav",
                   num_path + "58_f.wav", num_path + "59_f.wav"]

    # Added PM wave file path
    AMPM_WAV = [nav_path + "AM_f.wav", nav_path + "PM_f.wav"]

    HELP_WAV = audio_path + "press_k_for_help.wav"
    PRESS_AGAIN_FOR_HELP_WAV = nav_path + "Press_again_for_help_f.wav"

    UP_WAV = audio_path + "press_;_to_go_up.wav"
    DOWN_WAV = audio_path + "press_l_to_go_down.wav"
    SELECT_WAV = audio_path + "press_spacebar_to_select.wav"
    QUIT_WAV = audio_path + "press_j_to_quit.wav"

    SET_PERIOD_WAV = audio_path + "set_period.wav"

    CURRENT_DAY_WAV = audio_path + "current_day_is.wav"
    CURRENT_HOUR_WAV = audio_path + "current_hour_is.wav"
    CURRENT_MINUTE_WAV = audio_path + "current_minute_is.wav"
    CURRENT_AMPM_WAV = audio_path + "current_period_is.wav"

    OH_WAV = num_path + "oh_f.wav"

    PRESS_AGAIN_TO_QUIT_WAV = nav_path + "Press_again_to_quit_f.wav"
    EXITING_PROGRAM_WAV = nav_path + "Exiting_program_f.wav"
    EXITING_PROGRAM_WAV_DURATION = 1.09 # in s. 1.09 is accurate but 0.45 saves time.

    TMP_FILE_WAV = "tmp_file_p782s8u.wav" # Random filename  for output

################################################################################
# Verify all files can be loaded and played.
# Play all sound files to make sure the paths and filenames are correct and valid.
# The very last sound tested/played should be the sound that plays at startup.
################################################################################
def verify_sound_filenames():
    sound.Play(PRESS_AGAIN_TO_QUIT_WAV)
    sound.Play(EXITING_PROGRAM_WAV)
    sound.Play(YOU_SELECTED_WAV)
    sound.Play(HOURS_WAV[0])
    sound.Play(HOURS_WAV[1])
    sound.Play(HOURS_WAV[2])
    sound.Play(HOURS_WAV[3])
    sound.Play(AMPM_WAV[0])
    sound.Play(INTRO_WAV)

################################################################################
# Create some global constants and variables for the menu.
################################################################################
def create_menu_globals():

    # Declare global variables as such.
    global FORWARD_KEY, BACKWARD_KEY, QUIT_KEY, SELECT_KEY, HELP_KEY, MINIMAL_HELP_STRING, CURRENT_TIME

    # Constants
    # Keystrokes for the keyboard interaction.
    FORWARD_KEY = ';'
    BACKWARD_KEY = 'l'
    HELP_KEY = 'k'
    QUIT_KEY = 'j'
    SELECT_KEY = '\x20' # space bar
    # A bare minimum of text to display to guide the user.
    MINIMAL_HELP_STRING = "Press '" + QUIT_KEY + "' to quit."

    # Global variables
    CURRENT_TIME = 0    # The current time that is set. (Just an integer for now.)


################################################################################
# Run the menu in an endless loop until the user exits.
################################################################################
def run_menu():

    global CURRENT_TIME

    # Provide a minimal indication that the program has started.
    print(MINIMAL_HELP_STRING)

    #Play all key assignments
    sound.Play(INTRO_WAV)
    time.sleep(3)
    sound.Play(HELP_WAV)
    time.sleep(2)
    sound.Play(DOWN_WAV)
    time.sleep(2.5)
    sound.Play(UP_WAV)
    time.sleep(2.5)
    sound.Play(SELECT_WAV)
    time.sleep(3)

    #Initialize selection process
    set_day()

def set_day():
    global CURRENT_TIME
    global CURRENT_DAY

    CURRENT_TIME = 0

    #Play the entering state audio
    sound.Play(SET_DAY_WAV)
    time.sleep(1.4)

    #Play current day selection
    sound.combine_wav_files(TMP_FILE_WAV, CURRENT_DAY_WAV, DAYS_WAV[CURRENT_TIME])
    sound.Play(TMP_FILE_WAV)
    time.sleep(3)

    # Get the first keystroke.
    c = readchar.readchar()

    # Endless loop responding to the user's last keystroke.
    # The loop breaks when the user hits the SELECT_KEY or the QUIT_KEY
    while True:

        # Respond to the user's input.
        if c == FORWARD_KEY:

            # Advance the time, looping back around to the start.
            CURRENT_TIME += 1
            if CURRENT_TIME == len(DAYS_WAV):
                CURRENT_TIME = 0

            # Concatenate two audio files to generate the message.
            sound.combine_wav_files(TMP_FILE_WAV, DAYS_WAV[CURRENT_TIME])

            # Play the concatenated file.
            sound.Play(TMP_FILE_WAV)

        # Backward key
        if c == BACKWARD_KEY:

            # Move backward, looping around
            CURRENT_TIME -= 1
            if CURRENT_TIME == -1:
                CURRENT_TIME = len(DAYS_WAV) - 1

            # Concatenate two audio files to generate the message.
            sound.combine_wav_files(TMP_FILE_WAV, DAYS_WAV[CURRENT_TIME])

            # Play the concatenated file.
            sound.Play(TMP_FILE_WAV)


        # Selects current time
        if c == SELECT_KEY:
            sound.combine_wav_files(TMP_FILE_WAV, YOU_SELECTED_WAV,
                                    DAYS_WAV[CURRENT_TIME])

            # Save the hour selection
            CURRENT_DAY = CURRENT_TIME

            # Play the concatenated file.
            sound.Play(TMP_FILE_WAV)
            time.sleep(2.8)

            #Go to set hour state
            set_hour()
            break

        #User presses help key
        if c == HELP_KEY:

            # Notify the user that another HELP_KEY will play the help menu
            sound.Play(PRESS_AGAIN_FOR_HELP_WAV)

            # Get the user's next keystroke.
            c = readchar.readchar()

            # If the user pressed HELP_KEY, play key options
            if c == HELP_KEY:
                sound.combine_wav_files(TMP_FILE_WAV, QUIT_WAV, HELP_WAV,
                                        DOWN_WAV, UP_WAV, SELECT_WAV)
                sound.Play(TMP_FILE_WAV)

        # User quits.
        if c == QUIT_KEY:

            # Notify the user that another QUIT_MENU_KEY will quit the program.
            sound.Play(PRESS_AGAIN_TO_QUIT_WAV)

            # Get the user's next keystroke.
            c = readchar.readchar()

            # If the user pressed QUIT_MENU_KEY, quit the program.
            if c == QUIT_KEY:
                sound.Play(EXITING_PROGRAM_WAV)
                # A delay is needed so the sound gets played before quitting.
                time.sleep(EXITING_PROGRAM_WAV_DURATION)
                sound.cleanup()
                # Quit the program
                break

        # The user presses a key that will have no effect.
        else:
            # Get the user's next keystroke.
            c = readchar.readchar()




def set_hour():
    global CURRENT_TIME
    global CURRENT_HOUR

    CURRENT_TIME = 0

    #Entering new state, play audio to tell user
    sound.Play(SET_HOUR_WAV)
    time.sleep(1)

    #Play current hour selection
    sound.combine_wav_files(TMP_FILE_WAV, CURRENT_HOUR_WAV, HOURS_WAV[CURRENT_TIME])
    sound.Play(TMP_FILE_WAV)
    time.sleep(2.6)

    # Get the first keystroke.
    c = readchar.readchar()

    # Endless loop responding to the user's last keystroke.
    # The loop breaks when the user hits the SELECT_KEY or the QUIT_KEY
    while True:

        # Respond to the user's input.
        if c == FORWARD_KEY:

            # Advance the time, looping back around to the start.
            CURRENT_TIME += 1
            if CURRENT_TIME == len(HOURS_WAV):
                CURRENT_TIME = 0

            # Concatenate two audio files to generate the message.
            sound.combine_wav_files(TMP_FILE_WAV, HOURS_WAV[CURRENT_TIME])

            # Play the concatenated file.
            sound.Play(TMP_FILE_WAV)

        # Backward key
        if c == BACKWARD_KEY:

            # Move backward, looping around
            CURRENT_TIME -= 1
            if CURRENT_TIME == -1:
                CURRENT_TIME = len(HOURS_WAV) - 1

            # Concatenate two audio files to generate the message.
            sound.combine_wav_files(TMP_FILE_WAV, HOURS_WAV[CURRENT_TIME])

            # Play the concatenated file.
            sound.Play(TMP_FILE_WAV)


        # Selects current time
        if c == SELECT_KEY:
            sound.combine_wav_files(TMP_FILE_WAV, YOU_SELECTED_WAV,
                                    HOURS_WAV[CURRENT_TIME])

            # Save the hour selection
            CURRENT_HOUR = CURRENT_TIME

            # Play the concatenated file.
            sound.Play(TMP_FILE_WAV)
            time.sleep(2.8)

            #Go to set minute state
            set_minute()
            break

        #User presses help key
        if c == HELP_KEY:

            # Notify the user that another HELP_KEY will play the help menu
            sound.Play(PRESS_AGAIN_FOR_HELP_WAV)

            # Get the user's next keystroke.
            c = readchar.readchar()

            # If the user pressed HELP_KEY, play key options
            if c == HELP_KEY:
                sound.combine_wav_files(TMP_FILE_WAV, QUIT_WAV, HELP_WAV,
                                        DOWN_WAV, UP_WAV, SELECT_WAV)
                sound.Play(TMP_FILE_WAV)

        if c == QUIT_KEY:

            # Notify the user that another QUIT_MENU_KEY will quit the program.
            sound.Play(PRESS_AGAIN_TO_QUIT_WAV)

            # Get the user's next keystroke.
            c = readchar.readchar()

            # If the user pressed QUIT_MENU_KEY, quit the program.
            if c == QUIT_KEY:
                sound.Play(EXITING_PROGRAM_WAV)
                # A delay is needed so the sound gets played before quitting.
                time.sleep(EXITING_PROGRAM_WAV_DURATION)
                sound.cleanup()
                # Quit the program
                break

        # The user presses a key that will have no effect.
        else:
            # Get the user's next keystroke.
            c = readchar.readchar()



def set_minute():
    global CURRENT_TIME
    global CURRENT_MINUTE

    CURRENT_TIME = 0

    #Entering new state, play audio to tell user
    sound.Play(SET_MINUTES_WAV)
    time.sleep(1)

    #Play current minute selection
    sound.combine_wav_files(TMP_FILE_WAV, CURRENT_MINUTE_WAV, MINUTES_WAV[CURRENT_TIME])
    sound.Play(TMP_FILE_WAV)
    time.sleep(2.6)

    # Get the first keystroke.
    c = readchar.readchar()

    # Endless loop responding to the user's last keystroke.
    # The loop breaks when the user hits the SELECT_KEY or the QUIT_KEY
    while True:

        # Respond to the user's input.
        if c == FORWARD_KEY:

            # Advance the time, looping back around to the start.
            CURRENT_TIME += 1
            if CURRENT_TIME == len(MINUTES_WAV):
                CURRENT_TIME = 0

            # Concatenate two audio files to generate the message.
            sound.combine_wav_files(TMP_FILE_WAV, MINUTES_WAV[CURRENT_TIME])

            # Play the concatenated file.
            sound.Play(TMP_FILE_WAV)

        # Backward key
        if c == BACKWARD_KEY:

            # Move backward, looping around
            CURRENT_TIME -= 1
            if CURRENT_TIME == -1:
                CURRENT_TIME = len(MINUTES_WAV) - 1

            # Concatenate two audio files to generate the message.
            sound.combine_wav_files(TMP_FILE_WAV, MINUTES_WAV[CURRENT_TIME])

            # Play the concatenated file.
            sound.Play(TMP_FILE_WAV)

        # Selects current time
        if c == SELECT_KEY:
            sound.combine_wav_files(TMP_FILE_WAV, YOU_SELECTED_WAV,
                                    MINUTES_WAV[CURRENT_TIME])

            #Save minute selection
            CURRENT_MINUTE = CURRENT_TIME

            # Play the concatenated file.
            sound.Play(TMP_FILE_WAV)
            time.sleep(3)

            #Go to set the AM/PM state
            set_AMPM()
            break

        #User presses help key
        if c == HELP_KEY:

            # Notify the user that another HELP_KEY will play the help menu
            sound.Play(PRESS_AGAIN_FOR_HELP_WAV)

            # Get the user's next keystroke.
            c = readchar.readchar()

            # If the user pressed HELP_KEY, play key options
            if c == HELP_KEY:
                sound.combine_wav_files(TMP_FILE_WAV, QUIT_WAV, HELP_WAV,
                                        DOWN_WAV, UP_WAV, SELECT_WAV)
                sound.Play(TMP_FILE_WAV)

        # User quits.
        if c == QUIT_KEY:

            # Notify the user that another QUIT_MENU_KEY will quit the program.
            sound.Play(PRESS_AGAIN_TO_QUIT_WAV)

            # Get the user's next keystroke.
            c = readchar.readchar()

            # If the user pressed QUIT_MENU_KEY, quit the program.
            if c == QUIT_KEY:
                sound.Play(EXITING_PROGRAM_WAV)
                # A delay is needed so the sound gets played before quitting.
                time.sleep(EXITING_PROGRAM_WAV_DURATION)
                sound.cleanup()
                # Quit the program
                break

        # The user presses a key that will have no effect.
        else:
            # Get the user's next keystroke.
            c = readchar.readchar()

def set_AMPM():
    global CURRENT_TIME
    global CURRENT_AMPM

    CURRENT_TIME = 0

    #Entering new state, play audio to tell user
    sound.Play(SET_PERIOD_WAV)
    time.sleep(1.5)

    #Play current selection of period
    sound.combine_wav_files(TMP_FILE_WAV, CURRENT_AMPM_WAV, AMPM_WAV[CURRENT_TIME])
    sound.Play(TMP_FILE_WAV)
    time.sleep(2.6)

    # Get the first keystroke.
    c = readchar.readchar()

    # Endless loop responding to the user's last keystroke.
    # The loop breaks when the user hits the SELECT_KEY or the QUIT_KEY
    while True:

        # Respond to the user's input.
        if c == FORWARD_KEY:

            # Advance the time, looping back around to the start.
            CURRENT_TIME += 1
            if CURRENT_TIME == 2:
                CURRENT_TIME = 0

            # Concatenate two audio files to generate the message.
            sound.combine_wav_files(TMP_FILE_WAV, AMPM_WAV[CURRENT_TIME])

            # Play the concatenated file.
            sound.Play(TMP_FILE_WAV)

        # Backward key
        if c == BACKWARD_KEY:

            # Move backward, looping around
            CURRENT_TIME -= 1
            if CURRENT_TIME == -1:
                CURRENT_TIME = 1

            # Concatenate two audio files to generate the message.
            sound.combine_wav_files(TMP_FILE_WAV, AMPM_WAV[CURRENT_TIME])

            # Play the concatenated file.
            sound.Play(TMP_FILE_WAV)

        # Selects current time
        if c == SELECT_KEY:
            sound.combine_wav_files(TMP_FILE_WAV, YOU_SELECTED_WAV,
                                    AMPM_WAV[CURRENT_TIME])

            # Save minute selection
            CURRENT_AMPM = CURRENT_TIME

            # Play the concatenated file.
            sound.Play(TMP_FILE_WAV)
            time.sleep(2)

            #Selected last input, move on to play result and quit
            play_result_and_quit()
            break

        #User presses help key
        if c == HELP_KEY:

            # Notify the user that another HELP_KEY will play the help menu
            sound.Play(PRESS_AGAIN_FOR_HELP_WAV)

            # Get the user's next keystroke.
            c = readchar.readchar()

            # If the user pressed HELP_KEY, play key options
            if c == HELP_KEY:
                sound.combine_wav_files(TMP_FILE_WAV, QUIT_WAV, HELP_WAV,
                                        DOWN_WAV, UP_WAV, SELECT_WAV)
                sound.Play(TMP_FILE_WAV)

        # User quits.
        if c == QUIT_KEY:

            # Notify the user that another QUIT_MENU_KEY will quit the program.
            sound.Play(PRESS_AGAIN_TO_QUIT_WAV)

            # Get the user's next keystroke.
            c = readchar.readchar()

            # If the user pressed QUIT_MENU_KEY, quit the program.
            if c == QUIT_KEY:
                sound.Play(EXITING_PROGRAM_WAV)
                # A delay is needed so the sound gets played before quitting.
                time.sleep(EXITING_PROGRAM_WAV_DURATION)
                sound.cleanup()
                # Quit the program
                break

        # The user presses a key that will have no effect.
        else:
            # Get the user's next keystroke.
            c = readchar.readchar()

def play_result_and_quit():
    #End of selection process, program will now repeat back all selections

    #Top of the hour, disregard minute
    if CURRENT_MINUTE == 0:
        sound.combine_wav_files(TMP_FILE_WAV, YOU_SELECTED_WAV, DAYS_WAV[CURRENT_DAY],
                                HOURS_WAV[CURRENT_HOUR], AMPM_WAV[CURRENT_AMPM])

    #Single digit minute, use OH_WAV
    elif CURRENT_MINUTE >= 1 and CURRENT_MINUTE < 10:
        sound.combine_wav_files(TMP_FILE_WAV, YOU_SELECTED_WAV, DAYS_WAV[CURRENT_DAY],
                                HOURS_WAV[CURRENT_HOUR], OH_WAV, MINUTES_WAV[CURRENT_MINUTE],
                                AMPM_WAV[CURRENT_AMPM])

    else:
        sound.combine_wav_files(TMP_FILE_WAV, YOU_SELECTED_WAV, DAYS_WAV[CURRENT_DAY],
                            HOURS_WAV[CURRENT_HOUR], MINUTES_WAV[CURRENT_MINUTE],
                            AMPM_WAV[CURRENT_AMPM])

    sound.Play(TMP_FILE_WAV)
    time.sleep(4.8)

    sound.Play(EXITING_PROGRAM_WAV)
    # A delay is needed so the sound gets played before quitting.
    time.sleep(EXITING_PROGRAM_WAV_DURATION)
    sound.cleanup()

################################################################################
main()
################################################################################
