gecko_code_mp6_jp_can_enter_shop_price_check = f"""
C21EA41C 00000001
2C030000 00000000
"""

gecko_code_mp6_us_can_enter_shop_price_check = f"""
C21EA8C0 00000001
2C030000 00000000
"""

gecko_code_mp6_pal_can_enter_shop_price_check = f"""
C21EA41C 00000001
2C030000 00000000
"""

can_enter_shop_mp6_gecko_codes = [gecko_code_mp6_jp_can_enter_shop_price_check, gecko_code_mp6_us_can_enter_shop_price_check, gecko_code_mp6_pal_can_enter_shop_price_check]

gecko_code_header_mp6_us = f"""
C21EAAE4 00000027
48000069 60000000
"""

gecko_code_footer_mp6_us = f"""
7CE802A6 38E70004
7D040214 38600000
39400000 2C030058
41820014 7CA71A2E
7D4A2A14 38630004
4BFFFFEC 3CA08014
60A5D348 7CA903A6
7D435378 4E800421
80AD9AC0 1CA50108
3CC08026 38C65750
7CC62A14 A806001C
38800000 38A00000
2C050058 41820038
7CC72A2E 7C661850
2C030000 40A0001C
1D240004 39290003
7D2748AE 7C004800
4180FFA4 48000010
38840001 38A50004
4BFFFFC8 1D240004
7D293A14 88690002
88A90003 90680000
90A80004 3CA0801E
60A5A644 7CA903A6
4E800421 4E800020
60000000 00000000
"""

gecko_code_header_mp6_pal = f"""
C21EA640 00000027
48000069 60000000
"""

gecko_code_footer_mp6_pal = f"""
7CE802A6 38E70004
7D040214 38600000
39400000 2C030058
41820014 7CA71A2E
7D4A2A14 38630004
4BFFFFEC 3CA08014
60A5CD78 7CA903A6
7D435378 4E800421
80AD9AC0 1CA50108
3CC08028 38C62E70
7CC62A14 A806001C
38800000 38A00000
2C050058 41820038
7CC72A2E 7C661850
2C030000 40A0001C
1D240004 39290003
7D2748AE 7C004800
4180FFA4 48000010
38840001 38A50004
4BFFFFC8 1D240004
7D293A14 88690002
88A90003 90680000
90A80004 3CA0801E
60A5A644 7CA903A6
4E800421 4E800020
60000000 00000000
"""

gecko_code_header_mp5_pal = f"""
C20C9968 00000024
9421FFF0 7C0802A6
90010014 93E10000
48000081 60000000
"""

gecko_code_header_mp5_us = f"""
C20C8FA0 00000024
9421FFF0 7C0802A6
90010014 93E10000
48000081 60000000
"""

gecko_code_footer_mp5_pal = f"""
7CE802A6 38E70004
38600000 38800000
2C030074 41820014
7CA71A2E 7C842A14
38630004 4BFFFFEC
3CA08003 60A5B0CC
7CA903A6 7C832378
4E800421 38800000
38A00000 2C050074
41820024 7CC72A2E
7C661850 2C030000
40A00008 48000010
38840001 38A50004
4BFFFFDC 1C840004
38840002 7C6720AE
83E10000 80010014
7C0803A6 38210010
4E800020 00000000
"""

gecko_code_footer_mp5_us = f"""
7CE802A6 38E70004
38600000 38800000
2C030074 41820014
7CA71A2E 7C842A14
38630004 4BFFFFEC
3CA08003 60A5B0F4
7CA903A6 7C832378
4E800421 38800000
38A00000 2C050074
41820024 7CC72A2E
7C661850 2C030000
40A00008 48000010
38840001 38A50004
4BFFFFDC 1C840004
38840002 7C6720AE
83E10000 80010014
7C0803A6 38210010
4E800020 00000000
"""

gecko_code_header_mp4_us = f"""
C2083878 0000001E
48000041 60000000
"""

gecko_code_header_mp4_pal = f"""
C2083724 0000001E
48000041 60000000
"""

