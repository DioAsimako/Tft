print("Ptolemy System - The mapper.\n")

# Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creates the object champion with all the required attributes
#  for dueling and a function to represent the champion with its stats

class Champion:   
    
    def __init__(self, name='champ', cost=0, health1=0, health2=0, health3=0, damage1=0,
                 damage2=0, damage3=0, attackSpeed=0, armor=0,
                 magicResistance=0, mana=0, startingMana=0, attackRange=0):       
        self.name = name
        self.cost = cost
        self.health1 = health1
        self.health2 = health2
        self.health3 = health3
        self.damage1 = damage1
        self.damage2 = damage2
        self.damage3 = damage3
        self.attackSpeed = attackSpeed
        self.armor = armor
        self.magicResistance = magicResistance
        self.mana = mana
        self.startingMana = startingMana
        self.attackRange = attackRange   
        
    def exposition(self):
        print('Champion: ' + self.name)
        print('Cost : ' + str(self.cost))
        print('Health : ' + str(self.health1) + '/' + str(self.health2) +
              '/' + str(self.health3))
        print('Attack Damage : ' + str(self.damage1) + '/' + str(self.damage2) +
              '/' + str(self.damage3))
        print('Attack Speed: ' + str(self.attackSpeed))
        print('Armor: ' + str(self.armor))
        print('Magic Resistance: ' + str(self.magicResistance))
        print('Mana: ' + str(self.mana))
        print('Starting Mana: ' + str(self.startingMana))
        print('Attack Range: ' + str(self.attackRange))

# Takes two champion objects as arguments and simulates a basic duel providing 
#  info such as hits, damage and health reduction. Returns to a reporting 
#  method and one that plots

def duel(champ1, champ2):
    health_1 = champ1.health1
    health_2 = champ2.health1
    att_speed_1 = champ1.attackSpeed
    att_speed_2 = champ2.attackSpeed
    hits_1 = 1
    hits_2 = 1
    damage_1 = champ1.damage1
    damage_2 = champ2.damage1
    xtime = [0]
    xdamage1 = [0]
    xhealth1 = [health_1]
    xdamage2 = [0]
    xhealth2 = [health_2]
    
    for time_unit in np.arange(0.0, 1000.0, 0.05):
        if time_unit < hits_1 * att_speed_1 + 0.01 and time_unit > hits_1 * att_speed_1 - 0.01:
            damage_taken = damage_1 * 100 / (100 + champ2.armor)
            health_2 -= damage_taken
            xtime.append(time_unit)
            xhealth1.append(xhealth1[hits_1  + hits_2 - 2])
            xhealth2.append(health_2)
            xdamage1.append(damage_taken + xdamage1[hits_1  + hits_2 - 2])
            xdamage2.append(xdamage2[hits_1  + hits_2 - 2])
            hits_1 += 1
            if health_2 <= 0:
                report(champ1.name, champ2.name, health_1, time_unit,
                       hits_1 -1, hits_2 -1, xdamage1[-1], xdamage2[-1])
                plot_duel(xtime, xdamage1, xdamage2, xhealth1, xhealth2, champ1.name, champ2.name)
                break
        if time_unit < hits_2 * att_speed_2 + 0.01 and time_unit > hits_2 * att_speed_2 - 0.01:
            damage_taken = damage_2 * 100 / (100 + champ1.armor)
            health_1 -= damage_taken
            xtime.append(time_unit)
            xhealth2.append(xhealth2[hits_1  + hits_2 - 2])
            xhealth1.append(health_1)
            xdamage2.append(damage_taken + xdamage2[hits_1  + hits_2 - 2])
            xdamage1.append(xdamage1[hits_1  + hits_2 - 2])
            hits_2 += 1
            if health_1 <= 1:
                report(champ2.name, champ1.name, health_2, time_unit,
                       hits_2 -1, hits_1 -1, xdamage2[-1], xdamage1[-1])
                plot_duel(xtime, xdamage1, xdamage2, xhealth1, xhealth2, champ1.name, champ2.name)
                break

# Takes duel results as arguments and provide a readable version of the results

