import json
import sys

try:
    filename=sys.argv[1]

except:
    print ("Missing script file")
    exit()

try:
    filename_srt=sys.argv[2]

except:
    print ("Missing subtitle file")
    exit()

if not filename.endswith(".txt"):
    print ("Invalid format, only accept txt files")
    exit()
    
if not filename_srt.endswith(".srt"):
    print ("Invalid format, only accept srt files")
    exit()

def load_file(filename):
    """ Load a file and return a list with all values
        encoding options for files= utf8 or latin-1
    """
    with open(filename, encoding='latin-1') as f:
        content = f.readlines()
    return content

def get_spaces(string):
    """ Get current string, and count the leading spaces and return that number
    """
    spaces_number=0
    # iterate over the string, and count spaces, if letter is not space, return
    # the current space_number var
    for letter in string:
        if letter == " ":
            spaces_number+=1
        else:
            return spaces_number

    return spaces_number

def get_script_clean(script_text):
    # switch to determine when save and when not
    print_enable=False
    # clear dict to returnt the data filter
    dialog_dict={}
    """
    Example text, the dialog is always like this.
    A space before, then the user with uppercase, and dialog after, then another spaces
    so the script evaluate when a upper text appear continuos from a no upper text and no space
    when a space appears, it mean that the dialogue ends

    ANATOLY
    Kasimov, Kasimov, good that you called
    us.
    """
    counter=0 # use as line counter
    # itinerate over the lines in the script
    for x in range(len(script_text)):
        # check if the next item in the list exist (for the last line of the text)
        if x+1 < len(script_text):
            # check if string is upper, then, check that the next line is not space
            # this condition is for all dialogs, the dialogs always has the
            #person in upper case, and the next line is always with text ,no spaces
            # then check that the contect of the line dont have any in lowercase
            if script_text[x].isupper() and not (script_text[x+1].isspace()):# and not (script_text[x+1].isupper()):
                #check that the sentense have less than 4 words (the person who spoke)
                if (len(script_text[x].strip().split())) <= 4:
                    print_enable=True

        # when current line is empty or 100% spaces, disable print
        elif script_text[x].isspace():
            print_enable=False

        if print_enable: # the current word match the criteria, is not
            if (get_spaces(script_text[x])) >= 15: # check leading spaces
                dialog=str(script_text[x]).strip()
                #print ("entre")
                if dialog.isupper(): # this is the autor of the dialog
                    counter+=1
                    dialog_dict[counter] = dialog + "***" # * to delimit the author from the dialog
                else: # this is the dialog
                    dialog_dict[counter] = dialog_dict[counter] +"\n"+ str(dialog)

    return dialog_dict

def get_srt_clean(srt_values):
    # format srt subtitles to dictionary
    lines_clean=[]
    # remove leading spaces in the end or the end of the items
    for item in srt_values:
        if item.strip():
            lines_clean.append(item.strip())


    result_dict={}
    temp_list=[]

    for item in lines_clean:
        if item.isnumeric(): # number of line
            if temp_list: # if list has data in it
                # save in the dictionary
                result_dict[id_dict] = temp_list

            id_dict = item # save the number of line in
            result_dict[id_dict] = ""
            temp_list =[]

        else:
            temp_list.append(item)

    return result_dict

def found_line(value,script_clean):
    if len(value)==0:return "","",""
    timeframe=value[0] # save timeframe
    del value[0] # remove timeframe
    #counter=0
    formated_text_speech=""
    for string in value:
        # clean string, remove commond charsets
        string = string.replace("<i>","").replace("</i>","")
        # itinerate over the script and search the word
        for key_script, value_script in script_clean.items():
            if string in value_script: # foudn word
                # remove the **** from dialog
                formated_text_speech = value_script.replace("***","")
                script_clean.pop(key_script)
                return script_clean,formated_text_speech,timeframe

    return script_clean,formated_text_speech,timeframe

def main():
    print ("Formating script:", filename)
    script_text = load_file(filename)
    script_clean = get_script_clean(script_text)

    print ("Formating subtitles:", filename_srt)
    srt_values = load_file(filename_srt)
    srt_clean = get_srt_clean(srt_values)

    global_result={}

    counter=0
    # itinerate over subtitles clear dict
    for key_srt, value_srt in srt_clean.items():
        # call function found_line sending the current subtitle and the entire script
        script_clean,values,timeframe = found_line(value_srt,script_clean)
        if values:
            # if found the dialog
            values=values.split("\n")
            actor=values[0] # get actor
            del values[0] # remove actor from list
            text_to_save=("\n".join(values)) # join the list
            key_srt = "Line " + key_srt
            # save the data in the dict, actor, line and time
            global_result[key_srt] = {"actor":actor,"line":text_to_save,"time":timeframe}

    details = json.dumps(global_result)
    print(json.dumps(global_result, indent = 2))

if __name__ == '__main__':
    main()
