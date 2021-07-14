from drl_framework.dumper import Dumper
from drl_framework.env import Env 
from drl_framework.agent import Agent
from DQN.DQNAgent import DqnAgent
from drl_framework.experiment import Experiment
from utils.cfg import CfgMaker
from utils.logger import Logger
from utils.utils import *


if __name__ == "__main__":
    cfg = CfgMaker()
    
    # Get all config
    cfg_logger = cfg.make_cfg_logger()
    cfg_dumper = cfg.make_cfg_dumper()
    cfg_experiment = cfg.make_cfg_experiment()
    cfg_env = cfg.make_cfg_env()
    cfg_agent = cfg.make_cfg_agent()
    #cfg.show_configs()
    
    
    #Instantiate objects
    logger = Logger(cfg_logger)
    dumper = Dumper(cfg_dumper, logger)
    env = Env(cfg_env,logger)
    info_env = env.get_agent_info()
    agent = Agent.select_agent(cfg_agent['agent_class'], **{"cfg" :  cfg_agent, "info_env" : info_env, "logger": logger})
    experiment = Experiment(cfg_experiment,env,agent,dumper,logger)
    cfg.dump_cfg()

        
    try:

        experiment.train()
        experiment.test()

    except KeyboardInterrupt:
        env.handle_kb_int()
        dumper.handle_kb_int()
        agent.handle_kb_int()
        logger.handle_kb_int()

