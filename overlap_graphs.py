# import re
#
# fasta_map = {
# }
#
# adj_map = {
# }
#
# def get_fasta_headers(file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()
#         headers = re.findall(r'>.*', content)
#         return headers
#
# fo = open("overlap_graphs.txt")
# fasta_content = fo.read()
# headers = re.findall(r'^>(.*)$', fasta_content, re.MULTILINE)
#
# print(headers)
# print(get_fasta_headers("overlap_graphs.txt"))

# import re
#
# # Open the FASTA file
# with open('overlap_graphs.txt', 'r') as file:
#     # Read the entire file into a string
#     fasta_content = file.read()
#
# # Use regular expression to find all sequences (including headers)
# sequences = re.findall(r'>(.*?)\n([ATCG\n]+)', fasta_content, re.DOTALL)
#
# # Create a dictionary mapping headers to sequences
# fasta_dict = {header: seq.replace('\n', '') for header, seq in sequences}
#
# # Print the dictionary
# for key, value in fasta_dict.items():
#     print(f'{key} : {value}')

import re

# Open the FASTA file
with open('overlap_graphs.txt', 'r') as file:
    # Read the entire file into a string
    fasta_content = file.read()

# Use regular expression to find all sequences (header and DNA sequence)
sequences = re.findall(r'>([^\n]*)\n([^>]*)', fasta_content, re.DOTALL)

# Create a dictionary mapping headers to sequences
fasta_dict = {header: seq.strip() for header, seq in sequences}

# Print the dictionary
for key, value in fasta_dict.items():
    print(f'{key} : {value}')

def build_adjacency_graph(string_dict):
    graph = {}
    for key, string in string_dict.items():
        graph[key] = []
        suffix = string[-3:]
        for other_key, other_string in string_dict.items():
            if key != other_key and suffix in other_string:
                graph[key].append(other_key)
    for string, connections in graph.items():
        print(f"{string} -> {connections}")
    return graph

build_adjacency_graph(fasta_dict)



