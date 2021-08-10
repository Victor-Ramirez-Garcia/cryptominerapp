import random
import hashlib

# Creates a miner transaction reward
def block_reward():
    #creates random ammount of VRC
    number_of_vrc = str(random.randint(10, 100))
    #create a random transaction
    reward_transaction = 'MINER GETS ' + number_of_vrc + ' VRC, '
    #Return random transaction
    return reward_transaction

# Creates a fake transaction
def create_fake_transaction():
    #Load list of framework names
    with open(f'txt/first-names.txt') as f:
        first_names = f.read().split('\n')
    with open(f'txt/last-names.txt') as f:
        last_names = f.read().split('\n')
    #creates random name
    name = str((first_names[random.randint(0, 199)] + ' ' +
            last_names[random.randint(0, 299)]))
    #creates second random name
    name2 = str((first_names[random.randint(0, 199)] + ' ' +
            last_names[random.randint(0, 299)]))
    
    #creates random ammount of VRC
    number_of_vrc = str(random.randint(10, 100))
    #create a random transaction
    random_transaction = name + ' PAYS ' + name2 + ' ' + number_of_vrc + ' VRC, '
    #Return random transaction
    return random_transaction

# This creates a list of a random transaction
def create_block_list():
    #creates a transaction list
    list_of_transactions = ['TRANSACTIONS: ']
    list_of_transactions.append(block_reward())

    #Creates a list of 1-5 transactions    
    for transactions in range(random.randint(1, 5)):
        transactions = create_fake_transaction()
        list_of_transactions.append(transactions)

    nonce = 'NONCE: '

    list_of_transactions.append(nonce)

    #Returns list
    return list_of_transactions

def create_block():
    #Creates list of random transactions
    list_of_transactions = create_block_list()

    block_list = "".join(list_of_transactions)

    # Create the block
    encoded = block_list.encode()
    root_hash = hashlib.sha256(encoded).hexdigest()
    #Return block and transactions list
    return root_hash, list_of_transactions, block_list
