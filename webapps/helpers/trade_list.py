class Trade_list():
  def __init__(self, trades):
    self.trades = trades
    self.profits = []
    self.time_line = []
    self.min_profit = float('inf')
    self.max_profit = float('-inf')
    self.parse_profits()


  def parse_profits(self):
    trade_sum = 0
    mark_time_line = len(self.trades)//5
    for index, trade in enumerate(self.trades):
      if index % mark_time_line == 0:
        self.time_line.append([index, trade[0][3]])
      else:
        self.time_line.append([index, ""])
      trade_sum += float(trade[0][5])
      self.profits.append([index, trade_sum])
      self.min_profit = min(trade_sum, self.min_profit)
      self.max_profit = max(trade_sum, self.max_profit)