gecko_code_footer_mp4_us = f"""
7CE802A6 38E70004
38600000 38800000
2C030034 41820014
7CA71A2E 7C842A14
38630004 4BFFFFEC
3CA08005 60A5FB40
7CA903A6 7C832378
4E800421 38800000
38A00000 2C050034
41820024 7CC72A2E
7C661850 2C030000
40A00008 48000010
38840001 38A50004
4BFFFFDC 1C840004
38840002 7C8720AE
3CA0817F 60A5FFF0
90850000 2C040008
41800008 38840001
3CA00007 60A5006D
7C642A14 38800000
38A00000 38A00000
60000000 00000000
C2083028 0000003D
48000195 0B596F75
10676F74 1061101E
054D696E 69104D75
7368726F 6F6D1E08
85FF000B 596F7510
676F7410 61101E05
4D656761 104D7573
68726F6F 6D1E0885
FF000B59 6F751067
6F741061 101E0553
75706572 104D696E
69104D75 7368726F
6F6D1E08 85FF000B
596F7510 676F7410
61101E05 53757065
72104D65 6761104D
75736872 6F6F6D1E
0885FF00 0B596F75
10676F74 1061101E
054D696E 69104D65
67611048 616D6D65
721E0885 FF000B59
6F751067 6F741061
101E0557 61727010
50697065 1E0885FF
000B596F 7510676F
74106110 1E055377
61701043 6172641E
0885FF00 0B596F75
10676F74 1061101E
05537061 726B7910
53746963 6B65721E
0885FF00 0B596F75
10676F74 1061101E
05476164 646C6967
68741E08 85FF000B
596F7510 676F7410
61101E05 43686F6D
70104361 6C6C1E08
85FF000B 596F7510
676F7410 61101E05
426F7773 65721053
7569741E 0885FF00
0B596F75 10676F74
1061101E 04437279
7374616C 1042616C
6C1E0885 FF000B59
6F751067 6F741061
101E074D 61676963
104C616D 701E0885
FF000000 7C6802A6
3C80817F 6084FFF0
80840000 38A00000
38C00000 7CE518AE
2C070000 40A20020
7C062000 41820020
7C632A14 38630001
38C60001 38A00000
4BFFFFDC 38A50001
4BFFFFD4 7C641B78
38600000 00000000
C2083CF0 00000002
3C80817F 6084FFF0
80840000 00000000
"""

gecko_code_footer_mp4_pal = f"""
7CE802A6 38E70004
38600000 38800000
2C030034 41820014
7CA71A2E 7C842A14
38630004 4BFFFFEC
3CA08005 60A5F8F4
7CA903A6 7C832378
4E800421 38800000
38A00000 2C050034
41820024 7CC72A2E
7C661850 2C030000
40A00008 48000010
38840001 38A50004
4BFFFFDC 1C840004
38840002 7C8720AE
3CA0817F 60A5FFF0
90850000 2C040008
41800008 38840001
3CA00007 60A5006D
7C642A14 38800000
38A00000 38A00000
60000000 00000000
C2082ED4 0000003D
48000195 0B596F75
10676F74 1061101E
054D696E 69104D75
7368726F 6F6D1E08
85FF000B 596F7510
676F7410 61101E05
4D656761 104D7573
68726F6F 6D1E0885
FF000B59 6F751067
6F741061 101E0553
75706572 104D696E
69104D75 7368726F
6F6D1E08 85FF000B
596F7510 676F7410
61101E05 53757065
72104D65 6761104D
75736872 6F6F6D1E
0885FF00 0B596F75
10676F74 1061101E
054D696E 69104D65
67611048 616D6D65
721E0885 FF000B59
6F751067 6F741061
101E0557 61727010
50697065 1E0885FF
000B596F 7510676F
74106110 1E055377
61701043 6172641E
0885FF00 0B596F75
10676F74 1061101E
05537061 726B7910
53746963 6B65721E
0885FF00 0B596F75
10676F74 1061101E
05476164 646C6967
68741E08 85FF000B
596F7510 676F7410
61101E05 43686F6D
70104361 6C6C1E08
85FF000B 596F7510
676F7410 61101E05
426F7773 65721053
7569741E 0885FF00
0B596F75 10676F74
1061101E 04437279
7374616C 1042616C
6C1E0885 FF000B59
6F751067 6F741061
101E074D 61676963
104C616D 701E0885
FF000000 7C6802A6
3C80817F 6084FFF0
80840000 38A00000
38C00000 7CE518AE
2C070000 40A20020
7C062000 41820020
7C632A14 38630001
38C60001 38A00000
4BFFFFDC 38A50001
4BFFFFD4 7C641B78
38600000 00000000
C2083B9C 00000002
3C80817F 6084FFF0
80840000 00000000
"""


