############################################
#
# Now, imagine you are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#

CV = [{'user': 'john', 'jobs': ['analyst', 'engineer']}, {'user': 'jane', 'jobs': ['finance', 'software']}, {'user': 'henry', 'jobs': ['finance', 'journalist']}]



# we will refer to this as a "CV".



# 4)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.


def has_experience_as(CVs, title):
    names = []
    for cv in CVs: 
        if title in cv['jobs']:
            names.append(cv['user'])
    
    return names


#
# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.


def job_counts(CVs):
   
    jobs = []

    for cv in CVs:
        jobs.extend(cv['jobs'])

    jobcounts = {}
    for job in set(jobs):
        jobcounts.update({job:jobs.count(job)})
    
    return jobcounts


#
# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.

def most_popular_job(CVs):
    
    jobs = job_counts(CVs)

    for item in jobs.items():
        if item[1] == max(jobs.values()):
            return item

