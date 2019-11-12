class Trade_list():
  def __init__(self, trades, index_offset=0, profit_offset=0):
    self.trades = trades
    self.profits = []
    self.time_line = []
    self.min_profit = float('inf')
    self.max_profit = float('-inf')
    self.parse_profits(index_offset, profit_offset)


  def parse_profits(self, index_offset, profit_offset):
    trade_sum = profit_offset
    mark_time_line = len(self.trades)//5
    for index, trade in enumerate(self.trades):
      if index % mark_time_line == 0:
        self.time_line.append([index + index_offset, trade[0][3]])
      else:
        self.time_line.append([index + index_offset, ""])
      trade_sum += float(trade[0][5])
      self.profits.append([index + index_offset, trade_sum])
      self.min_profit = min(trade_sum, self.min_profit)
      self.max_profit = max(trade_sum, self.max_profit)

