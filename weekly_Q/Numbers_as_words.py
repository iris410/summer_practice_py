def read_numeber(integer):
    dict_special = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five',
    '6':'six', '7':'seven','8':'eight', '9':'nine', '10':'ten', '11':'eleven',
    '12':'twelve', '13':'thirteen','14':'fourteen', '15':'fifteen', '16':'sixteen',
    '17':'seventeen', '18':'eighteen', '19':'nineteen'}

    dict_tens = {'2':'twenty', '3':'thirty', '4':'forty', '5':'fifty', '6':'sixty',
    '7':'seventy','8':'eighty', '9':'ninety'}

    digit_list = ['','thousand','million','billion','trillion','quadrillion',
    'quintillion','sextillion']

    if integer == 0:
        print('zero')
        return 'zero'
    number_words = str(integer)#int -> string : O(log(N)) space (19)
    num_total = ''
    if len(number_words) % 3 !=0:
        num_zero = 3 - (len(number_words) % 3)
        number_words = "0" * num_zero + number_words
    #print(number_words[0])
    count = 0
    for i in range(len(number_words)-1,-1,-3):
        number_words_3 = number_words[i-2:i+1]
        read_three = []
        #print(number_words_3)
        if number_words_3[0] == '0':
            hundred = ''
        else:
            hundred = dict_special[number_words_3[0]] + " " + "hundred"
            read_three.append(hundred)
        if number_words_3[1] == '1':
                #print(number_words_3[1:3])
            ten = dict_special[number_words_3[1:3]]
            #read_three = (hundred + " " + ten)
            read_three.append(ten)
        else:
            if number_words_3[1] == '0':
                ten = ''
            else:
                ten = dict_tens[number_words_3[1]]
                read_three.append(ten)
            if number_words_3[2] == '0':
                one = ''
            else:
                one = dict_special[number_words_3[2]]
                read_three.append(one)
            #read_three = (hundred + " " + ten + " " + one).strip()
        read_three = ' '.join(read_three)

        if len(read_three) > 0:
            read_three = read_three + ' ' + digit_list[count]

        num_total = read_three + ' ' + num_total
        count += 1
    print(num_total.strip())
    return num_total.strip()

    # for i in range(0,len(number_words),3):
    #     number_words_3 = number_words[i:i+3]
    #     print(number_words_3)
    #     if number_words_3[0] != '0':
    #         hundred = dict[number_words_3[0]] + " " + "hundred"
    #     else:
    #         hundred = ''
    #     if number_words_3[1] == '1':
    #         #print(number_words_3[1:3])
    #         ten = dict[number_words_3[1:3]]
    #         read_three = (hundred + " " + ten)
    #     else:
    #         if number_words_3[1] == '0':
    #             ten = ''
    #         else:
    #             ten = dict_tenth[number_words_3[1]]
    #         one = dict[number_words_3[2]]
    #         read_three = (hundred + " " + ten + " " + one).strip()
    #     three += read_three + ' '
    # print(three)
test_list = [21234567890 #21,234,567,890
,10
,110
,0
,5050
,50515
,50000
,50000000 #50,000,000
,50505]
for i in test_list:
    print(i)
    read_numeber(i)
    print('\n')