def report(victor, loser, remaining_health, time, hitsv, hitsl, damagev, damagel):
    print('\n     Battle Results\n')
    print('Winner:', victor, '  Loser:', loser)
    print('The fight lasted ', time, ' seconds.')
    print('Remaining health: ', remaining_health)
    print('Total hits ' + victor + ' applied: ' + str(hitsv))
    print('Total hits ' + loser + ' applied: ' + str(hitsl))
    print(victor, 'total damage: ', damagev)
    print(loser, 'total damage: ', damagel)

# Creates two graphs that show the progress of health and damage inflicted for 
#  both champions of the duel

def plot_duel(xtime, xdamage1, xdamage2, xhealth1, xhealth2, dueler1, dueler2):  
    '''
    figure, axis = plt.subplots(2, 2)
    axis[0, 0].plot(xtime, xdamage1)
    axis[0, 0].set_title("Dueler 1 Damage")
    axis[0, 1].plot(xtime, xdamage2)
    axis[0, 1].set_title("Dueler 2 Damage")
    axis[1, 0].plot(xtime, xdamage1)
    axis[1, 0].set_title("Dueler 1 Health")
    axis[1, 1].plot(xtime, xdamage2)
    axis[1, 1].set_title("Dueler 2 Health")
    plt.show()
    '''
    
    figure, axis = plt.subplots(1, 2)
    axis[0].plot(xtime, xdamage1, label = "Dueler 1 ")
    axis[0].plot(xtime, xdamage2, label = "Dueler 2 ")
    axis[0].set_title("Damage - Time")
    axis[1].plot(xtime, xhealth1, label = dueler1)
    axis[1].plot(xtime, xhealth2, label = dueler2)
    axis[1].set_title("Health - Time")
    plt.legend()
    plt.show()
    
    '''
    plt.plot(xtime, xdamage1, label = "Dueler 1 ")
    plt.plot(xtime, xdamage2, label = "Dueler 2 ")
    plt.xlabel('time')
    plt.ylabel('damage')
    plt.title('Damage graph')
    plt.legend()
    plt.show()
    '''

# The main body of operations provides two options. Inspect the stat of a champion
#  or duel two champions. After users feedback a report message and graphs are given

champion_data = pd.read_csv (r'C:\Users\Dio\Documents\GitHub\Tft\TftStats.csv')   
champion_list = pd.DataFrame(champion_data) 
item_data = pd.read_csv (r'C:\Users\Dio\Documents\GitHub\Tft\tft items.csv')
item_list = pd.DataFrame(item_data) 
number_of_champions = len(champion_list)
champions = []
for champ in range(0, number_of_champions):
    champion = Champion(champion_list.iat[champ,0],
                        champion_list.iat[champ,1],
                        champion_list.iat[champ,2],
                        champion_list.iat[champ,3],
                        champion_list.iat[champ,4],
                        champion_list.iat[champ,7],
                        champion_list.iat[champ,8],
                        champion_list.iat[champ,9],
                        champion_list.iat[champ,10],
                        champion_list.iat[champ,5],
                        champion_list.iat[champ,6],
                        champion_list.iat[champ,11],
                        champion_list.iat[champ,12],
                        champion_list.iat[champ,13],
                        )
    champions.append(champion)
numbers_of_components = len(item_list)
component_items = np.zeros((9, 11))
for item in range(0, numbers_of_components):
    for stat in range(0, 11):
        component_items[item][stat] = item_list.iat[item, stat + 1]
        
action = input('Which action do you wish to perform\nA] Inspect a champion\n' +
               'B] Duel\n Enter your choice: ') 
if action == 'A' or action == 'a':
    champion_choice = input("Enter champion to inspect: ") 
    for champ in range(0, number_of_champions):
        if champions[champ].name == champion_choice:
            print('\n')
            print(champions[champ].exposition()) 
elif action == 'B' or action == 'b':
    challenger1 = []
    challenger2 = []
    dueler1 = input("Enter first champion for duel: ")    
    for champ in range(0, number_of_champions):
        if champions[champ].name == dueler1:
            challenger1.append(champions[champ])
    dueler2 = input("Enter second champion for duel: ")
    for champ in range(0, number_of_champions):
        if champions[champ].name == dueler2:
            challenger2.append(champions[champ])
    duel(challenger1[0], challenger2[0])
else:
    print('\nWrong entry, bye moron!')