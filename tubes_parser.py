def parser(sentence):

    tokens = sentence.split()
    tokens.append('EOS')

    non_terminals = ["S", "A", "B", "C", "D", "E", "F", "G"]
    terminals = ["for", ";", "=", "++", "--", "{", "}", "==", "!=", ">", "<", ">=", "<=", 
    "a", "b", "c", "0", "1", "2", "true", "false", "fmt.Print(a)", "a=a+b"]

    parse_table = {}

    parse_table[("S", "for")]           = ["for", "F", "A", "{", "G", "}"]
    parse_table[("S", ";")]             = ["error"] 
    parse_table[("S", "=")]             = ["error"] 
    parse_table[("S", "++")]            = ["error"] 
    parse_table[("S", "--")]            = ["error"]
    parse_table[("S", "{")]             = ["error"] 
    parse_table[("S", "}")]             = ["error"] 
    parse_table[("S", "==")]            = ["error"] 
    parse_table[("S", "!=")]            = ["error"]  
    parse_table[("S", ">")]             = ["error"] 
    parse_table[("S", "<")]             = ["error"] 
    parse_table[("S", ">=")]            = ["error"] 
    parse_table[("S", "<=")]            = ["error"] 
    parse_table[("S", "a")]             = ["error"] 
    parse_table[("S", "b")]             = ["error"] 
    parse_table[("S", "c")]             = ["error"] 
    parse_table[("S", "0")]             = ["error"] 
    parse_table[("S", "1")]             = ["error"] 
    parse_table[("S", "2")]             = ["error"] 
    parse_table[("S", "true")]          = ["error"] 
    parse_table[("S", "false")]         = ["error"] 
    parse_table[("S", "fmt.Print(a)")]  = ["error"]
    parse_table[("S", "a=a+b")]         = ["error"]
    parse_table[("S", "EOS")]           = ["error"] 

    parse_table[("A", "for")]           = ["error"]
    parse_table[("A", ";")]             = ["error"] 
    parse_table[("A", "=")]             = ["=", "E", ";", "B", ";", "F", "C"] 
    parse_table[("A", "++")]            = ["error"] 
    parse_table[("A", "--")]            = ["error"]
    parse_table[("A", "{")]             = ["error"] 
    parse_table[("A", "}")]             = ["error"] 
    parse_table[("A", "==")]            = ["D", "E"] 
    parse_table[("A", "!=")]            = ["D", "E"]  
    parse_table[("A", ">")]             = ["D", "E"] 
    parse_table[("A", "<")]             = ["D", "E"] 
    parse_table[("A", ">=")]            = ["D", "E"] 
    parse_table[("A", "<=")]            = ["D", "E"] 
    parse_table[("A", "a")]             = ["error"] 
    parse_table[("A", "b")]             = ["error"] 
    parse_table[("A", "c")]             = ["error"] 
    parse_table[("A", "0")]             = ["error"] 
    parse_table[("A", "1")]             = ["error"] 
    parse_table[("A", "2")]             = ["error"] 
    parse_table[("A", "true")]          = ["error"] 
    parse_table[("A", "false")]         = ["error"] 
    parse_table[("A", "fmt.Print(a)")]  = ["error"]
    parse_table[("A", "a=a+b")]         = ["error"]
    parse_table[("A", "EOS")]           = ["error"] 

    parse_table[("B", "for")]           = ["error"]
    parse_table[("B", ";")]             = ["error"] 
    parse_table[("B", "=")]             = ["error"] 
    parse_table[("B", "++")]            = ["error"] 
    parse_table[("B", "--")]            = ["error"]
    parse_table[("B", "{")]             = ["error"] 
    parse_table[("B", "}")]             = ["error"] 
    parse_table[("B", "==")]            = ["error"] 
    parse_table[("B", "!=")]            = ["error"]  
    parse_table[("B", ">")]             = ["error"] 
    parse_table[("B", "<")]             = ["error"] 
    parse_table[("B", ">=")]            = ["error"] 
    parse_table[("B", "<=")]            = ["error"] 
    parse_table[("B", "a")]             = ["F", "D", "E"] 
    parse_table[("B", "b")]             = ["F", "D", "E"] 
    parse_table[("B", "c")]             = ["F", "D", "E"] 
    parse_table[("B", "0")]             = ["error"] 
    parse_table[("B", "1")]             = ["error"] 
    parse_table[("B", "2")]             = ["error"] 
    parse_table[("B", "true")]          = ["error"] 
    parse_table[("B", "false")]         = ["error"] 
    parse_table[("B", "fmt.Print(a)")]  = ["error"]
    parse_table[("B", "a=a+b")]         = ["error"]
    parse_table[("B", "EOS")]           = ["error"] 

    parse_table[("C", "for")]           = ["error"]
    parse_table[("C", ";")]             = ["error"] 
    parse_table[("C", "=")]             = ["error"] 
    parse_table[("C", "++")]            = ["++"] 
    parse_table[("C", "--")]            = ["--"]
    parse_table[("C", "{")]             = ["error"] 
    parse_table[("C", "}")]             = ["error"] 
    parse_table[("C", "==")]            = ["error"] 
    parse_table[("C", "!=")]            = ["error"]  
    parse_table[("C", ">")]             = ["error"] 
    parse_table[("C", "<")]             = ["error"] 
    parse_table[("C", ">=")]            = ["error"] 
    parse_table[("C", "<=")]            = ["error"] 
    parse_table[("C", "a")]             = ["error"] 
    parse_table[("C", "b")]             = ["error"] 
    parse_table[("C", "c")]             = ["error"] 
    parse_table[("C", "0")]             = ["error"] 
    parse_table[("C", "1")]             = ["error"] 
    parse_table[("C", "2")]             = ["error"] 
    parse_table[("C", "true")]          = ["error"] 
    parse_table[("C", "false")]         = ["error"] 
    parse_table[("C", "fmt.Print(a)")]  = ["error"]
    parse_table[("C", "a=a+b")]         = ["error"]
    parse_table[("C", "EOS")]           = ["error"] 

    parse_table[("D", "for")]           = ["error"]
    parse_table[("D", ";")]             = ["error"] 
    parse_table[("D", "=")]             = ["error"] 
    parse_table[("D", "++")]            = ["error"] 
    parse_table[("D", "--")]            = ["error"]
    parse_table[("D", "{")]             = ["error"] 
    parse_table[("D", "}")]             = ["error"] 
    parse_table[("D", "==")]            = ["=="] 
    parse_table[("D", "!=")]            = ["!="]  
    parse_table[("D", ">")]             = [">"] 
    parse_table[("D", "<")]             = ["<"] 
    parse_table[("D", ">=")]            = [">="] 
    parse_table[("D", "<=")]            = ["<="] 
    parse_table[("D", "a")]             = ["error"] 
    parse_table[("D", "b")]             = ["error"] 
    parse_table[("D", "c")]             = ["error"] 
    parse_table[("D", "0")]             = ["error"] 
    parse_table[("D", "1")]             = ["error"] 
    parse_table[("D", "2")]             = ["error"] 
    parse_table[("D", "true")]          = ["error"] 
    parse_table[("D", "false")]         = ["error"] 
    parse_table[("D", "fmt.Print(a)")]  = ["error"]
    parse_table[("D", "a=a+b")]         = ["error"]
    parse_table[("D", "EOS")]           = ["error"] 

    parse_table[("E", "for")]           = ["error"]
    parse_table[("E", ";")]             = ["error"] 
    parse_table[("E", "=")]             = ["error"] 
    parse_table[("E", "++")]            = ["error"] 
    parse_table[("E", "--")]            = ["error"]
    parse_table[("E", "{")]             = ["error"] 
    parse_table[("E", "}")]             = ["error"] 
    parse_table[("E", "==")]            = ["error"] 
    parse_table[("E", "!=")]            = ["error"]  
    parse_table[("E", ">")]             = ["error"] 
    parse_table[("E", "<")]             = ["error"] 
    parse_table[("E", ">=")]            = ["error"] 
    parse_table[("E", "<=")]            = ["error"] 
    parse_table[("E", "a")]             = ["a"] 
    parse_table[("E", "b")]             = ["b"] 
    parse_table[("E", "c")]             = ["c"] 
    parse_table[("E", "0")]             = ["0"] 
    parse_table[("E", "1")]             = ["1"] 
    parse_table[("E", "2")]             = ["2"] 
    parse_table[("E", "true")]          = ["true"] 
    parse_table[("E", "false")]         = ["false"] 
    parse_table[("E", "fmt.Print(a)")]  = ["error"]
    parse_table[("E", "a=a+b")]         = ["error"]
    parse_table[("E", "EOS")]           = ["error"] 

    parse_table[("F", "for")]           = ["error"]
    parse_table[("F", ";")]             = ["error"] 
    parse_table[("F", "=")]             = ["error"] 
    parse_table[("F", "++")]            = ["error"] 
    parse_table[("F", "--")]            = ["error"]
    parse_table[("F", "{")]             = ["error"] 
    parse_table[("F", "}")]             = ["error"] 
    parse_table[("F", "==")]            = ["error"] 
    parse_table[("F", "!=")]            = ["error"]  
    parse_table[("F", ">")]             = ["error"] 
    parse_table[("F", "<")]             = ["error"] 
    parse_table[("F", ">=")]            = ["error"] 
    parse_table[("F", "<=")]            = ["error"] 
    parse_table[("F", "a")]             = ["a"] 
    parse_table[("F", "b")]             = ["b"] 
    parse_table[("F", "c")]             = ["c"] 
    parse_table[("F", "0")]             = ["error"] 
    parse_table[("F", "1")]             = ["error"] 
    parse_table[("F", "2")]             = ["error"] 
    parse_table[("F", "true")]          = ["error"] 
    parse_table[("F", "false")]         = ["error"] 
    parse_table[("F", "fmt.Print(a)")]  = ["error"]
    parse_table[("F", "a=a+b")]         = ["error"]
    parse_table[("F", "EOS")]           = ["error"] 

    parse_table[("G", "for")]           = ["error"]
    parse_table[("G", ";")]             = ["error"] 
    parse_table[("G", "=")]             = ["error"] 
    parse_table[("G", "++")]            = ["error"] 
    parse_table[("G", "--")]            = ["error"]
    parse_table[("G", "{")]             = ["error"] 
    parse_table[("G", "}")]             = ["error"] 
    parse_table[("G", "==")]            = ["error"] 
    parse_table[("G", "!=")]            = ["error"]  
    parse_table[("G", ">")]             = ["error"] 
    parse_table[("G", "<")]             = ["error"] 
    parse_table[("G", ">=")]            = ["error"] 
    parse_table[("G", "<=")]            = ["error"] 
    parse_table[("G", "a")]             = ["error"] 
    parse_table[("G", "b")]             = ["error"] 
    parse_table[("G", "c")]             = ["error"] 
    parse_table[("G", "0")]             = ["error"] 
    parse_table[("G", "1")]             = ["error"] 
    parse_table[("G", "2")]             = ["error"] 
    parse_table[("G", "true")]          = ["error"] 
    parse_table[("G", "false")]         = ["error"] 
    parse_table[("G", "fmt.Print(a)")]  = ["fmt.Print(a)"]
    parse_table[("G", "a=a+b")]         = ["a=a+b"]
    parse_table[("G", "EOS")]           = ["error"] 

    stack = []
    stack.append('#')
    stack.append('S')

    index_token = 0
    symbol = tokens[index_token]

    while(len(stack) > 0):
        top = stack[ len(stack) - 1 ]
        print('Top    = ', top)
        print('Symbol = ', symbol)
        if top in terminals:
            print('Top Adalah Simbol Terminal')
            if top == symbol:
                stack.pop()
                index_token = index_token + 1
                symbol = tokens[index_token]
                if symbol == "EOS":
                    stack.pop()
                    print('Isi Stack:', stack)
            else:
                print('ERROR')
                break;
        elif top in non_terminals:
            print('Top Adalah Simbol Non-Terminal')
            try:
                if parse_table[(top, symbol)][0] != 'error':
                    stack.pop()
                    symbol_to_be_pushed = parse_table[(top, symbol)]
                    for i in range(len(symbol_to_be_pushed)-1, -1, -1):
                        stack.append(symbol_to_be_pushed[i])
                else:
                    print('ERROR')
                    break;
            except:
                print('ERROR')
                break;
        else:
            print('ERROR')
            break;
        print('Isi Stack: ', stack)
        print()

    print()
    if symbol == 'EOS' and len(stack) == 0:
        print('Input Diterima')
    else:
        print('ERROR, Input Ditolak')  
    
    return parser

#Main Program Parser

"======= Contoh Input Diterima ======"
"for a = 0 ; a < 2 ; a ++ { fmt.Print(a) }"
"for a = 2 ; a >= 1 ; a -- { fmt.Print(a) }"
"for a <= 2 { a=a+b }"
"for a > 0 { fmt.Print(a) }"

"======= Contoh Input Ditolak ======"
"for a = 0 ; a < 2 ; a ++ { fmt.print(a) }"
"for a = 1 ; a >= 2 ; a -- fmt.Print(a)"
"for { a=a+b }"

#PERHATIAN!! Semua simbol yang ada di terminal tidak menggunakan spasi atau whitespace, jadi a=a+b tidak sama dengan a = a + b

print("====== Parser For Loop Golang ======")
sentence = "for a = 0 ; a < 2 ; a ++ { fmt.Print(a) }"
input_string = sentence+'#'
parser(sentence)
print("====================================")