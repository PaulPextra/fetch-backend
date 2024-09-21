from collections import defaultdict
from datetime import datetime

class PointsManager:
    def __init__(self):
        # Track the transactions
        self.transactions = []
        self.balance = defaultdict(int)

    def add_points(self, payer, points, timestamp):
        # Add the transaction and update the balance
        self.transactions.append({'payer': payer, 'points': points, 'timestamp': timestamp})
        self.transactions.sort(key=lambda x: x['timestamp'])  # Keep transactions sorted by timestamp
        self.balance[payer] += points

    def spend_points(self, points_to_spend):
        if points_to_spend > sum(self.balance.values()):
            raise ValueError("Insufficient points")

        spent_points = []
        for transaction in self.transactions:
            if points_to_spend <= 0:
                break

            payer = transaction['payer']
            available_points = transaction['points']

            if available_points > 0:
                spendable_points = min(available_points, points_to_spend)
                self.balance[payer] -= spendable_points
                transaction['points'] -= spendable_points
                spent_points.append({'payer': payer, 'points': -spendable_points})
                points_to_spend -= spendable_points

        return spent_points

    def get_balance(self):
        # Return current balance by payer
        return dict(self.balance)
