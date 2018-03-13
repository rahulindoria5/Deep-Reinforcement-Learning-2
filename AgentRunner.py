import DuelingDDQNAgentPER

setup_dict = {}
setup_dict['observing_frames'] = 30000
setup_dict['replay_memory_size'] = 30000
setup_dict['learning_rate'] = 2.5*1e-4
setup_dict['start_eps'] = 0.6
setup_dict['exploring_frames'] = 500000

agent = DuelingDDQNAgentPER.Dueling_DDQN_PER_Agent(setup_dict)
rewards = agent.train()
from matplotlib import pyplot as plt
plt.plot(range(len(rewards)), rewards)
plt.savefig(PLOT_NAME)