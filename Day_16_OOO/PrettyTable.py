from prettytable import PrettyTable

table = PrettyTable()
table.align = 'r' #this won't work because its before adding columns.
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = 'l'
print(table)


# added comment on Mar 19th 2023 :)
