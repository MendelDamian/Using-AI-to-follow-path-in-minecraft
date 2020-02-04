# Using AI to follow path in minecraft

#### Data
I have pre-trained model, you can find it and download it on my  [Kaggle profile](https://www.kaggle.com/myndel "Kaggle profile") and [notebook](https://www.kaggle.com/myndel/minecraft-v2-0 "notebook").

#### Description
Simply AI to follow path made by redstone or contrast block to its background. It looks at the left up corner of your monitor, then process the data on which AI looks after straight lines to follow path.

#### How to use
First of all you need to put minecraft window on left up corner and resize it to 800px width and 600px height. Then collet some data to fit AI. Create contrast path in your minecraft's world then run `collect_data.py`. More data the better your AI will be. Then balance the data by running `balance_data.py` and you can train your model - to do this use `train_model.py` (it can take some time). Finally you can use your trained AI, run `main.py`, open minecraft and activate AI by pressing `Y key` - check it out on your path.
