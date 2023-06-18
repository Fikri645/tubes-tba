import string

def lexical(sentence):
    character_list = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + list(string.punctuation)
    state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30']
    transition_table = {}

    for state in state_list:
        for char in character_list:
            transition_table[(state, char)] = "error"
            transition_table[(state, "#")] = "error"
            transition_table[(state, " ")] = "error"

    transition_table[("q0", " ")] = "q0"
    transition_table[("q29", "#")] = "accept"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q3", "#")] = "accept"
    transition_table[("q3", " ")] = "q30"
    transition_table[("q7", "#")] = "accept"
    transition_table[("q7", " ")] = "q30"
    transition_table[("q8", "#")] = "accept"
    transition_table[("q8", " ")] = "q30"
    transition_table[("q9", "#")] = "accept"
    transition_table[("q9", " ")] = "q30"
    transition_table[("q30", "#")] = "accept"
    transition_table[("q30", " ")] = "q30"

    transition_table[("q0", "f")] = "q1"
    transition_table[("q1", "o")] = "q2"
    transition_table[("q2", "r")] = "q29"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q30", "f")] = "q1"

    transition_table[("q0", ";")] = "q29"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q30", ";")] = "q29"
    
    transition_table[("q0", "=")] = "q3"
    transition_table[("q3", " ")] = "q30"
    transition_table[("q30", "=")] = "q3"

    
    transition_table[("q0", "+")] = "q4"
    transition_table[("q4", "+")] = "q29"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q30", "+")] = "q4"
    
    transition_table[("q0", "-")] = "q5"
    transition_table[("q5", "-")] = "q29"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q30", "-")] = "q5"
    
    transition_table[("q0", "{")] = "q29"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q30", "{")] = "q29"
    
    transition_table[("q0", "}")] = "q29"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q30", "}")] = "q29"
    
    transition_table[("q0", "=")] = "q3"
    transition_table[("q3", "=")] = "q29"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q30", "=")] = "q3"
    
    transition_table[("q0", "!")] = "q6"
    transition_table[("q6", "=")] = "q29"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q30", "!")] = "q6"
    
    transition_table[("q0", ">")] = "q7"
    transition_table[("q7", " ")] = "q30"
    transition_table[("q30", ">")] = "q7"
    
    transition_table[("q0", "<")] = "q8"
    transition_table[("q8", " ")] = "q30"
    transition_table[("q30", "<")] = "q8"
    
    transition_table[("q0", ">")] = "q7"
    transition_table[("q7", "=")] = "q29"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q30", ">")] = "q7"
    
    transition_table[("q0", "<")] = "q8"
    transition_table[("q8", "=")] = "q29"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q30", "<")] = "q8"
    
    transition_table[("q0", "a")] = "q9"
    transition_table[("q9", " ")] = "q30"
    transition_table[("q30", "a")] = "q9"
    
    transition_table[("q0", "b")] = "q29"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q30", "b")] = "q29"
    
    transition_table[("q0", "c")] = "q29"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q30", "c")] = "q29"
    
    transition_table[("q0", "0")] = "q29"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q30", "0")] = "q29"
    
    transition_table[("q0", "1")] = "q29"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q30", "1")] = "q29"
    
    transition_table[("q0", "2")] = "q29"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q30", "2")] = "q29"

    transition_table[("q0", "t")] = "q10"
    transition_table[("q10", "r")] = "q11"
    transition_table[("q11", "u")] = "q12"
    transition_table[("q12", "e")] = "q29"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q30", "t")] = "q10"
    
    transition_table[("q0", "f")] = "q1"
    transition_table[("q1", "a")] = "q13"
    transition_table[("q13", "l")] = "q14"
    transition_table[("q14", "s")] = "q15"
    transition_table[("q15", "e")] = "q29"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q30", "f")] = "q1"
    
    transition_table[("q0", "f")] = "q1"
    transition_table[("q1", "m")] = "q16"
    transition_table[("q16", "t")] = "q17"
    transition_table[("q17", ".")] = "q18"
    transition_table[("q18", "P")] = "q19"
    transition_table[("q19", "r")] = "q20"
    transition_table[("q20", "i")] = "q21"
    transition_table[("q21", "n")] = "q22"
    transition_table[("q22", "t")] = "q23"
    transition_table[("q23", "(")] = "q24"
    transition_table[("q24", "a")] = "q25"
    transition_table[("q25", ")")] = "q29"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q30", "f")] = "q1"
    
    transition_table[("q0", "a")] = "q9"
    transition_table[("q9", "=")] = "q26"
    transition_table[("q26", "a")] = "q27"
    transition_table[("q27", "+")] = "q28"
    transition_table[("q28", "b")] = "q29"
    transition_table[("q29", " ")] = "q30"
    transition_table[("q30", "a")] = "q9"

    idx_char = 0
    state = 'q0'
    current_token = ''
    while state != 'accept':
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if (state=='q29' or (state=='q3' and input_string[idx_char+1]!='=') or (state=='q7' and input_string[idx_char+1]!='=') or (state=='q8' and input_string[idx_char+1]!='=') or (state=='q9' and input_string[idx_char+1]!='=')):
            print('Current Token: ', current_token, ', valid')
            current_token = ''
        if state =="error":
            print('Current Token: ', current_token, ', invalid')
            current_token = ''
            print('Terdapat token yang tidak valid, proses lexical analysis dihentikan')
            break
        idx_char = idx_char + 1

    if state == "accept":
        print('Semua Token yang Di-Input yaitu: [', sentence, '], valid')
    
    return lexical


"=====================TERMINAL======================"
"for", ";", "=", "++", "--", "{", "}", "==", "!=", ">", "<", ">=", "<=", 
"a", "b", "c", "0", "1", "2", "true", "false", "fmt.Print(a)", "a=a+b"
#PERHATIAN!! Semua simbol yang ada di terminal tidak menggunakan spasi atau whitespace, jadi a=a+b tidak sama dengan a = a + b
"==================================================="

sentence = "for ; = ++ -- { } == != > < >= <= a b c 0 1 2 true false fmt.Print(a) a=a+b"
input_string = sentence+'#'

lexical(sentence)
