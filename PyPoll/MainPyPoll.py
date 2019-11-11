import os 
os.chdir("/Users/michellefitzpatrick/Python-Challenge")
import csv
csvpath = os.path.join("PyPoll", "election_data.csv")

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    total_votes = 0
    matrix =[]
    for row in csv_reader:
        matrix.append(row)
    total_votes = len(matrix)
    
    candidate_list = []
    
    khanvotes= 0
    correyvotes=0
    livotes=0
    otooleyvotes = 0

    for i in range(len(matrix)):
        candidate_list.append(matrix[i][2])
        if matrix[i][2] == "Khan":
            khanvotes = khanvotes + 1
        elif matrix[i][2] == "Correy":
            correyvotes = correyvotes + 1
        elif matrix[i][2] == "Li":
            livotes = livotes + 1
        else:
            otooleyvotes = otooleyvotes + 1

    print(khanvotes)
    print(correyvotes)
    print(livotes)
    print(otooleyvotes)

    candidate_unique_list = set(candidate_list)
    ok = list(candidate_unique_list)
    print(*ok, sep=', ')
    
    khan_percent = (khanvotes) /(total_votes)
    correy_percent = (correyvotes) / (total_votes)
    li_percent = (livotes) / (total_votes)
    otooley_percent = (otooleyvotes)/ (total_votes)

    khan_percent = "{:.3%}".format(khan_percent)
    correy_percent = "{:.3%}".format(correy_percent)
    li_percent = "{:.3%}".format(li_percent)
    otooley_percent = "{:.3%}".format(otooley_percent)

    print(khan_percent)
    print(correy_percent)
    print(li_percent)
    print(otooley_percent)

    maxwins = max([khanvotes, correyvotes, livotes, otooleyvotes])
    if maxwins == khanvotes:
        winner = "Khan"
    elif maxwins == correyvotes:
        winner = "Correy"
    elif maxwins == livotes:
        winner = "Li"
    else:
        winner = "O'Tooley"

    print(f"Election Results")
    print(f"--------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"--------------------------")
    print(f"Khan: {khan_percent} ({khanvotes})")
    print(f"Correy: {correy_percent} ({correyvotes})")
    print(f"Li:  {li_percent} ({livotes})")
    print(f"O'Tooley: {otooley_percent} ({otooleyvotes})")
    print(f"--------------------------")
    print(f"Winner: {winner} ({maxwins})")

PyPoll_Output = os.path.join('PyPoll','PyPollText.txt')
with open (PyPoll_Output, 'w') as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------- \n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"---------------------- \n")
    txtfile.write(f"Khan: {khan_percent} ({khanvotes})\n")
    txtfile.write(f"Correy: {correy_percent} ({correyvotes})\n")
    txtfile.write(f"Li:  {li_percent} ({livotes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent} ({otooleyvotes})\n")
    txtfile.write(f"---------------------- \n")
    txtfile.write(f"Winner: {winner} ({maxwins})")