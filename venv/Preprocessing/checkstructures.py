def sentence_proportion(essay, score):
    punctuations = ["'", '"', '.', ',', '?', '!']
    ct = 0
    mistakes = 0
    for word in essay:
        if(word in ['.', '?']):
            if(ct<8 or ct>20):
                mistakes+=1
            ct = 0
        else:
            if word not in punctuations:
                ct+=1
    if mistakes>40:
        score-=20
    else:
        score-=(mistakes/2)
    return score


def check_punctuations_capitalization(pos_list, score):
    mistakes = 0
    hasSeenVerb = False
    sinceFullStop = 0
    appostiveCommaAllowed = False
    openingQuotes = False

    for i in range(len(pos_list)):
        if sinceFullStop == 0:
            firstWord = pos_list[i]
        if pos_list[i][1][0] == 'V':
            hasSeenVerb = True

        if pos_list[i][0] == '.':
            sinceFullStop = 0
            if appostiveCommaAllowed == True:
                mistakes+=1
                appostiveCommaAllowed == False
            #Check for capitalization
            if  i!= len(pos_list)-1:
                if pos_list[i+1][0].islower() and pos_list[i+1][0][0]!='@':
                    nextCapital = False
                else:
                    nextCapital = True

                if hasSeenVerb == False or nextCapital == False:
                    #print(pos_list[i+1])
                    mistakes+=1
                else:
                    if pos_list[i+1][1] in ['NNP', 'NNPS']:
                        j=i+1
                        verbInside = False
                        while(j<len(pos_list)-1 and pos_list[j][0]!='.'):
                            if pos_list[j][1][0] == 'V':
                                verbInside = True
                                break
                            j+=1
                        if verbInside == False:
                            mistakes+=1

                hasSeenVerb = False

        elif pos_list[i][0] == ',':
            if i==0 or i==len(pos_list)-1:
                mistakes+=1
            else:
                isJustified = False

                if pos_list[i+1][1] == pos_list[i-1][1]:
                    isJustified = True
                elif pos_list[i+1][1][0] == pos_list[i-1][1][0] == 'N' and i+1!=len(pos_list)-1:
                    isJustified = True
                elif pos_list[i+1][1] == 'CC':
                    isJustified = True
                elif pos_list[i+1][0] in ['which', '"']:
                    isJustified = True
                #elif pos_list[i+1][0][1] == 'W':
                    #isJustified = True
                elif sinceFullStop>0 and sinceFullStop<=3 or pos_list[i+1][1] == 'IN':
                    #print(pos_list[i-1][0])
                    isJustified = True
                    appostiveCommaAllowed = True
                elif appostiveCommaAllowed == True:
                    #print(pos_list[i-1][0])
                    isJustified = True
                    appostiveCommaAllowed = False

                if(isJustified==False):
                    #print(pos_list[i-2:i+3])
                    mistakes+=1
        else:
            sinceFullStop+=1

        if pos_list[i][0] == '?':
            isJustified = False
            if firstWord[1][0] == 'V':
                isJustified = True
            elif firstWord[0].lower()=='how' or 'wh' in firstWord[0]:
                isJustified = True
            elif pos_list[i-3][0] == ',':
                isJustified = True
            elif openingQuotes == True:
                isJustified = True
            if isJustified==False:
                mistakes+=1

        if pos_list[i][0] in ["'", '"']:
            isJustified = False
            if openingQuotes == False:
                openingQuotes = True
                field = pos_list[i][0]
            else:
                openingQuotes = False
                if pos_list[i][0] == field:
                    isJustified = True
                elif pos_list[i-1][0] in ['?', '.']:
                    isJustified = True
                elif pos_list[i-1][0] == ',' and pos_list[i+2][1][0]=='V':
                    isJustified = True
                if isJustified==False:
                    mistakes+=1

    if pos_list[len(pos_list)-1][0] != '.' or hasSeenVerb == False:
        mistakes += 1
    #print('Mistakes: ', mistakes)
    if mistakes < 4:
        return score
    elif mistakes >= 4 and mistakes < 29:
        return score - mistakes + 4
    else:
        return score - 25