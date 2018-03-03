from neo import Neo

neo = Neo(command_prefix='!')

# Get token safely
token_file = open("neo_token.txt", 'r')
token = token_file.read()
token_file.close()

neo.run(token)