# gecko_code_price_mp4_us = """
# 00139D2C 00000005
# 00139D2D 00000005
# 00139D2E 0000000F
# 00139D2F 0000000F
# 00139D30 0000000A
# 00139D31 0000000A
# 00139D32 0000000F
# 00139D33 0000000F
# 00139D34 0000000F
# 00139D35 0000000F
# 00139D36 00000000
# 00139D37 00000019
# 00139D38 00000020
# 00139D39 00000020
# """

item_and_id_mp6 = {
    "Mushroom": "0",         # 00000000
    "Super 'Shroom": "1",    # 00000001
    "Sluggish 'Shroom": "2", # 00000002
    "Metal Mushroom": "3",   # 00000003
    "Bullet Bill": "4",      # 00000004
    "Warp Pipe": "5",        # 00000005
    "Flutter": "6",          # 00000006
    "Cursed Mushroom": "7",  # 00000007
    "Spiny": "A",            # 0000000A
    "Goomba": "B",           # 0000000B
    "Piranha Plant": "C",    # 0000000C
    "Klepto": "D",           # 0000000D
    "Toady": "F",            # 0000000F
    "Kamek": "10",           # 00000010
    "Mr. Blizzard": "11",    # 00000011
    "Podoboo": "14",         # 00000014
    "Zap": "15",             # 00000015
    "Tweester": "16",        # 00000016
    "Thwomp": "17",          # 00000017
    "Bob-omb": "18",         # 00000018
    "Paratroopa": "19",      # 00000019
    "Snack": "1E",           # 0000001E
    "Boo-away": "1F",        # 0000001F
}

item_and_id_mp5 = {
    "Mushroom": "0",          # 00000000
    "Super Mushroom": "1",    # 00000001
    "Cursed Mushroom": "2",   # 00000002
    "Warp Pipe": "3",         # 00000003
    "Klepto": "4",            # 00000004
    "Bubble": "5",            # 00000005
    "Wiggler": "6",           # 00000006
    "Hammer Bro": "A",        # 0000000A
    "Coin Block": "B",        # 0000000B
    "Spiny": "C",             # 0000000C
    "Paratroopa": "D",        # 0000000D
    "Bullet Bill": "E",       # 0000000E
    "Goomba": "F",            # 0000000F
    "Bob-omb": "10",          # 00000010
    "Koopa Bank": "11",       # 00000011
    "Kamek": "14",            # 00000014
    "Mr. Blizzard": "15",     # 00000015
    "Piranha Plant": "16",    # 00000016
    "Magikoopa": "17",        # 00000017
    "Ukiki": "18",            # 00000018
    "Lakitu": "19",           # 00000019
    "Tweester": "1E",         # 0000001E
    "Duel": "1F",             # 0000001F
    "Chain Chomp": "20",      # 00000020
    "Bone": "21",             # 00000021
    "Bowser": "22",           # 00000022
    "Chance": "23",           # 00000023
    "Miracle": "24",          # 00000024
    "Donkey Kong": "25",      # 00000025
}

item_and_id_mp4 = {
    "Mini Mushroom": "0",       # 00000000
    "Mushroom": "1",            # 00000001
    "Super Mini": "2",          # 00000002
    "Super Mega": "3",          # 00000003
    "Mini-Mega Hammer": "4",    # 00000004
    "Warp Pipe": "5",           # 00000005
    "Swap Card": "6",           # 00000006
    "Sparky Sticker": "7",      # 00000007
    "Gaddlight": "8",           # 00000008
    "Chomp Call": "9",          # 00000009
    "Bowser Suit": "A",         # 0000000A
    "Boo Crystal Ball": "B",    # 0000000B
    "Magic Lamp": "C",          # 0000000C
}

#cost, weight, on/off checked
button_texts_mp6 = {
    "Mushroom": ("5", "0", "0"),
    "Super 'Shroom": ("5", "0", "0"),
    "Sluggish 'Shroom": ("5", "0", "0"),
    "Metal Mushroom": ("5", "0", "0"),
    "Bullet Bill": ("5", "0", "0"),
    "Warp Pipe": ("5", "0", "0"),
    "Flutter": ("5", "0", "0"),
    "Cursed Mushroom": ("5", "0", "0"),
    "Spiny": ("5", "0", "0"),
    "Goomba": ("5", "0", "0"),
    "Piranha Plant": ("5", "0", "0"),
    "Klepto": ("5", "0", "0"),
    "Toady": ("5", "0", "0"),
    "Kamek": ("5", "0", "0"),
    "Mr. Blizzard": ("5", "0", "0"),
    "Podoboo": ("5", "0", "0"),
    "Zap": ("5", "0", "0"),
    "Tweester": ("5", "0", "0"),
    "Thwomp": ("5", "0", "0"),
    "Bob-omb": ("5", "0", "0"),
    "Paratroopa": ("5", "0", "0"),
    "Snack": ("5", "0", "0"),
    "Boo-away": ("5", "0", "0")
}

