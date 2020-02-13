def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    list1 = []
    for x in range(len(html)):
        if html[x] == "<":
            i = x
            html_tag = ""
            html_tag += ""
            while html[i] != ">":   #Run as long as the tag does not reach the closing tag
                html_tag += html[i] #Append our tag by the letter inside the brackets
                i += 1              #Increase i by one such that it runs its own loop without interfering with x
            html_tag += ">"         #If we reached the end of the while loop, we break
            list1.append(html_tag)  #Append our list with the entire tag
    return list1
            
        
def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    string = _extract_tags(html)   #Created a base list of strings that have the extracted tags
    s = []                         #Empty list to pop in and out of
    balanced = True                #Assumption that there is a balance in parenthesis unless otherwise
    
    for i in range(len(string)):
        symbol = string[i]         #setting a dummy variable to take o the value of the tag  
        if "/" not in symbol:      #checking if symbol is a closer or an opener
            s.append(symbol)       #appending the empty list
        else:
            if s == []:            #if s is an empty list, its not balanced
                balanced = False
            else:
                top = s.pop()      
                if top[1:]!=symbol[2:]:
                    balanced = False

    if balanced and s == []:
        return True
    else:
        return False

