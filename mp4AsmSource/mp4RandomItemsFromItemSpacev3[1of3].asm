#To be inserted at 80083878
#To be inserted at 80083878
# Array of integer percentages (assuming 12 items)
# Replace the values in this array with the desired percentages for each item
bl afterPercentages
nop #for python script alignment
percentages:
#Mini Mushroom
.2byte 0x0100 #weight
.2byte 0x0000 #item ID

#Mushroom
.2byte 0x0101 #weight
.2byte 0x0001 #item ID

#Super Mini Mushroom
.2byte 0x0102 #weight
.2byte 0x0002 #item ID

#Super Mega Mushroom
.2byte 0x0103 #weight
.2byte 0x0003 #item ID

#Mini Mega Hammer
.2byte 0x0104 #weight
.2byte 0x0004 #item ID

#Warp Pipe
.2byte 0x0105 #weight
.2byte 0x0005 #item ID

#Swap Card
.2byte 0x0106 #weight
.2byte 0x0006 #item ID

#Sparky Sticker
.2byte 0x0107 #weight
.2byte 0x0007 #item ID

#Gaddlight
.2byte 0x0108 #weight
.2byte 0x0008 #item ID

#Chomp Call
.2byte 0x0109 #weight
.2byte 0x0009 #item ID

#Bowser Suit
.2byte 0x010A #weight
.2byte 0x000A #item ID

#Boo Crystal Ball
.2byte 0x010B #weight
.2byte 0x000B #item ID

#Magic Lamp
.2byte 0x010C #weight
.2byte 0x000C #item ID

.4byte 0 #padding for easier python script generation


afterPercentages:
#make r7 hold pointer to percentages
mflr r7
addi r7, r7, 4 #skip over nop
# Calculate the range of random values based on percentages
li r3, 0
li r4, 0
loop_calc:
    cmpwi r3, 52 # Exit at 13 * 4 (4 being size of .4byte)
    beq- exit_calc
    lhzx r5, r7, r3 # Load the percentage for the current item using r3 as index
    add r4, r4, r5 # Add the percentage to the range of random values
    addi r3, r3, 4 # Increment index by 4 (size of an integer)
    b loop_calc
exit_calc:

# Call the random integer function
lis r5, 0x8005
ori r5, r5, 0xFB40 # 0x8005FB40 get rand int function
mtctr r5
mr r3, r4
bctrl

# rand integer in r3 in range of percentages array

# Select the item based on the random integer
li r4, 0
li r5, 0
loop_select:
    cmpwi r5, 52 # Exit at 13 * 4 (4 being size of .4byte)
    beq- exit_select
    lhzx r6, r7, r5 # Load the percentage for the current item using r5 as index
    sub r3, r3, r6 # Subtract the percentage from the random integer
    cmpwi r3, 0 # Compare the updated random integer with 0
    bge+ loop_increment # If the updated random integer is greater than or equal to 0, continue to the next item
    b exit_select
loop_increment:
    addi r4, r4, 1 #item id increment
    addi r5, r5, 4 # Increment index by 4 (size of an integer)
    b loop_select
exit_select:
    mulli r4, r4, 4 #i * sizeof int
    addi r4, r4, 2
    lhzx r4, r7, r4 #get new item id
exit:
lis r5, 0x817F
ori r5, r5, 0xFFF0
stw r4, 0 (r5)
cmpwi r4, 8
blt- skipModelIncrement
#there's a gap in the item models starting at gaddlight's item id (8)
addi r4, r4, 1
skipModelIncrement:
lis r5, 0x0007
ori r5, r5, 0x006d #base item id
add r3, r4, r5
li r4, 0 #restore from hook
li r5, 0 #restore from hook
li r5, 0 #restore from hook