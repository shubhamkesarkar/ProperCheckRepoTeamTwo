import sublime, sublime_plugin
import os
import sys

current_working_directory = os.getcwd() 																			#current working directory 
sys.path.append("/home/shubham/.config/sublime-text-3/Packages/User" + "/lib/python3.4/site-packages")		#Tells sublime python interpreter where modules are store

from git import *	



settings = sublime.load_settings("ProperCheckRepoTeamTwo.sublime-settings")



savedictionary = {}



#some global variables 																													#imports all from module git, because exceptions file needs to be imported


counter = 1




class myOpener(sublime_plugin.EventListener):		

	def on_post_save(self,view):



		temp_dir = str(view.file_name())

		accepted_extensions = settings.get("extensions")
		#string_accepted_extensions = accepted_extensions[1:]
		#sublime.message_dialog(str(string_accepted_extensions))
		extension_start = temp_dir.rfind('.', 0, len(temp_dir))   				#finds index of last forward slash
		file_extension = temp_dir[extension_start:]
		

		# sublime.message_dialog(str(file_extension in accepted_extensions))
		# sublime.message_dialog(file_extension)
		if(file_extension in accepted_extensions):






			#savedictionary.update({temp_dir:0})

			def repo_check(temp_dir):																									#code checks for .git in the folder	
				try :		
					global repo								
					repo = Repo(temp_dir,search_parent_directories=True)
					#self.view.insert(edit, 0, str(repo))
				except InvalidGitRepositoryError :																			#exception handled when .git is not found
						counter = 0


			repo_check(temp_dir)													#function call to repo_check
			

			global counter
			if counter == 1:
				#global repo
				sublime.message_dialog("on_post_save")
				sublime.message_dialog(str(repo.git.status()))
				#sublime.message_dialog("You have saved the file")


				sublime.message_dialog(str(repo.git.add( '--all' )))
				sublime.message_dialog(str(repo.git.commit( m ='committed all' )))

				#sublime.message_dialog("and now it has been committed")
				sublime.message_dialog(str(repo.git.status()))


				def push_repo():
					forwd_slash_index = temp_dir.rfind('/', 0, len(temp_dir))   				#finds index of last forward slash
					new_dir = temp_dir[0:forwd_slash_index]
					repo = Repo(new_dir)
					o = repo.remotes.origin
					o.pull()	
					o.push()
					#asdadsas
					#sublime.message_dialog(new_dir)
					sublime.message_dialog("repository pushed")


				


				if(temp_dir in savedictionary):
					savedictionary[temp_dir] += 1
					sublime.message_dialog(str(savedictionary[temp_dir]))
					sublime.message_dialog(str(settings.get("x_savespush")))
					if(savedictionary[temp_dir] == settings.get("x_savespush")):
						savedictionary[temp_dir] = 0
						push_repo()
				else:
					 savedictionary[temp_dir] = 1
					

			


		
		#sublime.set_timeout(on_post_save, Y_SECONDS_COMMIT * 1000)