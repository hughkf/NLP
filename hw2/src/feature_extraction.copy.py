# config {stack,buffer,label} 0.9281511895718024
def get_features(config,sent_dict):
    features = []

    # TODO Improve Features
    
    # distance between top of stack and first element in the buffer
    if len(config[0]) > 0 and len(config[1]) > 0:
        distance = config[0][-1] - config[1][-1]
        features.append('DISTANCE_STK_BUFF_' + str(distance))

    # first word in the buffer
    if len(config[1]) > 0:
        first = config[1][-1]
        # token
        features.append('TOP_BUFF_TOKEN_'+str(sent_dict['FORM'][first].lower()))
        # POS of first word in the buffer
        features.append('TOP_BUFF_POS_'+str(sent_dict['CPOSTAG'][first]))
#        features.append('TOP_BUFF_POSTAG_'+str(sent_dict['POSTAG'][first]))

    # second word in the buffer
    if len(config[1]) > 1:
        # token
        features.append('SEC_BUFF_TOKEN_'+str(sent_dict['FORM'][config[1][-2]].lower()))
        # POS 
        features.append('SEC_BUFF_POS_'+str(sent_dict['CPOSTAG'][config[1][-2]]))
#        features.append('SEC_BUFF_POSTAG_'+str(sent_dict['POSTAG'][config[1][-2]]))

    # third word in the buffer
    if len(config[1]) > 2:
        # token
        features.append('THIRD_BUFF_TOKEN_'+str(sent_dict['FORM'][config[1][-3]].lower()))
        # POS
        features.append('THIRD_BUFF_POS_'+str(sent_dict['CPOSTAG'][config[1][-3]]))
#        features.append('THIRD_BUFF_POSTAG_'+str(sent_dict['POSTAG'][config[1][-3]]))

    # fourth word in the buffer    
    if len(config[1]) > 3:
        # token
        features.append('FOURTH_BUFF_TOKEN_'+str(sent_dict['FORM'][config[1][-4]].lower()))
        # POS
        features.append('FOURTH_BUFF_POS_'+str(sent_dict['CPOSTAG'][config[1][-4]]))
#        features.append('FOURTH_BUFF_POSTAG_'+str(sent_dict['POSTAG'][config[1][-4]]))

    # third word in the buffer
    if len(config[1]) > 2:
        features.append('THIRD_BUFF_TOKEN_'+str(sent_dict['FORM'][config[1][-3]].lower()))
        # POS 
        features.append('THIRD_BUFF_POS_'+str(sent_dict['CPOSTAG'][config[1][-3]]))
#        features.append('THIRD_BUFF_POSTAG_'+str(sent_dict['POSTAG'][config[1][-3]]))

    # top of stack word
    if len(config[0]) > 0:
        # Top of stack.
        top = config[0][-1]
        # Token
        features.append('TOP_STK_TOKEN_'+str(sent_dict['FORM'][top].lower()))
        features.append('TOP_STK_POS_' + sent_dict['CPOSTAG'][top])
        features.append('TOP_STK_LEMMA_'+str(sent_dict['LEMMA'][top].lower())) # new
#        features.append('TOP_STK_POSTAG_' + sent_dict['POSTAG'][top])
        
    # 2nd item from top of stack
    if len(config[0]) > 1:
        # Top 2nd item of the stack
        top = config[0][-2]
        features.append('TOP2_STK_TOKEN_'+str(sent_dict['FORM'][top].lower()))
        features.append('TOP2_STK_POS_'+str(sent_dict['CPOSTAG'][config[0][-2]].lower()))
#        features.append('TOP2_STK_POSTAG_'+str(sent_dict['POSTAG'][config[0][-2]].lower()))

    # 3rd item from top of stack
    if len(config[0]) > 2:
        # Top 3rd item of the stack
        top = config[0][-3]
        features.append('TOP3_STK_TOKEN_'+str(sent_dict['LEMMA'][top].lower()))    

    def punctuation_type(sent_dict):
        if '!' in sent_dict['FORM']:
            return 1
        elif '?' in sent_dict['FORM']:
            return 2

#    features.append('PUNCT_' + str(re.match(r'[!@#$%^&*()?/.,;:~`<>"\\-_+={[|\]}]', sent_dict['TEXT']) is not None)) # new
    features.append('PUNCT_TYPE_' + str(punctuation_type(sent_dict)))
    features.append('VERB_IND_' + str('VERB' in sent_dict['CPOSTAG']))
    features.append('WH_IND_' + str(len(set(sent_dict['FORM'])
        .intersection(set(['who', 'what', 'why', 'where', 'when']))) > 0))

    return features
