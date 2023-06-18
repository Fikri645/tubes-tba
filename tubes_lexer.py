import string

def lexical(sentence):
    character_list = list()
    state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'qf1', 'qf2']
    transition_table = {}

    # Transition definitions
    for state in state_list:
        for alphabet in character_list:
            transition_table[(state, alphabet)] = "error"
            transition_table[(state, "#")] = "error"
            transition_table[(state, " ")] = "error"

    transition_table[("q0", " ")] = "q0"
    transition_table[("qf1", "#")] = "accept"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("q5", "#")] = "accept"
    transition_table[("q5", " ")] = "qf2"
    transition_table[("q7", "#")] = "accept"
    transition_table[("q7", " ")] = "qf2"
    transition_table[("q8", "#")] = "accept"
    transition_table[("q8", " ")] = "qf2"
    transition_table[("q27", "#")] = "accept"
    transition_table[("q27", " ")] = "qf2"
    transition_table[("qf2", "#")] = "accept"
    transition_table[("qf2", " ")] = "qf2"

    transition_table[("q0", "f")] = "q1"
    transition_table[("q1", "o")] = "q2"
    transition_table[("q2", "r")] = "qf1"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("qf2", "f")] = "q0"

    transition_table[("q0", ";")] = "qf1"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("qf2", ";")] = "qf1"
    
    transition_table[("q0", "=")] = "q5"
    transition_table[("q5", " ")] = "qf2"
    transition_table[("qf2", "=")] = "q5"

    
    transition_table[("q0", "+")] = "q3"
    transition_table[("q3", "+")] = "qf1"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("qf2", "+")] = "q3"
    
    transition_table[("q0", "-")] = "q4"
    transition_table[("q4", "-")] = "qf1"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("qf2", "-")] = "q4"
    
    transition_table[("q0", "{")] = "qf1"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("qf2", "{")] = "qf1"
    
    transition_table[("q0", "}")] = "qf1"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("qf2", "}")] = "qf1"
    
    transition_table[("q0", "=")] = "q5"
    transition_table[("q5", "=")] = "qf1"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("qf2", "=")] = "q5"
    
    transition_table[("q0", "!")] = "q6"
    transition_table[("q6", "=")] = "qf1"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("qf2", "!")] = "q6"
    
    transition_table[("q0", ">")] = "q7"
    transition_table[("q7", " ")] = "qf2"
    transition_table[("qf2", ">")] = "qf1"
    
    transition_table[("q0", "<")] = "q8"
    transition_table[("q8", " ")] = "qf2"
    transition_table[("qf2", "<")] = "qf1"
    
    transition_table[("q0", ">")] = "q7"
    transition_table[("q7", "=")] = "qf1"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("qf2", ">")] = "q7"
    
    transition_table[("q0", "<")] = "q8"
    transition_table[("q8", "=")] = "qf1"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("qf2", "<")] = "q8"
    
    transition_table[("q0", "a")] = "q27"
    transition_table[("q27", " ")] = "qf2"
    transition_table[("qf2", "a")] = "qf1"
    
    transition_table[("q0", "b")] = "qf1"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("qf2", "b")] = "qf1"
    
    transition_table[("q0", "c")] = "qf1"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("qf2", "c")] = "qf1"
    
    transition_table[("q0", "0")] = "qf1"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("qf2", "0")] = "qf1"
    
    transition_table[("q0", "1")] = "qf1"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("qf2", "1")] = "qf1"
    
    transition_table[("q0", "2")] = "qf1"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("qf2", "2")] = "qf1"

    transition_table[("q0", "t")] = "q9"
    transition_table[("q9", "r")] = "q10"
    transition_table[("q10", "u")] = "q11"
    transition_table[("q11", "e")] = "qf1"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("qf2", "t")] = "q9"
    
    transition_table[("q0", "f")] = "q1"
    transition_table[("q1", "a")] = "q13"
    transition_table[("q13", "l")] = "q14"
    transition_table[("q14", "s")] = "q15"
    transition_table[("q15", "e")] = "qf1"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("qf2", "f")] = "q1"
    
    transition_table[("q0", "f")] = "q1"
    transition_table[("q1", "m")] = "q17"
    transition_table[("q17", "t")] = "q18"
    transition_table[("q18", ".")] = "q19"
    transition_table[("q19", "P")] = "q20"
    transition_table[("q20", "r")] = "q21"
    transition_table[("q21", "i")] = "q22"
    transition_table[("q22", "n")] = "q23"
    transition_table[("q23", "t")] = "q24"
    transition_table[("q24", "(")] = "q25"
    transition_table[("q25", "a")] = "q26"
    transition_table[("q26", ")")] = "qf1"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("qf2", "f")] = "q1"
    
    transition_table[("q0", "a")] = "q27"
    transition_table[("q27", "=")] = "q28"
    transition_table[("q28", "a")] = "q29"
    transition_table[("q29", "+")] = "q30"
    transition_table[("q30", "b")] = "qf1"
    transition_table[("qf1", " ")] = "qf2"
    transition_table[("qf2", "a")] = "q27"

    #Lexical Analysis
    idx_char = 0
    state = 'q0'
    current_token = ''
    while state != 'accept':
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if (state=='qf1' or (state=='q5' and input_string[idx_char+1]!='=') or (state=='q7' and input_string[idx_char+1]!='=') or (state=='q8' and input_string[idx_char+1]!='=') or (state=='q27' and input_string[idx_char+1]!='=')):
            print('CURRENT TOKEN  : ', current_token, ', valid')
            current_token = ''
        if state =="error":
            print('ERROR')
            break
        idx_char = idx_char + 1

    #Conclusion || state yang di accept
    if state == "accept":
        print('SEMUA TOKEN YANG DIINPUT : ', sentence, ', valid')
    
    return lexical


"=====================TERMINAL======================"
"for", ";", "=", "++", "--", "{", "}", "==", "!=", ">", "<", ">=", "<=", 
"a", "b", "c", "0", "1", "2", "true", "false", "fmt.Print(a)", "a=a+b"
"==================================================="

sentence = "for ; = ++ -- { } == != > < >= <= a b c 0 1 2 true false fmt.Print(a) a=a+b"
input_string = sentence+'#'

lexical(sentence)
