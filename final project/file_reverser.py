"""file reverser
Oliver Rothe

Couldn't think of a 'big project' idea that filled all criteria,
so i made this small file to demonstrate my understanding of recursion, 
file IO, and exceptions"""

from pathlib import Path

#custom exception (I know, FileNotFound already exists as a basic exception)
class NoFileFoundError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def LoopDown(start, end, step, string: str, new_string = ""): #recursive loop to reverse a string
    if start < end:
        return new_string
    else:
        new_string = new_string + string[start]
        return LoopDown(start + step, end, step, string, new_string)

#setting up the CWD    
cwd = Path.cwd() 

#verifying the path exists to the input file
if Path.exists(Path(f"{cwd}/final project/file_in.txt")):
    file_to_read = Path(f"{cwd}/final project/file_in.txt")
else:
    #raise our custom error
    raise NoFileFoundError(f"no file found at address: {cwd}/final project/file_in.txt")

with open(file_to_read, "r") as file:
    file_line = file.readline()

#call the recursive reversing loop
reverse_line = LoopDown(len(file_line)-1, 0, -1, file_line)

#write reversed string to file
with open(f"{cwd}/final project/file_out.txt", "w+") as out_file:
    out_file.write(reverse_line)

# print(file_line)
# print(reverse_line)