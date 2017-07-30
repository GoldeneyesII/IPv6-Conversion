###########################################################
#
#  IP v. 6 Conversion

# This script will convert a full IPv.6 address to the shortened version.
# It will also convert a shortened IPv.6 address to the full version.
#
##########################################################
from time import sleep

def main():
    '''Encapsulating function.'''

    message = ["Please provide the IP address to convert: ",
            "Please enter a valid IPv6 address: "]
    # Get ip number to convert
    ip = __get_user(message[0])
    while ip == False:
        __get_user(message[1])
    # Determine if ip is short or full
    if len(ip) < 32 and len(ip) > 1:
        lengthen(ip)
    elif len(ip) == 32:
        shorten(ip)
    else:
        print("Fatal Error!!! Input was not correctly validated.")
        raise FatalError

    # Return alternate version

def __get_user(message):
    '''Gets user input and validates it.'''
    usr = input(message).upper()
    try:
        if len(usr) < 2 or len(usr) > 32: raise LengthError
        if usr.count("::") > 1: raise ColonError
        [int(c, 16) for c in usr if c != ':']
        return usr
    except LengthError:
        print("The input was out of range.")
    except ColonError:
        print("Too many :: were input.")
    except ValueError:
        print("Invalid character.")
    return False

def lengthen(ip):
    '''Returns full-length IPv6 address as string.'''
    ip_segs = ip.split(":")
    for i in range(0, 8-len(ip_segs)):
        ip_segs.insert(index(""), "0000")
    ip_segs.pop(index(""))
    for seg in ip_segs:
        while len(seg) < 4:
            seg_lst = list(seg)
            seg_lst.insert(0, '0')
            seg = ''.join(seg_lst)
    return ":".join(ip_segs)

def shorten(ip):
    '''Returns shortened IPv6 address as string.'''
    ip_segs = []
    for seg in ip.split(":"):
        ip_segs.append(seg.lstrip("0"))
    short = ":".join(ip_segs)
    # Find longest run of ":"
    longest = 0
    length = 0
    for char in short:
        if char == ":":
            length += 1
        else:
            if longest < length: longest = length
            length = 0
    # Replace longest run of ":" with proper count
    run = ":"*longest
    mult = 1 if short.find(run) == 0 else 2
    short = short.replace(run, ":"*mult, 1)
    # Add in 0's to empty segments that are not part of the "::".
            

def fatality():
    print("Fatal Error!!! Input was not correctly validated.")
    print("Program will now close.")
    sleep(5)
    exit()

if __name__ == '__main__':
    main()
