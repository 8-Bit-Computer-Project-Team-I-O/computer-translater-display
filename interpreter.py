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

# BT        INSTRUCTION     STEP    HLT MI  RI  RO  IO  II  AI  AO      ΣO  SU  BO  BI  OI  CE  CO  J
# FETCH     XXXX            000     0   1   0   0   0   0   0   0       0   0   0   0   0   0   1   0
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
# ADD       0010            011     0   0   0   1   0   0   0   0       0   0   0   1   0   0   0   0
#           0010            100     0   0   0   0   0   0   1   0       1   0   0   0   0   0   0   0
#
#           0011            010     0   1   0   0   1   0   0   0       0   0   0   0   0   0   0   0
# SUB       0011            011     0   0   0   1   0   0   0   0       0   0   1   0   0   0   0   0
#           0011            100     0   0   0   0   0   0   1   0       1   1   0   0   0   0   0   0
#
#           0100            010     0   1   0   0   1   0   0   0       0   0   0   0   0   0   0   0
# STA       0100            011     0   0   1   0   0   0   0   1       0   0   0   0   0   0   0   0
#           0100            100     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#
#           0101            010     0   0   0   0   1   0   1   0       0   0   0   0   0   0   0   0
# LDI       0101            011     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#           0101            100     0   0   0   0   0   0   0   0       0   0   0   0   0   0   0   0
#
#           0110            010     0   0   0   0   1   0   0   0       0   0   0   0   0   0   0   1
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
            voltage = 'Low Epoch'
            return voltage
        else:
            voltage = 'High Epoch'
            return voltage
    # return values[0]


def get_bus(values):
    # bus values, array of 8

    return values[1]


