import pandas as pd
import matplotlib.pyplot as plt


microdados_enem = pd.read_csv('/run/media/jhonata/_home/MICRODADOSENEM.csv', sep=';', encoding='ISO-8859-1') 
# Leitura dos dados armazenados no arquivo .csv
print(microdados_enem.head())
# Amostragem bruta dos dados
print(microdados_enem)
# Também pode-se visualizar os dados chammando apenas por sua variável
print(microdados_enem.columns.values)
# Com o método acima, é possível visualizar todas as colunas
# do arquivo .csv, assim sendo possível selecioná-las e
# visualizar apenas as que sejam interessante para uma certa
# atividade.

colunas_selecionadas_enem = ['NO_MUNICIPIO_RESIDENCIA', 'CO_UF_RESIDENCIA', 'SG_UF_RESIDENCIA',
       'NU_IDADE', 'TP_SEXO', 'TP_ESTADO_CIVIL', 'TP_COR_RACA',
       'TP_NACIONALIDADE', 'CO_MUNICIPIO_NASCIMENTO',
       'NO_MUNICIPIO_NASCIMENTO', 'CO_UF_NASCIMENTO', 'SG_UF_NASCIMENTO',
       'TP_ST_CONCLUSAO', 'TP_ANO_CONCLUIU', 'TP_ESCOLA', 'TP_ENSINO',
       'IN_TREINEIRO', 'CO_ESCOLA', 'CO_MUNICIPIO_ESC',
       'NO_MUNICIPIO_ESC', 'CO_UF_ESC', 'SG_UF_ESC',
       'TP_DEPENDENCIA_ADM_ESC', 'TP_LOCALIZACAO_ESC', 'TP_SIT_FUNC_ESC',
       'IN_BAIXA_VISAO', 'IN_CEGUEIRA', 'IN_SURDEZ',
       'IN_DEFICIENCIA_AUDITIVA', 'IN_SURDO_CEGUEIRA',
       'IN_DEFICIENCIA_FISICA', 'IN_DEFICIENCIA_MENTAL',
       'IN_DEFICIT_ATENCAO', 'IN_DISLEXIA', 'IN_DISCALCULIA',
       'IN_AUTISMO', 'IN_VISAO_MONOCULAR', 'IN_OUTRA_DEF', 'IN_GESTANTE',
       'IN_LACTANTE', 'IN_IDOSO', 'IN_ESTUDA_CLASSE_HOSPITALAR',
       'IN_SEM_RECURSO', 'IN_BRAILLE', 'IN_AMPLIADA_24', 'IN_AMPLIADA_18',
       'IN_LEDOR', 'IN_ACESSO', 'IN_TRANSCRICAO', 'IN_LIBRAS',
       'IN_LEITURA_LABIAL', 'IN_MESA_CADEIRA_RODAS',
       'IN_MESA_CADEIRA_SEPARADA', 'IN_APOIO_PERNA', 'IN_GUIA_INTERPRETE',
       'IN_COMPUTADOR', 'IN_CADEIRA_ESPECIAL', 'IN_CADEIRA_CANHOTO',
       'IN_CADEIRA_ACOLCHOADA', 'IN_PROVA_DEITADO', 'IN_MOBILIARIO_OBESO',
       'IN_LAMINA_OVERLAY', 'IN_PROTETOR_AURICULAR', 'IN_MEDIDOR_GLICOSE',
       'IN_MAQUINA_BRAILE', 'IN_SOROBAN', 'IN_MARCA_PASSO', 'IN_SONDA',
       'IN_MEDICAMENTOS', 'IN_SALA_INDIVIDUAL', 'IN_SALA_ESPECIAL',
       'IN_SALA_ACOMPANHANTE', 'IN_MOBILIARIO_ESPECIFICO',
       'IN_MATERIAL_ESPECIFICO', 'IN_NOME_SOCIAL', 'CO_MUNICIPIO_PROVA',
       'NO_MUNICIPIO_PROVA', 'CO_UF_PROVA', 'SG_UF_PROVA',
       'TP_PRESENCA_CN', 'TP_PRESENCA_CH', 'TP_PRESENCA_LC',
       'TP_PRESENCA_MT', 'CO_PROVA_CN', 'CO_PROVA_CH', 'CO_PROVA_LC',
       'CO_PROVA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC',
       'NU_NOTA_MT', 'TX_RESPOSTAS_CN', 'TX_RESPOSTAS_CH',
       'TX_RESPOSTAS_LC', 'TX_RESPOSTAS_MT', 'TP_LINGUA',
       'TX_GABARITO_CN', 'TX_GABARITO_CH', 'TX_GABARITO_LC',
       'TX_GABARITO_MT', 'TP_STATUS_REDACAO', 'NU_NOTA_COMP1',
       'NU_NOTA_COMP2', 'NU_NOTA_COMP3', 'NU_NOTA_COMP4', 'NU_NOTA_COMP5',
       'NU_NOTA_REDACAO', 'Q001', 'Q002', 'Q003', 'Q004', 'Q005', 'Q006',
       'Q007', 'Q008', 'Q009', 'Q010', 'Q011', 'Q012', 'Q013', 'Q014',
       'Q015', 'Q016', 'Q017', 'Q018', 'Q019', 'Q020', 'Q021', 'Q022',
       'Q023', 'Q024', 'Q025', 'Q026', 'Q027']
