import pandas as pd 
from fastapi import FastAPI 

app = FastAPI()

# Creo dataframes a partir de csv's con datos ya transformados 
df_amazon = pd.read_csv(r'amazon.csv', sep = ',', header = 0)
df_disney = pd.read_csv(r'disney.csv', sep = ',', header = 0)
df_hulu = pd.read_csv(r'hulu.csv', sep = ',', header = 0)
df_netflix = pd.read_csv(r'netflix.csv', sep = ',', header = 0)
df_general = pd.concat([df_amazon, df_disney, df_hulu, df_netflix])



# Funciones 

@app.get('/') #ruta raíz 
def get_root():
    return 'Esta es la API de consulta para datos de plataformas de streaming hecha por Carlos Alberto Trejo'



@app.get("/get_word_count/{plataforma}/{keyword}")
def get_word_count(plataforma, keyword):
    """
    Esta funcion devuelve la cantidad de veces que aparece una keyword en el título de peliculas/series por plataforma
    """
    if plataforma == 'amazon': 
        return str(df_amazon[df_amazon['title'].str.contains(keyword)].shape[0])
    elif plataforma == 'disney':
        return str(df_disney[df_disney['title'].str.contains(keyword)].shape[0])
    elif plataforma == 'hulu': 
        return str(df_hulu[df_hulu['title'].str.contains(keyword)].shape[0])
    elif plataforma == 'netflix': 
        return str(df_netflix[df_netflix['title'].str.contains(keyword)].shape[0])



@app.get("/get_score_count/{plataforma}/{score}/{anio}")
def get_score_count(plataforma, score, anio): 
    """
    Esta funcion devuelve la cantidad de peliculas por plataforma con un puntaje mayor a XX en determinado anio
    """
    if plataforma == 'amazon': 
        df = df_amazon[(df_amazon['type'] == 'movie') & (df_amazon['score']>score) & (df_amazon['release_year'] == anio)]
        return str(df.shape[0])
    elif plataforma == 'disney': 
        df = df_disney[(df_disney['type'] == 'movie') & (df_disney['score']>score) & (df_disney['release_year'] == anio)]
        return str(df.shape[0])
    elif plataforma == 'hulu': 
        df = df_hulu[(df_hulu['type'] == 'movie') & (df_hulu['score'] > score) & (df_hulu['release_year'] == anio)]
        return str(df.shape[0])
    elif plataforma == 'netflix': 
        df = df_netflix[(df_netflix['type'] == 'movie') & (df_netflix['score'] > score) & (df_netflix['release_year'] == anio)]
        return str(df.shape[0])



@app.get("/get_second_score/{plataforma}")
def get_second_score(plataforma):
    """
    Esta funcion devuelve la segunda pelicula por orden alfabetico con mayor score para una plataforma determinada
    """ 
    if plataforma == 'amazon': 
        df = df_amazon[(df_amazon['type'] == 'movie')]
        df = df.sort_values(['score','title'], ascending = [False,True])
        titulo = str(df.iloc[1,2])
        score = str(df.iloc[1,12])
        return (titulo,score)
    elif plataforma == 'disney': 
        df = df_disney[(df_disney['type'] == 'movie')]
        df = df.sort_values(['score', 'title'], ascending = [False,True])
        titulo = str(df.iloc[1,2])
        score = str(df.iloc[1,12])
        return(titulo,score)
    elif plataforma == 'hulu': 
        df = df_hulu[(df_hulu['type'] == 'movie')]
        df = df.sort_values(['score','title'], ascending = [False,True])
        titulo = str(df.iloc[1,2])
        score = str(df.iloc[1,12])
        return (titulo,score)
    elif plataforma == 'netflix': 
        df = df_netflix[(df_netflix['type'] == 'movie')]
        df = df.sort_values(['score','title'], ascending = [False,True])
        titulo = str(df.iloc[1,2])
        score = str(df.iloc[1,12])
        return (titulo,score)



@app.get("/get_longest/{plataforma}/{duration_type}/{anio}")
def get_longest(plataforma, duration_type, anio): 
    """
    Esta funcion devuelve la pelicula o serie de mayor duracion junto con su duracion (ya sea en minutos o temporadas segun sea el caso)
    a partir de un anio y plataforma seleccionada. 
    """
    if plataforma == 'amazon': 
        df = df_amazon[(df_amazon['duration_type'] == duration_type)&(df_amazon['release_year'] == anio)]
        df = df.sort_values('duration_int' , ascending=False)
        titulo = str(df.iloc[0,2])
        duracion = str(df.iloc[0,14])
        tipo = str(df.iloc[0,15])
        return (titulo,duracion, tipo)
    elif plataforma == 'disney': 
        df = df_disney[(df_disney['duration_type'] == duration_type) & (df_disney['release_year'] ==anio)]
        df = df.sort_values('duration_int' , ascending=False)
        titulo = str(df.iloc[0,2])
        duracion = str(df.iloc[0,14])
        tipo = str(df.iloc[0,15])
        return (titulo,duracion, tipo)
    elif plataforma == 'hulu': 
        df = df_hulu[(df_hulu['duration_type'] == duration_type) & (df_hulu['release_year']== anio)]
        df = df.sort_values('duration_int' , ascending=False)
        titulo = str(df.iloc[0,2])
        duracion = str(df.iloc[0,14])
        tipo = str(df.iloc[0,15])
        return (titulo,duracion, tipo)
    elif plataforma == 'netflix': 
        df = df_netflix[(df_netflix['duration_type'] == duration_type)&(df_netflix['release_year'] == anio)]
        df = df.sort_values('duration_int' , ascending=False)
        titulo = str(df.iloc[0,2])
        duracion = str(df.iloc[0,14])
        tipo = str(df.iloc[0,15])
        return (titulo,duracion, tipo)



@app.get("/get_rating_count/{rating}")
def get_rating_count(rating):
    """
    Esta funcion devuelve la cantidad de series y peliculas por rating seleccionado
    """
    df = df_general[(df_general['rating']==rating)]
    return str(df.shape[0])



# Deta Details
"""
{
        "name": "PI-CarlosTrejo",
        "id": "d02b514a-dcab-468e-b327-8678fa251de6",
        "project": "default",
        "runtime": "python3.9",
        "endpoint": "https://68bcz7.deta.dev",
        "region": "us-east-1",
        "dependencies": [
                "fastapi",
                "pandas"
        ],
        "visor": "disabled",
        "http_auth": "disabled"
}
"""