# BE        INSTRUCTION     STEP    HLT MI  RI  RO  IO  II  AI  AO      ΣO  SU  BI  OI  CE  CO  J   FI
# FETCH     XXXX            000     0   1   0   0   0   0   0   0       0   0   0   0   0   1   0   0
#           XXXX            001     0   0   0   1   0   1   0   0       0   0   0   0   1   0   0   0
#
#           0000            010     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
# NOP       0000            011     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#           0000            100     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#
#           0001            010     0   1   0   0   1   0   0   0       0   0   0   0   0   0   0   0
# LDA       0001            011     0   0   0   1   0   0   1   0       0   0   0   0   0   0   0   0
#           0001            100     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#
#           0010            010     0   1   0   0   1   0   0   0       0   0   0   0   0   0   0   0
# ADD       0010            011     0   0   0   1   0   0   0   0       0   0   1   0   0   0   0   0
#           0010            100     0   0   0   0   0   0   1   0       1   0   0   0   0   0   0   1
#
#           0011            010     0   1   0   0   1   0   0   0       0   0   0   0   0   0   0   0
# SUB       0011            011     0   0   0   1   0   0   0   0       0   0   1   0   0   0   0   0
#           0011            100     0   0   0   0   0   0   1   0       1   1   0   0   0   0   0   1
#
#           0100            010     0   1   0   0   1   0   0   0       0   0   0   0   0   0   0   0
# STA       0100            011     0   0   1   0   0   0   0   1       0   0   0   0   0   0   0   0
#           0100            100     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#
#           0101            010     0   0   0   0   1   0   1   0       0   0   0   0   0   0   0   0
# LDI       0101            011     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#           0101            100     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#
#           0110            010     0   0   0   0   1   0   0   0       0   0   0   0   0   0   1   0
# JMP       0110            011     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#           0110            100     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#
#           1110            010     0   0   0   0   0   0   0   1       0   0   0   1   0   0   0   0
# OUT       1110            011     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#           1110            100     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#
#           1111            010     1   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
# HLT       1111            011     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#           1111            100     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0


# BT ARCHITECTURE MUST BE UPDATED TO REFLECT PROPER MICROCODE VALUES
# BT        INSTRUCTION     STEP    HLT MI  RI  RO  IO  II  AI  AO      ΣO  SU  BO  BI  OI  CE  CO  J
# FETCH     XXXX            000     0   1   0   0   0   0   0   0       0   0   0   0   0   1   0   0
#           XXXX            001     0   0   0   1   0   1   0   0       0   0   0   0   1   0   0   0
#
#           0000            010     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
# NOP       0000            011     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#           0000            100     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#
#           0001            010     0   1   0   0   1   0   0   0       0   0   0   0   0   0   0   0
# LDA       0001            011     0   0   0   1   0   0   1   0       0   0   0   0   0   0   0   0
#           0001            100     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#
#           0010            010     0   1   0   0   1   0   0   0       0   0   0   0   0   0   0   0
# ADD       0010            011     0   0   0   1   0   0   0   0       0   0   1   0   0   0   0   0
#           0010            100     0   0   0   0   0   0   1   0       1   0   0   0   0   0   0   1
#
#           0011            010     0   1   0   0   1   0   0   0       0   0   0   0   0   0   0   0
# SUB       0011            011     0   0   0   1   0   0   0   0       0   0   1   0   0   0   0   0
#           0011            100     0   0   0   0   0   0   1   0       1   1   0   0   0   0   0   1
#
#           0100            010     0   1   0   0   1   0   0   0       0   0   0   0   0   0   0   0
# STA       0100            011     0   0   1   0   0   0   0   1       0   0   0   0   0   0   0   0
#           0100            100     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#
#           0101            010     0   0   0   0   1   0   1   0       0   0   0   0   0   0   0   0
# LDI       0101            011     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#           0101            100     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#
#           0110            010     0   0   0   0   1   0   0   0       0   0   0   0   0   0   1   0
# JMP       0110            011     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#           0110            100     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#
#           1110            010     0   0   0   0   0   0   0   1       0   0   0   1   0   0   0   0
# OUT       1110            011     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#           1110            100     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#
#           1111            010     1   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
# HLT       1111            011     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#           1111            100     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0


