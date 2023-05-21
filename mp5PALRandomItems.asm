#To be inserted at 800C9968
stwu r1, -16(r1)
mflr r0
stw r0, 20(r1)
stw r31, 0(r1)
bl afterPercentages
nop #padding convience for python program
percentages:
#Super Mushroom
.2byte 0x0101 #weight
.2byte 0x0001 #item ID

#Cursed Mushroom
.2byte 0x0102 #weight
.2byte 0x0002 #item ID

#Warp Pipe
.2byte 0x0103 #weight
.2byte 0x0003 #item ID

#Klepto
.2byte 0x0104 #weight
.2byte 0x0004 #item ID

#Bubble
.2byte 0x0105 #weight
.2byte 0x0005 #item ID

#Wiggler
.2byte 0x0106 #weight
.2byte 0x0006 #item ID

#Hammer Bro
.2byte 0x0107 #weight
.2byte 0x000A #item ID

#Coin Block
.2byte 0x0108 #weight
.2byte 0x000B #item ID

#Spiny
.2byte 0x0109 #weight
.2byte 0x000C #item ID

#Paratroopa
.2byte 0x010A #weight
.2byte 0x000D #item ID

#Bullet Bill
.2byte 0x010B #weight
.2byte 0x000E #item ID

#Goomba
.2byte 0x010C #weight
.2byte 0x000F #item ID

#Bob-omb
.2byte 0x010D #weight
.2byte 0x0010 #item ID

#Koopa Bank
.2byte 0x010E #weight
.2byte 0x0011 #item ID

#Kamek
.2byte 0x0111 #weight
.2byte 0x0014 #item ID

#Mr. Blizzard
.2byte 0x0112 #weight
.2byte 0x0015 #item ID

#Piranha Plant
.2byte 0x0113 #weight
.2byte 0x0016 #item ID

#Magikoopa
.2byte 0x0114 #weight
.2byte 0x0017 #item ID

#Ukiki
.2byte 0x0115 #weight
.2byte 0x0018 #item ID

#Lakitu
.2byte 0x0116 #weight
.2byte 0x0019 #item ID

#Tweester
.2byte 0x011B #weight
.2byte 0x001E #item ID

#Duel
.2byte 0x011C #weight
.2byte 0x001F #item ID

#Chain Chomp
.2byte 0x011D #weight
.2byte 0x0020 #item ID

#Bone
.2byte 0x011E #weight
.2byte 0x0021 #item ID

#Bowser
.2byte 0x011F #weight
.2byte 0x0022 #item ID

#Chance
.2byte 0x0120 #weight
.2byte 0x0023 #item ID

#Miracle
.2byte 0x0121 #weight
.2byte 0x0024 #item ID

#Donkey Kong
.2byte 0x0122 #weight
.2byte 0x0025 #item ID

#Versus
.2byte 0x0123 #weight
.2byte 0x0026 #item ID

.4byte 0 #padding for python program


afterPercentages:
#make r7 hold pointer to percentages
mflr r7
addi r7, r7, 4 #add 4 to skip over nop
# Calculate the range of random values based on percentages
li r3, 0
li r4, 0
loop_calc:
    cmpwi r3, 116 # Exit at 29 items * 4 (4 being size of .4byte)
    beq- exit_calc
    lhzx r5, r7, r3 # Load the percentage for the current item using r3 as index
    add r4, r4, r5 # Add the percentage to the range of random values
    addi r3, r3, 4 # Increment index by 4 (size of an integer)
    b loop_calc
exit_calc:

#odds total in r4
lis r5, 0x8003
ori r5, r5, 0xB0CC
mtctr r5
mr r3, r4 #odds total as func arg
bctrl

#rand int in r3

# Select the item based on the random integer
li r4, 0
li r5, 0
loop_select:
    cmpwi r5, 116 # Exit at 29 items * 4 (4 being size of .4byte)
    beq- exit_select
    lhzx r6, r7, r5 # Load the percentage for the current item using r5 as index
    sub r3, r3, r6 # Subtract the percentage from the random integer
    cmpwi r3, 0 # Compare the updated random integer with 0
    bge+ loop_increment # If the updated random integer is greater than or equal to 0, continue to the next item
    b exit_select
loop_increment:
    addi r4, r4, 1 #iterator id increment
    addi r5, r5, 4 # Increment index by 4
    b loop_select
exit_select:
    mulli r4, r4, 4 #i * sizeof int
    addi r4, r4, 2
    lhzx r3, r7, r4 #get new item id

exit:
  lwz r31, 0(r1)
  lwz r0, 20(r1)
  mtlr r0
  addi r1, r1, 0x10
  blr 