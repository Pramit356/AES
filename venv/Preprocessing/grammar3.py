def form_sentences(pos_list):
    temp = []
    sentences_tags = []
    for el in pos_list:
        if el[0]!='.':
            temp.append(el[1])
        else:
            sentences_tags.append(temp)
            temp = []
    return sentences_tags

def list_from_first_el(index, lst, dir):
    newList = []
    if dir == 'front':
        for i in range(index, len(lst)):
            newList.append(lst[i][0])
    else:
        for i in range(index+1):
            newList.append(lst[i][0])
    return newList


def find_noun_pronoun(index, leniency, lst):
    isJustified = False
    for i in range(index, index+leniency+1):
        if i<len(lst):
            if lst[i][0] == 'V' and lst[i]!='VBG':
                break
            elif lst[i][0] == 'N' or lst[i] in ['PRP', 'PRP$', 'VBG']:
                isJustified = True
                break
    return isJustified

def sentence_structure_errors(pos_list_grammar):
    tot_errors = 0
    tags_in_sentences = form_sentences(pos_list_grammar)
    #print(tags_in_sentences)
    for each_sentence in tags_in_sentences:
        errors = 0
        if 'V' not in list_from_first_el(0, each_sentence, 'front'):
            errors+=1
        for i in range(len(each_sentence)):
            if each_sentence[i][0] == 'J':
                isJustified = False
                if i!=len(each_sentence)-1 and each_sentence[i+1][0]=='N':
                    isJustified = True
                elif i!=len(each_sentence)-1 and ('PRP' in each_sentence[i+1:] or 'PRP$' in each_sentence[i+1:]):
                    isJustified = True
                elif i!=0 and (each_sentence[i-1][0]=='V' and 'N' in list_from_first_el(i-1, each_sentence, 'back')):
                    isJustified = True
                elif i!=0 and (each_sentence[i-1][0]=='V' and ('PRP' in each_sentence[:i] or 'PRP$' in each_sentence[:i])):
                    isJustified = True
                elif i!=0 and each_sentence[i-1][0]=='N':
                    isJustified = True
                elif i!=0 and ('PRP' in each_sentence[i-1] or 'PRP$' in each_sentence[i-1]):
                    isJustified = True
                elif i!=0 and each_sentence[i-1][0] == 'J':
                    if each_sentence[i-1] == 'JJR' or each_sentence[i] == 'JJR':
                        isJustified = False
                    else:
                        isJustified = True
                elif i>1 and each_sentence[i-2][0] == 'J':
                    if each_sentence[i-1] == 'JJR' or each_sentence[i] == 'JJR':
                        isJustified = False
                    else:
                        isJustified = True
                if isJustified == False:
                    errors+=1


            if each_sentence[i] == 'IN':          #Check prepositions
                if i==0 or i == len(each_sentence)-1:
                    errors+=1
                elif find_noun_pronoun(i+1, 3, each_sentence) == False:
                    errors+=1


            if each_sentence[i] == 'MD':
                isJustified = True
                for j in range(i+1, len(each_sentence)):
                    if each_sentence[j][0] == 'V' and each_sentence[j]!='VBG':
                        break
                    elif each_sentence[j] == 'TO':
                        isJustified = False
                        break
                if isJustified == False:
                    errors+=1
        if errors<=2:
            tot_errors+=errors
        else:
            tot_errors+=2
    return tot_errors

def check_verbal_agreement(essay, proximity):
    counter = 0
    errors = 0
    encountered = False
    tense = ''
    for i in range(len(essay)):
        if essay[i][0] == '.':
            encountered = False
            counter = 0
        if essay[i][1] in ['VBD', 'VBP', 'VBZ', 'MD']:
            if encountered == False:
                counter = 0
                if essay[i][1] in ['VBP', 'VBZ']:
                    tense = 'present'
                    encountered = True
                elif essay[i][1] == 'VBD':
                    tense = 'past'
                    encountered = True
                elif essay[i][1] == 'MD' and essay[i][0] in ['will', 'shall']:
                    tense = 'future'
                    encountered = True
            else:
                if essay[i][1] in ['VBP', 'VBZ'] and tense != 'present':
                    if counter<=proximity:
                        errors+=1
                    else:
                        counter = 0
                        tense = 'present'
                elif essay[i][1] == 'VBD' and tense != 'past':
                    if counter<=proximity:
                        errors+=1
                    else:
                        counter = 0
                        tense = 'past'
                elif essay[i][0] in ['will', 'shall'] and tense != 'future':
                    if counter<=proximity:
                        errors+=1
                    else:
                        counter = 0
                        tense = 'future'
                else:
                    if essay[i][1] in ['VBP', 'VBZ']:
                        counter = 0
                        tense = 'present'
                    elif essay[i][1] == 'VBD':
                        counter = 0
                        tense = 'past'
                    elif essay[i][1] in ['will', 'shall']:
                        counter = 0
                        tense = 'future'
        else:
            counter += 1
    return errors

# def check_subject_verb_agreement(essay):
#     for i in range(len(essay)):

def check_grammatical_errors(pos_list_with_punctuations, pos_list_without_punctuaions, score):
    incorrect = 0
    incorrect += sentence_structure_errors(pos_list_without_punctuaions)
    incorrect += check_verbal_agreement(pos_list_with_punctuations, 4)
    if (incorrect > 4 and incorrect <= 29):
        score -= (incorrect - 4)
    elif incorrect > 29:
        score -= 25
    return score

