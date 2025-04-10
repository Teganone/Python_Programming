import re

def predict_gene(file_path):
    with open(file_path, 'r') as file:
        sequences = file.readlines()
    
    potential_genes = []
    for seq in sequences:
        seq = seq.strip()
        # 判断基因长度是否为3的倍数
        if len(seq) % 3 != 0:
            continue
        # 判断是否以ATG开始
        if not seq.startswith('ATG'):
            continue
        # 判断是否以TAG、TAA、TGA结束
        if not (seq.endswith('TAG') or seq.endswith('TAA') or seq.endswith('TGA')):
            continue
        # 判断中间部分是否包含TAG、TAA、TGA
        if re.search(r'TAG|TAA|TGA', seq[3:-3]):
            continue
        potential_genes.append(seq)
    
    return potential_genes

# 测试
file_path = 'gene.txt'
potential_genes = predict_gene(file_path)
# print('潜在的基因序列：')
for i,gene in enumerate(potential_genes):
    print(f"{i+1}:{gene}")