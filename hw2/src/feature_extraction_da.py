# config {buffer,stack,label}
'''
0.9114285714285714
0.9130434782608695
'''
def get_features_da(config,sent_dict):
    features = []

    # distance between top of stack and first element in the buffer
    if len(config[0]) > 0 and len(config[1]) > 0:
        distance = config[0][-1] - config[1][-1]
        features.append('DISTANCE_STK_BUFF_' + str(distance))

    # distance between 2nd element on stack and second element in the buffer
    if len(config[0]) > 1 and len(config[1]) > 1:
        distance = config[0][-2] - config[1][-2]
        features.append('SEC_DISTANCE_STK_BUFF_' + str(distance))

    # first word in the buffer
    if len(config[1]) > 0:
        features.append('TOP_BUFF_TOKEN_'+str(sent_dict['FORM'][config[1][-1]].lower()))
        features.append('TOP_BUFF_POS_'+str(sent_dict['CPOSTAG'][config[1][-1]]))

    # second word in the buffer
    if len(config[1]) > 1:
        features.append('SEC_BUFF_TOKEN_'+str(sent_dict['FORM'][config[1][-2]].lower()))
        features.append('SEC_BUFF_POS_'+str(sent_dict['CPOSTAG'][config[1][-2]]))
        features.append('SEC_BUFF_POSTAG_'+str(sent_dict['POSTAG'][config[1][-2]]))

    # third word in the buffer
    if len(config[1]) > 2:
        features.append('THIRD_BUFF_TOKEN_'+str(sent_dict['FORM'][config[1][-3]].lower()))
        features.append('THIRD_BUFF_POS_'+str(sent_dict['CPOSTAG'][config[1][-3]]))

    # fourth word in the buffer    
    if len(config[1]) > 3:
        features.append('FOURTH_BUFF_TOKEN_'+str(sent_dict['FORM'][config[1][-4]].lower()))
        features.append('FOURTH_BUFF_POS_'+str(sent_dict['CPOSTAG'][config[1][-4]]))

    # top of stack word
    if len(config[0]) > 0:
        features.append('TOP_STK_TOKEN_'+str(sent_dict['FORM'][config[0][-1]].lower()))
        features.append('TOP_STK_POS_' + sent_dict['CPOSTAG'][config[0][-1]])
        features.append('TOP_STK_LEMMA_'+str(sent_dict['LEMMA'][config[0][-1]].lower())) 
        features.append('TOP_STK_POSTAG_' + sent_dict['POSTAG'][config[0][-1]])
        
    # 2nd item from top of stack
    if len(config[0]) > 1:
        # Top 2nd item of the stack
        features.append('TOP2_STK_TOKEN_'+str(sent_dict['FORM'][config[0][-2]].lower()))
        features.append('TOP2_STK_POS_'+str(sent_dict['CPOSTAG'][config[0][-2]]))

    # 3rd item from top of stack
    if len(config[0]) > 2:
        # Top 3rd item of the stack
        features.append('TOP3_STK_LEMMA_'+str(sent_dict['LEMMA'][config[0][-3]].lower()))    
        features.append('TOP3_STK_POS_'+str(sent_dict['CPOSTAG'][config[0][-3]]))    

    # is this a question or exclamation or neither (none)?
    def punctuation_type(sent_dict):
        if '!' in sent_dict['FORM']:
            return 1
        elif '?' in sent_dict['FORM']:
            return 2
        elif '.' in sent_dict['FORM']:
            return 3

    features.append('PUNCT_TYPE_' + str(punctuation_type(sent_dict)))
    features.append('VERB_IND_' + str('VERB' in sent_dict['CPOSTAG']))
    features.append('VERB_COUNT_' + str(sent_dict['CPOSTAG'].count('VERB')))
    features.append('WORD_TO_' + str('TO' in sent_dict['FORM']))
    
    return features
