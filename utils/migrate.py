import pandas as pd
from DJcv_backend.settings import DIR


def ImportDataBetter( folder ,filename:str):
    df = pd.read_csv(DIR+f"{folder}/csv/{filename}.csv")
    d=[]
    header = df.columns
    print(header)
    a = df.to_dict('records')
    len(a)
    for i in a:
        jdata={}
        for g in header:
            if pd.isna(i.get(g)):
                jdata.__setitem__(g,None)
            else:
                jdata.__setitem__(g,i.get(g))
        d.append(jdata)
    print(d)
    return d