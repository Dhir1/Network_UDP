Name: Dhir Talati

Phase: 1

Environment:
    - OS:       Windows
    - Language: Python
    - Language Version: 3.9
    - VisualStudio Code IDE

Supporting Files:
    1. server.py
    2. client.py


Compilation Instruction:
    - to start the server
        py.exe .\server.py 
    - to start client side
        py.ext .\client.py
    
Details:
    server.py
        - Basically creating a server to transfer data using UDP.
        - This server takes whatever the client side send, in thi case,
        - text, all lowercases. 
        - Then, turning those into uppercase letters.
        - Resend back to client side.

    client.py
        - This client allow, user to type in sentences, preferrably 
        - all lowercases.
        - Then, send to serverside, and receive serverside modified 
        - data, and print to the screen.

Reference:
    - code referenced from powerpoint slides provided by Professor.