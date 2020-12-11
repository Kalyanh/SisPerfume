# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class FrameMarca
###########################################################################

class FrameMarca ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Marcas", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Descrição:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.txtNome = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.txtNome, 1, wx.ALL, 5 )

		self.btnAdicionar = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnAdicionar, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.gridMarcas = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridMarcas.CreateGrid( 0, 2 )
		self.gridMarcas.EnableEditing( True )
		self.gridMarcas.EnableGridLines( True )
		self.gridMarcas.EnableDragGridSize( False )
		self.gridMarcas.SetMargins( 0, 0 )

		# Columns
		self.gridMarcas.SetColSize( 0, 30 )
		self.gridMarcas.SetColSize( 1, 300 )
		self.gridMarcas.EnableDragColMove( False )
		self.gridMarcas.EnableDragColSize( True )
		self.gridMarcas.SetColLabelSize( 30 )
		self.gridMarcas.SetColLabelValue( 0, u"ID" )
		self.gridMarcas.SetColLabelValue( 1, u"Nome" )
		self.gridMarcas.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridMarcas.EnableDragRowSize( True )
		self.gridMarcas.SetRowLabelSize( 80 )
		self.gridMarcas.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridMarcas.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.gridMarcas.SetToolTip( u"Pressione Enter para atualizar uma Marca" )

		bSizer3.Add( self.gridMarcas, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.fecharFrame )
		self.btnAdicionar.Bind( wx.EVT_BUTTON, self.adicionarMarca )
		self.gridMarcas.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.atualizarMarca )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def fecharFrame( self, event ):
		event.Skip()

	def adicionarMarca( self, event ):
		event.Skip()

	def atualizarMarca( self, event ):
		event.Skip()


###########################################################################
## Class FrameEssencia
###########################################################################

class FrameEssencia ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Essências", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Descrição:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer15.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.txtNome = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.txtNome, 1, wx.ALL, 5 )

		self.btnAdicionar = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.btnAdicionar, 0, wx.ALL, 5 )


		bSizer14.Add( bSizer15, 0, wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.gridEssências = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridEssências.CreateGrid( 0, 2 )
		self.gridEssências.EnableEditing( True )
		self.gridEssências.EnableGridLines( True )
		self.gridEssências.EnableDragGridSize( False )
		self.gridEssências.SetMargins( 0, 0 )

		# Columns
		self.gridEssências.SetColSize( 0, 30 )
		self.gridEssências.SetColSize( 1, 300 )
		self.gridEssências.EnableDragColMove( False )
		self.gridEssências.EnableDragColSize( True )
		self.gridEssências.SetColLabelSize( 30 )
		self.gridEssências.SetColLabelValue( 0, u"ID" )
		self.gridEssências.SetColLabelValue( 1, u"Nome" )
		self.gridEssências.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridEssências.EnableDragRowSize( True )
		self.gridEssências.SetRowLabelSize( 80 )
		self.gridEssências.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridEssências.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer17.Add( self.gridEssências, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer14.Add( bSizer17, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer14 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.fecharFrame )
		self.btnAdicionar.Bind( wx.EVT_BUTTON, self.adicionarEssencia )
		self.gridEssências.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.atualizarEssência )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def fecharFrame( self, event ):
		event.Skip()

	def adicionarEssencia( self, event ):
		event.Skip()

	def atualizarEssência( self, event ):
		event.Skip()


###########################################################################
## Class FrameFixacao
###########################################################################

class FrameFixacao ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Fixações", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Descrição:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer11.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.txtNome = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.txtNome, 1, wx.ALL, 5 )

		self.btnAdicionar = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.btnAdicionar, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer11, 0, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.gridFixações = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridFixações.CreateGrid( 0, 2 )
		self.gridFixações.EnableEditing( True )
		self.gridFixações.EnableGridLines( True )
		self.gridFixações.EnableDragGridSize( False )
		self.gridFixações.SetMargins( 0, 0 )

		# Columns
		self.gridFixações.SetColSize( 0, 30 )
		self.gridFixações.SetColSize( 1, 300 )
		self.gridFixações.EnableDragColMove( False )
		self.gridFixações.EnableDragColSize( True )
		self.gridFixações.SetColLabelSize( 30 )
		self.gridFixações.SetColLabelValue( 0, u"ID" )
		self.gridFixações.SetColLabelValue( 1, u"Nome" )
		self.gridFixações.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridFixações.EnableDragRowSize( True )
		self.gridFixações.SetRowLabelSize( 80 )
		self.gridFixações.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridFixações.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer13.Add( self.gridFixações, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer10.Add( bSizer13, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.fecharFrame )
		self.btnAdicionar.Bind( wx.EVT_BUTTON, self.adicionarFixacao )
		self.gridFixações.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.atualizarFixação )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def fecharFrame( self, event ):
		event.Skip()

	def adicionarFixacao( self, event ):
		event.Skip()

	def atualizarFixação( self, event ):
		event.Skip()


###########################################################################
## Class FrameVolumes
###########################################################################

class FrameVolumes ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Volumes", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Descrição:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.txtNome = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.txtNome, 1, wx.ALL, 5 )

		self.btnAdicionar = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnAdicionar, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.gridVolumes = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridVolumes.CreateGrid( 0, 2 )
		self.gridVolumes.EnableEditing( True )
		self.gridVolumes.EnableGridLines( True )
		self.gridVolumes.EnableDragGridSize( False )
		self.gridVolumes.SetMargins( 0, 0 )

		# Columns
		self.gridVolumes.SetColSize( 0, 30 )
		self.gridVolumes.SetColSize( 1, 300 )
		self.gridVolumes.EnableDragColMove( False )
		self.gridVolumes.EnableDragColSize( True )
		self.gridVolumes.SetColLabelSize( 30 )
		self.gridVolumes.SetColLabelValue( 0, u"ID" )
		self.gridVolumes.SetColLabelValue( 1, u"Nome" )
		self.gridVolumes.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridVolumes.EnableDragRowSize( True )
		self.gridVolumes.SetRowLabelSize( 80 )
		self.gridVolumes.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridVolumes.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.gridVolumes.SetToolTip( u"Pressione Enter para atualizar uma Marca" )

		bSizer3.Add( self.gridVolumes, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.fecharFrame )
		self.btnAdicionar.Bind( wx.EVT_BUTTON, self.adicionarVolume )
		self.gridVolumes.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.atualizarVolume )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def fecharFrame( self, event ):
		event.Skip()

	def adicionarVolume( self, event ):
		event.Skip()

	def atualizarVolume( self, event ):
		event.Skip()


