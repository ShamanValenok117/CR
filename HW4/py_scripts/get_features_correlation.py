def get_features_correlation(df, target_column='quality', target_value = 9, name='Test',save=False):
    import pandas as pd
    import matplotlib.pyplot as plt
    
    if type(target_value) != list: 
        target_value = list(target_value)    
    
    df['test'] = df[target_column].apply(lambda x: 1 if x in target_value else 0)
    corr = df.corr()
    fig = plt.figure(figsize=(15,7))
    a = corr.test[:-2]
    ax = fig.add_subplot(111)
    
    plt.bar(a.index,a,color='#ff8700')
    plt.plot(range(11),[0.015]*11,'b--')
    plt.plot(range(11),[-0.015]*11,'b--')
    plt.title(name ,pad=3, fontdict={'fontsize':18} )
    plt.text(.05,.95,'features between blue lines are not significant',fontsize=11, c='b',transform=ax.transAxes)
    fig.tight_layout()
    if save: fig.savefig(f'{name}.png');