# Program calculates the percentage of dialogue lines which have gotten
# a timestamp,
# these are the dialogue lines which are exactly the same in both the
# script as the .srt file

def calculate_matches(infile):
    # Open file
    with open(infile, 'r') as infile:
        output_file = infile.readlines()

    # Define matches and total number of dialogue lines
    matches = 0
    total = 0

    # For every dialogue line, increase total by 1
    # For every 'timestamp' increase matches by 1 (only matches
    # get a timestamp)
    for line in output_file:
        if '"D":' in line:
            total += 1
        elif '"timestamp":' in line:
            matches += 1

    # Calculate the percentage of dialogue lines which have a timestamp
    percentage_matches = round((matches / total) * 100, 2)
    return percentage_matches


def main():
    percentage_matches = calculate_matches('json_output.json')
    print(percentage_matches)


if __name__ == "__main__":
    main()
