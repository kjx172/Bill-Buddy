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

    
    
    def simplify_debts(self):
        balance = {}

        # Calculate net balance for each member
        for debtor, creditors in self.graph.items():
            for creditor, details in creditors.items():
                amount = details['amount']
                if debtor not in balance:
                    balance[debtor] = 0
                if creditor not in balance:
                    balance[creditor] = 0
                balance[debtor] -= amount
                balance[creditor] += amount

        # Create lists of debtors and creditors
        debtors = [member for member in balance if balance[member] < 0]
        creditors = [member for member in balance if balance[member] > 0]

        # Simplify debts
        simplified_graph = {}
        i, j = 0, 0
        while i < len(debtors) and j < len(creditors):
            debtor = debtors[i]
            creditor = creditors[j]
            debit = -balance[debtor]
            credit = balance[creditor]

            min_amount = min(debit, credit)

            if debtor not in simplified_graph:
                simplified_graph[debtor] = {}
            simplified_graph[debtor][creditor] = {
                'amount': min_amount,
            }

            balance[debtor] += min_amount
            balance[creditor] -= min_amount

            if balance[debtor] == 0:
                i += 1
            if balance[creditor] == 0:
                j += 1

        return simplified_graph