###########################################################################
## Class FramePrincipal
###########################################################################

class FramePrincipal ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sistema de Gestão de Perfumes", pos = wx.DefaultPosition, size = wx.Size( 903,561 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.menuMarcas = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Marcas", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menuMarcas )

		self.menuEssencias = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Essências", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menuEssencias )

		self.menuFixacoes = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Fixações", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menuFixacoes )

		self.menuVolume = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Volumes", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menuVolume )

		self.m_menubar1.Append( self.m_menu1, u"Cadastros Básicos" )

		self.m_menu2 = wx.Menu()
		self.menuPerfumes = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Registros", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.menuPerfumes )

		self.menuPerfumeEssencia = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Adicionar Essencias", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.menuPerfumeEssencia )

		self.m_menubar1.Append( self.m_menu2, u"Perfumes" )

		self.m_menu3 = wx.Menu()
		self.menuSobre = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Sobre", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.menuSobre )

		self.menuSair = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Sair", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.menuSair )

		self.m_menubar1.Append( self.m_menu3, u"Ajuda" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.fecharFramePrincipal )
		self.Bind( wx.EVT_MENU, self.abrirMarca, id = self.menuMarcas.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirEssencia, id = self.menuEssencias.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirFixacao, id = self.menuFixacoes.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirVolumes, id = self.menuVolume.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirPerfume, id = self.menuPerfumes.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirEssencia, id = self.menuPerfumeEssencia.GetId() )
		self.Bind( wx.EVT_MENU, self.fecharApp, id = self.menuSair.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def fecharFramePrincipal( self, event ):
		event.Skip()

	def abrirMarca( self, event ):
		event.Skip()

	def abrirEssencia( self, event ):
		event.Skip()

	def abrirFixacao( self, event ):
		event.Skip()

	def abrirVolumes( self, event ):
		event.Skip()

	def abrirPerfume( self, event ):
		event.Skip()


	def fecharApp( self, event ):
		event.Skip()


###########################################################################
## Class FramePerfumes
###########################################################################

class FramePerfumes ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Perfumes", pos = wx.DefaultPosition, size = wx.Size( 1032,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.gridPerfumes = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridPerfumes.CreateGrid( 0, 6 )
		self.gridPerfumes.EnableEditing( True )
		self.gridPerfumes.EnableGridLines( True )
		self.gridPerfumes.EnableDragGridSize( False )
		self.gridPerfumes.SetMargins( 0, 0 )

		# Columns
		self.gridPerfumes.SetColSize( 0, 30 )
		self.gridPerfumes.SetColSize( 1, 200 )
		self.gridPerfumes.SetColSize( 2, 100 )
		self.gridPerfumes.SetColSize( 3, 200 )
		self.gridPerfumes.SetColSize( 4, 200 )
		self.gridPerfumes.SetColSize( 5, 200 )
		self.gridPerfumes.EnableDragColMove( False )
		self.gridPerfumes.EnableDragColSize( True )
		self.gridPerfumes.SetColLabelSize( 30 )
		self.gridPerfumes.SetColLabelValue( 0, u"ID" )
		self.gridPerfumes.SetColLabelValue( 1, u"Nome" )
		self.gridPerfumes.SetColLabelValue( 2, u"Quantidade" )
		self.gridPerfumes.SetColLabelValue( 3, u"Volume" )
		self.gridPerfumes.SetColLabelValue( 4, u"Marca" )
		self.gridPerfumes.SetColLabelValue( 5, u"Fixação" )
		self.gridPerfumes.SetColLabelValue( 6, wx.EmptyString )
		self.gridPerfumes.SetColLabelValue( 7, wx.EmptyString )
		self.gridPerfumes.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridPerfumes.EnableDragRowSize( True )
		self.gridPerfumes.SetRowLabelSize( 80 )
		self.gridPerfumes.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridPerfumes.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer21.Add( self.gridPerfumes, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer20.Add( bSizer21, 1, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnAdicionar = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.btnAdicionar, 1, wx.ALL, 5 )

		self.btnSalvar = wx.Button( self, wx.ID_ANY, u"Salvar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.btnSalvar, 1, wx.ALL, 5 )


		bSizer20.Add( bSizer22, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer20 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.fecharFrame )
		self.Bind( wx.EVT_SHOW, self.exibirFrame )
		self.btnAdicionar.Bind( wx.EVT_BUTTON, self.adicionarLinha )
		self.btnSalvar.Bind( wx.EVT_BUTTON, self.salvarPerfume )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def fecharFrame( self, event ):
		event.Skip()

	def exibirFrame( self, event ):
		event.Skip()

	def adicionarLinha( self, event ):
		event.Skip()

	def salvarPerfume( self, event ):
		event.Skip()