voltage = ''


def get_clock(values):
    # one epoch, values of 0 and 1 to signify time passage
    global voltage

    for x in values:
        if x == '0':
            # epoch passed, discern between low and high epoch for now
            voltage = 'low epoch'
            return voltage
        else:
            voltage = 'high epoch'
            return voltage
    # return values[0]


def get_bus(values):
    # bus values, array of 8

    return values[1]


a_mc = ''
b_mc = ''
microcode = ''
instruction = ''


def get_mc(values):
    # microcode values, array of 16

    global voltage

    global a_mc
    global b_mc
    global microcode
    global instruction

    # Control whether cycle tests occur based on low/high epoch voltage (this helps oddities like NOP)
    if voltage == 'low epoch':

        # FETCH cycle test
        if '0100000000000100' in values and a_mc == '':
            a_mc = '0100000000000100'
            microcode = 'MI,CO'
            print("Microcode Instructions: " + microcode)
            print("Expected Instruction: FETCH")
        elif '0001010000001000' in values and a_mc == '0100000000000100':
            a_mc = ''
            microcode = 'RO,II,CE'
            instruction = 'FETCH'
            print("Microcode Instructions: " + microcode)
            return ("Instruction: " + instruction)

        # NOP cycle test
        if '0000000000000000' in values and a_mc == '':
            a_mc = '0000000000000000'
            microcode = ''
            print("Microcode Instructions: None")
            print("Expected Instruction: NOP")
        elif '0000000000000000' in values and a_mc == '0000000000000000' and b_mc == '':
            b_mc = '0000000000000000'
            microcode = ''
            print("Microcode Instructions: None")
            print("Expected Instruction: NOP")
        elif '0000000000000000' in values and a_mc == '0000000000000000' and b_mc == '0000000000000000':
            a_mc = ''
            b_mc = ''
            microcode = ''
            instruction = 'NOP'
            print("Microcode Instructions: None")
            return ("Instruction: " + instruction)

        # LDA cycle test
        if '0100100000000000' in values and a_mc == '':
            a_mc = '0100100000000000'
            microcode = 'MI,IO'
            print("Microcode Instructions: " + microcode)
            print("Expected Instruction: LDA, ADD, SUB, or STA")
        elif '0001001000000000' in values and a_mc == '0100100000000000' and b_mc == '':
            b_mc = '0001001000000000'
            microcode = 'RO,AI'
            print("Microcode Instructions: " + microcode)
            print("Expected Instruction: LDA")
        elif '0000000000000000' in values and a_mc == '0100100000000000' and b_mc == '0001001000000000':
            a_mc = ''
            b_mc = ''
            microcode = ''
            instruction = 'LDA'
            print("Microcode Instructions: None")
            return ("Instruction: " + instruction)

        # ADD cycle test
        if '0100100000000000' in values and a_mc == '':
            a_mc = '0100100000000000'
            microcode = 'MI,IO'
            print("Microcode Instructions: " + microcode)
            print("Expected Instruction: LDA, ADD, SUB, or STA")
        elif '0001000000100000' in values and a_mc == '0100100000000000' and b_mc == '':
            b_mc = '0001000000100000'
            microcode = 'RO,BI'
            print("Microcode Instructions: " + microcode)
            print("Expected Instruction: ADD or SUB")
        elif '0000001010000001' in values and a_mc == '0100100000000000' and b_mc == '0001000000100000':
            a_mc = ''
            b_mc = ''
            microcode = 'AI,ΣO'
            instruction = 'ADD'
            print("Microcode Instructions: " + microcode)
            return ("Instruction: " + instruction)

        # SUB cycle test
        if '0100100000000000' in values and a_mc == '':
            a_mc = '0100100000000000'
            microcode = 'MI,IO'
            print("Microcode Instructions: " + microcode)
            print("Expected Instruction: LDA, ADD, SUB, or STA")
        elif '0001000000100000' in values and a_mc == '0100100000000000' and b_mc == '':
            b_mc = '0001000000100000'
            microcode = 'RO,BI'
            print("Microcode Instructions: " + microcode)
            print("Expected Instruction: ADD or SUB")
        elif '0000001011000001' in values and a_mc == '0100100000000000' and b_mc == '0001000000100000':
            a_mc = ''
            b_mc = ''
            microcode = 'AI,ΣO,SU'
            instruction = 'SUB'
            print("Microcode Instructions: " + microcode)
            return ("Instruction: " + instruction)

        # STA cycle test
        if '0100100000000000' in values and a_mc == '':
            a_mc = '0100100000000000'
            microcode = 'MI,IO'
            print("Microcode Instructions: " + microcode)
            print("Expected Instruction: LDA, ADD, SUB, or STA")
        elif '0010000100000000' in values and a_mc == '0100100000000000' and b_mc == '':
            b_mc = '0010000100000000'
            microcode = 'RI,AO'
            print("Microcode Instructions: " + microcode)
            print("Expected Instruction: STA")
        elif '0000000000000000' in values and a_mc == '0100100000000000' and b_mc == '0010000100000000':
            a_mc = ''
            b_mc = ''
            microcode = ''
            instruction = 'STA'
            print("Microcode Instructions: None")
            return ("Instruction: " + instruction)

        # LDI cycle test
        if '0000101000000000' in values and a_mc == '':
            a_mc = '0000101000000000'
            microcode = 'IO,AI'
            print("Microcode Instructions: " + microcode)
            print("Expected Instruction: LDI")
        elif '0000000000000000' in values and a_mc == '0000101000000000' and b_mc == '':
            b_mc = '0000000000000000'
            microcode = ''
            print("Microcode Instructions: None")
            print("Expected Instruction: LDI")
        elif '0000000000000000' in values and a_mc == '0000101000000000' and b_mc == '0000000000000000':
            a_mc = ''
            b_mc = ''
            microcode = ''
            instruction = 'LDI'
            print("Microcode Instructions: None")
            return ("Instruction: " + instruction)

        # JMP cycle test
        if '0000100000000010' in values and a_mc == '':
            a_mc = '0000100000000010'
            microcode = 'IO,J'
            print("Microcode Instructions: " + microcode)
            print("Expected Instruction: JMP")
        elif '0000000000000000' in values and a_mc == '0000100000000010' and b_mc == '':
            b_mc = '0000000000000000'
            microcode = ''
            print("Microcode Instructions: None")
            print("Expected Instruction: JMP")
        elif '0000000000000000' in values and a_mc == '0000100000000010' and b_mc == '0000000000000000':
            a_mc = ''
            b_mc = ''
            microcode = ''
            instruction = 'JMP'
            print("Microcode Instructions: None")
            return ("Instruction: " + instruction)

        # OUT cycle test
        if '0000000100010000' in values and a_mc == '':
            a_mc = '0000000100010000'
            microcode = 'AO,OI'
            print("Microcode Instructions: " + microcode)
            print("Expected Instruction: OUT")
        elif '0000000000000000' in values and a_mc == '0000000100010000' and b_mc == '':
            b_mc = '0000000000000000'
            microcode = ''
            print("Microcode Instructions: None")
            print("Expected Instruction: OUT")
        elif '0000000000000000' in values and a_mc == '0000000100010000' and b_mc == '0000000000000000':
            a_mc = ''
            b_mc = ''
            microcode = ''
            instruction = 'OUT'
            print("Microcode Instructions: None")
            return ("Instruction: " + instruction)

        # HLT cycle test
        if '1000000000000000' in values:  # and a_mc == '':
            # a_mc = '1000000000000000'
            microcode = 'HLT'
            instruction = 'HLT'
            print("Microcode Instructions: " + microcode)
            return ("Instruction: " + instruction)
        # elif '0000000000000000' in values and a_mc == '1000000000000000' and b_mc == '':
        #     b_mc = '0000000000000000'
        #     microcode = ''
        #     print("Microcode Instructions: None")
        #     print("Expected Instruction: HLT")
        # elif '0000000000000000' in values and a_mc == '1000000000000000' and b_mc == '0000000000000000':
        #     a_mc = ''
        #     b_mc = ''
        #     microcode = ''
        #     instruction = 'HLT'
        #     print("Microcode Instructions: None")
        #     return("Instruction: " + instruction)

    else:
        return

    # No Instruction Found
    # else:
    #     print("ERROR: INVALID INSTRUCTION, EXITING PROGRAM")
    #     exit(1)

    # return values[2]


