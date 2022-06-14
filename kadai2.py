from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import imdb
from keras.preprocessing.text import Tokenizer
from keras import models
from keras import layers
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split

#データの呼び出し
#imdbは映画のレビュー文を集めてそれが肯定的か否定的か評価するデータ
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

#データをワンホットベクトル（文章を0か1で表したベクトル）の行列に直す
tokenizer = Tokenizer(num_words=10000)
X_train = tokenizer.sequences_to_matrix(train_data, mode='binary')
X_test = tokenizer.sequences_to_matrix(train_data, mode='binary')

#ラベルもnumpy配列に変換
y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(train_labels).astype('float32')

#トレーニングデータを更にトレーニングと検証に分割
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1, random_state=0)


#モデル作成
model = models.Sequential()
model.add(layers.Dense(32, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

#学習処理の内容
model.compile(optimizer='Adam', loss = 'binary_crossentropy', metrics=['accuracy'])

#学習の実行
history = model.fit(x=X_train, y=y_train, epochs=20, batch_size=512, verbose=1, validation_data=(X_val,y_val))


history_dict = history.history
print(history_dict.keys())


#正確度の可視化
acc = history_dict['accuracy']
val_acc = history_dict['val_accuracy']
epochs = range(1, len(acc)+1)
plt.figure(figsize=(12, 8))
plt.plot(epochs, acc, label='acc')
plt.plot(epochs, val_acc, label='val_acc')
plt.ylim((0,1))
plt.legend(loc='best')
plt.show()

#損失の可視化
acc = history_dict['loss']
val_acc = history_dict['val_loss']
epochs = range(1, len(acc)+1)
plt.figure(figsize=(12, 8))
plt.plot(epochs, acc, label='loss')
plt.plot(epochs, val_acc, label='val_loss')
plt.ylim((0,1))
plt.legend(loc='best')
plt.show()


#アーリーストップを加える
callbacks = [EarlyStopping(monitor='val_accuracy', patience=3)]

#モデル作成
model1 = models.Sequential()
model1.add(layers.Dense(32, activation='relu', input_shape=(10000,)))
model1.add(layers.Dense(16, activation='relu'))
model1.add(layers.Dense(1, activation='sigmoid'))

#学習処理の内容
model1.compile(optimizer='Adam', loss = 'binary_crossentropy', metrics=['accuracy'])

#学習の実行
history1 = model1.fit(x=X_train, y=y_train, epochs=20, batch_size=512, 
                    verbose=1, callbacks=callbacks, validation_data=(X_val,y_val))


#アーリーストップを加えたモデルの可視化
history_dict1 = history1.history
print(history_dict1.keys())


#正確度の可視化
acc = history_dict1['accuracy']
val_acc = history_dict1['val_accuracy']
epochs = range(1, len(acc)+1)
plt.figure(figsize=(12, 8))
plt.plot(epochs, acc, label='acc')
plt.plot(epochs, val_acc, label='val_acc')
plt.ylim((0,1))
plt.legend(loc='best')
plt.show()

#損失の可視化
acc = history_dict1['loss']
val_acc = history_dict1['val_loss']
epochs = range(1, len(acc)+1)
plt.figure(figsize=(12, 8))
plt.plot(epochs, acc, label='loss')
plt.plot(epochs, val_acc, label='val_loss')
plt.ylim((0,1))
plt.legend(loc='best')
plt.show()


#テストセットを使ってスコアを見る
score = model1.evaluate(X_test, y_test)
print("Test set loss: {}, Test set acc: {}".format(score[0], score[1]))


#モデルを改善してみる
model2 = models.Sequential()
model2.add(layers.Dense(1, activation='sigmoid', input_shape=(10000,)))
#model.add(layers.Dense(16, activation='relu'))
#model.add(layers.Dense(1, activation='sigmoid'))

model2.compile(optimizer='Adam', loss = 'binary_crossentropy', metrics=['accuracy'])

#学習の実行
history2 = model2.fit(x=X_train, y=y_train, epochs=20, batch_size=512, 
                    verbose=1, callbacks=callbacks, validation_data=(X_val,y_val))

#簡略化モデルの可視化
history_dict2 = history2.history
print(history_dict2.keys())


#正確度の可視化
acc = history_dict2['accuracy']
val_acc = history_dict2['val_accuracy']
epochs = range(1, len(acc)+1)
plt.figure(figsize=(12, 8))
plt.plot(epochs, acc, label='acc')
plt.plot(epochs, val_acc, label='val_acc')
plt.ylim((0,1))
plt.legend(loc='best')
plt.show()

#損失の可視化
acc = history_dict2['loss']
val_acc = history_dict2['val_loss']
epochs = range(1, len(acc)+1)
plt.figure(figsize=(12, 8))
plt.plot(epochs, acc, label='loss')
plt.plot(epochs, val_acc, label='val_loss')
plt.ylim((0,1))
plt.legend(loc='best')
plt.show()

#テストセットを使ってスコアを見る
score2 = model2.evaluate(X_test, y_test)
print("Test set loss: {}, Test set acc: {}".format(score2[0], score2[1]))