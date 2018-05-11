# coding:utf8
import warnings


class DefaultConfig(object):
    env = 'default'  # visdom environment
    model = 'ResNet34'  # the model, name must be the same as in models/__init__.py

    train_data_root = './data/train/'  # path the training dataset
    test_data_root = './data/test1'  # path to the testing dataset
    load_model_path = None  # path to the pre-trained model，None for not loading

    batch_size = 32  # batch size
    use_gpu = True  # user GPU or not
    num_workers = 4  # how many workers for loading data
    print_freq = 20  # print info every N batch

    debug_file = '/tmp/debug'  # if os.path.exists(debug_file): enter ipdb
    result_file = 'result.csv'

    max_epoch = 10
    lr = 0.001  # initial learning rate
    lr_decay = 0.5  # when val_loss increase, lr = lr*lr_decay
    weight_decay = 0e-5 


def parse(self, kwargs):
    """
    update config parameter from kwargs dict
    """
    for k, v in kwargs.items():
        if not hasattr(self, k):
            warnings.warn("Warning: opt has not attribut %s" % k)
        setattr(self, k, v)

    print('user config:')
    for k, v in self.__class__.__dict__.items():
        if not k.startswith('__'):
            print(k, getattr(self, k))


DefaultConfig.parse = parse
opt = DefaultConfig()
# opt.parse = parse
