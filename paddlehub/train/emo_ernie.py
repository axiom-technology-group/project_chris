import paddlehub as hub

# Load ernie pretrained model
module = hub.Module(name="ernie")
inputs, outputs, program = module.context(trainable=True, max_seq_len=128)
module = hub.Module(name="bert_chinese_L-12_H-768_A-12")
dataset = hub.dataset.ChnSentiCorp()
reader = hub.reader.ClassifyReader(
    dataset=dataset,
    vocab_path=module.get_vocab_path(),
    max_seq_len=128)
#
strategy = hub.AdamWeightDecayStrategy(
    learning_rate=5e-5,
    weight_decay=0.01,
    warmup_proportion=0.0,
    lr_scheduler="linear_decay",
)

config = hub.RunConfig(use_cuda=False, num_epoch=3, batch_size=32, strategy=strategy)
pooled_output = outputs["pooled_output"]

# feed_list的Tensor顺序不可以调整
feed_list = [
    inputs["input_ids"].name,
    inputs["position_ids"].name,
    inputs["segment_ids"].name,
    inputs["input_mask"].name,
]

cls_task = hub.TextClassifierTask(
    data_reader=reader,
    feature=pooled_output,
    feed_list=feed_list,
    num_classes=dataset.num_labels,
    config=config)

cls_task.finetune_and_eval()
CKPT_DIR=".ckpt_chnsentiment/best_model"
