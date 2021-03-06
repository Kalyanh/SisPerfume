"""Subclass of FrameFixacao, which is generated by wxFormBuilder."""

import wx
import guiperfumes
import db

# Implementing FrameFixacao
class FrameFixacao( guiperfumes.FrameFixacao ):
	def __init__( self, parent ):
		guiperfumes.FrameFixacao.__init__( self, parent )
		self.atualizarGrid()

	# Handlers for FrameFixacao events.
	def fecharFrame( self, event ):
		self.Show(False)
		# TODO: Implement fecharFrame
		pass

	def adicionarFixacao( self, event ):
		nome = self.txtNome.GetValue()
		db.inserirFixacao(nome)
		wx.MessageBox(message="Fixação Inserida com Sucesso", caption="SisPerfumes", style=wx.OK, parent=self)
		self.atualizarGrid()

		# TODO: Implement adicionarFixacao
		pass

	def atualizarFixação( self, event ):
		nome_fixacao = self.gridFixações.GetCellValue(event.GetRow(), event.GetCol())
		if (nome_fixacao):
			id_fixacao = int(self.gridFixações.GetCellValue(event.GetRow(),
															  0))  # Pegue na linha editada, o conteúdo da primeira coluna
			db.atualizarFixação(id_fixacao, nome_fixacao)  # Chame a função para atualizar uma marca
			wx.MessageBox(message="Fixação Atualizada com Sucesso", caption="SysPerfumes", style=wx.OK, parent=self)
		# TODO: Implement atualizarFixação
		pass

	def atualizarGrid(self):
		if (self.gridFixações.GetNumberRows()>0):
			self.gridFixações.DeleteRows(0,self.gridFixações.GetNumberRows()) #Limpa a tabela
		fixacoes=db.listarFixacao() #Chama a função listar marcas, retornando a lista de marcas existentes
		for fixacao in fixacoes:
			self.gridFixações.AppendRows(1)#Adiciona uma linha em branco
			self.gridFixações.SetCellValue(self.gridFixações.GetNumberRows()-1,0,str(fixacao[0])) #adicione o id da marca
			self.gridFixações.SetCellValue(self.gridFixações.GetNumberRows() - 1, 1, fixacao[1]) #adiciona o nome da marca
			self.gridFixações.SetReadOnly(self.gridFixações.GetNumberRows() - 1, 0, True) #Informa que a coluna 0(ID) é somente leitura


