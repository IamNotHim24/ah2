freq_cnt = {}

str = 'mississippi'

for s in str:
    if s in freq_cnt:
        freq_cnt[s]+=1
    else:
        freq_cnt[s] = 1

print(freq_cnt)