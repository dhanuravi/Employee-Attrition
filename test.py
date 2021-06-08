import pickle
import numpy as np
#data = [43,	2,	1034	,2,	16	,3,	2,	1,	4	,0,	80	,3,	4	,3,	4,	1,	16064,	7744,	5,	1	,22,	4	,3,	80,	1	,22	,3	,3,	17	,13	,1,	9]
#data = [39	,0	,592,	1	,2	,3	,1	,1	,1	,0	,54,	2	,1,	2	,1	,2	,3646,	17181	,2	,1	,23	,4,	2	,80,	0	,11,	2	,4	,1,	0	,0	,0]
#data = [39,	0,	592	,1,	2	,3,	1	,1,	1	,0,	54,	2	,1,	2	,1,	2,	3646,	17181,	2,	1,	23,	4	,2,	80,	0,	11	,2,	4	,1,	0,	0	,0]

def gb(data):
    model = pickle.load(open('gb.pkl', 'rb'))
    prediction=model.predict([data])#86
    return(prediction)

def ada(data):
    model = pickle.load(open('ada.pkl', 'rb'))#87
    prediction=model.predict([data])
    return(prediction)

def xg(data):
    model = pickle.load(open('xg.pkl', 'rb'))#85
    prediction=model.predict(np.array([data]))
    return(prediction)