import hashlib
import json
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request


DIFFICULTY = 6


@app.route('/mine', methods=['POST'])
def mine():
    # Handle non-json response
    try:
        values = request.get_json()
    except ValueError:
        print("Error:  Non-json response")
        print("Response returned:")
        print(request)
        return "Error"
    required = ['proof', 'id']
    if not all(k in values for k in required):
      response = {'message': "Missing Values"}
      return jsonify(response), 400
    
    submitted_proof = values['proof']
    
    # Determine if proof is valid
    last_block = blockchain.last_block
    last_block_string = json.dumps(last_block, sort_keys=True)
    if blockchain.valid_proof(last_block_string, submitted_proof):
    
      # Forge the new Block by adding it to the chain with the proof
      previous_hash = blockchain.hash(blockchain.last_block)
      block = blockchain.new_block(submitted_proof, previous_hash)
      response = {
          # TODO: Send a JSON response with the new block
          'message': "New Block Forged",
          'block': block
      }

      return jsonify(response), 200
    
    else:
      response = {
    'message': "Proof Invalid or already submitted"
      }
      
      return jsonify(response), 200
      


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        # TODO: Return the chain and its current length
        'length': len(blockchain.chain),
        'chain': blockchain.chain
    }
    return jsonify(response), 200
  
  
@app.route('/last_block', methods=['GET'])
def return_last_block():
    response = {
        'last_block': blockchain.last_block
    }
    return jsonify(response), 200  


# Run the program on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)