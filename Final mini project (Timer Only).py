import sublime, sublime_plugin
import os
import sys

current_working_directory = os.getcwd() 																			#current working directory 
sys.path.append("/home/shubham/.config/sublime-text-3/Packages/User" + "/lib/python3.4/site-packages")		#Tells sublime python interpreter where modules are store

from git import *	



settings = sublime.load_settings("ProperCheckRepoTeamTwo.sublime-settings")



savedictionary = {}



#some global variables 																													#imports all from module git, because exceptions file needs to be imported
global number_saves_before_push

number_saves_before_push = 0

counter = 1



class myOpener(sublime_plugin.EventListener):		

	def on_post_save(self,view):



		temp_dir = str(view.file_name())

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
			sublime.message_dialog("File is saved")
			sublime.message_dialog(str(repo.git.status()))
			#sublime.message_dialog("You have saved the file")


			sublime.message_dialog(str(repo.git.add( temp_dir )))
			sublime.message_dialog(str(repo.git.commit( m ='your repository has been comitted' )))

			#sublime.message_dialog("and now it has been committed")
			sublime.message_dialog(str(repo.git.status()))


			def push_repo():
				forwd_slash_index = temp_dir.rfind('/', 0, len(temp_dir))   				#finds index of last forward slash
				new_dir = temp_dir[0:forwd_slash_index]
				repo = Repo(new_dir)
				o = repo.remotes.origin
				o.pull()	
				o.push()
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


			
		


		#def on_load(view)
		#	sublime.set_timeout(on_post_save, (settings.get("Y_SECONDS_COMMIT")) * 8000)