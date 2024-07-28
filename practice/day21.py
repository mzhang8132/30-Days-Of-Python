# Day 21: 30 Days of python programming

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

class Statistics():
    def __init__ (self, arr):
        self.arr = arr

    def count(self):
        return len(self.arr)
    
    def sum(self):
        total = 0
        for i in self.arr:
            total += i
        return (total)
    
    def min(self):
        return sorted(self.arr)[0]
    
    def max(self):
        return sorted(self.arr)[-1]
    
    def range(self):
        ordered = sorted(self.arr)
        return ordered[-1] - ordered[0]
    
    def mean(self):
        return self.sum() / self.count()
    
    def median(self):
        length = self.count()
        ordered = sorted(self.arr)
        if length % 2 == 1:
            return ordered[length//2]
        else:
            return (ordered[(length//2) - 1] + ordered[length//2]) / 2
    
    def mode(self):
        occurances = {}
        for i in self.arr:
            if i in occurances.keys():
                occurances[i] += 1
            else:
                occurances[i] = 1
        ordered = [{"mode":k, "count":v} for k, v in sorted(occurances.items(), key = lambda x: x[1], reverse = True)]
        return ordered[0]        

    def std(self):
        avg = self.mean()
        length = self.count()
        var = 0
        for i in self.arr:
            var += (i - avg)**2
        return (var / length)**(1/2)

    def var(self):
        avg = self.mean()
        length = self.count()
        var = 0
        for i in self.arr:
            var += (i - avg)**2
        return var / length

    def freq_dist(self):
        occurances = {}
        length = self.count()
        for i in self.arr:
            if i in occurances.keys():
                occurances[i] += 1
            else:
                occurances[i] = 1
        ordered = [(v / length * 100, k) for k, v in sorted(occurances.items(), key = lambda x: x[1], reverse = True)]
        return ordered
    
    def describe(self):
        return (
            f"Count: {data.count()}\n"
            f"Sum: {data.sum()}\n"
            f"Min: {data.min()}\n"
            f"Max: {data.max()}\n"
            f"Range: {data.range()}\n"
            f"Mean: {data.mean()}\n"
            f"Median: {data.median()}\n"
            f"Mode: {data.mode()}\n"
            f"Standard Deviation: {data.std()}\n"
            f"Variance: {data.var()}\n"
            f"Frequency Distribution: {data.freq_dist()}"
        )

data = Statistics(ages)
print(f"Count: {data.count()}")
print(f"Sum: {data.sum()}")
print(f"Min: {data.min()}")
print(f"Max: {data.max()}")
print(f"Range: {data.range()}")
print(f"Mean: {data.mean()}")
print(f"Median: {data.median()}")
print(f"Mode: {data.mode()}")
print(f"Standard Deviation: {data.std()}")
print(f"Variance: {data.var()}")
print(f"Frequency Distribution: {data.freq_dist()}")
print(data.describe())

class PersonAccount(self):
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
    
    def total_income(self):
        total = 0
        for i in self.incomes:
            total += i[0]
        return total
    
    def total_expense(self):
        total = 0
        for i in self.expenses:
            total += i[0]
        return total

    def account_info(self):
        return (
            f"First name: {self.firstname}\n"
            f"Last name: {self.lastname}\n"
            f"Total income: {self.total_income()}\n"
            f"Total expense: {self.total_expense()}\n"
            f"Account balance: {self.account_balance()}"
        )

    def add_income(self, income):
        self.incomes.append(income)

    def add_expense(self, expense):
        self.expenses.append(expense)

    def account_balance(self):
        return self.total_income() - self.total_expense()
    