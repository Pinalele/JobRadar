class Posting:
    def __init__(self, title, company, location, max_salary, pay_period):
        self.title = title
        self.company = company
        self.location = location
        self.max_salary = max_salary
        self.pay_period = pay_period

    def city(self):
        """Return the city from a location like 'Lisbon, Portugal'."""
        if self.location == "United States":
            return "Remote / unspecified"
        else:
            return self.location.split(",")[0].strip()

    def annual_salary(self):
        if not self.max_salary:
            return None
        try:
            salary = float(self.max_salary)
        except ValueError:
            return None
        if self.pay_period == "YEARLY":
            return salary
        elif self.pay_period == "MONTHLY":
            return salary * 14
        elif self.pay_period == "HOURLY":
            return salary * 2080
        else:
            return None


    def summary(self):
        if self.annual_salary() is None:
            salary_text = "salary not available"
        else:
            salary_text = f"{self.annual_salary():,.2f}"

        return f'{self.title} @ {self.company} ({self.city()}): {salary_text}'

postings = [
    Posting("ML Engineer", "Acme AI Labs", "Lisbon, Portugal", "50.0", "HOURLY"),
    Posting("Data Scientist", "DataCo", "Porto, Portugal", "3000.0", "MONTHLY"),
    Posting("AI Engineer", "Robo Inc", "Braga, Portugal", "", ""),
]

for posting in postings:
    print(posting.summary())