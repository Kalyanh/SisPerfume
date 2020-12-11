'''
Essa função lista todos os perfumes, trazendo as informações completas e relacionadas com as outras tabelas,
de forma que a lista final tem os segintes campos: id do Perfume, nome do perfume, quantidade do perfume,
nome do volume, nome da marca e nome da fixação
'''

def listarPerfumes():
    sql='''
        select Perfumes.id, Perfumes.nome,Perfumes.quantidade,Volumes.nome,Marcas.nome,Fixacoes.nome from 
        Perfumes inner join Volumes on Perfumes.id_volume=Volumes.id 
        inner join Marcas on Perfumes.id_marca=Marcas.id inner join Fixacoes on Perfumes.id_fixacao=Fixacoes.id
    '''
    cursor=banco.cursor()
    cursor.execute(sql)
    perfumes=cursor.fetchall()
    return perfumes
'''
Essa função é a mais complexa do nosso programa. Ela recebe como parâmetro uma lista de perfumes,
que virá do FramePerfumes. Essa lista deve conter 6 elementos:
listaPerfumes[0]--> id do perfume. Se for vazio, significa que iremos inserir
listaPerfumes[1]--> Nome do Perfume
listaPerfumes[2]--> Quantidade do Perfume
listaPerfumes[3]--> Nome do Volume
listaPerfumes[4]--> Nome da Marca
listaPerfumes[5]-->Nome da Fixação

'''
def salvarPerfumes(listaPerfumes):
    cursor=banco.cursor()
    for perfume in listaPerfumes: #For percorre a lista de perfumes, inserindo ou atualizando, um por um
        sql=''
        #Se perfume[0] for vazio, ou seja, o id, significa que temos que incliuir o registro
        if perfume[0]=='':
            #As funções localizar buscam o id do volume, marca e fixacao, de forma a garantir a integridade do banco de dados
            sql="insert into perfumes (nome,quantidade,id_volume,id_marca,id_fixacao) " \
                "values('{0}',{1},{2},{3},{4})".format(perfume[1],perfume[2],localizarVolumePorNome(perfume[3])[0],
                                                       localizarMarcaPorNome(perfume[4])[0],
                                                       localizarFixacaoPorNome(perfume[5])[0])
        #Caso contrário, devemos atualizar
        else:
            sql="update perfumes set nome='{1}',quantidade={2},id_volume={3}," \
                "id_marca={4},id_fixacao={5} where id={0}".format(perfume[0],perfume[1],perfume[2],
                                                                  localizarVolumePorNome(perfume[3])[0],
                                                                  localizarMarcaPorNome(perfume[4])[0],
                                                                  localizarFixacaoPorNome(perfume[5])[0])
        try:
            cursor.execute(sql) #Executo a instrução, se der um erro, retorna a mensagem de erro
        except sqlite3.Error as e:
            return False,"Erro ao salvar perfume: "+e.args[0]
    banco.commit() #Se tudo correr bem, confirma as alterações no banco
    cursor.close() #Fecha a conexão
    return True,None #Retorna dizendo que deu certo salvar a lista de perfumes