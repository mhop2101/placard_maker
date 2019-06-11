import pyautogui
import time
import pandas
import datetime
import pyautogui as p


def nameWithCommittee():
    timen = datetime.datetime.now()
    names = NamesFile["Delegation"].tolist()
    print("Starting at: %s" % timen)
    total = len(NamesFile["Delegation"])
    current = 1
    for name in names:
        pyautogui.FAILSAFE = True
        print("-------------\n\nEditing....\n\n-------------")
        pyautogui.click(bg_text_x,bg_text_y)
        time.sleep(speed)
        pyautogui.click(name_text_x,name_text_y)
        pyautogui.click(name_text_x,name_text_y)
        pyautogui.typewrite(name,interval=0)
        time.sleep(speed)
        print("-------------\n\nSaving....\n\n-------------")
        pyautogui.click(file_x,file_y)
        time.sleep(speed)
        pyautogui.click(saveas_x,saveas_y)
        time.sleep(speed)
        pyautogui.click(filename_x,filename_y)
        pyautogui.click(filename_x,filename_y)
        time.sleep(speed)
        pyautogui.typewrite(name, interval=0)
        time.sleep(speed)
        pyautogui.click(saveastype_x,saveastype_y)
        time.sleep(speed)
        pyautogui.click(jpg_x,jpg_y)
        time.sleep(speed)
        pyautogui.click(save_x,save_y)
        time.sleep(speed)
        pyautogui.click(ok_x,ok_y)
        percentage = str(float((current / total) * 100)) + '%'
        percentage = percentage[0:4] + ' ' + percentage[-1]
        print("-------------\n\nSaved %s....\n\n-------------(%s/%s) ==> %s \n\n" % (name, current, total, percentage))
        current += 1

def getInitials(string):
    splitvar = string.split()
    for word in splitvar:
        if word.islower() == True:
            splitvar.remove(word)
    final = ""
    for word in splitvar:
        final = final + word[0]
    initial = ""
    for letter in final:
        initial = initial + letter + "."
    initial = initial[0:-1]
    return initial

def nameWithInitials():
    timen = datetime.datetime.now()
    NamesFile["Initials"] = NamesFile["Delegation"].apply(getInitials)
    names = NamesFile["Delegation"].tolist()
    initials = NamesFile["Initials"].tolist()
    print("Starting at: %s" % timen)
    total = len(NamesFile["Delegation"])
    current = 1
    for name, initial in zip(names,initials):
        pyautogui.FAILSAFE = True
        pyautogui.click(bg_text_x,bg_text_y)
        time.sleep(speed)
        pyautogui.click(bg_text_x,bg_text_y)
        pyautogui.click(bg_text_x,bg_text_y)
        pyautogui.typewrite(initial,interval=0.1)
        time.sleep(speed)
        pyautogui.click(name_text_x,name_text_y)
        pyautogui.click(name_text_x,name_text_y)
        pyautogui.typewrite(name,interval=0)
        time.sleep(speed)
        pyautogui.click(file_x,file_y)
        time.sleep(speed)
        pyautogui.click(saveas_x,saveas_y)
        time.sleep(speed)
        pyautogui.click(filename_x,filename_y)
        pyautogui.click(filename_x,filename_y)
        time.sleep(speed)
        pyautogui.typewrite(name, interval=0)
        time.sleep(speed)
        pyautogui.click(saveastype_x,saveastype_y)
        time.sleep(speed)
        pyautogui.click(jpg_x,jpg_y)
        time.sleep(speed)
        pyautogui.click(save_x,save_y)
        time.sleep(speed)
        pyautogui.click(ok_x,ok_y)
        percentage = str(float((current / total) * 100)) + '%'
        percentage = percentage[0:4] + ' ' + percentage[-1]
        print("-------------\n\nSaved %s....\n\n-------------(%s/%s) ==> %s \n\n" % (name, current, total, percentage))
        current += 1

