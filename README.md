# GBDT
The number of each express delivery stations and the independent variable factors were counted in 3325 grids of size 500m*500m. 
The independent variables were the number of residential areas, Colleges and universities, Scenic spots, Office buildings, Daily retail, Non-daily retail, Bus and subway in each grid. Specifically, the sample was divided into 10 subsets and the model was fitted with seven different subsets (70% of the data) and validated by the remaining subsets (30% of the data). 

The learning rate of the model was fixed at 0.001, in which case the prediction bias of the model was very low. 
In addition, the number of trees was set to a maximum of 10,000. 
A series of tests were carried out on the level of interaction depth of the trees in order to obtain the best results. 
The final model was based on a tree complexity of 10.

For run GBDT, your device has to download python3.6 
