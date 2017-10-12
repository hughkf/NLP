import re
import numpy as np

# config {stack,buffer,label} 0.892000184897121
def get_features(config,sent_dict):
    features = []

    # TODO Improve Features
    
    # distance between top of stack and first element in the buffer
    if len(config[0]) > 0 and len(config[1]) > 0:
        distance = config[0][-1] - config[1][-1]
        features.append('DISTANCE_STK_BUFF_' + str(distance))

    # word first in the buffer
    if len(config[1]) > 0:
        # first element in buffer.
        first = config[1][-1]
        # Token
        features.append('TOP_BUFF_TOKEN_'+str(sent_dict['FORM'][first].lower()))

    # POS of first word in the buffer
    if len(config[1]) > 0:
        # first element in buffer.
        first = config[1][-1]
        # POS
        features.append('TOP_BUFF_POS_'+str(sent_dict['CPOSTAG'][first]))

    # top of stack word
    if len(config[0]) > 0:
        # Top of stack.
        top = config[0][-1]
        # Token
        features.append('TOP_STK_TOKEN_'+str(sent_dict['FORM'][top].lower()))
        features.append('TOP_STK_POS_' + sent_dict['CPOSTAG'][top])
        
    # 2nd item from top of stack
    if len(config[0]) > 1:
        # Top 2nd item of the stack
        top = config[0][-2]
        features.append('TOP2_STK_TOKEN_'+str(sent_dict['FORM'][top].lower()))
#        features.append(sent_dict['CPOSTAG'][top])

    # 3rd item from top of stack
    if len(config[0]) > 2:
        # Top 3rd item of the stack
        top = config[0][-3]
        features.append('TOP3_STK_TOKEN_'+str(sent_dict['FORM'][top].lower()))    
#        features.append(sent_dict['CPOSTAG'][top])
    
    def punctuation_type(sent_dict):
        if '!' in sent_dict['FORM']:
            return 1
        elif '?' in sent_dict['FORM']:
            return 2
        else:
            return 0

    features.append('PUNCT_TYPE_' + str(punctuation_type(sent_dict)))
    features.append('VERB_IND_' + str('VERB' in sent_dict['CPOSTAG']))
    features.append('WH_IND_' + str(len(set(sent_dict['FORM'])
        .intersection(set(['who', 'what', 'why', 'where', 'when']))) > 0))

#    def verb_forms(sent_dict):
#        f = lambda s: re.match('VB.*', s) is not None
#        return len([x for x in filter(f, sent_dict['POSTAG'])])
#    features.append(verb_forms(sent_dict))    
#    features.append(sent_dict['CPOSTAG'].count('VERB'))
#    features.append(1 if '!' in sent_dict['FORM'] else 0)
#    features.append(1 if 'PRON' in sent_dict['CPOSTAG'] else 0) # PRON
#    features.append(1 if 'NOUN' in sent_dict['CPOSTAG'] else 0)
#    features.append(1 if 'INTJ' in sent_dict['CPOSTAG'] else 0)

    return features
