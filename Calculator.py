"""Calculate DCA"""

__author__ = "Ray Hong"
__version__ = "1.0.0"

class InvestmentCalculator:
    def __init__(self, annual_rate: float, annual_amount: float, years: int, frequency: str = "monthly"):
        """
        Initializes the Dollar-Cost Averaging (DCA) calculator.
        :param annual_rate: Expected annual return rate (e.g., 0.08 for 8%).
        :param annual_amount: Total amount invested per year.
        :param years: Investment duration in years.
        :param frequency: Investment frequency ('monthly' or 'yearly').
        """
        self.annual_rate = annual_rate
        self.annual_amount = annual_amount
        self.years = years
        self.frequency = frequency.lower()
        
        # Internal state variables for results
        self.total_invested = 0.0
        self.total_wealth = 0.0
        self.total_profit = 0.0

    def calculate(self):
        """Calculates the compound interest based on the investment strategy."""
        if self.frequency == "monthly":
            # For monthly DCA: periods = years * 12, amount per period = annual amount / 12
            periods = self.years * 12
            periodic_amount = self.annual_amount / 12
            # Simple periodic rate calculation
            periodic_rate = self.annual_rate / 12 
        else:
            # For yearly DCA
            periods = self.years
            periodic_amount = self.annual_amount
            periodic_rate = self.annual_rate

        self.total_invested = periodic_amount * periods
        self.total_wealth = 0.0

        # Simulate the compounding process assuming contributions at the start of each period
        for _ in range(periods):
            self.total_wealth = (self.total_wealth + periodic_amount) * (1 + periodic_rate)
        
        self.total_profit = self.total_wealth - self.total_invested

    def display_results(self):
        """Prints a formatted investment report to the console."""
        print("\n" + "="*40)
        print("       DCA INVESTMENT REPORT       ")
        print("="*40)
        strategy_type = "Split Monthly" if self.frequency == "monthly" else "Once a Year"
        print(f"Strategy:         ${self.annual_amount:,.2f}/year ({strategy_type})\033[0m")
        print(f"Expected Return:  {self.annual_rate * 100:.2f}% annual")
        print(f"Duration:         {self.years} years")
        print("-"*40)
        print(f"Total Invested:   ${self.total_invested:,.2f}")
        print(f"Final Portfolio:  ${self.total_wealth:,.2f}")
        print(f"Net Profit:       ${self.total_profit:,.2f}")
        print(f"Total Return %:   {(self.total_profit / self.total_invested) * 100:.2f}%")
        print("="*40)


# --- Main Execution Block ---
if __name__ == "__main__":
    print("Welcome to the OOP DCA Calculator!")
    
    try:
        # Prompt user inputs with explicit type casting
        annual_rate_input = float(input("Please enter your annual rate (e.g., 0.08 for 8%): "))
        annual_amount_input = float(input("Please enter your recurring investment (annual amount): "))
        years_input = int(input("Please enter investment duration (in years): "))
        freq_input = input("Choose frequency - 'monthly' or 'yearly' (default is monthly): ").strip()
        
        if not freq_input:
            freq_input = "monthly"

        # Instantiate the object
        calculator = InvestmentCalculator(
            annual_rate=annual_rate_input,
            annual_amount=annual_amount_input,
            years=years_input,
            frequency=freq_input
        )
        
        # Execute business logic
        calculator.calculate()
        calculator.display_results()

    except ValueError:
        print("\n❌ Input Error: Please enter valid numbers!")