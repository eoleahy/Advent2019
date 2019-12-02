
import sys

def run_opcode(ops):


    for i in range(0, len(ops), 4):
        opcode = int(ops[i])
        #print(opcode)
        res = ops[0]

        if(opcode == 99):
            print("Value at 0:",ops[0])
            #print("Exiting...")
            return res

        elif(opcode == 1):
             
            ops[int(ops[i+3])] = int(ops[int(ops[i+1])]) + int(ops[int(ops[i+2])]) 


        elif(opcode == 2):

            ops[int(ops[i+3])] = int(ops[int(ops[i+1])]) * int(ops[int(ops[i+2])]) 



def main():

    with open("input.txt","r") as f:

        operations = f.read().split(",")      

        target = 19690720

        for noun in range(0,99):

            for verb in range(0,99):

                memory = operations.copy()
                memory[1] = noun
                memory[2] = verb
                #print(*operations)
                res = run_opcode(memory)
                if(res == target):
                    print("Found, Noun: {} , Verb: {}".format(noun,verb))
                    print((100 * noun) + verb)
                    sys.exit()

       

if __name__ == "__main__":
    main()