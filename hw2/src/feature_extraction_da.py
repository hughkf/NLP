# config {buffer,stack,label}
def get_features_da(config,sent_dict):
    features = []

    # distance between top of stack and first element in the buffer
    if len(config[0]) > 0 and len(config[1]) > 0:
        distance = config[0][-1] - config[1][-1]
        features.append('DISTANCE_STK_BUFF_' + str(distance))

    # distance between 2nd element on stack and second element in the buffer
    if len(config[0]) > 1 and len(config[1]) > 1:
        distance = config[0][-2] - config[1][-2]
        features.append('SECOND_DISTANCE_STK_BUFF_' + str(distance))

    # first word in the buffer
    if len(config[1]) > 0:
        features.append('TOP_BUFF_TOKEN_'+str(sent_dict['FORM'][config[1][-1]].lower()))
        # POS of first word in the buffer
        features.append('TOP_BUFF_CPOSTAG_'+str(sent_dict['CPOSTAG'][config[1][-1]]))

    # second word in the buffer
    if len(config[1]) > 1:
        # token
        features.append('SECOND_BUFF_TOKEN_'+str(sent_dict['FORM'][config[1][-2]].lower()))
        # POS 
        features.append('SECOND_BUFF_CPOSTAG_'+str(sent_dict['CPOSTAG'][config[1][-2]]))
        features.append('SECOND_BUFF_POSTAG_'+str(sent_dict['POSTAG'][config[1][-2]]))

    # third word in the buffer
    if len(config[1]) > 2:
        # token
        features.append('THIRD_BUFF_TOKEN_'+str(sent_dict['FORM'][config[1][-3]].lower()))
        # POS
        features.append('THIRD_BUFF_CPOSTAG_'+str(sent_dict['CPOSTAG'][config[1][-3]]))

    # fourth word in the buffer    
    if len(config[1]) > 3:
        # token
        features.append('FOURTH_BUFF_TOKEN_'+str(sent_dict['FORM'][config[1][-4]].lower()))
        # POS
        features.append('FOURTH_BUFF_CPOSTAG_'+str(sent_dict['CPOSTAG'][config[1][-4]]))

    # top of stack word
    if len(config[0]) > 0:
        features.append('TOP_STK_TOKEN_'+str(sent_dict['FORM'][config[0][-1]].lower()))
        features.append('TOP_STK_CPOSTAG_' + sent_dict['CPOSTAG'][config[0][-1]])
        features.append('TOP_STK_LEMMA_'+str(sent_dict['LEMMA'][config[0][-1]].lower())) 
        features.append('TOP_STK_POSTAG_' + sent_dict['POSTAG'][config[0][-1]])
        
    # 2nd item from top of stack
    if len(config[0]) > 1:
        # Top 2nd item of the stack
        features.append('SECOND_STK_TOKEN_'+str(sent_dict['FORM'][config[0][-2]].lower()))
        features.append('SECOND_STK_CPOSTAG_'+str(sent_dict['CPOSTAG'][config[0][-2]]))

    # 3rd item from top of stack
    if len(config[0]) > 2:
        # Top 3rd item of the stack
        features.append('THIRD_STK_LEMMA_'+str(sent_dict['LEMMA'][config[0][-3]].lower()))    
        features.append('THIRD_STK_CPOSTAG_'+str(sent_dict['CPOSTAG'][config[0][-3]]))    

    features.append('VERB_IND_' + str('VERB' in sent_dict['CPOSTAG']))
    features.append('MD_IND_' + str('MD' in sent_dict['POSTAG']))
    features.append('UH_IND_' + str('UH' in sent_dict['POSTAG']))
    features.append('NOUN_COUNT_' + str('NOUN' in sent_dict['CPOSTAG']))
    features.append('VBG_IND_' + str('VBG' in sent_dict['POSTAG']))
    
    return features
