"""
This is a story based game of a tiger with a play who has multiple choices to pick items and play.
Group Members:
Cheena, Daniela, Swekshya, Maaz, Sahil and Aderemi
Mid-Term Project - Python
ANA-1001 Programming For Analytics
"""
# Python imports
import random
import time
import os
from datetime import datetime

# Local imports
import view
import api


# Player's GAIN HEALTH Parameters
RECHARGE_HEALTH = 50
RECHARGE_WATER = 5

# Tiger DAMAGES Parameters
FIRE_WEAPON_DAMAGE = 80
MAP_OF_VALLEY_DAMAGE = 30
KNIFE_DAMAGE = 5


# THESE ARE THE SHORT CONSTANTS THAT WE USED SO FAR.
HILLTOP = "ht"
FOREST = "fo"
RIVER_SIDE = "rs"
VALLEY = "va"

PLAYER_HEALTH = 100
PLAYER_TOOLS = ["Knife", "Water"]
TIGER_HEALTH = 100


def greeting_message(subject, _object) -> None:
    """
    This function will greet the player.
    :param subject:
    :param _object:
    :return:
    """
    if subject == "Valley area":
        print(f"\nYou have reached {subject}, ready to fight with tiger")
    else:
        PLAYER_TOOLS.append(_object)
        print(f"\nYou have reached {subject}. {_object} is available here.")


def items_message():
    """
    This function is used to display player tools that what he got behind him to fight with tiger.
    :return:
    """
    for item in PLAYER_TOOLS:
        print(f"You got {item}")


def fight_message():
    """
    This function will only display the fight message
    :return:
    """
    print("\n\t\t\tFight will start in 5 seconds\t\t\t")
    time.sleep(1)
    print("\t\t\tFight will start in 4 seconds\t\t\t")
    time.sleep(1)
    print("\t\t\tFight will start in 3 seconds\t\t\t")
    time.sleep(1)
    print("\t\t\tFight will start in 2 seconds\t\t\t")
    time.sleep(1)
    print("\t\t\tFight will start in 1 second\t\t\t")
    time.sleep(1)
    print("\nFight starts. Player will attack first.")
    print("\nPlayer can choose from following options:\n\n"
          "Press HK to use Health Kit. (Can use only one time)\n"
          "Press FW to use Fire Weapon. (Can use only one time)\n"
          "Press KN to use Knife (Can use multiple times)\n"
          "Press DW to Drink Water (Can use multiple times)")


def fight_health_decision(user_choice):
    """
    This function will be used to deduct health of player and tiger
    :param user_choice:
    :return:
    """

    global PLAYER_HEALTH, TIGER_HEALTH
    if user_choice == "HK":
        if "Health kit" not in PLAYER_TOOLS:
            print("You're out of Health Kit.")
            return
        PLAYER_TOOLS.remove("Health kit")
        if PLAYER_HEALTH > 50:
            PLAYER_HEALTH = 100
        else:
            PLAYER_HEALTH += RECHARGE_HEALTH
    elif user_choice == "FW":
        if "Fire weapon" not in PLAYER_TOOLS:
            print("You're out of Fire Weapon.")
            return
        PLAYER_TOOLS.remove("Fire weapon")
        TIGER_HEALTH -= FIRE_WEAPON_DAMAGE
    elif user_choice == "KN":
        TIGER_HEALTH -= KNIFE_DAMAGE
    elif user_choice == "DW":
        PLAYER_HEALTH += RECHARGE_WATER


def update_player_health():
    """
    If the user doesn't select map of valley, then his points will be deducted by 30
    :return:
    """
    global PLAYER_HEALTH
    if "Water and map of valley" not in PLAYER_TOOLS:
        print(f"\nDeducting {MAP_OF_VALLEY_DAMAGE} points because player didn't carry Map of Valley with himself.")
        PLAYER_HEALTH -= MAP_OF_VALLEY_DAMAGE


def fight_measures():
    """
    Things to do and measure before the start of fight
    :return:
    """
    fight_message()
    update_player_health()


def fight_with_tiger():
    """
    This function is responsible to take input from player and reduce health vice versa.
    :return:
    """
    global PLAYER_HEALTH
    player_hit = str(input("\nEnter your choice: ")).upper()
    while player_hit not in ["HK", "FW", "KN", "DW"]:
        print("\nInvalid Choice. Please try again!")
        player_hit = str(input("\nEnter your choice: ")).upper()

    fight_health_decision(user_choice=player_hit)

    # Now its tiger turn to hit back
    if TIGER_HEALTH > 0:
        tiger_damage = random.choice([15, 20, 25])
        PLAYER_HEALTH -= tiger_damage