a_mc = ''
b_mc = ''
microcode = ''
instruction = ''


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
    if json_vals["BT Architecture"] == "False":
        mc_code = "micro_code_eater"
    else:
        mc_code = "micro_code_bastian"
    # get the current microcode values based on its current binary value
    current_mc = json_vals[mc_code][vals_array[2]][0]

    # this is a special case where a string gets output to the instruction register, the rest are digits
    if current_mc == "RO,II,CE":
        # get the upper 4 bits of the current bus value
        current_control_word = str(json_vals["control_words"][vals_array[1][0:4]][0])

        # get the lower 4 bits of the current bus value
        addressVal = vals_array[1][4:8]
        # fill in the associated control word interpretation with the lower 4 bus bits to representing the address
        current_control_word = current_control_word.replace("#", str(int(addressVal, 2)))

        # get the associated ui variable name associated with the micro code value
        current_change = json_vals[mc_code][vals_array[2]][1]

        # change that in the ui variable dict
        json_vals["ui_variables"][str(json_vals["ui_variables"]["memory_address_register"])] = str(json_vals["control_words"][vals_array[1][0:4]][1])
        json_vals["ui_variables"]["bus"] = int(addressVal, 2)
        # if clock epoch is high, counter is incremented
        if get_clock(vals_array) == "High Epoch":
            json_vals["ui_variables"]["program_counter"] += 1
            if json_vals["ui_variables"]["program_counter"] > 15:
                json_vals["ui_variables"]["program_counter"] = 0
            json_vals["ui_variables"][current_change] = current_control_word

    # for every other case
    else:

        # get the value that is currently being changed base on the current microcode binary
        current_change = json_vals[mc_code][vals_array[2]][1]
        # for most other value changes, very simply just convert the current bus binary and hold it in it's
        # respective dict placement
        if current_change != "none":
            json_vals["ui_variables"]["bus"] = convert_binary_to_int(mc_code, vals_array, json_vals)

            # the values are only actually changed to what is on the bus when the epoch is high
            if get_clock(vals_array) == "High Epoch":
                json_vals["ui_variables"][current_change] = convert_binary_to_int(mc_code, vals_array, json_vals)

            # when these micro code values are being run, it gives us a look into what is currently being stored in the
            # ram, so fill ram values with the respective bus value

            # ALSO REQUIRES A 2'S COMPLEMENT CHECK.
            if (json_vals[mc_code][vals_array[2]][0] == "RO, AI" or
                    json_vals[mc_code][vals_array[2]][0] == "RO, BI"):
                current_ram_address = json_vals["ui_variables"]["memory_address_register"]
                current_value = json_vals["ui_variables"][current_change]
                if json_vals["twosComplement"] == "True":
                    if current_value > 127:
                        current_value -= 256
                json_vals["ui_variables"][str(current_ram_address)] = current_value
        # if the current change is none, we don't want to change any of the values associated with the micro code
        else:
            #print("Do nothing")
            json_vals["ui_variables"]["bus"] = convert_binary_to_int(mc_code, vals_array, json_vals)

        # if the current change is the b_register or the a_register, we are also changing what is in the sum register
        # this will set it so that in case the subtraction flag gets set, it will only reupdate the sume register when
        # something gets put inside a or b to line up with how the computer actually works.

        # if the epoch is high, this is when the current change has been put into either the A or B register and
        # now needs to be represented on the sum register accordingly
        if current_change == "a_register" or current_change == "b_register" and get_clock(vals_array) == "High Epoch":
            sum_reg = json_vals["ui_variables"]["a_register"] + \
                      json_vals["ui_variables"]["b_register"]

            # this works almost exactly like the computer itself. If the current sum register value was
            # carried or equals zero, turn on a toggle bit that will send a value to the respective
            # flag register if the bit is set when sending the sum to the A register
            # note to add some if statements for if 2's complement is turned on
            if sum_reg > 255:
                # toggle the bit saying that the sum has been carried
                json_vals["ui_variables"]["carry_flag_toggle"] = 1

                # save what the carried value is
                sum_reg = sum_reg - 256

            else:
                json_vals["ui_variables"]["carry_flag_toggle"] = 0

            if sum_reg == 0:
                # toggle the bit saying that the sum is zero
                json_vals["ui_variables"]["zero_flag_toggle"] = 1

            else:
                json_vals["ui_variables"]["zero_flag_toggle"] = 0

            # update the sum register value in case it has changed
            json_vals["ui_variables"]["sum_register"] = sum_reg

        # If the subtract flag is set, we need to represent and refactor the
        # sum register and toggle bits now

        if current_change == "#" and get_clock(vals_array) == "High Epoch":
            current_ram_address = json_vals["ui_variables"]["memory_address_register"]

            # THIS REQUIRES A 2'S COMPLEMENT CHECK, only gets updated everytime .
            current_bus_val = json_vals["ui_variables"]["bus"]
            if json_vals[twosComplement] == "True":
                if current_bus_val > 127:
                    current_bus_val -= 256

            json_vals["ui_variables"][str(current_ram_address)] = current_bus_val

        if current_change == "a_register sub" and get_clock(vals_array) == "Low Epoch":
            # store a reference to the current subtraction
            sum_reg = json_vals["ui_variables"]["a_register"] - \
                      json_vals["ui_variables"]["b_register"]

            # toggle the right bits
            if sum_reg < 0:
                json_vals["ui_variables"]["carry_flag_toggle"] = 1
                sum_reg = sum_reg + 256
            else:
                json_vals["ui_variables"]["carry_flag_toggle"] = 0

            if sum_reg == 0:
                json_vals["ui_variables"]["zero_flag_toggle"] = 1
            else:
                json_vals["ui_variables"]["zero_flag_toggle"] = 0

            # update sum register and a register
            json_vals["ui_variables"]["sum_register"] = sum_reg

        if current_change == "a_register add" and get_clock(vals_array) == "Low Epoch":
            # store a reference to the current subtraction
            sum_reg = json_vals["ui_variables"]["a_register"] + \
                      json_vals["ui_variables"]["b_register"]

            # toggle the right bits
            if sum_reg > 255:
                json_vals["ui_variables"]["carry_flag_toggle"] = 1
                sum_reg = sum_reg - 256
            else:
                json_vals["ui_variables"]["carry_flag_toggle"] = 0

            if sum_reg == 0:
                json_vals["ui_variables"]["zero_flag_toggle"] = 1
            else:
                json_vals["ui_variables"]["zero_flag_toggle"] = 0

            # update sum register and a register
            json_vals["ui_variables"]["sum_register"] = sum_reg

        # if the subtraction flag is set and the voltage is high, we simply set any flags that there might be
        # and update the a register along with the sum register after the a register's value has been changed
        if current_change == "a_register sub" and get_clock(vals_array) == "High Epoch":

            if json_vals["ui_variables"]["carry_flag_toggle"] == 1:
                json_vals["ui_variables"]["carry_flag"] = 1
            else:
                json_vals["ui_variables"]["carry_flag"] = 0

            if json_vals["ui_variables"]["zero_flag_toggle"] == 1:
                json_vals["ui_variables"]["zero_flag"] = 1
            else:
                json_vals["ui_variables"]["zero_flag"] = 0

            # update sum register and a register
            json_vals["ui_variables"]["a_register"] = json_vals["ui_variables"]["sum_register"]
            sum_reg = json_vals["ui_variables"]["a_register"] - \
                      json_vals["ui_variables"]["b_register"]
            # update any changes after the subtraction
            # toggle the right bits
            if sum_reg < 0:
                json_vals["ui_variables"]["carry_flag_toggle"] = 1
                sum_reg = sum_reg + 256
            else:
                json_vals["ui_variables"]["carry_flag_toggle"] = 0

            if sum_reg == 0:
                json_vals["ui_variables"]["zero_flag_toggle"] = 1
            else:
                json_vals["ui_variables"]["zero_flag_toggle"] = 0

            # update sum register and a register
            json_vals["ui_variables"]["sum_register"] = sum_reg

        # if the microcode is just sum out and the epoch is high, there is no bookkeeping that needs to be done.
        # we only have to look at the toggled bits and set the respective flag registers
        if current_change == "a_register add" and get_clock(vals_array) == "High Epoch":

            # if the current sum register value was carried, set the carry flag, otherwise lift it
            if json_vals["ui_variables"]["carry_flag_toggle"] == 1:
                json_vals["ui_variables"]["carry_flag"] = 1
            else:
                json_vals["ui_variables"]["carry_flag"] = 0

            # if the current sum register value is zero, set the zero flag, otherwise lift it
            if json_vals["ui_variables"]["zero_flag_toggle"] == 1:
                json_vals["ui_variables"]["zero_flag"] = 1
            else:
                json_vals["ui_variables"]["zero_flag"] = 0

            # update sum register and a register
            json_vals["ui_variables"]["a_register"] = json_vals["ui_variables"]["sum_register"]
            sum_reg = json_vals["ui_variables"]["a_register"] + \
                                                        json_vals["ui_variables"]["b_register"]
            # toggle the right bits
            if sum_reg > 255:
                json_vals["ui_variables"]["carry_flag_toggle"] = 1
                sum_reg = sum_reg - 256
            else:
                json_vals["ui_variables"]["carry_flag_toggle"] = 0

            if sum_reg == 0:
                json_vals["ui_variables"]["zero_flag_toggle"] = 1
            else:
                json_vals["ui_variables"]["zero_flag_toggle"] = 0
            # update sum register and a register
            json_vals["ui_variables"]["sum_register"] = sum_reg


    if json_vals["twosComplement"] == "True":
        if json_vals["ui_variables"]["a_register"] > 127:
            json_vals["ui_variables"]["a_register_display"] = json_vals["ui_variables"]["a_register"] - 256
        else:
            json_vals["ui_variables"]["a_register_display"] = json_vals["ui_variables"]["a_register"]

        if json_vals["ui_variables"]["b_register"] > 127:
            json_vals["ui_variables"]["b_register_display"] = json_vals["ui_variables"]["b_register"] - 256
        else:
            json_vals["ui_variables"]["b_register_display"] = json_vals["ui_variables"]["b_register"]

        if json_vals["ui_variables"]["sum_register"] > 127:
            json_vals["ui_variables"]["sum_register_display"] = json_vals["ui_variables"]["sum_register"] - 256
        else:
            json_vals["ui_variables"]["sum_register_display"] = json_vals["ui_variables"]["sum_register"]

        # Only update the bus value's two's complement if it directly pertains to an integer value going into the a
        # register, b register, Output register, or some ram register
        if current_change == "a_register" or current_change == "a_register sub" or current_change == "a_register add" or current_change == "b_register" or current_change == "output_register" or current_change == "#":
            if json_vals["ui_variables"]["bus"] > 127:
                json_vals["ui_variables"]["bus_display"] = json_vals["ui_variables"][
                                                               "bus"] - 256
            else:
                json_vals["ui_variables"]["bus_display"] = json_vals["ui_variables"]["bus"]
        else:
            json_vals["ui_variables"]["bus_display"] = json_vals["ui_variables"]["bus"]

        # two's complement for the output register
        if json_vals["ui_variables"]["output_register"] > 127:
            json_vals["ui_variables"]["output_register_display"] = json_vals["ui_variables"]["output_register"] - 256
        else:
            json_vals["ui_variables"]["output_register_display"] = json_vals["ui_variables"]["output_register"]
    else:
        # the values do not change at all when two's complement is disabled. Just make them equal to the actual value.
        json_vals["ui_variables"]["a_register_display"] = json_vals["ui_variables"]["a_register"]
        json_vals["ui_variables"]["b_register_display"] = json_vals["ui_variables"]["b_register"]
        json_vals["ui_variables"]["sum_register_display"] = json_vals["ui_variables"]["sum_register"]
        json_vals["ui_variables"]["bus_display"] = json_vals["ui_variables"]["bus"]
        json_vals["ui_variables"]["output_register_display"] = json_vals["ui_variables"]["output_register"]

        # Update the layman's terms box to represent the current microcode operation every time.
    json_vals["ui_variables"]["laymans"] = str(json_vals[mc_code][vals_array[2]][3]).replace("#", str(
        json_vals["ui_variables"]["bus_display"]))
    json_vals["ui_variables"]["laymans"] = str(json_vals["ui_variables"]["laymans"].replace("&", str(
        json_vals["ui_variables"]["memory_address_register"])))

    print(json_vals["ui_variables"])

    return json_vals