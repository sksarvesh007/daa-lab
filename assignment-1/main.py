import random

def generator(n, lower, upper, output_file):
    with open(output_file, 'w') as file:
        for i in range(n):
            file.write(str(random.randint(lower, upper)) + '\n')

if __name__ == "__main__":
    input_file = str(input("Enter the name of the input file: "))
    output_file = str(input("Enter the name of the output file: "))

    try:
        with open(input_file, 'r') as file:
            n = int(file.readline().strip()) 
            lower = int(file.readline().strip())
            upper = int(file.readline().strip())
    except FileNotFoundError:
        print(f"File named {input_file} not found")
        exit(1)
    except ValueError:
        print("Invalid input in the file.")
        exit(1)

    generator(n, lower, upper, output_file)
    print(f"Random numbers generated successfully and saved to {output_file}")
