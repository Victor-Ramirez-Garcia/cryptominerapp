from flask import render_template
from flask.views import MethodView
from importFiles.block_creator import create_block
from importFiles.mining import mining_block

class Miner(MethodView):
    def get(self):
        root_hash, list_of_transactions, block_list = create_block()
        nonce, new_block_list, nonce_hash = mining_block(block_list, root_hash)
        return render_template('miner.html', 
                                list_of_transactions=list_of_transactions, 
                                root_hash=root_hash, 
                                block_list=block_list,
                                nonce=nonce,
                                new_block_list=new_block_list,
                                nonce_hash=nonce_hash)
