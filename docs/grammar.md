# Grammar

The grammar for the language is as follows:

    <expr> ::= <term> | <term> "+" <expr>
    <term> ::= <factor> | <factor> "*" <term>
    <factor> ::= <number> | "(" <expr> ")" 

    <number> ::= <float> | <integer> | <scientific>
    <scientific> ::= <signed_float> "e" <signed_integer> | <float> "e" <signed_integer> | <integer> "e" <signed_integer>
    <float> ::= <digit>+ "." <digit>+
    <signed_float> ::= <sign> <float>
    <integer> ::= <digit> | <nonzero> <digits>
    <signed_integer> ::= <sign> <integer>
    <digits> ::= <digit> | <digit> <digits>

    <builtin_function> ::= "sin" | "cos" | "tan" | "cot" | "sec" | "csc" | "log" | "ln" | "sqrt" | "abs"
    <constant> ::= "pi" | "e"
    <operator> ::= "+" | "-" | "*" | "/" | "^"
    <nonzero> ::= "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" 
    <digit> ::= "0" | <nonzero>
    <sign> ::= "+" | "-"

    
