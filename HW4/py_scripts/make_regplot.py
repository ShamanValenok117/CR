def make_regplot(df,y,x='quality'):
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    if type(y) is str:
        y = [y]
    elif type(y) is not list:
        print('y is only acceptable list or str')
        return
    for i in y:
        plt.figure(figsize=(7,3))
        sns.regplot(x='quality',y= i, 
                    data=df,color='green',x_estimator=np.mean, x_ci=100,n_boot=500);
        plt.xlim(2.5,9.5)
        plt.title(f'{i} vs quality')
        plt.show()
    return