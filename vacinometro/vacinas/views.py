from django.shortcuts import render
from .utils import get_dados_vacinas
import pandas as pd
import plotly.express as px

def dashboard(request):
    dados = get_dados_vacinas()
    df = pd.DataFrame(dados)

    print(df.columns)  # Veja no terminal quais colunas vieram

    if 'sigla_uf_paciente' in df.columns:
        fig = px.histogram(df, x='sigla_uf_paciente', title='Distribuição de Doses por Estado (Paciente)')
        grafico = fig.to_html(full_html=False)
    else:
        grafico = "<p>Coluna 'sigla_uf_paciente' não encontrada nos dados.</p>"

    return render(request, 'vacinas/dashboard.html', {'grafico': grafico})
