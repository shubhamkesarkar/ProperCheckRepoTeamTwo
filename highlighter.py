import sublime, sublime_plugin

class AddregionCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		for region in self.view.sel():

			# print(region)
			# print(type(region))
			self.view.add_regions('y', [region], 'comment', 'dot', sublime.HIDE_ON_MINIMAP)

class printer(sublime_plugin.EventListener):
	def on_selection_modified(self,view):
		for region in view.sel():
			print(region)

class regionSelect(sublime_plugin.EventListener):
	def on_selection_modified(self,view):

		region1 = view.get_regions("x")
		view.add_regions('x', region1, 'comment', 'dot', sublime.HIDE_ON_MINIMAP)

		region2 = view.get_regions("y")
		view.add_regions('y', region2, 'comment', 'dot', sublime.HIDE_ON_MINIMAP)

		for region in view.sel():
			if region1[0].contains(region) :
					view.add_regions('x', region1, 'string', 'dot', sublime.HIDE_ON_MINIMAP)

			elif region2[0].contains(region) :
					view.add_regions('y', region2, 'string', 'dot', sublime.HIDE_ON_MINIMAP)
			

			
	
