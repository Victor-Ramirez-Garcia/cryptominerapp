import hashlib

def mining_block(block_list, root_hash):
    #Creates a for loop were in range of 0-11
    #Will add number to block_list and create a hash block
    for number in range(10000):
        # Creates a new list with block_list in it
        list_of_transactions = [block_list]
        # start of with number 1
        nonce = str(number)
        #Append number to block_list
        list_of_transactions.append(nonce)
        # join list together
        new_block_list = "".join(list_of_transactions)
        # Encodes block list
        encoded = new_block_list.encode()
        #Creates hash block
        nonce_hash = hashlib.sha256(encoded).hexdigest()
        #Create an if statement:
        #if hash does not start off with 5 zeros    
        if nonce_hash.startswith("000") == True and nonce_hash < root_hash:
            break
    return nonce, new_block_list, nonce_hash
