class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_member(self, member):
        if member not in self.graph:
            self.graph[member] = {}

    def remove_member(self, member):
        if member in self.graph:
            # Remove the member from the graph
            del self.graph[member]
            # Remove all references to this member in other members' transactions
            for from_member in self.graph:
                if member in self.graph[from_member]:
                    del self.graph[from_member][member]
    
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

    def print_members(self):
        if self.graph:
            print("Members:")
            for member in self.graph:
                print(f"- {member}")
        else:
            print("No members in the graph.")

    def search_transaction(self, phrase):
        results = []

        for from_member, to_member in self.graph.items():
            for to_member, details in to_member.items():
                for transaction in details['transactions']:
                    if phrase.lower() in transaction[1].lower() or phrase.lower() in from_member.lower():
                        results.append((from_member, to_member, transaction[0], transaction[1]))

        return results

    
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