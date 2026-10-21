"""Calculate DCA"""

from test import hex_to_rgb, print_hex, input_hex

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
        """Prints a beautifully formatted and colored investment report using custom print_hex."""

        # 定义你的主题颜色码
        theme_blue = "#00D4FA"
        profit_green = "#2ECC71"  # 漂亮的薄荷绿，用于盈利
        accent_gray = "#FFFFFF"   # 次要标签或分割线，用于制造视觉层次
        theme_white = "#FFFFFF"

        # 头部边框
        print_hex("=" * 40, theme_blue)
        print_hex("       DCA INVESTMENT REPORT       ", theme_blue)
        print_hex("=" * 40, theme_blue)

        strategy_type = "Split Monthly" if self.frequency == "monthly" else "Once a Year"

        # 基础策略信息（统一使用主题蓝）
        print_hex(f"Strategy:         ${self.annual_amount:,.2f}/year ({strategy_type})", theme_blue)
        print_hex(f"Expected Return:  {self.annual_rate * 100:.2f}% annual", theme_blue)
        print_hex(f"Duration:         {self.years} years", theme_blue)

        # 用次要灰色做分割线，让报告更有高级感
        print_hex("-" * 40, accent_gray)

        # 核心财务数据
        print_hex(f"Total Invested:   ${self.total_invested:,.2f}", theme_white)

        # 最终资产总值（突出展示）
        print_hex(f"Final Portfolio:  ${self.total_wealth:,.2f}", theme_white)

        # 净利润与回报率（使用绿色高亮展示）
        print_hex(f"Net Profit:       +${self.total_profit:,.2f}", profit_green)

        total_return_pct = (self.total_profit / self.total_invested) * 100
        print_hex(f"Total Return %:   {total_return_pct:.2f}%", profit_green)

        # 尾部边框
        print_hex("=" * 40, theme_blue)

# --- Main Execution Block ---
if __name__ == "__main__":
    print_hex("Welcome to the OOP DCA Calculator!", "#07F52E")

    try:
        theme = "#FFFFFF"

        # 直接像用普通的 input 一样用它，文字会自动变色！
        annual_rate_input = float(input_hex("Please enter your annual rate (e.g., 0.08 for 8%): ", theme))
        annual_amount_input = float(input_hex("Please enter your recurring investment (annual amount): ", theme))
        years_input = int(input_hex("Please enter investment duration (in years): ", theme))
        freq_input = input_hex("Choose frequency - 'monthly' or 'yearly' (default is monthly): ", theme).strip()

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
        print_hex("\n❌ Input Error: Please enter valid numbers!", "#3857BE")
