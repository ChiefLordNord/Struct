from tokenizer import tokenize

def parse_factor(tokens):
    if tokens["tag"] == "number":
        return {
            "tag":"number",
            "value":tokens["value"]
        }, tokens[1:]
    raise Exception(f"Unexpected token '{tokens['tag']}' at position {tokens['position']}")

def test_parse_factor():
    """"
    factor = <number>
    """
    print("test parse factor")
    for s in ["1","22", "333"]:
        tokens = tokenize(s)
        ast, tokens = parse_factor(tokens)
        assert ast == {"tag":"number","value":int(s)}
        assert tokens[0]['tag'] == None
    tokens = tokenize("1")
    ast, tokens = parse_factor(tokens)
    assert ast == {"tag":"number","value":1}
    assert tokens[0]['tag'] == None
    print(ast)
    print(tokens)
    exit(0)

def parse_term(tokens):
    # Placeholder implementation for parse_term
    return {"tag": "number", "value": int(tokens[0]["value"])}, tokens[1:]

def test_parse_term():
    """
    term = factor (('*' | '/') factor)*
    """
    print("testing parse_term()")
    for s in ["1","22","333"]:
        tokens = tokenize(s)
        ast, tokens = parse_term(tokens)
        assert ast == {"tag":"number","value":int(s)}
        assert tokens[0]['tag'] == None

def test_parse_expresion():
    tokens = tokenize("1")
    print(tokens)
    exit(0)

if __name__ == "__main__":
    #test_parse_expresion()
    test_parse_factor()
    test_parse_term()
