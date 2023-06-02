#To be inserted at 801eaae4
bl afterPercentages
nop #padding convience for python program
percentages:
#Mushroom
.2byte 0x0100 #weight
.byte 0x00 #item ID
.byte 0x00 #item cost

#Super 'Shroom
.2byte 0x0101 #weight
.byte 0x01 #item ID
.byte 0x01 #item cost

#Sluggish 'Shroom
.2byte 0x0102 #weight
.byte 0x02 #item ID
.byte 0x02 #item cost

#Metal Mushroom
.2byte 0x0103 #weight
.byte 0x03 #item ID
.byte 0x03 #item cost

#Bullet Bill
.2byte 0x0104 #weight
.byte 0x04 #item ID
.byte 0x04 #item cost

#Warp Pipe
.2byte 0x0105 #weight
.byte 0x05 #item ID
.byte 0x05 #item cost

#Flutter
.2byte 0x0106 #weight
.byte 0x06 #item ID
.byte 0x06 #item cost

#Cursed Mushroom
.2byte 0x0107 #weight
.byte 0x07 #item ID
.byte 0x07 #item cost

#Spiny
.2byte 0x010A #weight
.byte 0x0A #item ID
.byte 0x0A #item cost

#Goomba
.2byte 0x010B #weight
.byte 0x0B #item ID
.byte 0x0B #item cost

#Piranha Plant
.2byte 0x010C #weight
.byte 0x0C #item ID
.byte 0x0C #item cost

#Klepto
.2byte 0x010D #weight
.byte 0x0D #item ID
.byte 0x0D #item cost

#Toady
.2byte 0x010F #weight
.byte 0x0F #item ID
.byte 0x0F #item cost

#Kamek
.2byte 0x0110 #weight
.byte 0x10 #item ID
.byte 0x10 #item cost

#Mr. Blizzard
.2byte 0x0111 #weight
.byte 0x11 #item ID
.byte 0x11 #item cost

#Podoboo
.2byte 0x0114 #weight
.byte 0x14 #item ID
.byte 0x14 #item cost

#Zap
.2byte 0x0115 #weight
.byte 0x15 #item ID
.byte 0x15 #item cost

#Tweester
.2byte 0x0116 #weight
.byte 0x16 #item ID
.byte 0x16 #item cost

#Thwomp
.2byte 0x0117 #weight
.byte 0x17 #item ID
.byte 0x17 #item cost

#Bob-omb
.2byte 0x0118 #weight
.byte 0x18 #item ID
.byte 0x18 #item cost

#Paratroopa
.2byte 0x0119 #weight
.byte 0x19 #item ID
.byte 0x19 #item cost

#Snack
.2byte 0x011E #weight
.byte 0x1E #item ID
.byte 0x1E #item cost

#Boo-away
.2byte 0x011F #weight
.byte 0x1F #item ID
.byte 0x1F #item cost


.4byte 0 #padding for python program


afterPercentages:
#make r7 hold pointer to percentages
mflr r7
addi r7, r7, 4 #add 4 to skip over nop
add r8, r4, r0 #move pointer to item/coin table to r8

# Calculate the range of random values based on percentages
li r3, 0
li r10, 0
loop_calc:
    cmpwi r3, 88 # Exit at 22 items * 4 (4 being size of .4byte)
    beq- exit_calc
    lhzx r5, r7, r3 # Load the percentage for the current item using r3 as index
    add r10, r10, r5 # Add the percentage to the range of random values
    addi r3, r3, 4 # Increment index by 4 (size of an integer)
    b loop_calc
exit_calc:

rerollItem:
#odds total in r4
lis r5, 0x8014
ori r5, r5, 0xD348
mtctr r5
mr r3, r10 #odds total as func arg
bctrl

#rand int in r3

#get cur player coins
lwz r5, -0x6540 (r13) #cur player indedx
#get player coin count
mulli r5, r5, 264
lis r6, 0x8026
addi r6, r6, 22352
add r6, r6, r5
lha r0, 0x001C (r6) #cur player coins

# Select the item based on the random integer
li r4, 0
li r5, 0
loop_select:
    cmpwi r5, 88 # Exit at 22 items * 4 (4 being size of .4byte)
    beq- exit_select
    lhzx r6, r7, r5 # Load the percentage for the current item using r5 as index
    sub r3, r3, r6 # Subtract the percentage from the random integer
    cmpwi r3, 0 # Compare the updated random integer with 0
    bge+ loop_increment # If the updated random integer is greater than or equal to 0, continue to the next item
    #check if player can afford item
    mulli r9, r4, 4 #i * sizeof int
    addi r9, r9, 3
    lbzx r9, r7, r9 #get new item price
    cmpw r0, r9
    blt+ rerollItem
    b exit_select
loop_increment:
    addi r4, r4, 1 #iterator id increment
    addi r5, r5, 4 # Increment index by 4
    b loop_select
exit_select:
    mulli r9, r4, 4 #i * sizeof int
    add r9, r9, r7 #r9 now points to item id
    lbz r3, 0x0002 (r9) #get new item id
    lbz r5, 0x0003 (r9) #get new item price

    stw r3, 0x0000 (r8) #set new id (and return r3)
    stw r5, 0x0004 (r8) #set new price


exit:
lis r5, 0x801e
ori r5, r5, 0xa644
mtctr r5
bctrl
  blr 