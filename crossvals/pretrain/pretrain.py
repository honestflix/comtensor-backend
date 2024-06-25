import bittensor as bt
from base.synapse_based_crossval import SynapseBasedCrossval
from .protocol import compute_wins, iswin, check_for_reasonable_output, compute_losses
from .mining import model_path, push, save, get_repo, load_best_model, load_model, load_gpt2_model, load_local_model, load_remote_model
class PretrainCrossVal(SynapseBasedCrossval):
    
    def __init__(self, netuid = 9, wallet_name = 'default', wallet_hotkey = 'default', network = "finney", topk = 1, subtensor = None):
        super().__init__(netuid, wallet_name, wallet_hotkey, network, topk, subtensor)
        self.dendrite = bt.dendrite( wallet = self.wallet )
    
    def forward(self):
        return True

    def run(self):
        response = self.forward()
        return response