def check_holiday(date):
    """
    This function will return a boolean value that if it is a holiday or not.
    :param date:
    :return:
    """
    holidays = api.get_holidays(country="CA", year="2022")
    for holiday in holidays:
        if holiday['date'] != date:
            pass
        return True, holiday
    return False, None


def display_weather():
    """
    This function will display the timings according to the region.
    :return:
    """
    weather = api.weather_city()
    print(f"\nToday, the temperature is {round(weather['C'], 2)}°C / {round(weather['F'], 2)}°F / "
          f"{round(weather['K'], 2)}K as per the weather API.")


def display_sunrise_sunset_timings():
    """
    This function will display the timings according to the region.
    :return: 
    """
    _time = api.sunset_and_sunrise_time()
    print(f"\nThe sunrise timing is: {_time['sunrise']}")
    print(f"The sunset timing is: {_time['sunset']}")
    
    
if __name__ == "__main__":

    currentDateAndTime = datetime.now()
    print("\nDo you want to play the game? Press any key to continue and 'q' to quit ")
    user_consent = str(input("Enter your choice: ")).upper()

    while user_consent not in ['QUIT', 'Q']:

        view.story_opinion_message()
        time.sleep(2)

        print("\nLets check for a holiday..")
        print("\nCalling Holiday API..")
        _, data = check_holiday(date=str(currentDateAndTime.date()))
        if _:
            print(f"\nOhh!! Today is {data['name']}.")
            print("\nDo you want to hunt on a holiday? Press any key to continue and q to Quit")
            holiday_consent = str(input("Enter your choice: ")).upper()
            if holiday_consent in ["Q", "QUIT"]:
                print("\nGame QUIT because of holiday!\n")
                os.abort()
        else:
            print("\nNo Holiday Today!")

        print("\n1- Check the weather of the city.")
        print("2- Check the sunrise / sunset timings of the city.")
        print("3- Continue to play game.")

        user_preference = int(input("Enter your choice: "))
        while user_preference in [1, 2]:
            if user_preference == 1:
                display_weather()
            elif user_preference == 2:
                display_sunrise_sunset_timings()
            print("\n1- Check the weather of the city.")
            print("2- Check the sunrise / sunset timings of the city.")
            print("3- Continue to play game.")
            user_preference = int(input("Enter your choice: "))

        time.sleep(2)
        print("\n\nHurray!! Lets continue the game..\n")
        view.start_of_story()
        time.sleep(3)
        view.instructions_of_story()
        time.sleep(4)
        view.pickup_options()
        time.sleep(5)
        view.location_choice()

        for i in range(2):
            items_message()
            userInput = str(input("\nEnter your choice: ")).lower()
            while userInput not in [HILLTOP, FOREST, RIVER_SIDE, VALLEY]:
                print("\nInvalid Choice. Please try again!")
                userInput = str(input("\nEnter your choice: ")).lower()

            if userInput == HILLTOP:
                greeting_message(subject="Hill Top", _object="Fire weapon")
            elif userInput == FOREST:
                greeting_message(subject="Forest", _object="Health kit")
            elif userInput == RIVER_SIDE:
                greeting_message(subject="River side", _object="Water and map of valley")
                view.map_view()
            elif userInput == VALLEY:
                greeting_message(subject="Valley area", _object="")
                break

        items_message()
        fight_measures()
        while PLAYER_HEALTH > 0 and TIGER_HEALTH > 0:
            print(f"\nPlayer health: {PLAYER_HEALTH}")
            print(f"Tiger health: {TIGER_HEALTH}")
            fight_with_tiger()

        print("\nResults: ")
        print(f"Player health: {PLAYER_HEALTH if PLAYER_HEALTH > 0 else 0}")
        print(f"Tiger health: {TIGER_HEALTH if TIGER_HEALTH > 0 else 0}")

        if PLAYER_HEALTH > TIGER_HEALTH or (PLAYER_HEALTH == 0 and PLAYER_HEALTH == TIGER_HEALTH):
            print("\nPlayer wins (Get 1000 coins in wallet).") \
                if 6 < currentDateAndTime.hour < 18 else \
                print("\nPlayer wins (Get 1500 coins in wallet).")
        else:
            print("\nPlayer loose.")

        print("\nDo you want to play the game again? Press any key to continue and 'q' to quit ")
        user_consent = str(input("Enter your choice: ")).upper()

    print("\nGame QUIT. Please come back again and earn points!\n")
    os.abort()

