INDENTS = 4


def print_hanging_indents(poem):
    
    index_next_line = False # a flag to track whether we should indent the next line
    lines = poem.split('\n')
    
    for line in lines:
        if line == '':
            index_next_line = False # the falg turned off to prevent indentation - if the line is empty
        else:
            if index_next_line:
                print(' ' * INDENTS + line.lstrip())
            
            else:
                print(line.lstrip())
        
            index_next_line = True
    
    
    
poem = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """


rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """
print(print_hanging_indents(poem))