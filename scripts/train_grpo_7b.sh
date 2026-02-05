set -x

# System setup (adjust paths according to your environment)
# if [ ! -d "/path/to/your/mount" ]; then
#     mkdir -p /path/to/your/mount
#     cd /path/to/your/mount
#     ln -s /path/to/your/dataset usr
#     ln -s /path/to/your/dataset nas
#     cd /path/to/your/mount/usr
# fi

nvidia-smi topo -m  # 查看 GPU 间连接方式（NVLink/PCIe）

export NCCL_SOCKET_IFNAME=eno1,en,eth,em,bond ;
export NCCL_TIMEOUT=1200 ;
apt update -y ;

pip3 install ray[default]
export RAY_RPC_TIMEOUT_MS=600000

export PYTHONUNBUFFERED=1

# Configuration variables (set these according to your setup)
ori_checkpoint_path="/path/to/your/model"  # Path to your fine-tuned model from SFT stage
dataset="your_dataset_name"  # Dataset name for UARPO training
run_name="uarpo_experiment_$(date +%Y%m%d_%H%M%S)"  # Experiment name
GPU_NUM=8  # Number of GPUs per node
WORLD_SIZE=1  # Number of nodes

# Change to your EasyR1 directory
cd .

bash run/run_ray.sh

MODEL_PATH=${ori_checkpoint_path}  # replace it with your local file path

python3 -m verl.trainer.main \
    config=examples/config.yaml\
    data.train_files=data/huggingface/${dataset}@train \
    data.val_files=data/huggingface/${dataset}@test \
    data.prompt_key="question" \
    data.answer_key="response" \
    data.image_key="images" \
    worker.actor.model.model_path=${MODEL_PATH} \
    trainer.logger="['console', 'tensorboard']"\
    worker.actor.micro_batch_size_per_device_for_update=1 \
    worker.actor.micro_batch_size_per_device_for_experience=2 \
    worker.critic.micro_batch_size_per_device_for_update=2 \
    worker.critic.micro_batch_size_per_device_for_experience=4 \
    worker.actor.fsdp.torch_dtype=bf16 \
    worker.actor.optim.strategy=adamw_bf16 \
    worker.rollout.tensor_parallel_size=$GPU_NUM \
    trainer.experiment_name=$run_name \
    trainer.n_gpus_per_node=$GPU_NUM \
    trainer.save_freq=8000 \
    trainer.val_freq=1000 \
    worker.actor.global_batch_size=16 \
    data.rollout_batch_size=16 \
    trainer.nnodes=$WORLD_SIZE

