"""Subclass of FramePerfumesGrid, which is generated by wxFormBuilder."""

import wx
import guiperfumes

# Implementing FramePerfumesGrid
class ProjSisPerfumesFramePerfumesGrid( guiperfumes.FramePerfumesGrid ):
	def __init__( self, parent ):
		guiperfumes.FramePerfumesGrid.__init__( self, parent )

	# Handlers for FramePerfumesGrid events.
	def exibirFrame( self, event ):
		# TODO: Implement exibirFrame
		pass

	def adicionarLinha( self, event ):
		# TODO: Implement adicionarLinha
		pass

	def salvarPerfume( self, event ):
		# TODO: Implement salvarPerfume
		pass
	def fecharFrame( self, event ):
		self.Show(False)

