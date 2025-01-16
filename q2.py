def count_words_in_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
           lines = infile.readlines()
        
        word_count = {}
        
        for line in lines:
            print(line.strip())
            words = line.strip().split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
        
        with open(output_file, 'w') as outfile:
            outfile.writelines(lines)
            outfile.write("\nWord_Count:\n")
            for word, count in word_count.items():
                outfile.write(f"{word}: {count}\n")
        
        print(f"\nWord counts saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_file = "input.txt"
output_file = "output.txt"

count_words_in_file(input_file, output_file)