# config {stack,buffer,label} 
def get_features(config,sent_dict):
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
        # POS of first word in the buffer
        features.append('TOP_BUFF_POS_'+str(sent_dict['CPOSTAG'][config[1][-1]]))

    # second word in the buffer
    if len(config[1]) > 1:
        # token
        features.append('SEC_BUFF_TOKEN_'+str(sent_dict['FORM'][config[1][-2]].lower()))
        # POS 
        features.append('SEC_BUFF_POS_'+str(sent_dict['CPOSTAG'][config[1][-2]]))
        features.append('SEC_BUFF_POSTAG_'+str(sent_dict['POSTAG'][config[1][-2]]))

    # third word in the buffer
    if len(config[1]) > 2:
        # token
        features.append('THIRD_BUFF_TOKEN_'+str(sent_dict['FORM'][config[1][-3]].lower()))
        # POS
        features.append('THIRD_BUFF_POS_'+str(sent_dict['CPOSTAG'][config[1][-3]]))

    # fourth word in the buffer    
    if len(config[1]) > 3:
        # token
        features.append('FOURTH_BUFF_TOKEN_'+str(sent_dict['FORM'][config[1][-4]].lower()))
        # POS
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

    features.append('NOUN_COUNT_' + str(sent_dict['CPOSTAG'].count('NOUN')))
    features.append('PUNCT_COUNT_' + str(sent_dict['CPOSTAG'].count('PUNCT')))
    features.append('VERB_IND_' + str('VERB' in sent_dict['CPOSTAG']))
    features.append('WORD_COUNT_' + str(len(sent_dict['FORM']) 
        - sent_dict['CPOSTAG'].count('PUNCT')))

    features.append('SYM_IND_' + str(sent_dict['POSTAG'].count('SYM')))
    features.append('VBZ_IND_' + str(sent_dict['POSTAG'].count('VBZ')))
    features.append('VBN_IND_' + str(sent_dict['POSTAG'].count('VBN')))    
    features.append('WDT_IND_' + str(sent_dict['POSTAG'].count('WDT')))
    features.append('WP_IND_' + str(sent_dict['POSTAG'].count('WP')))
    features.append('WRB_IND_' + str(sent_dict['POSTAG'].count('WRB')))
    
    features.append('WP_POS_IND_' + str(sent_dict['POSTAG'].count('WP$')))
    features.append('FW_IND_' + str(sent_dict['POSTAG'].count('FW')))
    features.append('LS_IND_' + str(sent_dict['POSTAG'].count('LS')))
    features.append('UH_IND_' + str(sent_dict['POSTAG'].count('UH')))
    features.append('VBG_IND_' + str(sent_dict['POSTAG'].count('VBG')))

    return features
