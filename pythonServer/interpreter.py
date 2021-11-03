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
        json_vals["ui_variables"][str(json_vals["ui_variables"]["memory_address_register"])] = current_control_word
        json_vals["ui_variables"]["bus"] = int(addressVal, 2)
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
            json_vals["ui_variables"]["bus"] = convert_binary_to_int(mc_code, vals_array, json_vals)
            json_vals["ui_variables"][current_change] = convert_binary_to_int(mc_code, vals_array, json_vals)

            # when these micro code values are being run, it gives us a look into what is currently being stored in the ram, so fill ram values with the respective bus value
            if (json_vals["micro_code_eater"][vals_array[2]][0] == "RO, AI" or json_vals["micro_code_eater"][vals_array[2]][0] == "RO, BI" or json_vals["micro_code_eater"][vals_array[2]][0] == "RI, AO"):
                current_ram_address=json_vals["ui_variables"]["memory_address_register"]
                json_vals["ui_variables"][str(current_ram_address)]=json_vals["ui_variables"][current_change]
        # if the current change is none, we don't want to change any of the values associated with the micro code
        else:
            print("Do nothing")
        # if the current change is the b_register or the a_register, we are also changing what is in the sum register, only do it if the epoch is high or else it will over add or subtract
        if current_change == "b_register" or current_change == "a_register" and get_clock(vals_array) == "high epoch":
            json_vals["ui_variables"]["sum_register"] = json_vals["ui_variables"]["a_register"] + \
                                                        json_vals["ui_variables"]["b_register"]
            # if the subtraction flag is set, subtract the current a nd b values, store them in the alu, then put them in the a register
        elif current_change == "a_register sub" and get_clock(vals_array) == "high epoch":
            json_vals["ui_variables"]["sum_register"] = json_vals["ui_variables"]["a_register"] - \
                                                        json_vals["ui_variables"]["b_register"]

            json_vals["ui_variables"]["a_register"] = json_vals["ui_variables"]["sum_register"]
    print(json_vals["ui_variables"])
    json_vals["ui_variables"]["laymans"] = json_vals[mc_code][vals_array[2]][3]
    return json_vals
