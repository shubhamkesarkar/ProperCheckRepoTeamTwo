
import sublime, sublime_plugin
import os
import sys

current_working_directory = os.getcwd() 																			#current working directory
sys.path.append("/home/rohit/.config/sublime-text-3/Packages/User" + "/lib/python3.4/site-packages")		#Tells sublime python interpreter where modules are store

from git import *



settings = sublime.load_settings("ProperCheckRepoTeamTwo.sublime-settings")



savedictionary = {} #dictionary









class myOpener(sublime_plugin.EventListener):

	def on_post_save(self,view):

		settings = sublime.load_settings("ProperCheckRepoTeamTwo.sublime-settings")

		file_path = str(view.file_name())
		f = open(file_path, 'r')
		# sublime.message_dialog(str(type(f.readline())))




		accepted_extensions = settings.get("extensions")
		extension_start = file_path.rfind('.', 0, len(file_path))   				#finds index of . which is the start of extension
		file_extension = file_path[extension_start:]



		# if(file_extension in accepted_extensions):
		if(f.readline() == "#work\n" or file_extension in accepted_extensions):


			def repo_check(file_path):
				global repo																								#code checks for .git in the folder
				repo = Repo(file_path,search_parent_directories=True)



			repo_check(file_path)													#function call to repo_check



			sublime.message_dialog("File is saved")
			#sublime.message_dialog(str(repo.git.status()))


			#sublime.message_dialog(str(
			repo.git.add( file_path )
			#))
			sublime.message_dialog(str(repo.git.commit( m ='your file has been comitted' )))


			sublime.message_dialog(str(repo.git.status()))


			def push_repo():
				forwd_slash_index = file_path.rfind('/', 0, len(file_path))   				#finds index of last forward slash
				new_dir = file_path[0:forwd_slash_index]
				repo = Repo(new_dir)
				remote_directory = repo.remotes.origin
				remote_directory.pull()
				remote_directory.push()
				sublime.message_dialog("repository pushed")




			#this is to handle multiple files.
			if(file_path in savedictionary):
				savedictionary[file_path] += 1
				sublime.message_dialog("Number of times this file has been saved:\n"+str(savedictionary[file_path]))
				sublime.message_dialog("Number of saves after which file will be pushed:\n"+str(settings.get("x_savespush")))
				if(savedictionary[file_path] == settings.get("x_savespush")):
					savedictionary[file_path] = 0
					push_repo()
			else:
				savedictionary[file_path] = 1
				sublime.message_dialog("Number of times this file has been saved:\n"+str(savedictionary[file_path]))
				sublime.message_dialog("Number of saves after which file will be pushed:\n"+str(settings.get("x_savespush")))



			#Over. Thank you.
