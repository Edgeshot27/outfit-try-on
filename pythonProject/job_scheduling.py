class Job:
    def __init__(self,id,deadline,profit):
        self.id=id
        self.deadline=deadline
        self.profit=profit

def sorted_jobs(jobs):
    return sorted(jobs,key=lambda x:x.profit,reverse=True)

def max_dead(jobs):
    m=float('-inf')
    for job in jobs:
        m=max(m,job.deadline)
    return m

def scheduling(jobs):
    maxdead=max_dead(jobs)
    arr=[-1]*maxdead
    total=0
    for job in jobs:
        for i in range(job.deadline-1,-1,-1):
            if arr[i]==-1:
                arr[i]=job.id
                total+=job.profit
                break
    return total,arr
def main():
    jobs=[]
    n=int(input("Enter the number of jobs: "))
    for i in range(n):
        id=int(input('enter id:'))
        deadline=int(input('enter deadline:'))
        profit=int(input('enter profit:'))
        jobs.append(Job(id,deadline,profit))
    jobs=sorted_jobs(jobs)
    profit,assignment=scheduling(jobs)
    print('the max profit is:',profit)
    print('the assignment is:',assignment)

if __name__=='__main__':
    main()