import os
# fallback to cpu if mps is not available for specific operations
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = "1"
import torch

# data directory
DATA_DIR = 'data/'

# checkpoint directory
CHECKPOINT_DIR = 'checkpoints'

# device
device = 'cpu'
if torch.cuda.is_available(): device = 'cuda'
#if torch.backends.mps.is_available(): device = 'mps'
os.environ['DEVICE'] = device

# robot port names
ROBOT_PORTS = {
    'leader': '/dev/ttyUSB1',
    'follower': '/dev/ttyUSB0'
    # 'leader': 'COM7',
    # 'follower': 'COM6'

}

MOTOR_VENDER = {
    'leader': 'feetech',
    'follower': 'feetech'
}


# task config (you can add new tasks)
TASK_CONFIG = {
    'dataset_dir': DATA_DIR,
    'episode_len': 30000,
    'state_dim': 6,
    'action_dim': 6,
    'cam_width': 640,
    'cam_height': 480,
    # 'camera_names': ['right', 'front'],
    'camera_names': ['front', 'wist'],
    'camera_port': [0,2]
}

POS_BIAS = [131, 157, -82, 35, 123, 750]


# POLICY_CLASS = "Diffusion"
POLICY_CLASS = "ACT"

# policy config
POLICY_CONFIG = {
    'lr': 1e-5,
    'device': device,
    'num_queries': 100,
    'kl_weight': 10,
    'hidden_dim': 512,
    'dim_feedforward': 3200,
    'lr_backbone': 1e-5,
    'backbone': 'resnet18',
    'enc_layers': 4,
    'dec_layers': 7,
    'nheads': 8,
    'camera_names': ['front', 'wist'],
    # 'camera_names': ['front'],
    'policy_class': 'ACT',
    'temporal_agg': False
}



# training config
TRAIN_CONFIG = {
    'seed': 42,
    'num_epochs': 4000,
    'batch_size_val': 16,
    'batch_size_train': 16,
    # 'eval_ckpt_name': 'policy_epoch_3200_seed_42.ckpt',
    'eval_ckpt_name': 'policy_last.ckpt',
    'checkpoint_dir': CHECKPOINT_DIR
}