print(colunas_selecionadas_enem)
microdados_enem_selecionados = microdados_enem.filter(items=colunas_selecionadas_enem)
# Atribuindo as colunas limitadas ao dataframe "microdados_enem_selecionandos"
print(microdados_enem_selecionados)

coluna_municipio_residência = microdados_enem_selecionados['NO_MUNICIPIO_RESIDENCIA'] 
# Criando uma variável que armazenará apenas os nomes da 
# cidade que os candidatos moram. Isso é útil para saber os 
# municipios que tiveram candidatos realizando o ENEM e 
# tambpem para saber a distribuição da candidatos dentre os
# municípios. 
print(coluna_municipio_residência) 
# Mostrando os municipior distribuição
print(coluna_municipio_residência.value_counts().sort_index())
# Mostrando a distribuição de candidatos dentre os municipios 

coluna_nu_idade = microdados_enem_selecionados['NU_IDADE']
# Criando uma variável que armazena a idade dos candidatos
print(coluna_nu_idade.value_counts().sort_index())
# Visualizando a coluna em ordem crescente.
coluna_nu_idade.hist(bins=30)
# Gerando gráfico com a predominância de idade dos candidatos

coluna_sg_uf_residen = microdados_enem_selecionados['SG_UF_RESIDENCIA']
# Gerando uma variável que armazena o estado em que cada candidato reside
print(coluna_sg_uf_residen.value_counts())
# Visualizando a distribuição de candidatos por estado
coluna_sg_uf_residen.hist(bins=50)
# Gerando gráfico com a predominância de candidatos por estado

coluna_in_gestante = microdados_enem_selecionados['IN_GESTANTE']
# Gerando uma variável que armazena o a quantidade de candidatas 
# declaradas gestantes 
dist_in_gestante = coluna_in_gestante.value_counts()
# Atribuindo as pessoas declaradas gestantes à uma variável
print(dist_in_gestante)
# Exibindo essa informação
percent_in_gestante = [100*x/dist_in_gestante.sum() for x in dist_in_gestante]
# Calculando o percentual de pessoas gestantes.
print(percent_in_gestante)

coluna_tp_sexo = microdados_enem_selecionados['TP_SEXO']
# Criando variável que separa as pessoas por seu sexo
dist_tp_sexo = coluna_tp_sexo.value_counts()
print(dist_tp_sexo)
percent_tp_sexo = [100*x/dist_tp_sexo.sum() for x in dist_tp_sexo]
# Calculando a porcentagem entre feminino e masculino
print(percent_tp_sexo)
sexoF = dist_tp_sexo[0]
nu_gest = dist_in_gestante[1]
percent_gestantes = 100*nu_gest/sexoF
percentNAOgestantes = 100 -percent_gestantes
# Calculando a porcentagem de pessoas do sexo feminino declaradas
# gestantes
print(percent_gestantes)
print(percentNAOgestantes)