def name_with_country_flag():
    counrtry_name_list = NamesFile["Countries"].tolist()
    timen = datetime.datetime.now()
    print("Starting at: %s" % timen)
    total = len(NamesFile["Countries"])
    current = 1
    for name in counrtry_name_list:
        pyautogui.FAILSAFE = True
        p.click(name_text_x,name_text_y)
        time.sleep(speed)
        p.doubleClick(name_text_x,name_text_y)
        p.typewrite(name,interval=0.1)
        p.click(bg_x,bg_y)
        time.sleep(speed)
        p.click(file_x,file_y)
        time.sleep(speed)
        p.click(placee_x,placee_y)
        time.sleep(speed)
        # custom to locate flags
        p.click(plq_x,plq_y)
        time.sleep(speed)
        p.doubleClick(script_x,script_y)
        time.sleep(speed)
        p.doubleClick(flags_x,flags_y)
        time.sleep(speed)
        p.click(search_x,search_y)
        time.sleep(speed)
        p.typewrite(name,interval=0.1)
        time.sleep(1)
        p.doubleClick(first_result_x,first_result_y)
        time.sleep(speed)
        # custom end
        p.click(place_x,place_y)
        time.sleep(1)
        pyautogui.click(corner_x,corner_y)
        pyautogui.dragTo(dragcorner_x, dragcorner_y, 2,button='left')
        time.sleep(1)
        pyautogui.click(corner_nd_x,corner_nd_y)
        pyautogui.dragTo(dragcorner_nd_x, dragcorner_nd_y, 2,button='left')
        time.sleep(speed)
        pyautogui.press('enter')
        time.sleep(0.7)
        p.click(fill_x,fill_y)
        time.sleep(0.7)
        p.click(fill_50_x,fill_50_y)
        time.sleep(0.7)
        pyautogui.click(file_x,file_y)
        time.sleep(speed)
        pyautogui.click(saveas_x,saveas_y)
        time.sleep(speed)
        pyautogui.click(filename_x,filename_y)
        pyautogui.click(filename_x,filename_y)
        time.sleep(speed)
        pyautogui.typewrite(name, interval=0)
        time.sleep(speed)
        pyautogui.click(saveastype_x,saveastype_y)
        time.sleep(speed)
        pyautogui.click(jpg_x,jpg_y)
        time.sleep(speed)
        pyautogui.click(save_x,save_y)
        time.sleep(speed)
        pyautogui.click(ok_x,ok_y)
        time.sleep(speed)
        p.click(bg_x,bg_y)
        time.sleep(speed)
        pyautogui.press('delete')
        time.sleep(1)
        percentage = str(float((current / total) * 100)) + '%'
        percentage = percentage[0:4] + ' ' + percentage[-1]
        print("-------------\n\nSaved %s....\n\n-------------(%s/%s) ==> %s \n\n" % (name, current, total, percentage))
        current += 1

bg_x = 1725
bg_y = 908

file_x = 1022
file_y = 17

placee_x = 1061
placee_y = 384

plq_x = 1316
plq_y = 50

script_x = 1323
script_y = 189

flags_x = 1234
flags_y = 164

search_x = 1762
search_y = 51

first_result_x = 1194
first_result_y = 135

place_x = 1738
place_y = 485

corner_x = 1263
corner_y = 566

dragcorner_x = 1060
dragcorner_y = 517

corner_nd_x = 1338
corner_nd_y = 604

dragcorner_nd_x = 1539
dragcorner_nd_y = 630

fill_x = 1866
fill_y = 744

fill_50_x = 1830
fill_50_y = 765

name_text_x = 1695
name_text_y = 817

saveas_x = 1075
saveas_y = 232

filename_x = 1277
filename_y = 330

saveastype_x = 1208
saveastype_y = 358

jpg_x = 1114
jpg_y = 504

save_x = 1747
save_y = 514

ok_x = 1396
ok_y = 284



print("Enter a value between 0.3 and 1")
print("0.3 ==> faster computers")
print("1   ==> slower computers")
speed = float(input())
while speed > 1 or speed < 0.3:
    print("Enter a value between 0.3 and 1")
    print("0.3 ==> faster computers")
    print("1   ==> slower computers")
    speed = float(input())
print("Enter the path or filename you would like to use ")
path = input()
NamesFile = pandas.read_csv(path)
# countries  first row == Countries
# characters first row == Delegation
print("Which function would you like to use: ")
print("1.Character name with background text initials")
print("2.Name with background text committee")
print("3.Country name with background flag")
option = int(input())
if option == 1:
    print("The current loaded file is: %s" % path)
    NamesFile["Initials"] = NamesFile["Delegation"].apply(getInitials)
    print(NamesFile)
    print("Is it correct ? Y/N")
    ynin = input()
    ynin.lower()
    if ynin == 'n':
        print("please correct it")
    elif ynin == 'y':
        nameWithInitials()
    else:
        print("err 1")
elif option == 2:
    nameWithCommittee()
elif option == 3:
    name_with_country_flag()
else:
    print("error")
