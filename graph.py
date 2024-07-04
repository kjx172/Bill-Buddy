class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_member(self, member):
        if member not in self.graph:
            self.graph[member] = {}
    
    def add_transaction(self, from_member, to_member, amount, reason):
        if from_member in self.graph and to_member in self.graph:
            if to_member in self.graph[from_member]:
                self.graph[from_member][to_member]['amount'] += amount
                self.graph[from_member][to_member]['transactions'].append((amount, reason))
            else:
                self.graph[from_member][to_member] = {
                    'amount': amount,
                    'transactions': [(amount, reason)]
                }
    
    '''
    def simplify_debts(self):
        # This method will contain the logic to simplify debts
        simplified_graph = {}
        for debtor, creditors in self.graph.items():
            for creditor, details in creditors.items():
                amount = details['amount']
                if creditor in self.graph and debtor in self.graph[creditor]:
                    if self.graph[creditor][debtor]['amount'] > amount:
                        self.graph[creditor][debtor]['amount'] -= amount
                        amount = 0
                    else:
                        amount -= self.graph[creditor][debtor]['amount']
                        del self.graph[creditor][debtor]
                if amount > 0:
                    if debtor not in simplified_graph:
                        simplified_graph[debtor] = {}
                    simplified_graph[debtor][creditor] = {
                        'amount': amount,
                        'transactions': details['transactions']
                    }
        self.graph = simplified_graph
    '''