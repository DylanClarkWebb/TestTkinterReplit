def check_type(s, lbl):
    output = "String"
    
    try:
        int(s)
        output = "Integer"
    except ValueError:
        pass
    
    try:
        float(s)
        output = "Float"
    except ValueError:
        pass
    
    if s == "True" or s == "False":
        output = "Boolean"
    
    lbl["text"] = output