button_texts_mp5 = {
    "Mushroom": ("5", "0", "0"),
    "Super Mushroom": ("5", "0", "0"),
    "Cursed Mushroom": ("5", "0", "0"),
    "Warp Pipe": ("5", "0", "0"),
    "Klepto": ("5", "0", "0"),
    "Bubble": ("5", "0", "0"),
    "Wiggler": ("5", "0", "0"),
    "Hammer Bro": ("5", "0", "0"),
    "Coin Block": ("5", "0", "0"),
    "Spiny": ("5", "0", "0"),
    "Paratroopa": ("5", "0", "0"),
    "Bullet Bill": ("5", "0", "0"),
    "Goomba": ("5", "0", "0"),
    "Bob-omb": ("5", "0", "0"),
    "Koopa Bank": ("5", "0", "0"),
    "Kamek": ("5", "0", "0"),
    "Mr. Blizzard": ("5", "0", "0"),
    "Piranha Plant": ("5", "0", "0"),
    "Magikoopa": ("5", "0", "0"),
    "Ukiki": ("5", "0", "0"),
    "Lakitu": ("5", "0", "0"),
    "Tweester": ("5", "0", "0"),
    "Duel": ("5", "0", "0"),
    "Chain Chomp": ("5", "0", "0"),
    "Bone": ("5", "0", "0"),
    "Bowser": ("5", "0", "0"),
    "Chance": ("5", "0", "0"),
    "Miracle": ("5", "0", "0"),
    "Donkey Kong": ("5", "0", "0")
}

button_texts_mp4 = {
    "Mini Mushroom": ("5", "0", "0"),
    "Mushroom": ("5", "0", "0"),
    "Super Mini": ("5", "0", "0"),
    "Super Mega": ("5", "0", "0"),
    "Mini-Mega Hammer": ("5", "0", "0"),
    "Warp Pipe": ("5", "0", "0"),
    "Swap Card": ("5", "0", "0"),
    "Sparky Sticker": ("5", "0", "0"),
    "Gaddlight": ("5", "0", "0"),
    "Chomp Call": ("5", "0", "0"),
    "Bowser Suit": ("5", "0", "0"),
    "Boo Crystal Ball": ("5", "0", "0"),
    "Magic Lamp": ("5", "0", "0")
}


#hex addresses, for gecko code 1 byte write
#jp, us, pal versions in order
#00 codetype to write 1 byte
#so actual address for MP4 US would be 0x801570B4
mp4_price_base_addresses = ["0", "0x001570B4", "0x00139D2C" ]

#04 codetype to write 4 bytes
mp5_price_base_addresses = ["0", "0x041CA21C", "0x041E8D94" ]

#mp6 doesn't use this
mp6_price_base_addresses = ["0", "0", "0" ]

price_base_addresses = [mp4_price_base_addresses, mp5_price_base_addresses, mp6_price_base_addresses]

gecko_code_mp4_headers = ["", gecko_code_header_mp4_us, gecko_code_header_mp4_pal]
gecko_code_mp4_footers = ["", gecko_code_footer_mp4_us, gecko_code_footer_mp4_pal]

gecko_code_mp5_headers = ["", gecko_code_header_mp5_us, gecko_code_header_mp5_pal]
gecko_code_mp5_footers = ["", gecko_code_footer_mp5_us, gecko_code_footer_mp5_pal]

gecko_code_mp6_headers = ["", gecko_code_header_mp6_us, gecko_code_header_mp6_pal]
gecko_code_mp6_footers = ["", gecko_code_footer_mp6_us, gecko_code_footer_mp6_pal]

gecko_code_headers = [gecko_code_mp4_headers, gecko_code_mp5_headers, gecko_code_mp6_headers]
gecko_code_footers = [gecko_code_mp4_footers, gecko_code_mp5_footers, gecko_code_mp6_footers]

item_names_and_ids_list = [item_and_id_mp4, item_and_id_mp5, item_and_id_mp6]
button_texts_list = [button_texts_mp4, button_texts_mp5, button_texts_mp6]