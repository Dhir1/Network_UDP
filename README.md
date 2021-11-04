Name: Dhir Talati Steven Tran Chris Newman Aaron Bernstein

Phase: 2

Environment:
    - OS:       Windows
    - Language: Python
    - Language Version: 3.9
    - VisualStudio Code IDE

Supporting Files:
    1. server.py
    2. client.py
    3. sample_bmp.bmp
    4. receivedSample_BMP.bmp


Compilation Instruction:
    - to start the server
        py.exe .\server.py 
    - to start client side
        py.ext .\client.py
    
Details:
    server.py
        - Basically creating a server to transfer data using UDP.
        - This server takes whatever the client side send, in this case,
        - packets created by the client.
        - For each packet, it prints SUCCESS status, and send that status
        - back to the client for feedback purpose.
        - Then, it extract received data.
        - Server side open the specified file on the specified path, and file
        - does not exist, it create and empty file.
        - It appened the data to the file.
        - Then, close the file, and print out "CONNECTION CLOSED" status.

    client.py
        - The client side open the specified file on the specified path.
        - Then it created multiple packets using make_packet function.
        - For each packet created, it send to the sever side using
        - send_data function.
        - It also receive the feedback from the server side.
        - Then print that feedback.
    

Reference:
    - Partial code referenced from powerpoint slides provided by Professor.