# -*- coding: utf-8 -*-

## Validators for the input form
INPUT_SIMULATION.LABEL.requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'INPUT_SIMULATION.LABEL')]
INPUT_SIMULATION.SIM_FILE.requires = [IS_UPLOAD_FILENAME(extension='pdf'), IS_LENGTH(1048576, 1024)]                                  
#Filmes.capa.requires = IS_EMPTY_OR(IS_IMAGE())

## Validators for simulations
SIMULATION.LABEL.requires = IS_IN_DB(db, 'INPUT_SIMULATION.LABEL', _and=IS_NOT_IN_DB(db, 'SIMULATION.LABEL'))                                 
#ItemsEstoque.filme.requires = IS_IN_DB(db, 'filmes.id', '%(titulo)s', _and=IS_NOT_IN_DB(db, 'items_estoque.filme'))

## Validators for timeframe
TIMEFRAME.LABEL.requires = IS_IN_DB(db, 'SIMULATION.LABEL', _and=IS_NOT_IN_DB(db, 'TIMEFRAME.LABEL'))      
TIMEFRAME.TIMESTEP.requires = IS_NOT_EMPTY()
TIMEFRAME.PDB.requires = IS_EMPTY_OR(IS_UPLOAD_FILENAME(extension='pdb'))

#Locacao.filmes.requires = IS_IN_DB(db, 'filmes.id', '%(titulo)s')
#Locacao.cliente.requires = IS_IN_DB(db, 'auth_user.id', '%(first_name)s %(last_name)s')
#Locacao.data_locacao.requires = IS_DATETIME(format='%d/%m/%Y')
#Locacao.data_devolucao.requires = IS_DATETIME(format='%d/%m/%Y')