def convert_binary_to_int(mc_code, vals_array, json_vals):
    # the last index of the array the key leads to says the number of bits
    number_of_bits = json_vals[mc_code][vals_array[2]][2]
    # all 8 bits or the lower 4 bits
    starting_point = 8 - number_of_bits
    current_bus_val = get_bus(vals_array)
    int_conversion = int(current_bus_val[starting_point:8], 2)
    return int_conversion


def interpret(vals_array, json_vals):
    # check which microcode values to use
    if json_vals["BE Architecture"] == "False":
        mc_code = "micro_code_eater"
    else:
        mc_code = "micro_code_bastian"
    # get the current microcode values based on its current binary value
    current_mc = json_vals[mc_code][vals_array[2]][0]
    json_vals["ui_variables"]["bus"] = int(get_bus(vals_array), 2)
    # this is a special case where a string gets output to the instruction register, the rest are digits
    if current_mc == "RO,II,CE":
        # get the upper 4 bits of the current bus value
        current_control_word = str(json_vals["control_words"][vals_array[1][0:4]])
        # get the lower 4 bits of the current bus value
        addressVal = vals_array[1][4:8]
        # fill in the associated control word interpretation with the lower 4 bus bits to representing the address
        current_control_word = current_control_word.replace("#", str(int(addressVal, 2)))
        #int(binary_string, 2)

        # get the associated ui variable name assiciated with the micro code value
        current_change = json_vals[mc_code][vals_array[2]][1]

        # change that in the ui variable dict
        json_vals["ui_variables"][current_change] = current_control_word

        # if clock epoch is high, counter is incremented
        if get_clock(vals_array) == "high epoch":
            json_vals["ui_variables"]["program_counter"] += 1

    # for every other case
    else:

        # get the value that is currently being changed base on the current microcode binary
        current_change = json_vals[mc_code][vals_array[2]][1]
        # for most other value changes, very simply just convert the current bus binary and hold it in it's
        # respective dict placement
        if current_change != "none":
            json_vals["ui_variables"][current_change] = convert_binary_to_int(mc_code, vals_array, json_vals)
        # if the subtraction flag is set, subtract the current a nd b values, store them in the alu, then put them in a
        elif current_change == "a_register sub":
            json_vals["ui_variables"]["sum_register"] = json_vals["ui_variables"]["a_register"] - \
                                                        json_vals["ui_variables"]["b_register"]

            json_vals["ui_variables"]["sum_register"] = json_vals["ui_variables"]["sum_register"]

        # if the current change is none, we don't want to change any of the values associated with the micro code
        else:
            print("Do nothing")
        # if the current change is the b_register or the a_register, we are also changing what is in the sum register
        if current_change == "b_register" or current_change == "a_register":
            json_vals["ui_variables"]["sum_register"] = json_vals["ui_variables"]["a_register"] + \
                                                        json_vals["ui_variables"]["b_register"]
    print(json_vals["ui_variables"])
    json_vals["ui_variables"]["laymans"] = json_vals[mc_code][vals_array[2]][3]
    return json_vals

# DO INTERPRETATION IN HERE
# def interpret(vals_array):
#     print(get_clock(vals_array))
#     if get_clock(vals_array) == "0":
#         print("Epoch passed")
