from rnn import CharGen
from rnn.train_model import train

train_new_model = True

if train_new_model:
    textgen = CharGen(name="Shakespeare")
    train(text_filepath='datasets/shakespeare.txt',
          textgen=textgen,
          num_epochs=25,
          bidirectional=True,
          rnn_size=1,
          rnn_layers=1,
          batch_size=1024,
          embedding_dims=75,
          train_new_model=train_new_model)

    print(textgen.model.summary())
else:
    textgen = CharGen(name='Test',
                      weights_filepath='/weights/Test_weights.hdf5',
                      vocab_filepath='/vocabulary/Test_vocab.json',
                      config_filepath='config/Test_config.json')

    train('harry.txt', textgen, train_new_model=train_new_model, num_epochs=1)
