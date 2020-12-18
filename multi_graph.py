import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
matplotlib.rcParams['agg.path.chunksize'] = 10000

#f = open('dqn_SoccerScoreGoal-v0_log2.json','r')
#f = open('time.json','r')
f1 = open('openaigym.episode_batch.0.455173.stats.json','r')
f2 = open('openaigym.episode_batch.0.482916.stats.json','r')
f3 = open('openaigym.episode_batch.0.536101.stats.json','r')
f5 = open('openaigym.episode_batch.0.591729.stats.json','r')
f4 = open('openaigym.episode_batch.0.580942.stats.json','r')
f6 = open('openaigym.episode_batch.0.617650.stats.json','r')
f7 = open('openaigym.episode_batch.0.596828.stats.json','r')
jsonData1 = json.load(f1)
jsonData2 = json.load(f2)
jsonData3 = json.load(f3)
jsonData4 = json.load(f4)
jsonData5 = json.load(f5)
jsonData6 = json.load(f6)
jsonData7 = json.load(f7)
fig = plt.figure(figsize=(12.8, 7.2))
"""
loss = jsonData['loss']
mean_absolute_error = jsonData['mean_absolute_error']
mean_q = jsonData['mean_q']
mean_eps = jsonData['mean_eps']
nb_episode_steps = jsonData['nb_episode_steps']
nb_episode_steps = jsonData['episode_reward']
reward_list = reward_list[:]
loss = loss[0:80000]
mean_absolute_error = mean_absolute_error[0:80000]
mean_q = mean_q[0:80000]
mean_eps = mean_eps[0:80000]
nb_episode_steps = nb_episode_steps[0:80000]
#x = range(0, 100)
"""
reward_list1 = jsonData1['episode_rewards']
reward_list2 = jsonData2['episode_rewards']
reward_list3 = jsonData3['episode_rewards']
reward_list4 = jsonData4['episode_rewards']
reward_list5 = jsonData5['episode_rewards']
reward_list5 = reward_list5[:20000]
reward_list6 = jsonData6['episode_rewards']
reward_list6 = reward_list6[:20000]
reward_list7 = jsonData7['episode_rewards']
#time_list = jsonData['time']
#N=100
#cumsum, moving_aves = [0], []
#
#for i, x in enumerate(reward_list1, 1):
#    cumsum.append(cumsum[i - 1] + x)
#    if i >= N:
#        moving_ave = (cumsum[i] - cumsum[i-N])/N
#        moving_aves.append(moving_ave)
#
#x = range(0, 20901)
#y = moving_aves
#plt.plot(x,y,label='RND1',color='green')
#
#cumsum, moving_aves = [0], []
#for i, x in enumerate(reward_list2, 1):
#    cumsum.append(cumsum[i - 1] + x)
#    if i >= N:
#        moving_ave = (cumsum[i] - cumsum[i-N])/N
#        moving_aves.append(moving_ave)
#
#x = range(0, 20901)
#y = moving_aves
#plt.plot(x,y,label='RND2',color='pink')
#
#cumsum, moving_aves = [0], []
#for i, x in enumerate(reward_list3, 1):
#    cumsum.append(cumsum[i - 1] + x)
#    if i >= N:
#        moving_ave = (cumsum[i] - cumsum[i-N])/N
#        moving_aves.append(moving_ave)
#
#x = range(0, 20901)
#y = moving_aves
#plt.plot(x,y,label='RND3',color='gold')
#
#N=100
#cumsum, moving_aves = [0], []
#
#for i, x in enumerate(reward_list4, 1):
#    cumsum.append(cumsum[i - 1] + x)
#    if i >= N:
#        moving_ave = (cumsum[i] - cumsum[i-N])/N
#        moving_aves.append(moving_ave)
#
#x = range(0, 20901)
#y = moving_aves
#plt.plot(x,y,label='RND4',color='blue')

N=100
cumsum, moving_aves = [0], []

for i, x in enumerate(reward_list5, 1):
    cumsum.append(cumsum[i - 1] + x)
    if i >= N:
        moving_ave = (cumsum[i] - cumsum[i-N])/N
        moving_aves.append(moving_ave)

x = range(0, 19901)
y = moving_aves
plt.plot(x, y, label='RND5', color='blue')

x = range(0,20000)
y = reward_list5
plt.plot(x, y, alpha=0.1, color='blue')

N=100
cumsum, moving_aves = [0], []

for i, x in enumerate(reward_list6, 1):
    cumsum.append(cumsum[i - 1] + x)
    if i >= N:
        moving_ave = (cumsum[i] - cumsum[i-N])/N
        moving_aves.append(moving_ave)

x = range(0, 19901)
y = moving_aves
plt.plot(x, y, label='PADDPG', color='red')

x = range(0,20000)
y = reward_list6
plt.plot(x, y, alpha=0.1, color='red')

#N=100
#cumsum, moving_aves = [0], []
#
#for i, x in enumerate(reward_list7, 1):
#    cumsum.append(cumsum[i - 1] + x)
#    if i >= N:
#        moving_ave = (cumsum[i] - cumsum[i-N])/N
#        moving_aves.append(moving_ave)
#
#x = range(0, 30901)
#y = moving_aves
#plt.plot(x,y,label='RND5+episode30000',color='lightseagreen')

plt.xlabel("episode", fontsize=18)
plt.ylabel("reward", fontsize=18)
plt.legend(fontsize=18)
plt.tick_params(labelsize=18)
plt.tight_layout()
plt.grid(which='major', color='gray', linestyle='-')
plt.savefig("2reward.png", dpi=300)
#plt.show()
