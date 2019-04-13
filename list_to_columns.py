
#### cycles through a file of a list of jobs that take up 2 lines each,
##### with blank lines between
with open('list_for_script.txt', 'rb') as file:
    job = []
    for line in file:
        if len(job) == 2:
            #### prints out each pair of lines with order reversed
            print job[1] + "\t" + job[0]
            job = []
        if line.rstrip():
            job.append(line.rstrip())
