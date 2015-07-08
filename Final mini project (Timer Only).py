import sublime, sublime_plugin
import os
import sys

current_working_directory = os.getcwd() 																			#current working directory 
sys.path.append("/home/shubham/.config/sublime-text-3/Packages/User" + "/lib/python3.4/site-packages")		#Tells sublime python interpreter where modules are store

from git import *	



settings = sublime.load_settings("ProperCheckRepoTeamTwo.sublime-settings")


savedictionary = {}



#some global variables adfs																														#imports all from module git, because exceptions file needs to be imported
global number_saves_before_push

number_saves_before_push = 0

counter = 1



#repo = Repo(settings.get("REPO_PATH"))

# class UserinputCommand(sublime_plugin.TextCommand):
# 	def run(self, edit):
# # 		#temp_dir = "/home/kahlil/TestingGit"
# # 		#join = os.path.join
# # 		#sublime.message_dialog("control is here")
# 		sublime.message_dialog(str(settings.get("x_savespush")))
# # 		self.view.window().show_input_panel("Push after number of commits", "Enter number here", self.on_done, None, None)																										#creates a git.Repo object to represent your repository.
		

# # 	def on_done(self, user_input):
# # 		sublime.message_dialog("Push after "+ X_SAVES_Push + " commits")
# # 		global commit_before_push
# # 		commit_before_push = int(user_input)


# class GitfunctionsCommand(sublime_plugin.TextCommand):
# 	def run(self, edit):
		
# 		#join = os.path.join																											#creates a git.Repo object to represent your repository.
		

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
			global repo
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


			sublime.message_dialog(str(savedictionary))


			if(temp_dir in savedictionary):
				savedictionary[temp_dir] += 1
				sublime.message_dialog(str(savedictionary[temp_dir]))
				sublime.message_dialog(str(settings.get("x_savespush")))
				if(savedictionary[temp_dir] == settings.get("x_savespush")):
					savedictionary[temp_dir] = 0
					push_repo()
			else:
				 savedictionary[temp_dir] = 1


			# global number_saves_before_push
			# number_saves_before_push += 1 
			# sublime.message_dialog(str(number_saves_before_push))
			# sublime.message_dialog(str(settings.get("x_savespush")))
			# if number_saves_before_push == settings.get("x_savespush") :
			# 	number_saves_before_pushfore_push = 0
			# 	push_repo()
			#adfasd
				

		


		
		#sublime.set_timeout(on_post_save, Y_SECONDS_COMMIT * 1000)

w